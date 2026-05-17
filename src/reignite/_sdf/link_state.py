### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose, _PoseT, _pose
from ..utils.vector3 import Vector3 as _SDFVector3, _Vector3T, _vector3

if typing.TYPE_CHECKING:
    from ..elements.pose import Pose


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")


def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


class LinkState(BaseModel):
    class AngularAcceleration(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            angular_acceleration: _Vector3T = None,
            degrees: bool = False
        ):
            super().__init__(sdf_version)
            if angular_acceleration is None:
                angular_acceleration = _vector3("0 0 0")
            else:
                angular_acceleration = _vector3(angular_acceleration)
            self.angular_acceleration = angular_acceleration
            self.degrees = degrees

        def to_version(self, target_version: str) -> "LinkState.AngularAcceleration":
            kwargs = {"sdf_version": target_version}
            kwargs["angular_acceleration"] = self.angular_acceleration
            kwargs["degrees"] = self.degrees
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("angular_acceleration")
            if self.angular_acceleration is not None:
                el.text = str(self.angular_acceleration)
            if self.degrees is not None:
                el.set("degrees", str(self.degrees).lower())
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "LinkState.AngularAcceleration | SDFError":
            _text = el.text or "0 0 0"
            _angular_acceleration = _parse_vector3(_text)
            if isinstance(_angular_acceleration, SDFError):
                return _angular_acceleration
            _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
            if isinstance(_degrees, SDFError):
                return _degrees.extend("@degrees")
            return cls(sdf_version=version, angular_acceleration=_angular_acceleration, degrees=_degrees)

    class AngularVelocity(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            angular_velocity: _Vector3T = None,
            degrees: bool = False
        ):
            super().__init__(sdf_version)
            if angular_velocity is None:
                angular_velocity = _vector3("0 0 0")
            else:
                angular_velocity = _vector3(angular_velocity)
            self.angular_velocity = angular_velocity
            self.degrees = degrees

        def to_version(self, target_version: str) -> "LinkState.AngularVelocity":
            kwargs = {"sdf_version": target_version}
            kwargs["angular_velocity"] = self.angular_velocity
            kwargs["degrees"] = self.degrees
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("angular_velocity")
            if self.angular_velocity is not None:
                el.text = str(self.angular_velocity)
            if self.degrees is not None:
                el.set("degrees", str(self.degrees).lower())
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "LinkState.AngularVelocity | SDFError":
            _text = el.text or "0 0 0"
            _angular_velocity = _parse_vector3(_text)
            if isinstance(_angular_velocity, SDFError):
                return _angular_velocity
            _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
            if isinstance(_degrees, SDFError):
                return _degrees.extend("@degrees")
            return cls(sdf_version=version, angular_velocity=_angular_velocity, degrees=_degrees)

    class CollisionState(BaseModel):
        def __init__(self, sdf_version: str | None = None, name: str = "__default__"):
            super().__init__(sdf_version)
            self.name = name

        def to_version(self, target_version: str) -> "LinkState.CollisionState":
            kwargs = {"sdf_version": target_version}
            kwargs["name"] = self.name
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("collision_state")
            if self.name is not None:
                el.set("name", self.name)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "LinkState.CollisionState | SDFError":
            _name = el.get("name", "__default__")
            if isinstance(_name, SDFError):
                return _name.extend("@name")
            return cls(sdf_version=version, name=_name)

    def __init__(
        self,
        sdf_version: str | None = None,
        acceleration: _PoseT = None,
        angular_acceleration: "LinkState.AngularAcceleration" = None,
        angular_velocity: "LinkState.AngularVelocity" = None,
        collision_states: List["LinkState.CollisionState"] = None,
        force: _Vector3T = None,
        linear_acceleration: _Vector3T = None,
        linear_velocity: _Vector3T = None,
        name: str = "__default__",
        pose: "Pose" = None,
        torque: _Vector3T = None,
        velocity: _PoseT = None,
        wrench: _PoseT = None
    ):
        super().__init__(sdf_version)
        if acceleration is None:
            acceleration = _pose("0 0 0 0 0 0")
        else:
            acceleration = _pose(acceleration)
        if force is None:
            force = _vector3("0 0 0")
        else:
            force = _vector3(force)
        if linear_acceleration is None:
            linear_acceleration = _vector3("0 0 0")
        else:
            linear_acceleration = _vector3(linear_acceleration)
        if linear_velocity is None:
            linear_velocity = _vector3("0 0 0")
        else:
            linear_velocity = _vector3(linear_velocity)
        if torque is None:
            torque = _vector3("0 0 0")
        else:
            torque = _vector3(torque)
        if velocity is None:
            velocity = _pose("0 0 0 0 0 0")
        else:
            velocity = _pose(velocity)
        if wrench is None:
            wrench = _pose("0 0 0 0 0 0")
        else:
            wrench = _pose(wrench)
        self.acceleration = acceleration
        self.angular_acceleration = angular_acceleration
        self.angular_velocity = angular_velocity
        self.collision_states = collision_states or []
        self.force = force
        self.linear_acceleration = linear_acceleration
        self.linear_velocity = linear_velocity
        self.name = name
        self.pose = pose
        self.torque = torque
        self.velocity = velocity
        self.wrench = wrench
        if self.angular_acceleration is not None and hasattr(self.angular_acceleration, 'to_version'):
            if getattr(self.angular_acceleration, '__version__', None) is None:
                self.angular_acceleration.__version__ = self.__version__
            elif getattr(self.angular_acceleration, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.angular_acceleration = self.angular_acceleration.to_version(self.__version__)
        if self.angular_velocity is not None and hasattr(self.angular_velocity, 'to_version'):
            if getattr(self.angular_velocity, '__version__', None) is None:
                self.angular_velocity.__version__ = self.__version__
            elif getattr(self.angular_velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.angular_velocity = self.angular_velocity.to_version(self.__version__)
        for _i, _c in enumerate(self.collision_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.collision_states[_i] = _c.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def add_collision_state(self, *items: "LinkState.CollisionState"):
        if self.collision_states is None:
            self.collision_states = []
        self.collision_states.extend(items)

    def to_version(self, target_version: str) -> "LinkState":
        from ..elements.pose import Pose
        kwargs = {"sdf_version": target_version}
        kwargs["acceleration"] = self.acceleration
        kwargs["angular_acceleration"] = self.angular_acceleration.to_version(target_version) if hasattr(self.angular_acceleration, "to_version") else self.angular_acceleration
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if hasattr(self.angular_velocity, "to_version") else self.angular_velocity
        kwargs["collision_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.collision_states or [])]
        kwargs["force"] = self.force
        kwargs["linear_acceleration"] = self.linear_acceleration
        kwargs["linear_velocity"] = self.linear_velocity
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
        kwargs["torque"] = self.torque
        kwargs["velocity"] = self.velocity
        kwargs["wrench"] = self.wrench
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("link_state")
        if self.acceleration is not None:
            _c_tmp = ET.Element("acceleration")
            _c_tmp.text = str(self.acceleration)
            el.append(_c_tmp)
        if self.angular_acceleration is not None:
            if hasattr(self.angular_acceleration, 'to_sdf'):
                _child_res = self.angular_acceleration.to_sdf(version)
            else:
                _child_res = str(self.angular_acceleration)
            if isinstance(_child_res, str):
                _item_el = ET.Element('angular_acceleration')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.angular_velocity is not None:
            if hasattr(self.angular_velocity, 'to_sdf'):
                _child_res = self.angular_velocity.to_sdf(version)
            else:
                _child_res = str(self.angular_velocity)
            if isinstance(_child_res, str):
                _item_el = ET.Element('angular_velocity')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.collision_states or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('collision_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.force is not None:
            _c_tmp = ET.Element("force")
            _c_tmp.text = str(self.force)
            el.append(_c_tmp)
        if self.linear_acceleration is not None:
            _c_tmp = ET.Element("linear_acceleration")
            _c_tmp.text = str(self.linear_acceleration)
            el.append(_c_tmp)
        if self.linear_velocity is not None:
            _c_tmp = ET.Element("linear_velocity")
            _c_tmp.text = str(self.linear_velocity)
            el.append(_c_tmp)
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            if hasattr(self.pose, 'to_sdf'):
                _child_res = self.pose.to_sdf(version)
            else:
                _child_res = str(self.pose)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.torque is not None:
            _c_tmp = ET.Element("torque")
            _c_tmp.text = str(self.torque)
            el.append(_c_tmp)
        if self.velocity is not None:
            _c_tmp = ET.Element("velocity")
            _c_tmp.text = str(self.velocity)
            el.append(_c_tmp)
        if self.wrench is not None:
            _c_tmp = ET.Element("wrench")
            _c_tmp.text = str(self.wrench)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "LinkState | SDFError":
        from ..elements.pose import Pose
        _c_tmp = el.find("acceleration")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text)
            if isinstance(_val, SDFError):
                return _val.extend("acceleration")
            _acceleration = _val
        else:
            _acceleration = None
        _c_angular_acceleration = el.find("angular_acceleration")
        if _c_angular_acceleration is not None:
            _res = cls.AngularAcceleration._from_sdf(_c_angular_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_acceleration")
            _angular_acceleration = _res
        else:
            _angular_acceleration = None
        _c_angular_velocity = el.find("angular_velocity")
        if _c_angular_velocity is not None:
            _res = cls.AngularVelocity._from_sdf(_c_angular_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_velocity")
            _angular_velocity = _res
        else:
            _angular_velocity = None
        _collision_states = []
        for c in el.findall("collision_state"):
            _res = cls.CollisionState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision_state")
            _collision_states.append(_res)
        _c_tmp = el.find("force")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("force")
            _force = _val
        else:
            _force = None
        _c_tmp = el.find("linear_acceleration")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("linear_acceleration")
            _linear_acceleration = _val
        else:
            _linear_acceleration = None
        _c_tmp = el.find("linear_velocity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("linear_velocity")
            _linear_velocity = _val
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
        _c_tmp = el.find("torque")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("torque")
            _torque = _val
        else:
            _torque = None
        _c_tmp = el.find("velocity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text)
            if isinstance(_val, SDFError):
                return _val.extend("velocity")
            _velocity = _val
        else:
            _velocity = None
        _c_tmp = el.find("wrench")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text)
            if isinstance(_val, SDFError):
                return _val.extend("wrench")
            _wrench = _val
        else:
            _wrench = None
        return cls(sdf_version=version, acceleration=_acceleration, angular_acceleration=_angular_acceleration, angular_velocity=_angular_velocity, collision_states=_collision_states, force=_force, linear_acceleration=_linear_acceleration, linear_velocity=_linear_velocity, name=_name, pose=_pose, torque=_torque, velocity=_velocity, wrench=_wrench)
