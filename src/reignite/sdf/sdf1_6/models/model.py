from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_5.models.static import Static as _PrevStatic
from ...sdf1_5.models.model import Model as _PrevModel
from .frame import Frame
from .pose import Pose
from .link import Link
from .joint import Joint
from .plugin import Plugin
from .gripper import Gripper
from .self_collide import SelfCollide
from .allow_auto_disable import AllowAutoDisable
from .include import Include
from .model import Model
from .enable_wind import EnableWind


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
        model: List["Model"] = None,
        enable_wind: "EnableWind" = None
    ):
        super().__init__(name=name)
        self.frame = frame or []
        self.pose = pose
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.gripper = gripper or []
        self.static = static
        self.self_collide = self_collide
        self.allow_auto_disable = allow_auto_disable
        self.include = include or []
        self.model = model or []
        self.enable_wind = enable_wind

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        for item in (self.link or []):
            el.append(item.to_sdf())
        for item in (self.joint or []):
            el.append(item.to_sdf())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        for item in (self.gripper or []):
            el.append(item.to_sdf())
        if self.static is not None:
            el.append(self.static.to_sdf())
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf())
        if self.allow_auto_disable is not None:
            el.append(self.allow_auto_disable.to_sdf())
        for item in (self.include or []):
            el.append(item.to_sdf())
        for item in (self.model or []):
            el.append(item.to_sdf())
        if self.enable_wind is not None:
            el.append(self.enable_wind.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        _base = _PrevModel.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _link = [Link.from_sdf(c) for c in el.findall("link")]
        _joint = [Joint.from_sdf(c) for c in el.findall("joint")]
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _gripper = [Gripper.from_sdf(c) for c in el.findall("gripper")]
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static) if _c_static is not None else None
        _c_self_collide = el.find("self_collide")
        _self_collide = SelfCollide.from_sdf(_c_self_collide) if _c_self_collide is not None else None
        _c_allow_auto_disable = el.find("allow_auto_disable")
        _allow_auto_disable = AllowAutoDisable.from_sdf(_c_allow_auto_disable) if _c_allow_auto_disable is not None else None
        _include = [Include.from_sdf(c) for c in el.findall("include")]
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        _c_enable_wind = el.find("enable_wind")
        _enable_wind = EnableWind.from_sdf(_c_enable_wind) if _c_enable_wind is not None else None
        return cls(name=_base.name, frame=_frame, pose=_pose, link=_link, joint=_joint, plugin=_plugin, gripper=_gripper, static=_static, self_collide=_self_collide, allow_auto_disable=_allow_auto_disable, include=_include, model=_model, enable_wind=_enable_wind)
