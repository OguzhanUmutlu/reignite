from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .name import Name
from .plugin import Plugin
from .pose import Pose
from .uri import Uri
from ..model import Model
from ...sdf1_4.models.static import Static as _PrevStatic


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


class Include(Model):
    def __init__(
            self,
            plugin: List["Plugin"] = None,
            uri: "Uri" = None,
            pose: "Pose" = None,
            name: "Name" = None,
            static: "Static" = None
    ):
        self.plugin = plugin or []
        self.uri = uri
        self.pose = pose
        self.name = name
        self.static = static

    def to_sdf(self) -> ET.Element:
        el = ET.Element("include")
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.uri is not None:
            el.append(self.uri.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.name is not None:
            el.append(self.name.to_sdf())
        if self.static is not None:
            el.append(self.static.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Include":
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri) if _c_uri is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name) if _c_name is not None else None
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static) if _c_static is not None else None
        return cls(plugin=_plugin, uri=_uri, pose=_pose, name=_name, static=_static)
