from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .name import Name
from .plugin import Plugin
from .pose import Pose
from .uri import Uri
from ...sdf1_5.models.include import Include as _PrevInclude
from ...sdf1_5.models.static import Static as _PrevStatic


class Static(_PrevStatic):
    def __init__(self, static: bool = False):
        super().__init__(static=static)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Static":
        _base = _PrevStatic.from_sdf(el)
        return cls(static=_base.static)


class Include(_PrevInclude):
    def __init__(
            self,
            plugin: List["Plugin"] = None,
            uri: "Uri" = None,
            pose: "Pose" = None,
            name: "Name" = None,
            static: "Static" = None
    ):
        super().__init__(plugin=plugin, uri=uri, pose=pose, name=name, static=static)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Include":
        _base = _PrevInclude.from_sdf(el)
        return cls(plugin=_base.plugin, uri=_base.uri, pose=_base.pose, name=_base.name, static=_base.static)
