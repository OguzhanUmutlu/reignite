from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_8.models.environment_map import EnvironmentMap as _PrevEnvironmentMap


class EnvironmentMap(_PrevEnvironmentMap):
    def __init__(self, environment_map: str = ""):
        super().__init__(environment_map=environment_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnvironmentMap":
        _base = _PrevEnvironmentMap.from_sdf(el)
        return cls(environment_map=_base.environment_map)
