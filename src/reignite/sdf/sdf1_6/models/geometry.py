from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.geometry import Geometry as _PrevGeometry
from .box import Box
from .cylinder import Cylinder
from .heightmap import Heightmap
from .image import Image
from .mesh import Mesh
from .plane import Plane
from .polyline import Polyline
from .sphere import Sphere
from .empty import Empty


class Geometry(_PrevGeometry):
    def __init__(
        self,
        box: "Box" = None,
        cylinder: "Cylinder" = None,
        heightmap: "Heightmap" = None,
        image: "Image" = None,
        mesh: "Mesh" = None,
        plane: "Plane" = None,
        polyline: "Polyline" = None,
        sphere: "Sphere" = None,
        empty: "Empty" = None
    ):
        super().__init__(box=box, cylinder=cylinder, heightmap=heightmap, image=image, mesh=mesh, plane=plane, polyline=polyline, sphere=sphere, empty=empty)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Geometry":
        _base = _PrevGeometry.from_sdf(el)
        return cls(box=_base.box, cylinder=_base.cylinder, heightmap=_base.heightmap, image=_base.image, mesh=_base.mesh, plane=_base.plane, polyline=_base.polyline, sphere=_base.sphere, empty=_base.empty)
