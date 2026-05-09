from __future__ import annotations

from xml.etree import ElementTree as ET

from .cfm import Cfm
from .contact_max_correcting_vel import ContactMaxCorrectingVel
from .contact_surface_layer import ContactSurfaceLayer
from .erp import Erp
from ...sdf1_0.models.constraints import Constraints as _PrevConstraints


class Constraints(_PrevConstraints):
    def __init__(
            self,
            cfm: "Cfm" = None,
            erp: "Erp" = None,
            contact_max_correcting_vel: "ContactMaxCorrectingVel" = None,
            contact_surface_layer: "ContactSurfaceLayer" = None
    ):
        super().__init__(cfm=cfm, erp=erp, contact_max_correcting_vel=contact_max_correcting_vel,
                         contact_surface_layer=contact_surface_layer)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Constraints":
        _base = _PrevConstraints.from_sdf(el)
        return cls(cfm=_base.cfm, erp=_base.erp, contact_max_correcting_vel=_base.contact_max_correcting_vel,
                   contact_surface_layer=_base.contact_surface_layer)
