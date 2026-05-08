from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .multiplier import Multiplier
from .offset import Offset
from .reference import Reference


class Mimic(Model):
    def __init__(
        self,
        joint: str = "",
        axis: str = "axis",
        multiplier: "Multiplier" = None,
        offset: "Offset" = None,
        reference: "Reference" = None
    ):
        self.joint = joint
        self.axis = axis
        self.multiplier = multiplier
        self.offset = offset
        self.reference = reference

    def to_sdf(self) -> ET.Element:
        el = ET.Element("mimic")
        if self.joint is not None:
            el.set("joint", self.joint)
        if self.axis is not None:
            el.set("axis", self.axis)
        if self.multiplier is not None:
            el.append(self.multiplier.to_sdf())
        if self.offset is not None:
            el.append(self.offset.to_sdf())
        if self.reference is not None:
            el.append(self.reference.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mimic":
        _joint = el.get("joint", "")
        _axis = el.get("axis", "axis")
        _c_multiplier = el.find("multiplier")
        _multiplier = Multiplier.from_sdf(_c_multiplier) if _c_multiplier is not None else None
        _c_offset = el.find("offset")
        _offset = Offset.from_sdf(_c_offset) if _c_offset is not None else None
        _c_reference = el.find("reference")
        _reference = Reference.from_sdf(_c_reference) if _c_reference is not None else None
        return cls(joint=_joint, axis=_axis, multiplier=_multiplier, offset=_offset, reference=_reference)
