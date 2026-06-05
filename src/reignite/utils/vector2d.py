from __future__ import annotations

from typing import Union

_Vector2dT = Union[float, tuple[float, float], "Vector2d"]


def _vector2d(x: float | tuple[float, float] | Vector2d | str, y: float = None) -> Vector2d:
    if hasattr(x, "__float__") and y is None:
        y = float(x)
    if isinstance(x, Vector2d):
        return x
    if isinstance(x, str):
        parts = x.split()
        if len(parts) == 2:
            try:
                px, py = (float(p) for p in parts)
                return Vector2d(px, py)
            except ValueError:
                pass
    if hasattr(x, "__iter__") and len(x) == 2:
        x, y = (float(k) for k in x)
        return Vector2d(x, y)
    if y is not None:
        return Vector2d(float(x), float(y))
    raise ValueError(f"Invalid input for Vector2d: {x}, {y}")


class Vector2d:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def to_sdf(self, _=None):
        return str(self)

    def __str__(self) -> str:
        return f"{self.x} {self.y}"
