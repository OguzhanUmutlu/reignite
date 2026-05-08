from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.lens import Lens as _PrevLens
from .type import Type
from .scale_to_hfov import ScaleToHfov
from .custom_function import CustomFunction
from .cutoff_angle import CutoffAngle
from .env_texture_size import EnvTextureSize
from .intrinsics import Intrinsics
from .projection import Projection


class Lens(_PrevLens):
    def __init__(
        self,
        type: "Type" = None,
        scale_to_hfov: "ScaleToHfov" = None,
        custom_function: "CustomFunction" = None,
        cutoff_angle: "CutoffAngle" = None,
        env_texture_size: "EnvTextureSize" = None,
        intrinsics: "Intrinsics" = None,
        projection: "Projection" = None
    ):
        super().__init__(type=type, scale_to_hfov=scale_to_hfov, custom_function=custom_function, cutoff_angle=cutoff_angle, env_texture_size=env_texture_size, intrinsics=intrinsics)
        self.projection = projection

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.projection is not None:
            el.append(self.projection.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Lens":
        _base = _PrevLens.from_sdf(el)
        _c_projection = el.find("projection")
        _projection = Projection.from_sdf(_c_projection) if _c_projection is not None else None
        return cls(type=_base.type, scale_to_hfov=_base.scale_to_hfov, custom_function=_base.custom_function, cutoff_angle=_base.cutoff_angle, env_texture_size=_base.env_texture_size, intrinsics=_base.intrinsics, projection=_projection)
