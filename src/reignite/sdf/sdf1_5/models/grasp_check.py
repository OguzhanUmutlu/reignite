from __future__ import annotations

from xml.etree import ElementTree as ET

from .attach_steps import AttachSteps
from .detach_steps import DetachSteps
from .min_contact_count import MinContactCount
from ...sdf1_4.models.grasp_check import GraspCheck as _PrevGraspCheck


class GraspCheck(_PrevGraspCheck):
    def __init__(
            self,
            detach_steps: "DetachSteps" = None,
            attach_steps: "AttachSteps" = None,
            min_contact_count: "MinContactCount" = None
    ):
        super().__init__(detach_steps=detach_steps, attach_steps=attach_steps, min_contact_count=min_contact_count)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GraspCheck":
        _base = _PrevGraspCheck.from_sdf(el)
        return cls(detach_steps=_base.detach_steps, attach_steps=_base.attach_steps,
                   min_contact_count=_base.min_contact_count)
