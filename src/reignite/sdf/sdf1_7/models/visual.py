from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_6.models.visual import Visual as _PrevVisual
from .pose import Pose
from .material import Material
from .geometry import Geometry
from .plugin import Plugin
from .cast_shadows import CastShadows
from .laser_retro import LaserRetro
from .transparency import Transparency
from .visibility_flags import VisibilityFlags
from .meta import Meta


class Visual(_PrevVisual):
    def __init__(
        self,
        name: str = "__default__",
        pose: "Pose" = None,
        material: "Material" = None,
        geometry: "Geometry" = None,
        plugin: List["Plugin"] = None,
        cast_shadows: "CastShadows" = None,
        laser_retro: "LaserRetro" = None,
        transparency: "Transparency" = None,
        visibility_flags: "VisibilityFlags" = None,
        meta: "Meta" = None
    ):
        super().__init__(name=name, pose=pose, material=material, geometry=geometry, plugin=plugin, cast_shadows=cast_shadows, laser_retro=laser_retro, transparency=transparency, meta=meta)
        self.visibility_flags = visibility_flags

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.visibility_flags is not None:
            el.append(self.visibility_flags.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visual":
        _base = _PrevVisual.from_sdf(el)
        _c_visibility_flags = el.find("visibility_flags")
        _visibility_flags = VisibilityFlags.from_sdf(_c_visibility_flags) if _c_visibility_flags is not None else None
        return cls(name=_base.name, pose=_base.pose, material=_base.material, geometry=_base.geometry, plugin=_base.plugin, cast_shadows=_base.cast_shadows, laser_retro=_base.laser_retro, transparency=_base.transparency, visibility_flags=_visibility_flags, meta=_base.meta)
