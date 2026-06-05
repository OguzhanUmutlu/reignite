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
        filename: str | None = None,
        name: str | None = None
    ):
        super().__init__(sdf_version)
        self.filename = filename
        self.name = name

    def to_version(self, target_version: str) -> "Plugin":
        kwargs: dict = {"sdf_version": target_version, "filename": self.filename, "name": self.name}
        return Plugin(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("plugin")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Plugin | SDFError":
        _raw_filename = el.get("filename")
        if _raw_filename is not None:
            _filename = _raw_filename
            if isinstance(_filename, SDFError):
                return _filename.extend("@filename")
        else:
            _filename = None
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        return cls(sdf_version=version, filename=_filename, name=_name)
