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


class BiasMean(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _bias_mean = _parse_double(_text)
        if isinstance(_bias_mean, SDFError):
            return _bias_mean
        return cls(sdf_version=version, bias_mean=_bias_mean)


class BiasStddev(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _bias_stddev = _parse_double(_text)
        if isinstance(_bias_stddev, SDFError):
            return _bias_stddev
        return cls(sdf_version=version, bias_stddev=_bias_stddev)


class Precision(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _precision = _parse_double(_text)
        if isinstance(_precision, SDFError):
            return _precision
        return cls(sdf_version=version, precision=_precision)


class DynamicBiasStddev(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _dynamic_bias_stddev = _parse_double(_text)
        if isinstance(_dynamic_bias_stddev, SDFError):
            return _dynamic_bias_stddev
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            if _dynamic_bias_stddev != 0.0:
                return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, dynamic_bias_stddev=_dynamic_bias_stddev)


class DynamicBiasCorrelationTime(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _dynamic_bias_correlation_time = _parse_double(_text)
        if isinstance(_dynamic_bias_correlation_time, SDFError):
            return _dynamic_bias_correlation_time
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            if _dynamic_bias_correlation_time != 0.0:
                return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, dynamic_bias_correlation_time=_dynamic_bias_correlation_time)


class Noise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None,
        mean: "Mean" = None,
        precision: "Precision" = None,
        stddev: "Stddev" = None,
        type: str = "none"
    ):
        self.__version__ = sdf_version
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev
        self.mean = mean
        self.precision = precision
        self.stddev = stddev
        self.type = type

    def to_version(self, target_version: str) -> "Noise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, bias_mean=_bias_mean, bias_stddev=_bias_stddev, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev, mean=_mean, precision=_precision, stddev=_stddev, type=_type)


class X(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class Y(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class Z(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class Magnetometer(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)
