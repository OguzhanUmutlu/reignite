from __future__ import annotations

from xml.etree import ElementTree as ET

from .fluid_added_mass import FluidAddedMass
from .inertia import Inertia
from .mass import Mass
from .pose import Pose
from ...sdf1_9.models.inertial import Inertial as _PrevInertial


class Inertial(_PrevInertial):
    def __init__(
            self,
            mass: "Mass" = None,
            pose: "Pose" = None,
            inertia: "Inertia" = None,
            fluid_added_mass: "FluidAddedMass" = None
    ):
        super().__init__(mass=mass, pose=pose, inertia=inertia)
        self.fluid_added_mass = fluid_added_mass

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.fluid_added_mass is not None:
            el.append(self.fluid_added_mass.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _base = _PrevInertial.from_sdf(el)
        _c_fluid_added_mass = el.find("fluid_added_mass")
        _fluid_added_mass = FluidAddedMass.from_sdf(_c_fluid_added_mass) if _c_fluid_added_mass is not None else None
        return cls(mass=_base.mass, pose=_base.pose, inertia=_base.inertia, fluid_added_mass=_fluid_added_mass)
