from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .grasp_check import GraspCheck
from .gripper_link import GripperLink
from .palm_link import PalmLink
from ...sdf1_3.models.gripper import Gripper as _PrevGripper


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
