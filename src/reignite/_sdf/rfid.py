### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


class Rfid(BaseModel):
    def __init__(self, sdf_version: str | None = None):
        super().__init__(sdf_version)

    def to_version(self, target_version: str) -> "Rfid":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("rfid")
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Rfid | SDFError":
        return cls(sdf_version=version)
