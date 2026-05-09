from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .actor import Actor
from .audio import Audio
from .gui import Gui
from .include import Include
from .joint import Joint
from .light import Light
from .model import Model
from .plugin import Plugin
from .road import Road
from .scene import Scene
from .spherical_coordinates import SphericalCoordinates
from .state import State
from ...sdf1_3.models.ode import Ode as _PrevOde
from ...sdf1_3.models.physics import Physics as _PrevPhysics
from ...sdf1_3.models.world import World as _PrevWorld


class Ode(_PrevOde):
    def __init__(self, solver: "Solver" = None, constraints: "Constraints" = None):
        super().__init__()
        self.solver = solver
        self.constraints = constraints

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.solver is not None:
            el.append(self.solver.to_sdf())
        if self.constraints is not None:
            el.append(self.constraints.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver) if _c_solver is not None else None
        _c_constraints = el.find("constraints")
        _constraints = Constraints.from_sdf(_c_constraints) if _c_constraints is not None else None
        return cls(solver=_solver, constraints=_constraints)


class Physics(_PrevPhysics):
    def __init__(
            self,
            type: str = "ode",
            max_step_size: "MaxStepSize" = None,
            real_time_factor: "RealTimeFactor" = None,
            real_time_update_rate: "RealTimeUpdateRate" = None,
            max_contacts: "MaxContacts" = None,
            gravity: "Gravity" = None,
            simbody: "Simbody" = None,
            bullet: "Bullet" = None,
            ode: "Ode" = None
    ):
        super().__init__(ode=ode)
        self.type = type
        self.max_step_size = max_step_size
        self.real_time_factor = real_time_factor
        self.real_time_update_rate = real_time_update_rate
        self.max_contacts = max_contacts
        self.gravity = gravity
        self.simbody = simbody
        self.bullet = bullet

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.type is not None:
            el.set("type", self.type)
        if self.max_step_size is not None:
            el.append(self.max_step_size.to_sdf())
        if self.real_time_factor is not None:
            el.append(self.real_time_factor.to_sdf())
        if self.real_time_update_rate is not None:
            el.append(self.real_time_update_rate.to_sdf())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        if self.gravity is not None:
            el.append(self.gravity.to_sdf())
        if self.simbody is not None:
            el.append(self.simbody.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Physics":
        _base = _PrevPhysics.from_sdf(el)
        _type = el.get("type", "ode")
        _c_max_step_size = el.find("max_step_size")
        _max_step_size = MaxStepSize.from_sdf(_c_max_step_size) if _c_max_step_size is not None else None
        _c_real_time_factor = el.find("real_time_factor")
        _real_time_factor = RealTimeFactor.from_sdf(_c_real_time_factor) if _c_real_time_factor is not None else None
        _c_real_time_update_rate = el.find("real_time_update_rate")
        _real_time_update_rate = RealTimeUpdateRate.from_sdf(
            _c_real_time_update_rate) if _c_real_time_update_rate is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_simbody = el.find("simbody")
        _simbody = Simbody.from_sdf(_c_simbody) if _c_simbody is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(type=_type, max_step_size=_max_step_size, real_time_factor=_real_time_factor,
                   real_time_update_rate=_real_time_update_rate, max_contacts=_max_contacts, gravity=_gravity,
                   simbody=_simbody, bullet=_bullet, ode=_base.ode)


class World(_PrevWorld):
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
            spherical_coordinates: "SphericalCoordinates" = None,
            state: List["State"] = None,
            audio: "Audio" = None,
            include: List["Include"] = None
    ):
        super().__init__(name=name, gui=gui, physics=physics, scene=scene, light=light, model=model, actor=actor,
                         plugin=plugin, joint=joint, road=road, state=state)
        self.spherical_coordinates = spherical_coordinates
        self.audio = audio
        self.include = include or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.spherical_coordinates is not None:
            el.append(self.spherical_coordinates.to_sdf())
        if self.audio is not None:
            el.append(self.audio.to_sdf())
        for item in (self.include or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "World":
        _base = _PrevWorld.from_sdf(el)
        _c_spherical_coordinates = el.find("spherical_coordinates")
        _spherical_coordinates = SphericalCoordinates.from_sdf(
            _c_spherical_coordinates) if _c_spherical_coordinates is not None else None
        _c_audio = el.find("audio")
        _audio = Audio.from_sdf(_c_audio) if _c_audio is not None else None
        _include = [Include.from_sdf(c) for c in el.findall("include")]
        return cls(name=_base.name, gui=_base.gui, physics=_base.physics, scene=_base.scene, light=_base.light,
                   model=_base.model, actor=_base.actor, plugin=_base.plugin, joint=_base.joint, road=_base.road,
                   spherical_coordinates=_spherical_coordinates, state=_base.state, audio=_audio, include=_include)
