from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.noise import Noise as _PrevNoise
from ...sdf1_4.models.imu import Imu as _PrevImu
from .topic import Topic
from .angular_velocity import AngularVelocity
from .linear_acceleration import LinearAcceleration


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


class Imu(_PrevImu):
    def __init__(
        self,
        topic: "Topic" = None,
        angular_velocity: "AngularVelocity" = None,
        linear_acceleration: "LinearAcceleration" = None,
        noise: "Noise" = None
    ):
        super().__init__(topic=topic, noise=noise)
        self.angular_velocity = angular_velocity
        self.linear_acceleration = linear_acceleration

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf())
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Imu":
        _base = _PrevImu.from_sdf(el)
        _c_angular_velocity = el.find("angular_velocity")
        _angular_velocity = AngularVelocity.from_sdf(_c_angular_velocity) if _c_angular_velocity is not None else None
        _c_linear_acceleration = el.find("linear_acceleration")
        _linear_acceleration = LinearAcceleration.from_sdf(_c_linear_acceleration) if _c_linear_acceleration is not None else None
        return cls(topic=_base.topic, angular_velocity=_angular_velocity, linear_acceleration=_linear_acceleration, noise=_base.noise)
