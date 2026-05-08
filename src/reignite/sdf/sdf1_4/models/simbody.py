from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .min_step_size import MinStepSize
from .accuracy import Accuracy
from .max_transient_velocity import MaxTransientVelocity
from .contact import Contact


class Simbody(Model):
    def __init__(
        self,
        min_step_size: "MinStepSize" = None,
        accuracy: "Accuracy" = None,
        max_transient_velocity: "MaxTransientVelocity" = None,
        contact: "Contact" = None
    ):
        self.min_step_size = min_step_size
        self.accuracy = accuracy
        self.max_transient_velocity = max_transient_velocity
        self.contact = contact

    def to_sdf(self) -> ET.Element:
        el = ET.Element("simbody")
        if self.min_step_size is not None:
            el.append(self.min_step_size.to_sdf())
        if self.accuracy is not None:
            el.append(self.accuracy.to_sdf())
        if self.max_transient_velocity is not None:
            el.append(self.max_transient_velocity.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Simbody":
        _c_min_step_size = el.find("min_step_size")
        _min_step_size = MinStepSize.from_sdf(_c_min_step_size) if _c_min_step_size is not None else None
        _c_accuracy = el.find("accuracy")
        _accuracy = Accuracy.from_sdf(_c_accuracy) if _c_accuracy is not None else None
        _c_max_transient_velocity = el.find("max_transient_velocity")
        _max_transient_velocity = MaxTransientVelocity.from_sdf(_c_max_transient_velocity) if _c_max_transient_velocity is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        return cls(min_step_size=_min_step_size, accuracy=_accuracy, max_transient_velocity=_max_transient_velocity, contact=_contact)
