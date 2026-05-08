from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class EnableMetrics(Model):
    def __init__(self, enable_metrics: bool = False):
        self.enable_metrics = enable_metrics

    def to_sdf(self) -> ET.Element:
        el = ET.Element("enable_metrics")
        if self.enable_metrics is not None:
            el.text = str(self.enable_metrics).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnableMetrics":
        _text = el.text or False
        _enable_metrics = _text.strip().lower() == 'true'
        return cls(enable_metrics=_enable_metrics)
