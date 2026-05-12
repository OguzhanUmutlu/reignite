### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


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



class Accel(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        mean: "Mean" = None,
        stddev: "Stddev" = None
    ):
        self.__version__ = sdf_version
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.mean = mean
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Accel":
        kwargs = {"sdf_version": target_version}
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("accel")
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
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
        return cls(sdf_version=version, bias_mean=_bias_mean, bias_stddev=_bias_stddev, mean=_mean, stddev=_stddev)


class AngularVelocity(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "AngularVelocity":
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
        el = ET.Element("angular_velocity")
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


class CustomRpy(BaseModel):
    def __init__(self, sdf_version: str, custom_rpy: _SDFVector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if custom_rpy is None:
            custom_rpy = _SDFVector3.from_sdf("0 0 0")
        self.custom_rpy = custom_rpy
        self.parent_frame = parent_frame

    def to_version(self, target_version: str) -> "CustomRpy":
        kwargs = {"sdf_version": target_version}
        kwargs["custom_rpy"] = self.custom_rpy
        kwargs["parent_frame"] = self.parent_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("custom_rpy")
        if self.custom_rpy is not None:
            el.text = self.custom_rpy.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _custom_rpy = _SDFVector3._from_sdf(_text, version)
        if isinstance(_custom_rpy, SDFError):
            return _custom_rpy
        _parent_frame = el.get("parent_frame", "")
        if isinstance(_parent_frame, SDFError):
            return _parent_frame.extend("@parent_frame")
        return cls(sdf_version=version, custom_rpy=_custom_rpy, parent_frame=_parent_frame)


class EnableOrientation(BaseModel):
    def __init__(self, sdf_version: str, enable_orientation: bool = True):
        self.__version__ = sdf_version
        self.enable_orientation = enable_orientation

    def to_version(self, target_version: str) -> "EnableOrientation":
        if self.enable_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_orientation"] = self.enable_orientation
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_orientation")
        if self.enable_orientation is not None:
            el.text = str(self.enable_orientation).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _enable_orientation = str(_text).strip().lower() == 'true'
        if isinstance(_enable_orientation, SDFError):
            return _enable_orientation
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            if _enable_orientation != True:
                return SDFError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, enable_orientation=_enable_orientation)


class GravDirX(BaseModel):
    def __init__(self, sdf_version: str, grav_dir_x: _SDFVector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if grav_dir_x is None:
            grav_dir_x = _SDFVector3.from_sdf("1 0 0")
        self.grav_dir_x = grav_dir_x
        self.parent_frame = parent_frame

    def to_version(self, target_version: str) -> "GravDirX":
        kwargs = {"sdf_version": target_version}
        kwargs["grav_dir_x"] = self.grav_dir_x
        kwargs["parent_frame"] = self.parent_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grav_dir_x")
        if self.grav_dir_x is not None:
            el.text = self.grav_dir_x.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 0 0"
        _grav_dir_x = _SDFVector3._from_sdf(_text, version)
        if isinstance(_grav_dir_x, SDFError):
            return _grav_dir_x
        _parent_frame = el.get("parent_frame", "")
        if isinstance(_parent_frame, SDFError):
            return _parent_frame.extend("@parent_frame")
        return cls(sdf_version=version, grav_dir_x=_grav_dir_x, parent_frame=_parent_frame)


class Imu(BaseModel):
    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}, {"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}]}]

    def __init__(
        self,
        sdf_version: str,
        angular_velocity: "AngularVelocity" = None,
        enable_orientation: "EnableOrientation" = None,
        linear_acceleration: "LinearAcceleration" = None,
        noise: "Noise" = None,
        orientation_reference_frame: "OrientationReferenceFrame" = None,
        topic: "Topic" = None
    ):
        self.__version__ = sdf_version
        self.angular_velocity = angular_velocity
        self.enable_orientation = enable_orientation
        self.linear_acceleration = linear_acceleration
        self.noise = noise
        self.orientation_reference_frame = orientation_reference_frame
        self.topic = topic

    def to_version(self, target_version: str) -> "Imu":
        from ..elements.noise import Noise
        if self.angular_velocity is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'angular_velocity' is not supported in SDF version {target_version} (added in 1.5)")
        if self.enable_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        if self.linear_acceleration is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'linear_acceleration' is not supported in SDF version {target_version} (added in 1.5)")
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.noise is not None and cmp_version(target_version, "1.6") >= 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (removed in 1.6)")
        if self.orientation_reference_frame is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'orientation_reference_frame' is not supported in SDF version {target_version} (added in 1.6)")
        if self.topic is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'topic' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if self.angular_velocity is not None else None
        kwargs["enable_orientation"] = self.enable_orientation.to_version(target_version) if self.enable_orientation is not None else None
        kwargs["linear_acceleration"] = self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["orientation_reference_frame"] = self.orientation_reference_frame.to_version(target_version) if self.orientation_reference_frame is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.noise import Noise
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("imu")
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
        if self.enable_orientation is not None:
            el.append(self.enable_orientation.to_sdf(version))
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.orientation_reference_frame is not None:
            el.append(self.orientation_reference_frame.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.noise import Noise
        _c_angular_velocity = el.find("angular_velocity")
        if _c_angular_velocity is not None:
            _res = AngularVelocity._from_sdf(_c_angular_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_velocity")
            _angular_velocity = _res
        else:
            _angular_velocity = None
        if _angular_velocity is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'angular_velocity' is not supported in SDF version {version} (added in 1.5)")
        _c_enable_orientation = el.find("enable_orientation")
        if _c_enable_orientation is not None:
            _res = EnableOrientation._from_sdf(_c_enable_orientation, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_orientation")
            _enable_orientation = _res
        else:
            _enable_orientation = None
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        _c_linear_acceleration = el.find("linear_acceleration")
        if _c_linear_acceleration is not None:
            _res = LinearAcceleration._from_sdf(_c_linear_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_acceleration")
            _linear_acceleration = _res
        else:
            _linear_acceleration = None
        if _linear_acceleration is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'linear_acceleration' is not supported in SDF version {version} (added in 1.5)")
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
        _c_orientation_reference_frame = el.find("orientation_reference_frame")
        if _c_orientation_reference_frame is not None:
            _res = OrientationReferenceFrame._from_sdf(_c_orientation_reference_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("orientation_reference_frame")
            _orientation_reference_frame = _res
        else:
            _orientation_reference_frame = None
        if _orientation_reference_frame is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'orientation_reference_frame' is not supported in SDF version {version} (added in 1.6)")
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = Topic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        return cls(sdf_version=version, angular_velocity=_angular_velocity, enable_orientation=_enable_orientation, linear_acceleration=_linear_acceleration, noise=_noise, orientation_reference_frame=_orientation_reference_frame, topic=_topic)


class LinearAcceleration(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "LinearAcceleration":
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
        el = ET.Element("linear_acceleration")
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


class Localization(BaseModel):
    def __init__(self, sdf_version: str, localization: str = "CUSTOM"):
        self.__version__ = sdf_version
        self.localization = localization

    def to_version(self, target_version: str) -> "Localization":
        kwargs = {"sdf_version": target_version}
        kwargs["localization"] = self.localization
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("localization")
        if self.localization is not None:
            el.text = self.localization
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "CUSTOM"
        _localization = _text
        if isinstance(_localization, SDFError):
            return _localization
        return cls(sdf_version=version, localization=_localization)


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


class Noise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        accel: "Accel" = None,
        rate: "Rate" = None,
        type: "Type" = None
    ):
        self.__version__ = sdf_version
        self.accel = accel
        self.rate = rate
        self.type = type

    def to_version(self, target_version: str) -> "Noise":
        kwargs = {"sdf_version": target_version}
        kwargs["accel"] = self.accel.to_version(target_version) if self.accel is not None else None
        kwargs["rate"] = self.rate.to_version(target_version) if self.rate is not None else None
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.accel is None:
            self.accel = Accel(sdf_version=version)
        if self.accel is not None:
            el.append(self.accel.to_sdf(version))
        if self.rate is None:
            self.rate = Rate(sdf_version=version)
        if self.rate is not None:
            el.append(self.rate.to_sdf(version))
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_accel = el.find("accel")
        if _c_accel is not None:
            _res = Accel._from_sdf(_c_accel, version)
            if isinstance(_res, SDFError):
                return _res.extend("accel")
            _accel = _res
        else:
            _res = Accel._from_sdf(ET.Element("accel"), version)
            if isinstance(_res, SDFError):
                return _res.extend("accel")
            _accel = _res
        _c_rate = el.find("rate")
        if _c_rate is not None:
            _res = Rate._from_sdf(_c_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("rate")
            _rate = _res
        else:
            _res = Rate._from_sdf(ET.Element("rate"), version)
            if isinstance(_res, SDFError):
                return _res.extend("rate")
            _rate = _res
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        return cls(sdf_version=version, accel=_accel, rate=_rate, type=_type)


class OrientationReferenceFrame(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        custom_rpy: "CustomRpy" = None,
        grav_dir_x: "GravDirX" = None,
        localization: "Localization" = None
    ):
        self.__version__ = sdf_version
        self.custom_rpy = custom_rpy
        self.grav_dir_x = grav_dir_x
        self.localization = localization

    def to_version(self, target_version: str) -> "OrientationReferenceFrame":
        kwargs = {"sdf_version": target_version}
        kwargs["custom_rpy"] = self.custom_rpy.to_version(target_version) if self.custom_rpy is not None else None
        kwargs["grav_dir_x"] = self.grav_dir_x.to_version(target_version) if self.grav_dir_x is not None else None
        kwargs["localization"] = self.localization.to_version(target_version) if self.localization is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("orientation_reference_frame")
        if self.custom_rpy is not None:
            el.append(self.custom_rpy.to_sdf(version))
        if self.grav_dir_x is not None:
            el.append(self.grav_dir_x.to_sdf(version))
        if self.localization is not None:
            el.append(self.localization.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_custom_rpy = el.find("custom_rpy")
        if _c_custom_rpy is not None:
            _res = CustomRpy._from_sdf(_c_custom_rpy, version)
            if isinstance(_res, SDFError):
                return _res.extend("custom_rpy")
            _custom_rpy = _res
        else:
            _custom_rpy = None
        _c_grav_dir_x = el.find("grav_dir_x")
        if _c_grav_dir_x is not None:
            _res = GravDirX._from_sdf(_c_grav_dir_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("grav_dir_x")
            _grav_dir_x = _res
        else:
            _grav_dir_x = None
        _c_localization = el.find("localization")
        if _c_localization is not None:
            _res = Localization._from_sdf(_c_localization, version)
            if isinstance(_res, SDFError):
                return _res.extend("localization")
            _localization = _res
        else:
            _localization = None
        return cls(sdf_version=version, custom_rpy=_custom_rpy, grav_dir_x=_grav_dir_x, localization=_localization)


class Rate(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        mean: "Mean" = None,
        stddev: "Stddev" = None
    ):
        self.__version__ = sdf_version
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.mean = mean
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Rate":
        kwargs = {"sdf_version": target_version}
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rate")
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
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
        return cls(sdf_version=version, bias_mean=_bias_mean, bias_stddev=_bias_stddev, mean=_mean, stddev=_stddev)


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


class Topic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = "__default_topic__"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "Topic":
        if self.topic is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'topic' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default_topic__"
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


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


class X(BaseModel):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "X":
        from ..elements.noise import Noise
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.noise import Noise
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("x")
        if self.noise is None:
            self.noise = Noise(sdf_version=version)
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.noise import Noise
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _res = Noise._from_sdf(ET.Element("noise"), version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        return cls(sdf_version=version, noise=_noise)


class Y(BaseModel):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Y":
        from ..elements.noise import Noise
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.noise import Noise
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("y")
        if self.noise is None:
            self.noise = Noise(sdf_version=version)
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.noise import Noise
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _res = Noise._from_sdf(ET.Element("noise"), version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        return cls(sdf_version=version, noise=_noise)


class Z(BaseModel):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Z":
        from ..elements.noise import Noise
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.noise import Noise
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("z")
        if self.noise is None:
            self.noise = Noise(sdf_version=version)
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.noise import Noise
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _res = Noise._from_sdf(ET.Element("noise"), version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        return cls(sdf_version=version, noise=_noise)
