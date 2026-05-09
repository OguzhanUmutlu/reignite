### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class SurfaceModel(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "EARTH_WGS84"
        _surface_model = _text
        if isinstance(_surface_model, SDFError):
            return _surface_model
        return cls(sdf_version=version, surface_model=_surface_model)


class LatitudeDeg(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _latitude_deg = _parse_double(_text)
        if isinstance(_latitude_deg, SDFError):
            return _latitude_deg
        return cls(sdf_version=version, latitude_deg=_latitude_deg)


class LongitudeDeg(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _longitude_deg = _parse_double(_text)
        if isinstance(_longitude_deg, SDFError):
            return _longitude_deg
        return cls(sdf_version=version, longitude_deg=_longitude_deg)


class Elevation(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _elevation = _parse_double(_text)
        if isinstance(_elevation, SDFError):
            return _elevation
        return cls(sdf_version=version, elevation=_elevation)


class HeadingDeg(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _heading_deg = _parse_double(_text)
        if isinstance(_heading_deg, SDFError):
            return _heading_deg
        return cls(sdf_version=version, heading_deg=_heading_deg)


class WorldFrameOrientation(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "ENU"
        _world_frame_orientation = _text
        if isinstance(_world_frame_orientation, SDFError):
            return _world_frame_orientation
        if _world_frame_orientation is not None and cmp_version(version, "1.6") < 0:
            if _world_frame_orientation != "ENU":
                return SDFError(f"'world_frame_orientation' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, world_frame_orientation=_world_frame_orientation)


class SurfaceAxisEquatorial(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _surface_axis_equatorial = _parse_double(_text)
        if isinstance(_surface_axis_equatorial, SDFError):
            return _surface_axis_equatorial
        if _surface_axis_equatorial is not None and cmp_version(version, "1.10") < 0:
            if _surface_axis_equatorial != 0.0:
                return SDFError(f"'surface_axis_equatorial' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, surface_axis_equatorial=_surface_axis_equatorial)


class SurfaceAxisPolar(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _surface_axis_polar = _parse_double(_text)
        if isinstance(_surface_axis_polar, SDFError):
            return _surface_axis_polar
        if _surface_axis_polar is not None and cmp_version(version, "1.10") < 0:
            if _surface_axis_polar != 0.0:
                return SDFError(f"'surface_axis_polar' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, surface_axis_polar=_surface_axis_polar)


class SphericalCoordinates(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_surface_model = el.find("surface_model")
        if _c_surface_model is not None:
            _res = SurfaceModel._from_sdf(_c_surface_model, version)
            if isinstance(_res, SDFError):
                return _res.extend("surface_model")
            _surface_model = _res
        else:
            _surface_model = None
        _c_latitude_deg = el.find("latitude_deg")
        if _c_latitude_deg is not None:
            _res = LatitudeDeg._from_sdf(_c_latitude_deg, version)
            if isinstance(_res, SDFError):
                return _res.extend("latitude_deg")
            _latitude_deg = _res
        else:
            _latitude_deg = None
        _c_longitude_deg = el.find("longitude_deg")
        if _c_longitude_deg is not None:
            _res = LongitudeDeg._from_sdf(_c_longitude_deg, version)
            if isinstance(_res, SDFError):
                return _res.extend("longitude_deg")
            _longitude_deg = _res
        else:
            _longitude_deg = None
        _c_elevation = el.find("elevation")
        if _c_elevation is not None:
            _res = Elevation._from_sdf(_c_elevation, version)
            if isinstance(_res, SDFError):
                return _res.extend("elevation")
            _elevation = _res
        else:
            _elevation = None
        _c_heading_deg = el.find("heading_deg")
        if _c_heading_deg is not None:
            _res = HeadingDeg._from_sdf(_c_heading_deg, version)
            if isinstance(_res, SDFError):
                return _res.extend("heading_deg")
            _heading_deg = _res
        else:
            _heading_deg = None
        _c_world_frame_orientation = el.find("world_frame_orientation")
        if _c_world_frame_orientation is not None:
            _res = WorldFrameOrientation._from_sdf(_c_world_frame_orientation, version)
            if isinstance(_res, SDFError):
                return _res.extend("world_frame_orientation")
            _world_frame_orientation = _res
        else:
            _world_frame_orientation = None
        if _world_frame_orientation is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'world_frame_orientation' is not supported in SDF version {version} (added in 1.6)")
        _c_surface_axis_equatorial = el.find("surface_axis_equatorial")
        if _c_surface_axis_equatorial is not None:
            _res = SurfaceAxisEquatorial._from_sdf(_c_surface_axis_equatorial, version)
            if isinstance(_res, SDFError):
                return _res.extend("surface_axis_equatorial")
            _surface_axis_equatorial = _res
        else:
            _surface_axis_equatorial = None
        if _surface_axis_equatorial is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'surface_axis_equatorial' is not supported in SDF version {version} (added in 1.10)")
        _c_surface_axis_polar = el.find("surface_axis_polar")
        if _c_surface_axis_polar is not None:
            _res = SurfaceAxisPolar._from_sdf(_c_surface_axis_polar, version)
            if isinstance(_res, SDFError):
                return _res.extend("surface_axis_polar")
            _surface_axis_polar = _res
        else:
            _surface_axis_polar = None
        if _surface_axis_polar is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'surface_axis_polar' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, surface_model=_surface_model, latitude_deg=_latitude_deg, longitude_deg=_longitude_deg, elevation=_elevation, heading_deg=_heading_deg, world_frame_orientation=_world_frame_orientation, surface_axis_equatorial=_surface_axis_equatorial, surface_axis_polar=_surface_axis_polar)
