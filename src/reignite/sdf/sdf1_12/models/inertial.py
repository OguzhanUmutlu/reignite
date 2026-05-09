from __future__ import annotations

from xml.etree import ElementTree as ET

from .auto_inertia_params import AutoInertiaParams
from .density import Density
from .fluid_added_mass import FluidAddedMass
from .inertia import Inertia
from .mass import Mass
from .pose import Pose
from ...sdf1_11.models.inertial import Inertial as _PrevInertial


class Inertial(_PrevInertial):
    def __init__(
            self,
            auto: bool = False,
            mass: "Mass" = None,
            density: "Density" = None,
            auto_inertia_params: "AutoInertiaParams" = None,
            pose: "Pose" = None,
            inertia: "Inertia" = None,
            fluid_added_mass: "FluidAddedMass" = None
    ):
        super().__init__(auto=auto, mass=mass, density=density, auto_inertia_params=auto_inertia_params, pose=pose,
                         inertia=inertia, fluid_added_mass=fluid_added_mass)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _base = _PrevInertial.from_sdf(el)
        return cls(auto=_base.auto, mass=_base.mass, density=_base.density,
                   auto_inertia_params=_base.auto_inertia_params, pose=_base.pose, inertia=_base.inertia,
                   fluid_added_mass=_base.fluid_added_mass)
