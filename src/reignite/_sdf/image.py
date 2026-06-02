### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_int32
from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class Image(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        granularity: int | None = 1,
        height: float | None = 1,
        scale: float | None = 1,
        threshold: int | None = 200,
        uri: str | None = "__default__"
    ):
        super().__init__(sdf_version)
        self.granularity = granularity if granularity is not None else 1
        self.height = height if height is not None else 1
        self.scale = scale if scale is not None else 1
        self.threshold = threshold if threshold is not None else 200
        self.uri = uri if uri is not None else "__default__"

    def to_version(self, target_version: str) -> "Image":
        kwargs: dict = {"sdf_version": target_version, "granularity": self.granularity, "height": self.height, "scale": self.scale, "threshold": self.threshold, "uri": self.uri}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("image")
        if self.granularity is not None:
            _c_tmp = ET.Element("granularity")
            _c_tmp.text = str(self.granularity)
            el.append(_c_tmp)
        if self.height is not None:
            _c_tmp = ET.Element("height")
            _c_tmp.text = str(self.height)
            el.append(_c_tmp)
        if self.scale is not None:
            _c_tmp = ET.Element("scale")
            _c_tmp.text = str(self.scale)
            el.append(_c_tmp)
        if self.threshold is not None:
            _c_tmp = ET.Element("threshold")
            _c_tmp.text = str(self.threshold)
            el.append(_c_tmp)
        if self.uri is not None:
            _c_tmp = ET.Element("uri")
            _c_tmp.text = self.uri
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Image | SDFError":
        _c_tmp = el.find("granularity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_int32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("granularity")
            _granularity = _val
        else:
            _granularity = None
        _c_tmp = el.find("height")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("height")
            _height = _val
        else:
            _height = None
        _c_tmp = el.find("scale")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("scale")
            _scale = _val
        else:
            _scale = None
        _c_tmp = el.find("threshold")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 200
            _val = _parse_int32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("threshold")
            _threshold = _val
        else:
            _threshold = None
        _c_tmp = el.find("uri")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("uri")
            _uri = _val
        else:
            _uri = None
        return cls(sdf_version=version, granularity=_granularity, height=_height, scale=_scale, threshold=_threshold, uri=_uri)
