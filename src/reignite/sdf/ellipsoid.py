### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3


class Ellipsoid(BaseModel):
    class Radii(BaseModel):
        def __init__(self, sdf_version: str | None = None, radii: _SDFVector3 = None):
            super().__init__(sdf_version)
            if radii is None:
                radii = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
            self.radii = radii

        def to_version(self, target_version: str) -> "Ellipsoid.Radii":
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
            el = ET.Element("radii")
            if self.radii is not None:
                el.text = self.radii.to_sdf(version)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Ellipsoid.Radii | SDFError":
            _text = el.text or "1 1 1"
            _radii = _SDFVector3._from_sdf(_text, version)
            if isinstance(_radii, SDFError):
                return _radii
            return cls(sdf_version=version, radii=_radii)

    def __init__(self, sdf_version: str | None = None, radii: "Ellipsoid.Radii" = None):
        super().__init__(sdf_version)
        self.radii = radii
        if self.radii is not None:
            if getattr(self.radii, '__version__', None) is None:
                self.radii.__version__ = self.__version__
            elif getattr(self.radii, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.radii = self.radii.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Ellipsoid":
        kwargs = {"sdf_version": target_version}
        kwargs["radii"] = self.radii.to_version(target_version) if self.radii is not None else None
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
            el.append(self.radii.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Ellipsoid | SDFError":
        _c_radii = el.find("radii")
        if _c_radii is not None:
            _res = cls.Radii._from_sdf(_c_radii, version)
            if isinstance(_res, SDFError):
                return _res.extend("radii")
            _radii = _res
        else:
            _radii = None
        return cls(sdf_version=version, radii=_radii)
