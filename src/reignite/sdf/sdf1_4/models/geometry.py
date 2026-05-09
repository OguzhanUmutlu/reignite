from __future__ import annotations

from xml.etree import ElementTree as ET

from .box import Box
from .cylinder import Cylinder
from .empty import Empty
from .heightmap import Heightmap
from .image import Image
from .mesh import Mesh
from .plane import Plane
from .sphere import Sphere
from ...sdf1_3.models.geometry import Geometry as _PrevGeometry


class Geometry(_PrevGeometry):
    def __init__(
            self,
            box: "Box" = None,
            cylinder: "Cylinder" = None,
            heightmap: "Heightmap" = None,
            image: "Image" = None,
            mesh: "Mesh" = None,
            plane: "Plane" = None,
            sphere: "Sphere" = None,
            empty: "Empty" = None
    ):
        super().__init__(box=box, cylinder=cylinder, heightmap=heightmap, image=image, mesh=mesh, plane=plane,
                         sphere=sphere, empty=empty)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Geometry":
        _base = _PrevGeometry.from_sdf(el)
        return cls(box=_base.box, cylinder=_base.cylinder, heightmap=_base.heightmap, image=_base.image,
                   mesh=_base.mesh, plane=_base.plane, sphere=_base.sphere, empty=_base.empty)
