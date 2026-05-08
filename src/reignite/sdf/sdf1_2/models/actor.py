from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_0.models.actor import Actor as _PrevActor
from .link import Link
from .joint import Joint
from .plugin import Plugin
from .pose import Pose
from .skin import Skin
from .animation import Animation
from .script import Script


class Actor(_PrevActor):
    def __init__(
        self,
        name: str = "__default__",
        static: bool = False,
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        pose: "Pose" = None,
        skin: "Skin" = None,
        animation: List["Animation"] = None,
        script: "Script" = None
    ):
        super().__init__(name=name, static=static, link=link, joint=joint, plugin=plugin, skin=skin, animation=animation, script=script)
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Actor":
        _base = _PrevActor.from_sdf(el)
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_base.name, static=_base.static, link=_base.link, joint=_base.joint, plugin=_base.plugin, pose=_pose, skin=_base.skin, animation=_base.animation, script=_base.script)
