### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class Rfid(BaseModel):
    def __init__(self, sdf_version: str | None = None):
        super().__init__(sdf_version)

    def to_version(self, target_version: str) -> "Rfid":
        kwargs: dict = {"sdf_version": target_version}
        return Rfid(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("rfid")
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Rfid | SDFError":
        return cls(sdf_version=version)
