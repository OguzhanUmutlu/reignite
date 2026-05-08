from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class MustBeLoopJoint(Model):
    def __init__(self, must_be_loop_joint: bool = False):
        self.must_be_loop_joint = must_be_loop_joint

    def to_sdf(self) -> ET.Element:
        el = ET.Element("must_be_loop_joint")
        if self.must_be_loop_joint is not None:
            el.text = str(self.must_be_loop_joint).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MustBeLoopJoint":
        _text = el.text or False
        _must_be_loop_joint = _text.strip().lower() == 'true'
        return cls(must_be_loop_joint=_must_be_loop_joint)
