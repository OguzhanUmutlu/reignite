from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.bias_mean import BiasMean as _PrevBiasMean
from ...sdf1_6.models.bias_stddev import BiasStddev as _PrevBiasStddev
from ...sdf1_6.models.dynamic_bias_correlation_time import DynamicBiasCorrelationTime as _PrevDynamicBiasCorrelationTime
from ...sdf1_6.models.dynamic_bias_stddev import DynamicBiasStddev as _PrevDynamicBiasStddev
from ...sdf1_6.models.horizontal import Horizontal as _PrevHorizontal
from ...sdf1_6.models.mean import Mean as _PrevMean
from ...sdf1_6.models.noise import Noise as _PrevNoise
from ...sdf1_6.models.position_sensing import PositionSensing as _PrevPositionSensing
from ...sdf1_6.models.precision import Precision as _PrevPrecision
from ...sdf1_6.models.stddev import Stddev as _PrevStddev
from ...sdf1_6.models.velocity_sensing import VelocitySensing as _PrevVelocitySensing
from ...sdf1_6.models.vertical import Vertical as _PrevVertical


def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class Mean(_PrevMean):
    def __init__(self, mean: float = 0.0):
        super().__init__(mean=mean)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mean":
        _base = _PrevMean.from_sdf(el)
        return cls(mean=_base.mean)


class Stddev(_PrevStddev):
    def __init__(self, stddev: float = 0.0):
        super().__init__(stddev=stddev)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Stddev":
        _base = _PrevStddev.from_sdf(el)
        return cls(stddev=_base.stddev)


class BiasMean(_PrevBiasMean):
    def __init__(self, bias_mean: float = 0.0):
        super().__init__(bias_mean=bias_mean)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "BiasMean":
        _base = _PrevBiasMean.from_sdf(el)
        return cls(bias_mean=_base.bias_mean)


class BiasStddev(_PrevBiasStddev):
    def __init__(self, bias_stddev: float = 0.0):
        super().__init__(bias_stddev=bias_stddev)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "BiasStddev":
        _base = _PrevBiasStddev.from_sdf(el)
        return cls(bias_stddev=_base.bias_stddev)


class DynamicBiasStddev(_PrevDynamicBiasStddev):
    def __init__(self, dynamic_bias_stddev: float = 0.0):
        super().__init__(dynamic_bias_stddev=dynamic_bias_stddev)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DynamicBiasStddev":
        _base = _PrevDynamicBiasStddev.from_sdf(el)
        return cls(dynamic_bias_stddev=_base.dynamic_bias_stddev)


class DynamicBiasCorrelationTime(_PrevDynamicBiasCorrelationTime):
    def __init__(self, dynamic_bias_correlation_time: float = 0.0):
        super().__init__(dynamic_bias_correlation_time=dynamic_bias_correlation_time)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DynamicBiasCorrelationTime":
        _base = _PrevDynamicBiasCorrelationTime.from_sdf(el)
        return cls(dynamic_bias_correlation_time=_base.dynamic_bias_correlation_time)


class Precision(_PrevPrecision):
    def __init__(self, precision: float = 0.0):
        super().__init__(precision=precision)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Precision":
        _base = _PrevPrecision.from_sdf(el)
        return cls(precision=_base.precision)


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


class Horizontal(_PrevHorizontal):
    def __init__(self, noise: "Noise" = None):
        super().__init__()
        self.noise = noise

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Horizontal":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        return cls(noise=_noise)


class Vertical(_PrevVertical):
    def __init__(self, noise: "Noise" = None):
        super().__init__()
        self.noise = noise

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Vertical":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        return cls(noise=_noise)


class PositionSensing(_PrevPositionSensing):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        super().__init__(horizontal=horizontal, vertical=vertical)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PositionSensing":
        _base = _PrevPositionSensing.from_sdf(el)
        return cls(horizontal=_base.horizontal, vertical=_base.vertical)


class VelocitySensing(_PrevVelocitySensing):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        super().__init__(horizontal=horizontal, vertical=vertical)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VelocitySensing":
        _base = _PrevVelocitySensing.from_sdf(el)
        return cls(horizontal=_base.horizontal, vertical=_base.vertical)


class Navsat(Model):
    def __init__(
            self,
            position_sensing: "PositionSensing" = None,
            velocity_sensing: "VelocitySensing" = None
    ):
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_sdf(self) -> ET.Element:
        el = ET.Element("navsat")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf())
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Navsat":
        _c_position_sensing = el.find("position_sensing")
        _position_sensing = PositionSensing.from_sdf(_c_position_sensing) if _c_position_sensing is not None else None
        _c_velocity_sensing = el.find("velocity_sensing")
        _velocity_sensing = VelocitySensing.from_sdf(_c_velocity_sensing) if _c_velocity_sensing is not None else None
        return cls(position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)
