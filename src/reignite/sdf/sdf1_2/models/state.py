from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_0.models.state import State as _PrevState
from .time import Time
from .model import Model


class State(_PrevState):
    def __init__(
        self,
        world_name: str = "__default__",
        time: "Time" = None,
        model: List["Model"] = None
    ):
        super().__init__(world_name=world_name, time=time, model=model)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "State":
        _base = _PrevState.from_sdf(el)
        return cls(world_name=_base.world_name, time=_base.time, model=_base.model)
