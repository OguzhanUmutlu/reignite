from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_6.models.include import Include as _PrevInclude
from .pose import Pose
from .plugin import Plugin
from .uri import Uri
from .name import Name
from .static import Static


class Include(_PrevInclude):
    def __init__(
        self,
        pose: "Pose" = None,
        plugin: List["Plugin"] = None,
        uri: "Uri" = None,
        name: "Name" = None,
        static: "Static" = None
    ):
        super().__init__(pose=pose, plugin=plugin, uri=uri, name=name, static=static)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Include":
        _base = _PrevInclude.from_sdf(el)
        return cls(pose=_base.pose, plugin=_base.plugin, uri=_base.uri, name=_base.name, static=_base.static)
