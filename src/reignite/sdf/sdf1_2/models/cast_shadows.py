from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class CastShadows(Model):
    def __init__(self, cast_shadows: bool = True):
        self.cast_shadows = cast_shadows

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cast_shadows")
        if self.cast_shadows is not None:
            el.text = str(self.cast_shadows).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CastShadows":
        _text = el.text or True
        _cast_shadows = _text.strip().lower() == 'true'
        return cls(cast_shadows=_cast_shadows)
