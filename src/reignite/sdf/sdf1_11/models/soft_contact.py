from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.stiffness import Stiffness as _PrevStiffness
from ...sdf1_10.models.dart import Dart as _PrevDart
from ...sdf1_10.models.soft_contact import SoftContact as _PrevSoftContact


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



class Stiffness(_PrevStiffness):
    def __init__(self, stiffness: float = 100.0):
        super().__init__(stiffness=stiffness)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Stiffness":
        _base = _PrevStiffness.from_sdf(el)
        return cls(stiffness=_base.stiffness)


class Dart(_PrevDart):
    def __init__(
        self,
        bone_attachment: "BoneAttachment" = None,
        stiffness: "Stiffness" = None,
        damping: "Damping" = None,
        flesh_mass_fraction: "FleshMassFraction" = None
    ):
        super().__init__(bone_attachment=bone_attachment, stiffness=stiffness, damping=damping, flesh_mass_fraction=flesh_mass_fraction)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dart":
        _base = _PrevDart.from_sdf(el)
        return cls(bone_attachment=_base.bone_attachment, stiffness=_base.stiffness, damping=_base.damping, flesh_mass_fraction=_base.flesh_mass_fraction)


class SoftContact(_PrevSoftContact):
    def __init__(self, dart: "Dart" = None):
        super().__init__(dart=dart)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SoftContact":
        _base = _PrevSoftContact.from_sdf(el)
        return cls(dart=_base.dart)
