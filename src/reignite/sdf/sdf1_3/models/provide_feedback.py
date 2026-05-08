from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class ProvideFeedback(Model):
    def __init__(self, provide_feedback: bool = False):
        self.provide_feedback = provide_feedback

    def to_sdf(self) -> ET.Element:
        el = ET.Element("provide_feedback")
        if self.provide_feedback is not None:
            el.text = str(self.provide_feedback).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ProvideFeedback":
        _text = el.text or False
        _provide_feedback = _text.strip().lower() == 'true'
        return cls(provide_feedback=_provide_feedback)
