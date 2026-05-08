from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_11.models.pose import Pose as _PrevPose
from ...sdf1_11.models.include import Include as _PrevInclude
from ....utils.pose import Pose
from .model_state import ModelState
from .plugin import Plugin
from .uri import Uri
from .name import Name
from .static import Static
from .placement_frame import PlacementFrame


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
        return cls(pose=_base.pose, relative_to=_base.relative_to, rotation_format=_base.rotation_format, degrees=_base.degrees)


class Include(_PrevInclude):
    def __init__(
        self,
        merge: bool = False,
        model_state: "ModelState" = None,
        pose: "Pose" = None,
        plugin: List["Plugin"] = None,
        uri: "Uri" = None,
        name: "Name" = None,
        static: "Static" = None,
        placement_frame: "PlacementFrame" = None
    ):
        super().__init__(merge=merge, pose=pose, plugin=plugin, uri=uri, name=name, static=static, placement_frame=placement_frame)
        self.model_state = model_state

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.model_state is not None:
            el.append(self.model_state.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Include":
        _base = _PrevInclude.from_sdf(el)
        _c_model_state = el.find("model_state")
        _model_state = ModelState.from_sdf(_c_model_state) if _c_model_state is not None else None
        return cls(merge=_base.merge, model_state=_model_state, pose=_base.pose, plugin=_base.plugin, uri=_base.uri, name=_base.name, static=_base.static, placement_frame=_base.placement_frame)
