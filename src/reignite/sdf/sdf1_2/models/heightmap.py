from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_0.models.heightmap import Heightmap as _PrevHeightmap
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
        super().__init__(size=size, texture=texture, blend=blend)
        self.uri = uri
        self.pos = pos

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.uri is not None:
            el.append(self.uri.to_sdf())
        if self.pos is not None:
            el.append(self.pos.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Heightmap":
        _base = _PrevHeightmap.from_sdf(el)
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri) if _c_uri is not None else None
        _c_pos = el.find("pos")
        _pos = Pos.from_sdf(_c_pos) if _c_pos is not None else None
        return cls(uri=_uri, size=_base.size, pos=_pos, texture=_base.texture, blend=_base.blend)
