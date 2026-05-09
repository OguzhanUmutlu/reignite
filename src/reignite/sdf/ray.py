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



class MinAngle(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min_angle = _parse_double(_text)
        if isinstance(_min_angle, SDFError):
            return _min_angle
        if _min_angle is not None and cmp_version(version, "1.2") < 0:
            if _min_angle != 0:
                return SDFError(f"'min_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min_angle=_min_angle)


class MaxAngle(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max_angle = _parse_double(_text)
        if isinstance(_max_angle, SDFError):
            return _max_angle
        if _max_angle is not None and cmp_version(version, "1.2") < 0:
            if _max_angle != 0:
                return SDFError(f"'max_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max_angle=_max_angle)


class Resolution(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _resolution = _parse_double(_text)
        if isinstance(_resolution, SDFError):
            return _resolution
        if _resolution is not None and cmp_version(version, "1.2") < 0:
            if _resolution != 1:
                return SDFError(f"'resolution' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, resolution=_resolution)


class Samples(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 640
        _samples = _parse_uint32(_text)
        if isinstance(_samples, SDFError):
            return _samples
        if _samples is not None and cmp_version(version, "1.2") < 0:
            if _samples != 640:
                return SDFError(f"'samples' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, samples=_samples)


class Horizontal(BaseModel):
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
        if self.samples is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'samples' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.min_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.max_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (removed in 1.2)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _samples = _parse_uint32(el.get("samples", 1))
        if isinstance(_samples, SDFError):
            return _samples.extend("@samples")
        _resolution = _parse_double(el.get("resolution", 1))
        if isinstance(_resolution, SDFError):
            return _resolution.extend("@resolution")
        _min_angle = _parse_double(el.get("min_angle", 0))
        if isinstance(_min_angle, SDFError):
            return _min_angle.extend("@min_angle")
        _max_angle = _parse_double(el.get("max_angle", 0))
        if isinstance(_max_angle, SDFError):
            return _max_angle.extend("@max_angle")
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class VerticalSamples(BaseModel):
    def __init__(self, sdf_version: str, samples: int = 1):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "VerticalSamples":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _samples = _parse_uint32(_text)
        if isinstance(_samples, SDFError):
            return _samples
        if _samples is not None and cmp_version(version, "1.2") < 0:
            if _samples != 1:
                return SDFError(f"'samples' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, samples=_samples)


class Vertical(BaseModel):
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
        if self.samples is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'samples' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.min_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.max_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (removed in 1.2)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _samples = _parse_uint32(el.get("samples", 1))
        if isinstance(_samples, SDFError):
            return _samples.extend("@samples")
        _resolution = _parse_double(el.get("resolution", 1))
        if isinstance(_resolution, SDFError):
            return _resolution.extend("@resolution")
        _min_angle = _parse_double(el.get("min_angle", 0))
        if isinstance(_min_angle, SDFError):
            return _min_angle.extend("@min_angle")
        _max_angle = _parse_double(el.get("max_angle", 0))
        if isinstance(_max_angle, SDFError):
            return _max_angle.extend("@max_angle")
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class Scan(BaseModel):
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
        if self.horizontal is None:
            self.horizontal = Horizontal(sdf_version=version)
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_horizontal = el.find("horizontal")
        if _c_horizontal is not None:
            _res = Horizontal._from_sdf(_c_horizontal, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        else:
            _res = Horizontal._from_sdf(ET.Element("horizontal"), version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        _c_vertical = el.find("vertical")
        if _c_vertical is not None:
            _res = Vertical._from_sdf(_c_vertical, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical")
            _vertical = _res
        else:
            _vertical = None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Min(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min = _parse_double(_text)
        if isinstance(_min, SDFError):
            return _min
        if _min is not None and cmp_version(version, "1.2") < 0:
            if _min != 0:
                return SDFError(f"'min' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min=_min)


class RangeResolution(BaseModel):
    def __init__(self, sdf_version: str, resolution: float = 0):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "RangeResolution":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _resolution = _parse_double(_text)
        if isinstance(_resolution, SDFError):
            return _resolution
        if _resolution is not None and cmp_version(version, "1.2") < 0:
            if _resolution != 0:
                return SDFError(f"'resolution' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, resolution=_resolution)


class Max(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max = _parse_double(_text)
        if isinstance(_max, SDFError):
            return _max
        if _max is not None and cmp_version(version, "1.2") < 0:
            if _max != 0:
                return SDFError(f"'max' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max=_max)


class Range(BaseModel):
    def __init__(self, sdf_version: str, min: float = 0, max: float = 0, resolution: float = 0):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Range":
        if self.min is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'min' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.max is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'max' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _min = _parse_double(el.get("min", 0))
        if isinstance(_min, SDFError):
            return _min.extend("@min")
        _max = _parse_double(el.get("max", 0))
        if isinstance(_max, SDFError):
            return _max.extend("@max")
        _resolution = _parse_double(el.get("resolution", 0))
        if isinstance(_resolution, SDFError):
            return _resolution.extend("@resolution")
        return cls(sdf_version=version, min=_min, max=_max, resolution=_resolution)


class Type(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "gaussian"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        return cls(sdf_version=version, type=_type)


class Mean(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _mean = _parse_double(_text)
        if isinstance(_mean, SDFError):
            return _mean
        return cls(sdf_version=version, mean=_mean)


class Stddev(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _stddev = _parse_double(_text)
        if isinstance(_stddev, SDFError):
            return _stddev
        return cls(sdf_version=version, stddev=_stddev)


class Noise(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev)


class VisibilityMask(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4294967295
        _visibility_mask = _parse_uint32(_text)
        if isinstance(_visibility_mask, SDFError):
            return _visibility_mask
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            if _visibility_mask != 4294967295:
                return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, visibility_mask=_visibility_mask)


class Ray(BaseModel):
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
        if self.scan is None:
            self.scan = Scan(sdf_version=version)
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is None:
            self.range = Range(sdf_version=version)
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_scan = el.find("scan")
        if _c_scan is not None:
            _res = Scan._from_sdf(_c_scan, version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        else:
            _res = Scan._from_sdf(ET.Element("scan"), version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        _c_range = el.find("range")
        if _c_range is not None:
            _res = Range._from_sdf(_c_range, version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        else:
            _res = Range._from_sdf(ET.Element("range"), version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_visibility_mask = el.find("visibility_mask")
        if _c_visibility_mask is not None:
            _res = VisibilityMask._from_sdf(_c_visibility_mask, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_mask")
            _visibility_mask = _res
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)
