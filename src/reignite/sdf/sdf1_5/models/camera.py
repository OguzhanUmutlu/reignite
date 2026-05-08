from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_4.models.noise import Noise as _PrevNoise
from ...sdf1_4.models.camera import Camera as _PrevCamera
from .frame import Frame
from .pose import Pose
from .horizontal_fov import HorizontalFov
from .image import Image
from .clip import Clip
from .save import Save
from .depth_camera import DepthCamera
from .distortion import Distortion
from .lens import Lens


class Noise(_PrevNoise):
    def __init__(
        self,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None
    ):
        super().__init__(type=type, mean=mean, stddev=stddev)
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf())
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf())
        if self.precision is not None:
            el.append(self.precision.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Noise":
        _base = _PrevNoise.from_sdf(el)
        _c_bias_mean = el.find("bias_mean")
        _bias_mean = BiasMean.from_sdf(_c_bias_mean) if _c_bias_mean is not None else None
        _c_bias_stddev = el.find("bias_stddev")
        _bias_stddev = BiasStddev.from_sdf(_c_bias_stddev) if _c_bias_stddev is not None else None
        _c_precision = el.find("precision")
        _precision = Precision.from_sdf(_c_precision) if _c_precision is not None else None
        return cls(type=_base.type, mean=_base.mean, stddev=_base.stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision)


class Camera(_PrevCamera):
    def __init__(
        self,
        name: str = "__default__",
        frame: List["Frame"] = None,
        pose: "Pose" = None,
        horizontal_fov: "HorizontalFov" = None,
        image: "Image" = None,
        clip: "Clip" = None,
        save: "Save" = None,
        depth_camera: "DepthCamera" = None,
        noise: "Noise" = None,
        distortion: "Distortion" = None,
        lens: "Lens" = None
    ):
        super().__init__(name=name, pose=pose, horizontal_fov=horizontal_fov, image=image, clip=clip, save=save, depth_camera=depth_camera, noise=noise)
        self.frame = frame or []
        self.distortion = distortion
        self.lens = lens

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.distortion is not None:
            el.append(self.distortion.to_sdf())
        if self.lens is not None:
            el.append(self.lens.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _base = _PrevCamera.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_distortion = el.find("distortion")
        _distortion = Distortion.from_sdf(_c_distortion) if _c_distortion is not None else None
        _c_lens = el.find("lens")
        _lens = Lens.from_sdf(_c_lens) if _c_lens is not None else None
        return cls(name=_base.name, frame=_frame, pose=_base.pose, horizontal_fov=_base.horizontal_fov, image=_base.image, clip=_base.clip, save=_base.save, depth_camera=_base.depth_camera, noise=_base.noise, distortion=_distortion, lens=_lens)
