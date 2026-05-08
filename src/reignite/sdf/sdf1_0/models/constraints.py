from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


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



class Constraints(Model):
    def __init__(
        self,
        cfm: float = 0,
        erp: float = 0.2,
        contact_max_correcting_vel: float = 100.0,
        contact_surface_layer: float = 0.001
    ):
        self.cfm = cfm
        self.erp = erp
        self.contact_max_correcting_vel = contact_max_correcting_vel
        self.contact_surface_layer = contact_surface_layer

    def to_sdf(self) -> ET.Element:
        el = ET.Element("constraints")
        if self.cfm is not None:
            el.set("cfm", str(self.cfm))
        if self.erp is not None:
            el.set("erp", str(self.erp))
        if self.contact_max_correcting_vel is not None:
            el.set("contact_max_correcting_vel", str(self.contact_max_correcting_vel))
        if self.contact_surface_layer is not None:
            el.set("contact_surface_layer", str(self.contact_surface_layer))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Constraints":
        _cfm = _parse_double(el.get("cfm", 0))
        _erp = _parse_double(el.get("erp", 0.2))
        _contact_max_correcting_vel = _parse_double(el.get("contact_max_correcting_vel", 100.0))
        _contact_surface_layer = _parse_double(el.get("contact_surface_layer", 0.001))
        return cls(cfm=_cfm, erp=_erp, contact_max_correcting_vel=_contact_max_correcting_vel, contact_surface_layer=_contact_surface_layer)
