from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.sky import Sky as _PrevSky
from .time import Time
from .sunrise import Sunrise
from .sunset import Sunset
from .clouds import Clouds


class Sky(_PrevSky):
    def __init__(
        self,
        time: "Time" = None,
        sunrise: "Sunrise" = None,
        sunset: "Sunset" = None,
        clouds: "Clouds" = None
    ):
        super().__init__()
        self.time = time
        self.sunrise = sunrise
        self.sunset = sunset
        self.clouds = clouds

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.time is not None:
            el.append(self.time.to_sdf())
        if self.sunrise is not None:
            el.append(self.sunrise.to_sdf())
        if self.sunset is not None:
            el.append(self.sunset.to_sdf())
        if self.clouds is not None:
            el.append(self.clouds.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sky":
        _c_time = el.find("time")
        _time = Time.from_sdf(_c_time) if _c_time is not None else None
        _c_sunrise = el.find("sunrise")
        _sunrise = Sunrise.from_sdf(_c_sunrise) if _c_sunrise is not None else None
        _c_sunset = el.find("sunset")
        _sunset = Sunset.from_sdf(_c_sunset) if _c_sunset is not None else None
        _c_clouds = el.find("clouds")
        _clouds = Clouds.from_sdf(_c_clouds) if _c_clouds is not None else None
        return cls(time=_time, sunrise=_sunrise, sunset=_sunset, clouds=_clouds)
