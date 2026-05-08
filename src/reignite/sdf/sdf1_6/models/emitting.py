from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Emitting(Model):
    def __init__(self, emitting: bool = True):
        self.emitting = emitting

    def to_sdf(self) -> ET.Element:
        el = ET.Element("emitting")
        if self.emitting is not None:
            el.text = str(self.emitting).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Emitting":
        _text = el.text or True
        _emitting = _text.strip().lower() == 'true'
        return cls(emitting=_emitting)
