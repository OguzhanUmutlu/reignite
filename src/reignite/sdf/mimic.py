from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model


import math

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > math.inf:
        raise ValueError(f"double out of range: {raw}")
    return v



class Multiplier(Model):
    def __init__(self, sdf_version: str, multiplier: float = 1.0):
        self.__version__ = sdf_version
        self.multiplier = multiplier

    def to_version(self, target_version: str) -> "Multiplier":
        kwargs = {"sdf_version": target_version}
        kwargs["multiplier"] = self.multiplier
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("multiplier")
        if self.multiplier is not None:
            el.text = str(self.multiplier)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Multiplier":
        _text = el.text or 1.0
        _multiplier = _parse_double(_text)
        return cls(sdf_version=version, multiplier=_multiplier)


class Offset(Model):
    def __init__(self, sdf_version: str, offset: float = 0):
        self.__version__ = sdf_version
        self.offset = offset

    def to_version(self, target_version: str) -> "Offset":
        kwargs = {"sdf_version": target_version}
        kwargs["offset"] = self.offset
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("offset")
        if self.offset is not None:
            el.text = str(self.offset)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Offset":
        _text = el.text or 0
        _offset = _parse_double(_text)
        return cls(sdf_version=version, offset=_offset)


class Reference(Model):
    def __init__(self, sdf_version: str, reference: float = 0):
        self.__version__ = sdf_version
        self.reference = reference

    def to_version(self, target_version: str) -> "Reference":
        kwargs = {"sdf_version": target_version}
        kwargs["reference"] = self.reference
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("reference")
        if self.reference is not None:
            el.text = str(self.reference)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Reference":
        _text = el.text or 0
        _reference = _parse_double(_text)
        return cls(sdf_version=version, reference=_reference)


class Mimic(Model):
    def __init__(
        self,
        sdf_version: str,
        joint: str = "",
        axis: str = "axis",
        multiplier: "Multiplier" = None,
        offset: "Offset" = None,
        reference: "Reference" = None
    ):
        self.__version__ = sdf_version
        self.joint = joint
        self.axis = axis
        self.multiplier = multiplier
        self.offset = offset
        self.reference = reference

    def to_version(self, target_version: str) -> "Mimic":
        kwargs = {"sdf_version": target_version}
        kwargs["joint"] = self.joint
        kwargs["axis"] = self.axis
        kwargs["multiplier"] = self.multiplier.to_version(target_version) if self.multiplier is not None else None
        kwargs["offset"] = self.offset.to_version(target_version) if self.offset is not None else None
        kwargs["reference"] = self.reference.to_version(target_version) if self.reference is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mimic")
        if self.joint is not None:
            el.set("joint", self.joint)
        if self.axis is not None:
            el.set("axis", self.axis)
        if self.multiplier is not None:
            el.append(self.multiplier.to_sdf(version))
        if self.offset is not None:
            el.append(self.offset.to_sdf(version))
        if self.reference is not None:
            el.append(self.reference.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mimic":
        _joint = el.get("joint", "")
        _axis = el.get("axis", "axis")
        _c_multiplier = el.find("multiplier")
        _multiplier = Multiplier.from_sdf(_c_multiplier, version) if _c_multiplier is not None else None
        _c_offset = el.find("offset")
        _offset = Offset.from_sdf(_c_offset, version) if _c_offset is not None else None
        _c_reference = el.find("reference")
        _reference = Reference.from_sdf(_c_reference, version) if _c_reference is not None else None
        return cls(sdf_version=version, joint=_joint, axis=_axis, multiplier=_multiplier, offset=_offset, reference=_reference)
