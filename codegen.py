import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional
from xml.etree import ElementTree as ET

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR / "sdformat"
SRC_DIR = SCRIPT_DIR / "src" / "reignite"
TYPES_DIR = SRC_DIR / "utils"
SDF_SRC_DIR = SRC_DIR / "_sdf"
ELEMENTS_SRC_DIR = SRC_DIR / "elements"

SDF_REPO_URL = "https://github.com/gazebosim/sdformat.git"

BASE_VERSION = "1.0"


def make_plural(s: str) -> str:
    if s.endswith("s"):
        return s + "es"
    if s.endswith("y") and s[-2] not in "aeiou":
        return s[:-1] + "ies"
    return s + "s"


def fix_keyword(s: str) -> str:
    if s in {"class", "def", "return", "from", "import", "as", "if", "else", "elif", "for", "while",
             "try", "except", "finally", "with", "lambda", "or", "and", "not", "is", "in",
             "global", "nonlocal", "assert", "yield", "del", "pass", "break", "continue"}:
        return s + "_"
    return s


def cmp_version(v1: str, v2: str) -> int:
    t1 = tuple(int(x) for x in v1.split("."))
    t2 = tuple(int(x) for x in v2.split("."))
    if t1 < t2: return -1
    if t1 > t2: return 1
    return 0


PRIMITIVE_TYPES: dict[str, tuple[str, str, str, str]] = {
    "string": ("str", '""', "{val}", "{raw}"),
    "bool": ("bool", "False", "str({val}).lower()", "str({raw}).strip().lower() == 'true'"),
    "int": ("int", "0", "str({val})", "_parse_int32({raw})"),
    "unsigned int": ("int", "0", "str({val})", "_parse_uint32({raw})"),
    "double": ("float", "0.0", "str({val})", "_parse_double({raw})"),
    "float": ("float", "0.0", "str({val})", "_parse_double({raw})"),
    "time": ("float", "0.0", "f'{int({val})} {round(({val} - int({val})) * 1e9)}'", "_parse_time({raw})")
}


def resolve_type(sdf_type: Optional[str]) -> tuple[str, str, str, str, Optional[str]]:
    if sdf_type is None:
        return "None", "None", "str({val})", "str({raw})", None

    t = sdf_type.strip().lower()

    if t in PRIMITIVE_TYPES:
        hint, default, to_expr, from_expr = PRIMITIVE_TYPES[t]
        return hint, default, to_expr, from_expr, None

    _require_type_file(t)
    cls = _to_classname(t)
    type_alias = f"_{cls}T"
    class_ref = f"_SDF{cls}"
    return (
        type_alias,
        f"{class_ref}()",
        "str({val})",
        f"_parse_{t}({{raw}})",
        t,
    )


def _require_type_file(mod: str):
    path = TYPES_DIR / f"{mod}.py"
    if not path.exists():
        exit(
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
        if raw == "inf":
            return "float('inf')"
        if raw == "-inf":
            return "float('-inf')"
        parts = raw.split()
        if len(parts) == 2:
            try:
                sec, nsec = int(parts[0]), int(parts[1])
                val = sec + nsec * 1e-9
                return repr(round(val, 9))
            except ValueError:
                pass
        try:
            float(raw)
            return raw
        except ValueError:
            return '"{}"'.format(raw)
    return '"{}"'.format(raw)


def _module_name_for(name: str) -> str:
    return name.replace("-", "_")


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

        child_name = fname.replace(".sdf", "")
        child_schema = {
            "_is_include": True,
            "_required": inc.get("required", "0")
        }

        if fname in version_files:
            try:
                inc_root = ET.fromstring(version_files[fname])
                child_name = inc_root.get("name", child_name)
                parsed = parse_element(inc_root, version_files)
                child_schema.update(parsed)
            except ET.ParseError:
                pass
        child_schema["_include_filename"] = fname.replace(".sdf", "")

        out[child_name] = child_schema

    if includes_seen:
        out["_includes"] = includes_seen

    for child in el.findall("element"):
        cname = child.get("name", "")
        if cname:
            out[cname] = parse_element(child, version_files)

    return out


def union_schema(base: dict, new: dict, version: Optional[str]):
    if "_required" in new and "_required" in base:
        if new["_required"] != base["_required"]:
            if "_required_history" not in base:
                base["_required_history"] = {}
                if BASE_VERSION not in base["_required_history"]:
                    base["_required_history"][BASE_VERSION] = base["_required"]
            base["_required_history"][version] = new["_required"]

    for k in ("_description", "_type", "_default", "_required", "_is_include", "_ref"):
        if k in new and k not in base:
            base[k] = new[k]

    if "_attributes" in new:
        if "_attributes" not in base:
            base["_attributes"] = {}

        for aname, ameta in new["_attributes"].items():
            if aname not in base["_attributes"]:
                ameta["_added_in"] = version
                base["_attributes"][aname] = ameta
            else:
                bmeta = base["_attributes"][aname]
                if ameta.get("required") != bmeta.get("required"):
                    if "_required_history" not in bmeta:
                        bmeta["_required_history"] = {}
                        if BASE_VERSION not in bmeta["_required_history"]:
                            bmeta["_required_history"][BASE_VERSION] = bmeta.get("required", "0")
                    bmeta["_required_history"][version] = ameta.get("required")

        for aname, bmeta in base["_attributes"].items():
            if aname not in new["_attributes"] and "_removed_in" not in bmeta:
                bmeta["_removed_in"] = version
    elif "_attributes" in base:
        for aname, bmeta in base["_attributes"].items():
            if "_removed_in" not in bmeta:
                bmeta["_removed_in"] = version

    child_keys_new = set(k for k in new.keys() if not k.startswith("_"))
    child_keys_base = set(k for k in base.keys() if not k.startswith("_"))

    for cname in child_keys_new:
        if cname not in base:
            base[cname] = dict(new[cname])
            base[cname]["_added_in"] = version
        else:
            union_schema(base[cname], new[cname], version)

    for cname in child_keys_base:
        if cname not in child_keys_new and "_removed_in" not in base[cname]:
            base[cname]["_removed_in"] = version


def _effective_required(base_required: str, required_history: dict[str, str]) -> str:
    if not required_history:
        return base_required
    latest_v = max(required_history, key=lambda v: tuple(int(x) for x in v.split(".")))
    return required_history[latest_v]


def _fixup_include_refs(node: dict, schema_keys: set[str]):
    """Walk the schema and fix _ref for includes whose root element name
    doesn't match a schema key but whose source filename does."""
    for k, v in node.items():
        if k.startswith("_") or not isinstance(v, dict):
            continue
        inc_fname = v.get("_include_filename")
        if inc_fname and v.get("_is_include") and "_ref" not in v:
            if k not in schema_keys and inc_fname in schema_keys:
                v["_ref"] = inc_fname
        _fixup_include_refs(v, schema_keys)


def parse_all_versions() -> dict:
    versions = available_versions()
    base_schema: dict = {}
    for version in versions:
        files = load_version_files(version)
        schema: dict = {}
        for fname, xml_text in files.items():
            try:
                root = ET.fromstring(xml_text)
            except ET.ParseError as exc:
                if version == BASE_VERSION:
                    print(f"  [warn] parse error {version}/{fname}: {exc}")
                continue
            if root.tag == "element":
                name = root.get("name", fname.replace(".sdf", ""))
                if name in schema:
                    name = fname.replace(".sdf", "")
                schema[name] = parse_element(root, files)
            else:
                for child in root.findall("element"):
                    name = child.get("name", "")
                    if name:
                        schema[name] = parse_element(child, files)
        union_schema(base_schema, schema, version if version != BASE_VERSION else None)
    _fixup_include_refs(base_schema, set(base_schema.keys()))
    return base_schema


_NOOP_RENAME_RE = re.compile(
    r'<rename>\n\s+<from attribute="([^"]+)"/>\n\s+<to element="\1"/>\n\s+</rename>'
)

_EMPTY_CONVERT_RE = re.compile(
    r'<convert name="[^"]+">\n\s+</convert>\s*(?:<!--[^-]+-->)?'
)


def clean_convert_text(text: str) -> str:
    text = _NOOP_RENAME_RE.sub("", text)
    while True:
        new_text = _EMPTY_CONVERT_RE.sub("", text)
        if new_text == text:
            break
        text = new_text
    return text.strip()


RenameMap = dict[str, list[dict]]


def _parse_convert_ops(el: ET.Element, path: str, ops: list[dict]):
    name = el.get("name") or el.get("descendant_name", "")
    current_path = f"{path}/{name}" if name else path

    for rename in el.findall("rename"):
        frm = rename.find("from")
        to = rename.find("to")
        if frm is not None and to is not None:
            op: dict = {"type": "rename", "path": current_path}
            if frm.get("element"):
                op["from_element"] = frm.get("element")
            if frm.get("attribute"):
                op["from_attribute"] = frm.get("attribute")
            if to.get("element"):
                op["to_element"] = to.get("element")
            if to.get("attribute"):
                op["to_attribute"] = to.get("attribute")
            ops.append(op)

    for move in el.findall("move"):
        frm = move.find("from")
        to = move.find("to")
        if frm is not None and to is not None:
            op = {"type": "move", "path": current_path}
            if frm.get("element"):
                op["from_element"] = frm.get("element")
            if frm.get("attribute"):
                op["from_attribute"] = frm.get("attribute")
            if to.get("element"):
                op["to_element"] = to.get("element")
            if to.get("attribute"):
                op["to_attribute"] = to.get("attribute")
            ops.append(op)

    for add in el.findall("add"):
        op = {"type": "add", "path": current_path}
        if add.get("element"):
            op["element"] = add.get("element")
        if add.get("value"):
            op["value"] = add.get("value")
        ops.append(op)

    for remove in el.findall("remove"):
        op = {"type": "remove", "path": current_path}
        if remove.get("element"):
            op["element"] = remove.get("element")
        ops.append(op)

    for copy_op in el.findall("copy"):
        frm = copy_op.find("from")
        to = copy_op.find("to")
        if frm is not None and to is not None:
            op = {"type": "copy", "path": current_path}
            if frm.get("element"): op["from_element"] = frm.get("element")
            if frm.get("attribute"): op["from_attribute"] = frm.get("attribute")
            if to.get("element"): op["to_element"] = to.get("element")
            if to.get("attribute"): op["to_attribute"] = to.get("attribute")
            ops.append(op)

    for map_op in el.findall("map"):
        frm = map_op.find("from")
        to = map_op.find("to")
        if frm is not None and to is not None:
            op = {
                "type": "map",
                "path": current_path,
                "from_name": frm.get("name"),
                "from_values": [v.text for v in frm.findall("value")],
                "to_name": to.get("name")
            }
            to_val = to.find("value")
            op["to_value"] = to_val.text if to_val is not None else ""
            ops.append(op)

    for child_convert in el.findall("convert"):
        _parse_convert_ops(child_convert, current_path, ops)


def parse_convert_file(version: str) -> list[dict]:
    sdf_dir = REPO_DIR / "sdf" / version
    convert_files = list(sdf_dir.glob("*.convert"))
    if not convert_files:
        return []

    convert_path = convert_files[0]
    raw_text = convert_path.read_text(encoding="utf-8")
    cleaned = clean_convert_text(raw_text)

    if not cleaned:
        return []

    try:
        root = ET.fromstring(cleaned)
    except ET.ParseError:
        try:
            root = ET.fromstring(f"<root>{cleaned}</root>")
        except ET.ParseError as exc:
            print(f"  [warn] failed to parse cleaned convert for {version}: {exc}",
                  file=sys.stderr)
            return []

    ops: list[dict] = []
    _parse_convert_ops(root, "", ops)
    return ops


import hashlib
import json


def get_node_hash(node: dict) -> str:
    def strip_meta(n):
        if not isinstance(n, dict):
            return n
        out = {}
        for k, v in n.items():
            if k in ("_description", "_added_in", "_removed_in", "_required_history", "_required"):
                continue
            out[k] = strip_meta(v)
        return out

    clean = strip_meta(node)
    s = json.dumps(clean, sort_keys=True)
    return hashlib.md5(s.encode("utf-8")).hexdigest()


class ClassParam:
    def __init__(
            self, py_name: str, hint: str, default: str, raw_default: str, to_expr: str, from_expr: str,
            description: str, is_list: bool, kind: str, original_name: str,
            init_default_expr: Optional[str], renames: dict[str, dict], added_in: Optional[str],
            removed_in: Optional[str], is_required: bool, required_history: dict[str, str],
            mod: Optional[str], item_default: str
    ):
        self.py_name = py_name
        self.hint = hint
        self.default = default
        self.raw_default = raw_default
        self.to_expr = to_expr
        self.from_expr = from_expr
        self.description = description
        self.is_list = is_list
        self.kind = kind
        self.original_name = original_name
        self.init_default_expr = init_default_expr
        self.renames = renames
        self.added_in = added_in
        self.removed_in = removed_in
        self.is_required = is_required
        self.required_history = required_history
        self.mod = mod
        self.item_default = item_default


def _collect_class_spec(
        name: str,
        node: dict,
        defined: dict[str, str],
        all_convert_ops: dict[str, list[dict]],
        parent_name: str = None,
        external_imports: set[str] = None,
        qualified_names=None,  # NEW: bare_cls -> "Root.Parent.Cls"
        my_qualified_prefix=""  # NEW: e.g. "Navsat.PositionSensing."
) -> dict:
    if qualified_names is None:
        qualified_names = {}

    if external_imports is None:
        external_imports = set()

    base_class_name = _to_classname(name)
    class_name = base_class_name
    node_hash = get_node_hash(node)

    if class_name in defined:
        if defined[class_name] == node_hash:
            return {"class_name": class_name, "_reuse": True, "element_name": name}
        if parent_name:
            class_name = _to_classname(parent_name) + base_class_name
        else:
            class_name = base_class_name + "2"
        if class_name in defined and defined[class_name] != node_hash:
            class_name = class_name + "2"
        if class_name in defined and defined[class_name] == node_hash:
            return {"class_name": class_name, "_reuse": True, "element_name": name}

    defined[class_name] = node_hash
    qualified_names[class_name] = f"{my_qualified_prefix}{class_name}"

    applicable_ops = []
    for v, ops in all_convert_ops.items():
        for op in ops:
            leaf = str(op.get("path", "")).split("/")[-1]
            if leaf == name:
                op_copy: dict = dict(op)
                op_copy["_version"] = v
                applicable_ops.append(op_copy)
            elif parent_name and leaf == parent_name and op.get("from_element") == name:
                op_copy = dict(op)
                op_copy["_version"] = v
                applicable_ops.append(op_copy)

    child_items = {}
    leaf_items = {}
    for k, v in node.items():
        if not k.startswith("_") and isinstance(v, dict):
            has_children = any(not sub_k.startswith("_") for sub_k in v.keys())
            has_attrs = bool(v.get("_attributes"))
            is_include = v.get("_is_include")
            is_ref = bool(v.get("_ref"))
            if not has_children and not has_attrs and not is_include and not is_ref:
                leaf_items[k] = v
            else:
                child_items[k] = v

    child_specs: list[dict] = []
    child_class_names: dict[str, str] = {}

    for cname, cnode in sorted(child_items.items()):
        if cnode.get("_is_include") or cnode.get("_ref"):
            ref_name = cnode.get("_ref") or cname
            child_cls = _to_classname(ref_name)
            if child_cls in qualified_names:
                child_class_names[cname] = qualified_names[child_cls]
            else:
                external_imports.add(ref_name)
                child_class_names[cname] = child_cls
        else:
            child_spec = _collect_class_spec(
                cname, cnode, defined, all_convert_ops,
                parent_name=name,
                external_imports=external_imports,
                qualified_names=qualified_names,
                my_qualified_prefix=f"{my_qualified_prefix}{class_name}.",
            )
            child_class_names[cname] = child_spec["class_name"]
            if not child_spec.get("_reuse"):
                child_specs.append(child_spec)

    child_specs.sort(key=lambda s: s["class_name"])

    params: list[ClassParam] = []
    type_imports: dict[str, str] = {}
    needs_helpers: set[str] = set()
    custom_helpers: set[str] = set()
    seen_py_names: set[str] = set()

    for aname, ameta in (node.get("_attributes") or {}).items():
        py_name = aname.replace("-", "_")
        if py_name in seen_py_names:
            continue
        seen_py_names.add(py_name)
        added_in = ameta.get("_added_in")
        removed_in = ameta.get("_removed_in")
        for op in applicable_ops:
            if op.get("type") == "remove" and op.get("attribute") == aname:
                if not removed_in or cmp_version(op["_version"], removed_in) < 0:
                    removed_in = op["_version"]
        ameta["_removed_in"] = removed_in
        hint, default, to_expr, from_expr, mod = resolve_type(ameta.get("type"))
        raw_default = default
        init_default_expr = None
        if mod:
            type_imports[mod] = hint
        for fn in ("_parse_int32", "_parse_uint32", "_parse_double", "_parse_time"):
            if fn in from_expr:
                needs_helpers.add(fn)
        if mod and f"_parse_{mod}" in from_expr:
            custom_helpers.add(mod)
        schema_default = ameta.get("default", "")
        if schema_default != "":
            raw_default = _format_default(hint, schema_default)
            if mod:
                default = "None"
                init_default_expr = f"_{mod}({raw_default})"
            else:
                default = raw_default
        renames = {}
        for op in applicable_ops:
            if op.get("type") == "rename" and op.get("from_attribute") == aname:
                if not op.get("from_element") or op.get("from_element") == name:
                    if op.get("to_element") == name and not op.get("to_attribute"):
                        renames[op["_version"]] = {"kind": "text"}
                    elif op.get("to_element"):
                        renames[op["_version"]] = {"kind": "leaf", "name": op["to_element"]}
                    elif op.get("to_attribute"):
                        renames[op["_version"]] = {"kind": "attr", "name": op["to_attribute"]}
        required_history = ameta.get("_required_history", {})
        effective_req = _effective_required(ameta.get("required", "0"), required_history)
        is_required = effective_req == "1"
        if is_required and ameta.get("default", "") != "":
            is_required = False
        params.append(ClassParam(
            py_name, hint, default, raw_default, to_expr, from_expr,
            ameta.get("description", ""), False, "attr", aname,
            init_default_expr, renames, added_in, removed_in, is_required, required_history,
            mod, raw_default
        ))

    for lname, lnode in sorted(leaf_items.items()):
        py_name = lname.replace("-", "_")
        required = lnode.get("_required", "0")
        is_list = required in ("*", "+")
        if is_list:
            py_name = make_plural(py_name)
        py_name = fix_keyword(py_name)
        if py_name in seen_py_names:
            continue
        seen_py_names.add(py_name)

        added_in = lnode.get("_added_in")
        removed_in = lnode.get("_removed_in")
        for op in applicable_ops:
            if op.get("type") == "remove" and op.get("element") == lname:
                if not removed_in or cmp_version(op["_version"], removed_in) < 0:
                    removed_in = op["_version"]
        lnode["_removed_in"] = removed_in

        hint, default, to_expr, from_expr, mod = resolve_type(lnode.get("_type"))
        raw_default = default
        init_default_expr = None
        if mod:
            type_imports[mod] = hint
        for fn in ("_parse_int32", "_parse_uint32", "_parse_double", "_parse_time"):
            if fn in from_expr:
                needs_helpers.add(fn)
        if mod and f"_parse_{mod}" in from_expr:
            custom_helpers.add(mod)

        schema_default = lnode.get("_default", "")
        if schema_default != "":
            raw_default = _format_default(hint, schema_default)
            if mod:
                default = "None"
                init_default_expr = f"_{mod}({raw_default})"
            else:
                default = raw_default
        item_raw_default = raw_default

        renames = {}
        for op in applicable_ops:
            if op.get("type") == "rename" and op.get("from_element") == lname and not op.get("from_attribute"):
                if op.get("to_element"):
                    renames[op["_version"]] = {"kind": "child", "name": op["to_element"]}
                elif op.get("to_attribute"):
                    renames[op["_version"]] = {"kind": "attr", "name": op["to_attribute"]}

        required_history = lnode.get("_required_history", {})
        effective_req = _effective_required(required, required_history)
        is_required = effective_req == "1" or effective_req == "+"
        if is_required and lnode.get("_default", "") != "":
            is_required = False

        if is_list:
            hint = f'List[{hint}]'
            default = "None"
            raw_default = "None"

        params.append(ClassParam(
            py_name, hint, default, raw_default, to_expr, from_expr,
            lnode.get("_description", ""), is_list, "child_leaf", lname,
            init_default_expr, renames, added_in, removed_in, is_required, required_history,
            mod, item_default=item_raw_default
        ))

    for cname, cnode in child_items.items():
        py_name = cname.replace("-", "_")
        required = cnode.get("_required", "0")
        is_list = required in ("*", "+")
        if is_list:
            py_name = make_plural(py_name)
        py_name = fix_keyword(py_name)
        if py_name in seen_py_names:
            continue
        seen_py_names.add(py_name)
        added_in = cnode.get("_added_in")
        removed_in = cnode.get("_removed_in")
        for op in applicable_ops:
            if op.get("type") == "remove" and op.get("element") == cname:
                if not removed_in or cmp_version(op["_version"], removed_in) < 0:
                    removed_in = op["_version"]
        cnode["_removed_in"] = removed_in
        child_cls = child_class_names.get(cname, _to_classname(cname))
        hint = f'List["{child_cls}"]' if is_list else f'"{child_cls}"'
        default = "None"
        desc = cnode.get("_description", "")
        renames = {}
        for op in applicable_ops:
            if op.get("type") == "rename" and op.get("from_element") == cname and not op.get("from_attribute"):
                if op.get("to_element"):
                    renames[op["_version"]] = {"kind": "child", "name": op["to_element"]}
                elif op.get("to_attribute"):
                    renames[op["_version"]] = {"kind": "attr", "name": op["to_attribute"]}
        required_history = cnode.get("_required_history", {})
        effective_req = _effective_required(required, required_history)
        is_required = effective_req == "1" or effective_req == "+"
        if is_required and cnode.get("_default", "") != "":
            is_required = False
        params.append(ClassParam(
            py_name, hint, default, default, "", "", desc,
            is_list, "child", cname, None, renames, added_in, removed_in, is_required, required_history,
            None, default
        ))

    if node.get("_type") and not child_items and not leaf_items:
        py_name = name.replace("-", "_")
        if py_name not in seen_py_names:
            seen_py_names.add(py_name)
            added_in = node.get("_added_in")
            hint, default, to_expr, from_expr, mod = resolve_type(node["_type"])
            raw_default = default
            init_default_expr = None
            if mod:
                type_imports[mod] = hint
            for fn in ("_parse_int32", "_parse_uint32", "_parse_double", "_parse_time"):
                if fn in from_expr:
                    needs_helpers.add(fn)
            if mod and f"_parse_{mod}" in from_expr:
                custom_helpers.add(mod)
            schema_default = node.get("_default", "")
            if schema_default != "":
                raw_default = _format_default(hint, schema_default)
                if mod:
                    default = "None"
                    init_default_expr = f"_{mod}({raw_default})"
                else:
                    default = raw_default
            renames = {}
            for op in applicable_ops:
                if op.get("type") == "rename" and op.get("from_element") == name and not op.get("from_attribute"):
                    if op.get("to_element"):
                        renames[op["_version"]] = {"kind": "leaf", "name": op["to_element"]}
                    elif op.get("to_attribute"):
                        renames[op["_version"]] = {"kind": "attr", "name": op["to_attribute"]}
            required_history = node.get("_required_history", {})
            effective_req = _effective_required(node.get("_required", "0"), required_history)
            is_required = effective_req == "1" or effective_req == "+"
            if is_required and node.get("_default", "") != "":
                is_required = False
            params.insert(0, ClassParam(
                name.replace("-", "_"), hint, default, raw_default, to_expr, from_expr,
                node.get("_description", ""), False, "leaf", name, init_default_expr, renames,
                added_in, node.get("_removed_in"), is_required, required_history, mod, raw_default
            ))

    class_migrations: dict[str, list] = {}
    for op in applicable_ops:
        if op.get("type") in ("move", "copy", "map"):
            v = op["_version"]
            if v not in class_migrations:
                class_migrations[v] = []
            mig_op = {"type": op["type"]}
            if op["type"] in ("move", "copy"):
                frm = op.get("from_element", "")
                if op.get("from_attribute"): frm += ("::" if frm else "") + op["from_attribute"]
                to = op.get("to_element", "")
                if op.get("to_attribute"): to += ("::" if to else "") + op["to_attribute"]
                mig_op["from"] = frm.replace("-", "_")
                mig_op["to"] = to.replace("-", "_")
            elif op["type"] == "map":
                mig_op["from"] = op.get("from_name", "").replace("-", "_").replace("/@", "::")
                mig_op["to"] = op.get("to_name", "").replace("-", "_").replace("/@", "::")
                mig_op["from_values"] = op.get("from_values", [])
                mig_op["to_value"] = op.get("to_value", "")
            class_migrations[v].append(mig_op)

    return {
        "class_name": class_name,
        "element_name": name,
        "params": sorted(params, key=lambda p: p.py_name),
        "type_imports": type_imports,
        "needs_helpers": needs_helpers,
        "_custom_helpers": list(custom_helpers),
        "external_imports": external_imports,
        "child_class_names": child_class_names,
        "child_specs": child_specs,
        "migrations": [{"version": k, "ops": v} for k, v in class_migrations.items()]
    }


def _indent_block(lines: list[str], spaces: int) -> list[str]:
    pad = " " * spaces
    return [pad + line if line.strip() else line for line in lines]


def _render_class(spec: dict, file_external_imports: set[str], indent: int = 0,
                  outer_prefix: str = "") -> str:
    name = spec["element_name"]
    class_name = spec["class_name"]
    params: list[ClassParam] = spec["params"]
    child_class_names = spec.get("child_class_names", {})
    child_specs: list[dict] = spec.get("child_specs", [])

    nested_child_xml_names: set[str] = {s["element_name"] for s in child_specs}

    my_prefix = f"{outer_prefix}{class_name}."

    def _nested_bare(xml_name: str) -> str:
        return child_class_names.get(xml_name, _to_classname(xml_name))

    def _qualified_cls(xml_name: str) -> str:
        bare = _nested_bare(xml_name)
        if "." in bare:
            return f"cls.{bare}"
        if xml_name in nested_child_xml_names:
            return f"cls.{bare}"
        return bare

    def _qualified_self(xml_name: str) -> str:
        bare = _nested_bare(xml_name)
        if "." in bare:
            return f"self.__class__.{bare}"
        if xml_name in nested_child_xml_names:
            return f"self.__class__.{bare}"
        return bare

    local_import_lines = []
    for p in params:
        xml_kind = p.kind
        xml_name = p.original_name
        if xml_kind == "child" and xml_name in file_external_imports:
            bare = child_class_names.get(xml_name, _to_classname(xml_name))
            if "." not in bare:
                module = _module_name_for(xml_name)
                cls_ = _to_classname(xml_name)
                line = f"        from ..elements.{module} import {cls_}"
                if line not in local_import_lines:
                    local_import_lines.append(line)

    block: list[str] = [
        f"class {class_name}(BaseModel):"
    ]

    if child_specs:
        for child_spec in child_specs:
            child_src = _render_class(
                child_spec,
                file_external_imports,
                indent=0,
                outer_prefix=my_prefix,
            )
            nested_lines = _indent_block(child_src.splitlines(), 4)
            block.extend(nested_lines)
            block.append("")

    def _qualified_hint(p: ClassParam) -> str:
        if p.kind != "child":
            return p.hint + " | None"
        bare = _nested_bare(p.original_name)
        if "." in bare:
            full = f"{my_prefix.split('.')[0]}.{bare}"
        elif p.original_name in nested_child_xml_names:
            full = f"{my_prefix}{bare}"
        else:
            full = bare
        if p.is_list:
            return f'List["{full}"]'
        return f'"{full}"'

    if spec.get("migrations"):
        migs = json.dumps(spec["migrations"])
        block.append(f"    _MIGRATIONS = {migs}")
        block.append("")

    init_params = ["self", "sdf_version: str | None = None"] + [
        f"{p.py_name}: {_qualified_hint(p)} = {p.default}" for p in params
    ]
    sig = ", ".join(init_params)
    if len(f"    def __init__({sig}):") > 100:
        block.append("    def __init__(")
        block.append("        self,")
        block.append("        sdf_version: str | None = None,")
        for i, p in enumerate(params):
            comma = "," if i < len(params) - 1 else ""
            block.append(f"        {p.py_name}: {_qualified_hint(p)} = {p.default}{comma}")
        block.append("    ):")
    else:
        block.append(f"    def __init__({sig}):")

    block.append("        super().__init__(sdf_version)")

    for p in params:
        if p.is_list and p.mod:
            block.append(
                f"        self.{p.py_name} = list(map(_{p.mod}, {p.py_name})) if {p.py_name} is not None else []")
        elif p.init_default_expr:
            if p.mod:
                block.append(
                    f"        self.{p.py_name} = {p.init_default_expr} if {p.py_name} is None else _{p.mod}({p.py_name})")
            else:
                block.append(
                    f"        self.{p.py_name} = {p.init_default_expr} if {p.py_name} is None else {p.py_name}")
        elif p.mod:
            block.append(f"        self.{p.py_name} = _{p.mod}({p.py_name})")
        elif p.raw_default != "None":
            block.append(f"        self.{p.py_name} = {p.py_name} if {p.py_name} is not None else {p.raw_default}")
        else:
            block.append(f"        self.{p.py_name} = {p.py_name}" + (" or []" if p.is_list else ""))

    for p in params:
        if p.kind == "child":
            if p.is_list:
                block.append(f"        for _i, _c in enumerate(self.{p.py_name}):")
                block.append(f"            if not hasattr(_c, 'to_version'): continue")
                block.append(f"            if getattr(_c, 'sdfversion', None) is None:")
                block.append(f"                _c.sdfversion = self.sdfversion")
                block.append(
                    f"            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:")
                block.append(f"                self.{p.py_name}[_i] = _c.to_version(self.sdfversion)")
            else:
                block.append(f"        if self.{p.py_name} is not None and hasattr(self.{p.py_name}, 'to_version'):")
                block.append(f"            if getattr(self.{p.py_name}, 'sdfversion', None) is None:")
                block.append(f"                self.{p.py_name}.sdfversion = self.sdfversion")
                block.append(
                    f"            elif getattr(self.{p.py_name}, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:")
                block.append(f"                self.{p.py_name} = self.{p.py_name}.to_version(self.sdfversion)")

    block.append("")

    for p in params:
        if p.is_list and p.kind in ("child", "child_leaf"):
            if p.kind == "child":
                bare = _nested_bare(p.original_name)
                if p.original_name in nested_child_xml_names:
                    full = f"{my_prefix}{bare}"
                else:
                    full = bare
                type_hint = f'"{full}"'
            else:
                inner_hint = p.hint
                if inner_hint.startswith("List["):
                    inner_hint = inner_hint[5:-1]
                type_hint = inner_hint

            singular_name = p.original_name.replace("-", "_")
            block.append(f'    def add_{singular_name}(self, *items: {type_hint}):')
            block.append(f"        if self.{p.py_name} is None:")
            block.append(f"            self.{p.py_name} = []")
            block.append(f"        self.{p.py_name}.extend(items)")
            block.append("")

    block.append(f'    def to_version(self, target_version: str) -> "{outer_prefix}{class_name}":')
    if local_import_lines:
        block.extend(local_import_lines)
    for p in params:
        if p.added_in:
            block.append(
                f"        if self.{p.py_name} is not None and cmp_version(target_version, \"{p.added_in}\") < 0:")
            block.append(
                f'            raise ValueError(f"\'{p.py_name}\' is not supported in SDF version {{target_version}} (added in {p.added_in})")')
        if p.removed_in:
            block.append(
                f"        if self.{p.py_name} is not None and cmp_version(target_version, \"{p.removed_in}\") >= 0:")
            block.append(
                f'            raise ValueError(f"\'{p.py_name}\' is not supported in SDF version {{target_version}} (removed in {p.removed_in})")')

    kwargs_init = '        kwargs: dict = {"sdf_version": target_version'
    for p in params:
        if p.kind == "child":
            if p.is_list:
                kwargs_init += f', "{p.py_name}": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.{p.py_name} or [])]'
            else:
                kwargs_init += f', "{p.py_name}": self.{p.py_name}.to_version(target_version) if self.{p.py_name} is not None and hasattr(self.{p.py_name}, "to_version") else self.{p.py_name}'
        else:
            kwargs_init += f', "{p.py_name}": self.{p.py_name}'
    block.append(kwargs_init + "}")
    if spec.get("migrations"):
        block.append("        new_obj = self.__class__(**kwargs)")
        block.append("        apply_migrations(new_obj, target_version)")
        block.append("        return new_obj")
    else:
        block.append("        return self.__class__(**kwargs)")

    block.append("")
    block.append("    def to_sdf(self, version: str | None = None) -> ET.Element:")
    if local_import_lines:
        block.extend(local_import_lines)
    block.append("        if self.sdfversion is None and version is not None:")
    block.append("            self.sdfversion = version")
    block.append("        elif version is not None and version != self.sdfversion:")
    block.append("            return self.to_version(str(version)).to_sdf()")
    block.append(f'        el = ET.Element("{name}")')
    for p in params:
        val_ref = f"self.{p.py_name}"
        if p.is_required:
            check_conds = []
            if p.added_in:
                check_conds.append(f'cmp_version(version, "{p.added_in}") >= 0')
            if p.removed_in:
                check_conds.append(f'cmp_version(version, "{p.removed_in}") < 0')
            sorted_history = sorted(
                p.required_history.items(),
                key=lambda x: tuple(int(v) for v in x[0].split("."))
            )
            required_since = None
            optional_since = None
            for v, req in sorted_history:
                if req in ("1", "+") and required_since is None:
                    required_since = v
                elif req in ("0", "*") and required_since is not None:
                    optional_since = v
                    break
            if optional_since:
                check_conds.append(f'cmp_version(version, "{optional_since}") < 0')
            elif required_since and required_since != BASE_VERSION:
                check_conds.append(f'cmp_version(version, "{required_since}") >= 0')
            if check_conds:
                cond = " and ".join(check_conds)
                block.append(f"        if {cond}:")
                indent_ = "            "
            else:
                indent_ = "        "
            if p.is_list:
                block.append(f"{indent_}if not self.{p.py_name}:")
                block.append(
                    f'{indent_}    raise ValueError(f"\'{p.py_name}\' is required in SDF version {{version}}")')
            elif p.kind == "child":
                block.append(f"{indent_}if self.{p.py_name} is None:")
                block.append(f'{indent_}    self.{p.py_name} = {_qualified_self(p.original_name)}(sdf_version=version)')
            elif p.kind == "child_leaf":
                block.append(f"{indent_}if self.{p.py_name} is None:")
                block.append(
                    f'{indent_}    raise ValueError(f"\'{p.py_name}\' is required in SDF version {{version}}")')
            else:
                block.append(f"{indent_}if self.{p.py_name} is None:")
                block.append(
                    f'{indent_}    raise ValueError(f"\'{p.py_name}\' is required in SDF version {{version}}")')

        if p.kind in ("attr", "leaf"):
            expr = p.to_expr.replace("{val}", val_ref)
            if not p.renames:
                block.append(f"        if self.{p.py_name} is not None:")
                if p.kind == "attr":
                    block.append(f'            el.set("{p.original_name}", {expr})')
                else:
                    block.append(f"            el.text = {expr}")
            else:
                block.append(f"        if self.{p.py_name} is not None:")
                sorted_versions = sorted(p.renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = p.renames[v]
                    if first:
                        block.append(f'            if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'            elif cmp_version(version, "{v}") >= 0:')
                    if loc["kind"] == "attr":
                        block.append(f'                el.set("{loc["name"]}", {expr})')
                    elif loc["kind"] == "text":
                        block.append(f'                el.text = {expr}')
                    else:
                        block.append(f'                _c_tmp = ET.Element("{loc["name"]}")')
                        block.append(f'                _c_tmp.text = {expr}')
                        block.append(f'                el.append(_c_tmp)')
                block.append(f'            else:')
                if p.kind == "attr":
                    block.append(f'                el.set("{p.original_name}", {expr})')
                else:
                    block.append(f"                el.text = {expr}")

        elif p.kind == "child_leaf":
            if p.is_list:
                block.append(f"        for _v in (self.{p.py_name} or []):")
                expr = p.to_expr.replace("{val}", "_v")
                indent2 = "            "
            else:
                block.append(f"        if self.{p.py_name} is not None:")
                expr = p.to_expr.replace("{val}", f"self.{p.py_name}")
                indent2 = "            "

            if not p.renames:
                block.append(f'{indent2}_c_tmp = ET.Element("{p.original_name}")')
                block.append(f'{indent2}_c_tmp.text = {expr}')
                block.append(f'{indent2}el.append(_c_tmp)')
            else:
                sorted_versions = sorted(p.renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = p.renames[v]
                    if first:
                        block.append(f'{indent2}if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'{indent2}elif cmp_version(version, "{v}") >= 0:')

                    if loc["kind"] == "attr":
                        block.append(f'{indent2}    el.set("{loc["name"]}", {expr})')
                    else:
                        block.append(f'{indent2}    _c_tmp = ET.Element("{loc["name"]}")')
                        block.append(f'{indent2}    _c_tmp.text = {expr}')
                        block.append(f'{indent2}    el.append(_c_tmp)')
                block.append(f'{indent2}else:')
                block.append(f'{indent2}    _c_tmp = ET.Element("{p.original_name}")')
                block.append(f'{indent2}    _c_tmp.text = {expr}')
                block.append(f'{indent2}    el.append(_c_tmp)')
        elif p.kind == "child":
            if p.is_list:
                block.append(f"        for item in (self.{p.py_name} or []):")
                block.append(f"            _child_res = item.to_sdf(version)")
                indent_child = "            "
            else:
                block.append(f"        if self.{p.py_name} is not None:")
                block.append(f"            _child_res = self.{p.py_name}.to_sdf(version)")
                indent_child = "            "

            block.append(f"{indent_child}if isinstance(_child_res, str):")
            block.append(f"{indent_child}    _item_el = ET.Element('{p.original_name}')")
            block.append(f"{indent_child}    _item_el.text = _child_res")
            block.append(f"{indent_child}else:")
            block.append(f"{indent_child}    _item_el = _child_res")

            if not p.renames:
                block.append(f"{indent_child}el.append(_item_el)")
            else:
                sorted_versions = sorted(p.renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = p.renames[v]
                    if first:
                        block.append(f'{indent_child}if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'{indent_child}elif cmp_version(version, "{v}") >= 0:')
                    block.append(f'{indent_child}    _item_el.tag = "{loc["name"]}"')
                block.append(f'{indent_child}else:')
                block.append(f'{indent_child}    _item_el.tag = "{p.original_name}"')
                block.append(f'{indent_child}el.append(_item_el)')
    block.append("        return el")

    block.append("")
    block.append("    @classmethod")
    block.append(f'    def _from_sdf(cls, el: ET.Element, version: str) -> "{outer_prefix}{class_name} | SDFError":')
    if local_import_lines:
        block.extend(local_import_lines)
    init_args: list[str] = ["sdf_version=version"]
    for p in params:
        if p.kind in ("attr", "leaf"):
            if p.is_required:
                check_conds = []
                if p.added_in:
                    check_conds.append(f'cmp_version(version, "{p.added_in}") >= 0')
                if p.removed_in:
                    check_conds.append(f'cmp_version(version, "{p.removed_in}") < 0')
                sorted_history = sorted(
                    p.required_history.items(),
                    key=lambda x: tuple(int(v) for v in x[0].split("."))
                )
                required_since = None
                optional_since = None
                for v, req in sorted_history:
                    if req in ("1", "+") and required_since is None:
                        required_since = v
                    elif req in ("0", "*") and required_since is not None:
                        optional_since = v
                        break
                if optional_since:
                    check_conds.append(f'cmp_version(version, "{optional_since}") < 0')
                elif required_since and required_since != BASE_VERSION:
                    check_conds.append(f'cmp_version(version, "{required_since}") >= 0')
                if check_conds:
                    cond = " and ".join(check_conds)
                    block.append(f"        if {cond}:")
                    indent_ = "            "
                else:
                    indent_ = "        "
                if p.kind == "attr":
                    block.append(f'{indent_}if el.get("{p.original_name}") is None:')
                else:
                    block.append(f'{indent_}if el.text is None:')
                block.append(f'{indent_}    return SDFError(f"\'{p.py_name}\' is required in SDF version {{version}}")')

            if not p.renames:
                if p.kind == "attr":
                    raw_expr = f'el.get("{p.original_name}", {p.raw_default})'
                    val_expr = p.from_expr.replace("{raw}", raw_expr)
                    block.append(f"        _{p.py_name} = {val_expr}")
                    block.append(f"        if isinstance(_{p.py_name}, SDFError):")
                    block.append(f'            return _{p.py_name}.extend("@{p.original_name}")')
                else:
                    block.append(f"        _text = el.text or {p.raw_default}")
                    val_expr = p.from_expr.replace("{raw}", "_text")
                    block.append(f"        _{p.py_name} = {val_expr}")
                    block.append(f"        if isinstance(_{p.py_name}, SDFError):")
                    block.append(f'            return _{p.py_name}')
            else:
                block.append(f"        _raw_{p.py_name} = None")
                sorted_versions = sorted(p.renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = p.renames[v]
                    if first:
                        block.append(f'        if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'        elif cmp_version(version, "{v}") >= 0:')
                    if loc["kind"] == "attr":
                        block.append(f'            _raw_{p.py_name} = el.get("{loc["name"]}")')
                    elif loc["kind"] == "text":
                        block.append(f'            _raw_{p.py_name} = el.text')
                    else:
                        block.append(f'            _c_tmp = el.find("{loc["name"]}")')
                        block.append(f'            if _c_tmp is not None: _raw_{p.py_name} = _c_tmp.text')
                block.append(f'        else:')
                if p.kind == "attr":
                    block.append(f'            _raw_{p.py_name} = el.get("{p.original_name}")')
                else:
                    block.append(f'            _c_tmp = el.find("{p.original_name}")')
                    block.append(f'            if _c_tmp is not None: _raw_{p.py_name} = _c_tmp.text')
                block.append(f'        if _raw_{p.py_name} is None: _raw_{p.py_name} = {p.raw_default}')
                val_expr = p.from_expr.replace("{raw}", f"_raw_{p.py_name}")
                block.append(f"        _{p.py_name} = {val_expr}")
                block.append(f"        if isinstance(_{p.py_name}, SDFError):")
                if p.kind == "attr":
                    block.append(f'            return _{p.py_name}.extend("@{p.original_name}")')
                else:
                    block.append(f'            return _{p.py_name}')

        elif p.kind == "child_leaf":
            if p.is_required:
                check_conds = []
                if p.added_in:
                    check_conds.append(f'cmp_version(version, "{p.added_in}") >= 0')
                if p.removed_in:
                    check_conds.append(f'cmp_version(version, "{p.removed_in}") < 0')
                sorted_history = sorted(
                    p.required_history.items(),
                    key=lambda x: tuple(int(v) for v in x[0].split("."))
                )
                required_since = None
                optional_since = None
                for v, req in sorted_history:
                    if req in ("1", "+") and required_since is None:
                        required_since = v
                    elif req in ("0", "*") and required_since is not None:
                        optional_since = v
                        break
                if optional_since:
                    check_conds.append(f'cmp_version(version, "{optional_since}") < 0')
                elif required_since and required_since != BASE_VERSION:
                    check_conds.append(f'cmp_version(version, "{required_since}") >= 0')
                if check_conds:
                    cond = " and ".join(check_conds)
                    block.append(f"        if {cond}:")
                    indent_ = "            "
                else:
                    indent_ = "        "

                block.append(f'{indent_}if el.find("{p.original_name}") is None:')
                block.append(f'{indent_}    return SDFError(f"\'{p.py_name}\' is required in SDF version {{version}}")')

            if not p.renames:
                if p.is_list:
                    block.append(f'        _{p.py_name} = []')
                    block.append(f'        for c in el.findall("{p.original_name}"):')
                    block.append(f'            _text = c.text if c.text is not None else {p.item_default}')
                    block.append(f'            _val = {p.from_expr.replace("{raw}", "_text")}')
                    block.append(f'            if isinstance(_val, SDFError):')
                    block.append(f'                return _val.extend("{p.original_name}")')
                    block.append(f'            _{p.py_name}.append(_val)')
                else:
                    block.append(f'        _c_tmp = el.find("{p.original_name}")')
                    block.append(f'        if _c_tmp is not None:')
                    block.append(f'            _text = _c_tmp.text if _c_tmp.text is not None else {p.item_default}')
                    block.append(f'            _val = {p.from_expr.replace("{raw}", "_text")}')
                    block.append(f'            if isinstance(_val, SDFError):')
                    block.append(f'                return _val.extend("{p.original_name}")')
                    block.append(f'            _{p.py_name} = _val')
                    block.append(f'        else:')
                    block.append(f'            _{p.py_name} = None')
            else:
                block.append(f'        _is_present = False')
                block.append(f'        _raw_{p.py_name} = None')
                if p.is_list:
                    block.append(f'        _els_{p.py_name} = []')
                sorted_versions = sorted(p.renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = p.renames[v]
                    if first:
                        block.append(f'        if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'        elif cmp_version(version, "{v}") >= 0:')

                    if loc["kind"] == "attr":
                        if p.is_list:
                            block.append(f'            _val_str = el.get("{loc["name"]}")')
                            block.append(f'            if _val_str is not None: _els_{p.py_name} = [(_val_str, True)]')
                        else:
                            block.append(f'            _val_str = el.get("{loc["name"]}")')
                            block.append(f'            if _val_str is not None:')
                            block.append(f'                _raw_{p.py_name} = _val_str')
                            block.append(f'                _is_present = True')
                    else:
                        if p.is_list:
                            block.append(
                                f'            _els_{p.py_name} = [(c.text, False) for c in el.findall("{loc["name"]}")]')
                        else:
                            block.append(f'            _c_tmp = el.find("{loc["name"]}")')
                            block.append(f'            if _c_tmp is not None:')
                            block.append(f'                _raw_{p.py_name} = _c_tmp.text')
                            block.append(f'                _is_present = True')
                block.append(f'        else:')
                if p.is_list:
                    block.append(
                        f'            _els_{p.py_name} = [(c.text, False) for c in el.findall("{p.original_name}")]')
                else:
                    block.append(f'            _c_tmp = el.find("{p.original_name}")')
                    block.append(f'            if _c_tmp is not None:')
                    block.append(f'                _raw_{p.py_name} = _c_tmp.text')
                    block.append(f'                _is_present = True')

                if p.is_list:
                    block.append(f'        _{p.py_name} = []')
                    block.append(f'        for _text, _is_attr in _els_{p.py_name}:')
                    block.append(f'            if _text is None: _text = {p.raw_default}')
                    block.append(f'            _val = {p.from_expr.replace("{raw}", "_text")}')
                    block.append(f'            if isinstance(_val, SDFError):')
                    block.append(
                        f'                return _val.extend("@attribute" if _is_attr else "{p.original_name}")')
                    block.append(f'            _{p.py_name}.append(_val)')
                else:
                    block.append(f'        if _is_present:')
                    block.append(f'            if _raw_{p.py_name} is None: _raw_{p.py_name} = {p.raw_default}')
                    block.append(f'            _{p.py_name} = {p.from_expr.replace("{raw}", f"_raw_{p.py_name}")}')
                    block.append(f'            if isinstance(_{p.py_name}, SDFError):')
                    block.append(f'                return _{p.py_name}.extend("{p.original_name}")')
                    block.append(f'        else:')
                    block.append(f'            _{p.py_name} = None')

        elif p.kind == "child":
            child_cls = _qualified_cls(p.original_name)
            if not p.renames:
                if p.is_list:
                    block.append(f'        _{p.py_name} = []')
                    block.append(f'        for c in el.findall("{p.original_name}"):')
                    block.append(f'            _res = {child_cls}._from_sdf(c, version)')
                    block.append(f'            if isinstance(_res, SDFError):')
                    block.append(f'                return _res.extend("{p.original_name}")')
                    block.append(f'            _{p.py_name}.append(_res)')
                else:
                    block.append(f'        _c_{p.py_name} = el.find("{p.original_name}")')
                    block.append(f'        if _c_{p.py_name} is not None:')
                    block.append(f'            _res = {child_cls}._from_sdf(_c_{p.py_name}, version)')
                    block.append(f'            if isinstance(_res, SDFError):')
                    block.append(f'                return _res.extend("{p.original_name}")')
                    block.append(f'            _{p.py_name} = _res')
                    if p.is_required:
                        block.append(f'        else:')
                        block.append(
                            f'            _res = {child_cls}._from_sdf(ET.Element("{p.original_name}"), version)')
                        block.append(f'            if isinstance(_res, SDFError):')
                        block.append(f'                return _res.extend("{p.original_name}")')
                        block.append(f'            _{p.py_name} = _res')
                    else:
                        block.append(f'        else:')
                        block.append(f'            _{p.py_name} = None')
            else:
                if p.is_list:
                    block.append(f'        _els_{p.py_name} = []')
                else:
                    block.append(f'        _c_{p.py_name} = None')
                sorted_versions = sorted(p.renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = p.renames[v]
                    if first:
                        block.append(f'        if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'        elif cmp_version(version, "{v}") >= 0:')
                    if p.is_list:
                        block.append(f'            _els_{p.py_name} = el.findall("{loc["name"]}")')
                    else:
                        block.append(f'            _c_{p.py_name} = el.find("{loc["name"]}")')
                block.append(f'        else:')
                if p.is_list:
                    block.append(f'            _els_{p.py_name} = el.findall("{p.original_name}")')
                else:
                    block.append(f'            _c_{p.py_name} = el.find("{p.original_name}")')
                if p.is_list:
                    block.append(f'        _{p.py_name} = []')
                    block.append(f'        for c in _els_{p.py_name}:')
                    block.append(f'            _res = {child_cls}._from_sdf(c, version)')
                    block.append(f'            if isinstance(_res, SDFError):')
                    block.append(f'                return _res.extend("{p.original_name}")')
                    block.append(f'            _{p.py_name}.append(_res)')
                else:
                    block.append(f'        if _c_{p.py_name} is not None:')
                    block.append(f'            _res = {child_cls}._from_sdf(_c_{p.py_name}, version)')
                    block.append(f'            if isinstance(_res, SDFError):')
                    block.append(f'                return _res.extend("{p.original_name}")')
                    block.append(f'            _{p.py_name} = _res')
                    if p.is_required:
                        block.append(f'        else:')
                        block.append(
                            f'            _res = {child_cls}._from_sdf(ET.Element("{p.original_name}"), version)')
                        block.append(f'            if isinstance(_res, SDFError):')
                        block.append(f'                return _res.extend("{p.original_name}")')
                        block.append(f'            _{p.py_name} = _res')
                    else:
                        block.append(f'        else:')
                        block.append(f'            _{p.py_name} = None')

        if p.is_required and p.kind == "child" and p.is_list:
            check_conds = []
            if p.added_in:
                check_conds.append(f'cmp_version(version, "{p.added_in}") >= 0')
            if p.removed_in:
                check_conds.append(f'cmp_version(version, "{p.removed_in}") < 0')
            sorted_history = sorted(
                p.required_history.items(),
                key=lambda x: tuple(int(v) for v in x[0].split("."))
            )
            required_since = None
            optional_since = None
            for v, req in sorted_history:
                if req in ("1", "+") and required_since is None:
                    required_since = v
                elif req in ("0", "*") and required_since is not None:
                    optional_since = v
                    break
            if optional_since:
                check_conds.append(f'cmp_version(version, "{optional_since}") < 0')
            elif required_since and required_since != BASE_VERSION:
                check_conds.append(f'cmp_version(version, "{required_since}") >= 0')
            if check_conds:
                cond = " and ".join(check_conds)
                block.append(f"        if {cond}:")
                indent_ = "            "
            else:
                indent_ = "        "
            block.append(f"{indent_}if not _{p.py_name}:")
            block.append(f'{indent_}    return SDFError(f"\'{p.py_name}\' is required in SDF version {{version}}")')

        if p.added_in:
            if p.is_list:
                block.append(f'        if _{p.py_name} and cmp_version(version, "{p.added_in}") < 0:')
                block.append(
                    f'            return SDFError(f"\'{p.py_name}\' is not supported in SDF version {{version}} (added in {p.added_in})")')
            else:
                block.append(f'        if _{p.py_name} is not None and cmp_version(version, "{p.added_in}") < 0:')
                if p.kind in ("attr", "leaf"):
                    block.append(f"            if _{p.py_name} != {p.raw_default}:")
                    block.append(
                        f'                return SDFError(f"\'{p.py_name}\' is not supported in SDF version {{version}} (added in {p.added_in})")')
                else:
                    block.append(
                        f'            return SDFError(f"\'{p.py_name}\' is not supported in SDF version {{version}} (added in {p.added_in})")')

        init_args.append(f"{p.py_name}=_{p.py_name}")

    if init_args:
        args_str = ", ".join(init_args)
        block.append(f"        return cls({args_str})")
    else:
        block.append('        return cls(sdf_version=version)')

    block.append("")

    if indent > 0:
        block = _indent_block(block, indent)

    return "\n".join(block)


def _walk_specs(spec: dict):
    yield spec
    for child in spec.get("child_specs", []):
        yield from _walk_specs(child)


def generate_element_file(
        element_name: str,
        node: dict,
        convert_ops: dict[str, list[dict]],
) -> str:
    defined: dict[str, str] = {}
    external_imports: set[str] = set()

    root_spec = _collect_class_spec(
        element_name, node, defined, convert_ops,
        external_imports=external_imports,
    )

    all_type_imports: dict[str, str] = {}
    needs_list = False
    needs_helpers: set[str] = set()
    needs_version_cmp = False

    all_custom_helpers: set[str] = set()

    for spec in _walk_specs(root_spec):
        if spec.get("_reuse"):
            continue
        all_type_imports.update(spec.get("type_imports", {}))
        if any("List[" in p.hint for p in spec.get("params", [])):
            needs_list = True

        spec_custom_helpers = spec.get("_custom_helpers", [])
        all_custom_helpers.update(spec_custom_helpers)

        for n in spec.get("needs_helpers", []):
            needs_helpers.add(n)
        if any(len(p.renames) > 0 or p.added_in or p.removed_in for p in spec.get("params", [])):
            needs_version_cmp = True

    lines: list[str] = [
        "### THIS FILE WAS AUTO-GENERATED ###",
        "from __future__ import annotations",
        "",
        "from xml.etree import ElementTree as ET",
        "",
    ]

    if needs_helpers:
        lines.append(f"from ..utils.utils import {', '.join(sorted(needs_helpers))}")

    if external_imports:
        lines.append("import typing")

    if needs_list:
        lines.append("from typing import List")
        lines.append("")

    lines.append("from ..utils.model import BaseModel")
    lines.append("from ..utils.errors import SDFError")

    for mod, cls in sorted(all_type_imports.items()):
        class_name = _to_classname(mod)
        lines.append(f"from ..utils.{mod} import _{class_name}T, _{mod}")

    if needs_version_cmp:
        lines.append("from ..utils.version import cmp_version")

    if any(s.get("migrations") for s in _walk_specs(root_spec) if not s.get("_reuse")):
        lines.append("from ..utils.migration import apply_migrations")

    lines.append("")

    if external_imports:
        lines.append("if typing.TYPE_CHECKING:")
        for ext in sorted(external_imports):
            if ext == element_name:
                continue
            module = _module_name_for(ext)
            cls = _to_classname(ext)
            lines.append(f"    from ..elements.{module} import {cls}")
        lines.append("")

    for mod in sorted(all_custom_helpers):
        class_name = _to_classname(mod)
        lines.append(f"def _parse_{mod}(raw: str) -> _{class_name}T | SDFError:")
        lines.append(f"    try:")
        lines.append(f"        return _{mod}(raw)")
        lines.append(f"    except ValueError as e:")
        lines.append(f"        return SDFError(str(e))")
        lines.append("")

    lines.append("")

    if not root_spec.get("_reuse"):
        lines.append("# noinspection PyUnusedImports")
        lines.append(_render_class(root_spec, external_imports, indent=0))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def generate_init(element_names: list[str]) -> str:
    lines = [
        "### THIS FILE WAS AUTO-GENERATED ###",
        "from __future__ import annotations",
        ""
    ]
    for element in sorted(element_names):
        root_cls = _to_classname(element)
        lines.append(f"from .{_module_name_for(element)} import {root_cls}")
    lines.append("")
    element_list = ", ".join(f'"{t}"' for t in sorted(element_names))
    lines.append(f"ELEMENT_NAMES: list[str] = [{element_list}]")
    lines.append("")
    lines.append("ELEMENT_CLASS_MAP: dict[str, type] = {")
    for element in sorted(element_names):
        cls = _to_classname(element)
        lines.append(f'    "{element}": {cls},')
    lines.append("}")
    lines.append("")
    lines.append("def get_element_class(element: str) -> type | None:")
    lines.append("    return ELEMENT_CLASS_MAP.get(element)")
    lines.append("")
    return "\n".join(lines)


def main():
    clone_or_pull()

    versions = available_versions()
    if not versions:
        exit("No SDF versions found in cloned repo.")

    print(f"\n=== Parsing all SDF versions ===")
    base_schema = parse_all_versions()
    base_elements = set(base_schema.keys())
    print(f"  Found {len(base_elements)} elements: {sorted(base_elements)}")

    all_convert_ops: dict[str, list[dict]] = {}
    for v in versions:
        if v == BASE_VERSION:
            continue
        ops = parse_convert_file(v)
        all_convert_ops[v] = ops
        if ops:
            print(f"  {v}: {len(ops)} convert operations")
        else:
            print(f"  {v}: no meaningful convert operations")

    new_elements: set[str] = set()
    for v, ops in all_convert_ops.items():
        for op in ops:
            path_parts = [p for p in str(op.get("path", "")).split("/") if p]
            if path_parts:
                root_element = path_parts[0]
                if root_element not in ("gazebo", "sdf") and root_element not in base_elements:
                    new_elements.add(root_element)
                    print(f"  [info] New element '{root_element}' introduced in version {v}")
    if new_elements:
        print(f"  New elements found (not in base): {sorted(new_elements)}")

    print(f"\n=== Generating Python modules ===")

    if SDF_SRC_DIR.exists():
        for child in list(SDF_SRC_DIR.iterdir()):
            if child.is_dir() and child.name.startswith("sdf"):
                shutil.rmtree(child)
                print(f"  Removed old {child.name}/")
            elif child.is_file() and child.suffix == ".py" and child.name != "__init__.py":
                child.unlink()
    SDF_SRC_DIR.mkdir(parents=True, exist_ok=True)

    element_names: list[str] = []
    for element_name, node in sorted(base_schema.items()):
        if not isinstance(node, dict):
            continue
        element_names.append(element_name)
        py_src = generate_element_file(element_name, node, all_convert_ops)
        out_path = SDF_SRC_DIR / f"{_module_name_for(element_name)}.py"
        out_path.write_text(py_src, encoding="utf-8")
        out_el_path = ELEMENTS_SRC_DIR / f"{_module_name_for(element_name)}.py"
        if not out_el_path.exists():
            out_el_path.write_text(
                f"""from .._sdf.{_module_name_for(element_name)} import {_to_classname(element_name)} as _{_to_classname(element_name)}


class {_to_classname(element_name)}(_{_to_classname(element_name)}):
    pass
""",
                encoding="utf-8")
        print(f"  Wrote {out_path}")

    init_path = SDF_SRC_DIR / "__init__.py"
    init_path.write_text(generate_init(element_names), encoding="utf-8")
    print(f"  Wrote {init_path}")
    init_elements_path = ELEMENTS_SRC_DIR / "__init__.py"
    init_elements_path.write_text(generate_init(element_names), encoding="utf-8")
    print(f"  Wrote {init_elements_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
