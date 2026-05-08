from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ....utils.pose import Pose
from ....utils.vector3 import Vector3
from .gui import Gui
from .scene import Scene
from .light import Light
from .model import Model
from .actor import Actor
from .road import Road
from .state import State


import math
import sys

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



class UpdateRate(Model):
    def __init__(self, update_rate: float = 1000):
        self.update_rate = update_rate

    def to_sdf(self) -> ET.Element:
        el = ET.Element("update_rate")
        if self.update_rate is not None:
            el.text = str(self.update_rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UpdateRate":
        _text = el.text or 1000
        _update_rate = _parse_double(_text)
        return cls(update_rate=_update_rate)


class MaxContacts(Model):
    def __init__(self, max_contacts: int = 20):
        self.max_contacts = max_contacts

    def to_sdf(self) -> ET.Element:
        el = ET.Element("max_contacts")
        if self.max_contacts is not None:
            el.text = str(self.max_contacts)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxContacts":
        _text = el.text or 20
        _max_contacts = _parse_int32(_text)
        return cls(max_contacts=_max_contacts)


class Gravity(Model):
    def __init__(self, gravity: Vector3 = None):
        if gravity is None:
            gravity = Vector3.from_sdf("0 0 -9.8")
        self.gravity = gravity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gravity")
        if self.gravity is not None:
            el.text = self.gravity.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gravity":
        _text = el.text or "0 0 -9.8"
        _gravity = Vector3.from_sdf(_text)
        return cls(gravity=_gravity)


class Dt(Model):
    def __init__(self, dt: float = 0.001):
        self.dt = dt

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dt")
        if self.dt is not None:
            el.text = str(self.dt)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dt":
        _text = el.text or 0.001
        _dt = _parse_double(_text)
        return cls(dt=_dt)


class Bullet(Model):
    def __init__(self, dt: "Dt" = None):
        self.dt = dt

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bullet")
        if self.dt is not None:
            el.append(self.dt.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _c_dt = el.find("dt")
        _dt = Dt.from_sdf(_c_dt) if _c_dt is not None else None
        return cls(dt=_dt)


class Type(Model):
    def __init__(self, type: str = "quick"):
        self.type = type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _text = el.text or "quick"
        _type = _text
        return cls(type=_type)


class Iters(Model):
    def __init__(self, iters: int = 50):
        self.iters = iters

    def to_sdf(self) -> ET.Element:
        el = ET.Element("iters")
        if self.iters is not None:
            el.text = str(self.iters)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Iters":
        _text = el.text or 50
        _iters = _parse_int32(_text)
        return cls(iters=_iters)


class PreconIters(Model):
    def __init__(self, precon_iters: int = 0):
        self.precon_iters = precon_iters

    def to_sdf(self) -> ET.Element:
        el = ET.Element("precon_iters")
        if self.precon_iters is not None:
            el.text = str(self.precon_iters)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PreconIters":
        _text = el.text or 0
        _precon_iters = _parse_int32(_text)
        return cls(precon_iters=_precon_iters)


class Sor(Model):
    def __init__(self, sor: float = 1.3):
        self.sor = sor

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sor")
        if self.sor is not None:
            el.text = str(self.sor)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sor":
        _text = el.text or 1.3
        _sor = _parse_double(_text)
        return cls(sor=_sor)


class Solver(Model):
    def __init__(
        self,
        type: "Type" = None,
        dt: "Dt" = None,
        iters: "Iters" = None,
        precon_iters: "PreconIters" = None,
        sor: "Sor" = None
    ):
        self.type = type
        self.dt = dt
        self.iters = iters
        self.precon_iters = precon_iters
        self.sor = sor

    def to_sdf(self) -> ET.Element:
        el = ET.Element("solver")
        if self.type is not None:
            el.append(self.type.to_sdf())
        if self.dt is not None:
            el.append(self.dt.to_sdf())
        if self.iters is not None:
            el.append(self.iters.to_sdf())
        if self.precon_iters is not None:
            el.append(self.precon_iters.to_sdf())
        if self.sor is not None:
            el.append(self.sor.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Solver":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type) if _c_type is not None else None
        _c_dt = el.find("dt")
        _dt = Dt.from_sdf(_c_dt) if _c_dt is not None else None
        _c_iters = el.find("iters")
        _iters = Iters.from_sdf(_c_iters) if _c_iters is not None else None
        _c_precon_iters = el.find("precon_iters")
        _precon_iters = PreconIters.from_sdf(_c_precon_iters) if _c_precon_iters is not None else None
        _c_sor = el.find("sor")
        _sor = Sor.from_sdf(_c_sor) if _c_sor is not None else None
        return cls(type=_type, dt=_dt, iters=_iters, precon_iters=_precon_iters, sor=_sor)


class Cfm(Model):
    def __init__(self, cfm: float = 0):
        self.cfm = cfm

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cfm")
        if self.cfm is not None:
            el.text = str(self.cfm)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Cfm":
        _text = el.text or 0
        _cfm = _parse_double(_text)
        return cls(cfm=_cfm)


class Erp(Model):
    def __init__(self, erp: float = 0.2):
        self.erp = erp

    def to_sdf(self) -> ET.Element:
        el = ET.Element("erp")
        if self.erp is not None:
            el.text = str(self.erp)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Erp":
        _text = el.text or 0.2
        _erp = _parse_double(_text)
        return cls(erp=_erp)


class ContactMaxCorrectingVel(Model):
    def __init__(self, contact_max_correcting_vel: float = 100.0):
        self.contact_max_correcting_vel = contact_max_correcting_vel

    def to_sdf(self) -> ET.Element:
        el = ET.Element("contact_max_correcting_vel")
        if self.contact_max_correcting_vel is not None:
            el.text = str(self.contact_max_correcting_vel)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ContactMaxCorrectingVel":
        _text = el.text or 100.0
        _contact_max_correcting_vel = _parse_double(_text)
        return cls(contact_max_correcting_vel=_contact_max_correcting_vel)


class ContactSurfaceLayer(Model):
    def __init__(self, contact_surface_layer: float = 0.001):
        self.contact_surface_layer = contact_surface_layer

    def to_sdf(self) -> ET.Element:
        el = ET.Element("contact_surface_layer")
        if self.contact_surface_layer is not None:
            el.text = str(self.contact_surface_layer)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ContactSurfaceLayer":
        _text = el.text or 0.001
        _contact_surface_layer = _parse_double(_text)
        return cls(contact_surface_layer=_contact_surface_layer)


class Constraints(Model):
    def __init__(
        self,
        cfm: "Cfm" = None,
        erp: "Erp" = None,
        contact_max_correcting_vel: "ContactMaxCorrectingVel" = None,
        contact_surface_layer: "ContactSurfaceLayer" = None
    ):
        self.cfm = cfm
        self.erp = erp
        self.contact_max_correcting_vel = contact_max_correcting_vel
        self.contact_surface_layer = contact_surface_layer

    def to_sdf(self) -> ET.Element:
        el = ET.Element("constraints")
        if self.cfm is not None:
            el.append(self.cfm.to_sdf())
        if self.erp is not None:
            el.append(self.erp.to_sdf())
        if self.contact_max_correcting_vel is not None:
            el.append(self.contact_max_correcting_vel.to_sdf())
        if self.contact_surface_layer is not None:
            el.append(self.contact_surface_layer.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Constraints":
        _c_cfm = el.find("cfm")
        _cfm = Cfm.from_sdf(_c_cfm) if _c_cfm is not None else None
        _c_erp = el.find("erp")
        _erp = Erp.from_sdf(_c_erp) if _c_erp is not None else None
        _c_contact_max_correcting_vel = el.find("contact_max_correcting_vel")
        _contact_max_correcting_vel = ContactMaxCorrectingVel.from_sdf(_c_contact_max_correcting_vel) if _c_contact_max_correcting_vel is not None else None
        _c_contact_surface_layer = el.find("contact_surface_layer")
        _contact_surface_layer = ContactSurfaceLayer.from_sdf(_c_contact_surface_layer) if _c_contact_surface_layer is not None else None
        return cls(cfm=_cfm, erp=_erp, contact_max_correcting_vel=_contact_max_correcting_vel, contact_surface_layer=_contact_surface_layer)


class Ode(Model):
    def __init__(self, solver: "Solver" = None, constraints: "Constraints" = None):
        self.solver = solver
        self.constraints = constraints

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ode")
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


class Physics(Model):
    def __init__(
        self,
        type: str = "ode",
        update_rate: "UpdateRate" = None,
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
            el.append(self.update_rate.to_sdf())
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
        _c_update_rate = el.find("update_rate")
        _update_rate = UpdateRate.from_sdf(_c_update_rate) if _c_update_rate is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(type=_type, update_rate=_update_rate, max_contacts=_max_contacts, gravity=_gravity, bullet=_bullet, ode=_ode)


class Plugin(Model):
    def __init__(self, name: str = "__default__", filename: str = "__default__"):
        self.name = name
        self.filename = filename

    def to_sdf(self) -> ET.Element:
        el = ET.Element("plugin")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.set("filename", self.filename)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Plugin":
        _name = el.get("name", "__default__")
        _filename = el.get("filename", "__default__")
        return cls(name=_name, filename=_filename)


class Parent(Model):
    def __init__(self, parent: str = "__default__"):
        self.parent = parent

    def to_sdf(self) -> ET.Element:
        el = ET.Element("parent")
        if self.parent is not None:
            el.text = self.parent
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Parent":
        _text = el.text or "__default__"
        _parent = _text
        return cls(parent=_parent)


class Child(Model):
    def __init__(self, child: str = "__default__"):
        self.child = child

    def to_sdf(self) -> ET.Element:
        el = ET.Element("child")
        if self.child is not None:
            el.text = self.child
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Child":
        _text = el.text or "__default__"
        _child = _text
        return cls(child=_child)


class Pose(Model):
    def __init__(self, pose: Pose = None):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        return cls(pose=_pose)


class ThreadPitch(Model):
    def __init__(self, thread_pitch: float = 1.0):
        self.thread_pitch = thread_pitch

    def to_sdf(self) -> ET.Element:
        el = ET.Element("thread_pitch")
        if self.thread_pitch is not None:
            el.text = str(self.thread_pitch)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ThreadPitch":
        _text = el.text or 1.0
        _thread_pitch = _parse_double(_text)
        return cls(thread_pitch=_thread_pitch)


class Xyz(Model):
    def __init__(self, xyz: Vector3 = None):
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz

    def to_sdf(self) -> ET.Element:
        el = ET.Element("xyz")
        if self.xyz is not None:
            el.text = self.xyz.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Xyz":
        _text = el.text or "0 0 1"
        _xyz = Vector3.from_sdf(_text)
        return cls(xyz=_xyz)


class Damping(Model):
    def __init__(self, damping: float = 0):
        self.damping = damping

    def to_sdf(self) -> ET.Element:
        el = ET.Element("damping")
        if self.damping is not None:
            el.text = str(self.damping)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Damping":
        _text = el.text or 0
        _damping = _parse_double(_text)
        return cls(damping=_damping)


class Friction(Model):
    def __init__(self, ode: "Ode" = None):
        self.ode = ode

    def to_sdf(self) -> ET.Element:
        el = ET.Element("friction")
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Friction":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(ode=_ode)


class Dynamics(Model):
    def __init__(self, damping: "Damping" = None, friction: "Friction" = None):
        self.damping = damping
        self.friction = friction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dynamics")
        if self.damping is not None:
            el.append(self.damping.to_sdf())
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dynamics":
        _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping) if _c_damping is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        return cls(damping=_damping, friction=_friction)


class Lower(Model):
    def __init__(self, lower: float = -1e16):
        self.lower = lower

    def to_sdf(self) -> ET.Element:
        el = ET.Element("lower")
        if self.lower is not None:
            el.text = str(self.lower)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Lower":
        _text = el.text or -1e16
        _lower = _parse_double(_text)
        return cls(lower=_lower)


class Upper(Model):
    def __init__(self, upper: float = 1e16):
        self.upper = upper

    def to_sdf(self) -> ET.Element:
        el = ET.Element("upper")
        if self.upper is not None:
            el.text = str(self.upper)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Upper":
        _text = el.text or 1e16
        _upper = _parse_double(_text)
        return cls(upper=_upper)


class Effort(Model):
    def __init__(self, effort: float = -1):
        self.effort = effort

    def to_sdf(self) -> ET.Element:
        el = ET.Element("effort")
        if self.effort is not None:
            el.text = str(self.effort)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Effort":
        _text = el.text or -1
        _effort = _parse_double(_text)
        return cls(effort=_effort)


class Velocity(Model):
    def __init__(self, velocity: float = -1):
        self.velocity = velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = str(self.velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Velocity":
        _text = el.text or -1
        _velocity = _parse_double(_text)
        return cls(velocity=_velocity)


class Limit(Model):
    def __init__(
        self,
        lower: "Lower" = None,
        upper: "Upper" = None,
        effort: "Effort" = None,
        velocity: "Velocity" = None
    ):
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("limit")
        if self.lower is not None:
            el.append(self.lower.to_sdf())
        if self.upper is not None:
            el.append(self.upper.to_sdf())
        if self.effort is not None:
            el.append(self.effort.to_sdf())
        if self.velocity is not None:
            el.append(self.velocity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Limit":
        _c_lower = el.find("lower")
        _lower = Lower.from_sdf(_c_lower) if _c_lower is not None else None
        _c_upper = el.find("upper")
        _upper = Upper.from_sdf(_c_upper) if _c_upper is not None else None
        _c_effort = el.find("effort")
        _effort = Effort.from_sdf(_c_effort) if _c_effort is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity) if _c_velocity is not None else None
        return cls(lower=_lower, upper=_upper, effort=_effort, velocity=_velocity)


class Axis(Model):
    def __init__(self, xyz: "Xyz" = None, dynamics: "Dynamics" = None, limit: "Limit" = None):
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit

    def to_sdf(self) -> ET.Element:
        el = ET.Element("axis")
        if self.xyz is not None:
            el.append(self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf())
        if self.limit is not None:
            el.append(self.limit.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis":
        _c_xyz = el.find("xyz")
        _xyz = Xyz.from_sdf(_c_xyz) if _c_xyz is not None else None
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit) if _c_limit is not None else None
        return cls(xyz=_xyz, dynamics=_dynamics, limit=_limit)


class Axis2(Model):
    def __init__(self, xyz: "Xyz" = None, dynamics: "Dynamics" = None, limit: "Limit" = None):
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit

    def to_sdf(self) -> ET.Element:
        el = ET.Element("axis2")
        if self.xyz is not None:
            el.append(self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf())
        if self.limit is not None:
            el.append(self.limit.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis2":
        _c_xyz = el.find("xyz")
        _xyz = Xyz.from_sdf(_c_xyz) if _c_xyz is not None else None
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit) if _c_limit is not None else None
        return cls(xyz=_xyz, dynamics=_dynamics, limit=_limit)


class Joint(Model):
    def __init__(
        self,
        name: str = "__default__",
        type: str = "__default__",
        parent: "Parent" = None,
        child: "Child" = None,
        pose: "Pose" = None,
        thread_pitch: "ThreadPitch" = None,
        axis: "Axis" = None,
        axis2: "Axis2" = None,
        physics: "Physics" = None
    ):
        self.name = name
        self.type = type
        self.parent = parent
        self.child = child
        self.pose = pose
        self.thread_pitch = thread_pitch
        self.axis = axis
        self.axis2 = axis2
        self.physics = physics

    def to_sdf(self) -> ET.Element:
        el = ET.Element("joint")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.parent is not None:
            el.append(self.parent.to_sdf())
        if self.child is not None:
            el.append(self.child.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.thread_pitch is not None:
            el.append(self.thread_pitch.to_sdf())
        if self.axis is not None:
            el.append(self.axis.to_sdf())
        if self.axis2 is not None:
            el.append(self.axis2.to_sdf())
        if self.physics is not None:
            el.append(self.physics.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Joint":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _c_parent = el.find("parent")
        _parent = Parent.from_sdf(_c_parent) if _c_parent is not None else None
        _c_child = el.find("child")
        _child = Child.from_sdf(_c_child) if _c_child is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_thread_pitch = el.find("thread_pitch")
        _thread_pitch = ThreadPitch.from_sdf(_c_thread_pitch) if _c_thread_pitch is not None else None
        _c_axis = el.find("axis")
        _axis = Axis.from_sdf(_c_axis) if _c_axis is not None else None
        _c_axis2 = el.find("axis2")
        _axis2 = Axis2.from_sdf(_c_axis2) if _c_axis2 is not None else None
        _c_physics = el.find("physics")
        _physics = Physics.from_sdf(_c_physics) if _c_physics is not None else None
        return cls(name=_name, type=_type, parent=_parent, child=_child, pose=_pose, thread_pitch=_thread_pitch, axis=_axis, axis2=_axis2, physics=_physics)


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
        return cls(name=_name, gui=_gui, physics=_physics, scene=_scene, light=_light, model=_model, actor=_actor, plugin=_plugin, joint=_joint, road=_road, state=_state)
