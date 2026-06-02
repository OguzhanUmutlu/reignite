from math import isfinite, inf
from typing import Union

from .errors import SDFError

INT32_MIN = -(2 ** 31)
INT32_MAX = 2 ** 31 - 1
UINT32_MAX = 2 ** 32 - 1


def _parse_int32(raw) -> Union[int, SDFError]:
    try:
        v = int(raw)
        if not (INT32_MIN <= v <= INT32_MAX):
            return SDFError(f"int32 out of range: {{v}}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {{raw}}")


def _parse_uint32(raw) -> Union[int, SDFError]:
    try:
        v = int(raw)
        if not (0 <= v <= UINT32_MAX):
            return SDFError(f"uint32 out of range: {{v}}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {{raw}}")


def _parse_double(raw) -> Union[float, SDFError]:
    try:
        v = float(raw)
        if not isfinite(v) or abs(v) > inf:
            return SDFError(f"double out of range: {{raw}}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {{raw}}")


def _parse_time(raw) -> Union[float, SDFError]:
    try:
        sec, nsec = (int(x) for x in raw.split())
        if not isfinite(sec) or not isfinite(nsec) or abs(sec) > inf or abs(nsec) > inf:
            return SDFError(f"double out of range: {{raw}}")
        if sec < 0 or nsec < 0 or nsec >= 1e9:
            return SDFError(f"Invalid time: {{raw}}")
        return sec + nsec * 1e-9
    except ValueError:
        return SDFError(f"Invalid time: {{raw}}")
