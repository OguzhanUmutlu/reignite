from __future__ import annotations

from xml.etree import ElementTree as ET

from .max_dist import MaxDist
from .min_dist import MinDist
from .name import Name
from ...sdf1_3.models.track_visual import TrackVisual as _PrevTrackVisual


class TrackVisual(_PrevTrackVisual):
    def __init__(self, name: "Name" = None, min_dist: "MinDist" = None, max_dist: "MaxDist" = None):
        super().__init__(name=name, min_dist=min_dist, max_dist=max_dist)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "TrackVisual":
        _base = _PrevTrackVisual.from_sdf(el)
        return cls(name=_base.name, min_dist=_base.min_dist, max_dist=_base.max_dist)
