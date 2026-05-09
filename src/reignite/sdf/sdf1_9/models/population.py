from __future__ import annotations

from xml.etree import ElementTree as ET

from .box import Box
from .cylinder import Cylinder
from .distribution import Distribution
from .model import Model
from .model_count import ModelCount
from ..model import Model
from ...sdf1_8.models.population import Population as _PrevPopulation
from ...sdf1_8.models.pose import Pose as _PrevPose
from ....utils.pose import Pose


class Pose(_PrevPose):
    def __init__(
            self,
            pose: Pose = None,
            relative_to: str = "",
            rotation_format: str = "euler_rpy",
            degrees: bool = False
    ):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose, relative_to=relative_to)
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        _rotation_format = el.get("rotation_format", "euler_rpy")
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(pose=_base.pose, relative_to=_base.relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Population(_PrevPopulation):
    def __init__(
            self,
            name: str = "__default__",
            box: "Box" = None,
            cylinder: "Cylinder" = None,
            pose: "Pose" = None,
            model: "Model" = None,
            model_count: "ModelCount" = None,
            distribution: "Distribution" = None
    ):
        super().__init__(name=name, box=box, cylinder=cylinder, pose=pose, model=model, model_count=model_count,
                         distribution=distribution)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Population":
        _base = _PrevPopulation.from_sdf(el)
        return cls(name=_base.name, box=_base.box, cylinder=_base.cylinder, pose=_base.pose, model=_base.model,
                   model_count=_base.model_count, distribution=_base.distribution)
