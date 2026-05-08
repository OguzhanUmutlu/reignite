from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_4.models.visual import Visual as _PrevVisual
from .frame import Frame
from .pose import Pose
from .material import Material
from .geometry import Geometry
from .plugin import Plugin
from .cast_shadows import CastShadows
from .laser_retro import LaserRetro
from .transparency import Transparency
from .meta import Meta


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
        super().__init__(name=name, pose=pose, material=material, geometry=geometry, plugin=plugin, cast_shadows=cast_shadows, laser_retro=laser_retro, transparency=transparency)
        self.frame = frame or []
        self.meta = meta

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.meta is not None:
            el.append(self.meta.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visual":
        _base = _PrevVisual.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_meta = el.find("meta")
        _meta = Meta.from_sdf(_c_meta) if _c_meta is not None else None
        return cls(name=_base.name, frame=_frame, pose=_base.pose, material=_base.material, geometry=_base.geometry, plugin=_base.plugin, cast_shadows=_base.cast_shadows, laser_retro=_base.laser_retro, transparency=_base.transparency, meta=_meta)
