import os
import xml.etree.ElementTree as ET
from copy import deepcopy
from pathlib import Path
from typing import Optional, List

from .._sdf.plugin import Plugin as _Base
from ..utils.model import BaseModel


def get_plugin_paths():
    paths = [Path(x) for x in os.environ.get("GZ_SIM_SYSTEM_PLUGIN_PATH", "").split(":") if x]
    default_base = Path("/usr") / "lib" / "x86_64-linux-gnu"
    for folder in os.listdir(default_base):
        if folder.startswith("gz-sim-") or folder.startswith("ignition-gazebo"):
            paths.append(default_base / folder / "plugins")

    return paths


def find_plugin_binary(filename):
    if not filename.endswith(".so") and not filename.startswith("lib"):
        filename = f"lib{filename}.so"

    for path in get_plugin_paths():
        full_path = path / filename
        if full_path.exists():
            return full_path
    return None


plugin_classes: dict[str, type] = {}


class TextElement(BaseModel):
    def __init__(self, name: str, text, attributes: Optional[dict] = None, **extra: str):
        super().__init__(sdf_version=None)
        self.name = name
        self.text = str(text)
        self.attributes = {**(attributes or dict()), **extra}

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        text = el.text.strip() if el.text else ""
        return cls(el.tag, text, el.attrib)

    def to_sdf(self, version: str = None) -> ET.Element:
        e = ET.Element(self.name, **self.attributes)
        if self.text is not None:
            e.text = str(self.text)
        return e

    def to_version(self, target_version: str) -> "BaseModel":
        return self


class ParentElement(BaseModel):
    def __init__(self, name: str, children: List[BaseModel], attributes: Optional[dict] = None,
                 **extra: str):
        super().__init__(sdf_version=None)
        self.name = name
        self.attributes = {**(attributes or dict()), **extra}
        self.children = children

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        children = [TextElement._from_sdf(c, version) if len(c) == 0 else ParentElement._from_sdf(c, version) for c in
                    el]
        return cls(el.tag, children, el.attrib)

    def to_sdf(self, version: str = None) -> ET.Element:
        e = ET.Element(self.name, self.attributes)
        for child in self.children:
            e.append(child.to_sdf(version))
        return e

    def to_version(self, target_version: str) -> "BaseModel":
        return self


class Plugin(_Base):
    def __init__(
            self,
            sdf_version: Optional[str] = None,
            elements: Optional[List[BaseModel]] = None,
            filename: str = "__default__",
            name: str = "__default__",
            **extra: str
    ):
        super().__init__(sdf_version=sdf_version, filename=filename, name=name)
        self.elements = elements or []
        for k, v in extra.items():
            self.elements.append(TextElement(k, v))

    def to_version(self, target_version: str) -> "Plugin":
        return self.__class__(
            sdf_version=target_version,
            elements=deepcopy(self.elements),
            filename=self.filename,
            name=self.name
        )

    def to_sdf(self, version: Optional[str] = None) -> ET.Element:
        el = super().to_sdf(version)

        for item in self.elements:
            el.append(item.to_sdf())

        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        elements = []

        def _parse_et(e: ET.Element) -> BaseModel:
            if len(e) > 0:
                children = [_parse_et(c) for c in e]
                return ParentElement(e.tag, children, e.attrib)

            text = e.text.strip() if e.text else ""
            return TextElement(e.tag, text, e.attrib)

        for c in el:
            if c.tag not in ("name", "filename"):
                elements.append(_parse_et(c))

        return cls(
            sdf_version=version,
            elements=elements,
            filename=el.get("filename", "__default__"),
            name=el.get("name", "__default__")
        )

    """@classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        plugin = super()._from_sdf(el, version)
        if isinstance(plugin, SDFError):
            return plugin

        name = el.get("name")
        filename = el.get("filename")

        if not name or not filename:
            return SDFError("Missing 'name' or 'filename' attribute in <plugin> tag.")

        binary_path = find_plugin_binary(filename)
        if not binary_path:
            return SDFError(f"Could not find library [{filename}] in GZ_SIM_SYSTEM_PLUGIN_PATH.")

        try:
            which_gz = subprocess.run(["which", "gz"], stdout=subprocess.PIPE, text=True, check=True).stdout.strip()
            print(f"Using gz binary at: {which_gz}")
            result = subprocess.run(
                ["gz", "plugin", "--info", "-p", str(binary_path)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True, env=os.environ.copy()
            )

            print(str(result.stdout))

            if name not in result.stdout:
                return SDFError(f"Library [{filename}] found, but class [{name}] is not exported.")

        except subprocess.CalledProcessError as e:
            print(e)
            print(e.stdout)
            print(e.stderr)
            return SDFError(f"Library [{binary_path}] is not a valid Gazebo plugin (binary check failed).")

        plugin.config = dict_element(el)["children"]

        return plugin"""
