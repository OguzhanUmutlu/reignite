from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.save import Save as _PrevSave
from .path import Path


class Save(_PrevSave):
    def __init__(self, enabled: bool = False, path: "Path" = None):
        super().__init__(enabled=enabled, path=path)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Save":
        _base = _PrevSave.from_sdf(el)
        return cls(enabled=_base.enabled, path=_base.path)
