from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .cast_shadows import CastShadows
from .frame import Frame
from .geometry import Geometry
from .laser_retro import LaserRetro
from .material import Material
from .meta import Meta
from .plugin import Plugin
from .pose import Pose
from .transparency import Transparency
from ...sdf1_5.models.visual import Visual as _PrevVisual


class Visual(_PrevVisual):
    def __init__(
            self,
            name: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            material: "Material" = None,
            geometry: "Geometry" = None,
            plugin: List["Plugin"] = None,
            cast_shadows: "CastShadows" = None,
            laser_retro: "LaserRetro" = None,
            transparency: "Transparency" = None,
            meta: "Meta" = None
    ):
        super().__init__(name=name, frame=frame, pose=pose, material=material, geometry=geometry, plugin=plugin,
                         cast_shadows=cast_shadows, laser_retro=laser_retro, transparency=transparency, meta=meta)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visual":
        _base = _PrevVisual.from_sdf(el)
        return cls(name=_base.name, frame=_base.frame, pose=_base.pose, material=_base.material,
                   geometry=_base.geometry, plugin=_base.plugin, cast_shadows=_base.cast_shadows,
                   laser_retro=_base.laser_retro, transparency=_base.transparency, meta=_base.meta)
