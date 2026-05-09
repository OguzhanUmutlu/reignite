from __future__ import annotations

from xml.etree import ElementTree as ET

from .elevation import Elevation
from .heading_deg import HeadingDeg
from .latitude_deg import LatitudeDeg
from .longitude_deg import LongitudeDeg
from .surface_model import SurfaceModel
from ..model import Model


class SphericalCoordinates(Model):
    def __init__(
            self,
            surface_model: "SurfaceModel" = None,
            latitude_deg: "LatitudeDeg" = None,
            longitude_deg: "LongitudeDeg" = None,
            elevation: "Elevation" = None,
            heading_deg: "HeadingDeg" = None
    ):
        self.surface_model = surface_model
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.elevation = elevation
        self.heading_deg = heading_deg

    def to_sdf(self) -> ET.Element:
        el = ET.Element("spherical_coordinates")
        if self.surface_model is not None:
            el.append(self.surface_model.to_sdf())
        if self.latitude_deg is not None:
            el.append(self.latitude_deg.to_sdf())
        if self.longitude_deg is not None:
            el.append(self.longitude_deg.to_sdf())
        if self.elevation is not None:
            el.append(self.elevation.to_sdf())
        if self.heading_deg is not None:
            el.append(self.heading_deg.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SphericalCoordinates":
        _c_surface_model = el.find("surface_model")
        _surface_model = SurfaceModel.from_sdf(_c_surface_model) if _c_surface_model is not None else None
        _c_latitude_deg = el.find("latitude_deg")
        _latitude_deg = LatitudeDeg.from_sdf(_c_latitude_deg) if _c_latitude_deg is not None else None
        _c_longitude_deg = el.find("longitude_deg")
        _longitude_deg = LongitudeDeg.from_sdf(_c_longitude_deg) if _c_longitude_deg is not None else None
        _c_elevation = el.find("elevation")
        _elevation = Elevation.from_sdf(_c_elevation) if _c_elevation is not None else None
        _c_heading_deg = el.find("heading_deg")
        _heading_deg = HeadingDeg.from_sdf(_c_heading_deg) if _c_heading_deg is not None else None
        return cls(surface_model=_surface_model, latitude_deg=_latitude_deg, longitude_deg=_longitude_deg,
                   elevation=_elevation, heading_deg=_heading_deg)
