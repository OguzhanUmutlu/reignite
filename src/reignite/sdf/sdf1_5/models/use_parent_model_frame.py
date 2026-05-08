from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class UseParentModelFrame(Model):
    def __init__(self, use_parent_model_frame: bool = False):
        self.use_parent_model_frame = use_parent_model_frame

    def to_sdf(self) -> ET.Element:
        el = ET.Element("use_parent_model_frame")
        if self.use_parent_model_frame is not None:
            el.text = str(self.use_parent_model_frame).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UseParentModelFrame":
        _text = el.text or False
        _use_parent_model_frame = _text.strip().lower() == 'true'
        return cls(use_parent_model_frame=_use_parent_model_frame)
