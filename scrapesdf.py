import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional
from xml.etree import ElementTree as ET

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = Path(tempfile.gettempdir()) / "sdformat"
SRC_DIR = SCRIPT_DIR / "src" / "reignite"
TYPES_DIR = SRC_DIR / "utils"
SDF_SRC_DIR = SRC_DIR / "sdf"

SDF_REPO_URL = "https://github.com/gazebosim/sdformat.git"

PRIMITIVE_TYPES: dict[str, tuple[str, str, str, str]] = {
    "string": ("str", '""', "{val}", "{raw}"),
    "bool": ("bool", "False", "str({val}).lower()", "{raw}.strip().lower() == 'true'"),
    "int": ("int", "0", "str({val})", "_parse_int32({raw})"),
    "uint": ("int", "0", "str({val})", "_parse_uint32({raw})"),
    "unsigned int": ("int", "0", "str({val})", "_parse_uint32({raw})"),
    "double": ("float", "0.0", "str({val})", "_parse_double({raw})"),
    "float": ("float", "0.0", "str({val})", "_parse_double({raw})"),
    "char": ("str", '""', "{val}", "{raw}"),
    "time": ("float", "0.0", "str({val})", "_parse_double({raw})"),
}

NO_NAME_HINTS = {"max_step_size"}

INT32_MIN = -(2 ** 31)
INT32_MAX = 2 ** 31 - 1
UINT32_MAX = 2 ** 32 - 1
FLOAT_MAX = sys.float_info.max

INT_HELPERS = f'''\
import math
import sys

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not ({INT32_MIN} <= v <= {INT32_MAX}):
        raise ValueError(f"int32 out of range: {{v}}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= {UINT32_MAX}):
        raise ValueError(f"uint32 out of range: {{v}}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > {FLOAT_MAX}:
        raise ValueError(f"double out of range: {{raw}}")
    return v

'''


def resolve_type(sdf_type: Optional[str]) -> tuple[str, str, str, str, Optional[str]]:
    if sdf_type is None:
        return "None", "None", "str({val})", "str({raw})", None

    t = sdf_type.strip().lower()

    if t in PRIMITIVE_TYPES:
        hint, default, to_expr, from_expr = PRIMITIVE_TYPES[t]
        return hint, default, to_expr, from_expr, None

    _require_type_file(t)
    cls = _to_classname(t)
    return (
        cls,
        f"{cls}()",
        "{val}.to_sdf()",
        f"{cls}.from_sdf({{raw}})",
        t,
    )


def _require_type_file(mod: str):
    path = TYPES_DIR / f"{mod}.py"
    if not path.exists():
        sys.exit(
            f"\n[ERROR] Unknown type '{mod}' — no file found at:\n"
            f"  {path}\n"
            f"Please create that file and define the type before re-running.\n"
        )


def _to_classname(s: str) -> str:
    return "".join(p.capitalize() for p in s.replace("-", "_").split("_"))


def _format_default(hint: str, raw: str) -> str:
    if hint == "str":
        return '"{}"'.format(raw.replace('"', '\\"'))
    if hint == "bool":
        return "True" if raw.lower() == "true" else "False"
    if hint in ("int", "float"):
        try:
            float(raw)
            return raw
        except ValueError:
            return '"{}"'.format(raw)
    return '"{}"'.format(raw)


def clone_or_pull():
    if (REPO_DIR / ".git").exists():
        print("Pulling latest sdformat…")
        subprocess.run(["git", "-C", str(REPO_DIR), "pull", "--ff-only"], check=True)
    else:
        print("Cloning sdformat…")
        subprocess.run(["git", "clone", "--depth=1", SDF_REPO_URL, str(REPO_DIR)], check=True)


def available_versions() -> list[str]:
    sdf_dir = REPO_DIR / "sdf"
    versions = []
    for d in sdf_dir.iterdir():
        if d.is_dir():
            try:
                float(d.name)
                versions.append(d.name)
            except ValueError:
                pass
    return sorted(versions, key=lambda v: tuple(int(x) for x in v.split(".")))


def load_version_files(version: str) -> dict[str, str]:
    sdf_dir = REPO_DIR / "sdf" / version
    return {p.name: p.read_text(encoding="utf-8") for p in sdf_dir.glob("*.sdf")}


def load_existing_schema(version: str) -> Optional[dict]:
    json_path = SDF_SRC_DIR / _version_dir_name(version) / "data.json"
    if json_path.exists():
        return json.loads(json_path.read_text(encoding="utf-8"))
    return None


def parse_element(el: ET.Element, version_files: dict[str, str]) -> dict:
    out: dict = {}

    desc_el = el.find("description")
    if desc_el is not None and desc_el.text:
        out["_description"] = desc_el.text.strip()

    for k in ("required", "type", "default", "ref"):
        v = el.get(k)
        if v is not None:
            out[f"_{k}"] = v

    attrs = {}
    for a in el.findall("attribute"):
        aname = a.get("name", "")
        adesc = a.find("description")
        attrs[aname] = {
            "type": a.get("type", ""),
            "default": a.get("default", ""),
            "required": a.get("required", "0"),
            "description": adesc.text.strip() if adesc is not None and adesc.text else "",
        }
    if attrs:
        out["_attributes"] = attrs

    includes_seen = []
    for inc in el.findall("include"):
        fname = inc.get("filename", "")
        if not fname:
            continue
        includes_seen.append(fname)
        if fname in version_files:
            try:
                inc_root = ET.fromstring(version_files[fname])
                child_name = inc_root.get("name", fname.replace(".sdf", ""))
                child_schema = parse_element(inc_root, version_files)
                child_schema["_required"] = inc.get("required", "0")
                if child_name not in out:
                    out[child_name] = child_schema
            except ET.ParseError:
                pass

    if includes_seen:
        out["_includes"] = includes_seen

    for child in el.findall("element"):
        cname = child.get("name", "")
        if cname:
            out[cname] = parse_element(child, version_files)

    return out


def parse_version(version: str) -> dict:
    files = load_version_files(version)
    schema: dict = {}
    for fname, xml_text in files.items():
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError as exc:
            print(f"  [warn] parse error {version}/{fname}: {exc}", file=sys.stderr)
            continue
        if root.tag == "element":
            name = root.get("name", fname.replace(".sdf", ""))
            schema[name] = parse_element(root, files)
        else:
            for child in root.findall("element"):
                name = child.get("name", "")
                if name:
                    schema[name] = parse_element(child, files)
    return schema


def _rel_types_import(models_dir: Path) -> str:
    rel = os.path.relpath(TYPES_DIR, models_dir)
    parts = Path(rel).parts
    dots = "." * (parts.count("..") + 1)
    remaining = [p for p in parts if p != ".."]
    return dots + ".".join(remaining) if remaining else dots


def _rel_import(from_dir: Path, to_dir: Path) -> str:
    rel = os.path.relpath(to_dir, from_dir)
    parts = Path(rel).parts
    dots = "." * (parts.count("..") + 1)
    remaining = [p for p in parts if p != ".."]
    return dots + ".".join(remaining) if remaining else dots


def _model_import_base(module_dir: Path) -> str:
    return "."


def _module_name_for(name: str) -> str:
    return name.replace("-", "_")


def _version_dir_name(version: str) -> str:
    return "sdf" + version.replace(".", "_")


def _class_signature(
        class_name: str,
        params: list[tuple],
        prev_version: Optional[str],
        prev_param_names: set[str],
) -> tuple:
    sig_params = []
    for p in params:
        (
            py_name,
            hint,
            default,
            raw_default,
            to_expr,
            from_expr,
            _,
            is_list,
            xml_kind,
            xml_name,
            init_default_expr,
        ) = p
        sig_params.append(
            (
                py_name,
                hint,
                default,
                raw_default,
                to_expr,
                from_expr,
                is_list,
                xml_kind,
                xml_name,
                init_default_expr,
            )
        )
    return (
        class_name,
        tuple(sig_params),
        prev_version,
        tuple(sorted(prev_param_names)),
    )


def _collect_node_map(name: str, node: dict, out: dict[str, dict]) -> None:
    out[name] = node
    for cname, cnode in node.items():
        if cname.startswith("_") or not isinstance(cnode, dict):
            continue
        _collect_node_map(cname, cnode, out)


def _param_names_for_node(name: str, n: dict) -> list[str]:
    params: list[str] = []
    for aname in (n.get("_attributes") or {}).keys():
        params.append(aname.replace("-", "_"))

    child_items = {k: v for k, v in n.items() if not k.startswith("_") and isinstance(v, dict)}
    for cname in child_items.keys():
        params.append(cname.replace("-", "_"))

    if n.get("_type") and not child_items:
        params = [name.replace("-", "_")] + params

    return params


def schema_node_to_classes(
        tag_name: str,
        node: dict,
        models_dir: Path,
        prev_tag_node: Optional[dict],
        prev_version: Optional[str],
        subclass_registry: dict[str, list[dict]],
) -> tuple[str, dict[str, str]]:
    class_specs: list[dict] = []
    defined_classes: set[str] = set()
    prev_node_map: dict[str, dict] = {}
    if prev_tag_node is not None:
        _collect_node_map(tag_name, prev_tag_node, prev_node_map)

    def collect_classes(name: str, n: dict):
        class_name = _to_classname(name)
        if class_name in defined_classes:
            return
        defined_classes.add(class_name)

        child_items = {k: v for k, v in n.items() if not k.startswith("_") and isinstance(v, dict)}
        for cname, cnode in child_items.items():
            collect_classes(cname, cnode)

        params: list[tuple] = []
        type_imports: dict[str, str] = {}
        needs_int_helpers = False
        needs_float_helpers = False
        child_class_names = [_to_classname(cname) for cname in child_items.keys()]

        for aname, ameta in (n.get("_attributes") or {}).items():
            py_name = aname.replace("-", "_")
            hint, default, to_expr, from_expr, mod = resolve_type(ameta.get("type"))
            raw_default = default
            init_default_expr = None
            if mod:
                type_imports[mod] = hint
            if "_parse_int32" in from_expr or "_parse_uint32" in from_expr:
                needs_int_helpers = True
            if "_parse_double" in from_expr:
                needs_float_helpers = True
            schema_default = ameta.get("default", "")
            if schema_default != "":
                raw_default = _format_default(hint, schema_default)
                if mod:
                    default = "None"
                    init_default_expr = f"{hint}.from_sdf({raw_default})"
                else:
                    default = raw_default
            params.append(
                (
                    py_name,
                    hint,
                    default,
                    raw_default,
                    to_expr,
                    from_expr,
                    ameta.get("description", ""),
                    False,
                    "attr",
                    aname,
                    init_default_expr,
                )
            )

        for cname, cnode in child_items.items():
            py_name = cname.replace("-", "_")
            child_cls = _to_classname(cname)
            required = cnode.get("_required", "0")
            is_list = required in ("*", "+")
            hint = f'List["{child_cls}"]' if is_list else f'"{child_cls}"'
            default = "None"
            desc = cnode.get("_description", "")
            params.append((py_name, hint, default, default, "", "", desc, is_list, "child", cname, None))

        if n.get("_type") and not child_items:
            hint, default, to_expr, from_expr, mod = resolve_type(n["_type"])
            raw_default = default
            init_default_expr = None
            if mod:
                type_imports[mod] = hint
            if "_parse_int32" in from_expr or "_parse_uint32" in from_expr:
                needs_int_helpers = True
            if "_parse_double" in from_expr:
                needs_float_helpers = True
            schema_default = n.get("_default", "")
            if schema_default != "":
                raw_default = _format_default(hint, schema_default)
                if mod:
                    default = "None"
                    init_default_expr = f"{hint}.from_sdf({raw_default})"
                else:
                    default = raw_default
            params = [
                         (
                             name.replace("-", "_"),
                             hint,
                             default,
                             raw_default,
                             to_expr,
                             from_expr,
                             n.get("_description", ""),
                             False,
                             "leaf",
                             name,
                             init_default_expr,
                         )
                     ] + params

        prev_param_names: set[str] = set()
        prev_node = prev_node_map.get(name)
        if prev_node is not None and prev_version is not None:
            prev_param_names = set(_param_names_for_node(name, prev_node))

        base_ref = "Model"
        prev_alias = None
        if prev_node is not None and prev_version is not None:
            prev_file = SDF_SRC_DIR / _version_dir_name(prev_version) / "models" / f"{_module_name_for(name)}.py"
            if prev_file.exists():
                prev_alias = f"_Prev{class_name}"
                base_ref = prev_alias
            else:
                prev_param_names = set()

        class_specs.append(
            {
                "class_name": class_name,
                "element_name": name,
                "params": params,
                "type_imports": type_imports,
                "needs_int_helpers": needs_int_helpers,
                "needs_float_helpers": needs_float_helpers,
                "child_class_names": child_class_names,
                "prev_param_names": prev_param_names,
                "prev_alias": prev_alias,
                "base_ref": base_ref,
            }
        )

    collect_classes(tag_name, node)

    def render_class_block(spec: dict) -> str:
        name = spec["element_name"]
        class_name = spec["class_name"]
        params = spec["params"]
        base_ref = spec["base_ref"]
        prev_param_names = spec["prev_param_names"]

        params_to_emit = params if base_ref == "Model" else [
            p for p in params if p[0] not in prev_param_names
        ]
        shared_names = [p[0] for p in params if p[0] in prev_param_names]

        block: list[str] = [f"class {class_name}({base_ref}):"]
        sig_parts = ["self"] + [f"{p[0]}: {p[1]} = {p[2]}" for p in params]
        sig = ", ".join(sig_parts)
        if len(f"    def __init__({sig}):") > 100:
            block.append("    def __init__(")
            block.append("        self,")
            for i, p in enumerate(params):
                comma = "," if i < len(params) - 1 else ""
                block.append(f"        {p[0]}: {p[1]} = {p[2]}{comma}")
            block.append("    ):")
        else:
            block.append(f"    def __init__({sig}):")

        if not params and base_ref == "Model":
            block.append("        pass")
        else:
            for p in params:
                py_name, _, _, _, _, _, _, _, _, _, init_default_expr = p
                if init_default_expr:
                    block.append(f"        if {py_name} is None:")
                    block.append(f"            {py_name} = {init_default_expr}")

            if base_ref != "Model":
                if shared_names:
                    shared_args = ", ".join(f"{n}={n}" for n in shared_names)
                    block.append(f"        super().__init__({shared_args})")
                else:
                    block.append("        super().__init__()")

            for p in params:
                py_name, _, _, _, _, _, _, is_list, _, _, _ = p
                if py_name in prev_param_names:
                    continue
                block.append(f"        self.{py_name} = {py_name}" + (" or []" if is_list else ""))

        block.append("")
        block.append("    def to_sdf(self) -> ET.Element:")
        if base_ref == "Model":
            block.append(f'        el = ET.Element("{name}")')
        else:
            block.append("        el = super().to_sdf()")
        for p in params_to_emit:
            py_name, _, _, _, to_expr, _, _, is_list, xml_kind, xml_name, _ = p
            val_ref = f"self.{py_name}"
            if xml_kind == "attr":
                expr = to_expr.replace("{val}", val_ref)
                block.append(f"        if self.{py_name} is not None:")
                block.append(f'            el.set("{xml_name}", {expr})')
            elif xml_kind == "leaf":
                expr = to_expr.replace("{val}", val_ref)
                block.append(f"        if self.{py_name} is not None:")
                block.append(f"            el.text = {expr}")
            elif xml_kind == "child":
                if is_list:
                    block.append(f"        for item in (self.{py_name} or []):")
                    block.append(f"            el.append(item.to_sdf())")
                else:
                    block.append(f"        if self.{py_name} is not None:")
                    block.append(f"            el.append(self.{py_name}.to_sdf())")
        block.append("        return el")

        block.append("")
        block.append("    @classmethod")
        block.append("    def from_sdf(cls, el: ET.Element) -> \"" + class_name + "\":")
        init_args: list[str] = []
        if base_ref != "Model" and shared_names:
            block.append(f"        _base = {base_ref}.from_sdf(el)")
        for p in params:
            py_name, _, _, raw_default, _, from_expr, _, is_list, xml_kind, xml_name, _ = p
            if py_name in prev_param_names:
                init_args.append(f"{py_name}=_base.{py_name}")
                continue
            if xml_kind == "attr":
                raw_expr = f'el.get("{xml_name}", {raw_default})'
                val_expr = from_expr.replace("{raw}", raw_expr)
                block.append(f"        _{py_name} = {val_expr}")
            elif xml_kind == "leaf":
                block.append(f"        _text = el.text or {raw_default}")
                val_expr = from_expr.replace("{raw}", "_text")
                block.append(f"        _{py_name} = {val_expr}")
            elif xml_kind == "child":
                child_cls = _to_classname(xml_name)
                if is_list:
                    block.append(
                        f'        _{py_name} = [{child_cls}.from_sdf(c) for c in el.findall("{xml_name}")]'
                    )
                else:
                    block.append(f'        _c_{py_name} = el.find("{xml_name}")')
                    block.append(
                        f'        _{py_name} = {child_cls}.from_sdf(_c_{py_name}) if _c_{py_name} is not None else None'
                    )
            init_args.append(f"{py_name}=_{py_name}")

        if init_args:
            args_str = ", ".join(init_args)
            block.append(f"        return cls({args_str})")
        else:
            block.append("        return cls()")

        block.append("")
        return "\n".join(block)

    spec_by_name = {s["class_name"]: s for s in class_specs}

    def render_module(
            module_dir: Path,
            spec: dict,
            module_name: str,
            child_module_map: dict[str, str],
            is_root: bool,
    ) -> str:
        lines: list[str] = [
            "from __future__ import annotations",
            "",
            "from xml.etree import ElementTree as ET",
            "",
        ]

        visited = set()

        def get_inline_specs(s):
            inlines = []
            for cc in s["child_class_names"]:
                cm = child_module_map.get(cc)
                if cm == "<inline>" and cc not in visited:
                    visited.add(cc)
                    cspec = spec_by_name[cc]
                    inlines.extend(get_inline_specs(cspec))
                    inlines.append(cspec)
            return inlines

        inline_specs = get_inline_specs(spec)
        all_specs = inline_specs + [spec]

        needs_list = any("List[" in p[1] for s in all_specs for p in s["params"])
        if needs_list:
            lines.append("from typing import List")
            lines.append("")

        lines.append(f"from ..model import Model")

        for s in all_specs:
            if s["prev_alias"] and prev_version is not None:
                prev_dir = _version_dir_name(prev_version)
                if s == spec and is_root:
                    module_parts = ["models", tag_name]
                else:
                    prev_module_name = _module_name_for(s["element_name"])
                    module_parts = ["models", prev_module_name]
                prev_import = f"...{prev_dir}." + ".".join(module_parts)
                lines.append(f"from {prev_import} import {s['class_name']} as {s['prev_alias']}")

        rel_types = _rel_types_import(module_dir)
        all_type_imports = {}
        for s in all_specs:
            all_type_imports.update(s["type_imports"])
        for mod, cls in sorted(all_type_imports.items()):
            lines.append(f"from {rel_types}.{mod} import {cls}")

        prefix = ""
        for child_class in spec["child_class_names"]:
            child_module = child_module_map.get(child_class)
            if child_module and child_module != "<inline>":
                lines.append(f"from {prefix}.{child_module} import {child_class}")

        lines.append("")

        if any(s["needs_int_helpers"] or s["needs_float_helpers"] for s in all_specs):
            lines.append("")
            lines.append(INT_HELPERS)

        lines.append("")

        for s in inline_specs:
            lines.append(render_class_block(s))
            lines.append("")

        lines.append(render_class_block(spec))
        return "\n".join(lines).rstrip() + "\n"

    root_class_name = _to_classname(tag_name)
    subclass_sources: dict[str, str] = {}
    child_module_map: dict[str, str] = {}

    def ensure_subclass_module(spec: dict) -> tuple[str, bool]:
        class_name = spec["class_name"]
        signature = _class_signature(
            class_name,
            spec["params"],
            prev_version,
            spec["prev_param_names"],
        )
        entries = subclass_registry.setdefault(class_name, [])
        for entry in entries:
            if entry["signature"] == signature:
                child_module_map[class_name] = entry["module"]
                return entry["module"], False

        module_base = _module_name_for(spec["element_name"])
        module_name = module_base
        if entries:
            module_name = "<inline>"
            print(f"  [warn] subclass conflict for {class_name}: inlining")

        entries.append({"signature": signature, "module": module_name})
        child_module_map[class_name] = module_name
        return module_name, True

    for spec in class_specs:
        if spec["class_name"] == root_class_name:
            continue
        module_name, is_new = ensure_subclass_module(spec)
        if is_new and module_name != "<inline>" and module_name not in subclass_sources:
            subclass_sources[module_name] = render_module(
                models_dir,
                spec,
                module_name,
                child_module_map,
                is_root=False,
            )

    root_spec = next(s for s in class_specs if s["class_name"] == root_class_name)
    root_src = render_module(
        models_dir,
        root_spec,
        tag_name,
        child_module_map,
        is_root=True,
    )
    return root_src, subclass_sources


MODEL_PY = """\
from __future__ import annotations

from xml.etree import ElementTree as ET


class Model:
    def to_sdf(self) -> ET.Element:
        raise NotImplementedError

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        raise NotImplementedError
"""


def generate_init(tag_names: list[str]) -> str:
    lines = ["from __future__ import annotations", ""]
    for tag in sorted(tag_names):
        root_cls = _to_classname(tag)
        lines.append(f"from .{tag} import {root_cls}")
    lines.append("")
    tag_list = ", ".join(f'\"{t}\"' for t in sorted(tag_names))
    lines.append(f"TAG_NAMES: list[str] = [{tag_list}]")
    lines.append("")
    return "\n".join(lines)


def generate_version_init(tag_names: list[str]) -> str:
    lines = ["from __future__ import annotations", "", "from . import models as _models", ""]
    for tag in sorted(tag_names):
        cls = _to_classname(tag)
        lines.append(f"{cls} = _models.{cls}")
    lines.append("")
    tag_list = ", ".join(f'\"{t}\"' for t in sorted(tag_names))
    lines.append(f"TAG_NAMES: list[str] = [{tag_list}]")
    lines.append("TAG_CLASS_MAP: dict[str, type] = {")
    for tag in sorted(tag_names):
        cls = _to_classname(tag)
        lines.append(f"    \"{tag}\": {cls},")
    lines.append("}")
    lines.append("")
    lines.append("def get_tag_class(tag: str) -> type | None:")
    lines.append("    return TAG_CLASS_MAP.get(tag)")
    lines.append("")
    return "\n".join(lines)


def process_version(version: str, prev_version: Optional[str], prev_schema: Optional[dict]):
    print(f"\n=== {version} ===")

    version_dir = SDF_SRC_DIR / _version_dir_name(version)
    json_path = version_dir / "data.json"
    if json_path.parent.exists():
        shutil.rmtree(json_path.parent)
    json_path.parent.mkdir(parents=True)

    schema = parse_version(version)
    json_path.write_text(json.dumps(schema, ensure_ascii=False), encoding="utf-8")
    print(f"  Wrote {json_path}")

    model_py = version_dir / "model.py"
    model_py.write_text(MODEL_PY, encoding="utf-8")
    print(f"  Wrote {model_py}")

    version_init = version_dir / "__init__.py"
    version_init.write_text("", encoding="utf-8")

    models_dir = version_dir / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    subclass_registry: dict[str, list[dict]] = {}
    pending_subclasses: dict[str, str] = {}

    tag_names = []
    for tag, node in schema.items():
        if not isinstance(node, dict):
            continue
        tag_names.append(tag)
        prev_tag_node = prev_schema.get(tag) if prev_schema else None
        py_src, subclass_sources = schema_node_to_classes(
            tag,
            node,
            models_dir,
            prev_tag_node,
            prev_version,
            subclass_registry,
        )
        out_path = models_dir / f"{tag}.py"
        out_path.write_text(py_src, encoding="utf-8")
        print(f"  Wrote {out_path}")
        for module_name, module_src in subclass_sources.items():
            pending_subclasses[module_name] = module_src

    for module_name, module_src in pending_subclasses.items():
        out_path = models_dir / f"{module_name}.py"
        out_path.write_text(module_src, encoding="utf-8")
        print(f"  Wrote {out_path}")

    init_path = models_dir / "__init__.py"
    init_path.write_text(generate_init(tag_names), encoding="utf-8")
    print(f"  Wrote {init_path}")

    version_init.write_text(generate_version_init(tag_names), encoding="utf-8")
    print(f"  Wrote {version_init}")

    return schema


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Scrape sdformat specs and generate Python bindings.")
    parser.add_argument(
        "-r", "--regenerate",
        action="store_true",
        help="Regenerate all SDF versions from scratch, ignoring any already-generated output.",
    )
    args = parser.parse_args()

    clone_or_pull()

    versions = available_versions()
    if not versions:
        sys.exit("No SDF versions found in cloned repo.")

    prev_schema = None
    prev_version = None
    skipping = not args.regenerate
    for v in versions:
        version_dir = SDF_SRC_DIR / _version_dir_name(v)
        if skipping and (version_dir / "models" / "__init__.py").exists():
            prev_schema = load_existing_schema(v)
            prev_version = v
            continue
        skipping = False
        prev_schema = process_version(v, prev_version, prev_schema)
        prev_version = v

    print("\nDone.")


if __name__ == "__main__":
    main()
