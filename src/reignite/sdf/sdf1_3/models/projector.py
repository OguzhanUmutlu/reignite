from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_2.models.projector import Projector as _PrevProjector
from .plugin import Plugin
from .texture import Texture
from .pose import Pose
from .fov import Fov
from .near_clip import NearClip
from .far_clip import FarClip


class Projector(_PrevProjector):
    def __init__(
        self,
        name: str = "__default__",
        plugin: List["Plugin"] = None,
        texture: "Texture" = None,
        pose: "Pose" = None,
        fov: "Fov" = None,
        near_clip: "NearClip" = None,
        far_clip: "FarClip" = None
    ):
        super().__init__(name=name, plugin=plugin, texture=texture, pose=pose, fov=fov, near_clip=near_clip, far_clip=far_clip)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Projector":
        _base = _PrevProjector.from_sdf(el)
        return cls(name=_base.name, plugin=_base.plugin, texture=_base.texture, pose=_base.pose, fov=_base.fov, near_clip=_base.near_clip, far_clip=_base.far_clip)
