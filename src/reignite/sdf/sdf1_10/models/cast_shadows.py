from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.cast_shadows import CastShadows as _PrevCastShadows


class CastShadows(_PrevCastShadows):
    def __init__(self, cast_shadows: bool = True):
        super().__init__(cast_shadows=cast_shadows)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CastShadows":
        _base = _PrevCastShadows.from_sdf(el)
        return cls(cast_shadows=_base.cast_shadows)
