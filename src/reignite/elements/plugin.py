import os
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from ..sdf.plugin import Plugin as _Base
from ..utils.errors import SDFError


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
