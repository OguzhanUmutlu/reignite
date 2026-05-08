from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_2.models.geometry import Geometry as _PrevGeometry
from .box import Box
from .sphere import Sphere
from .cylinder import Cylinder
from .mesh import Mesh
from .plane import Plane
from .image import Image
from .heightmap import Heightmap
from .empty import Empty


class Geometry(_PrevGeometry):
    def __init__(
        self,
        box: "Box" = None,
        sphere: "Sphere" = None,
        cylinder: "Cylinder" = None,
        mesh: "Mesh" = None,
        plane: "Plane" = None,
        image: "Image" = None,
        heightmap: "Heightmap" = None,
        empty: "Empty" = None
    ):
        super().__init__(box=box, sphere=sphere, cylinder=cylinder, mesh=mesh, plane=plane, image=image, heightmap=heightmap)
        self.empty = empty

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.empty is not None:
            el.append(self.empty.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Geometry":
        _base = _PrevGeometry.from_sdf(el)
        _c_empty = el.find("empty")
        _empty = Empty.from_sdf(_c_empty) if _c_empty is not None else None
        return cls(box=_base.box, sphere=_base.sphere, cylinder=_base.cylinder, mesh=_base.mesh, plane=_base.plane, image=_base.image, heightmap=_base.heightmap, empty=_empty)
