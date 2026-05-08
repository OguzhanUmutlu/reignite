from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.particle_size import ParticleSize as _PrevParticleSize
from ....utils.vector3 import Vector3


class ParticleSize(_PrevParticleSize):
    def __init__(self, particle_size: Vector3 = None):
        if particle_size is None:
            particle_size = Vector3.from_sdf("1 1 1")
        super().__init__(particle_size=particle_size)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ParticleSize":
        _base = _PrevParticleSize.from_sdf(el)
        return cls(particle_size=_base.particle_size)
