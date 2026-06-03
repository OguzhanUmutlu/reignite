from __future__ import annotations

from typing import Sequence, Union

_PoseT = Union[Sequence[float], str, "Pose"]


def _pose(value: Pose | Sequence[float] | str) -> Pose:
    if isinstance(value, Pose):
        return value
    if isinstance(value, str):
        parts = value.split()
        if len(parts) == 6:
            try:
                x, y, z, r, p, yw = (float(v) for v in parts)
                return Pose(x, y, z, r, p, yw)
            except ValueError:
                pass
        elif len(parts) == 0:
            return Pose()
    value = list(value) if not isinstance(value, str) else []
    if len(value) != 6:
        value += [0.0] * (6 - len(value))
    return Pose(*value[:6])


class Pose:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, roll: float = 0.0, pitch: float = 0.0,
                 yaw: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def to_sdf(self, _=None):
        return str(self)

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z} {self.roll} {self.pitch} {self.yaw}"
