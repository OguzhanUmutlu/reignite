from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.type import Type as _PrevType
from .scale_to_hfov import ScaleToHfov
from .custom_function import CustomFunction
from .cutoff_angle import CutoffAngle
from .env_texture_size import EnvTextureSize


class Type(_PrevType):
    def __init__(self, type: str = "stereographic"):
        super().__init__(type=type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _base = _PrevType.from_sdf(el)
        return cls(type=_base.type)


class Lens(Model):
    def __init__(
        self,
        type: "Type" = None,
        scale_to_hfov: "ScaleToHfov" = None,
        custom_function: "CustomFunction" = None,
        cutoff_angle: "CutoffAngle" = None,
        env_texture_size: "EnvTextureSize" = None
    ):
        self.type = type
        self.scale_to_hfov = scale_to_hfov
        self.custom_function = custom_function
        self.cutoff_angle = cutoff_angle
        self.env_texture_size = env_texture_size

    def to_sdf(self) -> ET.Element:
        el = ET.Element("lens")
        if self.type is not None:
            el.append(self.type.to_sdf())
        if self.scale_to_hfov is not None:
            el.append(self.scale_to_hfov.to_sdf())
        if self.custom_function is not None:
            el.append(self.custom_function.to_sdf())
        if self.cutoff_angle is not None:
            el.append(self.cutoff_angle.to_sdf())
        if self.env_texture_size is not None:
            el.append(self.env_texture_size.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Lens":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type) if _c_type is not None else None
        _c_scale_to_hfov = el.find("scale_to_hfov")
        _scale_to_hfov = ScaleToHfov.from_sdf(_c_scale_to_hfov) if _c_scale_to_hfov is not None else None
        _c_custom_function = el.find("custom_function")
        _custom_function = CustomFunction.from_sdf(_c_custom_function) if _c_custom_function is not None else None
        _c_cutoff_angle = el.find("cutoff_angle")
        _cutoff_angle = CutoffAngle.from_sdf(_c_cutoff_angle) if _c_cutoff_angle is not None else None
        _c_env_texture_size = el.find("env_texture_size")
        _env_texture_size = EnvTextureSize.from_sdf(_c_env_texture_size) if _c_env_texture_size is not None else None
        return cls(type=_type, scale_to_hfov=_scale_to_hfov, custom_function=_custom_function, cutoff_angle=_cutoff_angle, env_texture_size=_env_texture_size)
