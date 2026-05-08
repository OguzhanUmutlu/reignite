from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_4.models.static import Static as _PrevStatic
from ...sdf1_4.models.include import Include as _PrevInclude
from ...sdf1_4.models.model import Model as _PrevModel
from .box import Box
from .cylinder import Cylinder
from .frame import Frame
from .pose import Pose
from .model_count import ModelCount
from .distribution import Distribution


class Static(_PrevStatic):
    def __init__(self, static: bool = False):
        super().__init__(static=static)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Static":
        _base = _PrevStatic.from_sdf(el)
        return cls(static=_base.static)


class Include(_PrevInclude):
    def __init__(
        self,
        plugin: List["Plugin"] = None,
        uri: "Uri" = None,
        pose: "Pose" = None,
        name: "Name" = None,
        static: "Static" = None
    ):
        super().__init__(uri=uri)
        self.plugin = plugin or []
        self.pose = pose
        self.name = name
        self.static = static

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.name is not None:
            el.append(self.name.to_sdf())
        if self.static is not None:
            el.append(self.static.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Include":
        _base = _PrevInclude.from_sdf(el)
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name) if _c_name is not None else None
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static) if _c_static is not None else None
        return cls(plugin=_plugin, uri=_base.uri, pose=_pose, name=_name, static=_static)


class Model(_PrevModel):
    def __init__(
        self,
        name: str = "__default__",
        frame: List["Frame"] = None,
        pose: "Pose" = None,
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        gripper: List["Gripper"] = None,
        static: "Static" = None,
        self_collide: "SelfCollide" = None,
        allow_auto_disable: "AllowAutoDisable" = None,
        include: List["Include"] = None,
        model: List["Model"] = None
    ):
        super().__init__(name=name, pose=pose, link=link, joint=joint, plugin=plugin, gripper=gripper, static=static, allow_auto_disable=allow_auto_disable)
        self.frame = frame or []
        self.self_collide = self_collide
        self.include = include or []
        self.model = model or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf())
        for item in (self.include or []):
            el.append(item.to_sdf())
        for item in (self.model or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        _base = _PrevModel.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_self_collide = el.find("self_collide")
        _self_collide = SelfCollide.from_sdf(_c_self_collide) if _c_self_collide is not None else None
        _include = [Include.from_sdf(c) for c in el.findall("include")]
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        return cls(name=_base.name, frame=_frame, pose=_base.pose, link=_base.link, joint=_base.joint, plugin=_base.plugin, gripper=_base.gripper, static=_base.static, self_collide=_self_collide, allow_auto_disable=_base.allow_auto_disable, include=_include, model=_model)


class Population(Model):
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
        self.name = name
        self.box = box
        self.cylinder = cylinder
        self.frame = frame or []
        self.pose = pose
        self.model = model
        self.model_count = model_count
        self.distribution = distribution

    def to_sdf(self) -> ET.Element:
        el = ET.Element("population")
        if self.name is not None:
            el.set("name", self.name)
        if self.box is not None:
            el.append(self.box.to_sdf())
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf())
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.model is not None:
            el.append(self.model.to_sdf())
        if self.model_count is not None:
            el.append(self.model_count.to_sdf())
        if self.distribution is not None:
            el.append(self.distribution.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Population":
        _name = el.get("name", "__default__")
        _c_box = el.find("box")
        _box = Box.from_sdf(_c_box) if _c_box is not None else None
        _c_cylinder = el.find("cylinder")
        _cylinder = Cylinder.from_sdf(_c_cylinder) if _c_cylinder is not None else None
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_model = el.find("model")
        _model = Model.from_sdf(_c_model) if _c_model is not None else None
        _c_model_count = el.find("model_count")
        _model_count = ModelCount.from_sdf(_c_model_count) if _c_model_count is not None else None
        _c_distribution = el.find("distribution")
        _distribution = Distribution.from_sdf(_c_distribution) if _c_distribution is not None else None
        return cls(name=_name, box=_box, cylinder=_cylinder, frame=_frame, pose=_pose, model=_model, model_count=_model_count, distribution=_distribution)
