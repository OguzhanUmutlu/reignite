from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_6.models.implicit_spring_damper import ImplicitSpringDamper as _PrevImplicitSpringDamper


class ImplicitSpringDamper(_PrevImplicitSpringDamper):
    def __init__(self, implicit_spring_damper: bool = False):
        super().__init__(implicit_spring_damper=implicit_spring_damper)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ImplicitSpringDamper":
        _base = _PrevImplicitSpringDamper.from_sdf(el)
        return cls(implicit_spring_damper=_base.implicit_spring_damper)
