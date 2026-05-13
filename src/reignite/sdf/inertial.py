### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.pose import Pose


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



class Inertial(BaseModel):
    class AutoInertiaParams(BaseModel):
        def __init__(self, sdf_version: str | None = None):
            super().__init__(sdf_version)

        def to_version(self, target_version: str) -> "Inertial.AutoInertiaParams":
            kwargs = {"sdf_version": target_version}
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("auto_inertia_params")
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.AutoInertiaParams | SDFError":
            return cls(sdf_version=version)

    class Density(BaseModel):
        def __init__(self, sdf_version: str | None = None, density: float = 1000.0):
            super().__init__(sdf_version)
            self.density = density

        def to_version(self, target_version: str) -> "Inertial.Density":
            if self.density is not None and cmp_version(target_version, "1.11") < 0:
                raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.11)")
            kwargs = {"sdf_version": target_version}
            kwargs["density"] = self.density
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("density")
            if self.density is not None:
                el.text = str(self.density)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Density | SDFError":
            _text = el.text or 1000.0
            _density = _parse_double(_text)
            if isinstance(_density, SDFError):
                return _density
            if _density is not None and cmp_version(version, "1.11") < 0:
                if _density != 1000.0:
                    return SDFError(f"'density' is not supported in SDF version {version} (added in 1.11)")
            return cls(sdf_version=version, density=_density)

    class FluidAddedMass(BaseModel):
        class Pp(BaseModel):
            def __init__(self, sdf_version: str | None = None, pp: float = 0.0):
                super().__init__(sdf_version)
                self.pp = pp

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Pp":
                kwargs = {"sdf_version": target_version}
                kwargs["pp"] = self.pp
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("pp")
                if self.pp is not None:
                    el.text = str(self.pp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Pp | SDFError":
                _text = el.text or 0.0
                _pp = _parse_double(_text)
                if isinstance(_pp, SDFError):
                    return _pp
                return cls(sdf_version=version, pp=_pp)

        class Pq(BaseModel):
            def __init__(self, sdf_version: str | None = None, pq: float = 0.0):
                super().__init__(sdf_version)
                self.pq = pq

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Pq":
                kwargs = {"sdf_version": target_version}
                kwargs["pq"] = self.pq
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("pq")
                if self.pq is not None:
                    el.text = str(self.pq)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Pq | SDFError":
                _text = el.text or 0.0
                _pq = _parse_double(_text)
                if isinstance(_pq, SDFError):
                    return _pq
                return cls(sdf_version=version, pq=_pq)

        class Pr(BaseModel):
            def __init__(self, sdf_version: str | None = None, pr: float = 0.0):
                super().__init__(sdf_version)
                self.pr = pr

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Pr":
                kwargs = {"sdf_version": target_version}
                kwargs["pr"] = self.pr
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("pr")
                if self.pr is not None:
                    el.text = str(self.pr)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Pr | SDFError":
                _text = el.text or 0.0
                _pr = _parse_double(_text)
                if isinstance(_pr, SDFError):
                    return _pr
                return cls(sdf_version=version, pr=_pr)

        class Qq(BaseModel):
            def __init__(self, sdf_version: str | None = None, qq: float = 0.0):
                super().__init__(sdf_version)
                self.qq = qq

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Qq":
                kwargs = {"sdf_version": target_version}
                kwargs["qq"] = self.qq
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("qq")
                if self.qq is not None:
                    el.text = str(self.qq)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Qq | SDFError":
                _text = el.text or 0.0
                _qq = _parse_double(_text)
                if isinstance(_qq, SDFError):
                    return _qq
                return cls(sdf_version=version, qq=_qq)

        class Qr(BaseModel):
            def __init__(self, sdf_version: str | None = None, qr: float = 0.0):
                super().__init__(sdf_version)
                self.qr = qr

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Qr":
                kwargs = {"sdf_version": target_version}
                kwargs["qr"] = self.qr
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("qr")
                if self.qr is not None:
                    el.text = str(self.qr)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Qr | SDFError":
                _text = el.text or 0.0
                _qr = _parse_double(_text)
                if isinstance(_qr, SDFError):
                    return _qr
                return cls(sdf_version=version, qr=_qr)

        class Rr(BaseModel):
            def __init__(self, sdf_version: str | None = None, rr: float = 0.0):
                super().__init__(sdf_version)
                self.rr = rr

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Rr":
                kwargs = {"sdf_version": target_version}
                kwargs["rr"] = self.rr
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("rr")
                if self.rr is not None:
                    el.text = str(self.rr)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Rr | SDFError":
                _text = el.text or 0.0
                _rr = _parse_double(_text)
                if isinstance(_rr, SDFError):
                    return _rr
                return cls(sdf_version=version, rr=_rr)

        class Xp(BaseModel):
            def __init__(self, sdf_version: str | None = None, xp: float = 0.0):
                super().__init__(sdf_version)
                self.xp = xp

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Xp":
                kwargs = {"sdf_version": target_version}
                kwargs["xp"] = self.xp
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("xp")
                if self.xp is not None:
                    el.text = str(self.xp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Xp | SDFError":
                _text = el.text or 0.0
                _xp = _parse_double(_text)
                if isinstance(_xp, SDFError):
                    return _xp
                return cls(sdf_version=version, xp=_xp)

        class Xq(BaseModel):
            def __init__(self, sdf_version: str | None = None, xq: float = 0.0):
                super().__init__(sdf_version)
                self.xq = xq

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Xq":
                kwargs = {"sdf_version": target_version}
                kwargs["xq"] = self.xq
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("xq")
                if self.xq is not None:
                    el.text = str(self.xq)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Xq | SDFError":
                _text = el.text or 0.0
                _xq = _parse_double(_text)
                if isinstance(_xq, SDFError):
                    return _xq
                return cls(sdf_version=version, xq=_xq)

        class Xr(BaseModel):
            def __init__(self, sdf_version: str | None = None, xr: float = 0.0):
                super().__init__(sdf_version)
                self.xr = xr

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Xr":
                kwargs = {"sdf_version": target_version}
                kwargs["xr"] = self.xr
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("xr")
                if self.xr is not None:
                    el.text = str(self.xr)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Xr | SDFError":
                _text = el.text or 0.0
                _xr = _parse_double(_text)
                if isinstance(_xr, SDFError):
                    return _xr
                return cls(sdf_version=version, xr=_xr)

        class Xx(BaseModel):
            def __init__(self, sdf_version: str | None = None, xx: float = 0.0):
                super().__init__(sdf_version)
                self.xx = xx

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Xx":
                kwargs = {"sdf_version": target_version}
                kwargs["xx"] = self.xx
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("xx")
                if self.xx is not None:
                    el.text = str(self.xx)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Xx | SDFError":
                _text = el.text or 0.0
                _xx = _parse_double(_text)
                if isinstance(_xx, SDFError):
                    return _xx
                return cls(sdf_version=version, xx=_xx)

        class Xy(BaseModel):
            def __init__(self, sdf_version: str | None = None, xy: float = 0.0):
                super().__init__(sdf_version)
                self.xy = xy

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Xy":
                kwargs = {"sdf_version": target_version}
                kwargs["xy"] = self.xy
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("xy")
                if self.xy is not None:
                    el.text = str(self.xy)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Xy | SDFError":
                _text = el.text or 0.0
                _xy = _parse_double(_text)
                if isinstance(_xy, SDFError):
                    return _xy
                return cls(sdf_version=version, xy=_xy)

        class Xz(BaseModel):
            def __init__(self, sdf_version: str | None = None, xz: float = 0.0):
                super().__init__(sdf_version)
                self.xz = xz

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Xz":
                kwargs = {"sdf_version": target_version}
                kwargs["xz"] = self.xz
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("xz")
                if self.xz is not None:
                    el.text = str(self.xz)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Xz | SDFError":
                _text = el.text or 0.0
                _xz = _parse_double(_text)
                if isinstance(_xz, SDFError):
                    return _xz
                return cls(sdf_version=version, xz=_xz)

        class Yp(BaseModel):
            def __init__(self, sdf_version: str | None = None, yp: float = 0.0):
                super().__init__(sdf_version)
                self.yp = yp

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Yp":
                kwargs = {"sdf_version": target_version}
                kwargs["yp"] = self.yp
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("yp")
                if self.yp is not None:
                    el.text = str(self.yp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Yp | SDFError":
                _text = el.text or 0.0
                _yp = _parse_double(_text)
                if isinstance(_yp, SDFError):
                    return _yp
                return cls(sdf_version=version, yp=_yp)

        class Yq(BaseModel):
            def __init__(self, sdf_version: str | None = None, yq: float = 0.0):
                super().__init__(sdf_version)
                self.yq = yq

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Yq":
                kwargs = {"sdf_version": target_version}
                kwargs["yq"] = self.yq
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("yq")
                if self.yq is not None:
                    el.text = str(self.yq)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Yq | SDFError":
                _text = el.text or 0.0
                _yq = _parse_double(_text)
                if isinstance(_yq, SDFError):
                    return _yq
                return cls(sdf_version=version, yq=_yq)

        class Yr(BaseModel):
            def __init__(self, sdf_version: str | None = None, yr: float = 0.0):
                super().__init__(sdf_version)
                self.yr = yr

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Yr":
                kwargs = {"sdf_version": target_version}
                kwargs["yr"] = self.yr
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("yr")
                if self.yr is not None:
                    el.text = str(self.yr)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Yr | SDFError":
                _text = el.text or 0.0
                _yr = _parse_double(_text)
                if isinstance(_yr, SDFError):
                    return _yr
                return cls(sdf_version=version, yr=_yr)

        class Yy(BaseModel):
            def __init__(self, sdf_version: str | None = None, yy: float = 0.0):
                super().__init__(sdf_version)
                self.yy = yy

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Yy":
                kwargs = {"sdf_version": target_version}
                kwargs["yy"] = self.yy
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("yy")
                if self.yy is not None:
                    el.text = str(self.yy)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Yy | SDFError":
                _text = el.text or 0.0
                _yy = _parse_double(_text)
                if isinstance(_yy, SDFError):
                    return _yy
                return cls(sdf_version=version, yy=_yy)

        class Yz(BaseModel):
            def __init__(self, sdf_version: str | None = None, yz: float = 0.0):
                super().__init__(sdf_version)
                self.yz = yz

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Yz":
                kwargs = {"sdf_version": target_version}
                kwargs["yz"] = self.yz
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("yz")
                if self.yz is not None:
                    el.text = str(self.yz)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Yz | SDFError":
                _text = el.text or 0.0
                _yz = _parse_double(_text)
                if isinstance(_yz, SDFError):
                    return _yz
                return cls(sdf_version=version, yz=_yz)

        class Zp(BaseModel):
            def __init__(self, sdf_version: str | None = None, zp: float = 0.0):
                super().__init__(sdf_version)
                self.zp = zp

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Zp":
                kwargs = {"sdf_version": target_version}
                kwargs["zp"] = self.zp
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("zp")
                if self.zp is not None:
                    el.text = str(self.zp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Zp | SDFError":
                _text = el.text or 0.0
                _zp = _parse_double(_text)
                if isinstance(_zp, SDFError):
                    return _zp
                return cls(sdf_version=version, zp=_zp)

        class Zq(BaseModel):
            def __init__(self, sdf_version: str | None = None, zq: float = 0.0):
                super().__init__(sdf_version)
                self.zq = zq

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Zq":
                kwargs = {"sdf_version": target_version}
                kwargs["zq"] = self.zq
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("zq")
                if self.zq is not None:
                    el.text = str(self.zq)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Zq | SDFError":
                _text = el.text or 0.0
                _zq = _parse_double(_text)
                if isinstance(_zq, SDFError):
                    return _zq
                return cls(sdf_version=version, zq=_zq)

        class Zr(BaseModel):
            def __init__(self, sdf_version: str | None = None, zr: float = 0.0):
                super().__init__(sdf_version)
                self.zr = zr

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Zr":
                kwargs = {"sdf_version": target_version}
                kwargs["zr"] = self.zr
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("zr")
                if self.zr is not None:
                    el.text = str(self.zr)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Zr | SDFError":
                _text = el.text or 0.0
                _zr = _parse_double(_text)
                if isinstance(_zr, SDFError):
                    return _zr
                return cls(sdf_version=version, zr=_zr)

        class Zz(BaseModel):
            def __init__(self, sdf_version: str | None = None, zz: float = 0.0):
                super().__init__(sdf_version)
                self.zz = zz

            def to_version(self, target_version: str) -> "Inertial.FluidAddedMass.Zz":
                kwargs = {"sdf_version": target_version}
                kwargs["zz"] = self.zz
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("zz")
                if self.zz is not None:
                    el.text = str(self.zz)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass.Zz | SDFError":
                _text = el.text or 0.0
                _zz = _parse_double(_text)
                if isinstance(_zz, SDFError):
                    return _zz
                return cls(sdf_version=version, zz=_zz)

        def __init__(
            self,
            sdf_version: str | None = None,
            pp: "Inertial.FluidAddedMass.Pp" = None,
            pq: "Inertial.FluidAddedMass.Pq" = None,
            pr: "Inertial.FluidAddedMass.Pr" = None,
            qq: "Inertial.FluidAddedMass.Qq" = None,
            qr: "Inertial.FluidAddedMass.Qr" = None,
            rr: "Inertial.FluidAddedMass.Rr" = None,
            xp: "Inertial.FluidAddedMass.Xp" = None,
            xq: "Inertial.FluidAddedMass.Xq" = None,
            xr: "Inertial.FluidAddedMass.Xr" = None,
            xx: "Inertial.FluidAddedMass.Xx" = None,
            xy: "Inertial.FluidAddedMass.Xy" = None,
            xz: "Inertial.FluidAddedMass.Xz" = None,
            yp: "Inertial.FluidAddedMass.Yp" = None,
            yq: "Inertial.FluidAddedMass.Yq" = None,
            yr: "Inertial.FluidAddedMass.Yr" = None,
            yy: "Inertial.FluidAddedMass.Yy" = None,
            yz: "Inertial.FluidAddedMass.Yz" = None,
            zp: "Inertial.FluidAddedMass.Zp" = None,
            zq: "Inertial.FluidAddedMass.Zq" = None,
            zr: "Inertial.FluidAddedMass.Zr" = None,
            zz: "Inertial.FluidAddedMass.Zz" = None
        ):
            super().__init__(sdf_version)
            self.pp = pp
            self.pq = pq
            self.pr = pr
            self.qq = qq
            self.qr = qr
            self.rr = rr
            self.xp = xp
            self.xq = xq
            self.xr = xr
            self.xx = xx
            self.xy = xy
            self.xz = xz
            self.yp = yp
            self.yq = yq
            self.yr = yr
            self.yy = yy
            self.yz = yz
            self.zp = zp
            self.zq = zq
            self.zr = zr
            self.zz = zz
            if self.pp is not None:
                if getattr(self.pp, '__version__', None) is None:
                    self.pp.__version__ = self.__version__
                elif getattr(self.pp, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.pp = self.pp.to_version(self.__version__)
            if self.pq is not None:
                if getattr(self.pq, '__version__', None) is None:
                    self.pq.__version__ = self.__version__
                elif getattr(self.pq, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.pq = self.pq.to_version(self.__version__)
            if self.pr is not None:
                if getattr(self.pr, '__version__', None) is None:
                    self.pr.__version__ = self.__version__
                elif getattr(self.pr, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.pr = self.pr.to_version(self.__version__)
            if self.qq is not None:
                if getattr(self.qq, '__version__', None) is None:
                    self.qq.__version__ = self.__version__
                elif getattr(self.qq, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.qq = self.qq.to_version(self.__version__)
            if self.qr is not None:
                if getattr(self.qr, '__version__', None) is None:
                    self.qr.__version__ = self.__version__
                elif getattr(self.qr, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.qr = self.qr.to_version(self.__version__)
            if self.rr is not None:
                if getattr(self.rr, '__version__', None) is None:
                    self.rr.__version__ = self.__version__
                elif getattr(self.rr, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.rr = self.rr.to_version(self.__version__)
            if self.xp is not None:
                if getattr(self.xp, '__version__', None) is None:
                    self.xp.__version__ = self.__version__
                elif getattr(self.xp, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.xp = self.xp.to_version(self.__version__)
            if self.xq is not None:
                if getattr(self.xq, '__version__', None) is None:
                    self.xq.__version__ = self.__version__
                elif getattr(self.xq, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.xq = self.xq.to_version(self.__version__)
            if self.xr is not None:
                if getattr(self.xr, '__version__', None) is None:
                    self.xr.__version__ = self.__version__
                elif getattr(self.xr, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.xr = self.xr.to_version(self.__version__)
            if self.xx is not None:
                if getattr(self.xx, '__version__', None) is None:
                    self.xx.__version__ = self.__version__
                elif getattr(self.xx, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.xx = self.xx.to_version(self.__version__)
            if self.xy is not None:
                if getattr(self.xy, '__version__', None) is None:
                    self.xy.__version__ = self.__version__
                elif getattr(self.xy, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.xy = self.xy.to_version(self.__version__)
            if self.xz is not None:
                if getattr(self.xz, '__version__', None) is None:
                    self.xz.__version__ = self.__version__
                elif getattr(self.xz, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.xz = self.xz.to_version(self.__version__)
            if self.yp is not None:
                if getattr(self.yp, '__version__', None) is None:
                    self.yp.__version__ = self.__version__
                elif getattr(self.yp, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.yp = self.yp.to_version(self.__version__)
            if self.yq is not None:
                if getattr(self.yq, '__version__', None) is None:
                    self.yq.__version__ = self.__version__
                elif getattr(self.yq, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.yq = self.yq.to_version(self.__version__)
            if self.yr is not None:
                if getattr(self.yr, '__version__', None) is None:
                    self.yr.__version__ = self.__version__
                elif getattr(self.yr, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.yr = self.yr.to_version(self.__version__)
            if self.yy is not None:
                if getattr(self.yy, '__version__', None) is None:
                    self.yy.__version__ = self.__version__
                elif getattr(self.yy, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.yy = self.yy.to_version(self.__version__)
            if self.yz is not None:
                if getattr(self.yz, '__version__', None) is None:
                    self.yz.__version__ = self.__version__
                elif getattr(self.yz, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.yz = self.yz.to_version(self.__version__)
            if self.zp is not None:
                if getattr(self.zp, '__version__', None) is None:
                    self.zp.__version__ = self.__version__
                elif getattr(self.zp, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.zp = self.zp.to_version(self.__version__)
            if self.zq is not None:
                if getattr(self.zq, '__version__', None) is None:
                    self.zq.__version__ = self.__version__
                elif getattr(self.zq, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.zq = self.zq.to_version(self.__version__)
            if self.zr is not None:
                if getattr(self.zr, '__version__', None) is None:
                    self.zr.__version__ = self.__version__
                elif getattr(self.zr, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.zr = self.zr.to_version(self.__version__)
            if self.zz is not None:
                if getattr(self.zz, '__version__', None) is None:
                    self.zz.__version__ = self.__version__
                elif getattr(self.zz, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.zz = self.zz.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Inertial.FluidAddedMass":
            kwargs = {"sdf_version": target_version}
            kwargs["pp"] = self.pp.to_version(target_version) if self.pp is not None else None
            kwargs["pq"] = self.pq.to_version(target_version) if self.pq is not None else None
            kwargs["pr"] = self.pr.to_version(target_version) if self.pr is not None else None
            kwargs["qq"] = self.qq.to_version(target_version) if self.qq is not None else None
            kwargs["qr"] = self.qr.to_version(target_version) if self.qr is not None else None
            kwargs["rr"] = self.rr.to_version(target_version) if self.rr is not None else None
            kwargs["xp"] = self.xp.to_version(target_version) if self.xp is not None else None
            kwargs["xq"] = self.xq.to_version(target_version) if self.xq is not None else None
            kwargs["xr"] = self.xr.to_version(target_version) if self.xr is not None else None
            kwargs["xx"] = self.xx.to_version(target_version) if self.xx is not None else None
            kwargs["xy"] = self.xy.to_version(target_version) if self.xy is not None else None
            kwargs["xz"] = self.xz.to_version(target_version) if self.xz is not None else None
            kwargs["yp"] = self.yp.to_version(target_version) if self.yp is not None else None
            kwargs["yq"] = self.yq.to_version(target_version) if self.yq is not None else None
            kwargs["yr"] = self.yr.to_version(target_version) if self.yr is not None else None
            kwargs["yy"] = self.yy.to_version(target_version) if self.yy is not None else None
            kwargs["yz"] = self.yz.to_version(target_version) if self.yz is not None else None
            kwargs["zp"] = self.zp.to_version(target_version) if self.zp is not None else None
            kwargs["zq"] = self.zq.to_version(target_version) if self.zq is not None else None
            kwargs["zr"] = self.zr.to_version(target_version) if self.zr is not None else None
            kwargs["zz"] = self.zz.to_version(target_version) if self.zz is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("fluid_added_mass")
            if self.pp is not None:
                el.append(self.pp.to_sdf(version))
            if self.pq is not None:
                el.append(self.pq.to_sdf(version))
            if self.pr is not None:
                el.append(self.pr.to_sdf(version))
            if self.qq is not None:
                el.append(self.qq.to_sdf(version))
            if self.qr is not None:
                el.append(self.qr.to_sdf(version))
            if self.rr is not None:
                el.append(self.rr.to_sdf(version))
            if self.xp is not None:
                el.append(self.xp.to_sdf(version))
            if self.xq is not None:
                el.append(self.xq.to_sdf(version))
            if self.xr is not None:
                el.append(self.xr.to_sdf(version))
            if self.xx is not None:
                el.append(self.xx.to_sdf(version))
            if self.xy is not None:
                el.append(self.xy.to_sdf(version))
            if self.xz is not None:
                el.append(self.xz.to_sdf(version))
            if self.yp is not None:
                el.append(self.yp.to_sdf(version))
            if self.yq is not None:
                el.append(self.yq.to_sdf(version))
            if self.yr is not None:
                el.append(self.yr.to_sdf(version))
            if self.yy is not None:
                el.append(self.yy.to_sdf(version))
            if self.yz is not None:
                el.append(self.yz.to_sdf(version))
            if self.zp is not None:
                el.append(self.zp.to_sdf(version))
            if self.zq is not None:
                el.append(self.zq.to_sdf(version))
            if self.zr is not None:
                el.append(self.zr.to_sdf(version))
            if self.zz is not None:
                el.append(self.zz.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass | SDFError":
            _c_pp = el.find("pp")
            if _c_pp is not None:
                _res = cls.Pp._from_sdf(_c_pp, version)
                if isinstance(_res, SDFError):
                    return _res.extend("pp")
                _pp = _res
            else:
                _pp = None
            _c_pq = el.find("pq")
            if _c_pq is not None:
                _res = cls.Pq._from_sdf(_c_pq, version)
                if isinstance(_res, SDFError):
                    return _res.extend("pq")
                _pq = _res
            else:
                _pq = None
            _c_pr = el.find("pr")
            if _c_pr is not None:
                _res = cls.Pr._from_sdf(_c_pr, version)
                if isinstance(_res, SDFError):
                    return _res.extend("pr")
                _pr = _res
            else:
                _pr = None
            _c_qq = el.find("qq")
            if _c_qq is not None:
                _res = cls.Qq._from_sdf(_c_qq, version)
                if isinstance(_res, SDFError):
                    return _res.extend("qq")
                _qq = _res
            else:
                _qq = None
            _c_qr = el.find("qr")
            if _c_qr is not None:
                _res = cls.Qr._from_sdf(_c_qr, version)
                if isinstance(_res, SDFError):
                    return _res.extend("qr")
                _qr = _res
            else:
                _qr = None
            _c_rr = el.find("rr")
            if _c_rr is not None:
                _res = cls.Rr._from_sdf(_c_rr, version)
                if isinstance(_res, SDFError):
                    return _res.extend("rr")
                _rr = _res
            else:
                _rr = None
            _c_xp = el.find("xp")
            if _c_xp is not None:
                _res = cls.Xp._from_sdf(_c_xp, version)
                if isinstance(_res, SDFError):
                    return _res.extend("xp")
                _xp = _res
            else:
                _xp = None
            _c_xq = el.find("xq")
            if _c_xq is not None:
                _res = cls.Xq._from_sdf(_c_xq, version)
                if isinstance(_res, SDFError):
                    return _res.extend("xq")
                _xq = _res
            else:
                _xq = None
            _c_xr = el.find("xr")
            if _c_xr is not None:
                _res = cls.Xr._from_sdf(_c_xr, version)
                if isinstance(_res, SDFError):
                    return _res.extend("xr")
                _xr = _res
            else:
                _xr = None
            _c_xx = el.find("xx")
            if _c_xx is not None:
                _res = cls.Xx._from_sdf(_c_xx, version)
                if isinstance(_res, SDFError):
                    return _res.extend("xx")
                _xx = _res
            else:
                _xx = None
            _c_xy = el.find("xy")
            if _c_xy is not None:
                _res = cls.Xy._from_sdf(_c_xy, version)
                if isinstance(_res, SDFError):
                    return _res.extend("xy")
                _xy = _res
            else:
                _xy = None
            _c_xz = el.find("xz")
            if _c_xz is not None:
                _res = cls.Xz._from_sdf(_c_xz, version)
                if isinstance(_res, SDFError):
                    return _res.extend("xz")
                _xz = _res
            else:
                _xz = None
            _c_yp = el.find("yp")
            if _c_yp is not None:
                _res = cls.Yp._from_sdf(_c_yp, version)
                if isinstance(_res, SDFError):
                    return _res.extend("yp")
                _yp = _res
            else:
                _yp = None
            _c_yq = el.find("yq")
            if _c_yq is not None:
                _res = cls.Yq._from_sdf(_c_yq, version)
                if isinstance(_res, SDFError):
                    return _res.extend("yq")
                _yq = _res
            else:
                _yq = None
            _c_yr = el.find("yr")
            if _c_yr is not None:
                _res = cls.Yr._from_sdf(_c_yr, version)
                if isinstance(_res, SDFError):
                    return _res.extend("yr")
                _yr = _res
            else:
                _yr = None
            _c_yy = el.find("yy")
            if _c_yy is not None:
                _res = cls.Yy._from_sdf(_c_yy, version)
                if isinstance(_res, SDFError):
                    return _res.extend("yy")
                _yy = _res
            else:
                _yy = None
            _c_yz = el.find("yz")
            if _c_yz is not None:
                _res = cls.Yz._from_sdf(_c_yz, version)
                if isinstance(_res, SDFError):
                    return _res.extend("yz")
                _yz = _res
            else:
                _yz = None
            _c_zp = el.find("zp")
            if _c_zp is not None:
                _res = cls.Zp._from_sdf(_c_zp, version)
                if isinstance(_res, SDFError):
                    return _res.extend("zp")
                _zp = _res
            else:
                _zp = None
            _c_zq = el.find("zq")
            if _c_zq is not None:
                _res = cls.Zq._from_sdf(_c_zq, version)
                if isinstance(_res, SDFError):
                    return _res.extend("zq")
                _zq = _res
            else:
                _zq = None
            _c_zr = el.find("zr")
            if _c_zr is not None:
                _res = cls.Zr._from_sdf(_c_zr, version)
                if isinstance(_res, SDFError):
                    return _res.extend("zr")
                _zr = _res
            else:
                _zr = None
            _c_zz = el.find("zz")
            if _c_zz is not None:
                _res = cls.Zz._from_sdf(_c_zz, version)
                if isinstance(_res, SDFError):
                    return _res.extend("zz")
                _zz = _res
            else:
                _zz = None
            return cls(sdf_version=version, pp=_pp, pq=_pq, pr=_pr, qq=_qq, qr=_qr, rr=_rr, xp=_xp, xq=_xq, xr=_xr, xx=_xx, xy=_xy, xz=_xz, yp=_yp, yq=_yq, yr=_yr, yy=_yy, yz=_yz, zp=_zp, zq=_zq, zr=_zr, zz=_zz)

    class Inertia(BaseModel):
        class Ixx(BaseModel):
            def __init__(self, sdf_version: str | None = None, ixx: float = 1.0):
                super().__init__(sdf_version)
                self.ixx = ixx

            def to_version(self, target_version: str) -> "Inertial.Inertia.Ixx":
                if self.ixx is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'ixx' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["ixx"] = self.ixx
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("ixx")
                if self.ixx is not None:
                    el.text = str(self.ixx)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Inertia.Ixx | SDFError":
                _text = el.text or 1.0
                _ixx = _parse_double(_text)
                if isinstance(_ixx, SDFError):
                    return _ixx
                if _ixx is not None and cmp_version(version, "1.2") < 0:
                    if _ixx != 1.0:
                        return SDFError(f"'ixx' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, ixx=_ixx)

        class Ixy(BaseModel):
            def __init__(self, sdf_version: str | None = None, ixy: float = 0.0):
                super().__init__(sdf_version)
                self.ixy = ixy

            def to_version(self, target_version: str) -> "Inertial.Inertia.Ixy":
                if self.ixy is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'ixy' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["ixy"] = self.ixy
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("ixy")
                if self.ixy is not None:
                    el.text = str(self.ixy)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Inertia.Ixy | SDFError":
                _text = el.text or 0.0
                _ixy = _parse_double(_text)
                if isinstance(_ixy, SDFError):
                    return _ixy
                if _ixy is not None and cmp_version(version, "1.2") < 0:
                    if _ixy != 0.0:
                        return SDFError(f"'ixy' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, ixy=_ixy)

        class Ixz(BaseModel):
            def __init__(self, sdf_version: str | None = None, ixz: float = 0.0):
                super().__init__(sdf_version)
                self.ixz = ixz

            def to_version(self, target_version: str) -> "Inertial.Inertia.Ixz":
                if self.ixz is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'ixz' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["ixz"] = self.ixz
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("ixz")
                if self.ixz is not None:
                    el.text = str(self.ixz)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Inertia.Ixz | SDFError":
                _text = el.text or 0.0
                _ixz = _parse_double(_text)
                if isinstance(_ixz, SDFError):
                    return _ixz
                if _ixz is not None and cmp_version(version, "1.2") < 0:
                    if _ixz != 0.0:
                        return SDFError(f"'ixz' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, ixz=_ixz)

        class Iyy(BaseModel):
            def __init__(self, sdf_version: str | None = None, iyy: float = 1.0):
                super().__init__(sdf_version)
                self.iyy = iyy

            def to_version(self, target_version: str) -> "Inertial.Inertia.Iyy":
                if self.iyy is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'iyy' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["iyy"] = self.iyy
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("iyy")
                if self.iyy is not None:
                    el.text = str(self.iyy)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Inertia.Iyy | SDFError":
                _text = el.text or 1.0
                _iyy = _parse_double(_text)
                if isinstance(_iyy, SDFError):
                    return _iyy
                if _iyy is not None and cmp_version(version, "1.2") < 0:
                    if _iyy != 1.0:
                        return SDFError(f"'iyy' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, iyy=_iyy)

        class Iyz(BaseModel):
            def __init__(self, sdf_version: str | None = None, iyz: float = 0.0):
                super().__init__(sdf_version)
                self.iyz = iyz

            def to_version(self, target_version: str) -> "Inertial.Inertia.Iyz":
                if self.iyz is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'iyz' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["iyz"] = self.iyz
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("iyz")
                if self.iyz is not None:
                    el.text = str(self.iyz)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Inertia.Iyz | SDFError":
                _text = el.text or 0.0
                _iyz = _parse_double(_text)
                if isinstance(_iyz, SDFError):
                    return _iyz
                if _iyz is not None and cmp_version(version, "1.2") < 0:
                    if _iyz != 0.0:
                        return SDFError(f"'iyz' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, iyz=_iyz)

        class Izz(BaseModel):
            def __init__(self, sdf_version: str | None = None, izz: float = 1.0):
                super().__init__(sdf_version)
                self.izz = izz

            def to_version(self, target_version: str) -> "Inertial.Inertia.Izz":
                if self.izz is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'izz' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["izz"] = self.izz
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("izz")
                if self.izz is not None:
                    el.text = str(self.izz)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Inertia.Izz | SDFError":
                _text = el.text or 1.0
                _izz = _parse_double(_text)
                if isinstance(_izz, SDFError):
                    return _izz
                if _izz is not None and cmp_version(version, "1.2") < 0:
                    if _izz != 1.0:
                        return SDFError(f"'izz' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, izz=_izz)

        def __init__(
            self,
            sdf_version: str | None = None,
            ixx: float = 0.0,
            ixy: float = 0.0,
            ixz: float = 0.0,
            iyy: float = 0.0,
            iyz: float = 0.0,
            izz: float = 0.0
        ):
            super().__init__(sdf_version)
            self.ixx = ixx
            self.ixy = ixy
            self.ixz = ixz
            self.iyy = iyy
            self.iyz = iyz
            self.izz = izz

        def to_version(self, target_version: str) -> "Inertial.Inertia":
            if self.ixx is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'ixx' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.ixy is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'ixy' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.ixz is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'ixz' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.iyy is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'iyy' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.iyz is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'iyz' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.izz is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'izz' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["ixx"] = self.ixx
            kwargs["ixy"] = self.ixy
            kwargs["ixz"] = self.ixz
            kwargs["iyy"] = self.iyy
            kwargs["iyz"] = self.iyz
            kwargs["izz"] = self.izz
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("inertia")
            if self.ixx is not None:
                el.set("ixx", str(self.ixx))
            if self.ixy is not None:
                el.set("ixy", str(self.ixy))
            if self.ixz is not None:
                el.set("ixz", str(self.ixz))
            if self.iyy is not None:
                el.set("iyy", str(self.iyy))
            if self.iyz is not None:
                el.set("iyz", str(self.iyz))
            if self.izz is not None:
                el.set("izz", str(self.izz))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Inertia | SDFError":
            _ixx = _parse_double(el.get("ixx", 0.0))
            if isinstance(_ixx, SDFError):
                return _ixx.extend("@ixx")
            _ixy = _parse_double(el.get("ixy", 0.0))
            if isinstance(_ixy, SDFError):
                return _ixy.extend("@ixy")
            _ixz = _parse_double(el.get("ixz", 0.0))
            if isinstance(_ixz, SDFError):
                return _ixz.extend("@ixz")
            _iyy = _parse_double(el.get("iyy", 0.0))
            if isinstance(_iyy, SDFError):
                return _iyy.extend("@iyy")
            _iyz = _parse_double(el.get("iyz", 0.0))
            if isinstance(_iyz, SDFError):
                return _iyz.extend("@iyz")
            _izz = _parse_double(el.get("izz", 0.0))
            if isinstance(_izz, SDFError):
                return _izz.extend("@izz")
            return cls(sdf_version=version, ixx=_ixx, ixy=_ixy, ixz=_ixz, iyy=_iyy, iyz=_iyz, izz=_izz)

    class Mass(BaseModel):
        def __init__(self, sdf_version: str | None = None, mass: float = 1.0):
            super().__init__(sdf_version)
            self.mass = mass

        def to_version(self, target_version: str) -> "Inertial.Mass":
            if self.mass is not None and cmp_version(target_version, "1.2") < 0:
                raise ValueError(f"'mass' is not supported in SDF version {target_version} (added in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["mass"] = self.mass
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("mass")
            if self.mass is not None:
                el.text = str(self.mass)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Mass | SDFError":
            _text = el.text or 1.0
            _mass = _parse_double(_text)
            if isinstance(_mass, SDFError):
                return _mass
            if _mass is not None and cmp_version(version, "1.2") < 0:
                if _mass != 1.0:
                    return SDFError(f"'mass' is not supported in SDF version {version} (added in 1.2)")
            return cls(sdf_version=version, mass=_mass)

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _SDFPose = None):
            super().__init__(sdf_version)
            if pose is None:
                pose = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
            self.pose = pose

        def to_version(self, target_version: str) -> "Inertial.Origin":
            kwargs = {"sdf_version": target_version}
            kwargs["pose"] = self.pose
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("origin")
            if self.pose is not None:
                el.set("pose", self.pose.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Origin | SDFError":
            _pose = _SDFPose._from_sdf(el.get("pose", "0 0 0 0 0 0"), version)
            if isinstance(_pose, SDFError):
                return _pose.extend("@pose")
            return cls(sdf_version=version, pose=_pose)

    def __init__(
        self,
        sdf_version: str | None = None,
        auto: bool = False,
        auto_inertia_params: "Inertial.AutoInertiaParams" = None,
        density: float = 1.0,
        fluid_added_mass: "Inertial.FluidAddedMass" = None,
        frames: List["Frame"] = None,
        inertia: "Inertial.Inertia" = None,
        mass: float = 1.0,
        origin: "Inertial.Origin" = None,
        pose: "Pose" = None
    ):
        super().__init__(sdf_version)
        self.auto = auto
        self.auto_inertia_params = auto_inertia_params
        self.density = density
        self.fluid_added_mass = fluid_added_mass
        self.frames = frames or []
        self.inertia = inertia
        self.mass = mass
        self.origin = origin
        self.pose = pose
        if self.auto_inertia_params is not None:
            if getattr(self.auto_inertia_params, '__version__', None) is None:
                self.auto_inertia_params.__version__ = self.__version__
            elif getattr(self.auto_inertia_params, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.auto_inertia_params = self.auto_inertia_params.to_version(self.__version__)
        if self.fluid_added_mass is not None:
            if getattr(self.fluid_added_mass, '__version__', None) is None:
                self.fluid_added_mass.__version__ = self.__version__
            elif getattr(self.fluid_added_mass, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.fluid_added_mass = self.fluid_added_mass.to_version(self.__version__)
        for _i, _c in enumerate(self.frames):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        if self.inertia is not None:
            if getattr(self.inertia, '__version__', None) is None:
                self.inertia.__version__ = self.__version__
            elif getattr(self.inertia, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.inertia = self.inertia.to_version(self.__version__)
        if self.origin is not None:
            if getattr(self.origin, '__version__', None) is None:
                self.origin.__version__ = self.__version__
            elif getattr(self.origin, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.origin = self.origin.to_version(self.__version__)
        if self.pose is not None:
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Inertial":
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.auto is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'auto' is not supported in SDF version {target_version} (added in 1.11)")
        if self.auto_inertia_params is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'auto_inertia_params' is not supported in SDF version {target_version} (added in 1.11)")
        if self.density is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.fluid_added_mass is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'fluid_added_mass' is not supported in SDF version {target_version} (added in 1.10)")
        if self.frames is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.mass is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'mass' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["auto"] = self.auto
        kwargs["auto_inertia_params"] = self.auto_inertia_params.to_version(target_version) if self.auto_inertia_params is not None else None
        kwargs["density"] = self.density
        kwargs["fluid_added_mass"] = self.fluid_added_mass.to_version(target_version) if self.fluid_added_mass is not None else None
        kwargs["frames"] = [c.to_version(target_version) for c in (self.frames or [])]
        kwargs["inertia"] = self.inertia.to_version(target_version) if self.inertia is not None else None
        kwargs["mass"] = self.mass
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("inertial")
        if self.auto is not None:
            el.set("auto", str(self.auto).lower())
        if self.auto_inertia_params is not None:
            el.append(self.auto_inertia_params.to_sdf(version))
        if self.density is not None:
            el.set("density", str(self.density))
        if self.fluid_added_mass is not None:
            el.append(self.fluid_added_mass.to_sdf(version))
        for item in (self.frames or []):
            el.append(item.to_sdf(version))
        if self.inertia is not None:
            el.append(self.inertia.to_sdf(version))
        if self.mass is not None:
            el.set("mass", str(self.mass))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial | SDFError":
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        _auto = str(el.get("auto", False)).strip().lower() == 'true'
        if isinstance(_auto, SDFError):
            return _auto.extend("@auto")
        if _auto is not None and cmp_version(version, "1.11") < 0:
            if _auto != False:
                return SDFError(f"'auto' is not supported in SDF version {version} (added in 1.11)")
        _c_auto_inertia_params = el.find("auto_inertia_params")
        if _c_auto_inertia_params is not None:
            _res = cls.AutoInertiaParams._from_sdf(_c_auto_inertia_params, version)
            if isinstance(_res, SDFError):
                return _res.extend("auto_inertia_params")
            _auto_inertia_params = _res
        else:
            _auto_inertia_params = None
        if _auto_inertia_params is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'auto_inertia_params' is not supported in SDF version {version} (added in 1.11)")
        _density = _parse_double(el.get("density", 1.0))
        if isinstance(_density, SDFError):
            return _density.extend("@density")
        _c_fluid_added_mass = el.find("fluid_added_mass")
        if _c_fluid_added_mass is not None:
            _res = cls.FluidAddedMass._from_sdf(_c_fluid_added_mass, version)
            if isinstance(_res, SDFError):
                return _res.extend("fluid_added_mass")
            _fluid_added_mass = _res
        else:
            _fluid_added_mass = None
        if _fluid_added_mass is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'fluid_added_mass' is not supported in SDF version {version} (added in 1.10)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _c_inertia = el.find("inertia")
        if _c_inertia is not None:
            _res = cls.Inertia._from_sdf(_c_inertia, version)
            if isinstance(_res, SDFError):
                return _res.extend("inertia")
            _inertia = _res
        else:
            _inertia = None
        _mass = _parse_double(el.get("mass", 1.0))
        if isinstance(_mass, SDFError):
            return _mass.extend("@mass")
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = cls.Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, auto=_auto, auto_inertia_params=_auto_inertia_params, density=_density, fluid_added_mass=_fluid_added_mass, frames=_frames, inertia=_inertia, mass=_mass, origin=_origin, pose=_pose)
