from __future__ import annotations

from typing import Union

_Vector3T = Union[float, tuple[float, float, float], "Vector3"]


def _vector3(v: _Vector3T, y: float = None, z: float = None) -> Vector3:
    if hasattr(v, "__float__") and y is None:
        y = v
    if hasattr(v, "__float__") and z is None:
        z = v
    if isinstance(v, Vector3):
        return v
    if isinstance(v, str):
        parts = v.split()
        if len(parts) == 3:
            try:
                x, py, pz = (float(p) for p in parts)
                return Vector3(x, py, pz)
            except ValueError:
                pass
    if hasattr(v, "__iter__") and len(v) == 3:
        x, y, z = (float(k) for k in v)
        return Vector3(x, y, z)
    if y is not None and z is not None:
        return Vector3(float(v), float(y), float(z))
    raise ValueError(f"Invalid input for Vector3: {v}, {y}, {z}")


class Vector3:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def to_sdf(self, _=None):
        return str(self)

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z}"
