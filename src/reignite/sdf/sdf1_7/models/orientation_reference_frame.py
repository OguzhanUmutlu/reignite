from __future__ import annotations

from xml.etree import ElementTree as ET

from .custom_rpy import CustomRpy
from .grav_dir_x import GravDirX
from .localization import Localization
from ...sdf1_6.models.orientation_reference_frame import OrientationReferenceFrame as _PrevOrientationReferenceFrame


class OrientationReferenceFrame(_PrevOrientationReferenceFrame):
    def __init__(
            self,
            localization: "Localization" = None,
            custom_rpy: "CustomRpy" = None,
            grav_dir_x: "GravDirX" = None
    ):
        super().__init__(localization=localization, custom_rpy=custom_rpy, grav_dir_x=grav_dir_x)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "OrientationReferenceFrame":
        _base = _PrevOrientationReferenceFrame.from_sdf(el)
        return cls(localization=_base.localization, custom_rpy=_base.custom_rpy, grav_dir_x=_base.grav_dir_x)
