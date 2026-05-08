from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.constraints import Constraints as _PrevConstraints
from .cfm import Cfm
from .erp import Erp
from .contact_surface_layer import ContactSurfaceLayer
from .split_impulse import SplitImpulse
from .split_impulse_penetration_threshold import SplitImpulsePenetrationThreshold


class Constraints(_PrevConstraints):
    def __init__(
        self,
        cfm: "Cfm" = None,
        erp: "Erp" = None,
        contact_surface_layer: "ContactSurfaceLayer" = None,
        split_impulse: "SplitImpulse" = None,
        split_impulse_penetration_threshold: "SplitImpulsePenetrationThreshold" = None
    ):
        super().__init__(cfm=cfm, erp=erp, contact_surface_layer=contact_surface_layer)
        self.split_impulse = split_impulse
        self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.split_impulse is not None:
            el.append(self.split_impulse.to_sdf())
        if self.split_impulse_penetration_threshold is not None:
            el.append(self.split_impulse_penetration_threshold.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Constraints":
        _base = _PrevConstraints.from_sdf(el)
        _c_split_impulse = el.find("split_impulse")
        _split_impulse = SplitImpulse.from_sdf(_c_split_impulse) if _c_split_impulse is not None else None
        _c_split_impulse_penetration_threshold = el.find("split_impulse_penetration_threshold")
        _split_impulse_penetration_threshold = SplitImpulsePenetrationThreshold.from_sdf(_c_split_impulse_penetration_threshold) if _c_split_impulse_penetration_threshold is not None else None
        return cls(cfm=_base.cfm, erp=_base.erp, contact_surface_layer=_base.contact_surface_layer, split_impulse=_split_impulse, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)
