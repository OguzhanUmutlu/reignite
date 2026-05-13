### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3


class Box(BaseModel):
    class Size(BaseModel):
        def __init__(self, sdf_version: str | None = None, size: _SDFVector3 = None):
            super().__init__(sdf_version)
            if size is None:
                size = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
            self.size = size

        def to_version(self, target_version: str) -> "Box.Size":
            kwargs = {"sdf_version": target_version}
            kwargs["size"] = self.size
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("size")
            if self.size is not None:
                el.text = self.size.to_sdf(version)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Box.Size | SDFError":
            _text = el.text or "1 1 1"
            _size = _SDFVector3._from_sdf(_text, version)
            if isinstance(_size, SDFError):
                return _size
            return cls(sdf_version=version, size=_size)

    def __init__(self, sdf_version: str | None = None, size: "Box.Size" = None):
        super().__init__(sdf_version)
        self.size = size
        if self.size is not None:
            if getattr(self.size, '__version__', None) is None:
                self.size.__version__ = self.__version__
            elif getattr(self.size, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.size = self.size.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Box":
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("box")
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Box | SDFError":
        _c_size = el.find("size")
        if _c_size is not None:
            _res = cls.Size._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        return cls(sdf_version=version, size=_size)
