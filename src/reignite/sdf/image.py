from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model


import math

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > math.inf:
        raise ValueError(f"double out of range: {raw}")
    return v



class Uri(Model):
    def __init__(self, sdf_version: str, uri: str = "__default__"):
        self.__version__ = sdf_version
        self.uri = uri

    def to_version(self, target_version: str) -> "Uri":
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("uri")
        if self.uri is not None:
            el.text = self.uri
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Uri":
        _text = el.text or "__default__"
        _uri = _text
        return cls(sdf_version=version, uri=_uri)


class Scale(Model):
    def __init__(self, sdf_version: str, scale: float = 1):
        self.__version__ = sdf_version
        self.scale = scale

    def to_version(self, target_version: str) -> "Scale":
        kwargs = {"sdf_version": target_version}
        kwargs["scale"] = self.scale
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = str(self.scale)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Scale":
        _text = el.text or 1
        _scale = _parse_double(_text)
        return cls(sdf_version=version, scale=_scale)


class Threshold(Model):
    def __init__(self, sdf_version: str, threshold: int = 200):
        self.__version__ = sdf_version
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Threshold":
        kwargs = {"sdf_version": target_version}
        kwargs["threshold"] = self.threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("threshold")
        if self.threshold is not None:
            el.text = str(self.threshold)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Threshold":
        _text = el.text or 200
        _threshold = _parse_int32(_text)
        return cls(sdf_version=version, threshold=_threshold)


class Height(Model):
    def __init__(self, sdf_version: str, height: float = 1):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("height")
        if self.height is not None:
            el.text = str(self.height)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Height":
        _text = el.text or 1
        _height = _parse_double(_text)
        return cls(sdf_version=version, height=_height)


class Granularity(Model):
    def __init__(self, sdf_version: str, granularity: int = 1):
        self.__version__ = sdf_version
        self.granularity = granularity

    def to_version(self, target_version: str) -> "Granularity":
        kwargs = {"sdf_version": target_version}
        kwargs["granularity"] = self.granularity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("granularity")
        if self.granularity is not None:
            el.text = str(self.granularity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Granularity":
        _text = el.text or 1
        _granularity = _parse_int32(_text)
        return cls(sdf_version=version, granularity=_granularity)


class Image(Model):
    def __init__(
        self,
        sdf_version: str,
        uri: "Uri" = None,
        scale: "Scale" = None,
        threshold: "Threshold" = None,
        height: "Height" = None,
        granularity: "Granularity" = None
    ):
        self.__version__ = sdf_version
        self.uri = uri
        self.scale = scale
        self.threshold = threshold
        self.height = height
        self.granularity = granularity

    def to_version(self, target_version: str) -> "Image":
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        kwargs["threshold"] = self.threshold.to_version(target_version) if self.threshold is not None else None
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        kwargs["granularity"] = self.granularity.to_version(target_version) if self.granularity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("image")
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        if self.threshold is not None:
            el.append(self.threshold.to_sdf(version))
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        if self.granularity is not None:
            el.append(self.granularity.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Image":
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale, version) if _c_scale is not None else None
        _c_threshold = el.find("threshold")
        _threshold = Threshold.from_sdf(_c_threshold, version) if _c_threshold is not None else None
        _c_height = el.find("height")
        _height = Height.from_sdf(_c_height, version) if _c_height is not None else None
        _c_granularity = el.find("granularity")
        _granularity = Granularity.from_sdf(_c_granularity, version) if _c_granularity is not None else None
        return cls(sdf_version=version, uri=_uri, scale=_scale, threshold=_threshold, height=_height, granularity=_granularity)
