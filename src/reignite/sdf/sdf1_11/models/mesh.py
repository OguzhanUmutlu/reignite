from __future__ import annotations

from xml.etree import ElementTree as ET

from .convex_decomposition import ConvexDecomposition
from .scale import Scale
from .submesh import Submesh
from .uri import Uri
from ...sdf1_10.models.mesh import Mesh as _PrevMesh


class Mesh(_PrevMesh):
    def __init__(
            self,
            optimization: str = "",
            convex_decomposition: "ConvexDecomposition" = None,
            uri: "Uri" = None,
            submesh: "Submesh" = None,
            scale: "Scale" = None
    ):
        super().__init__(uri=uri, submesh=submesh, scale=scale)
        self.optimization = optimization
        self.convex_decomposition = convex_decomposition

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.optimization is not None:
            el.set("optimization", self.optimization)
        if self.convex_decomposition is not None:
            el.append(self.convex_decomposition.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mesh":
        _base = _PrevMesh.from_sdf(el)
        _optimization = el.get("optimization", "")
        _c_convex_decomposition = el.find("convex_decomposition")
        _convex_decomposition = ConvexDecomposition.from_sdf(
            _c_convex_decomposition) if _c_convex_decomposition is not None else None
        return cls(optimization=_optimization, convex_decomposition=_convex_decomposition, uri=_base.uri,
                   submesh=_base.submesh, scale=_base.scale)
