from __future__ import annotations

from xml.etree import ElementTree as ET

from .granularity import Granularity
from .height import Height
from .scale import Scale
from .threshold import Threshold
from .uri import Uri
from ...sdf1_7.models.image import Image as _PrevImage


class Image(_PrevImage):
    def __init__(
            self,
            uri: "Uri" = None,
            scale: "Scale" = None,
            threshold: "Threshold" = None,
            height: "Height" = None,
            granularity: "Granularity" = None
    ):
        super().__init__(height=height)
        self.uri = uri
        self.scale = scale
        self.threshold = threshold
        self.granularity = granularity

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.uri is not None:
            el.append(self.uri.to_sdf())
        if self.scale is not None:
            el.append(self.scale.to_sdf())
        if self.threshold is not None:
            el.append(self.threshold.to_sdf())
        if self.granularity is not None:
            el.append(self.granularity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Image":
        _base = _PrevImage.from_sdf(el)
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri) if _c_uri is not None else None
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale) if _c_scale is not None else None
        _c_threshold = el.find("threshold")
        _threshold = Threshold.from_sdf(_c_threshold) if _c_threshold is not None else None
        _c_granularity = el.find("granularity")
        _granularity = Granularity.from_sdf(_c_granularity) if _c_granularity is not None else None
        return cls(uri=_uri, scale=_scale, threshold=_threshold, height=_base.height, granularity=_granularity)
