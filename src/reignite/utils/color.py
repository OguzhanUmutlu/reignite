from __future__ import annotations

from typing import Sequence, Union

_ColorT = Union[Sequence[float], str, "Color"]


def _color(value: _ColorT) -> Color:
    if isinstance(value, Color):
        return value
    if isinstance(value, str):
        value = value.strip()
        if value.startswith("#"):
            return Color(value)
        parts = value.split()
        if len(parts) == 3:
            parts.append("1.0")
        if len(parts) == 4:
            try:
                r, g, b, a = (int(float(x) * 255) for x in parts)
                return Color(r, g, b, a)
            except ValueError:
                pass
        return Color(value)
    return Color(*value)


class Color:
    def __init__(self, r: int | str, g: int = None, b: int = None, a: int = 255):
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
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.a = int(a)

    def to_sdf(self, _=None):
        return str(self)

    def __str__(self) -> str:
        return f"{self.r / 255.0} {self.g / 255.0} {self.b / 255.0} {self.a / 255.0}"
