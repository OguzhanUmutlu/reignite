from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_4.models.texture import Texture as _PrevTexture
from ...sdf1_4.models.heightmap import Heightmap as _PrevHeightmap
from .uri import Uri
from .size import Size
from .pos import Pos
from .blend import Blend
from .use_terrain_paging import UseTerrainPaging


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
        super().__init__(uri=uri, size=size, pos=pos, texture=texture, blend=blend, use_terrain_paging=use_terrain_paging)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Heightmap":
        _base = _PrevHeightmap.from_sdf(el)
        return cls(uri=_base.uri, size=_base.size, pos=_base.pos, texture=_base.texture, blend=_base.blend, use_terrain_paging=_base.use_terrain_paging)
