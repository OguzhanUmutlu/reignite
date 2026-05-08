from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.shadows import Shadows as _PrevShadows


class Shadows(_PrevShadows):
    def __init__(self, shadows: bool = True):
        super().__init__()
        self.shadows = shadows

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.shadows is not None:
            el.text = str(self.shadows).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Shadows":
        _text = el.text or True
        _shadows = _text.strip().lower() == 'true'
        return cls(shadows=_shadows)
