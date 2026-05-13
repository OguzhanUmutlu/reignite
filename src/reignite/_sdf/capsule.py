### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


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



class Capsule(BaseModel):
    def __init__(self, sdf_version: str | None = None, length: float = 1, radius: float = 0.5):
        super().__init__(sdf_version)
        self.length = length
        self.radius = radius

    def to_version(self, target_version: str) -> "Capsule":
        kwargs = {"sdf_version": target_version}
        kwargs["length"] = self.length
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("capsule")
        if self.length is not None:
            _c_tmp = ET.Element("length")
            _c_tmp.text = str(self.length)
            el.append(_c_tmp)
        if self.radius is not None:
            _c_tmp = ET.Element("radius")
            _c_tmp.text = str(self.radius)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Capsule | SDFError":
        _c_tmp = el.find("length")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("length")
            _length = _val
        else:
            _length = None
        _c_tmp = el.find("radius")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.5
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("radius")
            _radius = _val
        else:
            _radius = None
        return cls(sdf_version=version, length=_length, radius=_radius)
