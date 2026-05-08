from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.mesh import Mesh as _PrevMesh
from .uri import Uri
from .submesh import Submesh
from .scale import Scale


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
