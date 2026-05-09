from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .clip import Clip
from .depth_camera import DepthCamera
from .distortion import Distortion
from .frame import Frame
from .horizontal_fov import HorizontalFov
from .image import Image
from .lens import Lens
from .pose import Pose
from .save import Save
from ...sdf1_5.models.camera import Camera as _PrevCamera
from ...sdf1_5.models.noise import Noise as _PrevNoise


class Noise(_PrevNoise):
    def __init__(
            self,
            type: str = "none",
            mean: "Mean" = None,
            stddev: "Stddev" = None,
            bias_mean: "BiasMean" = None,
            bias_stddev: "BiasStddev" = None,
            dynamic_bias_stddev: "DynamicBiasStddev" = None,
            dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
            precision: "Precision" = None
    ):
        super().__init__(type=type, mean=mean, stddev=stddev)
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.dynamic_bias_stddev = dynamic_bias_stddev
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.precision = precision

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf())
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf())
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf())
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf())
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
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        _dynamic_bias_stddev = DynamicBiasStddev.from_sdf(
            _c_dynamic_bias_stddev) if _c_dynamic_bias_stddev is not None else None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        _dynamic_bias_correlation_time = DynamicBiasCorrelationTime.from_sdf(
            _c_dynamic_bias_correlation_time) if _c_dynamic_bias_correlation_time is not None else None
        _c_precision = el.find("precision")
        _precision = Precision.from_sdf(_c_precision) if _c_precision is not None else None
        return cls(type=_base.type, mean=_base.mean, stddev=_base.stddev, bias_mean=_bias_mean,
                   bias_stddev=_bias_stddev, dynamic_bias_stddev=_dynamic_bias_stddev,
                   dynamic_bias_correlation_time=_dynamic_bias_correlation_time, precision=_precision)


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
        super().__init__(name=name, frame=frame, pose=pose, horizontal_fov=horizontal_fov, image=image, clip=clip,
                         save=save, depth_camera=depth_camera, noise=noise, distortion=distortion, lens=lens)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _base = _PrevCamera.from_sdf(el)
        return cls(name=_base.name, frame=_base.frame, pose=_base.pose, horizontal_fov=_base.horizontal_fov,
                   image=_base.image, clip=_base.clip, save=_base.save, depth_camera=_base.depth_camera,
                   noise=_base.noise, distortion=_base.distortion, lens=_base.lens)
