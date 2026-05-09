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


class BiasMean(Model):
    def __init__(self, sdf_version: str, bias_mean: float = 0.0):
        self.__version__ = sdf_version
        self.bias_mean = bias_mean

    def to_version(self, target_version: str) -> "BiasMean":
        kwargs = {"sdf_version": target_version}
        kwargs["bias_mean"] = self.bias_mean
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bias_mean")
        if self.bias_mean is not None:
            el.text = str(self.bias_mean)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "BiasMean":
        _text = el.text or 0.0
        _bias_mean = _parse_double(_text)
        return cls(sdf_version=version, bias_mean=_bias_mean)


class BiasStddev(Model):
    def __init__(self, sdf_version: str, bias_stddev: float = 0.0):
        self.__version__ = sdf_version
        self.bias_stddev = bias_stddev

    def to_version(self, target_version: str) -> "BiasStddev":
        kwargs = {"sdf_version": target_version}
        kwargs["bias_stddev"] = self.bias_stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bias_stddev")
        if self.bias_stddev is not None:
            el.text = str(self.bias_stddev)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "BiasStddev":
        _text = el.text or 0.0
        _bias_stddev = _parse_double(_text)
        return cls(sdf_version=version, bias_stddev=_bias_stddev)


class Precision(Model):
    def __init__(self, sdf_version: str, precision: float = 0.0):
        self.__version__ = sdf_version
        self.precision = precision

    def to_version(self, target_version: str) -> "Precision":
        kwargs = {"sdf_version": target_version}
        kwargs["precision"] = self.precision
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("precision")
        if self.precision is not None:
            el.text = str(self.precision)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Precision":
        _text = el.text or 0.0
        _precision = _parse_double(_text)
        return cls(sdf_version=version, precision=_precision)


class DynamicBiasStddev(Model):
    def __init__(self, sdf_version: str, dynamic_bias_stddev: float = 0.0):
        self.__version__ = sdf_version
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "DynamicBiasStddev":
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamic_bias_stddev")
        if self.dynamic_bias_stddev is not None:
            el.text = str(self.dynamic_bias_stddev)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "DynamicBiasStddev":
        _text = el.text or 0.0
        _dynamic_bias_stddev = _parse_double(_text)
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            if _dynamic_bias_stddev != 0.0:
                raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, dynamic_bias_stddev=_dynamic_bias_stddev)


class DynamicBiasCorrelationTime(Model):
    def __init__(self, sdf_version: str, dynamic_bias_correlation_time: float = 0.0):
        self.__version__ = sdf_version
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time

    def to_version(self, target_version: str) -> "DynamicBiasCorrelationTime":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamic_bias_correlation_time")
        if self.dynamic_bias_correlation_time is not None:
            el.text = str(self.dynamic_bias_correlation_time)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "DynamicBiasCorrelationTime":
        _text = el.text or 0.0
        _dynamic_bias_correlation_time = _parse_double(_text)
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            if _dynamic_bias_correlation_time != 0.0:
                raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, dynamic_bias_correlation_time=_dynamic_bias_correlation_time)


class Noise(Model):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_stddev = dynamic_bias_stddev
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time

    def to_version(self, target_version: str) -> "Noise":
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Noise":
        _type = el.get("type", "none")
        _c_mean = el.find("mean")
        _mean = Mean.from_sdf(_c_mean, version) if _c_mean is not None else None
        _c_stddev = el.find("stddev")
        _stddev = Stddev.from_sdf(_c_stddev, version) if _c_stddev is not None else None
        _c_bias_mean = el.find("bias_mean")
        _bias_mean = BiasMean.from_sdf(_c_bias_mean, version) if _c_bias_mean is not None else None
        _c_bias_stddev = el.find("bias_stddev")
        _bias_stddev = BiasStddev.from_sdf(_c_bias_stddev, version) if _c_bias_stddev is not None else None
        _c_precision = el.find("precision")
        _precision = Precision.from_sdf(_c_precision, version) if _c_precision is not None else None
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        _dynamic_bias_stddev = DynamicBiasStddev.from_sdf(_c_dynamic_bias_stddev, version) if _c_dynamic_bias_stddev is not None else None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        _dynamic_bias_correlation_time = DynamicBiasCorrelationTime.from_sdf(_c_dynamic_bias_correlation_time, version) if _c_dynamic_bias_correlation_time is not None else None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_stddev=_dynamic_bias_stddev, dynamic_bias_correlation_time=_dynamic_bias_correlation_time)


class X(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "X":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("x")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "X":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Y(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Y":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("y")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Y":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Z(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Z":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("z")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Z":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Magnetometer(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Magnetometer":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("magnetometer")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)
