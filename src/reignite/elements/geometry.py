from typing import Union

from .box import Box
from .capsule import Capsule
from .cone import Cone
from .cylinder import Cylinder
from .ellipsoid import Ellipsoid
from .mesh import Mesh
from .plane import Plane
from .polyline import Polyline
from .sphere import Sphere
from .._sdf.geometry import Geometry
from ..utils import Vector3, Vector2d


class BoxGeometry(Geometry):
    def __init__(self, size: Union[Vector3, float], y: float = None, z: float = None):
        if isinstance(size, (int, float)):
            size = Vector3(size, y if y is not None else size, z if z is not None else size)
        super().__init__(box=Box(size=size))


class CapsuleGeometry(Geometry):
    def __init__(self, radius: float, length: float):
        super().__init__(capsule=Capsule(radius=radius, length=length))


class ConeGeometry(Geometry):
    def __init__(self, radius: float, length: float):
        super().__init__(cone=Cone(radius=radius, length=length))


class CylinderGeometry(Geometry):
    def __init__(self, radius: float, length: float):
        super().__init__(cylinder=Cylinder(radius=radius, length=length))


class EllipsoidGeometry(Geometry):
    def __init__(self, radii: Union[Vector3, float], y: float = None, z: float = None):
        if isinstance(radii, (int, float)):
            radii = Vector3(radii, y if y is not None else radii, z if z is not None else radii)
        super().__init__(ellipsoid=Ellipsoid(radii=radii))


class EmptyGeometry(Geometry):
    def __init__(self):
        super().__init__(empty="")


class MeshGeometry(Geometry):
    def __init__(self, uri: str, scale: Vector3 = Vector3(1.0, 1.0, 1.0)):
        super().__init__(mesh=Mesh(uri=uri, scale=scale))


class PlaneGeometry(Geometry):
    def __init__(self, normal: Vector3, size: Vector2d):
        super().__init__(plane=Plane(normal=normal, size=size))


class PolylineGeometry(Geometry):
    def __init__(self, points: list[Vector2d], height: float = 0.01):
        super().__init__(polyline=Polyline(points=points, height=height))


class SphereGeometry(Geometry):
    def __init__(self, radius: float):
        super().__init__(sphere=Sphere(radius=radius))
