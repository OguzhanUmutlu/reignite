from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_3.models.allow_auto_disable import AllowAutoDisable as _PrevAllowAutoDisable


class AllowAutoDisable(_PrevAllowAutoDisable):
    def __init__(self, allow_auto_disable: bool = True):
        super().__init__(allow_auto_disable=allow_auto_disable)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AllowAutoDisable":
        _base = _PrevAllowAutoDisable.from_sdf(el)
        return cls(allow_auto_disable=_base.allow_auto_disable)
