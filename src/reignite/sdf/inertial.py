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



class AutoInertiaParams(BaseModel):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "AutoInertiaParams":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("auto_inertia_params")
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Density(BaseModel):
    def __init__(self, sdf_version: str, density: float = 1000.0):
        self.__version__ = sdf_version
        self.density = density

    def to_version(self, target_version: str) -> "Density":
        if self.density is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["density"] = self.density
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("density")
        if self.density is not None:
            el.text = str(self.density)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1000.0
        _density = _parse_double(_text)
        if isinstance(_density, SDFError):
            return _density
        if _density is not None and cmp_version(version, "1.11") < 0:
            if _density != 1000.0:
                return SDFError(f"'density' is not supported in SDF version {version} (added in 1.11)")
        return cls(sdf_version=version, density=_density)


class FluidAddedMass(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        pp: "Pp" = None,
        pq: "Pq" = None,
        pr: "Pr" = None,
        qq: "Qq" = None,
        qr: "Qr" = None,
        rr: "Rr" = None,
        xp: "Xp" = None,
        xq: "Xq" = None,
        xr: "Xr" = None,
        xx: "Xx" = None,
        xy: "Xy" = None,
        xz: "Xz" = None,
        yp: "Yp" = None,
        yq: "Yq" = None,
        yr: "Yr" = None,
        yy: "Yy" = None,
        yz: "Yz" = None,
        zp: "Zp" = None,
        zq: "Zq" = None,
        zr: "Zr" = None,
        zz: "Zz" = None
    ):
        self.__version__ = sdf_version
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

    def to_version(self, target_version: str) -> "FluidAddedMass":
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

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_pp = el.find("pp")
        if _c_pp is not None:
            _res = Pp._from_sdf(_c_pp, version)
            if isinstance(_res, SDFError):
                return _res.extend("pp")
            _pp = _res
        else:
            _pp = None
        _c_pq = el.find("pq")
        if _c_pq is not None:
            _res = Pq._from_sdf(_c_pq, version)
            if isinstance(_res, SDFError):
                return _res.extend("pq")
            _pq = _res
        else:
            _pq = None
        _c_pr = el.find("pr")
        if _c_pr is not None:
            _res = Pr._from_sdf(_c_pr, version)
            if isinstance(_res, SDFError):
                return _res.extend("pr")
            _pr = _res
        else:
            _pr = None
        _c_qq = el.find("qq")
        if _c_qq is not None:
            _res = Qq._from_sdf(_c_qq, version)
            if isinstance(_res, SDFError):
                return _res.extend("qq")
            _qq = _res
        else:
            _qq = None
        _c_qr = el.find("qr")
        if _c_qr is not None:
            _res = Qr._from_sdf(_c_qr, version)
            if isinstance(_res, SDFError):
                return _res.extend("qr")
            _qr = _res
        else:
            _qr = None
        _c_rr = el.find("rr")
        if _c_rr is not None:
            _res = Rr._from_sdf(_c_rr, version)
            if isinstance(_res, SDFError):
                return _res.extend("rr")
            _rr = _res
        else:
            _rr = None
        _c_xp = el.find("xp")
        if _c_xp is not None:
            _res = Xp._from_sdf(_c_xp, version)
            if isinstance(_res, SDFError):
                return _res.extend("xp")
            _xp = _res
        else:
            _xp = None
        _c_xq = el.find("xq")
        if _c_xq is not None:
            _res = Xq._from_sdf(_c_xq, version)
            if isinstance(_res, SDFError):
                return _res.extend("xq")
            _xq = _res
        else:
            _xq = None
        _c_xr = el.find("xr")
        if _c_xr is not None:
            _res = Xr._from_sdf(_c_xr, version)
            if isinstance(_res, SDFError):
                return _res.extend("xr")
            _xr = _res
        else:
            _xr = None
        _c_xx = el.find("xx")
        if _c_xx is not None:
            _res = Xx._from_sdf(_c_xx, version)
            if isinstance(_res, SDFError):
                return _res.extend("xx")
            _xx = _res
        else:
            _xx = None
        _c_xy = el.find("xy")
        if _c_xy is not None:
            _res = Xy._from_sdf(_c_xy, version)
            if isinstance(_res, SDFError):
                return _res.extend("xy")
            _xy = _res
        else:
            _xy = None
        _c_xz = el.find("xz")
        if _c_xz is not None:
            _res = Xz._from_sdf(_c_xz, version)
            if isinstance(_res, SDFError):
                return _res.extend("xz")
            _xz = _res
        else:
            _xz = None
        _c_yp = el.find("yp")
        if _c_yp is not None:
            _res = Yp._from_sdf(_c_yp, version)
            if isinstance(_res, SDFError):
                return _res.extend("yp")
            _yp = _res
        else:
            _yp = None
        _c_yq = el.find("yq")
        if _c_yq is not None:
            _res = Yq._from_sdf(_c_yq, version)
            if isinstance(_res, SDFError):
                return _res.extend("yq")
            _yq = _res
        else:
            _yq = None
        _c_yr = el.find("yr")
        if _c_yr is not None:
            _res = Yr._from_sdf(_c_yr, version)
            if isinstance(_res, SDFError):
                return _res.extend("yr")
            _yr = _res
        else:
            _yr = None
        _c_yy = el.find("yy")
        if _c_yy is not None:
            _res = Yy._from_sdf(_c_yy, version)
            if isinstance(_res, SDFError):
                return _res.extend("yy")
            _yy = _res
        else:
            _yy = None
        _c_yz = el.find("yz")
        if _c_yz is not None:
            _res = Yz._from_sdf(_c_yz, version)
            if isinstance(_res, SDFError):
                return _res.extend("yz")
            _yz = _res
        else:
            _yz = None
        _c_zp = el.find("zp")
        if _c_zp is not None:
            _res = Zp._from_sdf(_c_zp, version)
            if isinstance(_res, SDFError):
                return _res.extend("zp")
            _zp = _res
        else:
            _zp = None
        _c_zq = el.find("zq")
        if _c_zq is not None:
            _res = Zq._from_sdf(_c_zq, version)
            if isinstance(_res, SDFError):
                return _res.extend("zq")
            _zq = _res
        else:
            _zq = None
        _c_zr = el.find("zr")
        if _c_zr is not None:
            _res = Zr._from_sdf(_c_zr, version)
            if isinstance(_res, SDFError):
                return _res.extend("zr")
            _zr = _res
        else:
            _zr = None
        _c_zz = el.find("zz")
        if _c_zz is not None:
            _res = Zz._from_sdf(_c_zz, version)
            if isinstance(_res, SDFError):
                return _res.extend("zz")
            _zz = _res
        else:
            _zz = None
        return cls(sdf_version=version, pp=_pp, pq=_pq, pr=_pr, qq=_qq, qr=_qr, rr=_rr, xp=_xp, xq=_xq, xr=_xr, xx=_xx, xy=_xy, xz=_xz, yp=_yp, yq=_yq, yr=_yr, yy=_yy, yz=_yz, zp=_zp, zq=_zq, zr=_zr, zz=_zz)


class Inertia(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        ixx: float = 0.0,
        ixy: float = 0.0,
        ixz: float = 0.0,
        iyy: float = 0.0,
        iyz: float = 0.0,
        izz: float = 0.0
    ):
        self.__version__ = sdf_version
        self.ixx = ixx
        self.ixy = ixy
        self.ixz = ixz
        self.iyy = iyy
        self.iyz = iyz
        self.izz = izz

    def to_version(self, target_version: str) -> "Inertia":
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

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
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
    def _from_sdf(cls, el: ET.Element, version: str):
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


class Inertial(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        auto: bool = False,
        auto_inertia_params: "AutoInertiaParams" = None,
        density: float = 1.0,
        fluid_added_mass: "FluidAddedMass" = None,
        frame: List["Frame"] = None,
        inertia: "Inertia" = None,
        mass: float = 1.0,
        origin: "Origin" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.auto = auto
        self.auto_inertia_params = auto_inertia_params
        self.density = density
        self.fluid_added_mass = fluid_added_mass
        self.frame = frame or []
        self.inertia = inertia
        self.mass = mass
        self.origin = origin
        self.pose = pose

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
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
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
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["inertia"] = self.inertia.to_version(target_version) if self.inertia is not None else None
        kwargs["mass"] = self.mass
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inertial")
        if self.auto is not None:
            el.set("auto", str(self.auto).lower())
        if self.auto_inertia_params is not None:
            el.append(self.auto_inertia_params.to_sdf(version))
        if self.density is not None:
            el.set("density", str(self.density))
        if self.fluid_added_mass is not None:
            el.append(self.fluid_added_mass.to_sdf(version))
        for item in (self.frame or []):
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
    def _from_sdf(cls, el: ET.Element, version: str):
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
            _res = AutoInertiaParams._from_sdf(_c_auto_inertia_params, version)
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
            _res = FluidAddedMass._from_sdf(_c_fluid_added_mass, version)
            if isinstance(_res, SDFError):
                return _res.extend("fluid_added_mass")
            _fluid_added_mass = _res
        else:
            _fluid_added_mass = None
        if _fluid_added_mass is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'fluid_added_mass' is not supported in SDF version {version} (added in 1.10)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_inertia = el.find("inertia")
        if _c_inertia is not None:
            _res = Inertia._from_sdf(_c_inertia, version)
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
            _res = Origin._from_sdf(_c_origin, version)
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
        return cls(sdf_version=version, auto=_auto, auto_inertia_params=_auto_inertia_params, density=_density, fluid_added_mass=_fluid_added_mass, frame=_frame, inertia=_inertia, mass=_mass, origin=_origin, pose=_pose)


class Ixx(BaseModel):
    def __init__(self, sdf_version: str, ixx: float = 1.0):
        self.__version__ = sdf_version
        self.ixx = ixx

    def to_version(self, target_version: str) -> "Ixx":
        if self.ixx is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'ixx' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ixx"] = self.ixx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ixx")
        if self.ixx is not None:
            el.text = str(self.ixx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _ixx = _parse_double(_text)
        if isinstance(_ixx, SDFError):
            return _ixx
        if _ixx is not None and cmp_version(version, "1.2") < 0:
            if _ixx != 1.0:
                return SDFError(f"'ixx' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, ixx=_ixx)


class Ixy(BaseModel):
    def __init__(self, sdf_version: str, ixy: float = 0.0):
        self.__version__ = sdf_version
        self.ixy = ixy

    def to_version(self, target_version: str) -> "Ixy":
        if self.ixy is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'ixy' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ixy"] = self.ixy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ixy")
        if self.ixy is not None:
            el.text = str(self.ixy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _ixy = _parse_double(_text)
        if isinstance(_ixy, SDFError):
            return _ixy
        if _ixy is not None and cmp_version(version, "1.2") < 0:
            if _ixy != 0.0:
                return SDFError(f"'ixy' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, ixy=_ixy)


class Ixz(BaseModel):
    def __init__(self, sdf_version: str, ixz: float = 0.0):
        self.__version__ = sdf_version
        self.ixz = ixz

    def to_version(self, target_version: str) -> "Ixz":
        if self.ixz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'ixz' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ixz"] = self.ixz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ixz")
        if self.ixz is not None:
            el.text = str(self.ixz)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _ixz = _parse_double(_text)
        if isinstance(_ixz, SDFError):
            return _ixz
        if _ixz is not None and cmp_version(version, "1.2") < 0:
            if _ixz != 0.0:
                return SDFError(f"'ixz' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, ixz=_ixz)


class Iyy(BaseModel):
    def __init__(self, sdf_version: str, iyy: float = 1.0):
        self.__version__ = sdf_version
        self.iyy = iyy

    def to_version(self, target_version: str) -> "Iyy":
        if self.iyy is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'iyy' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["iyy"] = self.iyy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("iyy")
        if self.iyy is not None:
            el.text = str(self.iyy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _iyy = _parse_double(_text)
        if isinstance(_iyy, SDFError):
            return _iyy
        if _iyy is not None and cmp_version(version, "1.2") < 0:
            if _iyy != 1.0:
                return SDFError(f"'iyy' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, iyy=_iyy)


class Iyz(BaseModel):
    def __init__(self, sdf_version: str, iyz: float = 0.0):
        self.__version__ = sdf_version
        self.iyz = iyz

    def to_version(self, target_version: str) -> "Iyz":
        if self.iyz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'iyz' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["iyz"] = self.iyz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("iyz")
        if self.iyz is not None:
            el.text = str(self.iyz)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _iyz = _parse_double(_text)
        if isinstance(_iyz, SDFError):
            return _iyz
        if _iyz is not None and cmp_version(version, "1.2") < 0:
            if _iyz != 0.0:
                return SDFError(f"'iyz' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, iyz=_iyz)


class Izz(BaseModel):
    def __init__(self, sdf_version: str, izz: float = 1.0):
        self.__version__ = sdf_version
        self.izz = izz

    def to_version(self, target_version: str) -> "Izz":
        if self.izz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'izz' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["izz"] = self.izz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("izz")
        if self.izz is not None:
            el.text = str(self.izz)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _izz = _parse_double(_text)
        if isinstance(_izz, SDFError):
            return _izz
        if _izz is not None and cmp_version(version, "1.2") < 0:
            if _izz != 1.0:
                return SDFError(f"'izz' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, izz=_izz)


class Mass(BaseModel):
    def __init__(self, sdf_version: str, mass: float = 1.0):
        self.__version__ = sdf_version
        self.mass = mass

    def to_version(self, target_version: str) -> "Mass":
        if self.mass is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'mass' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mass"] = self.mass
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mass")
        if self.mass is not None:
            el.text = str(self.mass)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _mass = _parse_double(_text)
        if isinstance(_mass, SDFError):
            return _mass
        if _mass is not None and cmp_version(version, "1.2") < 0:
            if _mass != 1.0:
                return SDFError(f"'mass' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mass=_mass)


class Origin(BaseModel):
    def __init__(self, sdf_version: str, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "Origin":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("origin")
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _pose = _SDFPose._from_sdf(el.get("pose", "0 0 0 0 0 0"), version)
        if isinstance(_pose, SDFError):
            return _pose.extend("@pose")
        return cls(sdf_version=version, pose=_pose)


class Pp(BaseModel):
    def __init__(self, sdf_version: str, pp: float = 0.0):
        self.__version__ = sdf_version
        self.pp = pp

    def to_version(self, target_version: str) -> "Pp":
        kwargs = {"sdf_version": target_version}
        kwargs["pp"] = self.pp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pp")
        if self.pp is not None:
            el.text = str(self.pp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _pp = _parse_double(_text)
        if isinstance(_pp, SDFError):
            return _pp
        return cls(sdf_version=version, pp=_pp)


class Pq(BaseModel):
    def __init__(self, sdf_version: str, pq: float = 0.0):
        self.__version__ = sdf_version
        self.pq = pq

    def to_version(self, target_version: str) -> "Pq":
        kwargs = {"sdf_version": target_version}
        kwargs["pq"] = self.pq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pq")
        if self.pq is not None:
            el.text = str(self.pq)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _pq = _parse_double(_text)
        if isinstance(_pq, SDFError):
            return _pq
        return cls(sdf_version=version, pq=_pq)


class Pr(BaseModel):
    def __init__(self, sdf_version: str, pr: float = 0.0):
        self.__version__ = sdf_version
        self.pr = pr

    def to_version(self, target_version: str) -> "Pr":
        kwargs = {"sdf_version": target_version}
        kwargs["pr"] = self.pr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pr")
        if self.pr is not None:
            el.text = str(self.pr)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _pr = _parse_double(_text)
        if isinstance(_pr, SDFError):
            return _pr
        return cls(sdf_version=version, pr=_pr)


class Qq(BaseModel):
    def __init__(self, sdf_version: str, qq: float = 0.0):
        self.__version__ = sdf_version
        self.qq = qq

    def to_version(self, target_version: str) -> "Qq":
        kwargs = {"sdf_version": target_version}
        kwargs["qq"] = self.qq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("qq")
        if self.qq is not None:
            el.text = str(self.qq)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _qq = _parse_double(_text)
        if isinstance(_qq, SDFError):
            return _qq
        return cls(sdf_version=version, qq=_qq)


class Qr(BaseModel):
    def __init__(self, sdf_version: str, qr: float = 0.0):
        self.__version__ = sdf_version
        self.qr = qr

    def to_version(self, target_version: str) -> "Qr":
        kwargs = {"sdf_version": target_version}
        kwargs["qr"] = self.qr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("qr")
        if self.qr is not None:
            el.text = str(self.qr)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _qr = _parse_double(_text)
        if isinstance(_qr, SDFError):
            return _qr
        return cls(sdf_version=version, qr=_qr)


class Rr(BaseModel):
    def __init__(self, sdf_version: str, rr: float = 0.0):
        self.__version__ = sdf_version
        self.rr = rr

    def to_version(self, target_version: str) -> "Rr":
        kwargs = {"sdf_version": target_version}
        kwargs["rr"] = self.rr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rr")
        if self.rr is not None:
            el.text = str(self.rr)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _rr = _parse_double(_text)
        if isinstance(_rr, SDFError):
            return _rr
        return cls(sdf_version=version, rr=_rr)


class Xp(BaseModel):
    def __init__(self, sdf_version: str, xp: float = 0.0):
        self.__version__ = sdf_version
        self.xp = xp

    def to_version(self, target_version: str) -> "Xp":
        kwargs = {"sdf_version": target_version}
        kwargs["xp"] = self.xp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xp")
        if self.xp is not None:
            el.text = str(self.xp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _xp = _parse_double(_text)
        if isinstance(_xp, SDFError):
            return _xp
        return cls(sdf_version=version, xp=_xp)


class Xq(BaseModel):
    def __init__(self, sdf_version: str, xq: float = 0.0):
        self.__version__ = sdf_version
        self.xq = xq

    def to_version(self, target_version: str) -> "Xq":
        kwargs = {"sdf_version": target_version}
        kwargs["xq"] = self.xq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xq")
        if self.xq is not None:
            el.text = str(self.xq)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _xq = _parse_double(_text)
        if isinstance(_xq, SDFError):
            return _xq
        return cls(sdf_version=version, xq=_xq)


class Xr(BaseModel):
    def __init__(self, sdf_version: str, xr: float = 0.0):
        self.__version__ = sdf_version
        self.xr = xr

    def to_version(self, target_version: str) -> "Xr":
        kwargs = {"sdf_version": target_version}
        kwargs["xr"] = self.xr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xr")
        if self.xr is not None:
            el.text = str(self.xr)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _xr = _parse_double(_text)
        if isinstance(_xr, SDFError):
            return _xr
        return cls(sdf_version=version, xr=_xr)


class Xx(BaseModel):
    def __init__(self, sdf_version: str, xx: float = 0.0):
        self.__version__ = sdf_version
        self.xx = xx

    def to_version(self, target_version: str) -> "Xx":
        kwargs = {"sdf_version": target_version}
        kwargs["xx"] = self.xx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xx")
        if self.xx is not None:
            el.text = str(self.xx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _xx = _parse_double(_text)
        if isinstance(_xx, SDFError):
            return _xx
        return cls(sdf_version=version, xx=_xx)


class Xy(BaseModel):
    def __init__(self, sdf_version: str, xy: float = 0.0):
        self.__version__ = sdf_version
        self.xy = xy

    def to_version(self, target_version: str) -> "Xy":
        kwargs = {"sdf_version": target_version}
        kwargs["xy"] = self.xy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xy")
        if self.xy is not None:
            el.text = str(self.xy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _xy = _parse_double(_text)
        if isinstance(_xy, SDFError):
            return _xy
        return cls(sdf_version=version, xy=_xy)


class Xz(BaseModel):
    def __init__(self, sdf_version: str, xz: float = 0.0):
        self.__version__ = sdf_version
        self.xz = xz

    def to_version(self, target_version: str) -> "Xz":
        kwargs = {"sdf_version": target_version}
        kwargs["xz"] = self.xz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xz")
        if self.xz is not None:
            el.text = str(self.xz)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _xz = _parse_double(_text)
        if isinstance(_xz, SDFError):
            return _xz
        return cls(sdf_version=version, xz=_xz)


class Yp(BaseModel):
    def __init__(self, sdf_version: str, yp: float = 0.0):
        self.__version__ = sdf_version
        self.yp = yp

    def to_version(self, target_version: str) -> "Yp":
        kwargs = {"sdf_version": target_version}
        kwargs["yp"] = self.yp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yp")
        if self.yp is not None:
            el.text = str(self.yp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _yp = _parse_double(_text)
        if isinstance(_yp, SDFError):
            return _yp
        return cls(sdf_version=version, yp=_yp)


class Yq(BaseModel):
    def __init__(self, sdf_version: str, yq: float = 0.0):
        self.__version__ = sdf_version
        self.yq = yq

    def to_version(self, target_version: str) -> "Yq":
        kwargs = {"sdf_version": target_version}
        kwargs["yq"] = self.yq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yq")
        if self.yq is not None:
            el.text = str(self.yq)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _yq = _parse_double(_text)
        if isinstance(_yq, SDFError):
            return _yq
        return cls(sdf_version=version, yq=_yq)


class Yr(BaseModel):
    def __init__(self, sdf_version: str, yr: float = 0.0):
        self.__version__ = sdf_version
        self.yr = yr

    def to_version(self, target_version: str) -> "Yr":
        kwargs = {"sdf_version": target_version}
        kwargs["yr"] = self.yr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yr")
        if self.yr is not None:
            el.text = str(self.yr)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _yr = _parse_double(_text)
        if isinstance(_yr, SDFError):
            return _yr
        return cls(sdf_version=version, yr=_yr)


class Yy(BaseModel):
    def __init__(self, sdf_version: str, yy: float = 0.0):
        self.__version__ = sdf_version
        self.yy = yy

    def to_version(self, target_version: str) -> "Yy":
        kwargs = {"sdf_version": target_version}
        kwargs["yy"] = self.yy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yy")
        if self.yy is not None:
            el.text = str(self.yy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _yy = _parse_double(_text)
        if isinstance(_yy, SDFError):
            return _yy
        return cls(sdf_version=version, yy=_yy)


class Yz(BaseModel):
    def __init__(self, sdf_version: str, yz: float = 0.0):
        self.__version__ = sdf_version
        self.yz = yz

    def to_version(self, target_version: str) -> "Yz":
        kwargs = {"sdf_version": target_version}
        kwargs["yz"] = self.yz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yz")
        if self.yz is not None:
            el.text = str(self.yz)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _yz = _parse_double(_text)
        if isinstance(_yz, SDFError):
            return _yz
        return cls(sdf_version=version, yz=_yz)


class Zp(BaseModel):
    def __init__(self, sdf_version: str, zp: float = 0.0):
        self.__version__ = sdf_version
        self.zp = zp

    def to_version(self, target_version: str) -> "Zp":
        kwargs = {"sdf_version": target_version}
        kwargs["zp"] = self.zp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("zp")
        if self.zp is not None:
            el.text = str(self.zp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _zp = _parse_double(_text)
        if isinstance(_zp, SDFError):
            return _zp
        return cls(sdf_version=version, zp=_zp)


class Zq(BaseModel):
    def __init__(self, sdf_version: str, zq: float = 0.0):
        self.__version__ = sdf_version
        self.zq = zq

    def to_version(self, target_version: str) -> "Zq":
        kwargs = {"sdf_version": target_version}
        kwargs["zq"] = self.zq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("zq")
        if self.zq is not None:
            el.text = str(self.zq)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _zq = _parse_double(_text)
        if isinstance(_zq, SDFError):
            return _zq
        return cls(sdf_version=version, zq=_zq)


class Zr(BaseModel):
    def __init__(self, sdf_version: str, zr: float = 0.0):
        self.__version__ = sdf_version
        self.zr = zr

    def to_version(self, target_version: str) -> "Zr":
        kwargs = {"sdf_version": target_version}
        kwargs["zr"] = self.zr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("zr")
        if self.zr is not None:
            el.text = str(self.zr)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _zr = _parse_double(_text)
        if isinstance(_zr, SDFError):
            return _zr
        return cls(sdf_version=version, zr=_zr)


class Zz(BaseModel):
    def __init__(self, sdf_version: str, zz: float = 0.0):
        self.__version__ = sdf_version
        self.zz = zz

    def to_version(self, target_version: str) -> "Zz":
        kwargs = {"sdf_version": target_version}
        kwargs["zz"] = self.zz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("zz")
        if self.zz is not None:
            el.text = str(self.zz)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _zz = _parse_double(_text)
        if isinstance(_zz, SDFError):
            return _zz
        return cls(sdf_version=version, zz=_zz)
