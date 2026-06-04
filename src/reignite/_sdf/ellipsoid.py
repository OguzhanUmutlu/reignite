### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import _Vector3T, _vector3

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Ellipsoid(BaseModel):
    def __init__(self, sdf_version: str | None = None, radii: _Vector3T | None = None):
        super().__init__(sdf_version)
        self.radii = _vector3(radii) if radii is not None else None

    def to_version(self, target_version: str) -> "Ellipsoid":
        kwargs: dict = {"sdf_version": target_version, "radii": self.radii}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("ellipsoid")
        if self.radii is not None:
            _c_tmp = ET.Element("radii")
            _c_tmp.text = str(self.radii)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Ellipsoid | SDFError":
        _c_tmp = el.find("radii")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("radii")
            _radii = _val
        else:
            _radii = None
        return cls(sdf_version=version, radii=_radii)
