from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .xx import Xx
from .xy import Xy
from .xz import Xz
from .xp import Xp
from .xq import Xq
from .xr import Xr
from .yy import Yy
from .yz import Yz
from .yp import Yp
from .yq import Yq
from .yr import Yr
from .zz import Zz
from .zp import Zp
from .zq import Zq
from .zr import Zr
from .pp import Pp
from .pq import Pq
from .pr import Pr
from .qq import Qq
from .qr import Qr
from .rr import Rr


class FluidAddedMass(Model):
    def __init__(
        self,
        xx: "Xx" = None,
        xy: "Xy" = None,
        xz: "Xz" = None,
        xp: "Xp" = None,
        xq: "Xq" = None,
        xr: "Xr" = None,
        yy: "Yy" = None,
        yz: "Yz" = None,
        yp: "Yp" = None,
        yq: "Yq" = None,
        yr: "Yr" = None,
        zz: "Zz" = None,
        zp: "Zp" = None,
        zq: "Zq" = None,
        zr: "Zr" = None,
        pp: "Pp" = None,
        pq: "Pq" = None,
        pr: "Pr" = None,
        qq: "Qq" = None,
        qr: "Qr" = None,
        rr: "Rr" = None
    ):
        self.xx = xx
        self.xy = xy
        self.xz = xz
        self.xp = xp
        self.xq = xq
        self.xr = xr
        self.yy = yy
        self.yz = yz
        self.yp = yp
        self.yq = yq
        self.yr = yr
        self.zz = zz
        self.zp = zp
        self.zq = zq
        self.zr = zr
        self.pp = pp
        self.pq = pq
        self.pr = pr
        self.qq = qq
        self.qr = qr
        self.rr = rr

    def to_sdf(self) -> ET.Element:
        el = ET.Element("fluid_added_mass")
        if self.xx is not None:
            el.append(self.xx.to_sdf())
        if self.xy is not None:
            el.append(self.xy.to_sdf())
        if self.xz is not None:
            el.append(self.xz.to_sdf())
        if self.xp is not None:
            el.append(self.xp.to_sdf())
        if self.xq is not None:
            el.append(self.xq.to_sdf())
        if self.xr is not None:
            el.append(self.xr.to_sdf())
        if self.yy is not None:
            el.append(self.yy.to_sdf())
        if self.yz is not None:
            el.append(self.yz.to_sdf())
        if self.yp is not None:
            el.append(self.yp.to_sdf())
        if self.yq is not None:
            el.append(self.yq.to_sdf())
        if self.yr is not None:
            el.append(self.yr.to_sdf())
        if self.zz is not None:
            el.append(self.zz.to_sdf())
        if self.zp is not None:
            el.append(self.zp.to_sdf())
        if self.zq is not None:
            el.append(self.zq.to_sdf())
        if self.zr is not None:
            el.append(self.zr.to_sdf())
        if self.pp is not None:
            el.append(self.pp.to_sdf())
        if self.pq is not None:
            el.append(self.pq.to_sdf())
        if self.pr is not None:
            el.append(self.pr.to_sdf())
        if self.qq is not None:
            el.append(self.qq.to_sdf())
        if self.qr is not None:
            el.append(self.qr.to_sdf())
        if self.rr is not None:
            el.append(self.rr.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "FluidAddedMass":
        _c_xx = el.find("xx")
        _xx = Xx.from_sdf(_c_xx) if _c_xx is not None else None
        _c_xy = el.find("xy")
        _xy = Xy.from_sdf(_c_xy) if _c_xy is not None else None
        _c_xz = el.find("xz")
        _xz = Xz.from_sdf(_c_xz) if _c_xz is not None else None
        _c_xp = el.find("xp")
        _xp = Xp.from_sdf(_c_xp) if _c_xp is not None else None
        _c_xq = el.find("xq")
        _xq = Xq.from_sdf(_c_xq) if _c_xq is not None else None
        _c_xr = el.find("xr")
        _xr = Xr.from_sdf(_c_xr) if _c_xr is not None else None
        _c_yy = el.find("yy")
        _yy = Yy.from_sdf(_c_yy) if _c_yy is not None else None
        _c_yz = el.find("yz")
        _yz = Yz.from_sdf(_c_yz) if _c_yz is not None else None
        _c_yp = el.find("yp")
        _yp = Yp.from_sdf(_c_yp) if _c_yp is not None else None
        _c_yq = el.find("yq")
        _yq = Yq.from_sdf(_c_yq) if _c_yq is not None else None
        _c_yr = el.find("yr")
        _yr = Yr.from_sdf(_c_yr) if _c_yr is not None else None
        _c_zz = el.find("zz")
        _zz = Zz.from_sdf(_c_zz) if _c_zz is not None else None
        _c_zp = el.find("zp")
        _zp = Zp.from_sdf(_c_zp) if _c_zp is not None else None
        _c_zq = el.find("zq")
        _zq = Zq.from_sdf(_c_zq) if _c_zq is not None else None
        _c_zr = el.find("zr")
        _zr = Zr.from_sdf(_c_zr) if _c_zr is not None else None
        _c_pp = el.find("pp")
        _pp = Pp.from_sdf(_c_pp) if _c_pp is not None else None
        _c_pq = el.find("pq")
        _pq = Pq.from_sdf(_c_pq) if _c_pq is not None else None
        _c_pr = el.find("pr")
        _pr = Pr.from_sdf(_c_pr) if _c_pr is not None else None
        _c_qq = el.find("qq")
        _qq = Qq.from_sdf(_c_qq) if _c_qq is not None else None
        _c_qr = el.find("qr")
        _qr = Qr.from_sdf(_c_qr) if _c_qr is not None else None
        _c_rr = el.find("rr")
        _rr = Rr.from_sdf(_c_rr) if _c_rr is not None else None
        return cls(xx=_xx, xy=_xy, xz=_xz, xp=_xp, xq=_xq, xr=_xr, yy=_yy, yz=_yz, yp=_yp, yq=_yq, yr=_yr, zz=_zz, zp=_zp, zq=_zq, zr=_zr, pp=_pp, pq=_pq, pr=_pr, qq=_qq, qr=_qr, rr=_rr)
