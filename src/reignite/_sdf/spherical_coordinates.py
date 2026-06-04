### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


# noinspection PyUnusedImports
class SphericalCoordinates(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        elevation: float | None = None,
        heading_deg: float | None = None,
        latitude_deg: float | None = None,
        longitude_deg: float | None = None,
        surface_axis_equatorial: float | None = None,
        surface_axis_polar: float | None = None,
        surface_model: str | None = None,
        world_frame_orientation: str | None = None
    ):
        super().__init__(sdf_version)
        self.elevation = elevation
        self.heading_deg = heading_deg
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.surface_axis_equatorial = surface_axis_equatorial
        self.surface_axis_polar = surface_axis_polar
        self.surface_model = surface_model
        self.world_frame_orientation = world_frame_orientation

    def to_version(self, target_version: str) -> "SphericalCoordinates":
        if self.surface_axis_equatorial is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'surface_axis_equatorial' is not supported in SDF version {target_version} (added in 1.10)")
        if self.surface_axis_polar is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'surface_axis_polar' is not supported in SDF version {target_version} (added in 1.10)")
        if self.world_frame_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'world_frame_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs: dict = {"sdf_version": target_version, "elevation": self.elevation, "heading_deg": self.heading_deg, "latitude_deg": self.latitude_deg, "longitude_deg": self.longitude_deg, "surface_axis_equatorial": self.surface_axis_equatorial, "surface_axis_polar": self.surface_axis_polar, "surface_model": self.surface_model, "world_frame_orientation": self.world_frame_orientation}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("spherical_coordinates")
        if self.elevation is not None:
            _c_tmp = ET.Element("elevation")
            _c_tmp.text = str(self.elevation)
            el.append(_c_tmp)
        if self.heading_deg is not None:
            _c_tmp = ET.Element("heading_deg")
            _c_tmp.text = str(self.heading_deg)
            el.append(_c_tmp)
        if self.latitude_deg is not None:
            _c_tmp = ET.Element("latitude_deg")
            _c_tmp.text = str(self.latitude_deg)
            el.append(_c_tmp)
        if self.longitude_deg is not None:
            _c_tmp = ET.Element("longitude_deg")
            _c_tmp.text = str(self.longitude_deg)
            el.append(_c_tmp)
        if self.surface_axis_equatorial is not None:
            _c_tmp = ET.Element("surface_axis_equatorial")
            _c_tmp.text = str(self.surface_axis_equatorial)
            el.append(_c_tmp)
        if self.surface_axis_polar is not None:
            _c_tmp = ET.Element("surface_axis_polar")
            _c_tmp.text = str(self.surface_axis_polar)
            el.append(_c_tmp)
        if self.surface_model is not None:
            _c_tmp = ET.Element("surface_model")
            _c_tmp.text = self.surface_model
            el.append(_c_tmp)
        if self.world_frame_orientation is not None:
            _c_tmp = ET.Element("world_frame_orientation")
            _c_tmp.text = self.world_frame_orientation
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "SphericalCoordinates | SDFError":
        _c_tmp = el.find("elevation")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("elevation")
            _elevation = _val
        else:
            _elevation = None
        _c_tmp = el.find("heading_deg")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("heading_deg")
            _heading_deg = _val
        else:
            _heading_deg = None
        _c_tmp = el.find("latitude_deg")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("latitude_deg")
            _latitude_deg = _val
        else:
            _latitude_deg = None
        _c_tmp = el.find("longitude_deg")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("longitude_deg")
            _longitude_deg = _val
        else:
            _longitude_deg = None
        _c_tmp = el.find("surface_axis_equatorial")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("surface_axis_equatorial")
            _surface_axis_equatorial = _val
        else:
            _surface_axis_equatorial = None
        if _surface_axis_equatorial is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'surface_axis_equatorial' is not supported in SDF version {version} (added in 1.10)")
        _c_tmp = el.find("surface_axis_polar")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("surface_axis_polar")
            _surface_axis_polar = _val
        else:
            _surface_axis_polar = None
        if _surface_axis_polar is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'surface_axis_polar' is not supported in SDF version {version} (added in 1.10)")
        _c_tmp = el.find("surface_model")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "EARTH_WGS84"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("surface_model")
            _surface_model = _val
        else:
            _surface_model = None
        _c_tmp = el.find("world_frame_orientation")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "ENU"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("world_frame_orientation")
            _world_frame_orientation = _val
        else:
            _world_frame_orientation = None
        if _world_frame_orientation is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'world_frame_orientation' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, elevation=_elevation, heading_deg=_heading_deg, latitude_deg=_latitude_deg, longitude_deg=_longitude_deg, surface_axis_equatorial=_surface_axis_equatorial, surface_axis_polar=_surface_axis_polar, surface_model=_surface_model, world_frame_orientation=_world_frame_orientation)
