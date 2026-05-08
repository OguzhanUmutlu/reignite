from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_2.models.heightmap import Heightmap as _PrevHeightmap
from .uri import Uri
from .size import Size
from .pos import Pos
from .texture import Texture
from .blend import Blend


class Heightmap(_PrevHeightmap):
    def __init__(
        self,
        uri: "Uri" = None,
        size: "Size" = None,
        pos: "Pos" = None,
        texture: List["Texture"] = None,
        blend: List["Blend"] = None
    ):
        super().__init__(uri=uri, size=size, pos=pos, texture=texture, blend=blend)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Heightmap":
        _base = _PrevHeightmap.from_sdf(el)
        return cls(uri=_base.uri, size=_base.size, pos=_base.pos, texture=_base.texture, blend=_base.blend)
