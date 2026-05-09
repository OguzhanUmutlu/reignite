from __future__ import annotations

from xml.etree import ElementTree as ET

from .box import Box
from .capsule import Capsule
from .cylinder import Cylinder
from .ellipsoid import Ellipsoid
from .empty import Empty
from .heightmap import Heightmap
from .image import Image
from .mesh import Mesh
from .plane import Plane
from .polyline import Polyline
from .sphere import Sphere
from ...sdf1_9.models.geometry import Geometry as _PrevGeometry


class Geometry(_PrevGeometry):
    def __init__(
            self,
            box: "Box" = None,
            capsule: "Capsule" = None,
            cylinder: "Cylinder" = None,
            ellipsoid: "Ellipsoid" = None,
            heightmap: "Heightmap" = None,
            image: "Image" = None,
            mesh: "Mesh" = None,
            plane: "Plane" = None,
            polyline: "Polyline" = None,
            sphere: "Sphere" = None,
            empty: "Empty" = None
    ):
        super().__init__()
        self.box = box
        self.capsule = capsule
        self.cylinder = cylinder
        self.ellipsoid = ellipsoid
        self.heightmap = heightmap
        self.image = image
        self.mesh = mesh
        self.plane = plane
        self.polyline = polyline
        self.sphere = sphere
        self.empty = empty

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.box is not None:
            el.append(self.box.to_sdf())
        if self.capsule is not None:
            el.append(self.capsule.to_sdf())
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf())
        if self.ellipsoid is not None:
            el.append(self.ellipsoid.to_sdf())
        if self.heightmap is not None:
            el.append(self.heightmap.to_sdf())
        if self.image is not None:
            el.append(self.image.to_sdf())
        if self.mesh is not None:
            el.append(self.mesh.to_sdf())
        if self.plane is not None:
            el.append(self.plane.to_sdf())
        if self.polyline is not None:
            el.append(self.polyline.to_sdf())
        if self.sphere is not None:
            el.append(self.sphere.to_sdf())
        if self.empty is not None:
            el.append(self.empty.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Geometry":
        _c_box = el.find("box")
        _box = Box.from_sdf(_c_box) if _c_box is not None else None
        _c_capsule = el.find("capsule")
        _capsule = Capsule.from_sdf(_c_capsule) if _c_capsule is not None else None
        _c_cylinder = el.find("cylinder")
        _cylinder = Cylinder.from_sdf(_c_cylinder) if _c_cylinder is not None else None
        _c_ellipsoid = el.find("ellipsoid")
        _ellipsoid = Ellipsoid.from_sdf(_c_ellipsoid) if _c_ellipsoid is not None else None
        _c_heightmap = el.find("heightmap")
        _heightmap = Heightmap.from_sdf(_c_heightmap) if _c_heightmap is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image) if _c_image is not None else None
        _c_mesh = el.find("mesh")
        _mesh = Mesh.from_sdf(_c_mesh) if _c_mesh is not None else None
        _c_plane = el.find("plane")
        _plane = Plane.from_sdf(_c_plane) if _c_plane is not None else None
        _c_polyline = el.find("polyline")
        _polyline = Polyline.from_sdf(_c_polyline) if _c_polyline is not None else None
        _c_sphere = el.find("sphere")
        _sphere = Sphere.from_sdf(_c_sphere) if _c_sphere is not None else None
        _c_empty = el.find("empty")
        _empty = Empty.from_sdf(_c_empty) if _c_empty is not None else None
        return cls(box=_box, capsule=_capsule, cylinder=_cylinder, ellipsoid=_ellipsoid, heightmap=_heightmap,
                   image=_image, mesh=_mesh, plane=_plane, polyline=_polyline, sphere=_sphere, empty=_empty)
