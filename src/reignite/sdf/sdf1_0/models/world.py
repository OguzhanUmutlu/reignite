from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .actor import Actor
from .gui import Gui
from .joint import Joint
from .light import Light
from .model import Model
from .plugin import Plugin
from .road import Road
from .scene import Scene
from .state import State


def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class Physics(Model):
    def __init__(
            self,
            type: str = "ode",
            update_rate: float = 0,
            max_contacts: "MaxContacts" = None,
            gravity: "Gravity" = None,
            bullet: "Bullet" = None,
            ode: "Ode" = None
    ):
        self.type = type
        self.update_rate = update_rate
        self.max_contacts = max_contacts
        self.gravity = gravity
        self.bullet = bullet
        self.ode = ode

    def to_sdf(self) -> ET.Element:
        el = ET.Element("physics")
        if self.type is not None:
            el.set("type", self.type)
        if self.update_rate is not None:
            el.set("update_rate", str(self.update_rate))
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        if self.gravity is not None:
            el.append(self.gravity.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Physics":
        _type = el.get("type", "ode")
        _update_rate = _parse_double(el.get("update_rate", 0))
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(type=_type, update_rate=_update_rate, max_contacts=_max_contacts, gravity=_gravity, bullet=_bullet,
                   ode=_ode)


class World(Model):
    def __init__(
            self,
            name: str = "__default__",
            gui: "Gui" = None,
            physics: "Physics" = None,
            scene: "Scene" = None,
            light: List["Light"] = None,
            model: List["Model"] = None,
            actor: List["Actor"] = None,
            plugin: List["Plugin"] = None,
            joint: List["Joint"] = None,
            road: List["Road"] = None,
            state: List["State"] = None
    ):
        self.name = name
        self.gui = gui
        self.physics = physics
        self.scene = scene
        self.light = light or []
        self.model = model or []
        self.actor = actor or []
        self.plugin = plugin or []
        self.joint = joint or []
        self.road = road or []
        self.state = state or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("world")
        if self.name is not None:
            el.set("name", self.name)
        if self.gui is not None:
            el.append(self.gui.to_sdf())
        if self.physics is not None:
            el.append(self.physics.to_sdf())
        if self.scene is not None:
            el.append(self.scene.to_sdf())
        for item in (self.light or []):
            el.append(item.to_sdf())
        for item in (self.model or []):
            el.append(item.to_sdf())
        for item in (self.actor or []):
            el.append(item.to_sdf())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        for item in (self.joint or []):
            el.append(item.to_sdf())
        for item in (self.road or []):
            el.append(item.to_sdf())
        for item in (self.state or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "World":
        _name = el.get("name", "__default__")
        _c_gui = el.find("gui")
        _gui = Gui.from_sdf(_c_gui) if _c_gui is not None else None
        _c_physics = el.find("physics")
        _physics = Physics.from_sdf(_c_physics) if _c_physics is not None else None
        _c_scene = el.find("scene")
        _scene = Scene.from_sdf(_c_scene) if _c_scene is not None else None
        _light = [Light.from_sdf(c) for c in el.findall("light")]
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        _actor = [Actor.from_sdf(c) for c in el.findall("actor")]
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _joint = [Joint.from_sdf(c) for c in el.findall("joint")]
        _road = [Road.from_sdf(c) for c in el.findall("road")]
        _state = [State.from_sdf(c) for c in el.findall("state")]
        return cls(name=_name, gui=_gui, physics=_physics, scene=_scene, light=_light, model=_model, actor=_actor,
                   plugin=_plugin, joint=_joint, road=_road, state=_state)
