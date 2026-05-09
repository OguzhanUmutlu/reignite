from __future__ import annotations

from xml.etree import ElementTree as ET

from .scale import Scale
from .submesh import Submesh
from ...sdf1_3.models.mesh import Mesh as _PrevMesh
from ...sdf1_3.models.uri import Uri as _PrevUri


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


class Mesh(_PrevMesh):
    def __init__(self, uri: "Uri" = None, submesh: "Submesh" = None, scale: "Scale" = None):
        super().__init__(uri=uri, submesh=submesh, scale=scale)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mesh":
        _base = _PrevMesh.from_sdf(el)
        return cls(uri=_base.uri, submesh=_base.submesh, scale=_base.scale)
