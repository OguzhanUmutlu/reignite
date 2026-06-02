### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class Plugin(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        filename: str | None = "__default__",
        name: str | None = "__default__"
    ):
        super().__init__(sdf_version)
        self.filename = filename if filename is not None else "__default__"
        self.name = name if name is not None else "__default__"

    def to_version(self, target_version: str) -> "Plugin":
        kwargs: dict = {"sdf_version": target_version, "filename": self.filename, "name": self.name}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("plugin")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Plugin | SDFError":
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, filename=_filename, name=_name)
