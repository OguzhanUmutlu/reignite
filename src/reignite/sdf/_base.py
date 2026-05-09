from __future__ import annotations

from xml.etree import ElementTree as ET


class Model:
    __version__: str = ""

    def to_sdf(self, version: str) -> ET.Element:
        raise NotImplementedError

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Model":
        raise NotImplementedError
