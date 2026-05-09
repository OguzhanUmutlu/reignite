import os
import subprocess
import xml.etree.ElementTree as ET

from ..sdf.plugin import Plugin as _Base
from ..utils.errors import SDFError


def get_plugin_paths():
    paths = os.environ.get("GZ_SIM_SYSTEM_PLUGIN_PATH", "").split(":")
    default_base = "/usr/lib/x86_64-linux-gnu/"
    for folder in os.listdir(default_base):
        if folder.startswith("gz-sim-") or folder.startswith("ignition-gazebo"):
            paths.append(os.path.join(default_base, folder, "plugins"))

    return [p for p in paths if p]


def find_plugin_binary(filename):
    if not filename.endswith(".so"):
        filename = f"lib{filename}.so" if not filename.startswith("lib") else filename

    for path in get_plugin_paths():
        full_path = os.path.join(path, filename)
        if os.path.exists(full_path):
            return full_path
    return None


class Plugin(_Base):
    @classmethod
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
            result = subprocess.run(
                ["gz", "plugin", "--info", "-p", binary_path],
                capture_output=True, text=True, check=True
            )

            if name not in result.stdout:
                return SDFError(f"Library [{filename}] found, but class [{name}] is not exported.")

        except subprocess.CalledProcessError:
            return SDFError(f"Library [{binary_path}] is not a valid Gazebo plugin (binary check failed).")

        plugin.config = list(el)

        return plugin
