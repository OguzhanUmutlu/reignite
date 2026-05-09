from __future__ import annotations

from xml.etree import ElementTree as ET

from .errors import SDFError


class Pose:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, roll: float = 0.0, pitch: float = 0.0,
                 yaw: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def to_sdf(self) -> str:
        return f"{self.x} {self.y} {self.z} {self.roll} {self.pitch} {self.yaw}"

    @classmethod
    def _from_sdf(cls, source: str | ET.Element, version: str) -> Pose | SDFError:
        text = source.text if isinstance(source, ET.Element) else source
        if text is None:
            return cls()
        try:
            parts = text.split()
            if len(parts) == 0:
                return cls()
            if len(parts) != 6:
                return SDFError(f"Pose expects 6 values, got {len(parts)}")
            x, y, z, roll, pitch, yaw = (float(v) for v in parts)
            return cls(x, y, z, roll, pitch, yaw)
        except ValueError:
            return SDFError(f"Invalid float in Pose: {text}")

    @classmethod
    def from_sdf(cls, source: str | ET.Element, version: str) -> Pose:
        res = cls._from_sdf(source, version)
        if isinstance(res, SDFError):
            raise ValueError(str(res))
        return res
