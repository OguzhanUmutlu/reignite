from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.ode import Ode as _PrevOde
from .coefficient import Coefficient
from .use_patch_radius import UsePatchRadius
from .patch_radius import PatchRadius
from .surface_radius import SurfaceRadius


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


class Torsional(Model):
    def __init__(
        self,
        coefficient: "Coefficient" = None,
        use_patch_radius: "UsePatchRadius" = None,
        patch_radius: "PatchRadius" = None,
        surface_radius: "SurfaceRadius" = None,
        ode: "Ode" = None
    ):
        self.coefficient = coefficient
        self.use_patch_radius = use_patch_radius
        self.patch_radius = patch_radius
        self.surface_radius = surface_radius
        self.ode = ode

    def to_sdf(self) -> ET.Element:
        el = ET.Element("torsional")
        if self.coefficient is not None:
            el.append(self.coefficient.to_sdf())
        if self.use_patch_radius is not None:
            el.append(self.use_patch_radius.to_sdf())
        if self.patch_radius is not None:
            el.append(self.patch_radius.to_sdf())
        if self.surface_radius is not None:
            el.append(self.surface_radius.to_sdf())
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Torsional":
        _c_coefficient = el.find("coefficient")
        _coefficient = Coefficient.from_sdf(_c_coefficient) if _c_coefficient is not None else None
        _c_use_patch_radius = el.find("use_patch_radius")
        _use_patch_radius = UsePatchRadius.from_sdf(_c_use_patch_radius) if _c_use_patch_radius is not None else None
        _c_patch_radius = el.find("patch_radius")
        _patch_radius = PatchRadius.from_sdf(_c_patch_radius) if _c_patch_radius is not None else None
        _c_surface_radius = el.find("surface_radius")
        _surface_radius = SurfaceRadius.from_sdf(_c_surface_radius) if _c_surface_radius is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(coefficient=_coefficient, use_patch_radius=_use_patch_radius, patch_radius=_patch_radius, surface_radius=_surface_radius, ode=_ode)
