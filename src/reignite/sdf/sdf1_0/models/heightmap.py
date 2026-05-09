from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .blend import Blend
from .texture import Texture
from ..model import Model
from ....utils.vector3 import Vector3


class Heightmap(Model):
    def __init__(
            self,
            filename: str = "__default__",
            size: Vector3 = None,
            origin: Vector3 = None,
            texture: List["Texture"] = None,
            blend: List["Blend"] = None
    ):
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        if origin is None:
            origin = Vector3.from_sdf("0 0 0")
        self.filename = filename
        self.size = size
        self.origin = origin
        self.texture = texture or []
        self.blend = blend or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("heightmap")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.size is not None:
            el.set("size", self.size.to_sdf())
        if self.origin is not None:
            el.set("origin", self.origin.to_sdf())
        for item in (self.texture or []):
            el.append(item.to_sdf())
        for item in (self.blend or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Heightmap":
        _filename = el.get("filename", "__default__")
        _size = Vector3.from_sdf(el.get("size", "1 1 1"))
        _origin = Vector3.from_sdf(el.get("origin", "0 0 0"))
        _texture = [Texture.from_sdf(c) for c in el.findall("texture")]
        _blend = [Blend.from_sdf(c) for c in el.findall("blend")]
        return cls(filename=_filename, size=_size, origin=_origin, texture=_texture, blend=_blend)
