from __future__ import annotations

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
from ...sdf1_0.models.ode import Ode as _PrevOde
from ...sdf1_0.models.physics import Physics as _PrevPhysics
from ...sdf1_0.models.world import World as _PrevWorld


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
            update_rate: "UpdateRate" = None,
            max_contacts: "MaxContacts" = None,
            gravity: "Gravity" = None,
            bullet: "Bullet" = None,
            ode: "Ode" = None
    ):
        super().__init__(ode=ode)
        self.type = type
        self.update_rate = update_rate
        self.max_contacts = max_contacts
        self.gravity = gravity
        self.bullet = bullet

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.type is not None:
            el.set("type", self.type)
        if self.update_rate is not None:
            el.append(self.update_rate.to_sdf())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        if self.gravity is not None:
            el.append(self.gravity.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Physics":
        _base = _PrevPhysics.from_sdf(el)
        _type = el.get("type", "ode")
        _c_update_rate = el.find("update_rate")
        _update_rate = UpdateRate.from_sdf(_c_update_rate) if _c_update_rate is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(type=_type, update_rate=_update_rate, max_contacts=_max_contacts, gravity=_gravity, bullet=_bullet,
                   ode=_base.ode)


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
            state: List["State"] = None
    ):
        super().__init__(name=name, gui=gui, physics=physics, scene=scene, light=light, model=model, actor=actor,
                         plugin=plugin, joint=joint, road=road, state=state)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "World":
        _base = _PrevWorld.from_sdf(el)
        return cls(name=_base.name, gui=_base.gui, physics=_base.physics, scene=_base.scene, light=_base.light,
                   model=_base.model, actor=_base.actor, plugin=_base.plugin, joint=_base.joint, road=_base.road,
                   state=_base.state)
