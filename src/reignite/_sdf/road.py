### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.material import Material

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Road(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        material: "Material" = None,
        name: str | None = "__default__",
        points: List[_Vector3T] | None = None,
        width: float | None = 1.0
    ):
        super().__init__(sdf_version)
        self.material = material
        self.name = name if name is not None else "__default__"
        self.points = list(map(_vector3, points)) if points is not None else []
        self.width = width if width is not None else 1.0
        if self.material is not None and hasattr(self.material, 'to_version'):
            if getattr(self.material, 'sdfversion', None) is None:
                self.material.sdfversion = self.sdfversion
            elif getattr(self.material, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.material = self.material.to_version(self.sdfversion)

    def add_point(self, *items: _Vector3T):
        if self.points is None:
            self.points = []
        self.points.extend(items)

    def to_version(self, target_version: str) -> "Road":
        from ..elements.material import Material
        if self.material is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'material' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs: dict = {"sdf_version": target_version, "material": self.material.to_version(target_version) if self.material is not None and hasattr(self.material, "to_version") else self.material, "name": self.name, "points": self.points, "width": self.width}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.material import Material
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("road")
        if self.material is not None:
            _child_res = self.material.to_sdf(version)
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
            _c_tmp.text = str(_v)
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
            _val = _parse_vector3(_text)
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
