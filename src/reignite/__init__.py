from __future__ import annotations

import os
from pathlib import Path
from typing import TypeVar, Any
from xml.etree import ElementTree as ET

from .elements import get_element_class, ELEMENT_CLASS_MAP
from .utils import BaseModel

T = TypeVar("T")


def _to_classname(s: str) -> str:
    return "".join(p.capitalize() for p in s.replace("-", "_").split("_"))


def get_all_valid_models():
    for resource_path in os.getenv("GZ_SIM_RESOURCE_PATH", "").split(":"):
        for root, dirs, files in os.walk(resource_path):
            if "model.sdf" in files:
                yield Path(root).name
                dirs.clear()


def resolve_path(path: str | Path):
    if isinstance(path, Path):
        return path
    if path.startswith("model://"):
        rel = path[len("model://"):]
        if "GZ_SIM_RESOURCE_PATH" not in os.environ:
            return path
        for p in os.environ["GZ_SIM_RESOURCE_PATH"].split(":"):
            candidate = Path(p) / rel
            if candidate.exists():
                if candidate.is_dir():
                    if (candidate / "model.sdf").exists():
                        return candidate / "model.sdf"
                else:
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


def _process_includes(parent: ET.Element, allow_include: bool):
    for i, child in enumerate(list(parent)):
        if child.tag == "include":
            if not allow_include:
                raise ValueError("Include tags are not allowed when allow_include=False")

            uri_el = child.find("uri")
            if uri_el is None or not uri_el.text:
                raise ValueError("<include> must have a <uri> child")

            uri = uri_el.text
            resolved = resolve_path(uri)
            try:
                included_tree = ET.parse(resolved).getroot()
            except Exception as e:
                raise ValueError(f"Failed to parse included file {resolved}: {e}")

            _, included_el = _select_root_element(included_tree)

            for override_el in list(child):
                if override_el.tag == "uri":
                    continue
                elif override_el.tag == "name":
                    if override_el.text:
                        included_el.set("name", override_el.text)
                else:
                    if override_el.tag not in ("plugin", "model_state"):
                        existing = included_el.findall(override_el.tag)
                        for ex in existing:
                            included_el.remove(ex)
                    included_el.append(override_el)

            _process_includes(included_el, allow_include)
            parent[i] = included_el
        else:
            _process_includes(child, allow_include)


def read_sdf_from_element(root: ET.Element, assert_class: type[T] | None = None,
                          allow_include: bool = False) -> T | Any:
    _process_includes(root, allow_include)
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

    el = element_class.from_sdf(element, version)
    if assert_class is not None and not isinstance(el, assert_class):
        raise ValueError(
            f"Element is not of expected type {assert_class.__name__}: {type(el).__name__}")
    return el


def read_sdf(source: str | Path, assert_class: type[T] | None = None, allow_include: bool = True) -> T | Any:
    return read_sdf_from_element(ET.parse(resolve_path(source)).getroot(), assert_class, allow_include)


def read_sdf_string(xml_text: str, assert_class: type[T] | None = None, allow_include: bool = False) -> T | Any:
    return read_sdf_from_element(ET.fromstring(xml_text), assert_class, allow_include)


def sdf_to_root(el: ET.Element, version: str) -> ET.ElementTree:
    root = ET.Element("sdf", version=version)
    root.append(el)
    return ET.ElementTree(root)


def element_to_root(el: BaseModel, version: str) -> ET.ElementTree:
    return sdf_to_root(el.to_sdf(version), version)
