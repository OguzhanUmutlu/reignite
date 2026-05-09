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
SDF_SRC_DIR = SRC_DIR / "sdf"
ELEMENTS_SRC_DIR = SRC_DIR / "elements"

SDF_REPO_URL = "https://github.com/gazebosim/sdformat.git"

BASE_VERSION = "1.0"

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

INT32_MIN = -(2 ** 31)
INT32_MAX = 2 ** 31 - 1
UINT32_MAX = 2 ** 32 - 1

INT_HELPERS = f'''\
import math

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
    if not math.isfinite(v) or abs(v) > math.inf:
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


def union_schema(base: dict, new: dict, version: str):
    for k in ("_description", "_type", "_default", "_required"):
        if k in new and k not in base:
            base[k] = new[k]

    if "_attributes" in new:
        if "_attributes" not in base:
            base["_attributes"] = {}
        for aname, ameta in new["_attributes"].items():
            if aname not in base["_attributes"]:
                ameta["_added_in"] = version
                base["_attributes"][aname] = ameta

    if "_includes" in new:
        if "_includes" not in base:
            base["_includes"] = []
        for inc in new["_includes"]:
            if inc not in base["_includes"]:
                base["_includes"].append(inc)

    child_keys = [k for k in new.keys() if not k.startswith("_")]
    for cname in child_keys:
        if cname not in base:
            base[cname] = dict(new[cname])
            base[cname]["_added_in"] = version
        else:
            union_schema(base[cname], new[cname], version)


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
                schema[name] = parse_element(root, files)
            else:
                for child in root.findall("element"):
                    name = child.get("name", "")
                    if name:
                        schema[name] = parse_element(child, files)
        union_schema(base_schema, schema, version if version != BASE_VERSION else None)
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
            op = {"type": "rename", "path": current_path}
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
            op = {"type": "map", "path": current_path}
            op["from_name"] = frm.get("name")
            op["from_values"] = [v.text for v in frm.findall("value")]
            op["to_name"] = to.get("name")
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


def _collect_classes(
        name: str,
        node: dict,
        class_specs: list[dict],
        defined: set[str],
        all_convert_ops: dict[str, list[dict]],
):
    class_name = _to_classname(name)
    if class_name in defined:
        return
    defined.add(class_name)

    applicable_ops = []
    for v, ops in all_convert_ops.items():
        for op in ops:
            leaf = op.get("path", "").split("/")[-1]
            if leaf == name:
                op_copy = dict(op)
                op_copy["_version"] = v
                applicable_ops.append(op_copy)

    child_items = {k: v for k, v in node.items()
                   if not k.startswith("_") and isinstance(v, dict)}

    for cname, cnode in child_items.items():
        _collect_classes(cname, cnode, class_specs, defined, all_convert_ops)

    params: list[tuple] = []
    type_imports: dict[str, str] = {}
    needs_int_helpers = False
    needs_float_helpers = False
    child_class_names = [_to_classname(cname) for cname in child_items.keys()]
    seen_py_names = set()

    for aname, ameta in (node.get("_attributes") or {}).items():
        py_name = aname.replace("-", "_")
        if py_name in seen_py_names: continue
        seen_py_names.add(py_name)
        added_in = ameta.get("_added_in")

        removed_in = None
        for op in applicable_ops:
            if op.get("type") == "remove" and op.get("attribute") == aname:
                removed_in = op["_version"]

        ameta["_removed_in"] = removed_in
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
        renames = {}
        for op in applicable_ops:
            if op.get("type") == "rename" and op.get("from_attribute") == aname and not op.get("from_element"):
                if op.get("to_element"):
                    renames[op["_version"]] = {"kind": "leaf", "name": op["to_element"]}
                elif op.get("to_attribute"):
                    renames[op["_version"]] = {"kind": "attr", "name": op["to_attribute"]}
        params.append((
            py_name, hint, default, raw_default, to_expr, from_expr,
            ameta.get("description", ""), False, "attr", aname, init_default_expr, renames, added_in,
            ameta.get("_removed_in")
        ))

    for cname, cnode in child_items.items():
        py_name = cname.replace("-", "_")
        if py_name in seen_py_names: continue
        seen_py_names.add(py_name)
        added_in = cnode.get("_added_in")

        removed_in = None
        for op in applicable_ops:
            if op.get("type") == "remove" and op.get("element") == cname:
                removed_in = op["_version"]

        cnode["_removed_in"] = removed_in
        child_cls = _to_classname(cname)
        required = cnode.get("_required", "0")
        is_list = required in ("*", "+")
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
        params.append((
            py_name, hint, default, default, "", "", desc,
            is_list, "child", cname, None, renames, added_in, cnode.get("_removed_in")
        ))

    if node.get("_type") and not child_items:
        py_name = name.replace("-", "_")
        if py_name not in seen_py_names:
            seen_py_names.add(py_name)
            added_in = node.get("_added_in")
            hint, default, to_expr, from_expr, mod = resolve_type(node["_type"])
        raw_default = default
        init_default_expr = None
        if mod:
            type_imports[mod] = hint
        if "_parse_int32" in from_expr or "_parse_uint32" in from_expr:
            needs_int_helpers = True
        if "_parse_double" in from_expr:
            needs_float_helpers = True
        schema_default = node.get("_default", "")
        if schema_default != "":
            raw_default = _format_default(hint, schema_default)
            if mod:
                default = "None"
                init_default_expr = f"{hint}.from_sdf({raw_default})"
            else:
                default = raw_default
        renames = {}
        for op in applicable_ops:
            if op.get("type") == "rename" and op.get("from_element") == name and not op.get("from_attribute"):
                if op.get("to_element"):
                    renames[op["_version"]] = {"kind": "leaf", "name": op["to_element"]}
                elif op.get("to_attribute"):
                    renames[op["_version"]] = {"kind": "attr", "name": op["to_attribute"]}
        params = [(
            name.replace("-", "_"), hint, default, raw_default, to_expr, from_expr,
            node.get("_description", ""), False, "leaf", name, init_default_expr, renames, added_in, None
        )] + params

    class_migrations = {}
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

    formatted_migrations = [{"version": k, "ops": v} for k, v in class_migrations.items()]

    class_specs.append({
        "migrations": formatted_migrations,
        "class_name": class_name,
        "element_name": name,
        "params": params,
        "type_imports": type_imports,
        "needs_int_helpers": needs_int_helpers,
        "needs_float_helpers": needs_float_helpers,
        "child_class_names": child_class_names,
    })


def _render_class(spec: dict) -> str:
    name = spec["element_name"]
    class_name = spec["class_name"]
    params = spec["params"]

    block: list[str] = [f"class {class_name}(Model):"]

    if spec.get("migrations"):
        import json
        migs = json.dumps(spec["migrations"])
        block.append(f"    _MIGRATIONS = {migs}")
        block.append("")

    init_params = ["self", "sdf_version: str"] + [
        f"{p[0]}: {p[1]} = {p[2]}" for p in params
    ]
    sig = ", ".join(init_params)
    if len(f"    def __init__({sig}):") > 100:
        block.append("    def __init__(")
        block.append("        self,")
        block.append("        sdf_version: str,")
        for i, p in enumerate(params):
            comma = "," if i < len(params) - 1 else ""
            block.append(f"        {p[0]}: {p[1]} = {p[2]}{comma}")
        block.append("    ):")
    else:
        block.append(f"    def __init__({sig}):")

    if not params:
        block.append("        self.__version__ = sdf_version")
    else:
        block.append("        self.__version__ = sdf_version")
        for p in params:
            py_name = p[0]
            init_default_expr = p[10]
            if init_default_expr:
                block.append(f"        if {py_name} is None:")
                block.append(f"            {py_name} = {init_default_expr}")

        for p in params:
            py_name, _, _, _, _, _, _, is_list, _, _, _, _, _, _ = p
            block.append(
                f"        self.{py_name} = {py_name}" + (" or []" if is_list else "")
            )

    block.append("")
    block.append(f'    def to_version(self, target_version: str) -> "{class_name}":')
    for p in params:
        py_name, _, _, _, _, _, _, is_list, xml_kind, _, _, _, added_in, removed_in = p
        if added_in:
            block.append(f"        if self.{py_name} is not None and cmp_version(target_version, \"{added_in}\") < 0:")
            block.append(
                f'            raise ValueError(f"\'{py_name}\' is not supported in SDF version {{target_version}} (added in {added_in})")')

    block.append('        kwargs = {"sdf_version": target_version}')
    for p in params:
        py_name, _, _, _, _, _, _, is_list, xml_kind, _, _, _, _, _ = p
        if xml_kind == "child":
            if is_list:
                block.append(
                    f'        kwargs["{py_name}"] = [c.to_version(target_version) for c in (self.{py_name} or [])]')
            else:
                block.append(
                    f'        kwargs["{py_name}"] = self.{py_name}.to_version(target_version) if self.{py_name} is not None else None')
        else:
            block.append(f'        kwargs["{py_name}"] = self.{py_name}')
    block.append("        new_obj = self.__class__(**kwargs)")
    if spec.get("migrations"):
        block.append("        apply_migrations(new_obj, target_version)")
    block.append("        return new_obj")

    block.append("")
    block.append("    def to_sdf(self, version: str = None) -> ET.Element:")
    block.append("        if version is not None and version != self.__version__:")
    block.append("            return self.to_version(version).to_sdf()")
    block.append("        version = version or self.__version__")
    block.append(f'        el = ET.Element("{name}")')
    for p in params:
        py_name, _, _, _, to_expr, _, _, is_list, xml_kind, xml_name, _, renames, _, _ = p
        val_ref = f"self.{py_name}"
        if xml_kind in ("attr", "leaf"):
            expr = to_expr.replace("{val}", val_ref)
            if not renames:
                block.append(f"        if self.{py_name} is not None:")
                if xml_kind == "attr":
                    block.append(f'            el.set("{xml_name}", {expr})')
                else:
                    block.append(f"            el.text = {expr}")
            else:
                block.append(f"        if self.{py_name} is not None:")
                sorted_versions = sorted(renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = renames[v]
                    if first:
                        block.append(f'            if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'            elif cmp_version(version, "{v}") >= 0:')
                    if loc["kind"] == "attr":
                        block.append(f'                el.set("{loc["name"]}", {expr})')
                    else:
                        block.append(f'                _c_tmp = ET.Element("{loc["name"]}")')
                        block.append(f'                _c_tmp.text = {expr}')
                        block.append(f'                el.append(_c_tmp)')
                block.append(f'            else:')
                if xml_kind == "attr":
                    block.append(f'                el.set("{xml_name}", {expr})')
                else:
                    block.append(f"                el.text = {expr}")
        elif xml_kind == "child":
            if not renames:
                if is_list:
                    block.append(f"        for item in (self.{py_name} or []):")
                    block.append("            el.append(item.to_sdf(version))")
                else:
                    block.append(f"        if self.{py_name} is not None:")
                    block.append(f"            el.append(self.{py_name}.to_sdf(version))")
            else:
                if is_list:
                    block.append(f"        for item in (self.{py_name} or []):")
                    block.append("            _item_el = item.to_sdf(version)")
                else:
                    block.append(f"        if self.{py_name} is not None:")
                    block.append(f"            _item_el = self.{py_name}.to_sdf(version)")

                sorted_versions = sorted(renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = renames[v]
                    if first:
                        block.append(f'            if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'            elif cmp_version(version, "{v}") >= 0:')
                    block.append(f'                _item_el.tag = "{loc["name"]}"')
                block.append(f'            else:')
                block.append(f'                _item_el.tag = "{xml_name}"')
                block.append(f'            el.append(_item_el)')
    block.append("        return el")

    block.append("")
    block.append("    @classmethod")
    block.append(
        f'    def from_sdf(cls, el: ET.Element, version: str) -> "{class_name}":'
    )
    init_args: list[str] = ["sdf_version=version"]
    for p in params:
        py_name, _, _, raw_default, _, from_expr, _, is_list, xml_kind, xml_name, _, renames, added_in, removed_in = p
        if xml_kind in ("attr", "leaf"):
            if not renames:
                if xml_kind == "attr":
                    raw_expr = f'el.get("{xml_name}", {raw_default})'
                    val_expr = from_expr.replace("{raw}", raw_expr)
                    block.append(f"        _{py_name} = {val_expr}")
                else:
                    block.append(f"        _text = el.text or {raw_default}")
                    val_expr = from_expr.replace("{raw}", "_text")
                    block.append(f"        _{py_name} = {val_expr}")
            else:
                block.append(f"        _raw_{py_name} = None")
                sorted_versions = sorted(renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = renames[v]
                    if first:
                        block.append(f'        if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'        elif cmp_version(version, "{v}") >= 0:')

                    if loc["kind"] == "attr":
                        block.append(f'            _raw_{py_name} = el.get("{loc["name"]}")')
                    else:
                        block.append(f'            _c_tmp = el.find("{loc["name"]}")')
                        block.append(f'            if _c_tmp is not None: _raw_{py_name} = _c_tmp.text')

                block.append(f'        else:')
                if xml_kind == "attr":
                    block.append(f'            _raw_{py_name} = el.get("{xml_name}")')
                else:
                    block.append(f'            _c_tmp = el.find("{xml_name}")')
                    block.append(f'            if _c_tmp is not None: _raw_{py_name} = _c_tmp.text')

                block.append(f'        if _raw_{py_name} is None: _raw_{py_name} = {raw_default}')
                val_expr = from_expr.replace("{raw}", f"_raw_{py_name}")
                block.append(f"        _{py_name} = {val_expr}")

        elif xml_kind == "child":
            child_cls = _to_classname(xml_name)
            if not renames:
                if is_list:
                    block.append(
                        f'        _{py_name} = [{child_cls}.from_sdf(c, version) '
                        f'for c in el.findall("{xml_name}")]'
                    )
                else:
                    block.append(f'        _c_{py_name} = el.find("{xml_name}")')
                    block.append(
                        f"        _{py_name} = {child_cls}.from_sdf(_c_{py_name}, version) "
                        f"if _c_{py_name} is not None else None"
                    )
            else:
                if is_list:
                    block.append(f'        _els_{py_name} = []')
                else:
                    block.append(f'        _c_{py_name} = None')

                sorted_versions = sorted(renames.keys(), key=lambda v: tuple(int(x) for x in v.split(".")),
                                         reverse=True)
                first = True
                for v in sorted_versions:
                    loc = renames[v]
                    if first:
                        block.append(f'        if cmp_version(version, "{v}") >= 0:')
                        first = False
                    else:
                        block.append(f'        elif cmp_version(version, "{v}") >= 0:')

                    if is_list:
                        block.append(f'            _els_{py_name} = el.findall("{loc["name"]}")')
                    else:
                        block.append(f'            _c_{py_name} = el.find("{loc["name"]}")')

                block.append(f'        else:')
                if is_list:
                    block.append(f'            _els_{py_name} = el.findall("{xml_name}")')
                else:
                    block.append(f'            _c_{py_name} = el.find("{xml_name}")')

                if is_list:
                    block.append(f'        _{py_name} = [{child_cls}.from_sdf(c, version) for c in _els_{py_name}]')
                else:
                    block.append(
                        f"        _{py_name} = {child_cls}.from_sdf(_c_{py_name}, version) "
                        f"if _c_{py_name} is not None else None"
                    )
        if added_in:
            if is_list:
                block.append(f"        if _{py_name} and cmp_version(version, \"{added_in}\") < 0:")
                block.append(
                    f'            raise ValueError(f"\'{py_name}\' is not supported in SDF version {{version}} (added in {added_in})")')
            else:
                block.append(f"        if _{py_name} is not None and cmp_version(version, \"{added_in}\") < 0:")
                if xml_kind in ("attr", "leaf"):
                    block.append(f"            if _{py_name} != {raw_default}:")
                    block.append(
                        f'                raise ValueError(f"\'{py_name}\' is not supported in SDF version {{version}} (added in {added_in})")')
                else:
                    block.append(
                        f'            raise ValueError(f"\'{py_name}\' is not supported in SDF version {{version}} (added in {added_in})")')
        init_args.append(f"{py_name}=_{py_name}")

    if init_args:
        args_str = ", ".join(init_args)
        block.append(f"        return cls({args_str})")
    else:
        block.append('        return cls(sdf_version=version)')

    block.append("")
    return "\n".join(block)


def generate_element_file(
        element_name: str,
        node: dict,
        convert_ops: dict[str, list[dict]],
) -> str:
    class_specs: list[dict] = []
    defined: set[str] = set()
    _collect_classes(element_name, node, class_specs, defined, convert_ops)

    all_type_imports: dict[str, str] = {}
    needs_list = False
    needs_helpers = False
    needs_version_cmp = False

    for spec in class_specs:
        all_type_imports.update(spec["type_imports"])
        if any("List[" in p[1] for p in spec["params"]):
            needs_list = True
        if spec["needs_int_helpers"] or spec["needs_float_helpers"]:
            needs_helpers = True
        if any(len(p[11]) > 0 or p[12] for p in spec["params"]):
            needs_version_cmp = True

    lines: list[str] = [
        "### THIS FILE WAS AUTO-GENERATED ###",
        "from __future__ import annotations",
        "",
        "from xml.etree import ElementTree as ET",
        "",
    ]

    if needs_list:
        lines.append("from typing import List")
        lines.append("")

    lines.append("from ..utils.model import Model")

    for mod, cls in sorted(all_type_imports.items()):
        lines.append(f"from ..utils.{mod} import {cls}")

    if needs_version_cmp:
        lines.append("from ..utils.version import cmp_version")

    if spec.get("migrations"):
        lines.append("from ..utils.migration import apply_migrations")

    lines.append("")

    if needs_helpers:
        lines.append("")
        lines.append(INT_HELPERS)

    lines.append("")

    for spec in class_specs:
        lines.append(_render_class(spec))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def generate_init(element_names: list[str]) -> str:
    lines = ["from __future__ import annotations", ""]
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

    print(f"\n=== Parsing base version {BASE_VERSION} ===")
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
            path_parts = [p for p in op.get("path", "").split("/") if p]
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
            out_el_path.write_text(f"""from ..sdf.{_module_name_for(element_name)} import {_to_classname(element_name)} as _Base

class {_to_classname(element_name)}(_Base):
    pass
""", encoding="utf-8")
        print(f"  Wrote {out_path}")

    init_path = SDF_SRC_DIR / "__init__.py"
    init_path.write_text(generate_init(element_names), encoding="utf-8")
    print(f"  Wrote {init_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
