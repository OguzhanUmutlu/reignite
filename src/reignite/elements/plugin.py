import os
import xml.etree.ElementTree as ET
from copy import deepcopy
from pathlib import Path
from typing import Optional

from ..sdf.plugin import Plugin as _Base


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


def dict_element(el: ET.Element):
    return {
        "tag": el.tag,
        "attributes": el.attrib,
        "children": [dict_element(child) for child in el]
    }


plugin_classes: dict[str, type] = {}


class Plugin(_Base):
    def __init__(
            self,
            sdf_version: Optional[str] = None,
            copy_data: Optional[dict] = None,
            filename: str = "__default__",
            name: str = "__default__"
    ):
        super().__init__(sdf_version=sdf_version, filename=filename, name=name)
        self.copy_data = copy_data or {}

    def to_version(self, target_version: str) -> "Plugin":
        return self.__class__(
            sdf_version=target_version, copy_data=deepcopy(self.copy_data) if self.copy_data else None,
            filename=self.filename, name=self.name
        )

    def to_sdf(self, version: Optional[str] = None) -> ET.Element:
        el = super().to_sdf(version)

        def _build_et(tag, node_data):
            e = ET.Element(tag)
            if not isinstance(node_data, dict):
                e.text = str(node_data)
                return e
            if "attributes" in node_data:
                for ak, av in node_data["attributes"].items():
                    e.set(ak, str(av))
            if "text" in node_data:
                e.text = str(node_data["text"])
            if "children" in node_data:
                for ck, cv in node_data["children"].items():
                    if isinstance(cv, list):
                        for cv_item in cv:
                            e.append(_build_et(ck, cv_item))
                    else:
                        e.append(_build_et(ck, cv))
            return e

        for k, v in self.copy_data.items():
            if isinstance(v, list):
                for item in v:
                    el.append(_build_et(k, item))
            else:
                el.append(_build_et(k, v))

        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        copy_data = {}

        def _parse_et(e: ET.Element):
            out = {}
            if e.attrib:
                out["attributes"] = dict(e.attrib)
            if e.text and e.text.strip():
                out["text"] = e.text.strip()
            children = {}
            for c in e:
                cd = _parse_et(c)
                if c.tag in children:
                    if not isinstance(children[c.tag], list):
                        children[c.tag] = [children[c.tag]]
                    children[c.tag].append(cd)
                else:
                    children[c.tag] = cd
            if children:
                out["children"] = children
            return out

        for c in el:
            if c.tag not in ("name", "filename"):
                cd = _parse_et(c)
                if c.tag in copy_data:
                    if not isinstance(copy_data[c.tag], list):
                        copy_data[c.tag] = [copy_data[c.tag]]
                    copy_data[c.tag].append(cd)
                else:
                    copy_data[c.tag] = cd

        return cls(
            sdf_version=version, copy_data=copy_data, filename=el.get("filename", "__default__"),
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
