from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .name import Name
from .placement_frame import PlacementFrame
from .plugin import Plugin
from .static import Static
from .uri import Uri
from ...sdf1_7.models.include import Include as _PrevInclude
from ...sdf1_7.models.pose import Pose as _PrevPose
from ....utils.pose import Pose


class Pose(_PrevPose):
    def __init__(self, pose: Pose = None, relative_to: str = ""):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose, relative_to=relative_to)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        return cls(pose=_base.pose, relative_to=_base.relative_to)


class Include(_PrevInclude):
    def __init__(
            self,
            pose: "Pose" = None,
            plugin: List["Plugin"] = None,
            uri: "Uri" = None,
            name: "Name" = None,
            static: "Static" = None,
            placement_frame: "PlacementFrame" = None
    ):
        super().__init__(pose=pose, plugin=plugin, uri=uri, name=name, static=static)
        self.placement_frame = placement_frame

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.placement_frame is not None:
            el.append(self.placement_frame.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Include":
        _base = _PrevInclude.from_sdf(el)
        _c_placement_frame = el.find("placement_frame")
        _placement_frame = PlacementFrame.from_sdf(_c_placement_frame) if _c_placement_frame is not None else None
        return cls(pose=_base.pose, plugin=_base.plugin, uri=_base.uri, name=_base.name, static=_base.static,
                   placement_frame=_placement_frame)
