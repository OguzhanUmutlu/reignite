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
            angle: float | None = 0,
            axis: int | None = 0
        ):
            super().__init__(sdf_version)
            self.angle = angle if angle is not None else 0
            self.axis = axis if axis is not None else 0

        def to_version(self, target_version: str) -> "JointState.Angle":
            kwargs: dict = {"sdf_version": target_version, "angle": self.angle, "axis": self.axis}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
                acceleration: float | None = 0,
                degrees: bool | None = False
            ):
                super().__init__(sdf_version)
                self.acceleration = acceleration if acceleration is not None else 0
                self.degrees = degrees if degrees is not None else False

            def to_version(self, target_version: str) -> "JointState.Axis2State.Acceleration":
                kwargs: dict = {"sdf_version": target_version, "acceleration": self.acceleration, "degrees": self.degrees}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
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
            def __init__(
                self,
                sdf_version: str | None = None,
                degrees: bool | None = False,
                position: float | None = 0
            ):
                super().__init__(sdf_version)
                self.degrees = degrees if degrees is not None else False
                self.position = position if position is not None else 0

            def to_version(self, target_version: str) -> "JointState.Axis2State.Position":
                kwargs: dict = {"sdf_version": target_version, "degrees": self.degrees, "position": self.position}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
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
            def __init__(
                self,
                sdf_version: str | None = None,
                degrees: bool | None = False,
                velocity: float | None = 0
            ):
                super().__init__(sdf_version)
                self.degrees = degrees if degrees is not None else False
                self.velocity = velocity if velocity is not None else 0

            def to_version(self, target_version: str) -> "JointState.Axis2State.Velocity":
                kwargs: dict = {"sdf_version": target_version, "degrees": self.degrees, "velocity": self.velocity}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
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
            effort: float | None = 0,
            position: "JointState.Axis2State.Position" = None,
            velocity: "JointState.Axis2State.Velocity" = None
        ):
            super().__init__(sdf_version)
            self.acceleration = acceleration
            self.effort = effort if effort is not None else 0
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
                return self.to_version(str(version)).to_sdf()
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
            effort: float | None = 0,
            position: "Position" = None,
            velocity: "Velocity" = None
        ):
            super().__init__(sdf_version)
            self.acceleration = acceleration
            self.effort = effort if effort is not None else 0
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
                return self.to_version(str(version)).to_sdf()
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
        name: str | None = "__default__"
    ):
        super().__init__(sdf_version)
        self.angle = angle
        self.axis2_state = axis2_state
        self.axis_state = axis_state
        self.name = name if name is not None else "__default__"
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
            return self.to_version(str(version)).to_sdf()
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
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, angle=_angle, axis2_state=_axis2_state, axis_state=_axis_state, name=_name)
