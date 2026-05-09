from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model
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



class Min(Model):
    def __init__(self, sdf_version: str, min: float = 0):
        self.__version__ = sdf_version
        self.min = min

    def to_version(self, target_version: str) -> "Min":
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min")
        if self.min is not None:
            el.text = str(self.min)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Min":
        _text = el.text or 0
        _min = _parse_double(_text)
        return cls(sdf_version=version, min=_min)


class Max(Model):
    def __init__(self, sdf_version: str, max: float = 1.0):
        self.__version__ = sdf_version
        self.max = max

    def to_version(self, target_version: str) -> "Max":
        kwargs = {"sdf_version": target_version}
        kwargs["max"] = self.max
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max")
        if self.max is not None:
            el.text = str(self.max)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Max":
        _text = el.text or 1.0
        _max = _parse_double(_text)
        return cls(sdf_version=version, max=_max)


class Radius(Model):
    def __init__(self, sdf_version: str, radius: float = 0.5):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Radius":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("radius")
        if self.radius is not None:
            el.text = str(self.radius)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Radius":
        _text = el.text or 0.5
        _radius = _parse_double(_text)
        return cls(sdf_version=version, radius=_radius)


class Geometry(Model):
    def __init__(self, sdf_version: str, geometry: str = "cone"):
        self.__version__ = sdf_version
        self.geometry = geometry

    def to_version(self, target_version: str) -> "Geometry":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["geometry"] = self.geometry
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("geometry")
        if self.geometry is not None:
            el.text = self.geometry
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Geometry":
        _text = el.text or "cone"
        _geometry = _text
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            if _geometry != "cone":
                raise ValueError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, geometry=_geometry)


class Sonar(Model):
    def __init__(
        self,
        sdf_version: str,
        min: "Min" = None,
        max: "Max" = None,
        radius: "Radius" = None,
        geometry: "Geometry" = None
    ):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.radius = radius
        self.geometry = geometry

    def to_version(self, target_version: str) -> "Sonar":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min.to_version(target_version) if self.min is not None else None
        kwargs["max"] = self.max.to_version(target_version) if self.max is not None else None
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sonar")
        if self.min is not None:
            el.append(self.min.to_sdf(version))
        if self.max is not None:
            el.append(self.max.to_sdf(version))
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sonar":
        _c_min = el.find("min")
        _min = Min.from_sdf(_c_min, version) if _c_min is not None else None
        _c_max = el.find("max")
        _max = Max.from_sdf(_c_max, version) if _c_max is not None else None
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius, version) if _c_radius is not None else None
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry, version) if _c_geometry is not None else None
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, min=_min, max=_max, radius=_radius, geometry=_geometry)
