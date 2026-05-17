from __future__ import annotations

from xml.etree import ElementTree as ET

from .errors import SDFError


def _vector3(v: float | tuple[float, float, float] | Vector3, y: float = None, z: float = None) -> Vector3:
    if isinstance(v, Vector3):
        return v
    if isinstance(v, tuple) and len(v) == 3:
        return Vector3(v[0], v[1], v[2])
    if y is not None and z is not None:
        return Vector3(float(v), float(y), float(z))
    raise ValueError(f"Invalid input for Vector3: {v}, {y}, {z}")


class Vector3:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def to_sdf(self, version: str = None) -> str:
        return f"{self.x} {self.y} {self.z}"

    @classmethod
    def _from_sdf(cls, source: str | ET.Element, version: str = None) -> Vector3 | SDFError:
        text = source.text if isinstance(source, ET.Element) else source
        if text is None:
            return cls()
        try:
            parts = text.split()
            if len(parts) == 0:
                return cls()
            if len(parts) != 3:
                return SDFError(f"Vector3 expects 3 values, got {len(parts)}")
            x, y, z = (float(v) for v in parts)
            return cls(x, y, z)
        except ValueError:
            return SDFError(f"Invalid float in Vector3: {text}")

    @classmethod
    def from_sdf(cls, source: str | ET.Element, version: str = None) -> Vector3:
        res = cls._from_sdf(source, version)
        if isinstance(res, SDFError):
            raise ValueError(str(res))
        return res
