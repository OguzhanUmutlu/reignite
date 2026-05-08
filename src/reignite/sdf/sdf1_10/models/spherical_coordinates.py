from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.spherical_coordinates import SphericalCoordinates as _PrevSphericalCoordinates
from .surface_model import SurfaceModel
from .world_frame_orientation import WorldFrameOrientation
from .latitude_deg import LatitudeDeg
from .longitude_deg import LongitudeDeg
from .elevation import Elevation
from .surface_axis_equatorial import SurfaceAxisEquatorial
from .surface_axis_polar import SurfaceAxisPolar
from .heading_deg import HeadingDeg


class SphericalCoordinates(_PrevSphericalCoordinates):
    def __init__(
        self,
        surface_model: "SurfaceModel" = None,
        world_frame_orientation: "WorldFrameOrientation" = None,
        latitude_deg: "LatitudeDeg" = None,
        longitude_deg: "LongitudeDeg" = None,
        elevation: "Elevation" = None,
        surface_axis_equatorial: "SurfaceAxisEquatorial" = None,
        surface_axis_polar: "SurfaceAxisPolar" = None,
        heading_deg: "HeadingDeg" = None
    ):
        super().__init__(surface_model=surface_model, world_frame_orientation=world_frame_orientation, latitude_deg=latitude_deg, longitude_deg=longitude_deg, elevation=elevation, heading_deg=heading_deg)
        self.surface_axis_equatorial = surface_axis_equatorial
        self.surface_axis_polar = surface_axis_polar

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.surface_axis_equatorial is not None:
            el.append(self.surface_axis_equatorial.to_sdf())
        if self.surface_axis_polar is not None:
            el.append(self.surface_axis_polar.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SphericalCoordinates":
        _base = _PrevSphericalCoordinates.from_sdf(el)
        _c_surface_axis_equatorial = el.find("surface_axis_equatorial")
        _surface_axis_equatorial = SurfaceAxisEquatorial.from_sdf(_c_surface_axis_equatorial) if _c_surface_axis_equatorial is not None else None
        _c_surface_axis_polar = el.find("surface_axis_polar")
        _surface_axis_polar = SurfaceAxisPolar.from_sdf(_c_surface_axis_polar) if _c_surface_axis_polar is not None else None
        return cls(surface_model=_base.surface_model, world_frame_orientation=_base.world_frame_orientation, latitude_deg=_base.latitude_deg, longitude_deg=_base.longitude_deg, elevation=_base.elevation, surface_axis_equatorial=_surface_axis_equatorial, surface_axis_polar=_surface_axis_polar, heading_deg=_base.heading_deg)
