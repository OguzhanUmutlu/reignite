### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


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



class Sonar(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        geometry: str = "cone",
        max: float = 1.0,
        min: float = 0,
        radius: float = 0.5
    ):
        super().__init__(sdf_version)
        self.geometry = geometry
        self.max = max
        self.min = min
        self.radius = radius

    def to_version(self, target_version: str) -> "Sonar":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["geometry"] = self.geometry
        kwargs["max"] = self.max
        kwargs["min"] = self.min
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("sonar")
        if self.geometry is not None:
            _c_tmp = ET.Element("geometry")
            _c_tmp.text = self.geometry
            el.append(_c_tmp)
        if self.max is not None:
            _c_tmp = ET.Element("max")
            _c_tmp.text = str(self.max)
            el.append(_c_tmp)
        if self.min is not None:
            _c_tmp = ET.Element("min")
            _c_tmp.text = str(self.min)
            el.append(_c_tmp)
        if self.radius is not None:
            _c_tmp = ET.Element("radius")
            _c_tmp.text = str(self.radius)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Sonar | SDFError":
        _c_tmp = el.find("geometry")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "cone"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("geometry")
            _geometry = _val
        else:
            _geometry = None
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("max")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("max")
            _max = _val
        else:
            _max = None
        _c_tmp = el.find("min")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("min")
            _min = _val
        else:
            _min = None
        _c_tmp = el.find("radius")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.5
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("radius")
            _radius = _val
        else:
            _radius = None
        return cls(sdf_version=version, geometry=_geometry, max=_max, min=_min, radius=_radius)
