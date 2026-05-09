from __future__ import annotations

from xml.etree import ElementTree as ET

from .elevation import Elevation
from .heading_deg import HeadingDeg
from .latitude_deg import LatitudeDeg
from .longitude_deg import LongitudeDeg
from .surface_model import SurfaceModel
from .world_frame_orientation import WorldFrameOrientation
from ...sdf1_8.models.spherical_coordinates import SphericalCoordinates as _PrevSphericalCoordinates


class SphericalCoordinates(_PrevSphericalCoordinates):
    def __init__(
            self,
            surface_model: "SurfaceModel" = None,
            world_frame_orientation: "WorldFrameOrientation" = None,
            latitude_deg: "LatitudeDeg" = None,
            longitude_deg: "LongitudeDeg" = None,
            elevation: "Elevation" = None,
            heading_deg: "HeadingDeg" = None
    ):
        super().__init__(surface_model=surface_model, world_frame_orientation=world_frame_orientation,
                         latitude_deg=latitude_deg, longitude_deg=longitude_deg, elevation=elevation,
                         heading_deg=heading_deg)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SphericalCoordinates":
        _base = _PrevSphericalCoordinates.from_sdf(el)
        return cls(surface_model=_base.surface_model, world_frame_orientation=_base.world_frame_orientation,
                   latitude_deg=_base.latitude_deg, longitude_deg=_base.longitude_deg, elevation=_base.elevation,
                   heading_deg=_base.heading_deg)
