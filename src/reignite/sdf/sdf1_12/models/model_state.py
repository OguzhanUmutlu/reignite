from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .joint_state import JointState
from .link_state import LinkState
from .model_state import ModelState
from .scale import Scale
from ..model import Model
from ...sdf1_11.models.frame import Frame as _PrevFrame
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


class ModelState(Model):
    def __init__(
            self,
            name: str = "__default__",
            joint_state: List["JointState"] = None,
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            link_state: List["LinkState"] = None,
            model_state: List["ModelState"] = None,
            scale: "Scale" = None
    ):
        self.name = name
        self.joint_state = joint_state or []
        self.frame = frame or []
        self.pose = pose
        self.link_state = link_state or []
        self.model_state = model_state or []
        self.scale = scale

    def to_sdf(self) -> ET.Element:
        el = ET.Element("model_state")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.joint_state or []):
            el.append(item.to_sdf())
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        for item in (self.link_state or []):
            el.append(item.to_sdf())
        for item in (self.model_state or []):
            el.append(item.to_sdf())
        if self.scale is not None:
            el.append(self.scale.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ModelState":
        _name = el.get("name", "__default__")
        _joint_state = [JointState.from_sdf(c) for c in el.findall("joint_state")]
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _link_state = [LinkState.from_sdf(c) for c in el.findall("link_state")]
        _model_state = [ModelState.from_sdf(c) for c in el.findall("model_state")]
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale) if _c_scale is not None else None
        return cls(name=_name, joint_state=_joint_state, frame=_frame, pose=_pose, link_state=_link_state,
                   model_state=_model_state, scale=_scale)
