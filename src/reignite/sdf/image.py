### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


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



class Image(BaseModel):
    class Granularity(BaseModel):
        def __init__(self, sdf_version: str | None = None, granularity: int = 1):
            super().__init__(sdf_version)
            self.granularity = granularity

        def to_version(self, target_version: str) -> "Image.Granularity":
            kwargs = {"sdf_version": target_version}
            kwargs["granularity"] = self.granularity
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("granularity")
            if self.granularity is not None:
                el.text = str(self.granularity)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Image.Granularity | SDFError":
            _text = el.text or 1
            _granularity = _parse_int32(_text)
            if isinstance(_granularity, SDFError):
                return _granularity
            return cls(sdf_version=version, granularity=_granularity)

    class Height(BaseModel):
        def __init__(self, sdf_version: str | None = None, height: float = 1):
            super().__init__(sdf_version)
            self.height = height

        def to_version(self, target_version: str) -> "Image.Height":
            kwargs = {"sdf_version": target_version}
            kwargs["height"] = self.height
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("height")
            if self.height is not None:
                el.text = str(self.height)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Image.Height | SDFError":
            _text = el.text or 1
            _height = _parse_double(_text)
            if isinstance(_height, SDFError):
                return _height
            return cls(sdf_version=version, height=_height)

    class Scale(BaseModel):
        def __init__(self, sdf_version: str | None = None, scale: float = 1):
            super().__init__(sdf_version)
            self.scale = scale

        def to_version(self, target_version: str) -> "Image.Scale":
            kwargs = {"sdf_version": target_version}
            kwargs["scale"] = self.scale
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("scale")
            if self.scale is not None:
                el.text = str(self.scale)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Image.Scale | SDFError":
            _text = el.text or 1
            _scale = _parse_double(_text)
            if isinstance(_scale, SDFError):
                return _scale
            return cls(sdf_version=version, scale=_scale)

    class Threshold(BaseModel):
        def __init__(self, sdf_version: str | None = None, threshold: int = 200):
            super().__init__(sdf_version)
            self.threshold = threshold

        def to_version(self, target_version: str) -> "Image.Threshold":
            kwargs = {"sdf_version": target_version}
            kwargs["threshold"] = self.threshold
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("threshold")
            if self.threshold is not None:
                el.text = str(self.threshold)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Image.Threshold | SDFError":
            _text = el.text or 200
            _threshold = _parse_int32(_text)
            if isinstance(_threshold, SDFError):
                return _threshold
            return cls(sdf_version=version, threshold=_threshold)

    class Uri(BaseModel):
        def __init__(self, sdf_version: str | None = None, uri: str = "__default__"):
            super().__init__(sdf_version)
            self.uri = uri

        def to_version(self, target_version: str) -> "Image.Uri":
            kwargs = {"sdf_version": target_version}
            kwargs["uri"] = self.uri
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("uri")
            if self.uri is not None:
                el.text = self.uri
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Image.Uri | SDFError":
            _text = el.text or "__default__"
            _uri = _text
            if isinstance(_uri, SDFError):
                return _uri
            return cls(sdf_version=version, uri=_uri)

    def __init__(
        self,
        sdf_version: str | None = None,
        granularity: "Image.Granularity" = None,
        height: "Image.Height" = None,
        scale: "Image.Scale" = None,
        threshold: "Image.Threshold" = None,
        uri: "Image.Uri" = None
    ):
        super().__init__(sdf_version)
        self.granularity = granularity
        self.height = height
        self.scale = scale
        self.threshold = threshold
        self.uri = uri
        if self.granularity is not None:
            if getattr(self.granularity, '__version__', None) is None:
                self.granularity.__version__ = self.__version__
            elif getattr(self.granularity, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.granularity = self.granularity.to_version(self.__version__)
        if self.height is not None:
            if getattr(self.height, '__version__', None) is None:
                self.height.__version__ = self.__version__
            elif getattr(self.height, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.height = self.height.to_version(self.__version__)
        if self.scale is not None:
            if getattr(self.scale, '__version__', None) is None:
                self.scale.__version__ = self.__version__
            elif getattr(self.scale, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.scale = self.scale.to_version(self.__version__)
        if self.threshold is not None:
            if getattr(self.threshold, '__version__', None) is None:
                self.threshold.__version__ = self.__version__
            elif getattr(self.threshold, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.threshold = self.threshold.to_version(self.__version__)
        if self.uri is not None:
            if getattr(self.uri, '__version__', None) is None:
                self.uri.__version__ = self.__version__
            elif getattr(self.uri, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.uri = self.uri.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Image":
        kwargs = {"sdf_version": target_version}
        kwargs["granularity"] = self.granularity.to_version(target_version) if self.granularity is not None else None
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        kwargs["threshold"] = self.threshold.to_version(target_version) if self.threshold is not None else None
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("image")
        if self.granularity is not None:
            el.append(self.granularity.to_sdf(version))
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        if self.threshold is not None:
            el.append(self.threshold.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Image | SDFError":
        _c_granularity = el.find("granularity")
        if _c_granularity is not None:
            _res = cls.Granularity._from_sdf(_c_granularity, version)
            if isinstance(_res, SDFError):
                return _res.extend("granularity")
            _granularity = _res
        else:
            _granularity = None
        _c_height = el.find("height")
        if _c_height is not None:
            _res = cls.Height._from_sdf(_c_height, version)
            if isinstance(_res, SDFError):
                return _res.extend("height")
            _height = _res
        else:
            _height = None
        _c_scale = el.find("scale")
        if _c_scale is not None:
            _res = cls.Scale._from_sdf(_c_scale, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale")
            _scale = _res
        else:
            _scale = None
        _c_threshold = el.find("threshold")
        if _c_threshold is not None:
            _res = cls.Threshold._from_sdf(_c_threshold, version)
            if isinstance(_res, SDFError):
                return _res.extend("threshold")
            _threshold = _res
        else:
            _threshold = None
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = cls.Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        return cls(sdf_version=version, granularity=_granularity, height=_height, scale=_scale, threshold=_threshold, uri=_uri)
