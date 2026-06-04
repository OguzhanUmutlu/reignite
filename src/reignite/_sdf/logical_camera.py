### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class LogicalCamera(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        aspect_ratio: float | None = None,
        far: float | None = None,
        horizontal_fov: float | None = None,
        near: float | None = None
    ):
        super().__init__(sdf_version)
        self.aspect_ratio = aspect_ratio
        self.far = far
        self.horizontal_fov = horizontal_fov
        self.near = near

    def to_version(self, target_version: str) -> "LogicalCamera":
        kwargs: dict = {"sdf_version": target_version, "aspect_ratio": self.aspect_ratio, "far": self.far, "horizontal_fov": self.horizontal_fov, "near": self.near}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("logical_camera")
        if self.aspect_ratio is not None:
            _c_tmp = ET.Element("aspect_ratio")
            _c_tmp.text = str(self.aspect_ratio)
            el.append(_c_tmp)
        if self.far is not None:
            _c_tmp = ET.Element("far")
            _c_tmp.text = str(self.far)
            el.append(_c_tmp)
        if self.horizontal_fov is not None:
            _c_tmp = ET.Element("horizontal_fov")
            _c_tmp.text = str(self.horizontal_fov)
            el.append(_c_tmp)
        if self.near is not None:
            _c_tmp = ET.Element("near")
            _c_tmp.text = str(self.near)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "LogicalCamera | SDFError":
        _c_tmp = el.find("aspect_ratio")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("aspect_ratio")
            _aspect_ratio = _val
        else:
            _aspect_ratio = None
        _c_tmp = el.find("far")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("far")
            _far = _val
        else:
            _far = None
        _c_tmp = el.find("horizontal_fov")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("horizontal_fov")
            _horizontal_fov = _val
        else:
            _horizontal_fov = None
        _c_tmp = el.find("near")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("near")
            _near = _val
        else:
            _near = None
        return cls(sdf_version=version, aspect_ratio=_aspect_ratio, far=_far, horizontal_fov=_horizontal_fov, near=_near)
