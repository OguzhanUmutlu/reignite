from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.force_torque import ForceTorque as _PrevForceTorque
from .frame import Frame
from .measure_direction import MeasureDirection
from .force import Force
from .torque import Torque


class ForceTorque(_PrevForceTorque):
    def __init__(
        self,
        frame: "Frame" = None,
        measure_direction: "MeasureDirection" = None,
        force: "Force" = None,
        torque: "Torque" = None
    ):
        super().__init__(frame=frame, measure_direction=measure_direction)
        self.force = force
        self.torque = torque

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.force is not None:
            el.append(self.force.to_sdf())
        if self.torque is not None:
            el.append(self.torque.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ForceTorque":
        _base = _PrevForceTorque.from_sdf(el)
        _c_force = el.find("force")
        _force = Force.from_sdf(_c_force) if _c_force is not None else None
        _c_torque = el.find("torque")
        _torque = Torque.from_sdf(_c_torque) if _c_torque is not None else None
        return cls(frame=_base.frame, measure_direction=_base.measure_direction, force=_force, torque=_torque)
