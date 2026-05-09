### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

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



class Near(BaseModel):
    def __init__(self, sdf_version: str, near: float = 0):
        self.__version__ = sdf_version
        self.near = near

    def to_version(self, target_version: str) -> "Near":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("near")
        if self.near is None:
            raise ValueError(f"'near' is required in SDF version {version}")
        if self.near is not None:
            el.text = str(self.near)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'near' is required in SDF version {version}")
        _text = el.text or 0
        _near = _parse_double(_text)
        if isinstance(_near, SDFError):
            return _near
        return cls(sdf_version=version, near=_near)


class Far(BaseModel):
    def __init__(self, sdf_version: str, far: float = 1):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "Far":
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("far")
        if self.far is None:
            raise ValueError(f"'far' is required in SDF version {version}")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'far' is required in SDF version {version}")
        _text = el.text or 1
        _far = _parse_double(_text)
        if isinstance(_far, SDFError):
            return _far
        return cls(sdf_version=version, far=_far)


class AspectRatio(BaseModel):
    def __init__(self, sdf_version: str, aspect_ratio: float = 1):
        self.__version__ = sdf_version
        self.aspect_ratio = aspect_ratio

    def to_version(self, target_version: str) -> "AspectRatio":
        kwargs = {"sdf_version": target_version}
        kwargs["aspect_ratio"] = self.aspect_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("aspect_ratio")
        if self.aspect_ratio is None:
            raise ValueError(f"'aspect_ratio' is required in SDF version {version}")
        if self.aspect_ratio is not None:
            el.text = str(self.aspect_ratio)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'aspect_ratio' is required in SDF version {version}")
        _text = el.text or 1
        _aspect_ratio = _parse_double(_text)
        if isinstance(_aspect_ratio, SDFError):
            return _aspect_ratio
        return cls(sdf_version=version, aspect_ratio=_aspect_ratio)


class HorizontalFov(BaseModel):
    def __init__(self, sdf_version: str, horizontal_fov: float = 1):
        self.__version__ = sdf_version
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "HorizontalFov":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal_fov"] = self.horizontal_fov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal_fov")
        if self.horizontal_fov is None:
            raise ValueError(f"'horizontal_fov' is required in SDF version {version}")
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'horizontal_fov' is required in SDF version {version}")
        _text = el.text or 1
        _horizontal_fov = _parse_double(_text)
        if isinstance(_horizontal_fov, SDFError):
            return _horizontal_fov
        return cls(sdf_version=version, horizontal_fov=_horizontal_fov)


class LogicalCamera(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        near: "Near" = None,
        far: "Far" = None,
        aspect_ratio: "AspectRatio" = None,
        horizontal_fov: "HorizontalFov" = None
    ):
        self.__version__ = sdf_version
        self.near = near
        self.far = far
        self.aspect_ratio = aspect_ratio
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "LogicalCamera":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near.to_version(target_version) if self.near is not None else None
        kwargs["far"] = self.far.to_version(target_version) if self.far is not None else None
        kwargs["aspect_ratio"] = self.aspect_ratio.to_version(target_version) if self.aspect_ratio is not None else None
        kwargs["horizontal_fov"] = self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("logical_camera")
        if self.near is None:
            raise ValueError(f"'near' is required in SDF version {version}")
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        if self.far is None:
            raise ValueError(f"'far' is required in SDF version {version}")
        if self.far is not None:
            el.append(self.far.to_sdf(version))
        if self.aspect_ratio is None:
            raise ValueError(f"'aspect_ratio' is required in SDF version {version}")
        if self.aspect_ratio is not None:
            el.append(self.aspect_ratio.to_sdf(version))
        if self.horizontal_fov is None:
            raise ValueError(f"'horizontal_fov' is required in SDF version {version}")
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_near = el.find("near")
        if _c_near is not None:
            _res = Near._from_sdf(_c_near, version)
            if isinstance(_res, SDFError):
                return _res.extend("near")
            _near = _res
        else:
            _near = None
        if _near is None:
            return SDFError(f"'near' is required in SDF version {version}")
        _c_far = el.find("far")
        if _c_far is not None:
            _res = Far._from_sdf(_c_far, version)
            if isinstance(_res, SDFError):
                return _res.extend("far")
            _far = _res
        else:
            _far = None
        if _far is None:
            return SDFError(f"'far' is required in SDF version {version}")
        _c_aspect_ratio = el.find("aspect_ratio")
        if _c_aspect_ratio is not None:
            _res = AspectRatio._from_sdf(_c_aspect_ratio, version)
            if isinstance(_res, SDFError):
                return _res.extend("aspect_ratio")
            _aspect_ratio = _res
        else:
            _aspect_ratio = None
        if _aspect_ratio is None:
            return SDFError(f"'aspect_ratio' is required in SDF version {version}")
        _c_horizontal_fov = el.find("horizontal_fov")
        if _c_horizontal_fov is not None:
            _res = HorizontalFov._from_sdf(_c_horizontal_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal_fov")
            _horizontal_fov = _res
        else:
            _horizontal_fov = None
        if _horizontal_fov is None:
            return SDFError(f"'horizontal_fov' is required in SDF version {version}")
        return cls(sdf_version=version, near=_near, far=_far, aspect_ratio=_aspect_ratio, horizontal_fov=_horizontal_fov)
