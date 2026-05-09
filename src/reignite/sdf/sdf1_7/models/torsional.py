from __future__ import annotations

from xml.etree import ElementTree as ET

from .coefficient import Coefficient
from .patch_radius import PatchRadius
from .surface_radius import SurfaceRadius
from .use_patch_radius import UsePatchRadius
from ...sdf1_6.models.ode import Ode as _PrevOde
from ...sdf1_6.models.torsional import Torsional as _PrevTorsional


class Ode(_PrevOde):
    def __init__(self, slip: "Slip" = None):
        super().__init__()
        self.slip = slip

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.slip is not None:
            el.append(self.slip.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_slip = el.find("slip")
        _slip = Slip.from_sdf(_c_slip) if _c_slip is not None else None
        return cls(slip=_slip)


class Torsional(_PrevTorsional):
    def __init__(
            self,
            coefficient: "Coefficient" = None,
            use_patch_radius: "UsePatchRadius" = None,
            patch_radius: "PatchRadius" = None,
            surface_radius: "SurfaceRadius" = None,
            ode: "Ode" = None
    ):
        super().__init__(coefficient=coefficient, use_patch_radius=use_patch_radius, patch_radius=patch_radius,
                         surface_radius=surface_radius, ode=ode)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Torsional":
        _base = _PrevTorsional.from_sdf(el)
        return cls(coefficient=_base.coefficient, use_patch_radius=_base.use_patch_radius,
                   patch_radius=_base.patch_radius, surface_radius=_base.surface_radius, ode=_base.ode)
