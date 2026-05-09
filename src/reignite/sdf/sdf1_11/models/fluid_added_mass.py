from __future__ import annotations

from xml.etree import ElementTree as ET

from .pp import Pp
from .pq import Pq
from .pr import Pr
from .qq import Qq
from .qr import Qr
from .rr import Rr
from .xp import Xp
from .xq import Xq
from .xr import Xr
from .xx import Xx
from .xy import Xy
from .xz import Xz
from .yp import Yp
from .yq import Yq
from .yr import Yr
from .yy import Yy
from .yz import Yz
from .zp import Zp
from .zq import Zq
from .zr import Zr
from .zz import Zz
from ...sdf1_10.models.fluid_added_mass import FluidAddedMass as _PrevFluidAddedMass


class FluidAddedMass(_PrevFluidAddedMass):
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
        super().__init__(xx=xx, xy=xy, xz=xz, xp=xp, xq=xq, xr=xr, yy=yy, yz=yz, yp=yp, yq=yq, yr=yr, zz=zz, zp=zp,
                         zq=zq, zr=zr, pp=pp, pq=pq, pr=pr, qq=qq, qr=qr, rr=rr)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "FluidAddedMass":
        _base = _PrevFluidAddedMass.from_sdf(el)
        return cls(xx=_base.xx, xy=_base.xy, xz=_base.xz, xp=_base.xp, xq=_base.xq, xr=_base.xr, yy=_base.yy,
                   yz=_base.yz, yp=_base.yp, yq=_base.yq, yr=_base.yr, zz=_base.zz, zp=_base.zp, zq=_base.zq,
                   zr=_base.zr, pp=_base.pp, pq=_base.pq, pr=_base.pr, qq=_base.qq, qr=_base.qr, rr=_base.rr)
