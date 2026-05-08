from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.mesh import Mesh as _PrevMesh
from .filename import Filename
from .uri import Uri
from .scale import Scale


class Mesh(_PrevMesh):
    def __init__(self, filename: "Filename" = None, uri: "Uri" = None, scale: "Scale" = None):
        super().__init__(filename=filename, scale=scale)
        self.uri = uri

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.uri is not None:
            el.append(self.uri.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mesh":
        _base = _PrevMesh.from_sdf(el)
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri) if _c_uri is not None else None
        return cls(filename=_base.filename, uri=_uri, scale=_base.scale)
