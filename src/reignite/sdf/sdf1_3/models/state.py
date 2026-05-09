from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .deletions import Deletions
from .insertions import Insertions
from .model import Model
from .real_time import RealTime
from .sim_time import SimTime
from .wall_time import WallTime


class State(Model):
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
        self.world_name = world_name
        self.sim_time = sim_time
        self.wall_time = wall_time
        self.real_time = real_time
        self.insertions = insertions
        self.deletions = deletions
        self.model = model or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("state")
        if self.world_name is not None:
            el.set("world_name", self.world_name)
        if self.sim_time is not None:
            el.append(self.sim_time.to_sdf())
        if self.wall_time is not None:
            el.append(self.wall_time.to_sdf())
        if self.real_time is not None:
            el.append(self.real_time.to_sdf())
        if self.insertions is not None:
            el.append(self.insertions.to_sdf())
        if self.deletions is not None:
            el.append(self.deletions.to_sdf())
        for item in (self.model or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "State":
        _world_name = el.get("world_name", "__default__")
        _c_sim_time = el.find("sim_time")
        _sim_time = SimTime.from_sdf(_c_sim_time) if _c_sim_time is not None else None
        _c_wall_time = el.find("wall_time")
        _wall_time = WallTime.from_sdf(_c_wall_time) if _c_wall_time is not None else None
        _c_real_time = el.find("real_time")
        _real_time = RealTime.from_sdf(_c_real_time) if _c_real_time is not None else None
        _c_insertions = el.find("insertions")
        _insertions = Insertions.from_sdf(_c_insertions) if _c_insertions is not None else None
        _c_deletions = el.find("deletions")
        _deletions = Deletions.from_sdf(_c_deletions) if _c_deletions is not None else None
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        return cls(world_name=_world_name, sim_time=_sim_time, wall_time=_wall_time, real_time=_real_time,
                   insertions=_insertions, deletions=_deletions, model=_model)
