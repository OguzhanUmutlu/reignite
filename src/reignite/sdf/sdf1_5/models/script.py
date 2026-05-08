from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_4.models.script import Script as _PrevScript
from .uri import Uri
from .name import Name


class Script(_PrevScript):
    def __init__(self, uri: List["Uri"] = None, name: "Name" = None):
        super().__init__()
        self.uri = uri or []
        self.name = name

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.uri or []):
            el.append(item.to_sdf())
        if self.name is not None:
            el.append(self.name.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Script":
        _uri = [Uri.from_sdf(c) for c in el.findall("uri")]
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name) if _c_name is not None else None
        return cls(uri=_uri, name=_name)
