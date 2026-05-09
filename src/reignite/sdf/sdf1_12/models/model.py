from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .allow_auto_disable import AllowAutoDisable
from .enable_wind import EnableWind
from .gripper import Gripper
from .include import Include
from .joint import Joint
from .link import Link
from .model import Model
from .model_state import ModelState
from .plugin import Plugin
from .self_collide import SelfCollide
from .static import Static
from ...sdf1_11.models.frame import Frame as _PrevFrame
from ...sdf1_11.models.model import Model as _PrevModel
from ...sdf1_11.models.pose import Pose as _PrevPose
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
        super().__init__(pose=pose, relative_to=relative_to, rotation_format=rotation_format, degrees=degrees)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        return cls(pose=_base.pose, relative_to=_base.relative_to, rotation_format=_base.rotation_format,
                   degrees=_base.degrees)


class Frame(_PrevFrame):
    def __init__(self, name: str = "", attached_to: str = "", pose: "Pose" = None):
        super().__init__()
        self.name = name
        self.attached_to = attached_to
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.name is not None:
            el.set("name", self.name)
        if self.attached_to is not None:
            el.set("attached_to", self.attached_to)
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frame":
        _name = el.get("name", "")
        _attached_to = el.get("attached_to", "")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_name, attached_to=_attached_to, pose=_pose)


class Model(_PrevModel):
    def __init__(
            self,
            name: str = "__default__",
            canonical_link: str = "",
            placement_frame: str = "",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            link: List["Link"] = None,
            joint: List["Joint"] = None,
            plugin: List["Plugin"] = None,
            gripper: List["Gripper"] = None,
            model_state: "ModelState" = None,
            static: "Static" = None,
            self_collide: "SelfCollide" = None,
            allow_auto_disable: "AllowAutoDisable" = None,
            include: List["Include"] = None,
            model: List["Model"] = None,
            enable_wind: "EnableWind" = None
    ):
        super().__init__(name=name)
        self.canonical_link = canonical_link
        self.placement_frame = placement_frame
        self.frame = frame or []
        self.pose = pose
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.gripper = gripper or []
        self.model_state = model_state
        self.static = static
        self.self_collide = self_collide
        self.allow_auto_disable = allow_auto_disable
        self.include = include or []
        self.model = model or []
        self.enable_wind = enable_wind

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.canonical_link is not None:
            el.set("canonical_link", self.canonical_link)
        if self.placement_frame is not None:
            el.set("placement_frame", self.placement_frame)
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
        if self.model_state is not None:
            el.append(self.model_state.to_sdf())
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
        _canonical_link = el.get("canonical_link", "")
        _placement_frame = el.get("placement_frame", "")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _link = [Link.from_sdf(c) for c in el.findall("link")]
        _joint = [Joint.from_sdf(c) for c in el.findall("joint")]
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _gripper = [Gripper.from_sdf(c) for c in el.findall("gripper")]
        _c_model_state = el.find("model_state")
        _model_state = ModelState.from_sdf(_c_model_state) if _c_model_state is not None else None
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static) if _c_static is not None else None
        _c_self_collide = el.find("self_collide")
        _self_collide = SelfCollide.from_sdf(_c_self_collide) if _c_self_collide is not None else None
        _c_allow_auto_disable = el.find("allow_auto_disable")
        _allow_auto_disable = AllowAutoDisable.from_sdf(
            _c_allow_auto_disable) if _c_allow_auto_disable is not None else None
        _include = [Include.from_sdf(c) for c in el.findall("include")]
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        _c_enable_wind = el.find("enable_wind")
        _enable_wind = EnableWind.from_sdf(_c_enable_wind) if _c_enable_wind is not None else None
        return cls(name=_base.name, canonical_link=_canonical_link, placement_frame=_placement_frame, frame=_frame,
                   pose=_pose, link=_link, joint=_joint, plugin=_plugin, gripper=_gripper, model_state=_model_state,
                   static=_static, self_collide=_self_collide, allow_auto_disable=_allow_auto_disable, include=_include,
                   model=_model, enable_wind=_enable_wind)
