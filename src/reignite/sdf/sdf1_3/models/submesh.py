from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .name import Name
from .center import Center


class Submesh(Model):
    def __init__(self, name: "Name" = None, center: "Center" = None):
        self.name = name
        self.center = center

    def to_sdf(self) -> ET.Element:
        el = ET.Element("submesh")
        if self.name is not None:
            el.append(self.name.to_sdf())
        if self.center is not None:
            el.append(self.center.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Submesh":
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name) if _c_name is not None else None
        _c_center = el.find("center")
        _center = Center.from_sdf(_c_center) if _c_center is not None else None
        return cls(name=_name, center=_center)
