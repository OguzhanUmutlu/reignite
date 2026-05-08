from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.sky import Sky as _PrevSky
from .time import Time
from .sunrise import Sunrise
from .sunset import Sunset
from .clouds import Clouds
from .cubemap_uri import CubemapUri


class Sky(_PrevSky):
    def __init__(
        self,
        time: "Time" = None,
        sunrise: "Sunrise" = None,
        sunset: "Sunset" = None,
        clouds: "Clouds" = None,
        cubemap_uri: "CubemapUri" = None
    ):
        super().__init__(time=time, sunrise=sunrise, sunset=sunset, clouds=clouds, cubemap_uri=cubemap_uri)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sky":
        _base = _PrevSky.from_sdf(el)
        return cls(time=_base.time, sunrise=_base.sunrise, sunset=_base.sunset, clouds=_base.clouds, cubemap_uri=_base.cubemap_uri)
