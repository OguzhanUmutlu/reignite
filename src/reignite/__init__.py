from __future__ import annotations

import os
from pathlib import Path
from xml.etree import ElementTree as ET

from .elements import get_element_class, ELEMENT_CLASS_MAP
from .utils import BaseModel


def _to_classname(s: str) -> str:
    return "".join(p.capitalize() for p in s.replace("-", "_").split("_"))


def resolve_path(path: str | Path):
    if isinstance(path, Path):
        return path
    if path.startswith("model://"):
        rel = path[len("model://")]
        if "GZ_SIM_RESOURCE_PATH" not in os.environ:
            return path
        for p in os.environ["GZ_SIM_RESOURCE_PATH"].split(":"):
            candidate = Path(p) / rel
            if candidate.exists():
                return candidate
        raise ValueError(f"Could not resolve path: {path}")
    return Path(path)


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


def read_sdf_from_element(root: ET.Element):
    if root.tag != "sdf":
        raise ValueError(f"Expected root element to be <sdf>, got <{root.tag}>.")
    version = root.get("version")
    if not version:
        raise ValueError("SDF version attribute not found on root element.")

    element_name, element = _select_root_element(root)
    element_class = get_element_class(element_name)
    if element_class is None:
        available = sorted(ELEMENT_CLASS_MAP.keys())
        raise ValueError(f"Element '{element_name}' not supported. Available: {available}")

    return element_class.from_sdf(element, version)


def read_sdf(source: str | Path):
    return read_sdf_from_element(ET.parse(resolve_path(source)).getroot())


def read_sdf_string(xml_text: str):
    return read_sdf_from_element(ET.fromstring(xml_text))


def sdf_to_root(el: ET.Element, version: str) -> ET.ElementTree:
    root = ET.Element("sdf", version=version)
    root.append(el)
    return ET.ElementTree(root)


def element_to_root(el: BaseModel, version: str) -> ET.ElementTree:
    return sdf_to_root(el.to_sdf(version), version)
