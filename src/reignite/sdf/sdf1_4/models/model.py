from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_3.models.model import Model as _PrevModel
from .link import Link
from .joint import Joint
from .plugin import Plugin
from .gripper import Gripper
from .static import Static
from .allow_auto_disable import AllowAutoDisable
from .pose import Pose


class Model(_PrevModel):
    def __init__(
        self,
        name: str = "__default__",
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        gripper: List["Gripper"] = None,
        static: "Static" = None,
        allow_auto_disable: "AllowAutoDisable" = None,
        pose: "Pose" = None
    ):
        super().__init__(name=name, link=link, joint=joint, plugin=plugin, gripper=gripper, static=static, allow_auto_disable=allow_auto_disable, pose=pose)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        _base = _PrevModel.from_sdf(el)
        return cls(name=_base.name, link=_base.link, joint=_base.joint, plugin=_base.plugin, gripper=_base.gripper, static=_base.static, allow_auto_disable=_base.allow_auto_disable, pose=_base.pose)
