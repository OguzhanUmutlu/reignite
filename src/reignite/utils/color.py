from __future__ import annotations

from xml.etree import ElementTree as ET

from .errors import SDFError


class Color:
    def __init__(self, r: int, g: int, b: int, a: int):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def to_sdf(self) -> str:
        return f"{self.r / 255.0} {self.g / 255.0} {self.b / 255.0} {self.a / 255.0}"

    @classmethod
    def _from_sdf(cls, source: str | ET.Element, _version: str) -> Color | SDFError:
        text = source.text if isinstance(source, ET.Element) else source
        if text is None:
            return cls(0, 0, 0, 255)
        try:
            parts = text.split()
            if len(parts) == 0:
                return cls(0, 0, 0, 255)
            if len(parts) == 3:
                parts = [*parts, "1.0"]
            if len(parts) != 4:
                return SDFError(f"Color expects 3 or 4 values, got {len(parts)}")
            r, g, b, a = (int(float(x) * 255) for x in parts)
            return cls(r, g, b, a)
        except ValueError:
            return SDFError(f"Invalid Color value: {text}")

    @classmethod
    def from_sdf(cls, source: str | ET.Element, version: str) -> Color:
        res = cls._from_sdf(source, version)
        if isinstance(res, SDFError):
            raise ValueError(str(res))
        return res
