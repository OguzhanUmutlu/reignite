from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.include import Include as _PrevInclude
from ...sdf1_4.models.insertions import Insertions as _PrevInsertions
from ...sdf1_4.models.model import Model as _PrevModel
from ...sdf1_4.models.static import Static as _PrevStatic


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
        super().__init__(name=name, pose=pose, link=link, joint=joint, plugin=plugin, gripper=gripper, static=static,
                         allow_auto_disable=allow_auto_disable)
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
        return cls(name=_base.name, frame=_frame, pose=_base.pose, link=_base.link, joint=_base.joint,
                   plugin=_base.plugin, gripper=_base.gripper, static=_base.static, self_collide=_self_collide,
                   allow_auto_disable=_base.allow_auto_disable, include=_include, model=_model)


class Insertions(_PrevInsertions):
    def __init__(self, model: List["Model"] = None):
        super().__init__(model=model)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Insertions":
        _base = _PrevInsertions.from_sdf(el)
        return cls(model=_base.model)
