from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from .world import World
from .model import Model
from .actor import Actor
from .light import Light


class Gazebo(Model):
    def __init__(
        self,
        version: str = "1.0",
        world: List["World"] = None,
        model: List["Model"] = None,
        actor: List["Actor"] = None,
        light: List["Light"] = None
    ):
        self.version = version
        self.world = world or []
        self.model = model or []
        self.actor = actor or []
        self.light = light or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gazebo")
        if self.version is not None:
            el.set("version", self.version)
        for item in (self.world or []):
            el.append(item.to_sdf())
        for item in (self.model or []):
            el.append(item.to_sdf())
        for item in (self.actor or []):
            el.append(item.to_sdf())
        for item in (self.light or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gazebo":
        _version = el.get("version", "1.0")
        _world = [World.from_sdf(c) for c in el.findall("world")]
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        _actor = [Actor.from_sdf(c) for c in el.findall("actor")]
        _light = [Light.from_sdf(c) for c in el.findall("light")]
        return cls(version=_version, world=_world, model=_model, actor=_actor, light=_light)
