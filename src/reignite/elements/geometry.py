from __future__ import annotations

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
from ..utils.vector2d import _vector2d
from ..utils.vector3 import _vector3


class BoxGeometry(Geometry):
    def __init__(self, size: Vector3 | tuple[float, float, float] | float, y: float | None = None,
                 z: float | None = None):
        super().__init__(box=Box(size=_vector3(size, y, z)))


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
    def __init__(self, radii: Vector3 | tuple[float, float, float] | float, y: float | None = None,
                 z: float | None = None):
        super().__init__(ellipsoid=Ellipsoid(radii=_vector3(radii, y, z)))


class EmptyGeometry(Geometry):
    def __init__(self):
        super().__init__(empty="")  # noqa


class MeshGeometry(Geometry):
    def __init__(self, uri: str, scale: float | tuple[float, float, float] | Vector3 = 1.0, sy: float | None = None,
                 sz: float | None = None):
        super().__init__(mesh=Mesh(uri=uri, scale=_vector3(scale, sy, sz)))


class PlaneGeometry(Geometry):
    def __init__(self, size: Vector2d | tuple[float, float],
                 normal: Vector3 | tuple[float, float, float] = Vector3(0, 0, 1)):
        super().__init__(plane=Plane(normal=_vector3(normal), size=_vector2d(size)))


class PolylineGeometry(Geometry):
    def __init__(self, points: list[Vector2d | tuple[float, float]], height: float = 0.01):
        super().__init__(polyline=Polyline(points=list(map(_vector2d, points)), height=height))


class SphereGeometry(Geometry):
    def __init__(self, radius: float):
        super().__init__(sphere=Sphere(radius=radius))
