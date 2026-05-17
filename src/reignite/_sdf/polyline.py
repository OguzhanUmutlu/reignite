### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector2d import Vector2d as _SDFVector2d, _Vector2dT, _vector2d


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")


def _parse_vector2d(raw: str) -> _Vector2dT | SDFError:
    try:
        return _vector2d(raw)
    except ValueError as e:
        return SDFError(str(e))


class Polyline(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        height: float = 1.0,
        points: List[_Vector2dT] = None
    ):
        super().__init__(sdf_version)
        if points is None:
            points = _vector2d("0 0")
        else:
            points = _vector2d(points)
        self.height = height
        self.points = points or []

    def add_point(self, *items: _Vector2dT):
        if self.points is None:
            self.points = []
        self.points.extend(items)

    def to_version(self, target_version: str) -> "Polyline":
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height
        kwargs["points"] = self.points
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("polyline")
        if self.height is not None:
            _c_tmp = ET.Element("height")
            _c_tmp.text = str(self.height)
            el.append(_c_tmp)
        for _v in (self.points or []):
            _c_tmp = ET.Element("point")
            _c_tmp.text = str(_v)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Polyline | SDFError":
        _c_tmp = el.find("height")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("height")
            _height = _val
        else:
            _height = None
        _points = []
        for c in el.findall("point"):
            _text = c.text if c.text is not None else "0 0"
            _val = _parse_vector2d(_text)
            if isinstance(_val, SDFError):
                return _val.extend("point")
            _points.append(_val)
        return cls(sdf_version=version, height=_height, points=_points)
