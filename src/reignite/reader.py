from __future__ import annotations

import importlib
from pathlib import Path
from xml.etree import ElementTree as ET


def _version_dir_name(version: str) -> str:
    return "sdf" + version.replace(".", "_")


def _normalize_version(version: str) -> str:
    return version.replace("_", ".")


def _load_version_module(version: str):
    version = _normalize_version(version)
    module_name = f"reignite.sdf.{_version_dir_name(version)}"
    return importlib.import_module(module_name)


def _select_root_element(root: ET.Element) -> tuple[str, ET.Element]:
    if root.tag != "sdf":
        return root.tag, root

    children = [c for c in root if isinstance(c.tag, str)]
    if not children:
        raise ValueError("SDF root contains no element children.")

    if len(children) != 1:
        raise ValueError(
            "SDF root contains multiple top-level elements; pass tag_name to choose one: "
            f"{[c.tag for c in children]}"
        )
    return children[0].tag, children[0]


def _resolve_tag_class(module, tag: str):
    get_tag_class = getattr(module, "get_tag_class", None)
    if callable(get_tag_class):
        return get_tag_class(tag)

    models = getattr(module, "models", None)
    if models is None:
        return None

    tag_names = getattr(models, "TAG_NAMES", [])
    tag_map = {name: getattr(models, _to_classname(name)) for name in tag_names}
    return tag_map.get(tag)


def _to_classname(s: str) -> str:
    return "".join(p.capitalize() for p in s.replace("-", "_").split("_"))


def read_sdf_from_element(root: ET.Element):
    version = root.get("version")
    if not version:
        raise ValueError("SDF version attribute not found on root element.")

    tag, element = _select_root_element(root)
    module = _load_version_module(version)
    tag_class = _resolve_tag_class(module, tag)
    if tag_class is None:
        available = sorted(getattr(module, "TAG_CLASS_MAP", {}).keys())
        raise ValueError(f"Tag '{tag}' not supported for version {version}. Available: {available}")

    return tag_class.from_sdf(element)


def read_sdf(source: str | Path):
    return read_sdf_from_element(ET.parse(Path(source)).getroot())


def read_sdf_string(xml_text: str):
    return read_sdf_from_element(ET.fromstring(xml_text))
