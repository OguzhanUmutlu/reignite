from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model
from ..utils.vector3 import Vector3


class Size(Model):
    def __init__(self, sdf_version: str, size: Vector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        self.size = size

    def to_version(self, target_version: str) -> "Size":
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("size")
        if self.size is not None:
            el.text = self.size.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Size":
        _text = el.text or "1 1 1"
        _size = Vector3.from_sdf(_text)
        return cls(sdf_version=version, size=_size)


class Box(Model):
    def __init__(self, sdf_version: str, size: "Size" = None):
        self.__version__ = sdf_version
        self.size = size

    def to_version(self, target_version: str) -> "Box":
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("box")
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Box":
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size, version) if _c_size is not None else None
        return cls(sdf_version=version, size=_size)
