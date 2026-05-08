from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_8.models.pose import Pose as _PrevPose
from ...sdf1_8.models.actor import Actor as _PrevActor
from ....utils.pose import Pose
from .link import Link
from .joint import Joint
from .plugin import Plugin
from .skin import Skin
from .animation import Animation
from .script import Script


class Pose(_PrevPose):
    def __init__(
        self,
        pose: Pose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose, relative_to=relative_to)
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        _rotation_format = el.get("rotation_format", "euler_rpy")
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(pose=_base.pose, relative_to=_base.relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Actor(_PrevActor):
    def __init__(
        self,
        name: str = "__default__",
        pose: "Pose" = None,
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        skin: "Skin" = None,
        animation: List["Animation"] = None,
        script: "Script" = None
    ):
        super().__init__(name=name, pose=pose, link=link, joint=joint, plugin=plugin, skin=skin, animation=animation, script=script)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Actor":
        _base = _PrevActor.from_sdf(el)
        return cls(name=_base.name, pose=_base.pose, link=_base.link, joint=_base.joint, plugin=_base.plugin, skin=_base.skin, animation=_base.animation, script=_base.script)
