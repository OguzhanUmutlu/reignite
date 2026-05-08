from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.visual import Visual as _PrevVisual
from .geometry import Geometry
from .cast_shadows import CastShadows
from .laser_retro import LaserRetro
from .transparency import Transparency
from .pose import Pose
from .material import Material


class Visual(_PrevVisual):
    def __init__(
        self,
        name: str = "__default__",
        geometry: "Geometry" = None,
        cast_shadows: "CastShadows" = None,
        laser_retro: "LaserRetro" = None,
        transparency: "Transparency" = None,
        pose: "Pose" = None,
        material: "Material" = None
    ):
        super().__init__(name=name, geometry=geometry, cast_shadows=cast_shadows, laser_retro=laser_retro, transparency=transparency, material=material)
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visual":
        _base = _PrevVisual.from_sdf(el)
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_base.name, geometry=_base.geometry, cast_shadows=_base.cast_shadows, laser_retro=_base.laser_retro, transparency=_base.transparency, pose=_pose, material=_base.material)
