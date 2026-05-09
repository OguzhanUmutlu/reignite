from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.view_controller import ViewController as _PrevViewController


class ViewController(_PrevViewController):
    def __init__(self, view_controller: str = "orbit"):
        super().__init__(view_controller=view_controller)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ViewController":
        _base = _PrevViewController.from_sdf(el)
        return cls(view_controller=_base.view_controller)
