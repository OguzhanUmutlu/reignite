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



class Samples(BaseModel):
    def __init__(self, sdf_version: str, samples: int = 640):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "Samples":
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
        return cls(sdf_version=version, samples=_samples)


class Resolution(BaseModel):
    def __init__(self, sdf_version: str, resolution: float = 1):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Resolution":
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
        return cls(sdf_version=version, resolution=_resolution)


class MinAngle(BaseModel):
    def __init__(self, sdf_version: str, min_angle: float = 0):
        self.__version__ = sdf_version
        self.min_angle = min_angle

    def to_version(self, target_version: str) -> "MinAngle":
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
        return cls(sdf_version=version, min_angle=_min_angle)


class MaxAngle(BaseModel):
    def __init__(self, sdf_version: str, max_angle: float = 0):
        self.__version__ = sdf_version
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "MaxAngle":
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
        return cls(sdf_version=version, max_angle=_max_angle)


class Horizontal(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        max_angle: "MaxAngle" = None,
        min_angle: "MinAngle" = None,
        resolution: "Resolution" = None,
        samples: "Samples" = None
    ):
        self.__version__ = sdf_version
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.resolution = resolution
        self.samples = samples

    def to_version(self, target_version: str) -> "Horizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["max_angle"] = self.max_angle.to_version(target_version) if self.max_angle is not None else None
        kwargs["min_angle"] = self.min_angle.to_version(target_version) if self.min_angle is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        kwargs["samples"] = self.samples.to_version(target_version) if self.samples is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.max_angle is not None:
            el.append(self.max_angle.to_sdf(version))
        if self.min_angle is not None:
            el.append(self.min_angle.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        if self.samples is not None:
            el.append(self.samples.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_max_angle = el.find("max_angle")
        if _c_max_angle is not None:
            _res = MaxAngle._from_sdf(_c_max_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_angle")
            _max_angle = _res
        else:
            _max_angle = None
        _c_min_angle = el.find("min_angle")
        if _c_min_angle is not None:
            _res = MinAngle._from_sdf(_c_min_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_angle")
            _min_angle = _res
        else:
            _min_angle = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = Resolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        _c_samples = el.find("samples")
        if _c_samples is not None:
            _res = Samples._from_sdf(_c_samples, version)
            if isinstance(_res, SDFError):
                return _res.extend("samples")
            _samples = _res
        else:
            _samples = None
        return cls(sdf_version=version, max_angle=_max_angle, min_angle=_min_angle, resolution=_resolution, samples=_samples)


class VerticalSamples(BaseModel):
    def __init__(self, sdf_version: str, samples: int = 1):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "VerticalSamples":
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
        return cls(sdf_version=version, samples=_samples)


class Vertical(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        max_angle: "MaxAngle" = None,
        min_angle: "MinAngle" = None,
        resolution: "Resolution" = None,
        samples: "VerticalSamples" = None
    ):
        self.__version__ = sdf_version
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.resolution = resolution
        self.samples = samples

    def to_version(self, target_version: str) -> "Vertical":
        kwargs = {"sdf_version": target_version}
        kwargs["max_angle"] = self.max_angle.to_version(target_version) if self.max_angle is not None else None
        kwargs["min_angle"] = self.min_angle.to_version(target_version) if self.min_angle is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        kwargs["samples"] = self.samples.to_version(target_version) if self.samples is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.max_angle is not None:
            el.append(self.max_angle.to_sdf(version))
        if self.min_angle is not None:
            el.append(self.min_angle.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        if self.samples is not None:
            el.append(self.samples.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_max_angle = el.find("max_angle")
        if _c_max_angle is not None:
            _res = MaxAngle._from_sdf(_c_max_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_angle")
            _max_angle = _res
        else:
            _max_angle = None
        _c_min_angle = el.find("min_angle")
        if _c_min_angle is not None:
            _res = MinAngle._from_sdf(_c_min_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_angle")
            _min_angle = _res
        else:
            _min_angle = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = Resolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        _c_samples = el.find("samples")
        if _c_samples is not None:
            _res = VerticalSamples._from_sdf(_c_samples, version)
            if isinstance(_res, SDFError):
                return _res.extend("samples")
            _samples = _res
        else:
            _samples = None
        return cls(sdf_version=version, max_angle=_max_angle, min_angle=_min_angle, resolution=_resolution, samples=_samples)


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
        return cls(sdf_version=version, min=_min)


class Max(BaseModel):
    def __init__(self, sdf_version: str, max: float = 0):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max = _parse_double(_text)
        if isinstance(_max, SDFError):
            return _max
        return cls(sdf_version=version, max=_max)


class RangeResolution(BaseModel):
    def __init__(self, sdf_version: str, resolution: float = 0):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "RangeResolution":
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
        return cls(sdf_version=version, resolution=_resolution)


class Range(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        max: "Max" = None,
        min: "Min" = None,
        resolution: "RangeResolution" = None
    ):
        self.__version__ = sdf_version
        self.max = max
        self.min = min
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Range":
        kwargs = {"sdf_version": target_version}
        kwargs["max"] = self.max.to_version(target_version) if self.max is not None else None
        kwargs["min"] = self.min.to_version(target_version) if self.min is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.max is not None:
            el.append(self.max.to_sdf(version))
        if self.min is not None:
            el.append(self.min.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_max = el.find("max")
        if _c_max is not None:
            _res = Max._from_sdf(_c_max, version)
            if isinstance(_res, SDFError):
                return _res.extend("max")
            _max = _res
        else:
            _max = None
        _c_min = el.find("min")
        if _c_min is not None:
            _res = Min._from_sdf(_c_min, version)
            if isinstance(_res, SDFError):
                return _res.extend("min")
            _min = _res
        else:
            _min = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = RangeResolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        return cls(sdf_version=version, max=_max, min=_min, resolution=_resolution)


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
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        type: "Type" = None
    ):
        self.__version__ = sdf_version
        self.mean = mean
        self.stddev = stddev
        self.type = type

    def to_version(self, target_version: str) -> "Noise":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        return cls(sdf_version=version, mean=_mean, stddev=_stddev, type=_type)


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


class Lidar(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        noise: "Noise" = None,
        range: "Range" = None,
        scan: "Scan" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.noise = noise
        self.range = range
        self.scan = scan
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "Lidar":
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lidar")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.range is None:
            self.range = Range(sdf_version=version)
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.scan is None:
            self.scan = Scan(sdf_version=version)
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
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
        return cls(sdf_version=version, noise=_noise, range=_range, scan=_scan, visibility_mask=_visibility_mask)
