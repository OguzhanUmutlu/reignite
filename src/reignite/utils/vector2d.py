from __future__ import annotations

from typing import Union

_Vector2dT = Union[float, tuple[float, float], "Vector2d"]


def _vector2d(x: float | tuple[float, float] | Vector2d | str, y: float = None) -> Vector2d:
    if isinstance(x, float) and y is None:
        y = x
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
    if isinstance(x, tuple) and len(x) == 2:
        return Vector2d(x[0], x[1])
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
