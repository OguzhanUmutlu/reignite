### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_uint32
from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class JointState(BaseModel):
    class Angle(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            angle: float | None = None,
            axis: int | None = None
        ):
            super().__init__(sdf_version)
            self.angle = angle
            self.axis = axis

        def to_version(self, target_version: str) -> "JointState.Angle":
            kwargs: dict = {"sdf_version": target_version, "angle": self.angle, "axis": self.axis}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("angle")
            if self.angle is not None:
                el.text = str(self.angle)
            if self.axis is not None:
                el.set("axis", str(self.axis))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Angle | SDFError":
            _raw_angle = el.text
            if _raw_angle is not None:
                _angle = _parse_double(_raw_angle)
                if isinstance(_angle, SDFError):
                    return _angle
            else:
                _angle = None
            _raw_axis = el.get("axis")
            if _raw_axis is not None:
                _axis = _parse_uint32(_raw_axis)
                if isinstance(_axis, SDFError):
                    return _axis.extend("@axis")
            else:
                _axis = None
            return cls(sdf_version=version, angle=_angle, axis=_axis)

    class Axis2State(BaseModel):
        class Acceleration(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                acceleration: float | None = None,
                degrees: bool | None = None
            ):
                super().__init__(sdf_version)
                self.acceleration = acceleration
                self.degrees = degrees

            def to_version(self, target_version: str) -> "JointState.Axis2State.Acceleration":
                kwargs: dict = {"sdf_version": target_version, "acceleration": self.acceleration, "degrees": self.degrees}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("acceleration")
                if self.acceleration is not None:
                    el.text = str(self.acceleration)
                if self.degrees is not None:
                    el.set("degrees", str(self.degrees).lower())
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Axis2State.Acceleration | SDFError":
                _raw_acceleration = el.text
                if _raw_acceleration is not None:
                    _acceleration = _parse_double(_raw_acceleration)
                    if isinstance(_acceleration, SDFError):
                        return _acceleration
                else:
                    _acceleration = None
                _raw_degrees = el.get("degrees")
                if _raw_degrees is not None:
                    _degrees = str(_raw_degrees).strip().lower() == 'true'
                    if isinstance(_degrees, SDFError):
                        return _degrees.extend("@degrees")
                else:
                    _degrees = None
                return cls(sdf_version=version, acceleration=_acceleration, degrees=_degrees)

        class Position(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                degrees: bool | None = None,
                position: float | None = None
            ):
                super().__init__(sdf_version)
                self.degrees = degrees
                self.position = position

            def to_version(self, target_version: str) -> "JointState.Axis2State.Position":
                kwargs: dict = {"sdf_version": target_version, "degrees": self.degrees, "position": self.position}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("position")
                if self.degrees is not None:
                    el.set("degrees", str(self.degrees).lower())
                if self.position is not None:
                    el.text = str(self.position)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Axis2State.Position | SDFError":
                _raw_degrees = el.get("degrees")
                if _raw_degrees is not None:
                    _degrees = str(_raw_degrees).strip().lower() == 'true'
                    if isinstance(_degrees, SDFError):
                        return _degrees.extend("@degrees")
                else:
                    _degrees = None
                _raw_position = el.text
                if _raw_position is not None:
                    _position = _parse_double(_raw_position)
                    if isinstance(_position, SDFError):
                        return _position
                else:
                    _position = None
                return cls(sdf_version=version, degrees=_degrees, position=_position)

        class Velocity(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                degrees: bool | None = None,
                velocity: float | None = None
            ):
                super().__init__(sdf_version)
                self.degrees = degrees
                self.velocity = velocity

            def to_version(self, target_version: str) -> "JointState.Axis2State.Velocity":
                kwargs: dict = {"sdf_version": target_version, "degrees": self.degrees, "velocity": self.velocity}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("velocity")
                if self.degrees is not None:
                    el.set("degrees", str(self.degrees).lower())
                if self.velocity is not None:
                    el.text = str(self.velocity)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "JointState.Axis2State.Velocity | SDFError":
                _raw_degrees = el.get("degrees")
                if _raw_degrees is not None:
                    _degrees = str(_raw_degrees).strip().lower() == 'true'
                    if isinstance(_degrees, SDFError):
                        return _degrees.extend("@degrees")
                else:
                    _degrees = None
                _raw_velocity = el.text
                if _raw_velocity is not None:
                    _velocity = _parse_double(_raw_velocity)
                    if isinstance(_velocity, SDFError):
                        return _velocity
                else:
                    _velocity = None
                return cls(sdf_version=version, degrees=_degrees, velocity=_velocity)

        def __init__(
            self,
            sdf_version: str | None = None,
            acceleration: "JointState.Axis2State.Acceleration" = None,
            effort: float | None = None,
            position: "JointState.Axis2State.Position" = None,
            velocity: "JointState.Axis2State.Velocity" = None
        ):
            super().__init__(sdf_version)
            self.acceleration = acceleration
            self.effort = effort
            self.position = position
            self.velocity = velocity
            if self.acceleration is not None and hasattr(self.acceleration, 'to_version'):
                if getattr(self.acceleration, 'sdfversion', None) is None:
                    self.acceleration.sdfversion = self.sdfversion
                elif getattr(self.acceleration, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.acceleration = self.acceleration.to_version(self.sdfversion)
            if self.position is not None and hasattr(self.position, 'to_version'):
                if getattr(self.position, 'sdfversion', None) is None:
                    self.position.sdfversion = self.sdfversion
                elif getattr(self.position, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.position = self.position.to_version(self.sdfversion)
            if self.velocity is not None and hasattr(self.velocity, 'to_version'):
                if getattr(self.velocity, 'sdfversion', None) is None:
                    self.velocity.sdfversion = self.sdfversion
                elif getattr(self.velocity, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.velocity = self.velocity.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "JointState.Axis2State":
            kwargs: dict = {"sdf_version": target_version, "acceleration": self.acceleration.to_version(target_version) if self.acceleration is not None and hasattr(self.acceleration, "to_version") else self.acceleration, "effort": self.effort, "position": self.position.to_version(target_version) if self.position is not None and hasattr(self.position, "to_version") else self.position, "velocity": self.velocity.to_version(target_version) if self.velocity is not None and hasattr(self.velocity, "to_version") else self.velocity}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("axis2_state")
            if self.acceleration is not None:
                _child_res = self.acceleration.to_sdf(version)
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
                _child_res = self.position.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('position')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.velocity is not None:
                _child_res = self.velocity.to_sdf(version)
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
            effort: float | None = None,
            position: "Position" = None,
            velocity: "Velocity" = None
        ):
            super().__init__(sdf_version)
            self.acceleration = acceleration
            self.effort = effort
            self.position = position
            self.velocity = velocity
            if self.acceleration is not None and hasattr(self.acceleration, 'to_version'):
                if getattr(self.acceleration, 'sdfversion', None) is None:
                    self.acceleration.sdfversion = self.sdfversion
                elif getattr(self.acceleration, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.acceleration = self.acceleration.to_version(self.sdfversion)
            if self.position is not None and hasattr(self.position, 'to_version'):
                if getattr(self.position, 'sdfversion', None) is None:
                    self.position.sdfversion = self.sdfversion
                elif getattr(self.position, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.position = self.position.to_version(self.sdfversion)
            if self.velocity is not None and hasattr(self.velocity, 'to_version'):
                if getattr(self.velocity, 'sdfversion', None) is None:
                    self.velocity.sdfversion = self.sdfversion
                elif getattr(self.velocity, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.velocity = self.velocity.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "JointState.AxisState":
            kwargs: dict = {"sdf_version": target_version, "acceleration": self.acceleration.to_version(target_version) if self.acceleration is not None and hasattr(self.acceleration, "to_version") else self.acceleration, "effort": self.effort, "position": self.position.to_version(target_version) if self.position is not None and hasattr(self.position, "to_version") else self.position, "velocity": self.velocity.to_version(target_version) if self.velocity is not None and hasattr(self.velocity, "to_version") else self.velocity}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("axis_state")
            if self.acceleration is not None:
                _child_res = self.acceleration.to_sdf(version)
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
                _child_res = self.position.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('position')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.velocity is not None:
                _child_res = self.velocity.to_sdf(version)
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
        name: str | None = None
    ):
        super().__init__(sdf_version)
        self.angle = angle
        self.axis2_state = axis2_state
        self.axis_state = axis_state
        self.name = name
        if self.angle is not None and hasattr(self.angle, 'to_version'):
            if getattr(self.angle, 'sdfversion', None) is None:
                self.angle.sdfversion = self.sdfversion
            elif getattr(self.angle, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.angle = self.angle.to_version(self.sdfversion)
        if self.axis2_state is not None and hasattr(self.axis2_state, 'to_version'):
            if getattr(self.axis2_state, 'sdfversion', None) is None:
                self.axis2_state.sdfversion = self.sdfversion
            elif getattr(self.axis2_state, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.axis2_state = self.axis2_state.to_version(self.sdfversion)
        if self.axis_state is not None and hasattr(self.axis_state, 'to_version'):
            if getattr(self.axis_state, 'sdfversion', None) is None:
                self.axis_state.sdfversion = self.sdfversion
            elif getattr(self.axis_state, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.axis_state = self.axis_state.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "JointState":
        kwargs: dict = {"sdf_version": target_version, "angle": self.angle.to_version(target_version) if self.angle is not None and hasattr(self.angle, "to_version") else self.angle, "axis2_state": self.axis2_state.to_version(target_version) if self.axis2_state is not None and hasattr(self.axis2_state, "to_version") else self.axis2_state, "axis_state": self.axis_state.to_version(target_version) if self.axis_state is not None and hasattr(self.axis_state, "to_version") else self.axis_state, "name": self.name}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("joint_state")
        if self.angle is not None:
            _child_res = self.angle.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('angle')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.axis2_state is not None:
            _child_res = self.axis2_state.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('axis2_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.axis_state is not None:
            _child_res = self.axis_state.to_sdf(version)
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
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        return cls(sdf_version=version, angle=_angle, axis2_state=_axis2_state, axis_state=_axis_state, name=_name)
