from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_3.models.horizontal import Horizontal as _PrevHorizontal
from ...sdf1_3.models.scan import Scan as _PrevScan
from ...sdf1_3.models.vertical import Vertical as _PrevVertical


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


class Scan(_PrevScan):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        super().__init__(horizontal=horizontal, vertical=vertical)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scan":
        _base = _PrevScan.from_sdf(el)
        return cls(horizontal=_base.horizontal, vertical=_base.vertical)
