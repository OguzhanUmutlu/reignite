from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ....utils.pose import Pose
from ....utils.vector3 import Vector3
from .linear_velocity import LinearVelocity
from .angular_acceleration import AngularAcceleration
from .acceleration import Acceleration
from .wrench import Wrench
from .collision_state import CollisionState


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



class Pose(Model):
    def __init__(
        self,
        pose: Pose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        _relative_to = el.get("relative_to", "")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(pose=_pose, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class AngularVelocity(Model):
    def __init__(self, angular_velocity: Vector3 = None, degrees: bool = False):
        if angular_velocity is None:
            angular_velocity = Vector3.from_sdf("0 0 0")
        self.angular_velocity = angular_velocity
        self.degrees = degrees

    def to_sdf(self) -> ET.Element:
        el = ET.Element("angular_velocity")
        if self.angular_velocity is not None:
            el.text = self.angular_velocity.to_sdf()
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AngularVelocity":
        _text = el.text or "0 0 0"
        _angular_velocity = Vector3.from_sdf(_text)
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(angular_velocity=_angular_velocity, degrees=_degrees)


class Velocity(Model):
    def __init__(self, velocity: float = 0, degrees: bool = False):
        self.velocity = velocity
        self.degrees = degrees

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = str(self.velocity)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Velocity":
        _text = el.text or 0
        _velocity = _parse_double(_text)
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(velocity=_velocity, degrees=_degrees)


class LinearAcceleration(Model):
    def __init__(self, linear_acceleration: Vector3 = None):
        if linear_acceleration is None:
            linear_acceleration = Vector3.from_sdf("0 0 0")
        self.linear_acceleration = linear_acceleration

    def to_sdf(self) -> ET.Element:
        el = ET.Element("linear_acceleration")
        if self.linear_acceleration is not None:
            el.text = self.linear_acceleration.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LinearAcceleration":
        _text = el.text or "0 0 0"
        _linear_acceleration = Vector3.from_sdf(_text)
        return cls(linear_acceleration=_linear_acceleration)


class Torque(Model):
    def __init__(self, torque: Vector3 = None):
        if torque is None:
            torque = Vector3.from_sdf("0 0 0")
        self.torque = torque

    def to_sdf(self) -> ET.Element:
        el = ET.Element("torque")
        if self.torque is not None:
            el.text = self.torque.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Torque":
        _text = el.text or "0 0 0"
        _torque = Vector3.from_sdf(_text)
        return cls(torque=_torque)


class Force(Model):
    def __init__(self, force: Vector3 = None):
        if force is None:
            force = Vector3.from_sdf("0 0 0")
        self.force = force

    def to_sdf(self) -> ET.Element:
        el = ET.Element("force")
        if self.force is not None:
            el.text = self.force.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Force":
        _text = el.text or "0 0 0"
        _force = Vector3.from_sdf(_text)
        return cls(force=_force)


class LinkState(Model):
    def __init__(
        self,
        name: str = "__default__",
        pose: "Pose" = None,
        angular_velocity: "AngularVelocity" = None,
        linear_velocity: "LinearVelocity" = None,
        velocity: "Velocity" = None,
        angular_acceleration: "AngularAcceleration" = None,
        linear_acceleration: "LinearAcceleration" = None,
        acceleration: "Acceleration" = None,
        torque: "Torque" = None,
        force: "Force" = None,
        wrench: "Wrench" = None,
        collision_state: List["CollisionState"] = None
    ):
        self.name = name
        self.pose = pose
        self.angular_velocity = angular_velocity
        self.linear_velocity = linear_velocity
        self.velocity = velocity
        self.angular_acceleration = angular_acceleration
        self.linear_acceleration = linear_acceleration
        self.acceleration = acceleration
        self.torque = torque
        self.force = force
        self.wrench = wrench
        self.collision_state = collision_state or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("link_state")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf())
        if self.linear_velocity is not None:
            el.append(self.linear_velocity.to_sdf())
        if self.velocity is not None:
            el.append(self.velocity.to_sdf())
        if self.angular_acceleration is not None:
            el.append(self.angular_acceleration.to_sdf())
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf())
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf())
        if self.torque is not None:
            el.append(self.torque.to_sdf())
        if self.force is not None:
            el.append(self.force.to_sdf())
        if self.wrench is not None:
            el.append(self.wrench.to_sdf())
        for item in (self.collision_state or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LinkState":
        _name = el.get("name", "__default__")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_angular_velocity = el.find("angular_velocity")
        _angular_velocity = AngularVelocity.from_sdf(_c_angular_velocity) if _c_angular_velocity is not None else None
        _c_linear_velocity = el.find("linear_velocity")
        _linear_velocity = LinearVelocity.from_sdf(_c_linear_velocity) if _c_linear_velocity is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity) if _c_velocity is not None else None
        _c_angular_acceleration = el.find("angular_acceleration")
        _angular_acceleration = AngularAcceleration.from_sdf(_c_angular_acceleration) if _c_angular_acceleration is not None else None
        _c_linear_acceleration = el.find("linear_acceleration")
        _linear_acceleration = LinearAcceleration.from_sdf(_c_linear_acceleration) if _c_linear_acceleration is not None else None
        _c_acceleration = el.find("acceleration")
        _acceleration = Acceleration.from_sdf(_c_acceleration) if _c_acceleration is not None else None
        _c_torque = el.find("torque")
        _torque = Torque.from_sdf(_c_torque) if _c_torque is not None else None
        _c_force = el.find("force")
        _force = Force.from_sdf(_c_force) if _c_force is not None else None
        _c_wrench = el.find("wrench")
        _wrench = Wrench.from_sdf(_c_wrench) if _c_wrench is not None else None
        _collision_state = [CollisionState.from_sdf(c) for c in el.findall("collision_state")]
        return cls(name=_name, pose=_pose, angular_velocity=_angular_velocity, linear_velocity=_linear_velocity, velocity=_velocity, angular_acceleration=_angular_acceleration, linear_acceleration=_linear_acceleration, acceleration=_acceleration, torque=_torque, force=_force, wrench=_wrench, collision_state=_collision_state)
