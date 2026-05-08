from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.noise import Noise as _PrevNoise
from .mean import Mean
from .stddev import Stddev
from .bias_mean import BiasMean
from .bias_stddev import BiasStddev
from .precision import Precision


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
        super().__init__(type=type, mean=mean, stddev=stddev, bias_mean=bias_mean, bias_stddev=bias_stddev, precision=precision)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Noise":
        _base = _PrevNoise.from_sdf(el)
        return cls(type=_base.type, mean=_base.mean, stddev=_base.stddev, bias_mean=_base.bias_mean, bias_stddev=_base.bias_stddev, precision=_base.precision)
