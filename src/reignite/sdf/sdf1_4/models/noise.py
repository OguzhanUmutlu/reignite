from __future__ import annotations

from xml.etree import ElementTree as ET

from .bias_mean import BiasMean
from .bias_stddev import BiasStddev
from .mean import Mean
from .precision import Precision
from .stddev import Stddev
from ..model import Model


class Noise(Model):
    def __init__(
            self,
            type: str = "none",
            mean: "Mean" = None,
            stddev: "Stddev" = None,
            bias_mean: "BiasMean" = None,
            bias_stddev: "BiasStddev" = None,
            precision: "Precision" = None
    ):
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision

    def to_sdf(self) -> ET.Element:
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf())
        if self.stddev is not None:
            el.append(self.stddev.to_sdf())
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf())
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf())
        if self.precision is not None:
            el.append(self.precision.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Noise":
        _type = el.get("type", "none")
        _c_mean = el.find("mean")
        _mean = Mean.from_sdf(_c_mean) if _c_mean is not None else None
        _c_stddev = el.find("stddev")
        _stddev = Stddev.from_sdf(_c_stddev) if _c_stddev is not None else None
        _c_bias_mean = el.find("bias_mean")
        _bias_mean = BiasMean.from_sdf(_c_bias_mean) if _c_bias_mean is not None else None
        _c_bias_stddev = el.find("bias_stddev")
        _bias_stddev = BiasStddev.from_sdf(_c_bias_stddev) if _c_bias_stddev is not None else None
        _c_precision = el.find("precision")
        _precision = Precision.from_sdf(_c_precision) if _c_precision is not None else None
        return cls(type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev,
                   precision=_precision)
