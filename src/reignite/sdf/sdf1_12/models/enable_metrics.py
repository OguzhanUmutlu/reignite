from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.enable_metrics import EnableMetrics as _PrevEnableMetrics


class EnableMetrics(_PrevEnableMetrics):
    def __init__(self, enable_metrics: bool = False):
        super().__init__(enable_metrics=enable_metrics)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnableMetrics":
        _base = _PrevEnableMetrics.from_sdf(el)
        return cls(enable_metrics=_base.enable_metrics)
