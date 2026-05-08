from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_3.models.ambient import Ambient as _PrevAmbient
from ...sdf1_3.models.clouds import Clouds as _PrevClouds
from ....utils.color import Color
from .speed import Speed
from .direction import Direction
from .humidity import Humidity
from .mean_size import MeanSize


class Ambient(_PrevAmbient):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0.4 0.4 0.4 1.0")
        super().__init__(ambient=ambient)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _base = _PrevAmbient.from_sdf(el)
        return cls(ambient=_base.ambient)


class Clouds(_PrevClouds):
    def __init__(
        self,
        speed: "Speed" = None,
        direction: "Direction" = None,
        humidity: "Humidity" = None,
        mean_size: "MeanSize" = None,
        ambient: "Ambient" = None
    ):
        super().__init__(speed=speed, direction=direction, humidity=humidity, mean_size=mean_size, ambient=ambient)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Clouds":
        _base = _PrevClouds.from_sdf(el)
        return cls(speed=_base.speed, direction=_base.direction, humidity=_base.humidity, mean_size=_base.mean_size, ambient=_base.ambient)
