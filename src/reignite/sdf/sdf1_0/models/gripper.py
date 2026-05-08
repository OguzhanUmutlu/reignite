from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from .grasp_check import GraspCheck
from .gripper_link import GripperLink
from .palm_link import PalmLink


class Gripper(Model):
    def __init__(
        self,
        name: str = "__default__",
        grasp_check: "GraspCheck" = None,
        gripper_link: List["GripperLink"] = None,
        palm_link: "PalmLink" = None
    ):
        self.name = name
        self.grasp_check = grasp_check
        self.gripper_link = gripper_link or []
        self.palm_link = palm_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gripper")
        if self.name is not None:
            el.set("name", self.name)
        if self.grasp_check is not None:
            el.append(self.grasp_check.to_sdf())
        for item in (self.gripper_link or []):
            el.append(item.to_sdf())
        if self.palm_link is not None:
            el.append(self.palm_link.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gripper":
        _name = el.get("name", "__default__")
        _c_grasp_check = el.find("grasp_check")
        _grasp_check = GraspCheck.from_sdf(_c_grasp_check) if _c_grasp_check is not None else None
        _gripper_link = [GripperLink.from_sdf(c) for c in el.findall("gripper_link")]
        _c_palm_link = el.find("palm_link")
        _palm_link = PalmLink.from_sdf(_c_palm_link) if _c_palm_link is not None else None
        return cls(name=_name, grasp_check=_grasp_check, gripper_link=_gripper_link, palm_link=_palm_link)
