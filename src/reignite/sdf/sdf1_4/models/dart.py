from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .bone_attachment import BoneAttachment
from .damping import Damping
from .flesh_mass_fraction import FleshMassFraction


import math
import sys

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
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v



class Stiffness(Model):
    def __init__(self, stiffness: float = 100.0):
        self.stiffness = stiffness

    def to_sdf(self) -> ET.Element:
        el = ET.Element("stiffness")
        if self.stiffness is not None:
            el.text = str(self.stiffness)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Stiffness":
        _text = el.text or 100.0
        _stiffness = _parse_double(_text)
        return cls(stiffness=_stiffness)


class Dart(Model):
    def __init__(
        self,
        bone_attachment: "BoneAttachment" = None,
        stiffness: "Stiffness" = None,
        damping: "Damping" = None,
        flesh_mass_fraction: "FleshMassFraction" = None
    ):
        self.bone_attachment = bone_attachment
        self.stiffness = stiffness
        self.damping = damping
        self.flesh_mass_fraction = flesh_mass_fraction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dart")
        if self.bone_attachment is not None:
            el.append(self.bone_attachment.to_sdf())
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf())
        if self.damping is not None:
            el.append(self.damping.to_sdf())
        if self.flesh_mass_fraction is not None:
            el.append(self.flesh_mass_fraction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dart":
        _c_bone_attachment = el.find("bone_attachment")
        _bone_attachment = BoneAttachment.from_sdf(_c_bone_attachment) if _c_bone_attachment is not None else None
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness) if _c_stiffness is not None else None
        _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping) if _c_damping is not None else None
        _c_flesh_mass_fraction = el.find("flesh_mass_fraction")
        _flesh_mass_fraction = FleshMassFraction.from_sdf(_c_flesh_mass_fraction) if _c_flesh_mass_fraction is not None else None
        return cls(bone_attachment=_bone_attachment, stiffness=_stiffness, damping=_damping, flesh_mass_fraction=_flesh_mass_fraction)
