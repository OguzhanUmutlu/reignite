from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_2.models.ode import Ode as _PrevOde
from ...sdf1_2.models.contact import Contact as _PrevContact


class Ode(_PrevOde):
    def __init__(
        self,
        mu: "Mu" = None,
        mu2: "Mu2" = None,
        fdir1: "Fdir1" = None,
        slip1: "Slip1" = None,
        slip2: "Slip2" = None
    ):
        super().__init__()
        self.mu = mu
        self.mu2 = mu2
        self.fdir1 = fdir1
        self.slip1 = slip1
        self.slip2 = slip2

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.mu is not None:
            el.append(self.mu.to_sdf())
        if self.mu2 is not None:
            el.append(self.mu2.to_sdf())
        if self.fdir1 is not None:
            el.append(self.fdir1.to_sdf())
        if self.slip1 is not None:
            el.append(self.slip1.to_sdf())
        if self.slip2 is not None:
            el.append(self.slip2.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_mu = el.find("mu")
        _mu = Mu.from_sdf(_c_mu) if _c_mu is not None else None
        _c_mu2 = el.find("mu2")
        _mu2 = Mu2.from_sdf(_c_mu2) if _c_mu2 is not None else None
        _c_fdir1 = el.find("fdir1")
        _fdir1 = Fdir1.from_sdf(_c_fdir1) if _c_fdir1 is not None else None
        _c_slip1 = el.find("slip1")
        _slip1 = Slip1.from_sdf(_c_slip1) if _c_slip1 is not None else None
        _c_slip2 = el.find("slip2")
        _slip2 = Slip2.from_sdf(_c_slip2) if _c_slip2 is not None else None
        return cls(mu=_mu, mu2=_mu2, fdir1=_fdir1, slip1=_slip1, slip2=_slip2)


class Contact(_PrevContact):
    def __init__(self, ode: "Ode" = None):
        super().__init__()
        self.ode = ode

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Contact":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(ode=_ode)
