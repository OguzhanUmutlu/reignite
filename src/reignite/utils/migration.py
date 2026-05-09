import sys
import typing


def _get_path(obj, path: str):
    parts = path.split("::")
    current = obj
    for part in parts:
        if current is None:
            return None
        # Handle lists gracefully: we just use the first item for migrations.
        if isinstance(current, list):
            if not current:
                return None
            current = current[0]
        current = getattr(current, part, None)
    return current


def _set_path(obj, path: str, value):
    parts = path.split("::")
    current = obj
    for part in parts[:-1]:
        val = getattr(current, part, None)
        if val is None:
            mod = sys.modules[current.__module__]
            hints = typing.get_type_hints(type(current).__init__, globalns=mod.__dict__)
            cls = hints.get(part)
            if not cls:
                # If no type hint (e.g. primitive), we can't instantiate
                return
            if typing.get_origin(cls) == list:
                cls = typing.get_args(cls)[0]
                new_val = [cls(sdf_version=obj.__version__)]
            else:
                new_val = cls(sdf_version=obj.__version__)
            setattr(current, part, new_val)
            if isinstance(new_val, list):
                current = new_val[0]
            else:
                current = new_val
        else:
            if isinstance(val, list):
                if not val:
                    # Instantiate empty list item
                    mod = sys.modules[current.__module__]
                    hints = typing.get_type_hints(type(current).__init__, globalns=mod.__dict__)
                    cls = typing.get_args(hints[part])[0]
                    val.append(cls(sdf_version=obj.__version__))
                current = val[0]
            else:
                current = val
    # Handle the leaf
    leaf_part = parts[-1]
    if isinstance(current, list) and current:
        current = current[0]
    setattr(current, leaf_part, value)


def apply_migrations(obj, target_version: str):
    """
    Applies migrations defined in obj._MIGRATIONS to migrate obj to target_version.
    Mutates obj in place.
    """
    from .version import cmp_version
    current_version = getattr(obj, "__version__", "1.0")
    if current_version == target_version:
        return

    migrations = getattr(obj, "_MIGRATIONS", [])
    if not migrations:
        return

    forward = cmp_version(target_version, current_version) > 0

    # Sort migrations. If forward, sort ascending. If backward, sort descending.
    sorted_migrations = sorted(
        migrations,
        key=lambda m: tuple(int(x) for x in m["version"].split(".")),
        reverse=not forward
    )

    for mig in sorted_migrations:
        v = mig["version"]
        # If moving forward, we apply migration if we are crossing its boundary.
        # Boundary is when target >= v AND current < v
        if forward:
            if cmp_version(target_version, v) >= 0 and cmp_version(current_version, v) < 0:
                for op in mig["ops"]:
                    if op["type"] == "move":
                        val = _get_path(obj, op["from"])
                        if val is not None:
                            _set_path(obj, op["to"], val)
                            _set_path(obj, op["from"], None)
                    elif op["type"] == "copy":
                        val = _get_path(obj, op["from"])
                        if val is not None:
                            _set_path(obj, op["to"], val)
                    elif op["type"] == "map":
                        val = _get_path(obj, op["from"])
                        if val in op["from_values"]:
                            _set_path(obj, op["to"], op["to_value"])
        # If moving backward, we cross boundary if target < v AND current >= v
        else:
            if cmp_version(target_version, v) < 0 and cmp_version(current_version, v) >= 0:
                # Reverse ops
                for op in reversed(mig["ops"]):
                    if op["type"] == "move":
                        val = _get_path(obj, op["to"])
                        if val is not None:
                            _set_path(obj, op["from"], val)
                            _set_path(obj, op["to"], None)
                    elif op["type"] == "map":
                        val = _get_path(obj, op["to"])
                        if val == op["to_value"]:
                            # We can only restore the first from_value since we lost the original
                            _set_path(obj, op["from"], op["from_values"][0])
