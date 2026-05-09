from __future__ import annotations

from xml.etree import ElementTree as ET

from .auto_inertia_params import AutoInertiaParams
from .density import Density
from .fluid_added_mass import FluidAddedMass
from .inertia import Inertia
from .mass import Mass
from .pose import Pose
from ...sdf1_10.models.inertial import Inertial as _PrevInertial


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
        super().__init__(mass=mass, pose=pose, inertia=inertia, fluid_added_mass=fluid_added_mass)
        self.auto = auto
        self.density = density
        self.auto_inertia_params = auto_inertia_params

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.auto is not None:
            el.set("auto", str(self.auto).lower())
        if self.density is not None:
            el.append(self.density.to_sdf())
        if self.auto_inertia_params is not None:
            el.append(self.auto_inertia_params.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _base = _PrevInertial.from_sdf(el)
        _auto = el.get("auto", False).strip().lower() == 'true'
        _c_density = el.find("density")
        _density = Density.from_sdf(_c_density) if _c_density is not None else None
        _c_auto_inertia_params = el.find("auto_inertia_params")
        _auto_inertia_params = AutoInertiaParams.from_sdf(
            _c_auto_inertia_params) if _c_auto_inertia_params is not None else None
        return cls(auto=_auto, mass=_base.mass, density=_density, auto_inertia_params=_auto_inertia_params,
                   pose=_base.pose, inertia=_base.inertia, fluid_added_mass=_base.fluid_added_mass)
