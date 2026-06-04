import os
import xml.etree.ElementTree as ET
from copy import deepcopy
from pathlib import Path
from typing import Optional

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


def simple_str(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return ""
    return str(value)


class TextElement(BaseModel):
    def __init__(self, name: str, text, attributes: dict | None = None, **extra):
        super().__init__(sdf_version=None)
        self.name = name
        self.text = simple_str(text)
        self.attributes = {**(attributes or dict()), **extra}

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        text = el.text.strip() if el.text else ""
        return cls(el.tag, text, el.attrib)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        e = ET.Element(self.name, attrib=self.attributes)
        if self.text is not None:
            e.text = simple_str(self.text)
        return e

    def to_version(self, target_version: str) -> "BaseModel":
        return self


class ParentElement(BaseModel):
    def __init__(self, name: str, children: list[BaseModel | None], attributes: dict | None = None, **extra):
        super().__init__(sdf_version=None)
        self.name = name
        self.attributes = {**(attributes or dict()), **extra}
        self.children = list(filter(lambda x: x is not None, children))

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        children = [TextElement._from_sdf(c, version) if len(c) == 0 else ParentElement._from_sdf(c, version) for c in
                    el]
        return cls(el.tag, children, el.attrib)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        e = ET.Element(self.name, attrib=self.attributes)
        for child in self.children:
            e.append(child.to_sdf(version))
        return e

    def to_version(self, target_version: str) -> "BaseModel":
        return self


import inspect

class Plugin(_Base):
    @classmethod
    def register(cls, *names: str):
        def decorator(subclass):
            for name in names:
                if name and name != "None":
                    plugin_classes[name] = subclass
            return subclass
        return decorator

    def __init__(
            self,
            sdf_version: str | None = None,
            elements: list[BaseModel | None] | None = None,
            filename: str = "__default__",
            name: str = "__default__",
            **extra
    ):
        super().__init__(sdf_version=sdf_version, filename=filename, name=name)
        self.elements: list[BaseModel] = list(filter(lambda x: x is not None, elements or []))
        for k, v in extra.items():
            if v is None:
                continue
            self.elements.append(TextElement(k, v))

    def to_version(self, target_version: str) -> "Plugin":
        from copy import copy, deepcopy
        new_plugin = copy(self)
        new_plugin.sdfversion = target_version
        new_plugin.elements = [
            e.to_version(target_version) if hasattr(e, "to_version") else deepcopy(e)
            for e in self.elements
        ]
        return new_plugin

    def to_sdf(self, version: Optional[str] = None) -> ET.Element:
        el = super().to_sdf(version)

        for item in self.elements:
            el.append(item.to_sdf())

        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        filename = el.get("filename", "__default__")
        name = el.get("name", "__default__")

        elements = []

        def _parse_et(e: ET.Element) -> BaseModel:
            if len(e) > 0:
                children = [_parse_et(d) for d in e]
                return ParentElement(e.tag, children, e.attrib)

            text = e.text.strip() if e.text else ""
            return TextElement(e.tag, text, e.attrib)

        for c in el:
            if c.tag not in ("name", "filename"):
                elements.append(_parse_et(c))

        if cls is Plugin:
            target_cls = plugin_classes.get(filename) or plugin_classes.get(name)
            if target_cls and target_cls is not Plugin:
                try:
                    kwargs = {}
                    sig = inspect.signature(target_cls.__init__)
                    for param_name, param in sig.parameters.items():
                        if param_name in ('self', 'args', 'kwargs', 'gui_kwargs'):
                            continue
                        
                        tag = next((e for e in elements if e.name == param_name), None)
                        if tag is not None:
                            if isinstance(tag, TextElement):
                                val = tag.text
                                if param.annotation is float:
                                    val = float(val)
                                elif param.annotation is int:
                                    val = int(val)
                                elif param.annotation is bool:
                                    val = str(val).lower() in ('true', '1', 't', 'yes')
                                kwargs[param_name] = val
                            
                    return target_cls(**kwargs)
                except Exception:
                    pass

        return cls(
            sdf_version=version,
            elements=elements,
            filename=filename,
            name=name
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
