from __future__ import annotations

from xml.etree import ElementTree as ET

from .clip import Clip
from .depth_camera import DepthCamera
from .horizontal_fov import HorizontalFov
from .image import Image
from .save import Save
from ..model import Model


class Camera(Model):
    def __init__(
            self,
            horizontal_fov: "HorizontalFov" = None,
            image: "Image" = None,
            clip: "Clip" = None,
            save: "Save" = None,
            depth_camera: "DepthCamera" = None
    ):
        self.horizontal_fov = horizontal_fov
        self.image = image
        self.clip = clip
        self.save = save
        self.depth_camera = depth_camera

    def to_sdf(self) -> ET.Element:
        el = ET.Element("camera")
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf())
        if self.image is not None:
            el.append(self.image.to_sdf())
        if self.clip is not None:
            el.append(self.clip.to_sdf())
        if self.save is not None:
            el.append(self.save.to_sdf())
        if self.depth_camera is not None:
            el.append(self.depth_camera.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _c_horizontal_fov = el.find("horizontal_fov")
        _horizontal_fov = HorizontalFov.from_sdf(_c_horizontal_fov) if _c_horizontal_fov is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image) if _c_image is not None else None
        _c_clip = el.find("clip")
        _clip = Clip.from_sdf(_c_clip) if _c_clip is not None else None
        _c_save = el.find("save")
        _save = Save.from_sdf(_c_save) if _c_save is not None else None
        _c_depth_camera = el.find("depth_camera")
        _depth_camera = DepthCamera.from_sdf(_c_depth_camera) if _c_depth_camera is not None else None
        return cls(horizontal_fov=_horizontal_fov, image=_image, clip=_clip, save=_save, depth_camera=_depth_camera)
