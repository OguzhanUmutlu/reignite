from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .box import Box
from .cylinder import Cylinder
from .distribution import Distribution
from .model import Model
from .model_count import ModelCount
from ..model import Model
from ...sdf1_5.models.frame import Frame as _PrevFrame
from ...sdf1_5.models.population import Population as _PrevPopulation
from ...sdf1_5.models.pose import Pose as _PrevPose
from ....utils.pose import Pose


class Pose(_PrevPose):
    def __init__(self, pose: Pose = None, frame: str = ""):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose, frame=frame)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        return cls(pose=_base.pose, frame=_base.frame)


class Frame(_PrevFrame):
    def __init__(self, name: str = "", pose: "Pose" = None):
        super().__init__(name=name, pose=pose)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frame":
        _base = _PrevFrame.from_sdf(el)
        return cls(name=_base.name, pose=_base.pose)


class Population(_PrevPopulation):
    def __init__(
            self,
            name: str = "__default__",
            box: "Box" = None,
            cylinder: "Cylinder" = None,
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            model: "Model" = None,
            model_count: "ModelCount" = None,
            distribution: "Distribution" = None
    ):
        super().__init__(name=name, box=box, cylinder=cylinder, frame=frame, pose=pose, model=model,
                         model_count=model_count, distribution=distribution)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Population":
        _base = _PrevPopulation.from_sdf(el)
        return cls(name=_base.name, box=_base.box, cylinder=_base.cylinder, frame=_base.frame, pose=_base.pose,
                   model=_base.model, model_count=_base.model_count, distribution=_base.distribution)
