from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .localization import Localization
from .custom_rpy import CustomRpy
from .grav_dir_x import GravDirX


class OrientationReferenceFrame(Model):
    def __init__(
        self,
        localization: "Localization" = None,
        custom_rpy: "CustomRpy" = None,
        grav_dir_x: "GravDirX" = None
    ):
        self.localization = localization
        self.custom_rpy = custom_rpy
        self.grav_dir_x = grav_dir_x

    def to_sdf(self) -> ET.Element:
        el = ET.Element("orientation_reference_frame")
        if self.localization is not None:
            el.append(self.localization.to_sdf())
        if self.custom_rpy is not None:
            el.append(self.custom_rpy.to_sdf())
        if self.grav_dir_x is not None:
            el.append(self.grav_dir_x.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "OrientationReferenceFrame":
        _c_localization = el.find("localization")
        _localization = Localization.from_sdf(_c_localization) if _c_localization is not None else None
        _c_custom_rpy = el.find("custom_rpy")
        _custom_rpy = CustomRpy.from_sdf(_c_custom_rpy) if _c_custom_rpy is not None else None
        _c_grav_dir_x = el.find("grav_dir_x")
        _grav_dir_x = GravDirX.from_sdf(_c_grav_dir_x) if _c_grav_dir_x is not None else None
        return cls(localization=_localization, custom_rpy=_custom_rpy, grav_dir_x=_grav_dir_x)
