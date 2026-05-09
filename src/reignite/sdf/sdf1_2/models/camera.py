from __future__ import annotations

from xml.etree import ElementTree as ET

from .clip import Clip
from .depth_camera import DepthCamera
from .horizontal_fov import HorizontalFov
from .image import Image
from .save import Save
from ...sdf1_0.models.camera import Camera as _PrevCamera


class Camera(_PrevCamera):
    def __init__(
            self,
            horizontal_fov: "HorizontalFov" = None,
            image: "Image" = None,
            clip: "Clip" = None,
            save: "Save" = None,
            depth_camera: "DepthCamera" = None
    ):
        super().__init__(horizontal_fov=horizontal_fov, image=image, clip=clip, save=save, depth_camera=depth_camera)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _base = _PrevCamera.from_sdf(el)
        return cls(horizontal_fov=_base.horizontal_fov, image=_base.image, clip=_base.clip, save=_base.save,
                   depth_camera=_base.depth_camera)
