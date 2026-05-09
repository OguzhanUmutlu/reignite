from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .deletions import Deletions
from .insertions import Insertions
from .model import Model
from .real_time import RealTime
from .sim_time import SimTime
from .wall_time import WallTime
from ...sdf1_3.models.state import State as _PrevState


class State(_PrevState):
    def __init__(
            self,
            world_name: str = "__default__",
            sim_time: "SimTime" = None,
            wall_time: "WallTime" = None,
            real_time: "RealTime" = None,
            insertions: "Insertions" = None,
            deletions: "Deletions" = None,
            model: List["Model"] = None
    ):
        super().__init__(world_name=world_name, sim_time=sim_time, wall_time=wall_time, real_time=real_time,
                         insertions=insertions, deletions=deletions, model=model)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "State":
        _base = _PrevState.from_sdf(el)
        return cls(world_name=_base.world_name, sim_time=_base.sim_time, wall_time=_base.wall_time,
                   real_time=_base.real_time, insertions=_base.insertions, deletions=_base.deletions, model=_base.model)
