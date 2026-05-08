from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .box import Box
from .sphere import Sphere
from .cylinder import Cylinder
from .mesh import Mesh
from .plane import Plane
from .image import Image
from .heightmap import Heightmap


class Geometry(Model):
    def __init__(
        self,
        box: "Box" = None,
        sphere: "Sphere" = None,
        cylinder: "Cylinder" = None,
        mesh: "Mesh" = None,
        plane: "Plane" = None,
        image: "Image" = None,
        heightmap: "Heightmap" = None
    ):
        self.box = box
        self.sphere = sphere
        self.cylinder = cylinder
        self.mesh = mesh
        self.plane = plane
        self.image = image
        self.heightmap = heightmap

    def to_sdf(self) -> ET.Element:
        el = ET.Element("geometry")
        if self.box is not None:
            el.append(self.box.to_sdf())
        if self.sphere is not None:
            el.append(self.sphere.to_sdf())
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf())
        if self.mesh is not None:
            el.append(self.mesh.to_sdf())
        if self.plane is not None:
            el.append(self.plane.to_sdf())
        if self.image is not None:
            el.append(self.image.to_sdf())
        if self.heightmap is not None:
            el.append(self.heightmap.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Geometry":
        _c_box = el.find("box")
        _box = Box.from_sdf(_c_box) if _c_box is not None else None
        _c_sphere = el.find("sphere")
        _sphere = Sphere.from_sdf(_c_sphere) if _c_sphere is not None else None
        _c_cylinder = el.find("cylinder")
        _cylinder = Cylinder.from_sdf(_c_cylinder) if _c_cylinder is not None else None
        _c_mesh = el.find("mesh")
        _mesh = Mesh.from_sdf(_c_mesh) if _c_mesh is not None else None
        _c_plane = el.find("plane")
        _plane = Plane.from_sdf(_c_plane) if _c_plane is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image) if _c_image is not None else None
        _c_heightmap = el.find("heightmap")
        _heightmap = Heightmap.from_sdf(_c_heightmap) if _c_heightmap is not None else None
        return cls(box=_box, sphere=_sphere, cylinder=_cylinder, mesh=_mesh, plane=_plane, image=_image, heightmap=_heightmap)
