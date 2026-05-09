from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .gripper import Gripper
from .joint import Joint
from .link import Link
from .origin import Origin
from .plugin import Plugin
from ..model import Model


class Model(Model):
    def __init__(
            self,
            name: str = "__default__",
            static: bool = False,
            link: List["Link"] = None,
            joint: List["Joint"] = None,
            plugin: List["Plugin"] = None,
            gripper: List["Gripper"] = None,
            origin: "Origin" = None
    ):
        self.name = name
        self.static = static
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.gripper = gripper or []
        self.origin = origin

    def to_sdf(self) -> ET.Element:
        el = ET.Element("model")
        if self.name is not None:
            el.set("name", self.name)
        if self.static is not None:
            el.set("static", str(self.static).lower())
        for item in (self.link or []):
            el.append(item.to_sdf())
        for item in (self.joint or []):
            el.append(item.to_sdf())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        for item in (self.gripper or []):
            el.append(item.to_sdf())
        if self.origin is not None:
            el.append(self.origin.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        _name = el.get("name", "__default__")
        _static = el.get("static", False).strip().lower() == 'true'
        _link = [Link.from_sdf(c) for c in el.findall("link")]
        _joint = [Joint.from_sdf(c) for c in el.findall("joint")]
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _gripper = [Gripper.from_sdf(c) for c in el.findall("gripper")]
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin) if _c_origin is not None else None
        return cls(name=_name, static=_static, link=_link, joint=_joint, plugin=_plugin, gripper=_gripper,
                   origin=_origin)
