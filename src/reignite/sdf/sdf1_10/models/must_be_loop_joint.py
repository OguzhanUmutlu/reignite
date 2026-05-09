from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.must_be_loop_joint import MustBeLoopJoint as _PrevMustBeLoopJoint


class MustBeLoopJoint(_PrevMustBeLoopJoint):
    def __init__(self, must_be_loop_joint: bool = False):
        super().__init__(must_be_loop_joint=must_be_loop_joint)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MustBeLoopJoint":
        _base = _PrevMustBeLoopJoint.from_sdf(el)
        return cls(must_be_loop_joint=_base.must_be_loop_joint)
