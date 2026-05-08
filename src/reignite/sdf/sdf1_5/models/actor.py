from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_4.models.static import Static as _PrevStatic
from ...sdf1_4.models.actor import Actor as _PrevActor
from .frame import Frame
from .pose import Pose
from .link import Link
from .joint import Joint
from .plugin import Plugin
from .skin import Skin
from .animation import Animation
from .script import Script


class Static(_PrevStatic):
    def __init__(self, static: bool = False):
        super().__init__(static=static)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Static":
        _base = _PrevStatic.from_sdf(el)
        return cls(static=_base.static)


class Actor(_PrevActor):
    def __init__(
        self,
        name: str = "__default__",
        frame: List["Frame"] = None,
        pose: "Pose" = None,
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        static: "Static" = None,
        skin: "Skin" = None,
        animation: List["Animation"] = None,
        script: "Script" = None
    ):
        super().__init__(name=name, pose=pose, link=link, joint=joint, plugin=plugin, static=static, skin=skin, animation=animation, script=script)
        self.frame = frame or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Actor":
        _base = _PrevActor.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        return cls(name=_base.name, frame=_frame, pose=_base.pose, link=_base.link, joint=_base.joint, plugin=_base.plugin, static=_base.static, skin=_base.skin, animation=_base.animation, script=_base.script)
