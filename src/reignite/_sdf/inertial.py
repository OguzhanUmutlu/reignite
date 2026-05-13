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
    class FluidAddedMass(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            pp: float = 0.0,
            pq: float = 0.0,
            pr: float = 0.0,
            qq: float = 0.0,
            qr: float = 0.0,
            rr: float = 0.0,
            xp: float = 0.0,
            xq: float = 0.0,
            xr: float = 0.0,
            xx: float = 0.0,
            xy: float = 0.0,
            xz: float = 0.0,
            yp: float = 0.0,
            yq: float = 0.0,
            yr: float = 0.0,
            yy: float = 0.0,
            yz: float = 0.0,
            zp: float = 0.0,
            zq: float = 0.0,
            zr: float = 0.0,
            zz: float = 0.0
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

        def to_version(self, target_version: str) -> "Inertial.FluidAddedMass":
            kwargs = {"sdf_version": target_version}
            kwargs["pp"] = self.pp
            kwargs["pq"] = self.pq
            kwargs["pr"] = self.pr
            kwargs["qq"] = self.qq
            kwargs["qr"] = self.qr
            kwargs["rr"] = self.rr
            kwargs["xp"] = self.xp
            kwargs["xq"] = self.xq
            kwargs["xr"] = self.xr
            kwargs["xx"] = self.xx
            kwargs["xy"] = self.xy
            kwargs["xz"] = self.xz
            kwargs["yp"] = self.yp
            kwargs["yq"] = self.yq
            kwargs["yr"] = self.yr
            kwargs["yy"] = self.yy
            kwargs["yz"] = self.yz
            kwargs["zp"] = self.zp
            kwargs["zq"] = self.zq
            kwargs["zr"] = self.zr
            kwargs["zz"] = self.zz
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
                _c_tmp = ET.Element("pp")
                _c_tmp.text = str(self.pp)
                el.append(_c_tmp)
            if self.pq is not None:
                _c_tmp = ET.Element("pq")
                _c_tmp.text = str(self.pq)
                el.append(_c_tmp)
            if self.pr is not None:
                _c_tmp = ET.Element("pr")
                _c_tmp.text = str(self.pr)
                el.append(_c_tmp)
            if self.qq is not None:
                _c_tmp = ET.Element("qq")
                _c_tmp.text = str(self.qq)
                el.append(_c_tmp)
            if self.qr is not None:
                _c_tmp = ET.Element("qr")
                _c_tmp.text = str(self.qr)
                el.append(_c_tmp)
            if self.rr is not None:
                _c_tmp = ET.Element("rr")
                _c_tmp.text = str(self.rr)
                el.append(_c_tmp)
            if self.xp is not None:
                _c_tmp = ET.Element("xp")
                _c_tmp.text = str(self.xp)
                el.append(_c_tmp)
            if self.xq is not None:
                _c_tmp = ET.Element("xq")
                _c_tmp.text = str(self.xq)
                el.append(_c_tmp)
            if self.xr is not None:
                _c_tmp = ET.Element("xr")
                _c_tmp.text = str(self.xr)
                el.append(_c_tmp)
            if self.xx is not None:
                _c_tmp = ET.Element("xx")
                _c_tmp.text = str(self.xx)
                el.append(_c_tmp)
            if self.xy is not None:
                _c_tmp = ET.Element("xy")
                _c_tmp.text = str(self.xy)
                el.append(_c_tmp)
            if self.xz is not None:
                _c_tmp = ET.Element("xz")
                _c_tmp.text = str(self.xz)
                el.append(_c_tmp)
            if self.yp is not None:
                _c_tmp = ET.Element("yp")
                _c_tmp.text = str(self.yp)
                el.append(_c_tmp)
            if self.yq is not None:
                _c_tmp = ET.Element("yq")
                _c_tmp.text = str(self.yq)
                el.append(_c_tmp)
            if self.yr is not None:
                _c_tmp = ET.Element("yr")
                _c_tmp.text = str(self.yr)
                el.append(_c_tmp)
            if self.yy is not None:
                _c_tmp = ET.Element("yy")
                _c_tmp.text = str(self.yy)
                el.append(_c_tmp)
            if self.yz is not None:
                _c_tmp = ET.Element("yz")
                _c_tmp.text = str(self.yz)
                el.append(_c_tmp)
            if self.zp is not None:
                _c_tmp = ET.Element("zp")
                _c_tmp.text = str(self.zp)
                el.append(_c_tmp)
            if self.zq is not None:
                _c_tmp = ET.Element("zq")
                _c_tmp.text = str(self.zq)
                el.append(_c_tmp)
            if self.zr is not None:
                _c_tmp = ET.Element("zr")
                _c_tmp.text = str(self.zr)
                el.append(_c_tmp)
            if self.zz is not None:
                _c_tmp = ET.Element("zz")
                _c_tmp.text = str(self.zz)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.FluidAddedMass | SDFError":
            _c_tmp = el.find("pp")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("pp")
                _pp = _val
            else:
                _pp = None
            _c_tmp = el.find("pq")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("pq")
                _pq = _val
            else:
                _pq = None
            _c_tmp = el.find("pr")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("pr")
                _pr = _val
            else:
                _pr = None
            _c_tmp = el.find("qq")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("qq")
                _qq = _val
            else:
                _qq = None
            _c_tmp = el.find("qr")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("qr")
                _qr = _val
            else:
                _qr = None
            _c_tmp = el.find("rr")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("rr")
                _rr = _val
            else:
                _rr = None
            _c_tmp = el.find("xp")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("xp")
                _xp = _val
            else:
                _xp = None
            _c_tmp = el.find("xq")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("xq")
                _xq = _val
            else:
                _xq = None
            _c_tmp = el.find("xr")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("xr")
                _xr = _val
            else:
                _xr = None
            _c_tmp = el.find("xx")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("xx")
                _xx = _val
            else:
                _xx = None
            _c_tmp = el.find("xy")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("xy")
                _xy = _val
            else:
                _xy = None
            _c_tmp = el.find("xz")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("xz")
                _xz = _val
            else:
                _xz = None
            _c_tmp = el.find("yp")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("yp")
                _yp = _val
            else:
                _yp = None
            _c_tmp = el.find("yq")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("yq")
                _yq = _val
            else:
                _yq = None
            _c_tmp = el.find("yr")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("yr")
                _yr = _val
            else:
                _yr = None
            _c_tmp = el.find("yy")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("yy")
                _yy = _val
            else:
                _yy = None
            _c_tmp = el.find("yz")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("yz")
                _yz = _val
            else:
                _yz = None
            _c_tmp = el.find("zp")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("zp")
                _zp = _val
            else:
                _zp = None
            _c_tmp = el.find("zq")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("zq")
                _zq = _val
            else:
                _zq = None
            _c_tmp = el.find("zr")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("zr")
                _zr = _val
            else:
                _zr = None
            _c_tmp = el.find("zz")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("zz")
                _zz = _val
            else:
                _zz = None
            return cls(sdf_version=version, pp=_pp, pq=_pq, pr=_pr, qq=_qq, qr=_qr, rr=_rr, xp=_xp, xq=_xq, xr=_xr, xx=_xx, xy=_xy, xz=_xz, yp=_yp, yq=_yq, yr=_yr, yy=_yy, yz=_yz, zp=_zp, zq=_zq, zr=_zr, zz=_zz)

    class Inertia(BaseModel):
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
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("pose")
                    _c_tmp.text = self.pose.to_sdf(version)
                    el.append(_c_tmp)
                else:
                    el.set("pose", self.pose.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is None: _raw_pose = "0 0 0 0 0 0"
            _pose = _SDFPose._from_sdf(_raw_pose, version)
            if isinstance(_pose, SDFError):
                return _pose.extend("@pose")
            return cls(sdf_version=version, pose=_pose)

    def __init__(
        self,
        sdf_version: str | None = None,
        auto: bool = False,
        auto_inertia_params: None = None,
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
        if self.fluid_added_mass is not None and hasattr(self.fluid_added_mass, 'to_version'):
            if getattr(self.fluid_added_mass, '__version__', None) is None:
                self.fluid_added_mass.__version__ = self.__version__
            elif getattr(self.fluid_added_mass, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.fluid_added_mass = self.fluid_added_mass.to_version(self.__version__)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        if self.inertia is not None and hasattr(self.inertia, 'to_version'):
            if getattr(self.inertia, '__version__', None) is None:
                self.inertia.__version__ = self.__version__
            elif getattr(self.inertia, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.inertia = self.inertia.to_version(self.__version__)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, '__version__', None) is None:
                self.origin.__version__ = self.__version__
            elif getattr(self.origin, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.origin = self.origin.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

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
        kwargs["auto_inertia_params"] = self.auto_inertia_params
        kwargs["density"] = self.density
        kwargs["fluid_added_mass"] = self.fluid_added_mass.to_version(target_version) if hasattr(self.fluid_added_mass, "to_version") else self.fluid_added_mass
        kwargs["frames"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])]
        kwargs["inertia"] = self.inertia.to_version(target_version) if hasattr(self.inertia, "to_version") else self.inertia
        kwargs["mass"] = self.mass
        kwargs["origin"] = self.origin.to_version(target_version) if hasattr(self.origin, "to_version") else self.origin
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
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
            _c_tmp = ET.Element("auto_inertia_params")
            _c_tmp.text = str(self.auto_inertia_params)
            el.append(_c_tmp)
        if self.density is not None:
            el.set("density", str(self.density))
        if self.fluid_added_mass is not None:
            if hasattr(self.fluid_added_mass, 'to_sdf'):
                _child_res = self.fluid_added_mass.to_sdf(version)
            else:
                _child_res = str(self.fluid_added_mass)
            if isinstance(_child_res, str):
                _item_el = ET.Element('fluid_added_mass')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.frames or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.inertia is not None:
            if hasattr(self.inertia, 'to_sdf'):
                _child_res = self.inertia.to_sdf(version)
            else:
                _child_res = str(self.inertia)
            if isinstance(_child_res, str):
                _item_el = ET.Element('inertia')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.mass is not None:
            el.set("mass", str(self.mass))
        if self.origin is not None:
            if hasattr(self.origin, 'to_sdf'):
                _child_res = self.origin.to_sdf(version)
            else:
                _child_res = str(self.origin)
            if isinstance(_child_res, str):
                _item_el = ET.Element('origin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            if hasattr(self.pose, 'to_sdf'):
                _child_res = self.pose.to_sdf(version)
            else:
                _child_res = str(self.pose)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
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
        _c_tmp = el.find("auto_inertia_params")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else None
            _val = str(_text)
            if isinstance(_val, SDFError):
                return _val.extend("auto_inertia_params")
            _auto_inertia_params = _val
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
