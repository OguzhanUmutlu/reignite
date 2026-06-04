### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Imu(BaseModel):
    class AngularVelocity(BaseModel):
        class X(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, 'sdfversion', None) is None:
                        self.noise.sdfversion = self.sdfversion
                    elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.noise = self.noise.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "Imu.AngularVelocity.X":
                from ..elements.noise import Noise
                kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                from ..elements.noise import Noise
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("x")
                if self.noise is not None:
                    _child_res = self.noise.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('noise')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.AngularVelocity.X | SDFError":
                from ..elements.noise import Noise
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
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, 'sdfversion', None) is None:
                        self.noise.sdfversion = self.sdfversion
                    elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.noise = self.noise.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "Imu.AngularVelocity.Y":
                from ..elements.noise import Noise
                kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                from ..elements.noise import Noise
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("y")
                if self.noise is not None:
                    _child_res = self.noise.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('noise')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.AngularVelocity.Y | SDFError":
                from ..elements.noise import Noise
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
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, 'sdfversion', None) is None:
                        self.noise.sdfversion = self.sdfversion
                    elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.noise = self.noise.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "Imu.AngularVelocity.Z":
                from ..elements.noise import Noise
                kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                from ..elements.noise import Noise
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("z")
                if self.noise is not None:
                    _child_res = self.noise.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('noise')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.AngularVelocity.Z | SDFError":
                from ..elements.noise import Noise
                _c_noise = el.find("noise")
                if _c_noise is not None:
                    _res = Noise._from_sdf(_c_noise, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("noise")
                    _noise = _res
                else:
                    _noise = None
                return cls(sdf_version=version, noise=_noise)

        def __init__(
            self,
            sdf_version: str | None = None,
            x: "Imu.AngularVelocity.X" = None,
            y: "Imu.AngularVelocity.Y" = None,
            z: "Imu.AngularVelocity.Z" = None
        ):
            super().__init__(sdf_version)
            self.x = x
            self.y = y
            self.z = z
            if self.x is not None and hasattr(self.x, 'to_version'):
                if getattr(self.x, 'sdfversion', None) is None:
                    self.x.sdfversion = self.sdfversion
                elif getattr(self.x, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.x = self.x.to_version(self.sdfversion)
            if self.y is not None and hasattr(self.y, 'to_version'):
                if getattr(self.y, 'sdfversion', None) is None:
                    self.y.sdfversion = self.sdfversion
                elif getattr(self.y, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.y = self.y.to_version(self.sdfversion)
            if self.z is not None and hasattr(self.z, 'to_version'):
                if getattr(self.z, 'sdfversion', None) is None:
                    self.z.sdfversion = self.sdfversion
                elif getattr(self.z, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.z = self.z.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Imu.AngularVelocity":
            kwargs: dict = {"sdf_version": target_version, "x": self.x.to_version(target_version) if self.x is not None and hasattr(self.x, "to_version") else self.x, "y": self.y.to_version(target_version) if self.y is not None and hasattr(self.y, "to_version") else self.y, "z": self.z.to_version(target_version) if self.z is not None and hasattr(self.z, "to_version") else self.z}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("angular_velocity")
            if self.x is not None:
                _child_res = self.x.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('x')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.y is not None:
                _child_res = self.y.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('y')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.z is not None:
                _child_res = self.z.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('z')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.AngularVelocity | SDFError":
            _c_x = el.find("x")
            if _c_x is not None:
                _res = cls.X._from_sdf(_c_x, version)
                if isinstance(_res, SDFError):
                    return _res.extend("x")
                _x = _res
            else:
                _x = None
            _c_y = el.find("y")
            if _c_y is not None:
                _res = cls.Y._from_sdf(_c_y, version)
                if isinstance(_res, SDFError):
                    return _res.extend("y")
                _y = _res
            else:
                _y = None
            _c_z = el.find("z")
            if _c_z is not None:
                _res = cls.Z._from_sdf(_c_z, version)
                if isinstance(_res, SDFError):
                    return _res.extend("z")
                _z = _res
            else:
                _z = None
            return cls(sdf_version=version, x=_x, y=_y, z=_z)

    class LinearAcceleration(BaseModel):
        def __init__(self, sdf_version: str | None = None, x: "X" = None, y: "Y" = None, z: "Z" = None):
            super().__init__(sdf_version)
            self.x = x
            self.y = y
            self.z = z
            if self.x is not None and hasattr(self.x, 'to_version'):
                if getattr(self.x, 'sdfversion', None) is None:
                    self.x.sdfversion = self.sdfversion
                elif getattr(self.x, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.x = self.x.to_version(self.sdfversion)
            if self.y is not None and hasattr(self.y, 'to_version'):
                if getattr(self.y, 'sdfversion', None) is None:
                    self.y.sdfversion = self.sdfversion
                elif getattr(self.y, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.y = self.y.to_version(self.sdfversion)
            if self.z is not None and hasattr(self.z, 'to_version'):
                if getattr(self.z, 'sdfversion', None) is None:
                    self.z.sdfversion = self.sdfversion
                elif getattr(self.z, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.z = self.z.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Imu.LinearAcceleration":
            kwargs: dict = {"sdf_version": target_version, "x": self.x.to_version(target_version) if self.x is not None and hasattr(self.x, "to_version") else self.x, "y": self.y.to_version(target_version) if self.y is not None and hasattr(self.y, "to_version") else self.y, "z": self.z.to_version(target_version) if self.z is not None and hasattr(self.z, "to_version") else self.z}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("linear_acceleration")
            if self.x is not None:
                _child_res = self.x.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('x')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.y is not None:
                _child_res = self.y.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('y')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.z is not None:
                _child_res = self.z.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('z')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.LinearAcceleration | SDFError":
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

    class Noise(BaseModel):
        class Accel(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                bias_mean: float | None = None,
                bias_stddev: float | None = None,
                mean: float | None = None,
                stddev: float | None = None
            ):
                super().__init__(sdf_version)
                self.bias_mean = bias_mean
                self.bias_stddev = bias_stddev
                self.mean = mean
                self.stddev = stddev

            def to_version(self, target_version: str) -> "Imu.Noise.Accel":
                kwargs: dict = {"sdf_version": target_version, "bias_mean": self.bias_mean, "bias_stddev": self.bias_stddev, "mean": self.mean, "stddev": self.stddev}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("accel")
                if self.bias_mean is not None:
                    _c_tmp = ET.Element("bias_mean")
                    _c_tmp.text = str(self.bias_mean)
                    el.append(_c_tmp)
                if self.bias_stddev is not None:
                    _c_tmp = ET.Element("bias_stddev")
                    _c_tmp.text = str(self.bias_stddev)
                    el.append(_c_tmp)
                if self.mean is not None:
                    _c_tmp = ET.Element("mean")
                    _c_tmp.text = str(self.mean)
                    el.append(_c_tmp)
                if self.stddev is not None:
                    _c_tmp = ET.Element("stddev")
                    _c_tmp.text = str(self.stddev)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.Noise.Accel | SDFError":
                _c_tmp = el.find("bias_mean")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("bias_mean")
                    _bias_mean = _val
                else:
                    _bias_mean = None
                _c_tmp = el.find("bias_stddev")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("bias_stddev")
                    _bias_stddev = _val
                else:
                    _bias_stddev = None
                _c_tmp = el.find("mean")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("mean")
                    _mean = _val
                else:
                    _mean = None
                _c_tmp = el.find("stddev")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("stddev")
                    _stddev = _val
                else:
                    _stddev = None
                return cls(sdf_version=version, bias_mean=_bias_mean, bias_stddev=_bias_stddev, mean=_mean, stddev=_stddev)

        class Rate(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                bias_mean: float | None = None,
                bias_stddev: float | None = None,
                mean: float | None = None,
                stddev: float | None = None
            ):
                super().__init__(sdf_version)
                self.bias_mean = bias_mean
                self.bias_stddev = bias_stddev
                self.mean = mean
                self.stddev = stddev

            def to_version(self, target_version: str) -> "Imu.Noise.Rate":
                kwargs: dict = {"sdf_version": target_version, "bias_mean": self.bias_mean, "bias_stddev": self.bias_stddev, "mean": self.mean, "stddev": self.stddev}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("rate")
                if self.bias_mean is not None:
                    _c_tmp = ET.Element("bias_mean")
                    _c_tmp.text = str(self.bias_mean)
                    el.append(_c_tmp)
                if self.bias_stddev is not None:
                    _c_tmp = ET.Element("bias_stddev")
                    _c_tmp.text = str(self.bias_stddev)
                    el.append(_c_tmp)
                if self.mean is not None:
                    _c_tmp = ET.Element("mean")
                    _c_tmp.text = str(self.mean)
                    el.append(_c_tmp)
                if self.stddev is not None:
                    _c_tmp = ET.Element("stddev")
                    _c_tmp.text = str(self.stddev)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.Noise.Rate | SDFError":
                _c_tmp = el.find("bias_mean")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("bias_mean")
                    _bias_mean = _val
                else:
                    _bias_mean = None
                _c_tmp = el.find("bias_stddev")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("bias_stddev")
                    _bias_stddev = _val
                else:
                    _bias_stddev = None
                _c_tmp = el.find("mean")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("mean")
                    _mean = _val
                else:
                    _mean = None
                _c_tmp = el.find("stddev")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("stddev")
                    _stddev = _val
                else:
                    _stddev = None
                return cls(sdf_version=version, bias_mean=_bias_mean, bias_stddev=_bias_stddev, mean=_mean, stddev=_stddev)

        def __init__(
            self,
            sdf_version: str | None = None,
            accel: "Imu.Noise.Accel" = None,
            rate: "Imu.Noise.Rate" = None,
            type: str | None = None
        ):
            super().__init__(sdf_version)
            self.accel = accel
            self.rate = rate
            self.type = type
            if self.accel is not None and hasattr(self.accel, 'to_version'):
                if getattr(self.accel, 'sdfversion', None) is None:
                    self.accel.sdfversion = self.sdfversion
                elif getattr(self.accel, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.accel = self.accel.to_version(self.sdfversion)
            if self.rate is not None and hasattr(self.rate, 'to_version'):
                if getattr(self.rate, 'sdfversion', None) is None:
                    self.rate.sdfversion = self.sdfversion
                elif getattr(self.rate, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.rate = self.rate.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Imu.Noise":
            kwargs: dict = {"sdf_version": target_version, "accel": self.accel.to_version(target_version) if self.accel is not None and hasattr(self.accel, "to_version") else self.accel, "rate": self.rate.to_version(target_version) if self.rate is not None and hasattr(self.rate, "to_version") else self.rate, "type": self.type}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("noise")
            if self.accel is not None:
                _child_res = self.accel.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('accel')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.rate is not None:
                _child_res = self.rate.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('rate')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.type is not None:
                _c_tmp = ET.Element("type")
                _c_tmp.text = self.type
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.Noise | SDFError":
            _c_accel = el.find("accel")
            if _c_accel is not None:
                _res = cls.Accel._from_sdf(_c_accel, version)
                if isinstance(_res, SDFError):
                    return _res.extend("accel")
                _accel = _res
            else:
                _accel = None
            _c_rate = el.find("rate")
            if _c_rate is not None:
                _res = cls.Rate._from_sdf(_c_rate, version)
                if isinstance(_res, SDFError):
                    return _res.extend("rate")
                _rate = _res
            else:
                _rate = None
            _c_tmp = el.find("type")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "gaussian"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("type")
                _type = _val
            else:
                _type = None
            return cls(sdf_version=version, accel=_accel, rate=_rate, type=_type)

    class OrientationReferenceFrame(BaseModel):
        class CustomRpy(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                custom_rpy: _Vector3T | None = None,
                parent_frame: str | None = ""
            ):
                super().__init__(sdf_version)
                self.custom_rpy = _vector3(custom_rpy) if custom_rpy is not None else None
                self.parent_frame = parent_frame

            def to_version(self, target_version: str) -> "Imu.OrientationReferenceFrame.CustomRpy":
                kwargs: dict = {"sdf_version": target_version, "custom_rpy": self.custom_rpy, "parent_frame": self.parent_frame}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("custom_rpy")
                if self.custom_rpy is not None:
                    el.text = str(self.custom_rpy)
                if self.parent_frame is not None:
                    el.set("parent_frame", self.parent_frame)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.OrientationReferenceFrame.CustomRpy | SDFError":
                _text = el.text or "0 0 0"
                _custom_rpy = _parse_vector3(_text)
                if isinstance(_custom_rpy, SDFError):
                    return _custom_rpy
                _parent_frame = el.get("parent_frame", "")
                if isinstance(_parent_frame, SDFError):
                    return _parent_frame.extend("@parent_frame")
                return cls(sdf_version=version, custom_rpy=_custom_rpy, parent_frame=_parent_frame)

        class GravDirX(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                grav_dir_x: _Vector3T | None = None,
                parent_frame: str | None = ""
            ):
                super().__init__(sdf_version)
                self.grav_dir_x = _vector3(grav_dir_x) if grav_dir_x is not None else None
                self.parent_frame = parent_frame

            def to_version(self, target_version: str) -> "Imu.OrientationReferenceFrame.GravDirX":
                kwargs: dict = {"sdf_version": target_version, "grav_dir_x": self.grav_dir_x, "parent_frame": self.parent_frame}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("grav_dir_x")
                if self.grav_dir_x is not None:
                    el.text = str(self.grav_dir_x)
                if self.parent_frame is not None:
                    el.set("parent_frame", self.parent_frame)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.OrientationReferenceFrame.GravDirX | SDFError":
                _text = el.text or "1 0 0"
                _grav_dir_x = _parse_vector3(_text)
                if isinstance(_grav_dir_x, SDFError):
                    return _grav_dir_x
                _parent_frame = el.get("parent_frame", "")
                if isinstance(_parent_frame, SDFError):
                    return _parent_frame.extend("@parent_frame")
                return cls(sdf_version=version, grav_dir_x=_grav_dir_x, parent_frame=_parent_frame)

        def __init__(
            self,
            sdf_version: str | None = None,
            custom_rpy: "Imu.OrientationReferenceFrame.CustomRpy" = None,
            grav_dir_x: "Imu.OrientationReferenceFrame.GravDirX" = None,
            localization: str | None = None
        ):
            super().__init__(sdf_version)
            self.custom_rpy = custom_rpy
            self.grav_dir_x = grav_dir_x
            self.localization = localization
            if self.custom_rpy is not None and hasattr(self.custom_rpy, 'to_version'):
                if getattr(self.custom_rpy, 'sdfversion', None) is None:
                    self.custom_rpy.sdfversion = self.sdfversion
                elif getattr(self.custom_rpy, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.custom_rpy = self.custom_rpy.to_version(self.sdfversion)
            if self.grav_dir_x is not None and hasattr(self.grav_dir_x, 'to_version'):
                if getattr(self.grav_dir_x, 'sdfversion', None) is None:
                    self.grav_dir_x.sdfversion = self.sdfversion
                elif getattr(self.grav_dir_x, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.grav_dir_x = self.grav_dir_x.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Imu.OrientationReferenceFrame":
            kwargs: dict = {"sdf_version": target_version, "custom_rpy": self.custom_rpy.to_version(target_version) if self.custom_rpy is not None and hasattr(self.custom_rpy, "to_version") else self.custom_rpy, "grav_dir_x": self.grav_dir_x.to_version(target_version) if self.grav_dir_x is not None and hasattr(self.grav_dir_x, "to_version") else self.grav_dir_x, "localization": self.localization}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("orientation_reference_frame")
            if self.custom_rpy is not None:
                _child_res = self.custom_rpy.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('custom_rpy')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.grav_dir_x is not None:
                _child_res = self.grav_dir_x.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('grav_dir_x')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.localization is not None:
                _c_tmp = ET.Element("localization")
                _c_tmp.text = self.localization
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Imu.OrientationReferenceFrame | SDFError":
            _c_custom_rpy = el.find("custom_rpy")
            if _c_custom_rpy is not None:
                _res = cls.CustomRpy._from_sdf(_c_custom_rpy, version)
                if isinstance(_res, SDFError):
                    return _res.extend("custom_rpy")
                _custom_rpy = _res
            else:
                _custom_rpy = None
            _c_grav_dir_x = el.find("grav_dir_x")
            if _c_grav_dir_x is not None:
                _res = cls.GravDirX._from_sdf(_c_grav_dir_x, version)
                if isinstance(_res, SDFError):
                    return _res.extend("grav_dir_x")
                _grav_dir_x = _res
            else:
                _grav_dir_x = None
            _c_tmp = el.find("localization")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "CUSTOM"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("localization")
                _localization = _val
            else:
                _localization = None
            return cls(sdf_version=version, custom_rpy=_custom_rpy, grav_dir_x=_grav_dir_x, localization=_localization)

    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}, {"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}]}]

    def __init__(
        self,
        sdf_version: str | None = None,
        angular_velocity: "Imu.AngularVelocity" = None,
        enable_orientation: bool | None = None,
        linear_acceleration: "Imu.LinearAcceleration" = None,
        noise: "Imu.Noise" = None,
        orientation_reference_frame: "Imu.OrientationReferenceFrame" = None,
        topic: str | None = None
    ):
        super().__init__(sdf_version)
        self.angular_velocity = angular_velocity
        self.enable_orientation = enable_orientation
        self.linear_acceleration = linear_acceleration
        self.noise = noise
        self.orientation_reference_frame = orientation_reference_frame
        self.topic = topic
        if self.angular_velocity is not None and hasattr(self.angular_velocity, 'to_version'):
            if getattr(self.angular_velocity, 'sdfversion', None) is None:
                self.angular_velocity.sdfversion = self.sdfversion
            elif getattr(self.angular_velocity, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.angular_velocity = self.angular_velocity.to_version(self.sdfversion)
        if self.linear_acceleration is not None and hasattr(self.linear_acceleration, 'to_version'):
            if getattr(self.linear_acceleration, 'sdfversion', None) is None:
                self.linear_acceleration.sdfversion = self.sdfversion
            elif getattr(self.linear_acceleration, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.linear_acceleration = self.linear_acceleration.to_version(self.sdfversion)
        if self.noise is not None and hasattr(self.noise, 'to_version'):
            if getattr(self.noise, 'sdfversion', None) is None:
                self.noise.sdfversion = self.sdfversion
            elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.noise = self.noise.to_version(self.sdfversion)
        if self.orientation_reference_frame is not None and hasattr(self.orientation_reference_frame, 'to_version'):
            if getattr(self.orientation_reference_frame, 'sdfversion', None) is None:
                self.orientation_reference_frame.sdfversion = self.sdfversion
            elif getattr(self.orientation_reference_frame, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.orientation_reference_frame = self.orientation_reference_frame.to_version(self.sdfversion)

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
        kwargs: dict = {"sdf_version": target_version, "angular_velocity": self.angular_velocity.to_version(target_version) if self.angular_velocity is not None and hasattr(self.angular_velocity, "to_version") else self.angular_velocity, "enable_orientation": self.enable_orientation, "linear_acceleration": self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None and hasattr(self.linear_acceleration, "to_version") else self.linear_acceleration, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise, "orientation_reference_frame": self.orientation_reference_frame.to_version(target_version) if self.orientation_reference_frame is not None and hasattr(self.orientation_reference_frame, "to_version") else self.orientation_reference_frame, "topic": self.topic}
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.noise import Noise
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("imu")
        if self.angular_velocity is not None:
            _child_res = self.angular_velocity.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('angular_velocity')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.enable_orientation is not None:
            _c_tmp = ET.Element("enable_orientation")
            _c_tmp.text = str(self.enable_orientation).lower()
            el.append(_c_tmp)
        if self.linear_acceleration is not None:
            _child_res = self.linear_acceleration.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('linear_acceleration')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.noise is not None:
            _child_res = self.noise.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('noise')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.orientation_reference_frame is not None:
            _child_res = self.orientation_reference_frame.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('orientation_reference_frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.topic is not None:
            _c_tmp = ET.Element("topic")
            _c_tmp.text = self.topic
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Imu | SDFError":
        from ..elements.noise import Noise
        _c_angular_velocity = el.find("angular_velocity")
        if _c_angular_velocity is not None:
            _res = cls.AngularVelocity._from_sdf(_c_angular_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_velocity")
            _angular_velocity = _res
        else:
            _angular_velocity = None
        if _angular_velocity is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'angular_velocity' is not supported in SDF version {version} (added in 1.5)")
        _c_tmp = el.find("enable_orientation")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else True
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("enable_orientation")
            _enable_orientation = _val
        else:
            _enable_orientation = None
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        _c_linear_acceleration = el.find("linear_acceleration")
        if _c_linear_acceleration is not None:
            _res = cls.LinearAcceleration._from_sdf(_c_linear_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_acceleration")
            _linear_acceleration = _res
        else:
            _linear_acceleration = None
        if _linear_acceleration is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'linear_acceleration' is not supported in SDF version {version} (added in 1.5)")
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = cls.Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_orientation_reference_frame = el.find("orientation_reference_frame")
        if _c_orientation_reference_frame is not None:
            _res = cls.OrientationReferenceFrame._from_sdf(_c_orientation_reference_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("orientation_reference_frame")
            _orientation_reference_frame = _res
        else:
            _orientation_reference_frame = None
        if _orientation_reference_frame is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'orientation_reference_frame' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("topic")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default_topic__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("topic")
            _topic = _val
        else:
            _topic = None
        return cls(sdf_version=version, angular_velocity=_angular_velocity, enable_orientation=_enable_orientation, linear_acceleration=_linear_acceleration, noise=_noise, orientation_reference_frame=_orientation_reference_frame, topic=_topic)
