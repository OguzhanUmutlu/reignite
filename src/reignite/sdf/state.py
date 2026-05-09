### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color
from ..utils.pose import Pose
from ..utils.vector3 import Vector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations


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



class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: Pose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Pose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
        kwargs["relative_to"] = self.relative_to
        kwargs["rotation_format"] = self.rotation_format
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if cmp_version(version, "1.11") < 0:
            if self.pose is None:
                raise ValueError(f"'pose' is required in SDF version {version}")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if cmp_version(version, "1.11") < 0:
            if el.text is None:
                return SDFError(f"'pose' is required in SDF version {version}")
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Velocity(BaseModel):
    def __init__(self, sdf_version: str, velocity: Pose = None):
        self.__version__ = sdf_version
        if velocity is None:
            velocity = Pose.from_sdf("0 0 0 0 0 0")
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
        _velocity = Pose._from_sdf(_text, version)
        if isinstance(_velocity, SDFError):
            return _velocity
        return cls(sdf_version=version, velocity=_velocity)


class Pos(BaseModel):
    def __init__(self, sdf_version: str, pos: Vector3 = None):
        self.__version__ = sdf_version
        if pos is None:
            pos = Vector3.from_sdf("0 0 0")
        self.pos = pos

    def to_version(self, target_version: str) -> "Pos":
        if self.pos is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'pos' is not supported in SDF version {target_version} (removed in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["pos"] = self.pos
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pos")
        if self.pos is not None:
            el.text = self.pos.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _pos = Vector3._from_sdf(_text, version)
        if isinstance(_pos, SDFError):
            return _pos
        return cls(sdf_version=version, pos=_pos)


class Mag(BaseModel):
    def __init__(self, sdf_version: str, mag: Pose = None):
        self.__version__ = sdf_version
        if mag is None:
            mag = Pose.from_sdf("0 0 0 0 0 0")
        self.mag = mag

    def to_version(self, target_version: str) -> "Mag":
        if self.mag is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'mag' is not supported in SDF version {target_version} (removed in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["mag"] = self.mag
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mag")
        if cmp_version(version, "1.3") < 0:
            if self.mag is None:
                raise ValueError(f"'mag' is required in SDF version {version}")
        if self.mag is not None:
            el.text = self.mag.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if cmp_version(version, "1.3") < 0:
            if el.text is None:
                return SDFError(f"'mag' is required in SDF version {version}")
        _text = el.text or "0 0 0 0 0 0"
        _mag = Pose._from_sdf(_text, version)
        if isinstance(_mag, SDFError):
            return _mag
        return cls(sdf_version=version, mag=_mag)


class Wrench(BaseModel):
    def __init__(self, sdf_version: str, pos: "Pos" = None, mag: "Mag" = None):
        self.__version__ = sdf_version
        self.pos = pos
        self.mag = mag

    def to_version(self, target_version: str) -> "Wrench":
        if self.pos is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'pos' is not supported in SDF version {target_version} (removed in 1.3)")
        if self.mag is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'mag' is not supported in SDF version {target_version} (removed in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["pos"] = self.pos.to_version(target_version) if self.pos is not None else None
        kwargs["mag"] = self.mag.to_version(target_version) if self.mag is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("wrench")
        if self.pos is not None:
            el.append(self.pos.to_sdf(version))
        if cmp_version(version, "1.3") < 0:
            if self.mag is None:
                raise ValueError(f"'mag' is required in SDF version {version}")
        if self.mag is not None:
            el.append(self.mag.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_pos = el.find("pos")
        if _c_pos is not None:
            _res = Pos._from_sdf(_c_pos, version)
            if isinstance(_res, SDFError):
                return _res.extend("pos")
            _pos = _res
        else:
            _pos = None
        _c_mag = el.find("mag")
        if _c_mag is not None:
            _res = Mag._from_sdf(_c_mag, version)
            if isinstance(_res, SDFError):
                return _res.extend("mag")
            _mag = _res
        else:
            _mag = None
        if cmp_version(version, "1.3") < 0:
            if _mag is None:
                return SDFError(f"'mag' is required in SDF version {version}")
        return cls(sdf_version=version, pos=_pos, mag=_mag)


class Acceleration(BaseModel):
    def __init__(self, sdf_version: str, acceleration: Pose = None):
        self.__version__ = sdf_version
        if acceleration is None:
            acceleration = Pose.from_sdf("0 0 0 0 0 0")
        self.acceleration = acceleration

    def to_version(self, target_version: str) -> "Acceleration":
        if self.acceleration is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {target_version} (added in 1.3)")
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
        _acceleration = Pose._from_sdf(_text, version)
        if isinstance(_acceleration, SDFError):
            return _acceleration
        if _acceleration is not None and cmp_version(version, "1.3") < 0:
            if _acceleration != "0 0 0 0 0 0":
                return SDFError(f"'acceleration' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, acceleration=_acceleration)


class Collision(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__", pose: "Pose" = None):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "Collision":
        if self.pose is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (removed in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if cmp_version(version, "1.5") < 0:
            if self.pose is None:
                raise ValueError(f"'pose' is required in SDF version {version}")
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
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
        if cmp_version(version, "1.5") < 0:
            if _pose is None:
                return SDFError(f"'pose' is required in SDF version {version}")
        return cls(sdf_version=version, name=_name, pose=_pose)


class Frame(BaseModel):
    def __init__(self, sdf_version: str, name: str = "", pose: "Pose" = None):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "Frame":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "")
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
        return cls(sdf_version=version, name=_name, pose=_pose)


class Link(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        pose: "Pose" = None,
        velocity: "Velocity" = None,
        wrench: List["Wrench"] = None,
        acceleration: "Acceleration" = None,
        collision: List["Collision"] = None,
        frame: List["Frame"] = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose
        self.velocity = velocity
        self.wrench = wrench or []
        self.acceleration = acceleration
        self.collision = collision or []
        self.frame = frame or []

    def to_version(self, target_version: str) -> "Link":
        if self.acceleration is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {target_version} (added in 1.3)")
        if self.collision is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'collision' is not supported in SDF version {target_version} (added in 1.3)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["wrench"] = [c.to_version(target_version) for c in (self.wrench or [])]
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["collision"] = [c.to_version(target_version) for c in (self.collision or [])]
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("link")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if cmp_version(version, "1.11") < 0:
            if self.pose is None:
                raise ValueError(f"'pose' is required in SDF version {version}")
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        for item in (self.wrench or []):
            el.append(item.to_sdf(version))
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        for item in (self.collision or []):
            el.append(item.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
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
        if cmp_version(version, "1.11") < 0:
            if _pose is None:
                return SDFError(f"'pose' is required in SDF version {version}")
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        _wrench = []
        for c in el.findall("wrench"):
            _res = Wrench._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("wrench")
            _wrench.append(_res)
        _c_acceleration = el.find("acceleration")
        if _c_acceleration is not None:
            _res = Acceleration._from_sdf(_c_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("acceleration")
            _acceleration = _res
        else:
            _acceleration = None
        if _acceleration is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'acceleration' is not supported in SDF version {version} (added in 1.3)")
        _collision = []
        for c in el.findall("collision"):
            _res = Collision._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collision.append(_res)
        if _collision and cmp_version(version, "1.3") < 0:
            return SDFError(f"'collision' is not supported in SDF version {version} (added in 1.3)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, name=_name, pose=_pose, velocity=_velocity, wrench=_wrench, acceleration=_acceleration, collision=_collision, frame=_frame)


class Angle(BaseModel):
    def __init__(self, sdf_version: str, angle: float = 0, axis: int = 0):
        self.__version__ = sdf_version
        self.angle = angle
        self.axis = axis

    def to_version(self, target_version: str) -> "Angle":
        kwargs = {"sdf_version": target_version}
        kwargs["angle"] = self.angle
        kwargs["axis"] = self.axis
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angle")
        if self.angle is None:
            raise ValueError(f"'angle' is required in SDF version {version}")
        if self.angle is not None:
            el.text = str(self.angle)
        if self.axis is None:
            raise ValueError(f"'axis' is required in SDF version {version}")
        if self.axis is not None:
            el.set("axis", str(self.axis))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'angle' is required in SDF version {version}")
        _text = el.text or 0
        _angle = _parse_double(_text)
        if isinstance(_angle, SDFError):
            return _angle
        if el.get("axis") is None:
            return SDFError(f"'axis' is required in SDF version {version}")
        _axis = _parse_uint32(el.get("axis", 0))
        if isinstance(_axis, SDFError):
            return _axis.extend("@axis")
        return cls(sdf_version=version, angle=_angle, axis=_axis)


class Joint(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__", angle: List["Angle"] = None):
        self.__version__ = sdf_version
        self.name = name
        self.angle = angle or []

    def to_version(self, target_version: str) -> "Joint":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["angle"] = [c.to_version(target_version) for c in (self.angle or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("joint")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if not self.angle:
            raise ValueError(f"'angle' is required in SDF version {version}")
        for item in (self.angle or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _angle = []
        for c in el.findall("angle"):
            _res = Angle._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("angle")
            _angle.append(_res)
        if not _angle:
            return SDFError(f"'angle' is required in SDF version {version}")
        return cls(sdf_version=version, name=_name, angle=_angle)


class Scale(BaseModel):
    def __init__(self, sdf_version: str, scale: Vector3 = None):
        self.__version__ = sdf_version
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        self.scale = scale

    def to_version(self, target_version: str) -> "Scale":
        if self.scale is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["scale"] = self.scale
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = self.scale.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _scale = Vector3._from_sdf(_text, version)
        if isinstance(_scale, SDFError):
            return _scale
        if _scale is not None and cmp_version(version, "1.6") < 0:
            if _scale != "1 1 1":
                return SDFError(f"'scale' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, scale=_scale)


class Model(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        pose: "Pose" = None,
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        model: List["Model"] = None,
        frame: List["Frame"] = None,
        scale: "Scale" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose
        self.link = link or []
        self.joint = joint or []
        self.model = model or []
        self.frame = frame or []
        self.scale = scale

    def to_version(self, target_version: str) -> "Model":
        if self.joint is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'joint' is not supported in SDF version {target_version} (added in 1.3)")
        if self.model is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'model' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.scale is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["link"] = [c.to_version(target_version) for c in (self.link or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("model")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if cmp_version(version, "1.11") < 0:
            if self.pose is None:
                raise ValueError(f"'pose' is required in SDF version {version}")
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        for item in (self.link or []):
            el.append(item.to_sdf(version))
        for item in (self.joint or []):
            el.append(item.to_sdf(version))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
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
        if cmp_version(version, "1.11") < 0:
            if _pose is None:
                return SDFError(f"'pose' is required in SDF version {version}")
        _link = []
        for c in el.findall("link"):
            _res = Link._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link")
            _link.append(_res)
        _joint = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joint.append(_res)
        if _joint and cmp_version(version, "1.3") < 0:
            return SDFError(f"'joint' is not supported in SDF version {version} (added in 1.3)")
        _model = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _model.append(_res)
        if _model and cmp_version(version, "1.5") < 0:
            return SDFError(f"'model' is not supported in SDF version {version} (added in 1.5)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_scale = el.find("scale")
        if _c_scale is not None:
            _res = Scale._from_sdf(_c_scale, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale")
            _scale = _res
        else:
            _scale = None
        if _scale is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'scale' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, name=_name, pose=_pose, link=_link, joint=_joint, model=_model, frame=_frame, scale=_scale)


class Time(BaseModel):
    def __init__(self, sdf_version: str, time: float = "0 0"):
        self.__version__ = sdf_version
        self.time = time

    def to_version(self, target_version: str) -> "Time":
        if self.time is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'time' is not supported in SDF version {target_version} (added in 1.2)")
        if self.time is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'time' is not supported in SDF version {target_version} (removed in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["time"] = self.time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("time")
        if self.time is not None:
            el.text = str(self.time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _time = _parse_double(_text)
        if isinstance(_time, SDFError):
            return _time
        if _time is not None and cmp_version(version, "1.2") < 0:
            if _time != "0 0":
                return SDFError(f"'time' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, time=_time)


class WallTime(BaseModel):
    def __init__(self, sdf_version: str, wall_time: float = "0 0"):
        self.__version__ = sdf_version
        self.wall_time = wall_time

    def to_version(self, target_version: str) -> "WallTime":
        if self.wall_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'wall_time' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["wall_time"] = self.wall_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("wall_time")
        if self.wall_time is not None:
            el.text = str(self.wall_time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _wall_time = _parse_double(_text)
        if isinstance(_wall_time, SDFError):
            return _wall_time
        if _wall_time is not None and cmp_version(version, "1.3") < 0:
            if _wall_time != "0 0":
                return SDFError(f"'wall_time' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, wall_time=_wall_time)


class Name(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "Name":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("name")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _text = el.text or "__default__"
        _name = _text
        if isinstance(_name, SDFError):
            return _name
        return cls(sdf_version=version, name=_name)


class Deletions(BaseModel):
    def __init__(self, sdf_version: str, name: List["Name"] = None):
        self.__version__ = sdf_version
        self.name = name or []

    def to_version(self, target_version: str) -> "Deletions":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = [c.to_version(target_version) for c in (self.name or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("deletions")
        if not self.name:
            raise ValueError(f"'name' is required in SDF version {version}")
        for item in (self.name or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = []
        for c in el.findall("name"):
            _res = Name._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _name.append(_res)
        if not _name:
            return SDFError(f"'name' is required in SDF version {version}")
        return cls(sdf_version=version, name=_name)


class RealTime(BaseModel):
    def __init__(self, sdf_version: str, real_time: float = "0 0"):
        self.__version__ = sdf_version
        self.real_time = real_time

    def to_version(self, target_version: str) -> "RealTime":
        if self.real_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'real_time' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["real_time"] = self.real_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("real_time")
        if self.real_time is not None:
            el.text = str(self.real_time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _real_time = _parse_double(_text)
        if isinstance(_real_time, SDFError):
            return _real_time
        if _real_time is not None and cmp_version(version, "1.3") < 0:
            if _real_time != "0 0":
                return SDFError(f"'real_time' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, real_time=_real_time)


class CastShadows(BaseModel):
    def __init__(self, sdf_version: str, cast_shadows: bool = False):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows

    def to_version(self, target_version: str) -> "CastShadows":
        kwargs = {"sdf_version": target_version}
        kwargs["cast_shadows"] = self.cast_shadows
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cast_shadows")
        if self.cast_shadows is not None:
            el.text = str(self.cast_shadows).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _cast_shadows = str(_text).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows
        return cls(sdf_version=version, cast_shadows=_cast_shadows)


class Diffuse(BaseModel):
    def __init__(self, sdf_version: str, diffuse: Color = None):
        self.__version__ = sdf_version
        if diffuse is None:
            diffuse = Color.from_sdf("1 1 1 1")
        self.diffuse = diffuse

    def to_version(self, target_version: str) -> "Diffuse":
        kwargs = {"sdf_version": target_version}
        kwargs["diffuse"] = self.diffuse
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1 1"
        _diffuse = Color._from_sdf(_text, version)
        if isinstance(_diffuse, SDFError):
            return _diffuse
        return cls(sdf_version=version, diffuse=_diffuse)


class Specular(BaseModel):
    def __init__(self, sdf_version: str, specular: Color = None):
        self.__version__ = sdf_version
        if specular is None:
            specular = Color.from_sdf(".1 .1 .1 1")
        self.specular = specular

    def to_version(self, target_version: str) -> "Specular":
        kwargs = {"sdf_version": target_version}
        kwargs["specular"] = self.specular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular")
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ".1 .1 .1 1"
        _specular = Color._from_sdf(_text, version)
        if isinstance(_specular, SDFError):
            return _specular
        return cls(sdf_version=version, specular=_specular)


class Range(BaseModel):
    def __init__(self, sdf_version: str, range: float = 10):
        self.__version__ = sdf_version
        self.range = range

    def to_version(self, target_version: str) -> "Range":
        kwargs = {"sdf_version": target_version}
        kwargs["range"] = self.range
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.range is None:
            raise ValueError(f"'range' is required in SDF version {version}")
        if self.range is not None:
            el.text = str(self.range)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'range' is required in SDF version {version}")
        _text = el.text or 10
        _range = _parse_double(_text)
        if isinstance(_range, SDFError):
            return _range
        return cls(sdf_version=version, range=_range)


class Linear(BaseModel):
    def __init__(self, sdf_version: str, linear: float = 1):
        self.__version__ = sdf_version
        self.linear = linear

    def to_version(self, target_version: str) -> "Linear":
        kwargs = {"sdf_version": target_version}
        kwargs["linear"] = self.linear
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear")
        if self.linear is not None:
            el.text = str(self.linear)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _linear = _parse_double(_text)
        if isinstance(_linear, SDFError):
            return _linear
        return cls(sdf_version=version, linear=_linear)


class Constant(BaseModel):
    def __init__(self, sdf_version: str, constant: float = 1):
        self.__version__ = sdf_version
        self.constant = constant

    def to_version(self, target_version: str) -> "Constant":
        kwargs = {"sdf_version": target_version}
        kwargs["constant"] = self.constant
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("constant")
        if self.constant is not None:
            el.text = str(self.constant)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _constant = _parse_double(_text)
        if isinstance(_constant, SDFError):
            return _constant
        return cls(sdf_version=version, constant=_constant)


class Quadratic(BaseModel):
    def __init__(self, sdf_version: str, quadratic: float = 0):
        self.__version__ = sdf_version
        self.quadratic = quadratic

    def to_version(self, target_version: str) -> "Quadratic":
        kwargs = {"sdf_version": target_version}
        kwargs["quadratic"] = self.quadratic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("quadratic")
        if self.quadratic is not None:
            el.text = str(self.quadratic)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _quadratic = _parse_double(_text)
        if isinstance(_quadratic, SDFError):
            return _quadratic
        return cls(sdf_version=version, quadratic=_quadratic)


class Attenuation(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        range: "Range" = None,
        linear: "Linear" = None,
        constant: "Constant" = None,
        quadratic: "Quadratic" = None
    ):
        self.__version__ = sdf_version
        self.range = range
        self.linear = linear
        self.constant = constant
        self.quadratic = quadratic

    def to_version(self, target_version: str) -> "Attenuation":
        kwargs = {"sdf_version": target_version}
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["linear"] = self.linear.to_version(target_version) if self.linear is not None else None
        kwargs["constant"] = self.constant.to_version(target_version) if self.constant is not None else None
        kwargs["quadratic"] = self.quadratic.to_version(target_version) if self.quadratic is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("attenuation")
        if self.range is None:
            raise ValueError(f"'range' is required in SDF version {version}")
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.linear is not None:
            el.append(self.linear.to_sdf(version))
        if self.constant is not None:
            el.append(self.constant.to_sdf(version))
        if self.quadratic is not None:
            el.append(self.quadratic.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_range = el.find("range")
        if _c_range is not None:
            _res = Range._from_sdf(_c_range, version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        else:
            _range = None
        if _range is None:
            return SDFError(f"'range' is required in SDF version {version}")
        _c_linear = el.find("linear")
        if _c_linear is not None:
            _res = Linear._from_sdf(_c_linear, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear")
            _linear = _res
        else:
            _linear = None
        _c_constant = el.find("constant")
        if _c_constant is not None:
            _res = Constant._from_sdf(_c_constant, version)
            if isinstance(_res, SDFError):
                return _res.extend("constant")
            _constant = _res
        else:
            _constant = None
        _c_quadratic = el.find("quadratic")
        if _c_quadratic is not None:
            _res = Quadratic._from_sdf(_c_quadratic, version)
            if isinstance(_res, SDFError):
                return _res.extend("quadratic")
            _quadratic = _res
        else:
            _quadratic = None
        return cls(sdf_version=version, range=_range, linear=_linear, constant=_constant, quadratic=_quadratic)


class Direction(BaseModel):
    def __init__(self, sdf_version: str, direction: Vector3 = None):
        self.__version__ = sdf_version
        if direction is None:
            direction = Vector3.from_sdf("0 0 -1")
        self.direction = direction

    def to_version(self, target_version: str) -> "Direction":
        kwargs = {"sdf_version": target_version}
        kwargs["direction"] = self.direction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("direction")
        if self.direction is None:
            raise ValueError(f"'direction' is required in SDF version {version}")
        if self.direction is not None:
            el.text = self.direction.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'direction' is required in SDF version {version}")
        _text = el.text or "0 0 -1"
        _direction = Vector3._from_sdf(_text, version)
        if isinstance(_direction, SDFError):
            return _direction
        return cls(sdf_version=version, direction=_direction)


class InnerAngle(BaseModel):
    def __init__(self, sdf_version: str, inner_angle: float = 0):
        self.__version__ = sdf_version
        self.inner_angle = inner_angle

    def to_version(self, target_version: str) -> "InnerAngle":
        kwargs = {"sdf_version": target_version}
        kwargs["inner_angle"] = self.inner_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inner_angle")
        if self.inner_angle is None:
            raise ValueError(f"'inner_angle' is required in SDF version {version}")
        if self.inner_angle is not None:
            el.text = str(self.inner_angle)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'inner_angle' is required in SDF version {version}")
        _text = el.text or 0
        _inner_angle = _parse_double(_text)
        if isinstance(_inner_angle, SDFError):
            return _inner_angle
        return cls(sdf_version=version, inner_angle=_inner_angle)


class OuterAngle(BaseModel):
    def __init__(self, sdf_version: str, outer_angle: float = 0):
        self.__version__ = sdf_version
        self.outer_angle = outer_angle

    def to_version(self, target_version: str) -> "OuterAngle":
        kwargs = {"sdf_version": target_version}
        kwargs["outer_angle"] = self.outer_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("outer_angle")
        if self.outer_angle is None:
            raise ValueError(f"'outer_angle' is required in SDF version {version}")
        if self.outer_angle is not None:
            el.text = str(self.outer_angle)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'outer_angle' is required in SDF version {version}")
        _text = el.text or 0
        _outer_angle = _parse_double(_text)
        if isinstance(_outer_angle, SDFError):
            return _outer_angle
        return cls(sdf_version=version, outer_angle=_outer_angle)


class Falloff(BaseModel):
    def __init__(self, sdf_version: str, falloff: float = 0):
        self.__version__ = sdf_version
        self.falloff = falloff

    def to_version(self, target_version: str) -> "Falloff":
        kwargs = {"sdf_version": target_version}
        kwargs["falloff"] = self.falloff
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("falloff")
        if self.falloff is None:
            raise ValueError(f"'falloff' is required in SDF version {version}")
        if self.falloff is not None:
            el.text = str(self.falloff)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'falloff' is required in SDF version {version}")
        _text = el.text or 0
        _falloff = _parse_double(_text)
        if isinstance(_falloff, SDFError):
            return _falloff
        return cls(sdf_version=version, falloff=_falloff)


class Spot(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        inner_angle: "InnerAngle" = None,
        outer_angle: "OuterAngle" = None,
        falloff: "Falloff" = None
    ):
        self.__version__ = sdf_version
        self.inner_angle = inner_angle
        self.outer_angle = outer_angle
        self.falloff = falloff

    def to_version(self, target_version: str) -> "Spot":
        kwargs = {"sdf_version": target_version}
        kwargs["inner_angle"] = self.inner_angle.to_version(target_version) if self.inner_angle is not None else None
        kwargs["outer_angle"] = self.outer_angle.to_version(target_version) if self.outer_angle is not None else None
        kwargs["falloff"] = self.falloff.to_version(target_version) if self.falloff is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spot")
        if self.inner_angle is None:
            raise ValueError(f"'inner_angle' is required in SDF version {version}")
        if self.inner_angle is not None:
            el.append(self.inner_angle.to_sdf(version))
        if self.outer_angle is None:
            raise ValueError(f"'outer_angle' is required in SDF version {version}")
        if self.outer_angle is not None:
            el.append(self.outer_angle.to_sdf(version))
        if self.falloff is None:
            raise ValueError(f"'falloff' is required in SDF version {version}")
        if self.falloff is not None:
            el.append(self.falloff.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_inner_angle = el.find("inner_angle")
        if _c_inner_angle is not None:
            _res = InnerAngle._from_sdf(_c_inner_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("inner_angle")
            _inner_angle = _res
        else:
            _inner_angle = None
        if _inner_angle is None:
            return SDFError(f"'inner_angle' is required in SDF version {version}")
        _c_outer_angle = el.find("outer_angle")
        if _c_outer_angle is not None:
            _res = OuterAngle._from_sdf(_c_outer_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("outer_angle")
            _outer_angle = _res
        else:
            _outer_angle = None
        if _outer_angle is None:
            return SDFError(f"'outer_angle' is required in SDF version {version}")
        _c_falloff = el.find("falloff")
        if _c_falloff is not None:
            _res = Falloff._from_sdf(_c_falloff, version)
            if isinstance(_res, SDFError):
                return _res.extend("falloff")
            _falloff = _res
        else:
            _falloff = None
        if _falloff is None:
            return SDFError(f"'falloff' is required in SDF version {version}")
        return cls(sdf_version=version, inner_angle=_inner_angle, outer_angle=_outer_angle, falloff=_falloff)


class Intensity(BaseModel):
    def __init__(self, sdf_version: str, intensity: float = 1):
        self.__version__ = sdf_version
        self.intensity = intensity

    def to_version(self, target_version: str) -> "Intensity":
        if self.intensity is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.8)")
        kwargs = {"sdf_version": target_version}
        kwargs["intensity"] = self.intensity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("intensity")
        if self.intensity is not None:
            el.text = str(self.intensity)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _intensity = _parse_double(_text)
        if isinstance(_intensity, SDFError):
            return _intensity
        if _intensity is not None and cmp_version(version, "1.8") < 0:
            if _intensity != 1:
                return SDFError(f"'intensity' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, intensity=_intensity)


class LightOn(BaseModel):
    def __init__(self, sdf_version: str, light_on: bool = True):
        self.__version__ = sdf_version
        self.light_on = light_on

    def to_version(self, target_version: str) -> "LightOn":
        if self.light_on is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.8)")
        kwargs = {"sdf_version": target_version}
        kwargs["light_on"] = self.light_on
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light_on")
        if self.light_on is not None:
            el.text = str(self.light_on).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _light_on = str(_text).strip().lower() == 'true'
        if isinstance(_light_on, SDFError):
            return _light_on
        if _light_on is not None and cmp_version(version, "1.8") < 0:
            if _light_on != True:
                return SDFError(f"'light_on' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, light_on=_light_on)


class Visualize(BaseModel):
    def __init__(self, sdf_version: str, visualize: bool = True):
        self.__version__ = sdf_version
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Visualize":
        if self.visualize is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.8)")
        kwargs = {"sdf_version": target_version}
        kwargs["visualize"] = self.visualize
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visualize")
        if self.visualize is not None:
            el.text = str(self.visualize).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _visualize = str(_text).strip().lower() == 'true'
        if isinstance(_visualize, SDFError):
            return _visualize
        if _visualize is not None and cmp_version(version, "1.8") < 0:
            if _visualize != True:
                return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, visualize=_visualize)


class Light(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "point",
        frame: List["Frame"] = None,
        pose: "Pose" = None,
        cast_shadows: "CastShadows" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        attenuation: "Attenuation" = None,
        direction: "Direction" = None,
        spot: "Spot" = None,
        intensity: "Intensity" = None,
        light_on: "LightOn" = None,
        visualize: "Visualize" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.frame = frame or []
        self.pose = pose
        self.cast_shadows = cast_shadows
        self.diffuse = diffuse
        self.specular = specular
        self.attenuation = attenuation
        self.direction = direction
        self.spot = spot
        self.intensity = intensity
        self.light_on = light_on
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Light":
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.intensity is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.8)")
        if self.light_on is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.8)")
        if self.visualize is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.8)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["cast_shadows"] = self.cast_shadows.to_version(target_version) if self.cast_shadows is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["attenuation"] = self.attenuation.to_version(target_version) if self.attenuation is not None else None
        kwargs["direction"] = self.direction.to_version(target_version) if self.direction is not None else None
        kwargs["spot"] = self.spot.to_version(target_version) if self.spot is not None else None
        kwargs["intensity"] = self.intensity.to_version(target_version) if self.intensity is not None else None
        kwargs["light_on"] = self.light_on.to_version(target_version) if self.light_on is not None else None
        kwargs["visualize"] = self.visualize.to_version(target_version) if self.visualize is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is None:
            raise ValueError(f"'type' is required in SDF version {version}")
        if self.type is not None:
            el.set("type", self.type)
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.cast_shadows is not None:
            el.append(self.cast_shadows.to_sdf(version))
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.specular is not None:
            el.append(self.specular.to_sdf(version))
        if self.attenuation is not None:
            el.append(self.attenuation.to_sdf(version))
        if self.direction is None:
            raise ValueError(f"'direction' is required in SDF version {version}")
        if self.direction is not None:
            el.append(self.direction.to_sdf(version))
        if self.spot is not None:
            el.append(self.spot.to_sdf(version))
        if self.intensity is not None:
            el.append(self.intensity.to_sdf(version))
        if self.light_on is not None:
            el.append(self.light_on.to_sdf(version))
        if self.visualize is not None:
            el.append(self.visualize.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        if el.get("type") is None:
            return SDFError(f"'type' is required in SDF version {version}")
        _type = el.get("type", "point")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_cast_shadows = el.find("cast_shadows")
        if _c_cast_shadows is not None:
            _res = CastShadows._from_sdf(_c_cast_shadows, version)
            if isinstance(_res, SDFError):
                return _res.extend("cast_shadows")
            _cast_shadows = _res
        else:
            _cast_shadows = None
        _c_diffuse = el.find("diffuse")
        if _c_diffuse is not None:
            _res = Diffuse._from_sdf(_c_diffuse, version)
            if isinstance(_res, SDFError):
                return _res.extend("diffuse")
            _diffuse = _res
        else:
            _diffuse = None
        _c_specular = el.find("specular")
        if _c_specular is not None:
            _res = Specular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        _c_attenuation = el.find("attenuation")
        if _c_attenuation is not None:
            _res = Attenuation._from_sdf(_c_attenuation, version)
            if isinstance(_res, SDFError):
                return _res.extend("attenuation")
            _attenuation = _res
        else:
            _attenuation = None
        _c_direction = el.find("direction")
        if _c_direction is not None:
            _res = Direction._from_sdf(_c_direction, version)
            if isinstance(_res, SDFError):
                return _res.extend("direction")
            _direction = _res
        else:
            _direction = None
        if _direction is None:
            return SDFError(f"'direction' is required in SDF version {version}")
        _c_spot = el.find("spot")
        if _c_spot is not None:
            _res = Spot._from_sdf(_c_spot, version)
            if isinstance(_res, SDFError):
                return _res.extend("spot")
            _spot = _res
        else:
            _spot = None
        _c_intensity = el.find("intensity")
        if _c_intensity is not None:
            _res = Intensity._from_sdf(_c_intensity, version)
            if isinstance(_res, SDFError):
                return _res.extend("intensity")
            _intensity = _res
        else:
            _intensity = None
        if _intensity is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'intensity' is not supported in SDF version {version} (added in 1.8)")
        _c_light_on = el.find("light_on")
        if _c_light_on is not None:
            _res = LightOn._from_sdf(_c_light_on, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_on")
            _light_on = _res
        else:
            _light_on = None
        if _light_on is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'light_on' is not supported in SDF version {version} (added in 1.8)")
        _c_visualize = el.find("visualize")
        if _c_visualize is not None:
            _res = Visualize._from_sdf(_c_visualize, version)
            if isinstance(_res, SDFError):
                return _res.extend("visualize")
            _visualize = _res
        else:
            _visualize = None
        if _visualize is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, name=_name, type=_type, frame=_frame, pose=_pose, cast_shadows=_cast_shadows, diffuse=_diffuse, specular=_specular, attenuation=_attenuation, direction=_direction, spot=_spot, intensity=_intensity, light_on=_light_on, visualize=_visualize)


class Insertions(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        model: List["Model"] = None,
        light: List["Light"] = None,
        joint: List["Joint"] = None
    ):
        self.__version__ = sdf_version
        self.model = model or []
        self.light = light or []
        self.joint = joint or []

    def to_version(self, target_version: str) -> "Insertions":
        if self.light is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'light' is not supported in SDF version {target_version} (added in 1.6)")
        if self.joint is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'joint' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("insertions")
        if not self.model:
            raise ValueError(f"'model' is required in SDF version {version}")
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        if cmp_version(version, "1.6") >= 0:
            if not self.light:
                raise ValueError(f"'light' is required in SDF version {version}")
        for item in (self.light or []):
            el.append(item.to_sdf(version))
        if cmp_version(version, "1.12") >= 0:
            if not self.joint:
                raise ValueError(f"'joint' is required in SDF version {version}")
        for item in (self.joint or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _model = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _model.append(_res)
        if not _model:
            return SDFError(f"'model' is required in SDF version {version}")
        _light = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _light.append(_res)
        if cmp_version(version, "1.6") >= 0:
            if not _light:
                return SDFError(f"'light' is required in SDF version {version}")
        if _light and cmp_version(version, "1.6") < 0:
            return SDFError(f"'light' is not supported in SDF version {version} (added in 1.6)")
        _joint = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joint.append(_res)
        if cmp_version(version, "1.12") >= 0:
            if not _joint:
                return SDFError(f"'joint' is required in SDF version {version}")
        if _joint and cmp_version(version, "1.12") < 0:
            return SDFError(f"'joint' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, model=_model, light=_light, joint=_joint)


class SimTime(BaseModel):
    def __init__(self, sdf_version: str, sim_time: float = "0 0"):
        self.__version__ = sdf_version
        self.sim_time = sim_time

    def to_version(self, target_version: str) -> "SimTime":
        if self.sim_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'sim_time' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["sim_time"] = self.sim_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sim_time")
        if self.sim_time is not None:
            el.text = str(self.sim_time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _sim_time = _parse_double(_text)
        if isinstance(_sim_time, SDFError):
            return _sim_time
        if _sim_time is not None and cmp_version(version, "1.3") < 0:
            if _sim_time != "0 0":
                return SDFError(f"'sim_time' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, sim_time=_sim_time)


class Iterations(BaseModel):
    def __init__(self, sdf_version: str, iterations: int = 0):
        self.__version__ = sdf_version
        self.iterations = iterations

    def to_version(self, target_version: str) -> "Iterations":
        if self.iterations is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'iterations' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["iterations"] = self.iterations
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("iterations")
        if cmp_version(version, "1.5") >= 0:
            if self.iterations is None:
                raise ValueError(f"'iterations' is required in SDF version {version}")
        if self.iterations is not None:
            el.text = str(self.iterations)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if cmp_version(version, "1.5") >= 0:
            if el.text is None:
                return SDFError(f"'iterations' is required in SDF version {version}")
        _text = el.text or 0
        _iterations = _parse_uint32(_text)
        if isinstance(_iterations, SDFError):
            return _iterations
        if _iterations is not None and cmp_version(version, "1.5") < 0:
            if _iterations != 0:
                return SDFError(f"'iterations' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, iterations=_iterations)


class Position(BaseModel):
    def __init__(self, sdf_version: str, position: float = 0, degrees: bool = False):
        self.__version__ = sdf_version
        self.position = position
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Position":
        kwargs = {"sdf_version": target_version}
        kwargs["position"] = self.position
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("position")
        if self.position is not None:
            el.text = str(self.position)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _position = _parse_double(_text)
        if isinstance(_position, SDFError):
            return _position
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        return cls(sdf_version=version, position=_position, degrees=_degrees)


class Effort(BaseModel):
    def __init__(self, sdf_version: str, effort: float = 0):
        self.__version__ = sdf_version
        self.effort = effort

    def to_version(self, target_version: str) -> "Effort":
        kwargs = {"sdf_version": target_version}
        kwargs["effort"] = self.effort
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("effort")
        if self.effort is not None:
            el.text = str(self.effort)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _effort = _parse_double(_text)
        if isinstance(_effort, SDFError):
            return _effort
        return cls(sdf_version=version, effort=_effort)


class AxisState(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        position: "Position" = None,
        velocity: "Velocity" = None,
        acceleration: "Acceleration" = None,
        effort: "Effort" = None
    ):
        self.__version__ = sdf_version
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.effort = effort

    def to_version(self, target_version: str) -> "AxisState":
        kwargs = {"sdf_version": target_version}
        kwargs["position"] = self.position.to_version(target_version) if self.position is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["effort"] = self.effort.to_version(target_version) if self.effort is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis_state")
        if self.position is not None:
            el.append(self.position.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        if self.effort is not None:
            el.append(self.effort.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_position = el.find("position")
        if _c_position is not None:
            _res = Position._from_sdf(_c_position, version)
            if isinstance(_res, SDFError):
                return _res.extend("position")
            _position = _res
        else:
            _position = None
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        _c_acceleration = el.find("acceleration")
        if _c_acceleration is not None:
            _res = Acceleration._from_sdf(_c_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("acceleration")
            _acceleration = _res
        else:
            _acceleration = None
        _c_effort = el.find("effort")
        if _c_effort is not None:
            _res = Effort._from_sdf(_c_effort, version)
            if isinstance(_res, SDFError):
                return _res.extend("effort")
            _effort = _res
        else:
            _effort = None
        return cls(sdf_version=version, position=_position, velocity=_velocity, acceleration=_acceleration, effort=_effort)


class Axis2State(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        position: "Position" = None,
        velocity: "Velocity" = None,
        acceleration: "Acceleration" = None,
        effort: "Effort" = None
    ):
        self.__version__ = sdf_version
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.effort = effort

    def to_version(self, target_version: str) -> "Axis2State":
        kwargs = {"sdf_version": target_version}
        kwargs["position"] = self.position.to_version(target_version) if self.position is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["effort"] = self.effort.to_version(target_version) if self.effort is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis2_state")
        if self.position is not None:
            el.append(self.position.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        if self.effort is not None:
            el.append(self.effort.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_position = el.find("position")
        if _c_position is not None:
            _res = Position._from_sdf(_c_position, version)
            if isinstance(_res, SDFError):
                return _res.extend("position")
            _position = _res
        else:
            _position = None
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        _c_acceleration = el.find("acceleration")
        if _c_acceleration is not None:
            _res = Acceleration._from_sdf(_c_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("acceleration")
            _acceleration = _res
        else:
            _acceleration = None
        _c_effort = el.find("effort")
        if _c_effort is not None:
            _res = Effort._from_sdf(_c_effort, version)
            if isinstance(_res, SDFError):
                return _res.extend("effort")
            _effort = _res
        else:
            _effort = None
        return cls(sdf_version=version, position=_position, velocity=_velocity, acceleration=_acceleration, effort=_effort)


class JointState(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        angle: "Angle" = None,
        axis_state: "AxisState" = None,
        axis2_state: "Axis2State" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.angle = angle
        self.axis_state = axis_state
        self.axis2_state = axis2_state

    def to_version(self, target_version: str) -> "JointState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["angle"] = self.angle.to_version(target_version) if self.angle is not None else None
        kwargs["axis_state"] = self.axis_state.to_version(target_version) if self.axis_state is not None else None
        kwargs["axis2_state"] = self.axis2_state.to_version(target_version) if self.axis2_state is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("joint_state")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.angle is not None:
            el.append(self.angle.to_sdf(version))
        if self.axis_state is not None:
            el.append(self.axis_state.to_sdf(version))
        if self.axis2_state is not None:
            el.append(self.axis2_state.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_angle = el.find("angle")
        if _c_angle is not None:
            _res = Angle._from_sdf(_c_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("angle")
            _angle = _res
        else:
            _angle = None
        _c_axis_state = el.find("axis_state")
        if _c_axis_state is not None:
            _res = AxisState._from_sdf(_c_axis_state, version)
            if isinstance(_res, SDFError):
                return _res.extend("axis_state")
            _axis_state = _res
        else:
            _axis_state = None
        _c_axis2_state = el.find("axis2_state")
        if _c_axis2_state is not None:
            _res = Axis2State._from_sdf(_c_axis2_state, version)
            if isinstance(_res, SDFError):
                return _res.extend("axis2_state")
            _axis2_state = _res
        else:
            _axis2_state = None
        return cls(sdf_version=version, name=_name, angle=_angle, axis_state=_axis_state, axis2_state=_axis2_state)


class AngularVelocity(BaseModel):
    def __init__(self, sdf_version: str, angular_velocity: Vector3 = None, degrees: bool = False):
        self.__version__ = sdf_version
        if angular_velocity is None:
            angular_velocity = Vector3.from_sdf("0 0 0")
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
        _angular_velocity = Vector3._from_sdf(_text, version)
        if isinstance(_angular_velocity, SDFError):
            return _angular_velocity
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        return cls(sdf_version=version, angular_velocity=_angular_velocity, degrees=_degrees)


class LinearVelocity(BaseModel):
    def __init__(self, sdf_version: str, linear_velocity: Vector3 = None):
        self.__version__ = sdf_version
        if linear_velocity is None:
            linear_velocity = Vector3.from_sdf("0 0 0")
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
        _linear_velocity = Vector3._from_sdf(_text, version)
        if isinstance(_linear_velocity, SDFError):
            return _linear_velocity
        return cls(sdf_version=version, linear_velocity=_linear_velocity)


class AngularAcceleration(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        angular_acceleration: Vector3 = None,
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if angular_acceleration is None:
            angular_acceleration = Vector3.from_sdf("0 0 0")
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
        _angular_acceleration = Vector3._from_sdf(_text, version)
        if isinstance(_angular_acceleration, SDFError):
            return _angular_acceleration
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        return cls(sdf_version=version, angular_acceleration=_angular_acceleration, degrees=_degrees)


class LinearAcceleration(BaseModel):
    def __init__(self, sdf_version: str, linear_acceleration: Vector3 = None):
        self.__version__ = sdf_version
        if linear_acceleration is None:
            linear_acceleration = Vector3.from_sdf("0 0 0")
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
        _linear_acceleration = Vector3._from_sdf(_text, version)
        if isinstance(_linear_acceleration, SDFError):
            return _linear_acceleration
        return cls(sdf_version=version, linear_acceleration=_linear_acceleration)


class Torque(BaseModel):
    def __init__(self, sdf_version: str, torque: Vector3 = None):
        self.__version__ = sdf_version
        if torque is None:
            torque = Vector3.from_sdf("0 0 0")
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
        _torque = Vector3._from_sdf(_text, version)
        if isinstance(_torque, SDFError):
            return _torque
        return cls(sdf_version=version, torque=_torque)


class Force(BaseModel):
    def __init__(self, sdf_version: str, force: Vector3 = None):
        self.__version__ = sdf_version
        if force is None:
            force = Vector3.from_sdf("0 0 0")
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
        _force = Vector3._from_sdf(_text, version)
        if isinstance(_force, SDFError):
            return _force
        return cls(sdf_version=version, force=_force)


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
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, name=_name)


class LinkState(BaseModel):
    def __init__(
        self,
        sdf_version: str,
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
        self.__version__ = sdf_version
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

    def to_version(self, target_version: str) -> "LinkState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if self.angular_velocity is not None else None
        kwargs["linear_velocity"] = self.linear_velocity.to_version(target_version) if self.linear_velocity is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["angular_acceleration"] = self.angular_acceleration.to_version(target_version) if self.angular_acceleration is not None else None
        kwargs["linear_acceleration"] = self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None else None
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
        kwargs["wrench"] = self.wrench.to_version(target_version) if self.wrench is not None else None
        kwargs["collision_state"] = [c.to_version(target_version) for c in (self.collision_state or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("link_state")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
        if self.linear_velocity is not None:
            el.append(self.linear_velocity.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.angular_acceleration is not None:
            el.append(self.angular_acceleration.to_sdf(version))
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf(version))
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        if self.wrench is not None:
            el.append(self.wrench.to_sdf(version))
        for item in (self.collision_state or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
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
        _c_angular_velocity = el.find("angular_velocity")
        if _c_angular_velocity is not None:
            _res = AngularVelocity._from_sdf(_c_angular_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_velocity")
            _angular_velocity = _res
        else:
            _angular_velocity = None
        _c_linear_velocity = el.find("linear_velocity")
        if _c_linear_velocity is not None:
            _res = LinearVelocity._from_sdf(_c_linear_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_velocity")
            _linear_velocity = _res
        else:
            _linear_velocity = None
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        _c_angular_acceleration = el.find("angular_acceleration")
        if _c_angular_acceleration is not None:
            _res = AngularAcceleration._from_sdf(_c_angular_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_acceleration")
            _angular_acceleration = _res
        else:
            _angular_acceleration = None
        _c_linear_acceleration = el.find("linear_acceleration")
        if _c_linear_acceleration is not None:
            _res = LinearAcceleration._from_sdf(_c_linear_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_acceleration")
            _linear_acceleration = _res
        else:
            _linear_acceleration = None
        _c_acceleration = el.find("acceleration")
        if _c_acceleration is not None:
            _res = Acceleration._from_sdf(_c_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("acceleration")
            _acceleration = _res
        else:
            _acceleration = None
        _c_torque = el.find("torque")
        if _c_torque is not None:
            _res = Torque._from_sdf(_c_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("torque")
            _torque = _res
        else:
            _torque = None
        _c_force = el.find("force")
        if _c_force is not None:
            _res = Force._from_sdf(_c_force, version)
            if isinstance(_res, SDFError):
                return _res.extend("force")
            _force = _res
        else:
            _force = None
        _c_wrench = el.find("wrench")
        if _c_wrench is not None:
            _res = Wrench._from_sdf(_c_wrench, version)
            if isinstance(_res, SDFError):
                return _res.extend("wrench")
            _wrench = _res
        else:
            _wrench = None
        _collision_state = []
        for c in el.findall("collision_state"):
            _res = CollisionState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision_state")
            _collision_state.append(_res)
        return cls(sdf_version=version, name=_name, pose=_pose, angular_velocity=_angular_velocity, linear_velocity=_linear_velocity, velocity=_velocity, angular_acceleration=_angular_acceleration, linear_acceleration=_linear_acceleration, acceleration=_acceleration, torque=_torque, force=_force, wrench=_wrench, collision_state=_collision_state)


class ModelState(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        joint_state: List["JointState"] = None,
        frame: List["Frame"] = None,
        pose: "Pose" = None,
        link_state: List["LinkState"] = None,
        model_state: List["ModelState"] = None,
        scale: "Scale" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.joint_state = joint_state or []
        self.frame = frame or []
        self.pose = pose
        self.link_state = link_state or []
        self.model_state = model_state or []
        self.scale = scale

    def to_version(self, target_version: str) -> "ModelState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["joint_state"] = [c.to_version(target_version) for c in (self.joint_state or [])]
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["link_state"] = [c.to_version(target_version) for c in (self.link_state or [])]
        kwargs["model_state"] = [c.to_version(target_version) for c in (self.model_state or [])]
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("model_state")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.joint_state or []):
            el.append(item.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        for item in (self.link_state or []):
            el.append(item.to_sdf(version))
        for item in (self.model_state or []):
            el.append(item.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _joint_state = []
        for c in el.findall("joint_state"):
            _res = JointState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint_state")
            _joint_state.append(_res)
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _link_state = []
        for c in el.findall("link_state"):
            _res = LinkState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link_state")
            _link_state.append(_res)
        _model_state = []
        for c in el.findall("model_state"):
            _res = ModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_state")
            _model_state.append(_res)
        _c_scale = el.find("scale")
        if _c_scale is not None:
            _res = Scale._from_sdf(_c_scale, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale")
            _scale = _res
        else:
            _scale = None
        return cls(sdf_version=version, name=_name, joint_state=_joint_state, frame=_frame, pose=_pose, link_state=_link_state, model_state=_model_state, scale=_scale)


class LightState(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__", pose: "Pose" = None):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "LightState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light_state")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
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
        return cls(sdf_version=version, name=_name, pose=_pose)


class State(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        world_name: str = "__default__",
        time: float = "0 0",
        model: List["Model"] = None,
        wall_time: "WallTime" = None,
        deletions: "Deletions" = None,
        real_time: "RealTime" = None,
        insertions: "Insertions" = None,
        sim_time: "SimTime" = None,
        iterations: "Iterations" = None,
        light: List["Light"] = None,
        model_state: List["ModelState"] = None,
        joint_state: List["JointState"] = None,
        light_state: List["LightState"] = None
    ):
        self.__version__ = sdf_version
        self.world_name = world_name
        self.time = time
        self.model = model or []
        self.wall_time = wall_time
        self.deletions = deletions
        self.real_time = real_time
        self.insertions = insertions
        self.sim_time = sim_time
        self.iterations = iterations
        self.light = light or []
        self.model_state = model_state or []
        self.joint_state = joint_state or []
        self.light_state = light_state or []

    def to_version(self, target_version: str) -> "State":
        if self.time is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'time' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.model is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'model' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.wall_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'wall_time' is not supported in SDF version {target_version} (added in 1.3)")
        if self.deletions is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'deletions' is not supported in SDF version {target_version} (added in 1.3)")
        if self.real_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'real_time' is not supported in SDF version {target_version} (added in 1.3)")
        if self.insertions is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'insertions' is not supported in SDF version {target_version} (added in 1.3)")
        if self.sim_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'sim_time' is not supported in SDF version {target_version} (added in 1.3)")
        if self.iterations is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'iterations' is not supported in SDF version {target_version} (added in 1.5)")
        if self.light is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'light' is not supported in SDF version {target_version} (added in 1.5)")
        if self.light is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'light' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.model_state is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_state' is not supported in SDF version {target_version} (added in 1.12)")
        if self.joint_state is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'joint_state' is not supported in SDF version {target_version} (added in 1.12)")
        if self.light_state is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'light_state' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["world_name"] = self.world_name
        kwargs["time"] = self.time
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["wall_time"] = self.wall_time.to_version(target_version) if self.wall_time is not None else None
        kwargs["deletions"] = self.deletions.to_version(target_version) if self.deletions is not None else None
        kwargs["real_time"] = self.real_time.to_version(target_version) if self.real_time is not None else None
        kwargs["insertions"] = self.insertions.to_version(target_version) if self.insertions is not None else None
        kwargs["sim_time"] = self.sim_time.to_version(target_version) if self.sim_time is not None else None
        kwargs["iterations"] = self.iterations.to_version(target_version) if self.iterations is not None else None
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        kwargs["model_state"] = [c.to_version(target_version) for c in (self.model_state or [])]
        kwargs["joint_state"] = [c.to_version(target_version) for c in (self.joint_state or [])]
        kwargs["light_state"] = [c.to_version(target_version) for c in (self.light_state or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("state")
        if self.world_name is None:
            raise ValueError(f"'world_name' is required in SDF version {version}")
        if self.world_name is not None:
            el.set("world_name", self.world_name)
        if self.time is not None:
            el.set("time", str(self.time))
        if cmp_version(version, "1.12") < 0 and cmp_version(version, "1.11") < 0:
            if not self.model:
                raise ValueError(f"'model' is required in SDF version {version}")
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        if self.wall_time is not None:
            el.append(self.wall_time.to_sdf(version))
        if self.deletions is not None:
            el.append(self.deletions.to_sdf(version))
        if self.real_time is not None:
            el.append(self.real_time.to_sdf(version))
        if self.insertions is not None:
            el.append(self.insertions.to_sdf(version))
        if self.sim_time is not None:
            el.append(self.sim_time.to_sdf(version))
        if cmp_version(version, "1.5") >= 0:
            if self.iterations is None:
                raise ValueError(f"'iterations' is required in SDF version {version}")
        if self.iterations is not None:
            el.append(self.iterations.to_sdf(version))
        for item in (self.light or []):
            el.append(item.to_sdf(version))
        for item in (self.model_state or []):
            el.append(item.to_sdf(version))
        for item in (self.joint_state or []):
            el.append(item.to_sdf(version))
        for item in (self.light_state or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("world_name") is None:
            return SDFError(f"'world_name' is required in SDF version {version}")
        _world_name = el.get("world_name", "__default__")
        if isinstance(_world_name, SDFError):
            return _world_name.extend("@world_name")
        _time = _parse_double(el.get("time", "0 0"))
        if isinstance(_time, SDFError):
            return _time.extend("@time")
        _model = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _model.append(_res)
        if cmp_version(version, "1.12") < 0 and cmp_version(version, "1.11") < 0:
            if not _model:
                return SDFError(f"'model' is required in SDF version {version}")
        _c_wall_time = el.find("wall_time")
        if _c_wall_time is not None:
            _res = WallTime._from_sdf(_c_wall_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("wall_time")
            _wall_time = _res
        else:
            _wall_time = None
        if _wall_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'wall_time' is not supported in SDF version {version} (added in 1.3)")
        _c_deletions = el.find("deletions")
        if _c_deletions is not None:
            _res = Deletions._from_sdf(_c_deletions, version)
            if isinstance(_res, SDFError):
                return _res.extend("deletions")
            _deletions = _res
        else:
            _deletions = None
        if _deletions is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'deletions' is not supported in SDF version {version} (added in 1.3)")
        _c_real_time = el.find("real_time")
        if _c_real_time is not None:
            _res = RealTime._from_sdf(_c_real_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("real_time")
            _real_time = _res
        else:
            _real_time = None
        if _real_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'real_time' is not supported in SDF version {version} (added in 1.3)")
        _c_insertions = el.find("insertions")
        if _c_insertions is not None:
            _res = Insertions._from_sdf(_c_insertions, version)
            if isinstance(_res, SDFError):
                return _res.extend("insertions")
            _insertions = _res
        else:
            _insertions = None
        if _insertions is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'insertions' is not supported in SDF version {version} (added in 1.3)")
        _c_sim_time = el.find("sim_time")
        if _c_sim_time is not None:
            _res = SimTime._from_sdf(_c_sim_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("sim_time")
            _sim_time = _res
        else:
            _sim_time = None
        if _sim_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'sim_time' is not supported in SDF version {version} (added in 1.3)")
        _c_iterations = el.find("iterations")
        if _c_iterations is not None:
            _res = Iterations._from_sdf(_c_iterations, version)
            if isinstance(_res, SDFError):
                return _res.extend("iterations")
            _iterations = _res
        else:
            _iterations = None
        if cmp_version(version, "1.5") >= 0:
            if _iterations is None:
                return SDFError(f"'iterations' is required in SDF version {version}")
        if _iterations is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'iterations' is not supported in SDF version {version} (added in 1.5)")
        _light = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _light.append(_res)
        if _light and cmp_version(version, "1.5") < 0:
            return SDFError(f"'light' is not supported in SDF version {version} (added in 1.5)")
        _model_state = []
        for c in el.findall("model_state"):
            _res = ModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_state")
            _model_state.append(_res)
        if _model_state and cmp_version(version, "1.12") < 0:
            return SDFError(f"'model_state' is not supported in SDF version {version} (added in 1.12)")
        _joint_state = []
        for c in el.findall("joint_state"):
            _res = JointState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint_state")
            _joint_state.append(_res)
        if _joint_state and cmp_version(version, "1.12") < 0:
            return SDFError(f"'joint_state' is not supported in SDF version {version} (added in 1.12)")
        _light_state = []
        for c in el.findall("light_state"):
            _res = LightState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_state")
            _light_state.append(_res)
        if _light_state and cmp_version(version, "1.12") < 0:
            return SDFError(f"'light_state' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, world_name=_world_name, time=_time, model=_model, wall_time=_wall_time, deletions=_deletions, real_time=_real_time, insertions=_insertions, sim_time=_sim_time, iterations=_iterations, light=_light, model_state=_model_state, joint_state=_joint_state, light_state=_light_state)
