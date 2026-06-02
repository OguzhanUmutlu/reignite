### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


# noinspection PyUnusedImports
class Sonar(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        geometry: str | None = "cone",
        max: float | None = 1.0,
        min: float | None = 0,
        radius: float | None = 0.5
    ):
        super().__init__(sdf_version)
        self.geometry = geometry if geometry is not None else "cone"
        self.max = max if max is not None else 1.0
        self.min = min if min is not None else 0
        self.radius = radius if radius is not None else 0.5

    def to_version(self, target_version: str) -> "Sonar":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs: dict = {"sdf_version": target_version, "geometry": self.geometry, "max": self.max, "min": self.min, "radius": self.radius}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("sonar")
        if self.geometry is not None:
            _c_tmp = ET.Element("geometry")
            _c_tmp.text = self.geometry
            el.append(_c_tmp)
        if self.max is not None:
            _c_tmp = ET.Element("max")
            _c_tmp.text = str(self.max)
            el.append(_c_tmp)
        if self.min is not None:
            _c_tmp = ET.Element("min")
            _c_tmp.text = str(self.min)
            el.append(_c_tmp)
        if self.radius is not None:
            _c_tmp = ET.Element("radius")
            _c_tmp.text = str(self.radius)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Sonar | SDFError":
        _c_tmp = el.find("geometry")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "cone"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("geometry")
            _geometry = _val
        else:
            _geometry = None
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("max")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("max")
            _max = _val
        else:
            _max = None
        _c_tmp = el.find("min")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("min")
            _min = _val
        else:
            _min = None
        _c_tmp = el.find("radius")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.5
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("radius")
            _radius = _val
        else:
            _radius = None
        return cls(sdf_version=version, geometry=_geometry, max=_max, min=_min, radius=_radius)
