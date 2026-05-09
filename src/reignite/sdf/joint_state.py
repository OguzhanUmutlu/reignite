### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


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
        if self.angle is not None:
            el.text = str(self.angle)
        if self.axis is not None:
            el.set("axis", str(self.axis))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _angle = _parse_double(_text)
        if isinstance(_angle, SDFError):
            return _angle
        _axis = _parse_uint32(el.get("axis", 0))
        if isinstance(_axis, SDFError):
            return _axis.extend("@axis")
        return cls(sdf_version=version, angle=_angle, axis=_axis)


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


class Velocity(BaseModel):
    def __init__(self, sdf_version: str, velocity: float = 0, degrees: bool = False):
        self.__version__ = sdf_version
        self.velocity = velocity
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Velocity":
        kwargs = {"sdf_version": target_version}
        kwargs["velocity"] = self.velocity
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = str(self.velocity)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _velocity = _parse_double(_text)
        if isinstance(_velocity, SDFError):
            return _velocity
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        return cls(sdf_version=version, velocity=_velocity, degrees=_degrees)


class Acceleration(BaseModel):
    def __init__(self, sdf_version: str, acceleration: float = 0, degrees: bool = False):
        self.__version__ = sdf_version
        self.acceleration = acceleration
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Acceleration":
        kwargs = {"sdf_version": target_version}
        kwargs["acceleration"] = self.acceleration
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("acceleration")
        if self.acceleration is not None:
            el.text = str(self.acceleration)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _acceleration = _parse_double(_text)
        if isinstance(_acceleration, SDFError):
            return _acceleration
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        return cls(sdf_version=version, acceleration=_acceleration, degrees=_degrees)


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
