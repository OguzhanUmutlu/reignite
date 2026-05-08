from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_8.models.pose import Pose as _PrevPose
from ...sdf1_8.models.include import Include as _PrevInclude
from ....utils.pose import Pose
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


class Include(_PrevInclude):
    def __init__(
        self,
        merge: bool = False,
        pose: "Pose" = None,
        plugin: List["Plugin"] = None,
        uri: "Uri" = None,
        name: "Name" = None,
        static: "Static" = None,
        placement_frame: "PlacementFrame" = None
    ):
        super().__init__(pose=pose, plugin=plugin, uri=uri, name=name, static=static, placement_frame=placement_frame)
        self.merge = merge

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.merge is not None:
            el.set("merge", str(self.merge).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Include":
        _base = _PrevInclude.from_sdf(el)
        _merge = el.get("merge", False).strip().lower() == 'true'
        return cls(merge=_merge, pose=_base.pose, plugin=_base.plugin, uri=_base.uri, name=_base.name, static=_base.static, placement_frame=_base.placement_frame)
