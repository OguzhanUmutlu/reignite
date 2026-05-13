### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3


class Ellipsoid(BaseModel):
    def __init__(self, sdf_version: str | None = None, radii: _SDFVector3 = None):
        super().__init__(sdf_version)
        if radii is None:
            radii = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
        self.radii = radii

    def to_version(self, target_version: str) -> "Ellipsoid":
        kwargs = {"sdf_version": target_version}
        kwargs["radii"] = self.radii
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("ellipsoid")
        if self.radii is not None:
            _c_tmp = ET.Element("radii")
            _c_tmp.text = self.radii.to_sdf(version)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Ellipsoid | SDFError":
        _c_tmp = el.find("radii")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _SDFVector3._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("radii")
            _radii = _val
        else:
            _radii = None
        return cls(sdf_version=version, radii=_radii)
