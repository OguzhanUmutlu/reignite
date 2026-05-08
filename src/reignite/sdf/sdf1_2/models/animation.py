from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.animation import Animation as _PrevAnimation
from .filename import Filename
from .scale import Scale
from .interpolate_x import InterpolateX


class Animation(_PrevAnimation):
    def __init__(
        self,
        name: str = "__default__",
        filename: "Filename" = None,
        scale: "Scale" = None,
        interpolate_x: "InterpolateX" = None
    ):
        super().__init__(name=name, filename=filename, scale=scale, interpolate_x=interpolate_x)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Animation":
        _base = _PrevAnimation.from_sdf(el)
        return cls(name=_base.name, filename=_base.filename, scale=_base.scale, interpolate_x=_base.interpolate_x)
