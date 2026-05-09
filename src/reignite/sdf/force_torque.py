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



class Frame(BaseModel):
    def __init__(self, sdf_version: str, frame: str = "parent"):
        self.__version__ = sdf_version
        self.frame = frame

    def to_version(self, target_version: str) -> "Frame":
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.frame is not None:
            el.text = self.frame
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "parent"
        _frame = _text
        if isinstance(_frame, SDFError):
            return _frame
        return cls(sdf_version=version, frame=_frame)


class MeasureDirection(BaseModel):
    def __init__(self, sdf_version: str, measure_direction: str = "child_to_parent"):
        self.__version__ = sdf_version
        self.measure_direction = measure_direction

    def to_version(self, target_version: str) -> "MeasureDirection":
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["measure_direction"] = self.measure_direction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("measure_direction")
        if self.measure_direction is not None:
            el.text = self.measure_direction
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "child_to_parent"
        _measure_direction = _text
        if isinstance(_measure_direction, SDFError):
            return _measure_direction
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            if _measure_direction != "child_to_parent":
                return SDFError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, measure_direction=_measure_direction)


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


class DynamicBiasStddev(BaseModel):
    def __init__(self, sdf_version: str, dynamic_bias_stddev: float = 0.0):
        self.__version__ = sdf_version
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "DynamicBiasStddev":
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
        return cls(sdf_version=version, dynamic_bias_stddev=_dynamic_bias_stddev)


class DynamicBiasCorrelationTime(BaseModel):
    def __init__(self, sdf_version: str, dynamic_bias_correlation_time: float = 0.0):
        self.__version__ = sdf_version
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time

    def to_version(self, target_version: str) -> "DynamicBiasCorrelationTime":
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
        return cls(sdf_version=version, dynamic_bias_correlation_time=_dynamic_bias_correlation_time)


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


class Noise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        precision: "Precision" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.dynamic_bias_stddev = dynamic_bias_stddev
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.precision = precision

    def to_version(self, target_version: str) -> "Noise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is None:
            raise ValueError(f"'type' is required in SDF version {version}")
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
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("type") is None:
            return SDFError(f"'type' is required in SDF version {version}")
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
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
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, dynamic_bias_stddev=_dynamic_bias_stddev, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, precision=_precision)


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


class Torque(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Torque":
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
        el = ET.Element("torque")
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


class Force(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Force":
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
        el = ET.Element("force")
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


class ForceTorque(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        frame: "Frame" = None,
        measure_direction: "MeasureDirection" = None,
        torque: "Torque" = None,
        force: "Force" = None
    ):
        self.__version__ = sdf_version
        self.frame = frame
        self.measure_direction = measure_direction
        self.torque = torque
        self.force = force

    def to_version(self, target_version: str) -> "ForceTorque":
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        if self.torque is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {target_version} (added in 1.7)")
        if self.force is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame.to_version(target_version) if self.frame is not None else None
        kwargs["measure_direction"] = self.measure_direction.to_version(target_version) if self.measure_direction is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("force_torque")
        if self.frame is not None:
            el.append(self.frame.to_sdf(version))
        if self.measure_direction is not None:
            el.append(self.measure_direction.to_sdf(version))
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_frame = el.find("frame")
        if _c_frame is not None:
            _res = Frame._from_sdf(_c_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame = _res
        else:
            _frame = None
        _c_measure_direction = el.find("measure_direction")
        if _c_measure_direction is not None:
            _res = MeasureDirection._from_sdf(_c_measure_direction, version)
            if isinstance(_res, SDFError):
                return _res.extend("measure_direction")
            _measure_direction = _res
        else:
            _measure_direction = None
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        _c_torque = el.find("torque")
        if _c_torque is not None:
            _res = Torque._from_sdf(_c_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("torque")
            _torque = _res
        else:
            _torque = None
        if _torque is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'torque' is not supported in SDF version {version} (added in 1.7)")
        _c_force = el.find("force")
        if _c_force is not None:
            _res = Force._from_sdf(_c_force, version)
            if isinstance(_res, SDFError):
                return _res.extend("force")
            _force = _res
        else:
            _force = None
        if _force is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'force' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, frame=_frame, measure_direction=_measure_direction, torque=_torque, force=_force)
