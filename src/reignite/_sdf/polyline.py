### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector2d import Vector2d as _Vector2dT, _vector2d

def _parse_vector2d(raw: str) -> _Vector2dT | SDFError:
    try:
        return _vector2d(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Polyline(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        height: float | None = 1.0,
        points: List[_Vector2dT] | None = None
    ):
        super().__init__(sdf_version)
        self.height = height if height is not None else 1.0
        self.points = list(map(_vector2d, points)) if points is not None else []

    def add_point(self, *items: _Vector2dT):
        if self.points is None:
            self.points = []
        self.points.extend(items)

    def to_version(self, target_version: str) -> "Polyline":
        kwargs: dict = {"sdf_version": target_version, "height": self.height, "points": self.points}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
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
