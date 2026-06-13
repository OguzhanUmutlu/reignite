### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame

def _parse_pose(raw: str, el: ET.Element | None = None) -> _PoseT | SDFError:
    try:
        is_degrees = el is not None and str(el.get('degrees')).lower() == 'true'
        return _pose(raw, degrees=is_degrees)
    except ValueError as e:
        return SDFError(str(e))

def _pose_to_sdf(val: _PoseT, el: ET.Element | None = None) -> str:
    if el is not None:
        el.set('degrees', 'true')
    if isinstance(val, _Pose):
        return f'{val.x} {val.y} {val.z} {val.roll_deg} {val.pitch_deg} {val.yaw_deg}'
    p = _pose(val)
    return f'{p.x} {p.y} {p.z} {p.roll_deg} {p.pitch_deg} {p.yaw_deg}'


# noinspection PyUnusedImports
class Inertial(BaseModel):
    class FluidAddedMass(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            pp: float | None = None,
            pq: float | None = None,
            pr: float | None = None,
            qq: float | None = None,
            qr: float | None = None,
            rr: float | None = None,
            xp: float | None = None,
            xq: float | None = None,
            xr: float | None = None,
            xx: float | None = None,
            xy: float | None = None,
            xz: float | None = None,
            yp: float | None = None,
            yq: float | None = None,
            yr: float | None = None,
            yy: float | None = None,
            yz: float | None = None,
            zp: float | None = None,
            zq: float | None = None,
            zr: float | None = None,
            zz: float | None = None
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
            kwargs: dict = {"sdf_version": target_version, "pp": self.pp, "pq": self.pq, "pr": self.pr, "qq": self.qq, "qr": self.qr, "rr": self.rr, "xp": self.xp, "xq": self.xq, "xr": self.xr, "xx": self.xx, "xy": self.xy, "xz": self.xz, "yp": self.yp, "yq": self.yq, "yr": self.yr, "yy": self.yy, "yz": self.yz, "zp": self.zp, "zq": self.zq, "zr": self.zr, "zz": self.zz}
            return Inertial.FluidAddedMass(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
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
            ixx: float | None = None,
            ixy: float | None = None,
            ixz: float | None = None,
            iyy: float | None = None,
            iyz: float | None = None,
            izz: float | None = None
        ):
            super().__init__(sdf_version)
            self.ixx = ixx
            self.ixy = ixy
            self.ixz = ixz
            self.iyy = iyy
            self.iyz = iyz
            self.izz = izz

        def to_version(self, target_version: str) -> "Inertial.Inertia":
            kwargs: dict = {"sdf_version": target_version, "ixx": self.ixx, "ixy": self.ixy, "ixz": self.ixz, "iyy": self.iyy, "iyz": self.iyz, "izz": self.izz}
            return Inertial.Inertia(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("inertia")
            if self.ixx is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("ixx")
                    _c_tmp.text = str(self.ixx)
                    el.append(_c_tmp)
                else:
                    el.set("ixx", str(self.ixx))
            if self.ixy is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("ixy")
                    _c_tmp.text = str(self.ixy)
                    el.append(_c_tmp)
                else:
                    el.set("ixy", str(self.ixy))
            if self.ixz is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("ixz")
                    _c_tmp.text = str(self.ixz)
                    el.append(_c_tmp)
                else:
                    el.set("ixz", str(self.ixz))
            if self.iyy is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("iyy")
                    _c_tmp.text = str(self.iyy)
                    el.append(_c_tmp)
                else:
                    el.set("iyy", str(self.iyy))
            if self.iyz is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("iyz")
                    _c_tmp.text = str(self.iyz)
                    el.append(_c_tmp)
                else:
                    el.set("iyz", str(self.iyz))
            if self.izz is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("izz")
                    _c_tmp.text = str(self.izz)
                    el.append(_c_tmp)
                else:
                    el.set("izz", str(self.izz))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Inertia | SDFError":
            _raw_ixx = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("ixx")
                if _c_tmp is not None: _raw_ixx = _c_tmp.text
            else:
                _raw_ixx = el.get("ixx")
            if _raw_ixx is not None:
                _ixx = _parse_double(_raw_ixx)
                if isinstance(_ixx, SDFError):
                    return _ixx.extend("@ixx")
            else:
                _ixx = None
            _raw_ixy = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("ixy")
                if _c_tmp is not None: _raw_ixy = _c_tmp.text
            else:
                _raw_ixy = el.get("ixy")
            if _raw_ixy is not None:
                _ixy = _parse_double(_raw_ixy)
                if isinstance(_ixy, SDFError):
                    return _ixy.extend("@ixy")
            else:
                _ixy = None
            _raw_ixz = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("ixz")
                if _c_tmp is not None: _raw_ixz = _c_tmp.text
            else:
                _raw_ixz = el.get("ixz")
            if _raw_ixz is not None:
                _ixz = _parse_double(_raw_ixz)
                if isinstance(_ixz, SDFError):
                    return _ixz.extend("@ixz")
            else:
                _ixz = None
            _raw_iyy = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("iyy")
                if _c_tmp is not None: _raw_iyy = _c_tmp.text
            else:
                _raw_iyy = el.get("iyy")
            if _raw_iyy is not None:
                _iyy = _parse_double(_raw_iyy)
                if isinstance(_iyy, SDFError):
                    return _iyy.extend("@iyy")
            else:
                _iyy = None
            _raw_iyz = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("iyz")
                if _c_tmp is not None: _raw_iyz = _c_tmp.text
            else:
                _raw_iyz = el.get("iyz")
            if _raw_iyz is not None:
                _iyz = _parse_double(_raw_iyz)
                if isinstance(_iyz, SDFError):
                    return _iyz.extend("@iyz")
            else:
                _iyz = None
            _raw_izz = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("izz")
                if _c_tmp is not None: _raw_izz = _c_tmp.text
            else:
                _raw_izz = el.get("izz")
            if _raw_izz is not None:
                _izz = _parse_double(_raw_izz)
                if isinstance(_izz, SDFError):
                    return _izz.extend("@izz")
            else:
                _izz = None
            return cls(sdf_version=version, ixx=_ixx, ixy=_ixy, ixz=_ixz, iyy=_iyy, iyz=_iyz, izz=_izz)

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Inertial.Origin":
            kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
            return Inertial.Origin(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("origin")
            if self.pose is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("pose")
                    _c_tmp.text = _pose_to_sdf(self.pose, el)
                    el.append(_c_tmp)
                else:
                    el.set("pose", _pose_to_sdf(self.pose, el))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is not None:
                _pose = _parse_pose(_raw_pose, el)
                if isinstance(_pose, SDFError):
                    return _pose.extend("@pose")
            else:
                _pose = None
            return cls(sdf_version=version, pose=_pose)

    def __init__(
        self,
        sdf_version: str | None = None,
        auto: bool | None = None,
        auto_inertia_params: None | None = None,
        density: float | None = None,
        fluid_added_mass: "Inertial.FluidAddedMass" = None,
        frames: List["Frame"] = None,
        inertia: "Inertial.Inertia" = None,
        mass: float | None = None,
        origin: "Inertial.Origin" = None,
        pose: _PoseT | None = None
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
        self.pose = _pose(pose) if pose is not None else None
        if self.fluid_added_mass is not None and hasattr(self.fluid_added_mass, 'to_version'):
            if getattr(self.fluid_added_mass, 'sdfversion', None) is None:
                self.fluid_added_mass.sdfversion = self.sdfversion
            elif getattr(self.fluid_added_mass, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.fluid_added_mass = self.fluid_added_mass.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.inertia is not None and hasattr(self.inertia, 'to_version'):
            if getattr(self.inertia, 'sdfversion', None) is None:
                self.inertia.sdfversion = self.sdfversion
            elif getattr(self.inertia, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.inertia = self.inertia.to_version(self.sdfversion)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, 'sdfversion', None) is None:
                self.origin.sdfversion = self.sdfversion
            elif getattr(self.origin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.origin = self.origin.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def to_version(self, target_version: str) -> "Inertial":
        from ..elements.frame import Frame
        if self.auto is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'auto' is not supported in SDF version {target_version} (added in 1.11)")
        if self.auto_inertia_params is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'auto_inertia_params' is not supported in SDF version {target_version} (added in 1.11)")
        if self.fluid_added_mass is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'fluid_added_mass' is not supported in SDF version {target_version} (added in 1.10)")
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs: dict = {"sdf_version": target_version, "auto": self.auto, "auto_inertia_params": self.auto_inertia_params, "density": self.density, "fluid_added_mass": self.fluid_added_mass.to_version(target_version) if self.fluid_added_mass is not None and hasattr(self.fluid_added_mass, "to_version") else self.fluid_added_mass, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "inertia": self.inertia.to_version(target_version) if self.inertia is not None and hasattr(self.inertia, "to_version") else self.inertia, "mass": self.mass, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "pose": self.pose}
        return Inertial(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("inertial")
        if self.auto is not None:
            el.set("auto", str(self.auto).lower())
        if self.auto_inertia_params is not None:
            _c_tmp = ET.Element("auto_inertia_params")
            _c_tmp.text = str(self.auto_inertia_params)
            el.append(_c_tmp)
        if self.density is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("density")
                _c_tmp.text = str(self.density)
                el.append(_c_tmp)
            else:
                el.set("density", str(self.density))
        if self.fluid_added_mass is not None:
            _child_res = self.fluid_added_mass.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('fluid_added_mass')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.inertia is not None:
            _child_res = self.inertia.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('inertia')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.mass is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("mass")
                _c_tmp.text = str(self.mass)
                el.append(_c_tmp)
            else:
                el.set("mass", str(self.mass))
        if self.origin is not None:
            _child_res = self.origin.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('origin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = _pose_to_sdf(self.pose, _c_tmp)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Inertial | SDFError":
        from ..elements.frame import Frame
        _raw_auto = el.get("auto")
        if _raw_auto is not None:
            _auto = str(_raw_auto).strip().lower() == 'true'
            if isinstance(_auto, SDFError):
                return _auto.extend("@auto")
        else:
            _auto = None
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
        _raw_density = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("density")
            if _c_tmp is not None: _raw_density = _c_tmp.text
        else:
            _raw_density = el.get("density")
        if _raw_density is not None:
            _density = _parse_double(_raw_density)
            if isinstance(_density, SDFError):
                return _density.extend("@density")
        else:
            _density = None
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
        _raw_mass = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("mass")
            if _c_tmp is not None: _raw_mass = _c_tmp.text
        else:
            _raw_mass = el.get("mass")
        if _raw_mass is not None:
            _mass = _parse_double(_raw_mass)
            if isinstance(_mass, SDFError):
                return _mass.extend("@mass")
        else:
            _mass = None
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = cls.Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
        _c_tmp = el.find("pose")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text, _c_tmp)
            if isinstance(_val, SDFError):
                return _val.extend("pose")
            _pose = _val
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, auto=_auto, auto_inertia_params=_auto_inertia_params, density=_density, fluid_added_mass=_fluid_added_mass, frames=_frames, inertia=_inertia, mass=_mass, origin=_origin, pose=_pose)
