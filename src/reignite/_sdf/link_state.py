### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.pose import Pose

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


# noinspection PyUnusedImports
class LinkState(BaseModel):
    class AngularAcceleration(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            angular_acceleration: _Vector3T | None = None,
            degrees: bool | None = False
        ):
            super().__init__(sdf_version)
            self.angular_acceleration = _vector3("0 0 0") if angular_acceleration is None else _vector3(angular_acceleration)
            self.degrees = degrees if degrees is not None else False

        def to_version(self, target_version: str) -> "LinkState.AngularAcceleration":
            if self.angular_acceleration is not None and cmp_version(target_version, "1.12") < 0:
                raise ValueError(f"'angular_acceleration' is not supported in SDF version {target_version} (added in 1.12)")
            kwargs: dict = {"sdf_version": target_version, "angular_acceleration": self.angular_acceleration, "degrees": self.degrees}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
            if _angular_acceleration is not None and cmp_version(version, "1.12") < 0:
                if _angular_acceleration != "0 0 0":
                    return SDFError(f"'angular_acceleration' is not supported in SDF version {version} (added in 1.12)")
            _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
            if isinstance(_degrees, SDFError):
                return _degrees.extend("@degrees")
            return cls(sdf_version=version, angular_acceleration=_angular_acceleration, degrees=_degrees)

    class AngularVelocity(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            angular_velocity: _Vector3T | None = None,
            degrees: bool | None = False
        ):
            super().__init__(sdf_version)
            self.angular_velocity = _vector3("0 0 0") if angular_velocity is None else _vector3(angular_velocity)
            self.degrees = degrees if degrees is not None else False

        def to_version(self, target_version: str) -> "LinkState.AngularVelocity":
            if self.angular_velocity is not None and cmp_version(target_version, "1.12") < 0:
                raise ValueError(f"'angular_velocity' is not supported in SDF version {target_version} (added in 1.12)")
            kwargs: dict = {"sdf_version": target_version, "angular_velocity": self.angular_velocity, "degrees": self.degrees}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
            if _angular_velocity is not None and cmp_version(version, "1.12") < 0:
                if _angular_velocity != "0 0 0":
                    return SDFError(f"'angular_velocity' is not supported in SDF version {version} (added in 1.12)")
            _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
            if isinstance(_degrees, SDFError):
                return _degrees.extend("@degrees")
            return cls(sdf_version=version, angular_velocity=_angular_velocity, degrees=_degrees)

    class Collision(BaseModel):
        def __init__(self, sdf_version: str | None = None, name: str | None = "__default__"):
            super().__init__(sdf_version)
            self.name = name if name is not None else "__default__"

        def to_version(self, target_version: str) -> "LinkState.Collision":
            kwargs: dict = {"sdf_version": target_version, "name": self.name}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("collision")
            if self.name is not None:
                el.set("name", self.name)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "LinkState.Collision | SDFError":
            _name = el.get("name", "__default__")
            if isinstance(_name, SDFError):
                return _name.extend("@name")
            return cls(sdf_version=version, name=_name)

    class CollisionState(BaseModel):
        def __init__(self, sdf_version: str | None = None, name: str | None = "__default__"):
            super().__init__(sdf_version)
            self.name = name if name is not None else "__default__"

        def to_version(self, target_version: str) -> "LinkState.CollisionState":
            kwargs: dict = {"sdf_version": target_version, "name": self.name}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
        acceleration: _PoseT | None = None,
        angular_acceleration: "LinkState.AngularAcceleration" = None,
        angular_velocity: "LinkState.AngularVelocity" = None,
        collision_states: List["LinkState.CollisionState"] = None,
        collisions: List["LinkState.Collision"] = None,
        force: _Vector3T | None = None,
        frames: List["Frame"] = None,
        linear_acceleration: _Vector3T | None = None,
        linear_velocity: _Vector3T | None = None,
        name: str | None = "__default__",
        pose: "Pose" = None,
        torque: _Vector3T | None = None,
        velocity: _PoseT | None = None,
        wrench: _PoseT | None = None
    ):
        super().__init__(sdf_version)
        self.acceleration = _pose("0 0 0 0 0 0") if acceleration is None else _pose(acceleration)
        self.angular_acceleration = angular_acceleration
        self.angular_velocity = angular_velocity
        self.collision_states = collision_states or []
        self.collisions = collisions or []
        self.force = _vector3("0 0 0") if force is None else _vector3(force)
        self.frames = frames or []
        self.linear_acceleration = _vector3("0 0 0") if linear_acceleration is None else _vector3(linear_acceleration)
        self.linear_velocity = _vector3("0 0 0") if linear_velocity is None else _vector3(linear_velocity)
        self.name = name if name is not None else "__default__"
        self.pose = pose
        self.torque = _vector3("0 0 0") if torque is None else _vector3(torque)
        self.velocity = _pose("0 0 0 0 0 0") if velocity is None else _pose(velocity)
        self.wrench = _pose("0 0 0 0 0 0") if wrench is None else _pose(wrench)
        if self.angular_acceleration is not None and hasattr(self.angular_acceleration, 'to_version'):
            if getattr(self.angular_acceleration, 'sdfversion', None) is None:
                self.angular_acceleration.sdfversion = self.sdfversion
            elif getattr(self.angular_acceleration, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.angular_acceleration = self.angular_acceleration.to_version(self.sdfversion)
        if self.angular_velocity is not None and hasattr(self.angular_velocity, 'to_version'):
            if getattr(self.angular_velocity, 'sdfversion', None) is None:
                self.angular_velocity.sdfversion = self.sdfversion
            elif getattr(self.angular_velocity, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.angular_velocity = self.angular_velocity.to_version(self.sdfversion)
        for _i, _c in enumerate(self.collision_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.collision_states[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.collisions):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.collisions[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)

    def add_collision_state(self, *items: "LinkState.CollisionState"):
        if self.collision_states is None:
            self.collision_states = []
        self.collision_states.extend(items)

    def add_collision(self, *items: "LinkState.Collision"):
        if self.collisions is None:
            self.collisions = []
        self.collisions.extend(items)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def to_version(self, target_version: str) -> "LinkState":
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.angular_acceleration is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'angular_acceleration' is not supported in SDF version {target_version} (added in 1.12)")
        if self.angular_velocity is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'angular_velocity' is not supported in SDF version {target_version} (added in 1.12)")
        if self.collision_states is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'collision_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.collisions is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'collisions' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.force is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'force' is not supported in SDF version {target_version} (added in 1.12)")
        if self.frames is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.linear_acceleration is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'linear_acceleration' is not supported in SDF version {target_version} (added in 1.12)")
        if self.linear_velocity is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'linear_velocity' is not supported in SDF version {target_version} (added in 1.12)")
        if self.torque is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs: dict = {"sdf_version": target_version, "acceleration": self.acceleration, "angular_acceleration": self.angular_acceleration.to_version(target_version) if self.angular_acceleration is not None and hasattr(self.angular_acceleration, "to_version") else self.angular_acceleration, "angular_velocity": self.angular_velocity.to_version(target_version) if self.angular_velocity is not None and hasattr(self.angular_velocity, "to_version") else self.angular_velocity, "collision_states": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.collision_states or [])], "collisions": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.collisions or [])], "force": self.force, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "linear_acceleration": self.linear_acceleration, "linear_velocity": self.linear_velocity, "name": self.name, "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "torque": self.torque, "velocity": self.velocity, "wrench": self.wrench}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("link_state")
        if self.acceleration is not None:
            _c_tmp = ET.Element("acceleration")
            _c_tmp.text = str(self.acceleration)
            el.append(_c_tmp)
        if self.angular_acceleration is not None:
            _child_res = self.angular_acceleration.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('angular_acceleration')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.angular_velocity is not None:
            _child_res = self.angular_velocity.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('angular_velocity')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.collision_states or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('collision_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.collisions or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('collision')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.force is not None:
            _c_tmp = ET.Element("force")
            _c_tmp.text = str(self.force)
            el.append(_c_tmp)
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
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
            _child_res = self.pose.to_sdf(version)
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
        from ..elements.frame import Frame
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
        if _angular_acceleration is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'angular_acceleration' is not supported in SDF version {version} (added in 1.12)")
        _c_angular_velocity = el.find("angular_velocity")
        if _c_angular_velocity is not None:
            _res = cls.AngularVelocity._from_sdf(_c_angular_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_velocity")
            _angular_velocity = _res
        else:
            _angular_velocity = None
        if _angular_velocity is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'angular_velocity' is not supported in SDF version {version} (added in 1.12)")
        _collision_states = []
        for c in el.findall("collision_state"):
            _res = cls.CollisionState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision_state")
            _collision_states.append(_res)
        if _collision_states and cmp_version(version, "1.12") < 0:
            return SDFError(f"'collision_states' is not supported in SDF version {version} (added in 1.12)")
        _collisions = []
        for c in el.findall("collision"):
            _res = cls.Collision._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collisions.append(_res)
        _c_tmp = el.find("force")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("force")
            _force = _val
        else:
            _force = None
        if _force is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'force' is not supported in SDF version {version} (added in 1.12)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        _c_tmp = el.find("linear_acceleration")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("linear_acceleration")
            _linear_acceleration = _val
        else:
            _linear_acceleration = None
        if _linear_acceleration is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'linear_acceleration' is not supported in SDF version {version} (added in 1.12)")
        _c_tmp = el.find("linear_velocity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("linear_velocity")
            _linear_velocity = _val
        else:
            _linear_velocity = None
        if _linear_velocity is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'linear_velocity' is not supported in SDF version {version} (added in 1.12)")
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
        if _torque is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'torque' is not supported in SDF version {version} (added in 1.12)")
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
        return cls(sdf_version=version, acceleration=_acceleration, angular_acceleration=_angular_acceleration, angular_velocity=_angular_velocity, collision_states=_collision_states, collisions=_collisions, force=_force, frames=_frames, linear_acceleration=_linear_acceleration, linear_velocity=_linear_velocity, name=_name, pose=_pose, torque=_torque, velocity=_velocity, wrench=_wrench)
