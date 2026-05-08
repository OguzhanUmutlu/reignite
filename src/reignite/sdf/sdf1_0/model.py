from __future__ import annotations

from xml.etree import ElementTree as ET


class Model:
    def to_sdf(self) -> ET.Element:
        raise NotImplementedError

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        raise NotImplementedError
