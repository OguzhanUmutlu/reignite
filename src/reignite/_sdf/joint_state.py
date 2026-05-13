### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
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



class JointState(BaseModel):
    class Angle(BaseModel):
        def __init__(self, sdf_version: str | None = None, angle: float = 0, axis: int = 0):
            super().__init__(sdf_version)
            self.angle = angle
            self.axis = axis

        def to_version(self, target_version: str) -> "JointState.Angle":
            kwargs = {"sdf_version": target_version}
            kwargs["angle"] = self.angle
            kwargs["axis"] = self.axis
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("angle")
            if self.angle is not None:
                el.text = str(self.angle)
            if self.axis is not None:
                el.set("axis", str(self.axis))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Angle | SDFError":
            _text = el.text or 0
            _angle = _parse_double(_text)
            if isinstance(_angle, SDFError):
                return _angle
            _axis = _parse_uint32(el.get("axis", 0))
            if isinstance(_axis, SDFError):
                return _axis.extend("@axis")
            return cls(sdf_version=version, angle=_angle, axis=_axis)

    class Axis2State(BaseModel):
        class Acceleration(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                acceleration: float = 0,
                degrees: bool = False
            ):
                super().__init__(sdf_version)
                self.acceleration = acceleration
                self.degrees = degrees

            def to_version(self, target_version: str) -> "JointState.Axis2State.Acceleration":
                kwargs = {"sdf_version": target_version}
                kwargs["acceleration"] = self.acceleration
                kwargs["degrees"] = self.degrees
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("acceleration")
                if self.acceleration is not None:
                    el.text = str(self.acceleration)
                if self.degrees is not None:
                    el.set("degrees", str(self.degrees).lower())
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Axis2State.Acceleration | SDFError":
                _text = el.text or 0
                _acceleration = _parse_double(_text)
                if isinstance(_acceleration, SDFError):
                    return _acceleration
                _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
                if isinstance(_degrees, SDFError):
                    return _degrees.extend("@degrees")
                return cls(sdf_version=version, acceleration=_acceleration, degrees=_degrees)

        class Position(BaseModel):
            def __init__(self, sdf_version: str | None = None, degrees: bool = False, position: float = 0):
                super().__init__(sdf_version)
                self.degrees = degrees
                self.position = position

            def to_version(self, target_version: str) -> "JointState.Axis2State.Position":
                kwargs = {"sdf_version": target_version}
                kwargs["degrees"] = self.degrees
                kwargs["position"] = self.position
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("position")
                if self.degrees is not None:
                    el.set("degrees", str(self.degrees).lower())
                if self.position is not None:
                    el.text = str(self.position)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Axis2State.Position | SDFError":
                _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
                if isinstance(_degrees, SDFError):
                    return _degrees.extend("@degrees")
                _text = el.text or 0
                _position = _parse_double(_text)
                if isinstance(_position, SDFError):
                    return _position
                return cls(sdf_version=version, degrees=_degrees, position=_position)

        class Velocity(BaseModel):
            def __init__(self, sdf_version: str | None = None, degrees: bool = False, velocity: float = 0):
                super().__init__(sdf_version)
                self.degrees = degrees
                self.velocity = velocity

            def to_version(self, target_version: str) -> "JointState.Axis2State.Velocity":
                kwargs = {"sdf_version": target_version}
                kwargs["degrees"] = self.degrees
                kwargs["velocity"] = self.velocity
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("velocity")
                if self.degrees is not None:
                    el.set("degrees", str(self.degrees).lower())
                if self.velocity is not None:
                    el.text = str(self.velocity)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Axis2State.Velocity | SDFError":
                _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
                if isinstance(_degrees, SDFError):
                    return _degrees.extend("@degrees")
                _text = el.text or 0
                _velocity = _parse_double(_text)
                if isinstance(_velocity, SDFError):
                    return _velocity
                return cls(sdf_version=version, degrees=_degrees, velocity=_velocity)

        def __init__(
            self,
            sdf_version: str | None = None,
            acceleration: "JointState.Axis2State.Acceleration" = None,
            effort: float = 0,
            position: "JointState.Axis2State.Position" = None,
            velocity: "JointState.Axis2State.Velocity" = None
        ):
            super().__init__(sdf_version)
            self.acceleration = acceleration
            self.effort = effort
            self.position = position
            self.velocity = velocity
            if self.acceleration is not None and hasattr(self.acceleration, 'to_version'):
                if getattr(self.acceleration, '__version__', None) is None:
                    self.acceleration.__version__ = self.__version__
                elif getattr(self.acceleration, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.acceleration = self.acceleration.to_version(self.__version__)
            if self.position is not None and hasattr(self.position, 'to_version'):
                if getattr(self.position, '__version__', None) is None:
                    self.position.__version__ = self.__version__
                elif getattr(self.position, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.position = self.position.to_version(self.__version__)
            if self.velocity is not None and hasattr(self.velocity, 'to_version'):
                if getattr(self.velocity, '__version__', None) is None:
                    self.velocity.__version__ = self.__version__
                elif getattr(self.velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.velocity = self.velocity.to_version(self.__version__)

        def to_version(self, target_version: str) -> "JointState.Axis2State":
            kwargs = {"sdf_version": target_version}
            kwargs["acceleration"] = self.acceleration.to_version(target_version) if hasattr(self.acceleration, "to_version") else self.acceleration
            kwargs["effort"] = self.effort
            kwargs["position"] = self.position.to_version(target_version) if hasattr(self.position, "to_version") else self.position
            kwargs["velocity"] = self.velocity.to_version(target_version) if hasattr(self.velocity, "to_version") else self.velocity
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("axis2_state")
            if self.acceleration is not None:
                if hasattr(self.acceleration, 'to_sdf'):
                    _child_res = self.acceleration.to_sdf(version)
                else:
                    _child_res = str(self.acceleration)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('acceleration')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.effort is not None:
                _c_tmp = ET.Element("effort")
                _c_tmp.text = str(self.effort)
                el.append(_c_tmp)
            if self.position is not None:
                if hasattr(self.position, 'to_sdf'):
                    _child_res = self.position.to_sdf(version)
                else:
                    _child_res = str(self.position)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('position')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.velocity is not None:
                if hasattr(self.velocity, 'to_sdf'):
                    _child_res = self.velocity.to_sdf(version)
                else:
                    _child_res = str(self.velocity)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('velocity')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Axis2State | SDFError":
            _c_acceleration = el.find("acceleration")
            if _c_acceleration is not None:
                _res = cls.Acceleration._from_sdf(_c_acceleration, version)
                if isinstance(_res, SDFError):
                    return _res.extend("acceleration")
                _acceleration = _res
            else:
                _acceleration = None
            _c_tmp = el.find("effort")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("effort")
                _effort = _val
            else:
                _effort = None
            _c_position = el.find("position")
            if _c_position is not None:
                _res = cls.Position._from_sdf(_c_position, version)
                if isinstance(_res, SDFError):
                    return _res.extend("position")
                _position = _res
            else:
                _position = None
            _c_velocity = el.find("velocity")
            if _c_velocity is not None:
                _res = cls.Velocity._from_sdf(_c_velocity, version)
                if isinstance(_res, SDFError):
                    return _res.extend("velocity")
                _velocity = _res
            else:
                _velocity = None
            return cls(sdf_version=version, acceleration=_acceleration, effort=_effort, position=_position, velocity=_velocity)

    class AxisState(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            acceleration: "Acceleration" = None,
            effort: float = 0,
            position: "Position" = None,
            velocity: "Velocity" = None
        ):
            super().__init__(sdf_version)
            self.acceleration = acceleration
            self.effort = effort
            self.position = position
            self.velocity = velocity
            if self.acceleration is not None and hasattr(self.acceleration, 'to_version'):
                if getattr(self.acceleration, '__version__', None) is None:
                    self.acceleration.__version__ = self.__version__
                elif getattr(self.acceleration, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.acceleration = self.acceleration.to_version(self.__version__)
            if self.position is not None and hasattr(self.position, 'to_version'):
                if getattr(self.position, '__version__', None) is None:
                    self.position.__version__ = self.__version__
                elif getattr(self.position, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.position = self.position.to_version(self.__version__)
            if self.velocity is not None and hasattr(self.velocity, 'to_version'):
                if getattr(self.velocity, '__version__', None) is None:
                    self.velocity.__version__ = self.__version__
                elif getattr(self.velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.velocity = self.velocity.to_version(self.__version__)

        def to_version(self, target_version: str) -> "JointState.AxisState":
            kwargs = {"sdf_version": target_version}
            kwargs["acceleration"] = self.acceleration.to_version(target_version) if hasattr(self.acceleration, "to_version") else self.acceleration
            kwargs["effort"] = self.effort
            kwargs["position"] = self.position.to_version(target_version) if hasattr(self.position, "to_version") else self.position
            kwargs["velocity"] = self.velocity.to_version(target_version) if hasattr(self.velocity, "to_version") else self.velocity
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("axis_state")
            if self.acceleration is not None:
                if hasattr(self.acceleration, 'to_sdf'):
                    _child_res = self.acceleration.to_sdf(version)
                else:
                    _child_res = str(self.acceleration)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('acceleration')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.effort is not None:
                _c_tmp = ET.Element("effort")
                _c_tmp.text = str(self.effort)
                el.append(_c_tmp)
            if self.position is not None:
                if hasattr(self.position, 'to_sdf'):
                    _child_res = self.position.to_sdf(version)
                else:
                    _child_res = str(self.position)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('position')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.velocity is not None:
                if hasattr(self.velocity, 'to_sdf'):
                    _child_res = self.velocity.to_sdf(version)
                else:
                    _child_res = str(self.velocity)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('velocity')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.AxisState | SDFError":
            _c_acceleration = el.find("acceleration")
            if _c_acceleration is not None:
                _res = Acceleration._from_sdf(_c_acceleration, version)
                if isinstance(_res, SDFError):
                    return _res.extend("acceleration")
                _acceleration = _res
            else:
                _acceleration = None
            _c_tmp = el.find("effort")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("effort")
                _effort = _val
            else:
                _effort = None
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
            return cls(sdf_version=version, acceleration=_acceleration, effort=_effort, position=_position, velocity=_velocity)

    def __init__(
        self,
        sdf_version: str | None = None,
        angle: "JointState.Angle" = None,
        axis2_state: "JointState.Axis2State" = None,
        axis_state: "JointState.AxisState" = None,
        name: str = "__default__"
    ):
        super().__init__(sdf_version)
        self.angle = angle
        self.axis2_state = axis2_state
        self.axis_state = axis_state
        self.name = name
        if self.angle is not None and hasattr(self.angle, 'to_version'):
            if getattr(self.angle, '__version__', None) is None:
                self.angle.__version__ = self.__version__
            elif getattr(self.angle, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.angle = self.angle.to_version(self.__version__)
        if self.axis2_state is not None and hasattr(self.axis2_state, 'to_version'):
            if getattr(self.axis2_state, '__version__', None) is None:
                self.axis2_state.__version__ = self.__version__
            elif getattr(self.axis2_state, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.axis2_state = self.axis2_state.to_version(self.__version__)
        if self.axis_state is not None and hasattr(self.axis_state, 'to_version'):
            if getattr(self.axis_state, '__version__', None) is None:
                self.axis_state.__version__ = self.__version__
            elif getattr(self.axis_state, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.axis_state = self.axis_state.to_version(self.__version__)

    def to_version(self, target_version: str) -> "JointState":
        kwargs = {"sdf_version": target_version}
        kwargs["angle"] = self.angle.to_version(target_version) if hasattr(self.angle, "to_version") else self.angle
        kwargs["axis2_state"] = self.axis2_state.to_version(target_version) if hasattr(self.axis2_state, "to_version") else self.axis2_state
        kwargs["axis_state"] = self.axis_state.to_version(target_version) if hasattr(self.axis_state, "to_version") else self.axis_state
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("joint_state")
        if self.angle is not None:
            if hasattr(self.angle, 'to_sdf'):
                _child_res = self.angle.to_sdf(version)
            else:
                _child_res = str(self.angle)
            if isinstance(_child_res, str):
                _item_el = ET.Element('angle')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.axis2_state is not None:
            if hasattr(self.axis2_state, 'to_sdf'):
                _child_res = self.axis2_state.to_sdf(version)
            else:
                _child_res = str(self.axis2_state)
            if isinstance(_child_res, str):
                _item_el = ET.Element('axis2_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.axis_state is not None:
            if hasattr(self.axis_state, 'to_sdf'):
                _child_res = self.axis_state.to_sdf(version)
            else:
                _child_res = str(self.axis_state)
            if isinstance(_child_res, str):
                _item_el = ET.Element('axis_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "JointState | SDFError":
        _c_angle = el.find("angle")
        if _c_angle is not None:
            _res = cls.Angle._from_sdf(_c_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("angle")
            _angle = _res
        else:
            _angle = None
        _c_axis2_state = el.find("axis2_state")
        if _c_axis2_state is not None:
            _res = cls.Axis2State._from_sdf(_c_axis2_state, version)
            if isinstance(_res, SDFError):
                return _res.extend("axis2_state")
            _axis2_state = _res
        else:
            _axis2_state = None
        _c_axis_state = el.find("axis_state")
        if _c_axis_state is not None:
            _res = cls.AxisState._from_sdf(_c_axis_state, version)
            if isinstance(_res, SDFError):
                return _res.extend("axis_state")
            _axis_state = _res
        else:
            _axis_state = None
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, angle=_angle, axis2_state=_axis2_state, axis_state=_axis_state, name=_name)
