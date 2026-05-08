from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .near import Near
from .far import Far
from .aspect_ratio import AspectRatio
from .horizontal_fov import HorizontalFov


class LogicalCamera(Model):
    def __init__(
        self,
        near: "Near" = None,
        far: "Far" = None,
        aspect_ratio: "AspectRatio" = None,
        horizontal_fov: "HorizontalFov" = None
    ):
        self.near = near
        self.far = far
        self.aspect_ratio = aspect_ratio
        self.horizontal_fov = horizontal_fov

    def to_sdf(self) -> ET.Element:
        el = ET.Element("logical_camera")
        if self.near is not None:
            el.append(self.near.to_sdf())
        if self.far is not None:
            el.append(self.far.to_sdf())
        if self.aspect_ratio is not None:
            el.append(self.aspect_ratio.to_sdf())
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LogicalCamera":
        _c_near = el.find("near")
        _near = Near.from_sdf(_c_near) if _c_near is not None else None
        _c_far = el.find("far")
        _far = Far.from_sdf(_c_far) if _c_far is not None else None
        _c_aspect_ratio = el.find("aspect_ratio")
        _aspect_ratio = AspectRatio.from_sdf(_c_aspect_ratio) if _c_aspect_ratio is not None else None
        _c_horizontal_fov = el.find("horizontal_fov")
        _horizontal_fov = HorizontalFov.from_sdf(_c_horizontal_fov) if _c_horizontal_fov is not None else None
        return cls(near=_near, far=_far, aspect_ratio=_aspect_ratio, horizontal_fov=_horizontal_fov)
