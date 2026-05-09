from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .allow_auto_disable import AllowAutoDisable
from .joint import Joint
from .link import Link
from .plugin import Plugin
from .pose import Pose
from .static import Static
from ..model import Model
from ...sdf1_0.models.gripper import Gripper as _PrevGripper
from ...sdf1_0.models.model import Model as _PrevModel


class Gripper(_PrevGripper):
    def __init__(
            self,
            name: str = "__default__",
            grasp_check: "GraspCheck" = None,
            gripper_link: List["GripperLink"] = None,
            palm_link: "PalmLink" = None
    ):
        super().__init__(name=name, grasp_check=grasp_check, gripper_link=gripper_link, palm_link=palm_link)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gripper":
        _base = _PrevGripper.from_sdf(el)
        return cls(name=_base.name, grasp_check=_base.grasp_check, gripper_link=_base.gripper_link,
                   palm_link=_base.palm_link)


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
        super().__init__(name=name, link=link, joint=joint, plugin=plugin, gripper=gripper, static=static)
        self.allow_auto_disable = allow_auto_disable
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.allow_auto_disable is not None:
            el.append(self.allow_auto_disable.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        _base = _PrevModel.from_sdf(el)
        _c_allow_auto_disable = el.find("allow_auto_disable")
        _allow_auto_disable = AllowAutoDisable.from_sdf(
            _c_allow_auto_disable) if _c_allow_auto_disable is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_base.name, link=_base.link, joint=_base.joint, plugin=_base.plugin, gripper=_base.gripper,
                   static=_base.static, allow_auto_disable=_allow_auto_disable, pose=_pose)
