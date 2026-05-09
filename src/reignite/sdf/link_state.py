### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.migration import apply_migrations


class Acceleration(BaseModel):
    def __init__(self, sdf_version: str, acceleration: _SDFPose = None):
        self.__version__ = sdf_version
        if acceleration is None:
            acceleration = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.acceleration = acceleration

    def to_version(self, target_version: str) -> "Acceleration":
        kwargs = {"sdf_version": target_version}
        kwargs["acceleration"] = self.acceleration
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("acceleration")
        if self.acceleration is not None:
            el.text = self.acceleration.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _acceleration = _SDFPose._from_sdf(_text, version)
        if isinstance(_acceleration, SDFError):
            return _acceleration
        return cls(sdf_version=version, acceleration=_acceleration)


class AngularAcceleration(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        angular_acceleration: _SDFVector3 = None,
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if angular_acceleration is None:
            angular_acceleration = _SDFVector3.from_sdf("0 0 0")
        self.angular_acceleration = angular_acceleration
        self.degrees = degrees

    def to_version(self, target_version: str) -> "AngularAcceleration":
        kwargs = {"sdf_version": target_version}
        kwargs["angular_acceleration"] = self.angular_acceleration
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angular_acceleration")
        if self.angular_acceleration is not None:
            el.text = self.angular_acceleration.to_sdf()
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _angular_acceleration = _SDFVector3._from_sdf(_text, version)
        if isinstance(_angular_acceleration, SDFError):
            return _angular_acceleration
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        return cls(sdf_version=version, angular_acceleration=_angular_acceleration, degrees=_degrees)


class AngularVelocity(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        angular_velocity: _SDFVector3 = None,
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if angular_velocity is None:
            angular_velocity = _SDFVector3.from_sdf("0 0 0")
        self.angular_velocity = angular_velocity
        self.degrees = degrees

    def to_version(self, target_version: str) -> "AngularVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["angular_velocity"] = self.angular_velocity
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angular_velocity")
        if self.angular_velocity is not None:
            el.text = self.angular_velocity.to_sdf()
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _angular_velocity = _SDFVector3._from_sdf(_text, version)
        if isinstance(_angular_velocity, SDFError):
            return _angular_velocity
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        return cls(sdf_version=version, angular_velocity=_angular_velocity, degrees=_degrees)


class CollisionState(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "CollisionState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision_state")
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, name=_name)


class Force(BaseModel):
    def __init__(self, sdf_version: str, force: _SDFVector3 = None):
        self.__version__ = sdf_version
        if force is None:
            force = _SDFVector3.from_sdf("0 0 0")
        self.force = force

    def to_version(self, target_version: str) -> "Force":
        kwargs = {"sdf_version": target_version}
        kwargs["force"] = self.force
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("force")
        if self.force is not None:
            el.text = self.force.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _force = _SDFVector3._from_sdf(_text, version)
        if isinstance(_force, SDFError):
            return _force
        return cls(sdf_version=version, force=_force)


class LinearAcceleration(BaseModel):
    def __init__(self, sdf_version: str, linear_acceleration: _SDFVector3 = None):
        self.__version__ = sdf_version
        if linear_acceleration is None:
            linear_acceleration = _SDFVector3.from_sdf("0 0 0")
        self.linear_acceleration = linear_acceleration

    def to_version(self, target_version: str) -> "LinearAcceleration":
        kwargs = {"sdf_version": target_version}
        kwargs["linear_acceleration"] = self.linear_acceleration
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear_acceleration")
        if self.linear_acceleration is not None:
            el.text = self.linear_acceleration.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _linear_acceleration = _SDFVector3._from_sdf(_text, version)
        if isinstance(_linear_acceleration, SDFError):
            return _linear_acceleration
        return cls(sdf_version=version, linear_acceleration=_linear_acceleration)


class LinearVelocity(BaseModel):
    def __init__(self, sdf_version: str, linear_velocity: _SDFVector3 = None):
        self.__version__ = sdf_version
        if linear_velocity is None:
            linear_velocity = _SDFVector3.from_sdf("0 0 0")
        self.linear_velocity = linear_velocity

    def to_version(self, target_version: str) -> "LinearVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["linear_velocity"] = self.linear_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear_velocity")
        if self.linear_velocity is not None:
            el.text = self.linear_velocity.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _linear_velocity = _SDFVector3._from_sdf(_text, version)
        if isinstance(_linear_velocity, SDFError):
            return _linear_velocity
        return cls(sdf_version=version, linear_velocity=_linear_velocity)


class LinkState(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        acceleration: "Acceleration" = None,
        angular_acceleration: "AngularAcceleration" = None,
        angular_velocity: "AngularVelocity" = None,
        collision_state: List["CollisionState"] = None,
        force: "Force" = None,
        linear_acceleration: "LinearAcceleration" = None,
        linear_velocity: "LinearVelocity" = None,
        name: str = "__default__",
        pose: "Pose" = None,
        torque: "Torque" = None,
        velocity: "Velocity" = None,
        wrench: "Wrench" = None
    ):
        self.__version__ = sdf_version
        self.acceleration = acceleration
        self.angular_acceleration = angular_acceleration
        self.angular_velocity = angular_velocity
        self.collision_state = collision_state or []
        self.force = force
        self.linear_acceleration = linear_acceleration
        self.linear_velocity = linear_velocity
        self.name = name
        self.pose = pose
        self.torque = torque
        self.velocity = velocity
        self.wrench = wrench

    def to_version(self, target_version: str) -> "LinkState":
        kwargs = {"sdf_version": target_version}
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["angular_acceleration"] = self.angular_acceleration.to_version(target_version) if self.angular_acceleration is not None else None
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if self.angular_velocity is not None else None
        kwargs["collision_state"] = [c.to_version(target_version) for c in (self.collision_state or [])]
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
        kwargs["linear_acceleration"] = self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None else None
        kwargs["linear_velocity"] = self.linear_velocity.to_version(target_version) if self.linear_velocity is not None else None
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["wrench"] = self.wrench.to_version(target_version) if self.wrench is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("link_state")
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        if self.angular_acceleration is not None:
            el.append(self.angular_acceleration.to_sdf(version))
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
        for item in (self.collision_state or []):
            el.append(item.to_sdf(version))
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf(version))
        if self.linear_velocity is not None:
            el.append(self.linear_velocity.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.wrench is not None:
            el.append(self.wrench.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_acceleration = el.find("acceleration")
        if _c_acceleration is not None:
            _res = Acceleration._from_sdf(_c_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("acceleration")
            _acceleration = _res
        else:
            _acceleration = None
        _c_angular_acceleration = el.find("angular_acceleration")
        if _c_angular_acceleration is not None:
            _res = AngularAcceleration._from_sdf(_c_angular_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_acceleration")
            _angular_acceleration = _res
        else:
            _angular_acceleration = None
        _c_angular_velocity = el.find("angular_velocity")
        if _c_angular_velocity is not None:
            _res = AngularVelocity._from_sdf(_c_angular_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_velocity")
            _angular_velocity = _res
        else:
            _angular_velocity = None
        _collision_state = []
        for c in el.findall("collision_state"):
            _res = CollisionState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision_state")
            _collision_state.append(_res)
        _c_force = el.find("force")
        if _c_force is not None:
            _res = Force._from_sdf(_c_force, version)
            if isinstance(_res, SDFError):
                return _res.extend("force")
            _force = _res
        else:
            _force = None
        _c_linear_acceleration = el.find("linear_acceleration")
        if _c_linear_acceleration is not None:
            _res = LinearAcceleration._from_sdf(_c_linear_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_acceleration")
            _linear_acceleration = _res
        else:
            _linear_acceleration = None
        _c_linear_velocity = el.find("linear_velocity")
        if _c_linear_velocity is not None:
            _res = LinearVelocity._from_sdf(_c_linear_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_velocity")
            _linear_velocity = _res
        else:
            _linear_velocity = None
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_torque = el.find("torque")
        if _c_torque is not None:
            _res = Torque._from_sdf(_c_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("torque")
            _torque = _res
        else:
            _torque = None
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        _c_wrench = el.find("wrench")
        if _c_wrench is not None:
            _res = Wrench._from_sdf(_c_wrench, version)
            if isinstance(_res, SDFError):
                return _res.extend("wrench")
            _wrench = _res
        else:
            _wrench = None
        return cls(sdf_version=version, acceleration=_acceleration, angular_acceleration=_angular_acceleration, angular_velocity=_angular_velocity, collision_state=_collision_state, force=_force, linear_acceleration=_linear_acceleration, linear_velocity=_linear_velocity, name=_name, pose=_pose, torque=_torque, velocity=_velocity, wrench=_wrench)


class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        degrees: bool = False,
        pose: _SDFPose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy"
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.degrees = degrees
        self.pose = pose
        self.relative_to = relative_to
        self.rotation_format = rotation_format

    def to_version(self, target_version: str) -> "Pose":
        kwargs = {"sdf_version": target_version}
        kwargs["degrees"] = self.degrees
        kwargs["pose"] = self.pose
        kwargs["relative_to"] = self.relative_to
        kwargs["rotation_format"] = self.rotation_format
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        return cls(sdf_version=version, degrees=_degrees, pose=_pose, relative_to=_relative_to, rotation_format=_rotation_format)


class Torque(BaseModel):
    def __init__(self, sdf_version: str, torque: _SDFVector3 = None):
        self.__version__ = sdf_version
        if torque is None:
            torque = _SDFVector3.from_sdf("0 0 0")
        self.torque = torque

    def to_version(self, target_version: str) -> "Torque":
        kwargs = {"sdf_version": target_version}
        kwargs["torque"] = self.torque
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("torque")
        if self.torque is not None:
            el.text = self.torque.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _torque = _SDFVector3._from_sdf(_text, version)
        if isinstance(_torque, SDFError):
            return _torque
        return cls(sdf_version=version, torque=_torque)


class Velocity(BaseModel):
    def __init__(self, sdf_version: str, velocity: _SDFPose = None):
        self.__version__ = sdf_version
        if velocity is None:
            velocity = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Velocity":
        kwargs = {"sdf_version": target_version}
        kwargs["velocity"] = self.velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = self.velocity.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _velocity = _SDFPose._from_sdf(_text, version)
        if isinstance(_velocity, SDFError):
            return _velocity
        return cls(sdf_version=version, velocity=_velocity)


class Wrench(BaseModel):
    def __init__(self, sdf_version: str, wrench: _SDFPose = None):
        self.__version__ = sdf_version
        if wrench is None:
            wrench = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.wrench = wrench

    def to_version(self, target_version: str) -> "Wrench":
        kwargs = {"sdf_version": target_version}
        kwargs["wrench"] = self.wrench
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("wrench")
        if self.wrench is not None:
            el.text = self.wrench.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _wrench = _SDFPose._from_sdf(_text, version)
        if isinstance(_wrench, SDFError):
            return _wrench
        return cls(sdf_version=version, wrench=_wrench)
