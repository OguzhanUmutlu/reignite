from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


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
