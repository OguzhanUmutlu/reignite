from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_11.models.state import State as _PrevState
from .model_state import ModelState
from .light_state import LightState
from .joint_state import JointState
from .sim_time import SimTime
from .wall_time import WallTime
from .real_time import RealTime
from .iterations import Iterations
from .insertions import Insertions
from .deletions import Deletions


class State(_PrevState):
    def __init__(
        self,
        world_name: str = "__default__",
        model_state: List["ModelState"] = None,
        light_state: List["LightState"] = None,
        joint_state: List["JointState"] = None,
        sim_time: "SimTime" = None,
        wall_time: "WallTime" = None,
        real_time: "RealTime" = None,
        iterations: "Iterations" = None,
        insertions: "Insertions" = None,
        deletions: "Deletions" = None
    ):
        super().__init__(world_name=world_name, sim_time=sim_time, wall_time=wall_time, real_time=real_time, iterations=iterations, insertions=insertions, deletions=deletions)
        self.model_state = model_state or []
        self.light_state = light_state or []
        self.joint_state = joint_state or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.model_state or []):
            el.append(item.to_sdf())
        for item in (self.light_state or []):
            el.append(item.to_sdf())
        for item in (self.joint_state or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "State":
        _base = _PrevState.from_sdf(el)
        _model_state = [ModelState.from_sdf(c) for c in el.findall("model_state")]
        _light_state = [LightState.from_sdf(c) for c in el.findall("light_state")]
        _joint_state = [JointState.from_sdf(c) for c in el.findall("joint_state")]
        return cls(world_name=_base.world_name, model_state=_model_state, light_state=_light_state, joint_state=_joint_state, sim_time=_base.sim_time, wall_time=_base.wall_time, real_time=_base.real_time, iterations=_base.iterations, insertions=_base.insertions, deletions=_base.deletions)
