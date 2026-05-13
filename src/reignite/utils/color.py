from __future__ import annotations

from xml.etree import ElementTree as ET

from .errors import SDFError


class Color:
    def __init__(self, r: int | float | str, g: int | float = None, b: int | float = None, a: int | float = 1.0):
        if isinstance(r, str):
            if r.startswith("#"):
                r = r[1:]
                if len(r) == 6:
                    r, g, b = (int(r[i:i + 2], 16) for i in (0, 2, 4))
                    a = 255
                elif len(r) == 8:
                    r, g, b, a = (int(r[i:i + 2], 16) for i in (0, 2, 4, 6))
                elif len(r) == 3:
                    r, g, b = (int(r[i] * 2, 16) for i in range(3))
                    a = 255
                else:
                    raise ValueError(f"Invalid hex color: #{r}")
            else:
                raise ValueError(f"Invalid color string: {r}")
        if isinstance(r, float):
            r = int(r * 255)
        if isinstance(g, float):
            g = int(g * 255)
        if isinstance(b, float):
            b = int(b * 255)
        if isinstance(a, float):
            a = int(a * 255)
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def to_sdf(self, version: str = None) -> str:
        return f"{self.r / 255.0} {self.g / 255.0} {self.b / 255.0} {self.a / 255.0}"

    @classmethod
    def _from_sdf(cls, source: str | ET.Element, _version: str = None) -> Color | SDFError:
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
    def from_sdf(cls, source: str | ET.Element, version: str = None) -> Color:
        res = cls._from_sdf(source, version)
        if isinstance(res, SDFError):
            raise ValueError(str(res))
        return res
