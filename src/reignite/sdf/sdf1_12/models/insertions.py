from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_11.models.insertions import Insertions as _PrevInsertions
from .model import Model
from .light import Light
from .joint import Joint


class Insertions(_PrevInsertions):
    def __init__(
        self,
        model: List["Model"] = None,
        light: List["Light"] = None,
        joint: List["Joint"] = None
    ):
        super().__init__(model=model, light=light)
        self.joint = joint or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.joint or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Insertions":
        _base = _PrevInsertions.from_sdf(el)
        _joint = [Joint.from_sdf(c) for c in el.findall("joint")]
        return cls(model=_base.model, light=_base.light, joint=_joint)
