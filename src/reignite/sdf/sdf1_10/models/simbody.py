from __future__ import annotations

from xml.etree import ElementTree as ET

from .accuracy import Accuracy
from .contact import Contact
from .max_transient_velocity import MaxTransientVelocity
from .min_step_size import MinStepSize
from ...sdf1_9.models.simbody import Simbody as _PrevSimbody


class Simbody(_PrevSimbody):
    def __init__(
            self,
            min_step_size: "MinStepSize" = None,
            accuracy: "Accuracy" = None,
            max_transient_velocity: "MaxTransientVelocity" = None,
            contact: "Contact" = None
    ):
        super().__init__(min_step_size=min_step_size, accuracy=accuracy, max_transient_velocity=max_transient_velocity,
                         contact=contact)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Simbody":
        _base = _PrevSimbody.from_sdf(el)
        return cls(min_step_size=_base.min_step_size, accuracy=_base.accuracy,
                   max_transient_velocity=_base.max_transient_velocity, contact=_base.contact)
