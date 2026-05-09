from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .use_terrain_paging import UseTerrainPaging
from ...sdf1_3.models.blend import Blend as _PrevBlend
from ...sdf1_3.models.diffuse import Diffuse as _PrevDiffuse
from ...sdf1_3.models.fade_dist import FadeDist as _PrevFadeDist
from ...sdf1_3.models.heightmap import Heightmap as _PrevHeightmap
from ...sdf1_3.models.min_height import MinHeight as _PrevMinHeight
from ...sdf1_3.models.normal import Normal as _PrevNormal
from ...sdf1_3.models.pos import Pos as _PrevPos
from ...sdf1_3.models.size import Size as _PrevSize
from ...sdf1_3.models.texture import Texture as _PrevTexture
from ...sdf1_3.models.uri import Uri as _PrevUri
from ....utils.vector3 import Vector3


def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class Uri(_PrevUri):
    def __init__(self, uri: str = "__default__"):
        super().__init__(uri=uri)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Uri":
        _base = _PrevUri.from_sdf(el)
        return cls(uri=_base.uri)


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


class Pos(_PrevPos):
    def __init__(self, pos: Vector3 = None):
        if pos is None:
            pos = Vector3.from_sdf("0 0 0")
        super().__init__(pos=pos)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pos":
        _base = _PrevPos.from_sdf(el)
        return cls(pos=_base.pos)


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


class MinHeight(_PrevMinHeight):
    def __init__(self, min_height: float = 0):
        super().__init__(min_height=min_height)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MinHeight":
        _base = _PrevMinHeight.from_sdf(el)
        return cls(min_height=_base.min_height)


class FadeDist(_PrevFadeDist):
    def __init__(self, fade_dist: float = 0):
        super().__init__(fade_dist=fade_dist)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "FadeDist":
        _base = _PrevFadeDist.from_sdf(el)
        return cls(fade_dist=_base.fade_dist)


class Blend(_PrevBlend):
    def __init__(self, min_height: "MinHeight" = None, fade_dist: "FadeDist" = None):
        super().__init__(min_height=min_height, fade_dist=fade_dist)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Blend":
        _base = _PrevBlend.from_sdf(el)
        return cls(min_height=_base.min_height, fade_dist=_base.fade_dist)


class Heightmap(_PrevHeightmap):
    def __init__(
            self,
            uri: "Uri" = None,
            size: "Size" = None,
            pos: "Pos" = None,
            texture: List["Texture"] = None,
            blend: List["Blend"] = None,
            use_terrain_paging: "UseTerrainPaging" = None
    ):
        super().__init__(uri=uri, size=size, pos=pos, texture=texture, blend=blend)
        self.use_terrain_paging = use_terrain_paging

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.use_terrain_paging is not None:
            el.append(self.use_terrain_paging.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Heightmap":
        _base = _PrevHeightmap.from_sdf(el)
        _c_use_terrain_paging = el.find("use_terrain_paging")
        _use_terrain_paging = UseTerrainPaging.from_sdf(
            _c_use_terrain_paging) if _c_use_terrain_paging is not None else None
        return cls(uri=_base.uri, size=_base.size, pos=_base.pos, texture=_base.texture, blend=_base.blend,
                   use_terrain_paging=_use_terrain_paging)
