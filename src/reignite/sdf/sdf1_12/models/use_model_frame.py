from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_11.models.use_model_frame import UseModelFrame as _PrevUseModelFrame


class UseModelFrame(_PrevUseModelFrame):
    def __init__(self, use_model_frame: bool = True):
        super().__init__(use_model_frame=use_model_frame)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UseModelFrame":
        _base = _PrevUseModelFrame.from_sdf(el)
        return cls(use_model_frame=_base.use_model_frame)
