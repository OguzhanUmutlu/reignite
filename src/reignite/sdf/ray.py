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



class Samples(Model):
    def __init__(self, sdf_version: str, samples: int = 640):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "Samples":
        if self.samples is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'samples' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("samples")
        if self.samples is not None:
            el.text = str(self.samples)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Samples":
        _text = el.text or 640
        _samples = _parse_uint32(_text)
        if _samples is not None and cmp_version(version, "1.2") < 0:
            if _samples != 640:
                raise ValueError(f"'samples' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, samples=_samples)


class Resolution(Model):
    def __init__(self, sdf_version: str, resolution: float = 1):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Resolution":
        if self.resolution is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["resolution"] = self.resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("resolution")
        if self.resolution is not None:
            el.text = str(self.resolution)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Resolution":
        _text = el.text or 1
        _resolution = _parse_double(_text)
        if _resolution is not None and cmp_version(version, "1.2") < 0:
            if _resolution != 1:
                raise ValueError(f"'resolution' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, resolution=_resolution)


class MinAngle(Model):
    def __init__(self, sdf_version: str, min_angle: float = 0):
        self.__version__ = sdf_version
        self.min_angle = min_angle

    def to_version(self, target_version: str) -> "MinAngle":
        if self.min_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["min_angle"] = self.min_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_angle")
        if self.min_angle is not None:
            el.text = str(self.min_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinAngle":
        _text = el.text or 0
        _min_angle = _parse_double(_text)
        if _min_angle is not None and cmp_version(version, "1.2") < 0:
            if _min_angle != 0:
                raise ValueError(f"'min_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min_angle=_min_angle)


class MaxAngle(Model):
    def __init__(self, sdf_version: str, max_angle: float = 0):
        self.__version__ = sdf_version
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "MaxAngle":
        if self.max_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_angle")
        if self.max_angle is not None:
            el.text = str(self.max_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxAngle":
        _text = el.text or 0
        _max_angle = _parse_double(_text)
        if _max_angle is not None and cmp_version(version, "1.2") < 0:
            if _max_angle != 0:
                raise ValueError(f"'max_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max_angle=_max_angle)


class Horizontal(Model):
    def __init__(
        self,
        sdf_version: str,
        samples: int = 1,
        resolution: float = 1,
        min_angle: float = 0,
        max_angle: float = 0
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "Horizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        kwargs["resolution"] = self.resolution
        kwargs["min_angle"] = self.min_angle
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.samples is not None:
            el.set("samples", str(self.samples))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        if self.min_angle is not None:
            el.set("min_angle", str(self.min_angle))
        if self.max_angle is not None:
            el.set("max_angle", str(self.max_angle))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Horizontal":
        _samples = _parse_uint32(el.get("samples", 1))
        _resolution = _parse_double(el.get("resolution", 1))
        _min_angle = _parse_double(el.get("min_angle", 0))
        _max_angle = _parse_double(el.get("max_angle", 0))
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class Vertical(Model):
    def __init__(
        self,
        sdf_version: str,
        samples: int = 1,
        resolution: float = 1,
        min_angle: float = 0,
        max_angle: float = 0
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "Vertical":
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        kwargs["resolution"] = self.resolution
        kwargs["min_angle"] = self.min_angle
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.samples is not None:
            el.set("samples", str(self.samples))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        if self.min_angle is not None:
            el.set("min_angle", str(self.min_angle))
        if self.max_angle is not None:
            el.set("max_angle", str(self.max_angle))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Vertical":
        _samples = _parse_uint32(el.get("samples", 1))
        _resolution = _parse_double(el.get("resolution", 1))
        _min_angle = _parse_double(el.get("min_angle", 0))
        _max_angle = _parse_double(el.get("max_angle", 0))
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class Scan(Model):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "Horizontal" = None,
        vertical: "Vertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "Scan":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scan")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Scan":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal, version) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical, version) if _c_vertical is not None else None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Min(Model):
    def __init__(self, sdf_version: str, min: float = 0):
        self.__version__ = sdf_version
        self.min = min

    def to_version(self, target_version: str) -> "Min":
        if self.min is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'min' is not supported in SDF version {target_version} (added in 1.2)")
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
        if _min is not None and cmp_version(version, "1.2") < 0:
            if _min != 0:
                raise ValueError(f"'min' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min=_min)


class Max(Model):
    def __init__(self, sdf_version: str, max: float = 0):
        self.__version__ = sdf_version
        self.max = max

    def to_version(self, target_version: str) -> "Max":
        if self.max is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'max' is not supported in SDF version {target_version} (added in 1.2)")
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
        _text = el.text or 0
        _max = _parse_double(_text)
        if _max is not None and cmp_version(version, "1.2") < 0:
            if _max != 0:
                raise ValueError(f"'max' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max=_max)


class Range(Model):
    def __init__(self, sdf_version: str, min: float = 0, max: float = 0, resolution: float = 0):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Range":
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min
        kwargs["max"] = self.max
        kwargs["resolution"] = self.resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.min is not None:
            el.set("min", str(self.min))
        if self.max is not None:
            el.set("max", str(self.max))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Range":
        _min = _parse_double(el.get("min", 0))
        _max = _parse_double(el.get("max", 0))
        _resolution = _parse_double(el.get("resolution", 0))
        return cls(sdf_version=version, min=_min, max=_max, resolution=_resolution)


class Type(Model):
    def __init__(self, sdf_version: str, type: str = "gaussian"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Type":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Type":
        _text = el.text or "gaussian"
        _type = _text
        return cls(sdf_version=version, type=_type)


class Mean(Model):
    def __init__(self, sdf_version: str, mean: float = 0.0):
        self.__version__ = sdf_version
        self.mean = mean

    def to_version(self, target_version: str) -> "Mean":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mean")
        if self.mean is not None:
            el.text = str(self.mean)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mean":
        _text = el.text or 0.0
        _mean = _parse_double(_text)
        return cls(sdf_version=version, mean=_mean)


class Stddev(Model):
    def __init__(self, sdf_version: str, stddev: float = 0.0):
        self.__version__ = sdf_version
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Stddev":
        kwargs = {"sdf_version": target_version}
        kwargs["stddev"] = self.stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("stddev")
        if self.stddev is not None:
            el.text = str(self.stddev)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Stddev":
        _text = el.text or 0.0
        _stddev = _parse_double(_text)
        return cls(sdf_version=version, stddev=_stddev)


class Noise(Model):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        mean: "Mean" = None,
        stddev: "Stddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Noise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Noise":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type, version) if _c_type is not None else None
        _c_mean = el.find("mean")
        _mean = Mean.from_sdf(_c_mean, version) if _c_mean is not None else None
        _c_stddev = el.find("stddev")
        _stddev = Stddev.from_sdf(_c_stddev, version) if _c_stddev is not None else None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev)


class VisibilityMask(Model):
    def __init__(self, sdf_version: str, visibility_mask: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "VisibilityMask":
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_mask"] = self.visibility_mask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visibility_mask")
        if self.visibility_mask is not None:
            el.text = str(self.visibility_mask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VisibilityMask":
        _text = el.text or 4294967295
        _visibility_mask = _parse_uint32(_text)
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            if _visibility_mask != 4294967295:
                raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, visibility_mask=_visibility_mask)


class Ray(Model):
    def __init__(
        self,
        sdf_version: str,
        scan: "Scan" = None,
        range: "Range" = None,
        noise: "Noise" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.scan = scan
        self.range = range
        self.noise = noise
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "Ray":
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ray")
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ray":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan, version) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range, version) if _c_range is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_visibility_mask = el.find("visibility_mask")
        _visibility_mask = VisibilityMask.from_sdf(_c_visibility_mask, version) if _c_visibility_mask is not None else None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)
