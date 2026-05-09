from __future__ import annotations

from xml.etree import ElementTree as ET

from .angle import Angle
from .axis2_state import Axis2State
from .axis_state import AxisState
from ..model import Model


class JointState(Model):
    def __init__(
            self,
            name: str = "__default__",
            angle: "Angle" = None,
            axis_state: "AxisState" = None,
            axis2_state: "Axis2State" = None
    ):
        self.name = name
        self.angle = angle
        self.axis_state = axis_state
        self.axis2_state = axis2_state

    def to_sdf(self) -> ET.Element:
        el = ET.Element("joint_state")
        if self.name is not None:
            el.set("name", self.name)
        if self.angle is not None:
            el.append(self.angle.to_sdf())
        if self.axis_state is not None:
            el.append(self.axis_state.to_sdf())
        if self.axis2_state is not None:
            el.append(self.axis2_state.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "JointState":
        _name = el.get("name", "__default__")
        _c_angle = el.find("angle")
        _angle = Angle.from_sdf(_c_angle) if _c_angle is not None else None
        _c_axis_state = el.find("axis_state")
        _axis_state = AxisState.from_sdf(_c_axis_state) if _c_axis_state is not None else None
        _c_axis2_state = el.find("axis2_state")
        _axis2_state = Axis2State.from_sdf(_c_axis2_state) if _c_axis2_state is not None else None
        return cls(name=_name, angle=_angle, axis_state=_axis_state, axis2_state=_axis2_state)
