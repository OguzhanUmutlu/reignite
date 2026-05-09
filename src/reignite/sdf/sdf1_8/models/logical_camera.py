from __future__ import annotations

from xml.etree import ElementTree as ET

from .aspect_ratio import AspectRatio
from .far import Far
from .horizontal_fov import HorizontalFov
from .near import Near
from ...sdf1_7.models.logical_camera import LogicalCamera as _PrevLogicalCamera


class LogicalCamera(_PrevLogicalCamera):
    def __init__(
            self,
            near: "Near" = None,
            far: "Far" = None,
            aspect_ratio: "AspectRatio" = None,
            horizontal_fov: "HorizontalFov" = None
    ):
        super().__init__(near=near, far=far, aspect_ratio=aspect_ratio, horizontal_fov=horizontal_fov)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LogicalCamera":
        _base = _PrevLogicalCamera.from_sdf(el)
        return cls(near=_base.near, far=_base.far, aspect_ratio=_base.aspect_ratio, horizontal_fov=_base.horizontal_fov)
