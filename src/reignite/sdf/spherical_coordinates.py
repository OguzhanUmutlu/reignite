### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import Model
from ..utils.version import cmp_version


import math

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > math.inf:
        raise ValueError(f"double out of range: {raw}")
    return v



class SurfaceModel(Model):
    def __init__(self, sdf_version: str, surface_model: str = "EARTH_WGS84"):
        self.__version__ = sdf_version
        self.surface_model = surface_model

    def to_version(self, target_version: str) -> "SurfaceModel":
        kwargs = {"sdf_version": target_version}
        kwargs["surface_model"] = self.surface_model
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface_model")
        if self.surface_model is not None:
            el.text = self.surface_model
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SurfaceModel":
        _text = el.text or "EARTH_WGS84"
        _surface_model = _text
        return cls(sdf_version=version, surface_model=_surface_model)


class LatitudeDeg(Model):
    def __init__(self, sdf_version: str, latitude_deg: float = 0.0):
        self.__version__ = sdf_version
        self.latitude_deg = latitude_deg

    def to_version(self, target_version: str) -> "LatitudeDeg":
        kwargs = {"sdf_version": target_version}
        kwargs["latitude_deg"] = self.latitude_deg
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("latitude_deg")
        if self.latitude_deg is not None:
            el.text = str(self.latitude_deg)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LatitudeDeg":
        _text = el.text or 0.0
        _latitude_deg = _parse_double(_text)
        return cls(sdf_version=version, latitude_deg=_latitude_deg)


class LongitudeDeg(Model):
    def __init__(self, sdf_version: str, longitude_deg: float = 0.0):
        self.__version__ = sdf_version
        self.longitude_deg = longitude_deg

    def to_version(self, target_version: str) -> "LongitudeDeg":
        kwargs = {"sdf_version": target_version}
        kwargs["longitude_deg"] = self.longitude_deg
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("longitude_deg")
        if self.longitude_deg is not None:
            el.text = str(self.longitude_deg)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LongitudeDeg":
        _text = el.text or 0.0
        _longitude_deg = _parse_double(_text)
        return cls(sdf_version=version, longitude_deg=_longitude_deg)


class Elevation(Model):
    def __init__(self, sdf_version: str, elevation: float = 0.0):
        self.__version__ = sdf_version
        self.elevation = elevation

    def to_version(self, target_version: str) -> "Elevation":
        kwargs = {"sdf_version": target_version}
        kwargs["elevation"] = self.elevation
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("elevation")
        if self.elevation is not None:
            el.text = str(self.elevation)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Elevation":
        _text = el.text or 0.0
        _elevation = _parse_double(_text)
        return cls(sdf_version=version, elevation=_elevation)


class HeadingDeg(Model):
    def __init__(self, sdf_version: str, heading_deg: float = 0.0):
        self.__version__ = sdf_version
        self.heading_deg = heading_deg

    def to_version(self, target_version: str) -> "HeadingDeg":
        kwargs = {"sdf_version": target_version}
        kwargs["heading_deg"] = self.heading_deg
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("heading_deg")
        if self.heading_deg is not None:
            el.text = str(self.heading_deg)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "HeadingDeg":
        _text = el.text or 0.0
        _heading_deg = _parse_double(_text)
        return cls(sdf_version=version, heading_deg=_heading_deg)


class WorldFrameOrientation(Model):
    def __init__(self, sdf_version: str, world_frame_orientation: str = "ENU"):
        self.__version__ = sdf_version
        self.world_frame_orientation = world_frame_orientation

    def to_version(self, target_version: str) -> "WorldFrameOrientation":
        if self.world_frame_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'world_frame_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["world_frame_orientation"] = self.world_frame_orientation
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("world_frame_orientation")
        if self.world_frame_orientation is not None:
            el.text = self.world_frame_orientation
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "WorldFrameOrientation":
        _text = el.text or "ENU"
        _world_frame_orientation = _text
        if _world_frame_orientation is not None and cmp_version(version, "1.6") < 0:
            if _world_frame_orientation != "ENU":
                raise ValueError(f"'world_frame_orientation' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, world_frame_orientation=_world_frame_orientation)


class SurfaceAxisEquatorial(Model):
    def __init__(self, sdf_version: str, surface_axis_equatorial: float = 0.0):
        self.__version__ = sdf_version
        self.surface_axis_equatorial = surface_axis_equatorial

    def to_version(self, target_version: str) -> "SurfaceAxisEquatorial":
        if self.surface_axis_equatorial is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'surface_axis_equatorial' is not supported in SDF version {target_version} (added in 1.10)")
        kwargs = {"sdf_version": target_version}
        kwargs["surface_axis_equatorial"] = self.surface_axis_equatorial
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface_axis_equatorial")
        if self.surface_axis_equatorial is not None:
            el.text = str(self.surface_axis_equatorial)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SurfaceAxisEquatorial":
        _text = el.text or 0.0
        _surface_axis_equatorial = _parse_double(_text)
        if _surface_axis_equatorial is not None and cmp_version(version, "1.10") < 0:
            if _surface_axis_equatorial != 0.0:
                raise ValueError(f"'surface_axis_equatorial' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, surface_axis_equatorial=_surface_axis_equatorial)


class SurfaceAxisPolar(Model):
    def __init__(self, sdf_version: str, surface_axis_polar: float = 0.0):
        self.__version__ = sdf_version
        self.surface_axis_polar = surface_axis_polar

    def to_version(self, target_version: str) -> "SurfaceAxisPolar":
        if self.surface_axis_polar is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'surface_axis_polar' is not supported in SDF version {target_version} (added in 1.10)")
        kwargs = {"sdf_version": target_version}
        kwargs["surface_axis_polar"] = self.surface_axis_polar
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface_axis_polar")
        if self.surface_axis_polar is not None:
            el.text = str(self.surface_axis_polar)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SurfaceAxisPolar":
        _text = el.text or 0.0
        _surface_axis_polar = _parse_double(_text)
        if _surface_axis_polar is not None and cmp_version(version, "1.10") < 0:
            if _surface_axis_polar != 0.0:
                raise ValueError(f"'surface_axis_polar' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, surface_axis_polar=_surface_axis_polar)


class SphericalCoordinates(Model):
    def __init__(
        self,
        sdf_version: str,
        surface_model: "SurfaceModel" = None,
        latitude_deg: "LatitudeDeg" = None,
        longitude_deg: "LongitudeDeg" = None,
        elevation: "Elevation" = None,
        heading_deg: "HeadingDeg" = None,
        world_frame_orientation: "WorldFrameOrientation" = None,
        surface_axis_equatorial: "SurfaceAxisEquatorial" = None,
        surface_axis_polar: "SurfaceAxisPolar" = None
    ):
        self.__version__ = sdf_version
        self.surface_model = surface_model
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.elevation = elevation
        self.heading_deg = heading_deg
        self.world_frame_orientation = world_frame_orientation
        self.surface_axis_equatorial = surface_axis_equatorial
        self.surface_axis_polar = surface_axis_polar

    def to_version(self, target_version: str) -> "SphericalCoordinates":
        if self.world_frame_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'world_frame_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        if self.surface_axis_equatorial is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'surface_axis_equatorial' is not supported in SDF version {target_version} (added in 1.10)")
        if self.surface_axis_polar is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'surface_axis_polar' is not supported in SDF version {target_version} (added in 1.10)")
        kwargs = {"sdf_version": target_version}
        kwargs["surface_model"] = self.surface_model.to_version(target_version) if self.surface_model is not None else None
        kwargs["latitude_deg"] = self.latitude_deg.to_version(target_version) if self.latitude_deg is not None else None
        kwargs["longitude_deg"] = self.longitude_deg.to_version(target_version) if self.longitude_deg is not None else None
        kwargs["elevation"] = self.elevation.to_version(target_version) if self.elevation is not None else None
        kwargs["heading_deg"] = self.heading_deg.to_version(target_version) if self.heading_deg is not None else None
        kwargs["world_frame_orientation"] = self.world_frame_orientation.to_version(target_version) if self.world_frame_orientation is not None else None
        kwargs["surface_axis_equatorial"] = self.surface_axis_equatorial.to_version(target_version) if self.surface_axis_equatorial is not None else None
        kwargs["surface_axis_polar"] = self.surface_axis_polar.to_version(target_version) if self.surface_axis_polar is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spherical_coordinates")
        if self.surface_model is not None:
            el.append(self.surface_model.to_sdf(version))
        if self.latitude_deg is not None:
            el.append(self.latitude_deg.to_sdf(version))
        if self.longitude_deg is not None:
            el.append(self.longitude_deg.to_sdf(version))
        if self.elevation is not None:
            el.append(self.elevation.to_sdf(version))
        if self.heading_deg is not None:
            el.append(self.heading_deg.to_sdf(version))
        if self.world_frame_orientation is not None:
            el.append(self.world_frame_orientation.to_sdf(version))
        if self.surface_axis_equatorial is not None:
            el.append(self.surface_axis_equatorial.to_sdf(version))
        if self.surface_axis_polar is not None:
            el.append(self.surface_axis_polar.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SphericalCoordinates":
        _c_surface_model = el.find("surface_model")
        _surface_model = SurfaceModel.from_sdf(_c_surface_model, version) if _c_surface_model is not None else None
        _c_latitude_deg = el.find("latitude_deg")
        _latitude_deg = LatitudeDeg.from_sdf(_c_latitude_deg, version) if _c_latitude_deg is not None else None
        _c_longitude_deg = el.find("longitude_deg")
        _longitude_deg = LongitudeDeg.from_sdf(_c_longitude_deg, version) if _c_longitude_deg is not None else None
        _c_elevation = el.find("elevation")
        _elevation = Elevation.from_sdf(_c_elevation, version) if _c_elevation is not None else None
        _c_heading_deg = el.find("heading_deg")
        _heading_deg = HeadingDeg.from_sdf(_c_heading_deg, version) if _c_heading_deg is not None else None
        _c_world_frame_orientation = el.find("world_frame_orientation")
        _world_frame_orientation = WorldFrameOrientation.from_sdf(_c_world_frame_orientation, version) if _c_world_frame_orientation is not None else None
        if _world_frame_orientation is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'world_frame_orientation' is not supported in SDF version {version} (added in 1.6)")
        _c_surface_axis_equatorial = el.find("surface_axis_equatorial")
        _surface_axis_equatorial = SurfaceAxisEquatorial.from_sdf(_c_surface_axis_equatorial, version) if _c_surface_axis_equatorial is not None else None
        if _surface_axis_equatorial is not None and cmp_version(version, "1.10") < 0:
            raise ValueError(f"'surface_axis_equatorial' is not supported in SDF version {version} (added in 1.10)")
        _c_surface_axis_polar = el.find("surface_axis_polar")
        _surface_axis_polar = SurfaceAxisPolar.from_sdf(_c_surface_axis_polar, version) if _c_surface_axis_polar is not None else None
        if _surface_axis_polar is not None and cmp_version(version, "1.10") < 0:
            raise ValueError(f"'surface_axis_polar' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, surface_model=_surface_model, latitude_deg=_latitude_deg, longitude_deg=_longitude_deg, elevation=_elevation, heading_deg=_heading_deg, world_frame_orientation=_world_frame_orientation, surface_axis_equatorial=_surface_axis_equatorial, surface_axis_polar=_surface_axis_polar)
