from __future__ import annotations

from xml.etree import ElementTree as ET

from .scale import Scale
from .submesh import Submesh
from .uri import Uri
from ...sdf1_2.models.mesh import Mesh as _PrevMesh


class Mesh(_PrevMesh):
    def __init__(self, uri: "Uri" = None, submesh: "Submesh" = None, scale: "Scale" = None):
        super().__init__(uri=uri, scale=scale)
        self.submesh = submesh

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.submesh is not None:
            el.append(self.submesh.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mesh":
        _base = _PrevMesh.from_sdf(el)
        _c_submesh = el.find("submesh")
        _submesh = Submesh.from_sdf(_c_submesh) if _c_submesh is not None else None
        return cls(uri=_base.uri, submesh=_submesh, scale=_base.scale)
