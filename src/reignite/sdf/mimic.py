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



class Mimic(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        axis: str = "axis",
        joint: str = "",
        multiplier: float = 1.0,
        offset: float = 0,
        reference: float = 0
    ):
        super().__init__(sdf_version)
        self.axis = axis
        self.joint = joint
        self.multiplier = multiplier
        self.offset = offset
        self.reference = reference

    def to_version(self, target_version: str) -> "Mimic":
        kwargs = {"sdf_version": target_version}
        kwargs["axis"] = self.axis
        kwargs["joint"] = self.joint
        kwargs["multiplier"] = self.multiplier
        kwargs["offset"] = self.offset
        kwargs["reference"] = self.reference
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("mimic")
        if self.axis is not None:
            el.set("axis", self.axis)
        if self.joint is None:
            raise ValueError(f"'joint' is required in SDF version {version}")
        if self.joint is not None:
            el.set("joint", self.joint)
        if self.multiplier is not None:
            _c_tmp = ET.Element("multiplier")
            _c_tmp.text = str(self.multiplier)
            el.append(_c_tmp)
        if self.offset is not None:
            _c_tmp = ET.Element("offset")
            _c_tmp.text = str(self.offset)
            el.append(_c_tmp)
        if self.reference is not None:
            _c_tmp = ET.Element("reference")
            _c_tmp.text = str(self.reference)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Mimic | SDFError":
        _axis = el.get("axis", "axis")
        if isinstance(_axis, SDFError):
            return _axis.extend("@axis")
        if el.get("joint") is None:
            return SDFError(f"'joint' is required in SDF version {version}")
        _joint = el.get("joint", "")
        if isinstance(_joint, SDFError):
            return _joint.extend("@joint")
        _c_tmp = el.find("multiplier")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("multiplier")
            _multiplier = _val
        else:
            _multiplier = None
        _c_tmp = el.find("offset")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("offset")
            _offset = _val
        else:
            _offset = None
        _c_tmp = el.find("reference")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("reference")
            _reference = _val
        else:
            _reference = None
        return cls(sdf_version=version, axis=_axis, joint=_joint, multiplier=_multiplier, offset=_offset, reference=_reference)
