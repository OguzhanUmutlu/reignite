from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .far_clip import FarClip
from .fov import Fov
from .near_clip import NearClip
from .plugin import Plugin
from .pose import Pose
from ...sdf1_3.models.diffuse import Diffuse as _PrevDiffuse
from ...sdf1_3.models.normal import Normal as _PrevNormal
from ...sdf1_3.models.projector import Projector as _PrevProjector
from ...sdf1_3.models.size import Size as _PrevSize
from ...sdf1_3.models.texture import Texture as _PrevTexture
from ....utils.vector3 import Vector3


class Size(_PrevSize):
    def __init__(self, size: Vector3 = None):
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        super().__init__(size=size)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Size":
        _base = _PrevSize.from_sdf(el)
        return cls(size=_base.size)


class Diffuse(_PrevDiffuse):
    def __init__(self, diffuse: str = "__default__"):
        super().__init__(diffuse=diffuse)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _base = _PrevDiffuse.from_sdf(el)
        return cls(diffuse=_base.diffuse)


class Normal(_PrevNormal):
    def __init__(self, normal: str = "__default__"):
        super().__init__(normal=normal)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Normal":
        _base = _PrevNormal.from_sdf(el)
        return cls(normal=_base.normal)


class Texture(_PrevTexture):
    def __init__(self, size: "Size" = None, diffuse: "Diffuse" = None, normal: "Normal" = None):
        super().__init__()
        self.size = size
        self.diffuse = diffuse
        self.normal = normal

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.size is not None:
            el.append(self.size.to_sdf())
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf())
        if self.normal is not None:
            el.append(self.normal.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Texture":
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size) if _c_size is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse) if _c_diffuse is not None else None
        _c_normal = el.find("normal")
        _normal = Normal.from_sdf(_c_normal) if _c_normal is not None else None
        return cls(size=_size, diffuse=_diffuse, normal=_normal)


class Projector(_PrevProjector):
    def __init__(
            self,
            name: str = "__default__",
            plugin: List["Plugin"] = None,
            texture: "Texture" = None,
            pose: "Pose" = None,
            fov: "Fov" = None,
            near_clip: "NearClip" = None,
            far_clip: "FarClip" = None
    ):
        super().__init__(name=name, plugin=plugin, texture=texture, pose=pose, fov=fov, near_clip=near_clip,
                         far_clip=far_clip)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Projector":
        _base = _PrevProjector.from_sdf(el)
        return cls(name=_base.name, plugin=_base.plugin, texture=_base.texture, pose=_base.pose, fov=_base.fov,
                   near_clip=_base.near_clip, far_clip=_base.far_clip)
