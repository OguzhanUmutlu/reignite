from __future__ import annotations

from xml.etree import ElementTree as ET

from .clip import Clip
from .depth_camera import DepthCamera
from .horizontal_fov import HorizontalFov
from .image import Image
from .pose import Pose
from .save import Save
from ..model import Model
from ...sdf1_3.models.camera import Camera as _PrevCamera


class Type(Model):
    def __init__(self, type: str = "gaussian"):
        self.type = type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _text = el.text or "gaussian"
        _type = _text
        return cls(type=_type)


class Noise(Model):
    def __init__(self, type: "Type" = None, mean: "Mean" = None, stddev: "Stddev" = None):
        self.type = type
        self.mean = mean
        self.stddev = stddev

    def to_sdf(self) -> ET.Element:
        el = ET.Element("noise")
        if self.type is not None:
            el.append(self.type.to_sdf())
        if self.mean is not None:
            el.append(self.mean.to_sdf())
        if self.stddev is not None:
            el.append(self.stddev.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Noise":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type) if _c_type is not None else None
        _c_mean = el.find("mean")
        _mean = Mean.from_sdf(_c_mean) if _c_mean is not None else None
        _c_stddev = el.find("stddev")
        _stddev = Stddev.from_sdf(_c_stddev) if _c_stddev is not None else None
        return cls(type=_type, mean=_mean, stddev=_stddev)


class Camera(_PrevCamera):
    def __init__(
            self,
            name: str = "__default__",
            pose: "Pose" = None,
            horizontal_fov: "HorizontalFov" = None,
            image: "Image" = None,
            clip: "Clip" = None,
            save: "Save" = None,
            depth_camera: "DepthCamera" = None,
            noise: "Noise" = None
    ):
        super().__init__(name=name, pose=pose, horizontal_fov=horizontal_fov, image=image, clip=clip, save=save,
                         depth_camera=depth_camera)
        self.noise = noise

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _base = _PrevCamera.from_sdf(el)
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        return cls(name=_base.name, pose=_base.pose, horizontal_fov=_base.horizontal_fov, image=_base.image,
                   clip=_base.clip, save=_base.save, depth_camera=_base.depth_camera, noise=_noise)
