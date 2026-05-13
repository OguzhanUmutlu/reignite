### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.material import Material


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class Road(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        material: "Material" = None,
        name: str = "__default__",
        points: List[_SDFVector3] = None,
        width: float = 1.0
    ):
        super().__init__(sdf_version)
        if points is None:
            points = _SDFVector3.from_sdf("0 0 0", version=sdf_version)
        self.material = material
        self.name = name
        self.points = points or []
        self.width = width
        if self.material is not None and hasattr(self.material, 'to_version'):
            if getattr(self.material, '__version__', None) is None:
                self.material.__version__ = self.__version__
            elif getattr(self.material, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.material = self.material.to_version(self.__version__)

    def add_point(self, *items: _SDFVector3):
        if self.points is None:
            self.points = []
        self.points.extend(items)

    def to_version(self, target_version: str) -> "Road":
        from ..elements.material import Material
        if self.material is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'material' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["material"] = self.material.to_version(target_version) if hasattr(self.material, "to_version") else self.material
        kwargs["name"] = self.name
        kwargs["points"] = self.points
        kwargs["width"] = self.width
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.material import Material
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("road")
        if self.material is not None:
            if hasattr(self.material, 'to_sdf'):
                _child_res = self.material.to_sdf(version)
            else:
                _child_res = str(self.material)
            if isinstance(_child_res, str):
                _item_el = ET.Element('material')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        for _v in (self.points or []):
            _c_tmp = ET.Element("point")
            _c_tmp.text = _v.to_sdf(version)
            el.append(_c_tmp)
        if self.width is not None:
            _c_tmp = ET.Element("width")
            _c_tmp.text = str(self.width)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Road | SDFError":
        from ..elements.material import Material
        _c_material = el.find("material")
        if _c_material is not None:
            _res = Material._from_sdf(_c_material, version)
            if isinstance(_res, SDFError):
                return _res.extend("material")
            _material = _res
        else:
            _material = None
        if _material is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'material' is not supported in SDF version {version} (added in 1.5)")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _points = []
        for c in el.findall("point"):
            _text = c.text if c.text is not None else "0 0 0"
            _val = _SDFVector3._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("point")
            _points.append(_val)
        _c_tmp = el.find("width")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("width")
            _width = _val
        else:
            _width = None
        return cls(sdf_version=version, material=_material, name=_name, points=_points, width=_width)
