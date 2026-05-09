from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .actor import Actor
from .light import Light
from .model import Model
from .world import World
from ...sdf1_11.models.sdf import Sdf as _PrevSdf


class Sdf(_PrevSdf):
    def __init__(
            self,
            version: str = "1.12",
            world: List["World"] = None,
            model: "Model" = None,
            actor: "Actor" = None,
            light: "Light" = None
    ):
        super().__init__(version=version, world=world, model=model, actor=actor, light=light)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sdf":
        _base = _PrevSdf.from_sdf(el)
        return cls(version=_base.version, world=_base.world, model=_base.model, actor=_base.actor, light=_base.light)
