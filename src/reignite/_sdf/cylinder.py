### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class Cylinder(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        length: float | None = None,
        radius: float | None = None
    ):
        super().__init__(sdf_version)
        self.length = length
        self.radius = radius

    def to_version(self, target_version: str) -> "Cylinder":
        kwargs: dict = {"sdf_version": target_version, "length": self.length, "radius": self.radius}
        return Cylinder(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("cylinder")
        if self.length is not None:
            _c_tmp = ET.Element("length")
            _c_tmp.text = str(self.length)
            el.append(_c_tmp)
        if self.radius is not None:
            _c_tmp = ET.Element("radius")
            _c_tmp.text = str(self.radius)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Cylinder | SDFError":
        _c_tmp = el.find("length")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("length")
            _length = _val
        else:
            _length = None
        _c_tmp = el.find("radius")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("radius")
            _radius = _val
        else:
            _radius = None
        return cls(sdf_version=version, length=_length, radius=_radius)
