from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class ParticleSize(Model):
    def __init__(self, particle_size: Vector3 = None):
        if particle_size is None:
            particle_size = Vector3.from_sdf("1 1 1")
        self.particle_size = particle_size

    def to_sdf(self) -> ET.Element:
        el = ET.Element("particle_size")
        if self.particle_size is not None:
            el.text = self.particle_size.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ParticleSize":
        _text = el.text or "1 1 1"
        _particle_size = Vector3.from_sdf(_text)
        return cls(particle_size=_particle_size)
