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
        multiplier: "Multiplier" = None,
        offset: "Offset" = None,
        reference: "Reference" = None
    ):
        self.__version__ = sdf_version
        self.axis = axis
        self.joint = joint
        self.multiplier = multiplier
        self.offset = offset
        self.reference = reference
        if self.multiplier is not None:
            if getattr(self.multiplier, '__version__', None) is None:
                self.multiplier.__version__ = self.__version__
            elif getattr(self.multiplier, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.multiplier = self.multiplier.to_version(self.__version__)
        if self.offset is not None:
            if getattr(self.offset, '__version__', None) is None:
                self.offset.__version__ = self.__version__
            elif getattr(self.offset, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.offset = self.offset.to_version(self.__version__)
        if self.reference is not None:
            if getattr(self.reference, '__version__', None) is None:
                self.reference.__version__ = self.__version__
            elif getattr(self.reference, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.reference = self.reference.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Mimic":
        kwargs = {"sdf_version": target_version}
        kwargs["axis"] = self.axis
        kwargs["joint"] = self.joint
        kwargs["multiplier"] = self.multiplier.to_version(target_version) if self.multiplier is not None else None
        kwargs["offset"] = self.offset.to_version(target_version) if self.offset is not None else None
        kwargs["reference"] = self.reference.to_version(target_version) if self.reference is not None else None
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
            el.append(self.multiplier.to_sdf(version))
        if self.offset is not None:
            el.append(self.offset.to_sdf(version))
        if self.reference is not None:
            el.append(self.reference.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _axis = el.get("axis", "axis")
        if isinstance(_axis, SDFError):
            return _axis.extend("@axis")
        if el.get("joint") is None:
            return SDFError(f"'joint' is required in SDF version {version}")
        _joint = el.get("joint", "")
        if isinstance(_joint, SDFError):
            return _joint.extend("@joint")
        _c_multiplier = el.find("multiplier")
        if _c_multiplier is not None:
            _res = Multiplier._from_sdf(_c_multiplier, version)
            if isinstance(_res, SDFError):
                return _res.extend("multiplier")
            _multiplier = _res
        else:
            _multiplier = None
        _c_offset = el.find("offset")
        if _c_offset is not None:
            _res = Offset._from_sdf(_c_offset, version)
            if isinstance(_res, SDFError):
                return _res.extend("offset")
            _offset = _res
        else:
            _offset = None
        _c_reference = el.find("reference")
        if _c_reference is not None:
            _res = Reference._from_sdf(_c_reference, version)
            if isinstance(_res, SDFError):
                return _res.extend("reference")
            _reference = _res
        else:
            _reference = None
        return cls(sdf_version=version, axis=_axis, joint=_joint, multiplier=_multiplier, offset=_offset, reference=_reference)


class Multiplier(BaseModel):
    def __init__(self, sdf_version: str | None = None, multiplier: float = 1.0):
        self.__version__ = sdf_version
        self.multiplier = multiplier

    def to_version(self, target_version: str) -> "Multiplier":
        kwargs = {"sdf_version": target_version}
        kwargs["multiplier"] = self.multiplier
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("multiplier")
        if self.multiplier is not None:
            el.text = str(self.multiplier)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _multiplier = _parse_double(_text)
        if isinstance(_multiplier, SDFError):
            return _multiplier
        return cls(sdf_version=version, multiplier=_multiplier)


class Offset(BaseModel):
    def __init__(self, sdf_version: str | None = None, offset: float = 0):
        self.__version__ = sdf_version
        self.offset = offset

    def to_version(self, target_version: str) -> "Offset":
        kwargs = {"sdf_version": target_version}
        kwargs["offset"] = self.offset
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("offset")
        if self.offset is not None:
            el.text = str(self.offset)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _offset = _parse_double(_text)
        if isinstance(_offset, SDFError):
            return _offset
        return cls(sdf_version=version, offset=_offset)


class Reference(BaseModel):
    def __init__(self, sdf_version: str | None = None, reference: float = 0):
        self.__version__ = sdf_version
        self.reference = reference

    def to_version(self, target_version: str) -> "Reference":
        kwargs = {"sdf_version": target_version}
        kwargs["reference"] = self.reference
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("reference")
        if self.reference is not None:
            el.text = str(self.reference)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _reference = _parse_double(_text)
        if isinstance(_reference, SDFError):
            return _reference
        return cls(sdf_version=version, reference=_reference)
