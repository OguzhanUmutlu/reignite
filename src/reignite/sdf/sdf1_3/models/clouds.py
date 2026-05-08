from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color
from .speed import Speed
from .direction import Direction
from .humidity import Humidity
from .mean_size import MeanSize


class Ambient(Model):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0.2 0.2 0.2 1.0")
        self.ambient = ambient

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _text = el.text or "0.2 0.2 0.2 1.0"
        _ambient = Color.from_sdf(_text)
        return cls(ambient=_ambient)


class Clouds(Model):
    def __init__(
        self,
        speed: "Speed" = None,
        direction: "Direction" = None,
        humidity: "Humidity" = None,
        mean_size: "MeanSize" = None,
        ambient: "Ambient" = None
    ):
        self.speed = speed
        self.direction = direction
        self.humidity = humidity
        self.mean_size = mean_size
        self.ambient = ambient

    def to_sdf(self) -> ET.Element:
        el = ET.Element("clouds")
        if self.speed is not None:
            el.append(self.speed.to_sdf())
        if self.direction is not None:
            el.append(self.direction.to_sdf())
        if self.humidity is not None:
            el.append(self.humidity.to_sdf())
        if self.mean_size is not None:
            el.append(self.mean_size.to_sdf())
        if self.ambient is not None:
            el.append(self.ambient.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Clouds":
        _c_speed = el.find("speed")
        _speed = Speed.from_sdf(_c_speed) if _c_speed is not None else None
        _c_direction = el.find("direction")
        _direction = Direction.from_sdf(_c_direction) if _c_direction is not None else None
        _c_humidity = el.find("humidity")
        _humidity = Humidity.from_sdf(_c_humidity) if _c_humidity is not None else None
        _c_mean_size = el.find("mean_size")
        _mean_size = MeanSize.from_sdf(_c_mean_size) if _c_mean_size is not None else None
        _c_ambient = el.find("ambient")
        _ambient = Ambient.from_sdf(_c_ambient) if _c_ambient is not None else None
        return cls(speed=_speed, direction=_direction, humidity=_humidity, mean_size=_mean_size, ambient=_ambient)
