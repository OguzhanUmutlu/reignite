from __future__ import annotations

from xml.etree import ElementTree as ET

from .box import Box
from .cylinder import Cylinder
from .empty import Empty
from .heightmap import Heightmap
from .image import Image
from .mesh import Mesh
from .plane import Plane
from .polyline import Polyline
from .sphere import Sphere
from ...sdf1_4.models.geometry import Geometry as _PrevGeometry


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
        super().__init__(box=box, cylinder=cylinder, heightmap=heightmap, image=image, mesh=mesh, plane=plane,
                         sphere=sphere, empty=empty)
        self.polyline = polyline

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.polyline is not None:
            el.append(self.polyline.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Geometry":
        _base = _PrevGeometry.from_sdf(el)
        _c_polyline = el.find("polyline")
        _polyline = Polyline.from_sdf(_c_polyline) if _c_polyline is not None else None
        return cls(box=_base.box, cylinder=_base.cylinder, heightmap=_base.heightmap, image=_base.image,
                   mesh=_base.mesh, plane=_base.plane, polyline=_polyline, sphere=_base.sphere, empty=_base.empty)
