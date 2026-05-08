from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_9.models.texture import Texture as _PrevTexture
from ...sdf1_9.models.projector import Projector as _PrevProjector
from .pose import Pose
from .plugin import Plugin
from .fov import Fov
from .near_clip import NearClip
from .far_clip import FarClip
from .visibility_flags import VisibilityFlags


class Texture(_PrevTexture):
    def __init__(self, size: "Size" = None, diffuse: "Diffuse" = None, normal: "Normal" = None):
        super().__init__()
        self.size = size
        self.diffuse = diffuse
        self.normal = normal

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.size is not None:
            el.append(self.size.to_sdf())
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf())
        if self.normal is not None:
            el.append(self.normal.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Texture":
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size) if _c_size is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse) if _c_diffuse is not None else None
        _c_normal = el.find("normal")
        _normal = Normal.from_sdf(_c_normal) if _c_normal is not None else None
        return cls(size=_size, diffuse=_diffuse, normal=_normal)


class Projector(_PrevProjector):
    def __init__(
        self,
        name: str = "__default__",
        pose: "Pose" = None,
        plugin: List["Plugin"] = None,
        texture: "Texture" = None,
        fov: "Fov" = None,
        near_clip: "NearClip" = None,
        far_clip: "FarClip" = None,
        visibility_flags: "VisibilityFlags" = None
    ):
        super().__init__(name=name, pose=pose, plugin=plugin, texture=texture, fov=fov, near_clip=near_clip, far_clip=far_clip, visibility_flags=visibility_flags)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Projector":
        _base = _PrevProjector.from_sdf(el)
        return cls(name=_base.name, pose=_base.pose, plugin=_base.plugin, texture=_base.texture, fov=_base.fov, near_clip=_base.near_clip, far_clip=_base.far_clip, visibility_flags=_base.visibility_flags)
