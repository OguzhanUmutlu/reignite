from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.static import Static as _PrevStatic
from ...sdf1_5.models.xyz import Xyz as _PrevXyz
from ...sdf1_5.models.track_visual import TrackVisual as _PrevTrackVisual
from ....utils.vector3 import Vector3
from .name import Name
from .min_dist import MinDist
from .max_dist import MaxDist
from .use_model_frame import UseModelFrame
from .inherit_yaw import InheritYaw


class Static(_PrevStatic):
    def __init__(self, static: bool = False):
        super().__init__(static=static)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Static":
        _base = _PrevStatic.from_sdf(el)
        return cls(static=_base.static)


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
        super().__init__(name=name, min_dist=min_dist, max_dist=max_dist)
        self.static = static
        self.use_model_frame = use_model_frame
        self.xyz = xyz
        self.inherit_yaw = inherit_yaw

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.static is not None:
            el.append(self.static.to_sdf())
        if self.use_model_frame is not None:
            el.append(self.use_model_frame.to_sdf())
        if self.xyz is not None:
            el.append(self.xyz.to_sdf())
        if self.inherit_yaw is not None:
            el.append(self.inherit_yaw.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "TrackVisual":
        _base = _PrevTrackVisual.from_sdf(el)
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static) if _c_static is not None else None
        _c_use_model_frame = el.find("use_model_frame")
        _use_model_frame = UseModelFrame.from_sdf(_c_use_model_frame) if _c_use_model_frame is not None else None
        _c_xyz = el.find("xyz")
        _xyz = Xyz.from_sdf(_c_xyz) if _c_xyz is not None else None
        _c_inherit_yaw = el.find("inherit_yaw")
        _inherit_yaw = InheritYaw.from_sdf(_c_inherit_yaw) if _c_inherit_yaw is not None else None
        return cls(name=_base.name, min_dist=_base.min_dist, max_dist=_base.max_dist, static=_static, use_model_frame=_use_model_frame, xyz=_xyz, inherit_yaw=_inherit_yaw)
