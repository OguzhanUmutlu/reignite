from __future__ import annotations

import importlib
from pathlib import Path
from xml.etree import ElementTree as ET


def _to_classname(s: str) -> str:
    return "".join(p.capitalize() for p in s.replace("-", "_").split("_"))


def _load_sdf_module():
    return importlib.import_module("reignite.sdf")


def _select_root_element(root: ET.Element) -> tuple[str, ET.Element]:
    if root.tag not in ("sdf", "gazebo"):
        return root.tag, root

    children = [c for c in root if isinstance(c.tag, str)]
    if not children:
        raise ValueError("SDF root contains no element children.")

    if len(children) != 1:
        raise ValueError(
            "SDF root contains multiple top-level elements; pass element_name to choose one: "
            f"{[c.tag for c in children]}"
        )
    return children[0].tag, children[0]


def _resolve_element_class(module, element: str):
    get_element_class = getattr(module, "get_element_class", None)
    if callable(get_element_class):
        return get_element_class(element)
    return None


def read_sdf_from_element(root: ET.Element):
    version = root.get("version")
    if not version:
        raise ValueError("SDF version attribute not found on root element.")

    element_name, element = _select_root_element(root)
    module = _load_sdf_module()
    element_class = _resolve_element_class(module, element_name)
    if element_class is None:
        available = sorted(getattr(module, "ELEMENT_CLASS_MAP", {}).keys())
        raise ValueError(f"Element '{element_name}' not supported. Available: {available}")

    return element_class.from_sdf(element, version)


def read_sdf(source: str | Path):
    return read_sdf_from_element(ET.parse(Path(source)).getroot())


def read_sdf_string(xml_text: str):
    return read_sdf_from_element(ET.fromstring(xml_text))
