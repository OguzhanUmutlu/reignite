from __future__ import annotations

from xml.etree import ElementTree as ET

from .errors import SDFError


class Vector2d:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def to_sdf(self, version: str = None) -> str:
        return f"{self.x} {self.y}"

    @classmethod
    def _from_sdf(cls, source: str | ET.Element, version: str = None) -> Vector2d | SDFError:
        text = source.text if isinstance(source, ET.Element) else source
        if text is None:
            return cls()
        try:
            parts = text.split()
            if len(parts) == 0:
                return cls()
            if len(parts) != 2:
                return SDFError(f"Vector2d expects 2 values, got {len(parts)}")
            x, y = (float(v) for v in parts)
            return cls(x, y)
        except ValueError:
            return SDFError(f"Invalid float in Vector2d: {text}")

    @classmethod
    def from_sdf(cls, source: str | ET.Element, version: str = None) -> Vector2d:
        res = cls._from_sdf(source, version)
        if isinstance(res, SDFError):
            raise ValueError(str(res))
        return res
