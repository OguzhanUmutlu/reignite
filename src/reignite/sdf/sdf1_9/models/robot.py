from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .gripper import Gripper
from .joint import Joint
from .link import Link
from .plugin import Plugin
from .pose import Pose
from ...sdf1_8.models.robot import Robot as _PrevRobot


class Robot(_PrevRobot):
    def __init__(
            self,
            name: str = "__default__",
            link: List["Link"] = None,
            joint: List["Joint"] = None,
            plugin: List["Plugin"] = None,
            gripper: List["Gripper"] = None,
            pose: "Pose" = None
    ):
        super().__init__(name=name, link=link, joint=joint, plugin=plugin, gripper=gripper, pose=pose)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Robot":
        _base = _PrevRobot.from_sdf(el)
        return cls(name=_base.name, link=_base.link, joint=_base.joint, plugin=_base.plugin, gripper=_base.gripper,
                   pose=_base.pose)
