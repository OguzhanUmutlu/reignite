from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.xyz import Xyz as _PrevXyz
from ...sdf1_10.models.track_visual import TrackVisual as _PrevTrackVisual
from ....utils.vector3 import Vector3
from .name import Name
from .min_dist import MinDist
from .max_dist import MaxDist
from .static import Static
from .use_model_frame import UseModelFrame
from .inherit_yaw import InheritYaw


class Xyz(_PrevXyz):
    def __init__(self, xyz: Vector3 = None):
        if xyz is None:
            xyz = Vector3.from_sdf("-5.0 0.0 3.0")
        super().__init__(xyz=xyz)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Xyz":
        _base = _PrevXyz.from_sdf(el)
        return cls(xyz=_base.xyz)


class TrackVisual(_PrevTrackVisual):
    def __init__(
        self,
        name: "Name" = None,
        min_dist: "MinDist" = None,
        max_dist: "MaxDist" = None,
        static: "Static" = None,
        use_model_frame: "UseModelFrame" = None,
        xyz: "Xyz" = None,
        inherit_yaw: "InheritYaw" = None
    ):
        super().__init__(name=name, min_dist=min_dist, max_dist=max_dist, static=static, use_model_frame=use_model_frame, xyz=xyz, inherit_yaw=inherit_yaw)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "TrackVisual":
        _base = _PrevTrackVisual.from_sdf(el)
        return cls(name=_base.name, min_dist=_base.min_dist, max_dist=_base.max_dist, static=_base.static, use_model_frame=_base.use_model_frame, xyz=_base.xyz, inherit_yaw=_base.inherit_yaw)
