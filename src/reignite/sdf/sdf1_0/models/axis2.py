from __future__ import annotations

from xml.etree import ElementTree as ET

from .dynamics import Dynamics
from .limit import Limit
from ..model import Model
from ....utils.vector3 import Vector3


class Axis2(Model):
    def __init__(self, xyz: Vector3 = None, dynamics: "Dynamics" = None, limit: "Limit" = None):
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit

    def to_sdf(self) -> ET.Element:
        el = ET.Element("axis2")
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf())
        if self.limit is not None:
            el.append(self.limit.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis2":
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 1"))
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit) if _c_limit is not None else None
        return cls(xyz=_xyz, dynamics=_dynamics, limit=_limit)
