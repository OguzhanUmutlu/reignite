from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_11.models.provide_feedback import ProvideFeedback as _PrevProvideFeedback


class ProvideFeedback(_PrevProvideFeedback):
    def __init__(self, provide_feedback: bool = False):
        super().__init__(provide_feedback=provide_feedback)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ProvideFeedback":
        _base = _PrevProvideFeedback.from_sdf(el)
        return cls(provide_feedback=_base.provide_feedback)
