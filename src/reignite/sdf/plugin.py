### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


class Plugin(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__", filename: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name
        self.filename = filename

    def to_version(self, target_version: str) -> "Plugin":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["filename"] = self.filename
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plugin")
        if cmp_version(version, "1.12") < 0:
            if self.name is None:
                raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is None:
            raise ValueError(f"'filename' is required in SDF version {version}")
        if self.filename is not None:
            el.set("filename", self.filename)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if cmp_version(version, "1.12") < 0:
            if el.get("name") is None:
                return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        if el.get("filename") is None:
            return SDFError(f"'filename' is required in SDF version {version}")
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        return cls(sdf_version=version, name=_name, filename=_filename)
