from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .animation import Animation
from .joint import Joint
from .link import Link
from .origin import Origin
from .plugin import Plugin
from .script import Script
from .skin import Skin
from ..model import Model


class Actor(Model):
    def __init__(
            self,
            name: str = "__default__",
            static: bool = False,
            link: List["Link"] = None,
            joint: List["Joint"] = None,
            plugin: List["Plugin"] = None,
            origin: "Origin" = None,
            skin: "Skin" = None,
            animation: List["Animation"] = None,
            script: "Script" = None
    ):
        self.name = name
        self.static = static
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.origin = origin
        self.skin = skin
        self.animation = animation or []
        self.script = script

    def to_sdf(self) -> ET.Element:
        el = ET.Element("actor")
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
        if self.origin is not None:
            el.append(self.origin.to_sdf())
        if self.skin is not None:
            el.append(self.skin.to_sdf())
        for item in (self.animation or []):
            el.append(item.to_sdf())
        if self.script is not None:
            el.append(self.script.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Actor":
        _name = el.get("name", "__default__")
        _static = el.get("static", False).strip().lower() == 'true'
        _link = [Link.from_sdf(c) for c in el.findall("link")]
        _joint = [Joint.from_sdf(c) for c in el.findall("joint")]
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin) if _c_origin is not None else None
        _c_skin = el.find("skin")
        _skin = Skin.from_sdf(_c_skin) if _c_skin is not None else None
        _animation = [Animation.from_sdf(c) for c in el.findall("animation")]
        _c_script = el.find("script")
        _script = Script.from_sdf(_c_script) if _c_script is not None else None
        return cls(name=_name, static=_static, link=_link, joint=_joint, plugin=_plugin, origin=_origin, skin=_skin,
                   animation=_animation, script=_script)
