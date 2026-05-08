from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from .plugin import Plugin
from .texture import Texture
from .pose import Pose
from .fov import Fov
from .near_clip import NearClip
from .far_clip import FarClip


class Projector(Model):
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
        self.name = name
        self.plugin = plugin or []
        self.texture = texture
        self.pose = pose
        self.fov = fov
        self.near_clip = near_clip
        self.far_clip = far_clip

    def to_sdf(self) -> ET.Element:
        el = ET.Element("projector")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.texture is not None:
            el.append(self.texture.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.fov is not None:
            el.append(self.fov.to_sdf())
        if self.near_clip is not None:
            el.append(self.near_clip.to_sdf())
        if self.far_clip is not None:
            el.append(self.far_clip.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Projector":
        _name = el.get("name", "__default__")
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_texture = el.find("texture")
        _texture = Texture.from_sdf(_c_texture) if _c_texture is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_fov = el.find("fov")
        _fov = Fov.from_sdf(_c_fov) if _c_fov is not None else None
        _c_near_clip = el.find("near_clip")
        _near_clip = NearClip.from_sdf(_c_near_clip) if _c_near_clip is not None else None
        _c_far_clip = el.find("far_clip")
        _far_clip = FarClip.from_sdf(_c_far_clip) if _c_far_clip is not None else None
        return cls(name=_name, plugin=_plugin, texture=_texture, pose=_pose, fov=_fov, near_clip=_near_clip, far_clip=_far_clip)
