from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model


class GraspCheck(Model):
    def __init__(
        self,
        detach_steps: "DetachSteps" = None,
        attach_steps: "AttachSteps" = None,
        min_contact_count: "MinContactCount" = None
    ):
        self.detach_steps = detach_steps
        self.attach_steps = attach_steps
        self.min_contact_count = min_contact_count

    def to_sdf(self) -> ET.Element:
        el = ET.Element("grasp_check")
        if self.detach_steps is not None:
            el.append(self.detach_steps.to_sdf())
        if self.attach_steps is not None:
            el.append(self.attach_steps.to_sdf())
        if self.min_contact_count is not None:
            el.append(self.min_contact_count.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GraspCheck":
        _c_detach_steps = el.find("detach_steps")
        _detach_steps = DetachSteps.from_sdf(_c_detach_steps) if _c_detach_steps is not None else None
        _c_attach_steps = el.find("attach_steps")
        _attach_steps = AttachSteps.from_sdf(_c_attach_steps) if _c_attach_steps is not None else None
        _c_min_contact_count = el.find("min_contact_count")
        _min_contact_count = MinContactCount.from_sdf(_c_min_contact_count) if _c_min_contact_count is not None else None
        return cls(detach_steps=_detach_steps, attach_steps=_attach_steps, min_contact_count=_min_contact_count)


class GripperLink(Model):
    def __init__(self, gripper_link: str = "__default__"):
        self.gripper_link = gripper_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gripper_link")
        if self.gripper_link is not None:
            el.text = self.gripper_link
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GripperLink":
        _text = el.text or "__default__"
        _gripper_link = _text
        return cls(gripper_link=_gripper_link)


class PalmLink(Model):
    def __init__(self, palm_link: str = "__default__"):
        self.palm_link = palm_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("palm_link")
        if self.palm_link is not None:
            el.text = self.palm_link
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PalmLink":
        _text = el.text or "__default__"
        _palm_link = _text
        return cls(palm_link=_palm_link)


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
