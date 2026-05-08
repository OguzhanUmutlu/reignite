from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_3.models.gripper_link import GripperLink as _PrevGripperLink


class GripperLink(_PrevGripperLink):
    def __init__(self, gripper_link: str = "__default__"):
        super().__init__(gripper_link=gripper_link)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GripperLink":
        _base = _PrevGripperLink.from_sdf(el)
        return cls(gripper_link=_base.gripper_link)
