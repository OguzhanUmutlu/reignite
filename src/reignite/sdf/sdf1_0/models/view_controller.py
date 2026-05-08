from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class ViewController(Model):
    def __init__(self, view_controller: str = "oribit"):
        self.view_controller = view_controller

    def to_sdf(self) -> ET.Element:
        el = ET.Element("view_controller")
        if self.view_controller is not None:
            el.text = self.view_controller
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ViewController":
        _text = el.text or "oribit"
        _view_controller = _text
        return cls(view_controller=_view_controller)
