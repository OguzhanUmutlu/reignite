### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.vector2d import Vector2d as _SDFVector2d
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations


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



class Plugin(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__", filename: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name
        self.filename = filename

    def to_version(self, target_version: str) -> "Plugin":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["filename"] = self.filename
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plugin")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.set("filename", self.filename)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        return cls(sdf_version=version, name=_name, filename=_filename)


class HorizontalFov(BaseModel):
    def __init__(self, sdf_version: str, horizontal_fov: float = 1.047, angle: float = 1.047):
        self.__version__ = sdf_version
        self.horizontal_fov = horizontal_fov
        self.angle = angle

    def to_version(self, target_version: str) -> "HorizontalFov":
        if self.angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'angle' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal_fov"] = self.horizontal_fov
        kwargs["angle"] = self.angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal_fov")
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        if self.angle is not None:
            el.set("angle", str(self.angle))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.047
        _horizontal_fov = _parse_double(_text)
        if isinstance(_horizontal_fov, SDFError):
            return _horizontal_fov
        _angle = _parse_double(el.get("angle", 1.047))
        if isinstance(_angle, SDFError):
            return _angle.extend("@angle")
        return cls(sdf_version=version, horizontal_fov=_horizontal_fov, angle=_angle)


class Format(BaseModel):
    def __init__(self, sdf_version: str, format: str = "R8G8B8"):
        self.__version__ = sdf_version
        self.format = format

    def to_version(self, target_version: str) -> "Format":
        if self.format is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'format' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["format"] = self.format
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("format")
        if self.format is not None:
            el.text = self.format
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "R8G8B8"
        _format = _text
        if isinstance(_format, SDFError):
            return _format
        if _format is not None and cmp_version(version, "1.2") < 0:
            if _format != "R8G8B8":
                return SDFError(f"'format' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, format=_format)


class Height(BaseModel):
    def __init__(self, sdf_version: str, height: int = 240):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
        if self.height is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'height' is not supported in SDF version {target_version} (added in 1.2)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 240
        _height = _parse_int32(_text)
        if isinstance(_height, SDFError):
            return _height
        if _height is not None and cmp_version(version, "1.2") < 0:
            if _height != 240:
                return SDFError(f"'height' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, height=_height)


class Width(BaseModel):
    def __init__(self, sdf_version: str, width: int = 320):
        self.__version__ = sdf_version
        self.width = width

    def to_version(self, target_version: str) -> "Width":
        if self.width is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'width' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["width"] = self.width
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("width")
        if self.width is not None:
            el.text = str(self.width)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 320
        _width = _parse_int32(_text)
        if isinstance(_width, SDFError):
            return _width
        if _width is not None and cmp_version(version, "1.2") < 0:
            if _width != 320:
                return SDFError(f"'width' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, width=_width)


class AntiAliasing(BaseModel):
    def __init__(self, sdf_version: str, anti_aliasing: int = 4):
        self.__version__ = sdf_version
        self.anti_aliasing = anti_aliasing

    def to_version(self, target_version: str) -> "AntiAliasing":
        if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["anti_aliasing"] = self.anti_aliasing
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("anti_aliasing")
        if self.anti_aliasing is not None:
            el.text = str(self.anti_aliasing)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4
        _anti_aliasing = _parse_int32(_text)
        if isinstance(_anti_aliasing, SDFError):
            return _anti_aliasing
        if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
            if _anti_aliasing != 4:
                return SDFError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, anti_aliasing=_anti_aliasing)


class Image(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        width: int = 320,
        height: int = 240,
        format: str = "R8G8B8",
        anti_aliasing: "AntiAliasing" = None
    ):
        self.__version__ = sdf_version
        self.width = width
        self.height = height
        self.format = format
        self.anti_aliasing = anti_aliasing

    def to_version(self, target_version: str) -> "Image":
        if self.width is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'width' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.height is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'height' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.format is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'format' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["width"] = self.width
        kwargs["height"] = self.height
        kwargs["format"] = self.format
        kwargs["anti_aliasing"] = self.anti_aliasing.to_version(target_version) if self.anti_aliasing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("image")
        if self.width is not None:
            el.set("width", str(self.width))
        if self.height is not None:
            el.set("height", str(self.height))
        if self.format is not None:
            el.set("format", self.format)
        if self.anti_aliasing is not None:
            el.append(self.anti_aliasing.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _width = _parse_int32(el.get("width", 320))
        if isinstance(_width, SDFError):
            return _width.extend("@width")
        _height = _parse_int32(el.get("height", 240))
        if isinstance(_height, SDFError):
            return _height.extend("@height")
        _format = el.get("format", "R8G8B8")
        if isinstance(_format, SDFError):
            return _format.extend("@format")
        _c_anti_aliasing = el.find("anti_aliasing")
        if _c_anti_aliasing is not None:
            _res = AntiAliasing._from_sdf(_c_anti_aliasing, version)
            if isinstance(_res, SDFError):
                return _res.extend("anti_aliasing")
            _anti_aliasing = _res
        else:
            _anti_aliasing = None
        if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, width=_width, height=_height, format=_format, anti_aliasing=_anti_aliasing)


class Near(BaseModel):
    def __init__(self, sdf_version: str, near: float = .1):
        self.__version__ = sdf_version
        self.near = near

    def to_version(self, target_version: str) -> "Near":
        if self.near is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'near' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("near")
        if self.near is not None:
            el.text = str(self.near)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or .1
        _near = _parse_double(_text)
        if isinstance(_near, SDFError):
            return _near
        if _near is not None and cmp_version(version, "1.2") < 0:
            if _near != .1:
                return SDFError(f"'near' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, near=_near)


class Far(BaseModel):
    def __init__(self, sdf_version: str, far: float = 100):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "Far":
        if self.far is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'far' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("far")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100
        _far = _parse_double(_text)
        if isinstance(_far, SDFError):
            return _far
        if _far is not None and cmp_version(version, "1.2") < 0:
            if _far != 100:
                return SDFError(f"'far' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, far=_far)


class Clip(BaseModel):
    def __init__(self, sdf_version: str, near: float = .1, far: float = 100):
        self.__version__ = sdf_version
        self.near = near
        self.far = far

    def to_version(self, target_version: str) -> "Clip":
        if self.near is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'near' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.far is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'far' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("clip")
        if self.near is not None:
            el.set("near", str(self.near))
        if self.far is not None:
            el.set("far", str(self.far))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _near = _parse_double(el.get("near", .1))
        if isinstance(_near, SDFError):
            return _near.extend("@near")
        _far = _parse_double(el.get("far", 100))
        if isinstance(_far, SDFError):
            return _far.extend("@far")
        return cls(sdf_version=version, near=_near, far=_far)


class Path(BaseModel):
    def __init__(self, sdf_version: str, path: str = "__default__"):
        self.__version__ = sdf_version
        self.path = path

    def to_version(self, target_version: str) -> "Path":
        if self.path is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'path' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["path"] = self.path
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("path")
        if self.path is not None:
            el.text = self.path
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _path = _text
        if isinstance(_path, SDFError):
            return _path
        if _path is not None and cmp_version(version, "1.2") < 0:
            if _path != "__default__":
                return SDFError(f"'path' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, path=_path)


class Save(BaseModel):
    def __init__(self, sdf_version: str, enabled: bool = False, path: str = "__default__"):
        self.__version__ = sdf_version
        self.enabled = enabled
        self.path = path

    def to_version(self, target_version: str) -> "Save":
        if self.path is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'path' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["enabled"] = self.enabled
        kwargs["path"] = self.path
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("save")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        if self.path is not None:
            el.set("path", self.path)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _enabled = str(el.get("enabled", False)).strip().lower() == 'true'
        if isinstance(_enabled, SDFError):
            return _enabled.extend("@enabled")
        _path = el.get("path", "__default__")
        if isinstance(_path, SDFError):
            return _path.extend("@path")
        return cls(sdf_version=version, enabled=_enabled, path=_path)


class Output(BaseModel):
    def __init__(self, sdf_version: str, output: str = "depths"):
        self.__version__ = sdf_version
        self.output = output

    def to_version(self, target_version: str) -> "Output":
        if self.output is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'output' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["output"] = self.output
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("output")
        if self.output is not None:
            el.text = self.output
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "depths"
        _output = _text
        if isinstance(_output, SDFError):
            return _output
        if _output is not None and cmp_version(version, "1.2") < 0:
            if _output != "depths":
                return SDFError(f"'output' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, output=_output)


class ClipFar(BaseModel):
    def __init__(self, sdf_version: str, far: float = 10.0):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "ClipFar":
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("far")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10.0
        _far = _parse_double(_text)
        if isinstance(_far, SDFError):
            return _far
        return cls(sdf_version=version, far=_far)


class DepthCameraClip(BaseModel):
    def __init__(self, sdf_version: str, near: "Near" = None, far: "ClipFar" = None):
        self.__version__ = sdf_version
        self.near = near
        self.far = far

    def to_version(self, target_version: str) -> "DepthCameraClip":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near.to_version(target_version) if self.near is not None else None
        kwargs["far"] = self.far.to_version(target_version) if self.far is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("clip")
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        if self.far is not None:
            el.append(self.far.to_sdf(version))
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
        _c_far = el.find("far")
        if _c_far is not None:
            _res = ClipFar._from_sdf(_c_far, version)
            if isinstance(_res, SDFError):
                return _res.extend("far")
            _far = _res
        else:
            _far = None
        return cls(sdf_version=version, near=_near, far=_far)


class DepthCamera(BaseModel):
    def __init__(self, sdf_version: str, output: str = "depths", clip: "DepthCameraClip" = None):
        self.__version__ = sdf_version
        self.output = output
        self.clip = clip

    def to_version(self, target_version: str) -> "DepthCamera":
        if self.output is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'output' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.clip is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'clip' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["output"] = self.output
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("depth_camera")
        if self.output is not None:
            el.set("output", self.output)
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _output = el.get("output", "depths")
        if isinstance(_output, SDFError):
            return _output.extend("@output")
        _c_clip = el.find("clip")
        if _c_clip is not None:
            _res = DepthCameraClip._from_sdf(_c_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        else:
            _clip = None
        if _clip is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'clip' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, output=_output, clip=_clip)


class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Pose":
        if self.pose is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.3)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
        kwargs["relative_to"] = self.relative_to
        kwargs["rotation_format"] = self.rotation_format
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        if _pose is not None and cmp_version(version, "1.3") < 0:
            if _pose != "0 0 0 0 0 0":
                return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.3)")
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Type(BaseModel):
    def __init__(self, sdf_version: str, type: str = "gaussian"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Type":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "gaussian"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        return cls(sdf_version=version, type=_type)


class Mean(BaseModel):
    def __init__(self, sdf_version: str, mean: float = 0.0):
        self.__version__ = sdf_version
        self.mean = mean

    def to_version(self, target_version: str) -> "Mean":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mean")
        if self.mean is not None:
            el.text = str(self.mean)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _mean = _parse_double(_text)
        if isinstance(_mean, SDFError):
            return _mean
        return cls(sdf_version=version, mean=_mean)


class Stddev(BaseModel):
    def __init__(self, sdf_version: str, stddev: float = 0.0):
        self.__version__ = sdf_version
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Stddev":
        kwargs = {"sdf_version": target_version}
        kwargs["stddev"] = self.stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("stddev")
        if self.stddev is not None:
            el.text = str(self.stddev)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _stddev = _parse_double(_text)
        if isinstance(_stddev, SDFError):
            return _stddev
        return cls(sdf_version=version, stddev=_stddev)


class Noise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        mean: "Mean" = None,
        stddev: "Stddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Noise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev)


class LensType(BaseModel):
    def __init__(self, sdf_version: str, type: str = "stereographic"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "LensType":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "stereographic"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        return cls(sdf_version=version, type=_type)


class ScaleToHfov(BaseModel):
    def __init__(self, sdf_version: str, scale_to_hfov: bool = True):
        self.__version__ = sdf_version
        self.scale_to_hfov = scale_to_hfov

    def to_version(self, target_version: str) -> "ScaleToHfov":
        kwargs = {"sdf_version": target_version}
        kwargs["scale_to_hfov"] = self.scale_to_hfov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale_to_hfov")
        if self.scale_to_hfov is not None:
            el.text = str(self.scale_to_hfov).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _scale_to_hfov = str(_text).strip().lower() == 'true'
        if isinstance(_scale_to_hfov, SDFError):
            return _scale_to_hfov
        return cls(sdf_version=version, scale_to_hfov=_scale_to_hfov)


class C1(BaseModel):
    def __init__(self, sdf_version: str, c1: float = 1):
        self.__version__ = sdf_version
        self.c1 = c1

    def to_version(self, target_version: str) -> "C1":
        kwargs = {"sdf_version": target_version}
        kwargs["c1"] = self.c1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c1")
        if self.c1 is not None:
            el.text = str(self.c1)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _c1 = _parse_double(_text)
        if isinstance(_c1, SDFError):
            return _c1
        return cls(sdf_version=version, c1=_c1)


class C2(BaseModel):
    def __init__(self, sdf_version: str, c2: float = 1):
        self.__version__ = sdf_version
        self.c2 = c2

    def to_version(self, target_version: str) -> "C2":
        kwargs = {"sdf_version": target_version}
        kwargs["c2"] = self.c2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c2")
        if self.c2 is not None:
            el.text = str(self.c2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _c2 = _parse_double(_text)
        if isinstance(_c2, SDFError):
            return _c2
        return cls(sdf_version=version, c2=_c2)


class C3(BaseModel):
    def __init__(self, sdf_version: str, c3: float = 0):
        self.__version__ = sdf_version
        self.c3 = c3

    def to_version(self, target_version: str) -> "C3":
        kwargs = {"sdf_version": target_version}
        kwargs["c3"] = self.c3
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c3")
        if self.c3 is not None:
            el.text = str(self.c3)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _c3 = _parse_double(_text)
        if isinstance(_c3, SDFError):
            return _c3
        return cls(sdf_version=version, c3=_c3)


class F(BaseModel):
    def __init__(self, sdf_version: str, f: float = 1):
        self.__version__ = sdf_version
        self.f = f

    def to_version(self, target_version: str) -> "F":
        kwargs = {"sdf_version": target_version}
        kwargs["f"] = self.f
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("f")
        if self.f is not None:
            el.text = str(self.f)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _f = _parse_double(_text)
        if isinstance(_f, SDFError):
            return _f
        return cls(sdf_version=version, f=_f)


class Fun(BaseModel):
    def __init__(self, sdf_version: str, fun: str = "tan"):
        self.__version__ = sdf_version
        self.fun = fun

    def to_version(self, target_version: str) -> "Fun":
        kwargs = {"sdf_version": target_version}
        kwargs["fun"] = self.fun
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fun")
        if self.fun is not None:
            el.text = self.fun
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "tan"
        _fun = _text
        if isinstance(_fun, SDFError):
            return _fun
        return cls(sdf_version=version, fun=_fun)


class CustomFunction(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        c1: "C1" = None,
        c2: "C2" = None,
        c3: "C3" = None,
        f: "F" = None,
        fun: "Fun" = None
    ):
        self.__version__ = sdf_version
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.f = f
        self.fun = fun

    def to_version(self, target_version: str) -> "CustomFunction":
        kwargs = {"sdf_version": target_version}
        kwargs["c1"] = self.c1.to_version(target_version) if self.c1 is not None else None
        kwargs["c2"] = self.c2.to_version(target_version) if self.c2 is not None else None
        kwargs["c3"] = self.c3.to_version(target_version) if self.c3 is not None else None
        kwargs["f"] = self.f.to_version(target_version) if self.f is not None else None
        kwargs["fun"] = self.fun.to_version(target_version) if self.fun is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("custom_function")
        if self.c1 is not None:
            el.append(self.c1.to_sdf(version))
        if self.c2 is not None:
            el.append(self.c2.to_sdf(version))
        if self.c3 is not None:
            el.append(self.c3.to_sdf(version))
        if self.f is not None:
            el.append(self.f.to_sdf(version))
        if self.fun is not None:
            el.append(self.fun.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_c1 = el.find("c1")
        if _c_c1 is not None:
            _res = C1._from_sdf(_c_c1, version)
            if isinstance(_res, SDFError):
                return _res.extend("c1")
            _c1 = _res
        else:
            _c1 = None
        _c_c2 = el.find("c2")
        if _c_c2 is not None:
            _res = C2._from_sdf(_c_c2, version)
            if isinstance(_res, SDFError):
                return _res.extend("c2")
            _c2 = _res
        else:
            _c2 = None
        _c_c3 = el.find("c3")
        if _c_c3 is not None:
            _res = C3._from_sdf(_c_c3, version)
            if isinstance(_res, SDFError):
                return _res.extend("c3")
            _c3 = _res
        else:
            _c3 = None
        _c_f = el.find("f")
        if _c_f is not None:
            _res = F._from_sdf(_c_f, version)
            if isinstance(_res, SDFError):
                return _res.extend("f")
            _f = _res
        else:
            _f = None
        _c_fun = el.find("fun")
        if _c_fun is not None:
            _res = Fun._from_sdf(_c_fun, version)
            if isinstance(_res, SDFError):
                return _res.extend("fun")
            _fun = _res
        else:
            _fun = None
        return cls(sdf_version=version, c1=_c1, c2=_c2, c3=_c3, f=_f, fun=_fun)


class CutoffAngle(BaseModel):
    def __init__(self, sdf_version: str, cutoff_angle: float = 1.5707):
        self.__version__ = sdf_version
        self.cutoff_angle = cutoff_angle

    def to_version(self, target_version: str) -> "CutoffAngle":
        kwargs = {"sdf_version": target_version}
        kwargs["cutoff_angle"] = self.cutoff_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cutoff_angle")
        if self.cutoff_angle is not None:
            el.text = str(self.cutoff_angle)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.5707
        _cutoff_angle = _parse_double(_text)
        if isinstance(_cutoff_angle, SDFError):
            return _cutoff_angle
        return cls(sdf_version=version, cutoff_angle=_cutoff_angle)


class EnvTextureSize(BaseModel):
    def __init__(self, sdf_version: str, env_texture_size: int = 256):
        self.__version__ = sdf_version
        self.env_texture_size = env_texture_size

    def to_version(self, target_version: str) -> "EnvTextureSize":
        kwargs = {"sdf_version": target_version}
        kwargs["env_texture_size"] = self.env_texture_size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("env_texture_size")
        if self.env_texture_size is not None:
            el.text = str(self.env_texture_size)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 256
        _env_texture_size = _parse_int32(_text)
        if isinstance(_env_texture_size, SDFError):
            return _env_texture_size
        return cls(sdf_version=version, env_texture_size=_env_texture_size)


class Fx(BaseModel):
    def __init__(self, sdf_version: str, fx: float = 277):
        self.__version__ = sdf_version
        self.fx = fx

    def to_version(self, target_version: str) -> "Fx":
        kwargs = {"sdf_version": target_version}
        kwargs["fx"] = self.fx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fx")
        if self.fx is not None:
            el.text = str(self.fx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _fx = _parse_double(_text)
        if isinstance(_fx, SDFError):
            return _fx
        return cls(sdf_version=version, fx=_fx)


class Fy(BaseModel):
    def __init__(self, sdf_version: str, fy: float = 277):
        self.__version__ = sdf_version
        self.fy = fy

    def to_version(self, target_version: str) -> "Fy":
        kwargs = {"sdf_version": target_version}
        kwargs["fy"] = self.fy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fy")
        if self.fy is not None:
            el.text = str(self.fy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _fy = _parse_double(_text)
        if isinstance(_fy, SDFError):
            return _fy
        return cls(sdf_version=version, fy=_fy)


class Cx(BaseModel):
    def __init__(self, sdf_version: str, cx: float = 160):
        self.__version__ = sdf_version
        self.cx = cx

    def to_version(self, target_version: str) -> "Cx":
        kwargs = {"sdf_version": target_version}
        kwargs["cx"] = self.cx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cx")
        if self.cx is not None:
            el.text = str(self.cx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 160
        _cx = _parse_double(_text)
        if isinstance(_cx, SDFError):
            return _cx
        return cls(sdf_version=version, cx=_cx)


class Cy(BaseModel):
    def __init__(self, sdf_version: str, cy: float = 120):
        self.__version__ = sdf_version
        self.cy = cy

    def to_version(self, target_version: str) -> "Cy":
        kwargs = {"sdf_version": target_version}
        kwargs["cy"] = self.cy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cy")
        if self.cy is not None:
            el.text = str(self.cy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 120
        _cy = _parse_double(_text)
        if isinstance(_cy, SDFError):
            return _cy
        return cls(sdf_version=version, cy=_cy)


class S(BaseModel):
    def __init__(self, sdf_version: str, s: float = 0.0):
        self.__version__ = sdf_version
        self.s = s

    def to_version(self, target_version: str) -> "S":
        kwargs = {"sdf_version": target_version}
        kwargs["s"] = self.s
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("s")
        if self.s is not None:
            el.text = str(self.s)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _s = _parse_double(_text)
        if isinstance(_s, SDFError):
            return _s
        return cls(sdf_version=version, s=_s)


class Intrinsics(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        fx: "Fx" = None,
        fy: "Fy" = None,
        cx: "Cx" = None,
        cy: "Cy" = None,
        s: "S" = None
    ):
        self.__version__ = sdf_version
        self.fx = fx
        self.fy = fy
        self.cx = cx
        self.cy = cy
        self.s = s

    def to_version(self, target_version: str) -> "Intrinsics":
        kwargs = {"sdf_version": target_version}
        kwargs["fx"] = self.fx.to_version(target_version) if self.fx is not None else None
        kwargs["fy"] = self.fy.to_version(target_version) if self.fy is not None else None
        kwargs["cx"] = self.cx.to_version(target_version) if self.cx is not None else None
        kwargs["cy"] = self.cy.to_version(target_version) if self.cy is not None else None
        kwargs["s"] = self.s.to_version(target_version) if self.s is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("intrinsics")
        if self.fx is not None:
            el.append(self.fx.to_sdf(version))
        if self.fy is not None:
            el.append(self.fy.to_sdf(version))
        if self.cx is not None:
            el.append(self.cx.to_sdf(version))
        if self.cy is not None:
            el.append(self.cy.to_sdf(version))
        if self.s is not None:
            el.append(self.s.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_fx = el.find("fx")
        if _c_fx is not None:
            _res = Fx._from_sdf(_c_fx, version)
            if isinstance(_res, SDFError):
                return _res.extend("fx")
            _fx = _res
        else:
            _fx = None
        _c_fy = el.find("fy")
        if _c_fy is not None:
            _res = Fy._from_sdf(_c_fy, version)
            if isinstance(_res, SDFError):
                return _res.extend("fy")
            _fy = _res
        else:
            _fy = None
        _c_cx = el.find("cx")
        if _c_cx is not None:
            _res = Cx._from_sdf(_c_cx, version)
            if isinstance(_res, SDFError):
                return _res.extend("cx")
            _cx = _res
        else:
            _cx = None
        _c_cy = el.find("cy")
        if _c_cy is not None:
            _res = Cy._from_sdf(_c_cy, version)
            if isinstance(_res, SDFError):
                return _res.extend("cy")
            _cy = _res
        else:
            _cy = None
        _c_s = el.find("s")
        if _c_s is not None:
            _res = S._from_sdf(_c_s, version)
            if isinstance(_res, SDFError):
                return _res.extend("s")
            _s = _res
        else:
            _s = None
        return cls(sdf_version=version, fx=_fx, fy=_fy, cx=_cx, cy=_cy, s=_s)


class PFx(BaseModel):
    def __init__(self, sdf_version: str, p_fx: float = 277):
        self.__version__ = sdf_version
        self.p_fx = p_fx

    def to_version(self, target_version: str) -> "PFx":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fx"] = self.p_fx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_fx")
        if self.p_fx is not None:
            el.text = str(self.p_fx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _p_fx = _parse_double(_text)
        if isinstance(_p_fx, SDFError):
            return _p_fx
        return cls(sdf_version=version, p_fx=_p_fx)


class PFy(BaseModel):
    def __init__(self, sdf_version: str, p_fy: float = 277):
        self.__version__ = sdf_version
        self.p_fy = p_fy

    def to_version(self, target_version: str) -> "PFy":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fy"] = self.p_fy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_fy")
        if self.p_fy is not None:
            el.text = str(self.p_fy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _p_fy = _parse_double(_text)
        if isinstance(_p_fy, SDFError):
            return _p_fy
        return cls(sdf_version=version, p_fy=_p_fy)


class PCx(BaseModel):
    def __init__(self, sdf_version: str, p_cx: float = 160):
        self.__version__ = sdf_version
        self.p_cx = p_cx

    def to_version(self, target_version: str) -> "PCx":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cx"] = self.p_cx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_cx")
        if self.p_cx is not None:
            el.text = str(self.p_cx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 160
        _p_cx = _parse_double(_text)
        if isinstance(_p_cx, SDFError):
            return _p_cx
        return cls(sdf_version=version, p_cx=_p_cx)


class PCy(BaseModel):
    def __init__(self, sdf_version: str, p_cy: float = 120):
        self.__version__ = sdf_version
        self.p_cy = p_cy

    def to_version(self, target_version: str) -> "PCy":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cy"] = self.p_cy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_cy")
        if self.p_cy is not None:
            el.text = str(self.p_cy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 120
        _p_cy = _parse_double(_text)
        if isinstance(_p_cy, SDFError):
            return _p_cy
        return cls(sdf_version=version, p_cy=_p_cy)


class Tx(BaseModel):
    def __init__(self, sdf_version: str, tx: float = 0.0):
        self.__version__ = sdf_version
        self.tx = tx

    def to_version(self, target_version: str) -> "Tx":
        kwargs = {"sdf_version": target_version}
        kwargs["tx"] = self.tx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("tx")
        if self.tx is not None:
            el.text = str(self.tx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _tx = _parse_double(_text)
        if isinstance(_tx, SDFError):
            return _tx
        return cls(sdf_version=version, tx=_tx)


class Ty(BaseModel):
    def __init__(self, sdf_version: str, ty: float = 0.0):
        self.__version__ = sdf_version
        self.ty = ty

    def to_version(self, target_version: str) -> "Ty":
        kwargs = {"sdf_version": target_version}
        kwargs["ty"] = self.ty
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ty")
        if self.ty is not None:
            el.text = str(self.ty)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _ty = _parse_double(_text)
        if isinstance(_ty, SDFError):
            return _ty
        return cls(sdf_version=version, ty=_ty)


class Projection(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        p_fx: "PFx" = None,
        p_fy: "PFy" = None,
        p_cx: "PCx" = None,
        p_cy: "PCy" = None,
        tx: "Tx" = None,
        ty: "Ty" = None
    ):
        self.__version__ = sdf_version
        self.p_fx = p_fx
        self.p_fy = p_fy
        self.p_cx = p_cx
        self.p_cy = p_cy
        self.tx = tx
        self.ty = ty

    def to_version(self, target_version: str) -> "Projection":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fx"] = self.p_fx.to_version(target_version) if self.p_fx is not None else None
        kwargs["p_fy"] = self.p_fy.to_version(target_version) if self.p_fy is not None else None
        kwargs["p_cx"] = self.p_cx.to_version(target_version) if self.p_cx is not None else None
        kwargs["p_cy"] = self.p_cy.to_version(target_version) if self.p_cy is not None else None
        kwargs["tx"] = self.tx.to_version(target_version) if self.tx is not None else None
        kwargs["ty"] = self.ty.to_version(target_version) if self.ty is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("projection")
        if self.p_fx is not None:
            el.append(self.p_fx.to_sdf(version))
        if self.p_fy is not None:
            el.append(self.p_fy.to_sdf(version))
        if self.p_cx is not None:
            el.append(self.p_cx.to_sdf(version))
        if self.p_cy is not None:
            el.append(self.p_cy.to_sdf(version))
        if self.tx is not None:
            el.append(self.tx.to_sdf(version))
        if self.ty is not None:
            el.append(self.ty.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_p_fx = el.find("p_fx")
        if _c_p_fx is not None:
            _res = PFx._from_sdf(_c_p_fx, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_fx")
            _p_fx = _res
        else:
            _p_fx = None
        _c_p_fy = el.find("p_fy")
        if _c_p_fy is not None:
            _res = PFy._from_sdf(_c_p_fy, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_fy")
            _p_fy = _res
        else:
            _p_fy = None
        _c_p_cx = el.find("p_cx")
        if _c_p_cx is not None:
            _res = PCx._from_sdf(_c_p_cx, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_cx")
            _p_cx = _res
        else:
            _p_cx = None
        _c_p_cy = el.find("p_cy")
        if _c_p_cy is not None:
            _res = PCy._from_sdf(_c_p_cy, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_cy")
            _p_cy = _res
        else:
            _p_cy = None
        _c_tx = el.find("tx")
        if _c_tx is not None:
            _res = Tx._from_sdf(_c_tx, version)
            if isinstance(_res, SDFError):
                return _res.extend("tx")
            _tx = _res
        else:
            _tx = None
        _c_ty = el.find("ty")
        if _c_ty is not None:
            _res = Ty._from_sdf(_c_ty, version)
            if isinstance(_res, SDFError):
                return _res.extend("ty")
            _ty = _res
        else:
            _ty = None
        return cls(sdf_version=version, p_fx=_p_fx, p_fy=_p_fy, p_cx=_p_cx, p_cy=_p_cy, tx=_tx, ty=_ty)


class Lens(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: "LensType" = None,
        scale_to_hfov: "ScaleToHfov" = None,
        custom_function: "CustomFunction" = None,
        cutoff_angle: "CutoffAngle" = None,
        env_texture_size: "EnvTextureSize" = None,
        intrinsics: "Intrinsics" = None,
        projection: "Projection" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.scale_to_hfov = scale_to_hfov
        self.custom_function = custom_function
        self.cutoff_angle = cutoff_angle
        self.env_texture_size = env_texture_size
        self.intrinsics = intrinsics
        self.projection = projection

    def to_version(self, target_version: str) -> "Lens":
        if self.intrinsics is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'intrinsics' is not supported in SDF version {target_version} (added in 1.6)")
        if self.projection is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'projection' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["scale_to_hfov"] = self.scale_to_hfov.to_version(target_version) if self.scale_to_hfov is not None else None
        kwargs["custom_function"] = self.custom_function.to_version(target_version) if self.custom_function is not None else None
        kwargs["cutoff_angle"] = self.cutoff_angle.to_version(target_version) if self.cutoff_angle is not None else None
        kwargs["env_texture_size"] = self.env_texture_size.to_version(target_version) if self.env_texture_size is not None else None
        kwargs["intrinsics"] = self.intrinsics.to_version(target_version) if self.intrinsics is not None else None
        kwargs["projection"] = self.projection.to_version(target_version) if self.projection is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lens")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.scale_to_hfov is not None:
            el.append(self.scale_to_hfov.to_sdf(version))
        if self.custom_function is not None:
            el.append(self.custom_function.to_sdf(version))
        if self.cutoff_angle is not None:
            el.append(self.cutoff_angle.to_sdf(version))
        if self.env_texture_size is not None:
            el.append(self.env_texture_size.to_sdf(version))
        if self.intrinsics is not None:
            el.append(self.intrinsics.to_sdf(version))
        if self.projection is not None:
            el.append(self.projection.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_type = el.find("type")
        if _c_type is not None:
            _res = LensType._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        _c_scale_to_hfov = el.find("scale_to_hfov")
        if _c_scale_to_hfov is not None:
            _res = ScaleToHfov._from_sdf(_c_scale_to_hfov, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale_to_hfov")
            _scale_to_hfov = _res
        else:
            _scale_to_hfov = None
        _c_custom_function = el.find("custom_function")
        if _c_custom_function is not None:
            _res = CustomFunction._from_sdf(_c_custom_function, version)
            if isinstance(_res, SDFError):
                return _res.extend("custom_function")
            _custom_function = _res
        else:
            _custom_function = None
        _c_cutoff_angle = el.find("cutoff_angle")
        if _c_cutoff_angle is not None:
            _res = CutoffAngle._from_sdf(_c_cutoff_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("cutoff_angle")
            _cutoff_angle = _res
        else:
            _cutoff_angle = None
        _c_env_texture_size = el.find("env_texture_size")
        if _c_env_texture_size is not None:
            _res = EnvTextureSize._from_sdf(_c_env_texture_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("env_texture_size")
            _env_texture_size = _res
        else:
            _env_texture_size = None
        _c_intrinsics = el.find("intrinsics")
        if _c_intrinsics is not None:
            _res = Intrinsics._from_sdf(_c_intrinsics, version)
            if isinstance(_res, SDFError):
                return _res.extend("intrinsics")
            _intrinsics = _res
        else:
            _intrinsics = None
        if _intrinsics is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'intrinsics' is not supported in SDF version {version} (added in 1.6)")
        _c_projection = el.find("projection")
        if _c_projection is not None:
            _res = Projection._from_sdf(_c_projection, version)
            if isinstance(_res, SDFError):
                return _res.extend("projection")
            _projection = _res
        else:
            _projection = None
        if _projection is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'projection' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, type=_type, scale_to_hfov=_scale_to_hfov, custom_function=_custom_function, cutoff_angle=_cutoff_angle, env_texture_size=_env_texture_size, intrinsics=_intrinsics, projection=_projection)


class K1(BaseModel):
    def __init__(self, sdf_version: str, k1: float = 0.0):
        self.__version__ = sdf_version
        self.k1 = k1

    def to_version(self, target_version: str) -> "K1":
        kwargs = {"sdf_version": target_version}
        kwargs["k1"] = self.k1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k1")
        if self.k1 is not None:
            el.text = str(self.k1)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k1 = _parse_double(_text)
        if isinstance(_k1, SDFError):
            return _k1
        return cls(sdf_version=version, k1=_k1)


class K2(BaseModel):
    def __init__(self, sdf_version: str, k2: float = 0.0):
        self.__version__ = sdf_version
        self.k2 = k2

    def to_version(self, target_version: str) -> "K2":
        kwargs = {"sdf_version": target_version}
        kwargs["k2"] = self.k2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k2")
        if self.k2 is not None:
            el.text = str(self.k2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k2 = _parse_double(_text)
        if isinstance(_k2, SDFError):
            return _k2
        return cls(sdf_version=version, k2=_k2)


class K3(BaseModel):
    def __init__(self, sdf_version: str, k3: float = 0.0):
        self.__version__ = sdf_version
        self.k3 = k3

    def to_version(self, target_version: str) -> "K3":
        kwargs = {"sdf_version": target_version}
        kwargs["k3"] = self.k3
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k3")
        if self.k3 is not None:
            el.text = str(self.k3)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k3 = _parse_double(_text)
        if isinstance(_k3, SDFError):
            return _k3
        return cls(sdf_version=version, k3=_k3)


class P1(BaseModel):
    def __init__(self, sdf_version: str, p1: float = 0.0):
        self.__version__ = sdf_version
        self.p1 = p1

    def to_version(self, target_version: str) -> "P1":
        kwargs = {"sdf_version": target_version}
        kwargs["p1"] = self.p1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p1")
        if self.p1 is not None:
            el.text = str(self.p1)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _p1 = _parse_double(_text)
        if isinstance(_p1, SDFError):
            return _p1
        return cls(sdf_version=version, p1=_p1)


class P2(BaseModel):
    def __init__(self, sdf_version: str, p2: float = 0.0):
        self.__version__ = sdf_version
        self.p2 = p2

    def to_version(self, target_version: str) -> "P2":
        kwargs = {"sdf_version": target_version}
        kwargs["p2"] = self.p2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p2")
        if self.p2 is not None:
            el.text = str(self.p2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _p2 = _parse_double(_text)
        if isinstance(_p2, SDFError):
            return _p2
        return cls(sdf_version=version, p2=_p2)


class Center(BaseModel):
    def __init__(self, sdf_version: str, center: _SDFVector2d = None):
        self.__version__ = sdf_version
        if center is None:
            center = _SDFVector2d.from_sdf("0.5 0.5")
        self.center = center

    def to_version(self, target_version: str) -> "Center":
        kwargs = {"sdf_version": target_version}
        kwargs["center"] = self.center
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("center")
        if self.center is not None:
            el.text = self.center.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.5 0.5"
        _center = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_center, SDFError):
            return _center
        return cls(sdf_version=version, center=_center)


class Distortion(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        k1: "K1" = None,
        k2: "K2" = None,
        k3: "K3" = None,
        p1: "P1" = None,
        p2: "P2" = None,
        center: "Center" = None
    ):
        self.__version__ = sdf_version
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.p1 = p1
        self.p2 = p2
        self.center = center

    def to_version(self, target_version: str) -> "Distortion":
        kwargs = {"sdf_version": target_version}
        kwargs["k1"] = self.k1.to_version(target_version) if self.k1 is not None else None
        kwargs["k2"] = self.k2.to_version(target_version) if self.k2 is not None else None
        kwargs["k3"] = self.k3.to_version(target_version) if self.k3 is not None else None
        kwargs["p1"] = self.p1.to_version(target_version) if self.p1 is not None else None
        kwargs["p2"] = self.p2.to_version(target_version) if self.p2 is not None else None
        kwargs["center"] = self.center.to_version(target_version) if self.center is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("distortion")
        if self.k1 is not None:
            el.append(self.k1.to_sdf(version))
        if self.k2 is not None:
            el.append(self.k2.to_sdf(version))
        if self.k3 is not None:
            el.append(self.k3.to_sdf(version))
        if self.p1 is not None:
            el.append(self.p1.to_sdf(version))
        if self.p2 is not None:
            el.append(self.p2.to_sdf(version))
        if self.center is not None:
            el.append(self.center.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_k1 = el.find("k1")
        if _c_k1 is not None:
            _res = K1._from_sdf(_c_k1, version)
            if isinstance(_res, SDFError):
                return _res.extend("k1")
            _k1 = _res
        else:
            _k1 = None
        _c_k2 = el.find("k2")
        if _c_k2 is not None:
            _res = K2._from_sdf(_c_k2, version)
            if isinstance(_res, SDFError):
                return _res.extend("k2")
            _k2 = _res
        else:
            _k2 = None
        _c_k3 = el.find("k3")
        if _c_k3 is not None:
            _res = K3._from_sdf(_c_k3, version)
            if isinstance(_res, SDFError):
                return _res.extend("k3")
            _k3 = _res
        else:
            _k3 = None
        _c_p1 = el.find("p1")
        if _c_p1 is not None:
            _res = P1._from_sdf(_c_p1, version)
            if isinstance(_res, SDFError):
                return _res.extend("p1")
            _p1 = _res
        else:
            _p1 = None
        _c_p2 = el.find("p2")
        if _c_p2 is not None:
            _res = P2._from_sdf(_c_p2, version)
            if isinstance(_res, SDFError):
                return _res.extend("p2")
            _p2 = _res
        else:
            _p2 = None
        _c_center = el.find("center")
        if _c_center is not None:
            _res = Center._from_sdf(_c_center, version)
            if isinstance(_res, SDFError):
                return _res.extend("center")
            _center = _res
        else:
            _center = None
        return cls(sdf_version=version, k1=_k1, k2=_k2, k3=_k3, p1=_p1, p2=_p2, center=_center)


class FramePose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(self, sdf_version: str, pose: _SDFPose = None, frame: str = ""):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame

    def to_version(self, target_version: str) -> "FramePose":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.frame is not None:
            el.set("frame", self.frame)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        return cls(sdf_version=version, pose=_pose, frame=_frame)


class Frame(BaseModel):
    def __init__(self, sdf_version: str, name: str = "", pose: "FramePose" = None):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "Frame":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = FramePose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, name=_name, pose=_pose)


class OpticalFrameId(BaseModel):
    def __init__(self, sdf_version: str, optical_frame_id: str = ""):
        self.__version__ = sdf_version
        self.optical_frame_id = optical_frame_id

    def to_version(self, target_version: str) -> "OpticalFrameId":
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["optical_frame_id"] = self.optical_frame_id
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("optical_frame_id")
        if self.optical_frame_id is not None:
            el.text = self.optical_frame_id
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _optical_frame_id = _text
        if isinstance(_optical_frame_id, SDFError):
            return _optical_frame_id
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            if _optical_frame_id != "":
                return SDFError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, optical_frame_id=_optical_frame_id)


class CameraInfoTopic(BaseModel):
    def __init__(self, sdf_version: str, camera_info_topic: str = "__default__"):
        self.__version__ = sdf_version
        self.camera_info_topic = camera_info_topic

    def to_version(self, target_version: str) -> "CameraInfoTopic":
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["camera_info_topic"] = self.camera_info_topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera_info_topic")
        if self.camera_info_topic is not None:
            el.text = self.camera_info_topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _camera_info_topic = _text
        if isinstance(_camera_info_topic, SDFError):
            return _camera_info_topic
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            if _camera_info_topic != "__default__":
                return SDFError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, camera_info_topic=_camera_info_topic)


class VisibilityMask(BaseModel):
    def __init__(self, sdf_version: str, visibility_mask: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "VisibilityMask":
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_mask"] = self.visibility_mask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visibility_mask")
        if self.visibility_mask is not None:
            el.text = str(self.visibility_mask)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4294967295
        _visibility_mask = _parse_uint32(_text)
        if isinstance(_visibility_mask, SDFError):
            return _visibility_mask
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            if _visibility_mask != 4294967295:
                return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_mask=_visibility_mask)


class SegmentationType(BaseModel):
    def __init__(self, sdf_version: str, segmentation_type: str = "semantic"):
        self.__version__ = sdf_version
        self.segmentation_type = segmentation_type

    def to_version(self, target_version: str) -> "SegmentationType":
        if self.segmentation_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["segmentation_type"] = self.segmentation_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("segmentation_type")
        if self.segmentation_type is not None:
            el.text = self.segmentation_type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "semantic"
        _segmentation_type = _text
        if isinstance(_segmentation_type, SDFError):
            return _segmentation_type
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            if _segmentation_type != "semantic":
                return SDFError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, segmentation_type=_segmentation_type)


class BoxType(BaseModel):
    def __init__(self, sdf_version: str, box_type: str = "2d"):
        self.__version__ = sdf_version
        self.box_type = box_type

    def to_version(self, target_version: str) -> "BoxType":
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["box_type"] = self.box_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("box_type")
        if self.box_type is not None:
            el.text = self.box_type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "2d"
        _box_type = _text
        if isinstance(_box_type, SDFError):
            return _box_type
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            if _box_type != "2d":
                return SDFError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, box_type=_box_type)


class Triggered(BaseModel):
    def __init__(self, sdf_version: str, triggered: bool = False):
        self.__version__ = sdf_version
        self.triggered = triggered

    def to_version(self, target_version: str) -> "Triggered":
        if self.triggered is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["triggered"] = self.triggered
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("triggered")
        if self.triggered is not None:
            el.text = str(self.triggered).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _triggered = str(_text).strip().lower() == 'true'
        if isinstance(_triggered, SDFError):
            return _triggered
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            if _triggered != False:
                return SDFError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, triggered=_triggered)


class TriggerTopic(BaseModel):
    def __init__(self, sdf_version: str, trigger_topic: str = ""):
        self.__version__ = sdf_version
        self.trigger_topic = trigger_topic

    def to_version(self, target_version: str) -> "TriggerTopic":
        if self.trigger_topic is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["trigger_topic"] = self.trigger_topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("trigger_topic")
        if self.trigger_topic is not None:
            el.text = self.trigger_topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _trigger_topic = _text
        if isinstance(_trigger_topic, SDFError):
            return _trigger_topic
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            if _trigger_topic != "":
                return SDFError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, trigger_topic=_trigger_topic)


class Camera(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        horizontal_fov: "HorizontalFov" = None,
        image: "Image" = None,
        clip: "Clip" = None,
        save: "Save" = None,
        depth_camera: "DepthCamera" = None,
        pose: "Pose" = None,
        noise: "Noise" = None,
        lens: "Lens" = None,
        distortion: "Distortion" = None,
        frame: List["Frame"] = None,
        optical_frame_id: "OpticalFrameId" = None,
        camera_info_topic: "CameraInfoTopic" = None,
        visibility_mask: "VisibilityMask" = None,
        segmentation_type: "SegmentationType" = None,
        box_type: "BoxType" = None,
        triggered: "Triggered" = None,
        trigger_topic: "TriggerTopic" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.horizontal_fov = horizontal_fov
        self.image = image
        self.clip = clip
        self.save = save
        self.depth_camera = depth_camera
        self.pose = pose
        self.noise = noise
        self.lens = lens
        self.distortion = distortion
        self.frame = frame or []
        self.optical_frame_id = optical_frame_id
        self.camera_info_topic = camera_info_topic
        self.visibility_mask = visibility_mask
        self.segmentation_type = segmentation_type
        self.box_type = box_type
        self.triggered = triggered
        self.trigger_topic = trigger_topic

    def to_version(self, target_version: str) -> "Camera":
        if self.name is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.3)")
        if self.pose is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.3)")
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.lens is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'lens' is not supported in SDF version {target_version} (added in 1.5)")
        if self.distortion is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'distortion' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        if self.segmentation_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.9)")
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
        if self.triggered is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.9)")
        if self.trigger_topic is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["horizontal_fov"] = self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        kwargs["save"] = self.save.to_version(target_version) if self.save is not None else None
        kwargs["depth_camera"] = self.depth_camera.to_version(target_version) if self.depth_camera is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["lens"] = self.lens.to_version(target_version) if self.lens is not None else None
        kwargs["distortion"] = self.distortion.to_version(target_version) if self.distortion is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["optical_frame_id"] = self.optical_frame_id.to_version(target_version) if self.optical_frame_id is not None else None
        kwargs["camera_info_topic"] = self.camera_info_topic.to_version(target_version) if self.camera_info_topic is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        kwargs["segmentation_type"] = self.segmentation_type.to_version(target_version) if self.segmentation_type is not None else None
        kwargs["box_type"] = self.box_type.to_version(target_version) if self.box_type is not None else None
        kwargs["triggered"] = self.triggered.to_version(target_version) if self.triggered is not None else None
        kwargs["trigger_topic"] = self.trigger_topic.to_version(target_version) if self.trigger_topic is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera")
        if self.name is not None:
            el.set("name", self.name)
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf(version))
        if self.image is None:
            self.image = Image(sdf_version=version)
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.clip is None:
            self.clip = Clip(sdf_version=version)
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        if self.save is not None:
            el.append(self.save.to_sdf(version))
        if self.depth_camera is not None:
            el.append(self.depth_camera.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.lens is not None:
            el.append(self.lens.to_sdf(version))
        if self.distortion is not None:
            el.append(self.distortion.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.optical_frame_id is not None:
            el.append(self.optical_frame_id.to_sdf(version))
        if self.camera_info_topic is not None:
            el.append(self.camera_info_topic.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        if self.segmentation_type is not None:
            el.append(self.segmentation_type.to_sdf(version))
        if self.box_type is not None:
            el.append(self.box_type.to_sdf(version))
        if self.triggered is not None:
            el.append(self.triggered.to_sdf(version))
        if self.trigger_topic is not None:
            el.append(self.trigger_topic.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        if _name is not None and cmp_version(version, "1.3") < 0:
            if _name != "__default__":
                return SDFError(f"'name' is not supported in SDF version {version} (added in 1.3)")
        _c_horizontal_fov = el.find("horizontal_fov")
        if _c_horizontal_fov is not None:
            _res = HorizontalFov._from_sdf(_c_horizontal_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal_fov")
            _horizontal_fov = _res
        else:
            _horizontal_fov = None
        _c_image = el.find("image")
        if _c_image is not None:
            _res = Image._from_sdf(_c_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        else:
            _res = Image._from_sdf(ET.Element("image"), version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        _c_clip = el.find("clip")
        if _c_clip is not None:
            _res = Clip._from_sdf(_c_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        else:
            _res = Clip._from_sdf(ET.Element("clip"), version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        _c_save = el.find("save")
        if _c_save is not None:
            _res = Save._from_sdf(_c_save, version)
            if isinstance(_res, SDFError):
                return _res.extend("save")
            _save = _res
        else:
            _save = None
        _c_depth_camera = el.find("depth_camera")
        if _c_depth_camera is not None:
            _res = DepthCamera._from_sdf(_c_depth_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("depth_camera")
            _depth_camera = _res
        else:
            _depth_camera = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.3)")
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_lens = el.find("lens")
        if _c_lens is not None:
            _res = Lens._from_sdf(_c_lens, version)
            if isinstance(_res, SDFError):
                return _res.extend("lens")
            _lens = _res
        else:
            _lens = None
        if _lens is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'lens' is not supported in SDF version {version} (added in 1.5)")
        _c_distortion = el.find("distortion")
        if _c_distortion is not None:
            _res = Distortion._from_sdf(_c_distortion, version)
            if isinstance(_res, SDFError):
                return _res.extend("distortion")
            _distortion = _res
        else:
            _distortion = None
        if _distortion is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'distortion' is not supported in SDF version {version} (added in 1.5)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_optical_frame_id = el.find("optical_frame_id")
        if _c_optical_frame_id is not None:
            _res = OpticalFrameId._from_sdf(_c_optical_frame_id, version)
            if isinstance(_res, SDFError):
                return _res.extend("optical_frame_id")
            _optical_frame_id = _res
        else:
            _optical_frame_id = None
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        _c_camera_info_topic = el.find("camera_info_topic")
        if _c_camera_info_topic is not None:
            _res = CameraInfoTopic._from_sdf(_c_camera_info_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera_info_topic")
            _camera_info_topic = _res
        else:
            _camera_info_topic = None
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        _c_visibility_mask = el.find("visibility_mask")
        if _c_visibility_mask is not None:
            _res = VisibilityMask._from_sdf(_c_visibility_mask, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_mask")
            _visibility_mask = _res
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        _c_segmentation_type = el.find("segmentation_type")
        if _c_segmentation_type is not None:
            _res = SegmentationType._from_sdf(_c_segmentation_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("segmentation_type")
            _segmentation_type = _res
        else:
            _segmentation_type = None
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        _c_box_type = el.find("box_type")
        if _c_box_type is not None:
            _res = BoxType._from_sdf(_c_box_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("box_type")
            _box_type = _res
        else:
            _box_type = None
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        _c_triggered = el.find("triggered")
        if _c_triggered is not None:
            _res = Triggered._from_sdf(_c_triggered, version)
            if isinstance(_res, SDFError):
                return _res.extend("triggered")
            _triggered = _res
        else:
            _triggered = None
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        _c_trigger_topic = el.find("trigger_topic")
        if _c_trigger_topic is not None:
            _res = TriggerTopic._from_sdf(_c_trigger_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("trigger_topic")
            _trigger_topic = _res
        else:
            _trigger_topic = None
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, name=_name, horizontal_fov=_horizontal_fov, image=_image, clip=_clip, save=_save, depth_camera=_depth_camera, pose=_pose, noise=_noise, lens=_lens, distortion=_distortion, frame=_frame, optical_frame_id=_optical_frame_id, camera_info_topic=_camera_info_topic, visibility_mask=_visibility_mask, segmentation_type=_segmentation_type, box_type=_box_type, triggered=_triggered, trigger_topic=_trigger_topic)


class MaxAngle(BaseModel):
    def __init__(self, sdf_version: str, max_angle: float = 0):
        self.__version__ = sdf_version
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "MaxAngle":
        if self.max_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_angle")
        if self.max_angle is not None:
            el.text = str(self.max_angle)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max_angle = _parse_double(_text)
        if isinstance(_max_angle, SDFError):
            return _max_angle
        if _max_angle is not None and cmp_version(version, "1.2") < 0:
            if _max_angle != 0:
                return SDFError(f"'max_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max_angle=_max_angle)


class MinAngle(BaseModel):
    def __init__(self, sdf_version: str, min_angle: float = 0):
        self.__version__ = sdf_version
        self.min_angle = min_angle

    def to_version(self, target_version: str) -> "MinAngle":
        if self.min_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["min_angle"] = self.min_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_angle")
        if self.min_angle is not None:
            el.text = str(self.min_angle)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min_angle = _parse_double(_text)
        if isinstance(_min_angle, SDFError):
            return _min_angle
        if _min_angle is not None and cmp_version(version, "1.2") < 0:
            if _min_angle != 0:
                return SDFError(f"'min_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min_angle=_min_angle)


class Samples(BaseModel):
    def __init__(self, sdf_version: str, samples: int = 640):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "Samples":
        if self.samples is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'samples' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("samples")
        if self.samples is not None:
            el.text = str(self.samples)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 640
        _samples = _parse_uint32(_text)
        if isinstance(_samples, SDFError):
            return _samples
        if _samples is not None and cmp_version(version, "1.2") < 0:
            if _samples != 640:
                return SDFError(f"'samples' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, samples=_samples)


class Resolution(BaseModel):
    def __init__(self, sdf_version: str, resolution: float = 1):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Resolution":
        if self.resolution is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["resolution"] = self.resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("resolution")
        if self.resolution is not None:
            el.text = str(self.resolution)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _resolution = _parse_double(_text)
        if isinstance(_resolution, SDFError):
            return _resolution
        if _resolution is not None and cmp_version(version, "1.2") < 0:
            if _resolution != 1:
                return SDFError(f"'resolution' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, resolution=_resolution)


class Horizontal(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        samples: int = 1,
        resolution: float = 1,
        min_angle: float = 0,
        max_angle: float = 0
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "Horizontal":
        if self.samples is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'samples' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.min_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.max_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        kwargs["resolution"] = self.resolution
        kwargs["min_angle"] = self.min_angle
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.samples is not None:
            el.set("samples", str(self.samples))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        if self.min_angle is not None:
            el.set("min_angle", str(self.min_angle))
        if self.max_angle is not None:
            el.set("max_angle", str(self.max_angle))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _samples = _parse_uint32(el.get("samples", 1))
        if isinstance(_samples, SDFError):
            return _samples.extend("@samples")
        _resolution = _parse_double(el.get("resolution", 1))
        if isinstance(_resolution, SDFError):
            return _resolution.extend("@resolution")
        _min_angle = _parse_double(el.get("min_angle", 0))
        if isinstance(_min_angle, SDFError):
            return _min_angle.extend("@min_angle")
        _max_angle = _parse_double(el.get("max_angle", 0))
        if isinstance(_max_angle, SDFError):
            return _max_angle.extend("@max_angle")
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class VerticalSamples(BaseModel):
    def __init__(self, sdf_version: str, samples: int = 1):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "VerticalSamples":
        if self.samples is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'samples' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("samples")
        if self.samples is not None:
            el.text = str(self.samples)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _samples = _parse_uint32(_text)
        if isinstance(_samples, SDFError):
            return _samples
        if _samples is not None and cmp_version(version, "1.2") < 0:
            if _samples != 1:
                return SDFError(f"'samples' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, samples=_samples)


class Vertical(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        samples: int = 1,
        resolution: float = 1,
        min_angle: float = 0,
        max_angle: float = 0
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "Vertical":
        if self.samples is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'samples' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.min_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.max_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        kwargs["resolution"] = self.resolution
        kwargs["min_angle"] = self.min_angle
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.samples is not None:
            el.set("samples", str(self.samples))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        if self.min_angle is not None:
            el.set("min_angle", str(self.min_angle))
        if self.max_angle is not None:
            el.set("max_angle", str(self.max_angle))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _samples = _parse_uint32(el.get("samples", 1))
        if isinstance(_samples, SDFError):
            return _samples.extend("@samples")
        _resolution = _parse_double(el.get("resolution", 1))
        if isinstance(_resolution, SDFError):
            return _resolution.extend("@resolution")
        _min_angle = _parse_double(el.get("min_angle", 0))
        if isinstance(_min_angle, SDFError):
            return _min_angle.extend("@min_angle")
        _max_angle = _parse_double(el.get("max_angle", 0))
        if isinstance(_max_angle, SDFError):
            return _max_angle.extend("@max_angle")
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class Scan(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "Horizontal" = None,
        vertical: "Vertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "Scan":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scan")
        if self.horizontal is None:
            self.horizontal = Horizontal(sdf_version=version)
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_horizontal = el.find("horizontal")
        if _c_horizontal is not None:
            _res = Horizontal._from_sdf(_c_horizontal, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        else:
            _res = Horizontal._from_sdf(ET.Element("horizontal"), version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        _c_vertical = el.find("vertical")
        if _c_vertical is not None:
            _res = Vertical._from_sdf(_c_vertical, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical")
            _vertical = _res
        else:
            _vertical = None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Min(BaseModel):
    def __init__(self, sdf_version: str, min: float = 0):
        self.__version__ = sdf_version
        self.min = min

    def to_version(self, target_version: str) -> "Min":
        if self.min is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'min' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min")
        if self.min is not None:
            el.text = str(self.min)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min = _parse_double(_text)
        if isinstance(_min, SDFError):
            return _min
        if _min is not None and cmp_version(version, "1.2") < 0:
            if _min != 0:
                return SDFError(f"'min' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min=_min)


class Max(BaseModel):
    def __init__(self, sdf_version: str, max: float = 0):
        self.__version__ = sdf_version
        self.max = max

    def to_version(self, target_version: str) -> "Max":
        if self.max is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'max' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["max"] = self.max
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max")
        if self.max is not None:
            el.text = str(self.max)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max = _parse_double(_text)
        if isinstance(_max, SDFError):
            return _max
        if _max is not None and cmp_version(version, "1.2") < 0:
            if _max != 0:
                return SDFError(f"'max' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max=_max)


class RangeResolution(BaseModel):
    def __init__(self, sdf_version: str, resolution: float = 0):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "RangeResolution":
        if self.resolution is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["resolution"] = self.resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("resolution")
        if self.resolution is not None:
            el.text = str(self.resolution)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _resolution = _parse_double(_text)
        if isinstance(_resolution, SDFError):
            return _resolution
        if _resolution is not None and cmp_version(version, "1.2") < 0:
            if _resolution != 0:
                return SDFError(f"'resolution' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, resolution=_resolution)


class Range(BaseModel):
    def __init__(self, sdf_version: str, min: float = 0, max: float = 0, resolution: float = 0):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Range":
        if self.min is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'min' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.max is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'max' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min
        kwargs["max"] = self.max
        kwargs["resolution"] = self.resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.min is not None:
            el.set("min", str(self.min))
        if self.max is not None:
            el.set("max", str(self.max))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _min = _parse_double(el.get("min", 0))
        if isinstance(_min, SDFError):
            return _min.extend("@min")
        _max = _parse_double(el.get("max", 0))
        if isinstance(_max, SDFError):
            return _max.extend("@max")
        _resolution = _parse_double(el.get("resolution", 0))
        if isinstance(_resolution, SDFError):
            return _resolution.extend("@resolution")
        return cls(sdf_version=version, min=_min, max=_max, resolution=_resolution)


class Ray(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        scan: "Scan" = None,
        range: "Range" = None,
        noise: "Noise" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.scan = scan
        self.range = range
        self.noise = noise
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "Ray":
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ray")
        if self.scan is None:
            self.scan = Scan(sdf_version=version)
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is None:
            self.range = Range(sdf_version=version)
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_scan = el.find("scan")
        if _c_scan is not None:
            _res = Scan._from_sdf(_c_scan, version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        else:
            _res = Scan._from_sdf(ET.Element("scan"), version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        _c_range = el.find("range")
        if _c_range is not None:
            _res = Range._from_sdf(_c_range, version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        else:
            _res = Range._from_sdf(ET.Element("range"), version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_visibility_mask = el.find("visibility_mask")
        if _c_visibility_mask is not None:
            _res = VisibilityMask._from_sdf(_c_visibility_mask, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_mask")
            _visibility_mask = _res
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)


class Collision(BaseModel):
    def __init__(self, sdf_version: str, collision: str = "__default__", name: str = "__default__"):
        self.__version__ = sdf_version
        self.collision = collision
        self.name = name

    def to_version(self, target_version: str) -> "Collision":
        if self.name is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = self.collision
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision")
        if self.collision is not None:
            el.text = self.collision
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _collision = _text
        if isinstance(_collision, SDFError):
            return _collision
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, collision=_collision, name=_name)


class Topic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = "__default_topic__"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "Topic":
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default_topic__"
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


class Contact(BaseModel):
    def __init__(self, sdf_version: str, collision: "Collision" = None, topic: "Topic" = None):
        self.__version__ = sdf_version
        self.collision = collision
        self.topic = topic

    def to_version(self, target_version: str) -> "Contact":
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = self.collision.to_version(target_version) if self.collision is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.collision is not None:
            el.append(self.collision.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_collision = el.find("collision")
        if _c_collision is not None:
            _res = Collision._from_sdf(_c_collision, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collision = _res
        else:
            _collision = None
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = Topic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        return cls(sdf_version=version, collision=_collision, topic=_topic)


class Rfidtag(BaseModel):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "Rfidtag":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rfidtag")
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Rfid(BaseModel):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "Rfid":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rfid")
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Origin(BaseModel):
    def __init__(self, sdf_version: str, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "Origin":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("origin")
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _pose = _SDFPose._from_sdf(el.get("pose", "0 0 0 0 0 0"), version)
        if isinstance(_pose, SDFError):
            return _pose.extend("@pose")
        return cls(sdf_version=version, pose=_pose)


class SensorTopic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = "__default"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "SensorTopic":
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default"
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


class UpdateRate(BaseModel):
    def __init__(self, sdf_version: str, update_rate: float = 0):
        self.__version__ = sdf_version
        self.update_rate = update_rate

    def to_version(self, target_version: str) -> "UpdateRate":
        if self.update_rate is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'update_rate' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["update_rate"] = self.update_rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("update_rate")
        if self.update_rate is not None:
            el.text = str(self.update_rate)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _update_rate = _parse_double(_text)
        if isinstance(_update_rate, SDFError):
            return _update_rate
        if _update_rate is not None and cmp_version(version, "1.2") < 0:
            if _update_rate != 0:
                return SDFError(f"'update_rate' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, update_rate=_update_rate)


class AlwaysOn(BaseModel):
    def __init__(self, sdf_version: str, always_on: bool = False):
        self.__version__ = sdf_version
        self.always_on = always_on

    def to_version(self, target_version: str) -> "AlwaysOn":
        if self.always_on is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'always_on' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["always_on"] = self.always_on
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("always_on")
        if self.always_on is not None:
            el.text = str(self.always_on).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _always_on = str(_text).strip().lower() == 'true'
        if isinstance(_always_on, SDFError):
            return _always_on
        if _always_on is not None and cmp_version(version, "1.2") < 0:
            if _always_on != False:
                return SDFError(f"'always_on' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, always_on=_always_on)


class Visualize(BaseModel):
    def __init__(self, sdf_version: str, visualize: bool = False):
        self.__version__ = sdf_version
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Visualize":
        if self.visualize is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["visualize"] = self.visualize
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visualize")
        if self.visualize is not None:
            el.text = str(self.visualize).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _visualize = str(_text).strip().lower() == 'true'
        if isinstance(_visualize, SDFError):
            return _visualize
        if _visualize is not None and cmp_version(version, "1.2") < 0:
            if _visualize != False:
                return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, visualize=_visualize)


class BiasMean(BaseModel):
    def __init__(self, sdf_version: str, bias_mean: float = 0.0):
        self.__version__ = sdf_version
        self.bias_mean = bias_mean

    def to_version(self, target_version: str) -> "BiasMean":
        kwargs = {"sdf_version": target_version}
        kwargs["bias_mean"] = self.bias_mean
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bias_mean")
        if self.bias_mean is not None:
            el.text = str(self.bias_mean)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _bias_mean = _parse_double(_text)
        if isinstance(_bias_mean, SDFError):
            return _bias_mean
        return cls(sdf_version=version, bias_mean=_bias_mean)


class BiasStddev(BaseModel):
    def __init__(self, sdf_version: str, bias_stddev: float = 0.0):
        self.__version__ = sdf_version
        self.bias_stddev = bias_stddev

    def to_version(self, target_version: str) -> "BiasStddev":
        kwargs = {"sdf_version": target_version}
        kwargs["bias_stddev"] = self.bias_stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bias_stddev")
        if self.bias_stddev is not None:
            el.text = str(self.bias_stddev)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _bias_stddev = _parse_double(_text)
        if isinstance(_bias_stddev, SDFError):
            return _bias_stddev
        return cls(sdf_version=version, bias_stddev=_bias_stddev)


class Rate(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev

    def to_version(self, target_version: str) -> "Rate":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rate")
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        return cls(sdf_version=version, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev)


class Accel(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev

    def to_version(self, target_version: str) -> "Accel":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("accel")
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        return cls(sdf_version=version, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev)


class ImuNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        rate: "Rate" = None,
        accel: "Accel" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.rate = rate
        self.accel = accel

    def to_version(self, target_version: str) -> "ImuNoise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["rate"] = self.rate.to_version(target_version) if self.rate is not None else None
        kwargs["accel"] = self.accel.to_version(target_version) if self.accel is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.rate is None:
            self.rate = Rate(sdf_version=version)
        if self.rate is not None:
            el.append(self.rate.to_sdf(version))
        if self.accel is None:
            self.accel = Accel(sdf_version=version)
        if self.accel is not None:
            el.append(self.accel.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        _c_rate = el.find("rate")
        if _c_rate is not None:
            _res = Rate._from_sdf(_c_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("rate")
            _rate = _res
        else:
            _res = Rate._from_sdf(ET.Element("rate"), version)
            if isinstance(_res, SDFError):
                return _res.extend("rate")
            _rate = _res
        _c_accel = el.find("accel")
        if _c_accel is not None:
            _res = Accel._from_sdf(_c_accel, version)
            if isinstance(_res, SDFError):
                return _res.extend("accel")
            _accel = _res
        else:
            _res = Accel._from_sdf(ET.Element("accel"), version)
            if isinstance(_res, SDFError):
                return _res.extend("accel")
            _accel = _res
        return cls(sdf_version=version, type=_type, rate=_rate, accel=_accel)


class Precision(BaseModel):
    def __init__(self, sdf_version: str, precision: float = 0.0):
        self.__version__ = sdf_version
        self.precision = precision

    def to_version(self, target_version: str) -> "Precision":
        kwargs = {"sdf_version": target_version}
        kwargs["precision"] = self.precision
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("precision")
        if self.precision is not None:
            el.text = str(self.precision)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _precision = _parse_double(_text)
        if isinstance(_precision, SDFError):
            return _precision
        return cls(sdf_version=version, precision=_precision)


class DynamicBiasCorrelationTime(BaseModel):
    def __init__(self, sdf_version: str, dynamic_bias_correlation_time: float = 0.0):
        self.__version__ = sdf_version
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time

    def to_version(self, target_version: str) -> "DynamicBiasCorrelationTime":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamic_bias_correlation_time")
        if self.dynamic_bias_correlation_time is not None:
            el.text = str(self.dynamic_bias_correlation_time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _dynamic_bias_correlation_time = _parse_double(_text)
        if isinstance(_dynamic_bias_correlation_time, SDFError):
            return _dynamic_bias_correlation_time
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            if _dynamic_bias_correlation_time != 0.0:
                return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, dynamic_bias_correlation_time=_dynamic_bias_correlation_time)


class DynamicBiasStddev(BaseModel):
    def __init__(self, sdf_version: str, dynamic_bias_stddev: float = 0.0):
        self.__version__ = sdf_version
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "DynamicBiasStddev":
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamic_bias_stddev")
        if self.dynamic_bias_stddev is not None:
            el.text = str(self.dynamic_bias_stddev)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _dynamic_bias_stddev = _parse_double(_text)
        if isinstance(_dynamic_bias_stddev, SDFError):
            return _dynamic_bias_stddev
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            if _dynamic_bias_stddev != 0.0:
                return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, dynamic_bias_stddev=_dynamic_bias_stddev)


class XNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "XNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class X(BaseModel):
    def __init__(self, sdf_version: str, noise: "XNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "X":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("x")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = XNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class YNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "YNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class Y(BaseModel):
    def __init__(self, sdf_version: str, noise: "YNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Y":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("y")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = YNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class ZNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "ZNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class Z(BaseModel):
    def __init__(self, sdf_version: str, noise: "ZNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Z":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("z")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = ZNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class LinearAcceleration(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "LinearAcceleration":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear_acceleration")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class AngularVelocity(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "AngularVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angular_velocity")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class EnableOrientation(BaseModel):
    def __init__(self, sdf_version: str, enable_orientation: bool = True):
        self.__version__ = sdf_version
        self.enable_orientation = enable_orientation

    def to_version(self, target_version: str) -> "EnableOrientation":
        if self.enable_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_orientation"] = self.enable_orientation
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_orientation")
        if self.enable_orientation is not None:
            el.text = str(self.enable_orientation).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _enable_orientation = str(_text).strip().lower() == 'true'
        if isinstance(_enable_orientation, SDFError):
            return _enable_orientation
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            if _enable_orientation != True:
                return SDFError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, enable_orientation=_enable_orientation)


class Localization(BaseModel):
    def __init__(self, sdf_version: str, localization: str = "CUSTOM"):
        self.__version__ = sdf_version
        self.localization = localization

    def to_version(self, target_version: str) -> "Localization":
        kwargs = {"sdf_version": target_version}
        kwargs["localization"] = self.localization
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("localization")
        if self.localization is not None:
            el.text = self.localization
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "CUSTOM"
        _localization = _text
        if isinstance(_localization, SDFError):
            return _localization
        return cls(sdf_version=version, localization=_localization)


class CustomRpy(BaseModel):
    def __init__(self, sdf_version: str, custom_rpy: _SDFVector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if custom_rpy is None:
            custom_rpy = _SDFVector3.from_sdf("0 0 0")
        self.custom_rpy = custom_rpy
        self.parent_frame = parent_frame

    def to_version(self, target_version: str) -> "CustomRpy":
        kwargs = {"sdf_version": target_version}
        kwargs["custom_rpy"] = self.custom_rpy
        kwargs["parent_frame"] = self.parent_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("custom_rpy")
        if self.custom_rpy is not None:
            el.text = self.custom_rpy.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _custom_rpy = _SDFVector3._from_sdf(_text, version)
        if isinstance(_custom_rpy, SDFError):
            return _custom_rpy
        _parent_frame = el.get("parent_frame", "")
        if isinstance(_parent_frame, SDFError):
            return _parent_frame.extend("@parent_frame")
        return cls(sdf_version=version, custom_rpy=_custom_rpy, parent_frame=_parent_frame)


class GravDirX(BaseModel):
    def __init__(self, sdf_version: str, grav_dir_x: _SDFVector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if grav_dir_x is None:
            grav_dir_x = _SDFVector3.from_sdf("1 0 0")
        self.grav_dir_x = grav_dir_x
        self.parent_frame = parent_frame

    def to_version(self, target_version: str) -> "GravDirX":
        kwargs = {"sdf_version": target_version}
        kwargs["grav_dir_x"] = self.grav_dir_x
        kwargs["parent_frame"] = self.parent_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grav_dir_x")
        if self.grav_dir_x is not None:
            el.text = self.grav_dir_x.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 0 0"
        _grav_dir_x = _SDFVector3._from_sdf(_text, version)
        if isinstance(_grav_dir_x, SDFError):
            return _grav_dir_x
        _parent_frame = el.get("parent_frame", "")
        if isinstance(_parent_frame, SDFError):
            return _parent_frame.extend("@parent_frame")
        return cls(sdf_version=version, grav_dir_x=_grav_dir_x, parent_frame=_parent_frame)


class OrientationReferenceFrame(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        localization: "Localization" = None,
        custom_rpy: "CustomRpy" = None,
        grav_dir_x: "GravDirX" = None
    ):
        self.__version__ = sdf_version
        self.localization = localization
        self.custom_rpy = custom_rpy
        self.grav_dir_x = grav_dir_x

    def to_version(self, target_version: str) -> "OrientationReferenceFrame":
        kwargs = {"sdf_version": target_version}
        kwargs["localization"] = self.localization.to_version(target_version) if self.localization is not None else None
        kwargs["custom_rpy"] = self.custom_rpy.to_version(target_version) if self.custom_rpy is not None else None
        kwargs["grav_dir_x"] = self.grav_dir_x.to_version(target_version) if self.grav_dir_x is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("orientation_reference_frame")
        if self.localization is not None:
            el.append(self.localization.to_sdf(version))
        if self.custom_rpy is not None:
            el.append(self.custom_rpy.to_sdf(version))
        if self.grav_dir_x is not None:
            el.append(self.grav_dir_x.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_localization = el.find("localization")
        if _c_localization is not None:
            _res = Localization._from_sdf(_c_localization, version)
            if isinstance(_res, SDFError):
                return _res.extend("localization")
            _localization = _res
        else:
            _localization = None
        _c_custom_rpy = el.find("custom_rpy")
        if _c_custom_rpy is not None:
            _res = CustomRpy._from_sdf(_c_custom_rpy, version)
            if isinstance(_res, SDFError):
                return _res.extend("custom_rpy")
            _custom_rpy = _res
        else:
            _custom_rpy = None
        _c_grav_dir_x = el.find("grav_dir_x")
        if _c_grav_dir_x is not None:
            _res = GravDirX._from_sdf(_c_grav_dir_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("grav_dir_x")
            _grav_dir_x = _res
        else:
            _grav_dir_x = None
        return cls(sdf_version=version, localization=_localization, custom_rpy=_custom_rpy, grav_dir_x=_grav_dir_x)


class Imu(BaseModel):
    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}, {"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}]}]

    def __init__(
        self,
        sdf_version: str,
        topic: "Topic" = None,
        noise: "ImuNoise" = None,
        linear_acceleration: "LinearAcceleration" = None,
        angular_velocity: "AngularVelocity" = None,
        enable_orientation: "EnableOrientation" = None,
        orientation_reference_frame: "OrientationReferenceFrame" = None
    ):
        self.__version__ = sdf_version
        self.topic = topic
        self.noise = noise
        self.linear_acceleration = linear_acceleration
        self.angular_velocity = angular_velocity
        self.enable_orientation = enable_orientation
        self.orientation_reference_frame = orientation_reference_frame

    def to_version(self, target_version: str) -> "Imu":
        if self.topic is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'topic' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.noise is not None and cmp_version(target_version, "1.6") >= 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (removed in 1.6)")
        if self.linear_acceleration is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'linear_acceleration' is not supported in SDF version {target_version} (added in 1.5)")
        if self.angular_velocity is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'angular_velocity' is not supported in SDF version {target_version} (added in 1.5)")
        if self.enable_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        if self.orientation_reference_frame is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'orientation_reference_frame' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["linear_acceleration"] = self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None else None
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if self.angular_velocity is not None else None
        kwargs["enable_orientation"] = self.enable_orientation.to_version(target_version) if self.enable_orientation is not None else None
        kwargs["orientation_reference_frame"] = self.orientation_reference_frame.to_version(target_version) if self.orientation_reference_frame is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("imu")
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf(version))
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
        if self.enable_orientation is not None:
            el.append(self.enable_orientation.to_sdf(version))
        if self.orientation_reference_frame is not None:
            el.append(self.orientation_reference_frame.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = Topic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = ImuNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_linear_acceleration = el.find("linear_acceleration")
        if _c_linear_acceleration is not None:
            _res = LinearAcceleration._from_sdf(_c_linear_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_acceleration")
            _linear_acceleration = _res
        else:
            _linear_acceleration = None
        if _linear_acceleration is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'linear_acceleration' is not supported in SDF version {version} (added in 1.5)")
        _c_angular_velocity = el.find("angular_velocity")
        if _c_angular_velocity is not None:
            _res = AngularVelocity._from_sdf(_c_angular_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_velocity")
            _angular_velocity = _res
        else:
            _angular_velocity = None
        if _angular_velocity is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'angular_velocity' is not supported in SDF version {version} (added in 1.5)")
        _c_enable_orientation = el.find("enable_orientation")
        if _c_enable_orientation is not None:
            _res = EnableOrientation._from_sdf(_c_enable_orientation, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_orientation")
            _enable_orientation = _res
        else:
            _enable_orientation = None
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        _c_orientation_reference_frame = el.find("orientation_reference_frame")
        if _c_orientation_reference_frame is not None:
            _res = OrientationReferenceFrame._from_sdf(_c_orientation_reference_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("orientation_reference_frame")
            _orientation_reference_frame = _res
        else:
            _orientation_reference_frame = None
        if _orientation_reference_frame is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'orientation_reference_frame' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, topic=_topic, noise=_noise, linear_acceleration=_linear_acceleration, angular_velocity=_angular_velocity, enable_orientation=_enable_orientation, orientation_reference_frame=_orientation_reference_frame)


class HorizontalNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "HorizontalNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class PositionSensingHorizontal(BaseModel):
    def __init__(self, sdf_version: str, noise: "HorizontalNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "PositionSensingHorizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = HorizontalNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class VerticalNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "VerticalNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class PositionSensingVertical(BaseModel):
    def __init__(self, sdf_version: str, noise: "VerticalNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "PositionSensingVertical":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = VerticalNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class PositionSensing(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "PositionSensingHorizontal" = None,
        vertical: "PositionSensingVertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "PositionSensing":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("position_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_horizontal = el.find("horizontal")
        if _c_horizontal is not None:
            _res = PositionSensingHorizontal._from_sdf(_c_horizontal, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        else:
            _horizontal = None
        _c_vertical = el.find("vertical")
        if _c_vertical is not None:
            _res = PositionSensingVertical._from_sdf(_c_vertical, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical")
            _vertical = _res
        else:
            _vertical = None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class VelocitySensingHorizontal(BaseModel):
    def __init__(self, sdf_version: str, noise: "HorizontalNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VelocitySensingHorizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = HorizontalNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class VelocitySensingVertical(BaseModel):
    def __init__(self, sdf_version: str, noise: "VerticalNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VelocitySensingVertical":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = VerticalNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class VelocitySensing(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "VelocitySensingHorizontal" = None,
        vertical: "VelocitySensingVertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "VelocitySensing":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("velocity_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_horizontal = el.find("horizontal")
        if _c_horizontal is not None:
            _res = VelocitySensingHorizontal._from_sdf(_c_horizontal, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        else:
            _horizontal = None
        _c_vertical = el.find("vertical")
        if _c_vertical is not None:
            _res = VelocitySensingVertical._from_sdf(_c_vertical, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical")
            _vertical = _res
        else:
            _vertical = None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Gps(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        position_sensing: "PositionSensing" = None,
        velocity_sensing: "VelocitySensing" = None
    ):
        self.__version__ = sdf_version
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_version(self, target_version: str) -> "Gps":
        kwargs = {"sdf_version": target_version}
        kwargs["position_sensing"] = self.position_sensing.to_version(target_version) if self.position_sensing is not None else None
        kwargs["velocity_sensing"] = self.velocity_sensing.to_version(target_version) if self.velocity_sensing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gps")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf(version))
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_position_sensing = el.find("position_sensing")
        if _c_position_sensing is not None:
            _res = PositionSensing._from_sdf(_c_position_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("position_sensing")
            _position_sensing = _res
        else:
            _position_sensing = None
        _c_velocity_sensing = el.find("velocity_sensing")
        if _c_velocity_sensing is not None:
            _res = VelocitySensing._from_sdf(_c_velocity_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity_sensing")
            _velocity_sensing = _res
        else:
            _velocity_sensing = None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class SonarMax(BaseModel):
    def __init__(self, sdf_version: str, max: float = 1.0):
        self.__version__ = sdf_version
        self.max = max

    def to_version(self, target_version: str) -> "SonarMax":
        kwargs = {"sdf_version": target_version}
        kwargs["max"] = self.max
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max")
        if self.max is not None:
            el.text = str(self.max)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _max = _parse_double(_text)
        if isinstance(_max, SDFError):
            return _max
        return cls(sdf_version=version, max=_max)


class Radius(BaseModel):
    def __init__(self, sdf_version: str, radius: float = 0.5):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Radius":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("radius")
        if self.radius is not None:
            el.text = str(self.radius)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.5
        _radius = _parse_double(_text)
        if isinstance(_radius, SDFError):
            return _radius
        return cls(sdf_version=version, radius=_radius)


class Geometry(BaseModel):
    def __init__(self, sdf_version: str, geometry: str = "cone"):
        self.__version__ = sdf_version
        self.geometry = geometry

    def to_version(self, target_version: str) -> "Geometry":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["geometry"] = self.geometry
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("geometry")
        if self.geometry is not None:
            el.text = self.geometry
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "cone"
        _geometry = _text
        if isinstance(_geometry, SDFError):
            return _geometry
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            if _geometry != "cone":
                return SDFError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, geometry=_geometry)


class Sonar(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        min: "Min" = None,
        max: "SonarMax" = None,
        radius: "Radius" = None,
        geometry: "Geometry" = None
    ):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.radius = radius
        self.geometry = geometry

    def to_version(self, target_version: str) -> "Sonar":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min.to_version(target_version) if self.min is not None else None
        kwargs["max"] = self.max.to_version(target_version) if self.max is not None else None
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sonar")
        if self.min is not None:
            el.append(self.min.to_sdf(version))
        if self.max is not None:
            el.append(self.max.to_sdf(version))
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_min = el.find("min")
        if _c_min is not None:
            _res = Min._from_sdf(_c_min, version)
            if isinstance(_res, SDFError):
                return _res.extend("min")
            _min = _res
        else:
            _min = None
        _c_max = el.find("max")
        if _c_max is not None:
            _res = SonarMax._from_sdf(_c_max, version)
            if isinstance(_res, SDFError):
                return _res.extend("max")
            _max = _res
        else:
            _max = None
        _c_radius = el.find("radius")
        if _c_radius is not None:
            _res = Radius._from_sdf(_c_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("radius")
            _radius = _res
        else:
            _radius = None
        _c_geometry = el.find("geometry")
        if _c_geometry is not None:
            _res = Geometry._from_sdf(_c_geometry, version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        else:
            _geometry = None
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, min=_min, max=_max, radius=_radius, geometry=_geometry)


class Essid(BaseModel):
    def __init__(self, sdf_version: str, essid: str = "wireless"):
        self.__version__ = sdf_version
        self.essid = essid

    def to_version(self, target_version: str) -> "Essid":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("essid")
        if self.essid is not None:
            el.text = self.essid
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "wireless"
        _essid = _text
        if isinstance(_essid, SDFError):
            return _essid
        return cls(sdf_version=version, essid=_essid)


class Frequency(BaseModel):
    def __init__(self, sdf_version: str, frequency: float = 2442):
        self.__version__ = sdf_version
        self.frequency = frequency

    def to_version(self, target_version: str) -> "Frequency":
        kwargs = {"sdf_version": target_version}
        kwargs["frequency"] = self.frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frequency")
        if self.frequency is not None:
            el.text = str(self.frequency)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2442
        _frequency = _parse_double(_text)
        if isinstance(_frequency, SDFError):
            return _frequency
        return cls(sdf_version=version, frequency=_frequency)


class MinFrequency(BaseModel):
    def __init__(self, sdf_version: str, min_frequency: float = 2412):
        self.__version__ = sdf_version
        self.min_frequency = min_frequency

    def to_version(self, target_version: str) -> "MinFrequency":
        kwargs = {"sdf_version": target_version}
        kwargs["min_frequency"] = self.min_frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_frequency")
        if self.min_frequency is not None:
            el.text = str(self.min_frequency)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2412
        _min_frequency = _parse_double(_text)
        if isinstance(_min_frequency, SDFError):
            return _min_frequency
        return cls(sdf_version=version, min_frequency=_min_frequency)


class MaxFrequency(BaseModel):
    def __init__(self, sdf_version: str, max_frequency: float = 2484):
        self.__version__ = sdf_version
        self.max_frequency = max_frequency

    def to_version(self, target_version: str) -> "MaxFrequency":
        kwargs = {"sdf_version": target_version}
        kwargs["max_frequency"] = self.max_frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_frequency")
        if self.max_frequency is not None:
            el.text = str(self.max_frequency)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2484
        _max_frequency = _parse_double(_text)
        if isinstance(_max_frequency, SDFError):
            return _max_frequency
        return cls(sdf_version=version, max_frequency=_max_frequency)


class Gain(BaseModel):
    def __init__(self, sdf_version: str, gain: float = 2.5):
        self.__version__ = sdf_version
        self.gain = gain

    def to_version(self, target_version: str) -> "Gain":
        kwargs = {"sdf_version": target_version}
        kwargs["gain"] = self.gain
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gain")
        if self.gain is not None:
            el.text = str(self.gain)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2.5
        _gain = _parse_double(_text)
        if isinstance(_gain, SDFError):
            return _gain
        return cls(sdf_version=version, gain=_gain)


class Power(BaseModel):
    def __init__(self, sdf_version: str, power: float = 14.50):
        self.__version__ = sdf_version
        self.power = power

    def to_version(self, target_version: str) -> "Power":
        kwargs = {"sdf_version": target_version}
        kwargs["power"] = self.power
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("power")
        if self.power is not None:
            el.text = str(self.power)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 14.50
        _power = _parse_double(_text)
        if isinstance(_power, SDFError):
            return _power
        return cls(sdf_version=version, power=_power)


class Sensitivity(BaseModel):
    def __init__(self, sdf_version: str, sensitivity: float = -90):
        self.__version__ = sdf_version
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Sensitivity":
        kwargs = {"sdf_version": target_version}
        kwargs["sensitivity"] = self.sensitivity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sensitivity")
        if self.sensitivity is not None:
            el.text = str(self.sensitivity)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -90
        _sensitivity = _parse_double(_text)
        if isinstance(_sensitivity, SDFError):
            return _sensitivity
        return cls(sdf_version=version, sensitivity=_sensitivity)


class Transceiver(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        essid: "Essid" = None,
        frequency: "Frequency" = None,
        min_frequency: "MinFrequency" = None,
        max_frequency: "MaxFrequency" = None,
        gain: "Gain" = None,
        power: "Power" = None,
        sensitivity: "Sensitivity" = None
    ):
        self.__version__ = sdf_version
        self.essid = essid
        self.frequency = frequency
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.gain = gain
        self.power = power
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Transceiver":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid.to_version(target_version) if self.essid is not None else None
        kwargs["frequency"] = self.frequency.to_version(target_version) if self.frequency is not None else None
        kwargs["min_frequency"] = self.min_frequency.to_version(target_version) if self.min_frequency is not None else None
        kwargs["max_frequency"] = self.max_frequency.to_version(target_version) if self.max_frequency is not None else None
        kwargs["gain"] = self.gain.to_version(target_version) if self.gain is not None else None
        kwargs["power"] = self.power.to_version(target_version) if self.power is not None else None
        kwargs["sensitivity"] = self.sensitivity.to_version(target_version) if self.sensitivity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("transceiver")
        if self.essid is not None:
            el.append(self.essid.to_sdf(version))
        if self.frequency is not None:
            el.append(self.frequency.to_sdf(version))
        if self.min_frequency is not None:
            el.append(self.min_frequency.to_sdf(version))
        if self.max_frequency is not None:
            el.append(self.max_frequency.to_sdf(version))
        if self.gain is not None:
            el.append(self.gain.to_sdf(version))
        if self.power is not None:
            el.append(self.power.to_sdf(version))
        if self.sensitivity is not None:
            el.append(self.sensitivity.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_essid = el.find("essid")
        if _c_essid is not None:
            _res = Essid._from_sdf(_c_essid, version)
            if isinstance(_res, SDFError):
                return _res.extend("essid")
            _essid = _res
        else:
            _essid = None
        _c_frequency = el.find("frequency")
        if _c_frequency is not None:
            _res = Frequency._from_sdf(_c_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("frequency")
            _frequency = _res
        else:
            _frequency = None
        _c_min_frequency = el.find("min_frequency")
        if _c_min_frequency is not None:
            _res = MinFrequency._from_sdf(_c_min_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_frequency")
            _min_frequency = _res
        else:
            _min_frequency = None
        _c_max_frequency = el.find("max_frequency")
        if _c_max_frequency is not None:
            _res = MaxFrequency._from_sdf(_c_max_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_frequency")
            _max_frequency = _res
        else:
            _max_frequency = None
        _c_gain = el.find("gain")
        if _c_gain is not None:
            _res = Gain._from_sdf(_c_gain, version)
            if isinstance(_res, SDFError):
                return _res.extend("gain")
            _gain = _res
        else:
            _gain = None
        _c_power = el.find("power")
        if _c_power is not None:
            _res = Power._from_sdf(_c_power, version)
            if isinstance(_res, SDFError):
                return _res.extend("power")
            _power = _res
        else:
            _power = None
        _c_sensitivity = el.find("sensitivity")
        if _c_sensitivity is not None:
            _res = Sensitivity._from_sdf(_c_sensitivity, version)
            if isinstance(_res, SDFError):
                return _res.extend("sensitivity")
            _sensitivity = _res
        else:
            _sensitivity = None
        return cls(sdf_version=version, essid=_essid, frequency=_frequency, min_frequency=_min_frequency, max_frequency=_max_frequency, gain=_gain, power=_power, sensitivity=_sensitivity)


class ForceTorqueFrame(BaseModel):
    def __init__(self, sdf_version: str, frame: str = "parent"):
        self.__version__ = sdf_version
        self.frame = frame

    def to_version(self, target_version: str) -> "ForceTorqueFrame":
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.frame is not None:
            el.text = self.frame
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "parent"
        _frame = _text
        if isinstance(_frame, SDFError):
            return _frame
        return cls(sdf_version=version, frame=_frame)


class MeasureDirection(BaseModel):
    def __init__(self, sdf_version: str, measure_direction: str = "child_to_parent"):
        self.__version__ = sdf_version
        self.measure_direction = measure_direction

    def to_version(self, target_version: str) -> "MeasureDirection":
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["measure_direction"] = self.measure_direction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("measure_direction")
        if self.measure_direction is not None:
            el.text = self.measure_direction
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "child_to_parent"
        _measure_direction = _text
        if isinstance(_measure_direction, SDFError):
            return _measure_direction
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            if _measure_direction != "child_to_parent":
                return SDFError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, measure_direction=_measure_direction)


class Torque(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Torque":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("torque")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class Force(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Force":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("force")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class ForceTorque(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        frame: "ForceTorqueFrame" = None,
        measure_direction: "MeasureDirection" = None,
        torque: "Torque" = None,
        force: "Force" = None
    ):
        self.__version__ = sdf_version
        self.frame = frame
        self.measure_direction = measure_direction
        self.torque = torque
        self.force = force

    def to_version(self, target_version: str) -> "ForceTorque":
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        if self.torque is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {target_version} (added in 1.7)")
        if self.force is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame.to_version(target_version) if self.frame is not None else None
        kwargs["measure_direction"] = self.measure_direction.to_version(target_version) if self.measure_direction is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("force_torque")
        if self.frame is not None:
            el.append(self.frame.to_sdf(version))
        if self.measure_direction is not None:
            el.append(self.measure_direction.to_sdf(version))
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_frame = el.find("frame")
        if _c_frame is not None:
            _res = ForceTorqueFrame._from_sdf(_c_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame = _res
        else:
            _frame = None
        _c_measure_direction = el.find("measure_direction")
        if _c_measure_direction is not None:
            _res = MeasureDirection._from_sdf(_c_measure_direction, version)
            if isinstance(_res, SDFError):
                return _res.extend("measure_direction")
            _measure_direction = _res
        else:
            _measure_direction = None
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        _c_torque = el.find("torque")
        if _c_torque is not None:
            _res = Torque._from_sdf(_c_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("torque")
            _torque = _res
        else:
            _torque = None
        if _torque is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'torque' is not supported in SDF version {version} (added in 1.7)")
        _c_force = el.find("force")
        if _c_force is not None:
            _res = Force._from_sdf(_c_force, version)
            if isinstance(_res, SDFError):
                return _res.extend("force")
            _force = _res
        else:
            _force = None
        if _force is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'force' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, frame=_frame, measure_direction=_measure_direction, torque=_torque, force=_force)


class VerticalPositionNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "VerticalPositionNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class VerticalPosition(BaseModel):
    def __init__(self, sdf_version: str, noise: "VerticalPositionNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VerticalPosition":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical_position")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = VerticalPositionNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class VerticalVelocityNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "VerticalVelocityNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class VerticalVelocity(BaseModel):
    def __init__(self, sdf_version: str, noise: "VerticalVelocityNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VerticalVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical_velocity")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = VerticalVelocityNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class Altimeter(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        vertical_position: "VerticalPosition" = None,
        vertical_velocity: "VerticalVelocity" = None
    ):
        self.__version__ = sdf_version
        self.vertical_position = vertical_position
        self.vertical_velocity = vertical_velocity

    def to_version(self, target_version: str) -> "Altimeter":
        kwargs = {"sdf_version": target_version}
        kwargs["vertical_position"] = self.vertical_position.to_version(target_version) if self.vertical_position is not None else None
        kwargs["vertical_velocity"] = self.vertical_velocity.to_version(target_version) if self.vertical_velocity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("altimeter")
        if self.vertical_position is not None:
            el.append(self.vertical_position.to_sdf(version))
        if self.vertical_velocity is not None:
            el.append(self.vertical_velocity.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_vertical_position = el.find("vertical_position")
        if _c_vertical_position is not None:
            _res = VerticalPosition._from_sdf(_c_vertical_position, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical_position")
            _vertical_position = _res
        else:
            _vertical_position = None
        _c_vertical_velocity = el.find("vertical_velocity")
        if _c_vertical_velocity is not None:
            _res = VerticalVelocity._from_sdf(_c_vertical_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical_velocity")
            _vertical_velocity = _res
        else:
            _vertical_velocity = None
        return cls(sdf_version=version, vertical_position=_vertical_position, vertical_velocity=_vertical_velocity)


class Magnetometer(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Magnetometer":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("magnetometer")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class LogicalCameraNear(BaseModel):
    def __init__(self, sdf_version: str, near: float = 0):
        self.__version__ = sdf_version
        self.near = near

    def to_version(self, target_version: str) -> "LogicalCameraNear":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("near")
        if self.near is not None:
            el.text = str(self.near)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _near = _parse_double(_text)
        if isinstance(_near, SDFError):
            return _near
        return cls(sdf_version=version, near=_near)


class LogicalCameraFar(BaseModel):
    def __init__(self, sdf_version: str, far: float = 1):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "LogicalCameraFar":
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("far")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        if self.aspect_ratio is not None:
            el.text = str(self.aspect_ratio)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _aspect_ratio = _parse_double(_text)
        if isinstance(_aspect_ratio, SDFError):
            return _aspect_ratio
        return cls(sdf_version=version, aspect_ratio=_aspect_ratio)


class LogicalCameraHorizontalFov(BaseModel):
    def __init__(self, sdf_version: str, horizontal_fov: float = 1):
        self.__version__ = sdf_version
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "LogicalCameraHorizontalFov":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal_fov"] = self.horizontal_fov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal_fov")
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _horizontal_fov = _parse_double(_text)
        if isinstance(_horizontal_fov, SDFError):
            return _horizontal_fov
        return cls(sdf_version=version, horizontal_fov=_horizontal_fov)


class LogicalCamera(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        near: "LogicalCameraNear" = None,
        far: "LogicalCameraFar" = None,
        aspect_ratio: "AspectRatio" = None,
        horizontal_fov: "LogicalCameraHorizontalFov" = None
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
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        if self.far is not None:
            el.append(self.far.to_sdf(version))
        if self.aspect_ratio is not None:
            el.append(self.aspect_ratio.to_sdf(version))
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_near = el.find("near")
        if _c_near is not None:
            _res = LogicalCameraNear._from_sdf(_c_near, version)
            if isinstance(_res, SDFError):
                return _res.extend("near")
            _near = _res
        else:
            _near = None
        _c_far = el.find("far")
        if _c_far is not None:
            _res = LogicalCameraFar._from_sdf(_c_far, version)
            if isinstance(_res, SDFError):
                return _res.extend("far")
            _far = _res
        else:
            _far = None
        _c_aspect_ratio = el.find("aspect_ratio")
        if _c_aspect_ratio is not None:
            _res = AspectRatio._from_sdf(_c_aspect_ratio, version)
            if isinstance(_res, SDFError):
                return _res.extend("aspect_ratio")
            _aspect_ratio = _res
        else:
            _aspect_ratio = None
        _c_horizontal_fov = el.find("horizontal_fov")
        if _c_horizontal_fov is not None:
            _res = LogicalCameraHorizontalFov._from_sdf(_c_horizontal_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal_fov")
            _horizontal_fov = _res
        else:
            _horizontal_fov = None
        return cls(sdf_version=version, near=_near, far=_far, aspect_ratio=_aspect_ratio, horizontal_fov=_horizontal_fov)


class ReferenceAltitude(BaseModel):
    def __init__(self, sdf_version: str, reference_altitude: float = 0.0):
        self.__version__ = sdf_version
        self.reference_altitude = reference_altitude

    def to_version(self, target_version: str) -> "ReferenceAltitude":
        kwargs = {"sdf_version": target_version}
        kwargs["reference_altitude"] = self.reference_altitude
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("reference_altitude")
        if self.reference_altitude is not None:
            el.text = str(self.reference_altitude)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _reference_altitude = _parse_double(_text)
        if isinstance(_reference_altitude, SDFError):
            return _reference_altitude
        return cls(sdf_version=version, reference_altitude=_reference_altitude)


class PressureNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        precision: "Precision" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.dynamic_bias_stddev = dynamic_bias_stddev
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.precision = precision

    def to_version(self, target_version: str) -> "PressureNoise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, dynamic_bias_stddev=_dynamic_bias_stddev, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, precision=_precision)


class Pressure(BaseModel):
    def __init__(self, sdf_version: str, noise: "PressureNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Pressure":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pressure")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = PressureNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class AirPressure(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        reference_altitude: "ReferenceAltitude" = None,
        pressure: "Pressure" = None
    ):
        self.__version__ = sdf_version
        self.reference_altitude = reference_altitude
        self.pressure = pressure

    def to_version(self, target_version: str) -> "AirPressure":
        kwargs = {"sdf_version": target_version}
        kwargs["reference_altitude"] = self.reference_altitude.to_version(target_version) if self.reference_altitude is not None else None
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("air_pressure")
        if self.reference_altitude is not None:
            el.append(self.reference_altitude.to_sdf(version))
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_reference_altitude = el.find("reference_altitude")
        if _c_reference_altitude is not None:
            _res = ReferenceAltitude._from_sdf(_c_reference_altitude, version)
            if isinstance(_res, SDFError):
                return _res.extend("reference_altitude")
            _reference_altitude = _res
        else:
            _reference_altitude = None
        _c_pressure = el.find("pressure")
        if _c_pressure is not None:
            _res = Pressure._from_sdf(_c_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("pressure")
            _pressure = _res
        else:
            _pressure = None
        return cls(sdf_version=version, reference_altitude=_reference_altitude, pressure=_pressure)


class ScanHorizontal(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        samples: "Samples" = None,
        resolution: "Resolution" = None,
        min_angle: "MinAngle" = None,
        max_angle: "MaxAngle" = None
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "ScanHorizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples.to_version(target_version) if self.samples is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        kwargs["min_angle"] = self.min_angle.to_version(target_version) if self.min_angle is not None else None
        kwargs["max_angle"] = self.max_angle.to_version(target_version) if self.max_angle is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.samples is not None:
            el.append(self.samples.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        if self.min_angle is not None:
            el.append(self.min_angle.to_sdf(version))
        if self.max_angle is not None:
            el.append(self.max_angle.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_samples = el.find("samples")
        if _c_samples is not None:
            _res = Samples._from_sdf(_c_samples, version)
            if isinstance(_res, SDFError):
                return _res.extend("samples")
            _samples = _res
        else:
            _samples = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = Resolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        _c_min_angle = el.find("min_angle")
        if _c_min_angle is not None:
            _res = MinAngle._from_sdf(_c_min_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_angle")
            _min_angle = _res
        else:
            _min_angle = None
        _c_max_angle = el.find("max_angle")
        if _c_max_angle is not None:
            _res = MaxAngle._from_sdf(_c_max_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_angle")
            _max_angle = _res
        else:
            _max_angle = None
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class ScanVertical(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        samples: "VerticalSamples" = None,
        resolution: "Resolution" = None,
        min_angle: "MinAngle" = None,
        max_angle: "MaxAngle" = None
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "ScanVertical":
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples.to_version(target_version) if self.samples is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        kwargs["min_angle"] = self.min_angle.to_version(target_version) if self.min_angle is not None else None
        kwargs["max_angle"] = self.max_angle.to_version(target_version) if self.max_angle is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.samples is not None:
            el.append(self.samples.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        if self.min_angle is not None:
            el.append(self.min_angle.to_sdf(version))
        if self.max_angle is not None:
            el.append(self.max_angle.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_samples = el.find("samples")
        if _c_samples is not None:
            _res = VerticalSamples._from_sdf(_c_samples, version)
            if isinstance(_res, SDFError):
                return _res.extend("samples")
            _samples = _res
        else:
            _samples = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = Resolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        _c_min_angle = el.find("min_angle")
        if _c_min_angle is not None:
            _res = MinAngle._from_sdf(_c_min_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_angle")
            _min_angle = _res
        else:
            _min_angle = None
        _c_max_angle = el.find("max_angle")
        if _c_max_angle is not None:
            _res = MaxAngle._from_sdf(_c_max_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_angle")
            _max_angle = _res
        else:
            _max_angle = None
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class LidarScan(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "ScanHorizontal" = None,
        vertical: "ScanVertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "LidarScan":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scan")
        if self.horizontal is None:
            self.horizontal = ScanHorizontal(sdf_version=version)
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_horizontal = el.find("horizontal")
        if _c_horizontal is not None:
            _res = ScanHorizontal._from_sdf(_c_horizontal, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        else:
            _res = ScanHorizontal._from_sdf(ET.Element("horizontal"), version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        _c_vertical = el.find("vertical")
        if _c_vertical is not None:
            _res = ScanVertical._from_sdf(_c_vertical, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical")
            _vertical = _res
        else:
            _vertical = None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class LidarRange(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        min: "Min" = None,
        max: "Max" = None,
        resolution: "RangeResolution" = None
    ):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_version(self, target_version: str) -> "LidarRange":
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min.to_version(target_version) if self.min is not None else None
        kwargs["max"] = self.max.to_version(target_version) if self.max is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.min is not None:
            el.append(self.min.to_sdf(version))
        if self.max is not None:
            el.append(self.max.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_min = el.find("min")
        if _c_min is not None:
            _res = Min._from_sdf(_c_min, version)
            if isinstance(_res, SDFError):
                return _res.extend("min")
            _min = _res
        else:
            _min = None
        _c_max = el.find("max")
        if _c_max is not None:
            _res = Max._from_sdf(_c_max, version)
            if isinstance(_res, SDFError):
                return _res.extend("max")
            _max = _res
        else:
            _max = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = RangeResolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        return cls(sdf_version=version, min=_min, max=_max, resolution=_resolution)


class Lidar(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        scan: "LidarScan" = None,
        range: "LidarRange" = None,
        noise: "Noise" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.scan = scan
        self.range = range
        self.noise = noise
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "Lidar":
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lidar")
        if self.scan is None:
            self.scan = LidarScan(sdf_version=version)
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is None:
            self.range = LidarRange(sdf_version=version)
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_scan = el.find("scan")
        if _c_scan is not None:
            _res = LidarScan._from_sdf(_c_scan, version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        else:
            _res = LidarScan._from_sdf(ET.Element("scan"), version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        _c_range = el.find("range")
        if _c_range is not None:
            _res = LidarRange._from_sdf(_c_range, version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        else:
            _res = LidarRange._from_sdf(ET.Element("range"), version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        _c_visibility_mask = el.find("visibility_mask")
        if _c_visibility_mask is not None:
            _res = VisibilityMask._from_sdf(_c_visibility_mask, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_mask")
            _visibility_mask = _res
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)


class Navsat(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        position_sensing: "PositionSensing" = None,
        velocity_sensing: "VelocitySensing" = None
    ):
        self.__version__ = sdf_version
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_version(self, target_version: str) -> "Navsat":
        kwargs = {"sdf_version": target_version}
        kwargs["position_sensing"] = self.position_sensing.to_version(target_version) if self.position_sensing is not None else None
        kwargs["velocity_sensing"] = self.velocity_sensing.to_version(target_version) if self.velocity_sensing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("navsat")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf(version))
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_position_sensing = el.find("position_sensing")
        if _c_position_sensing is not None:
            _res = PositionSensing._from_sdf(_c_position_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("position_sensing")
            _position_sensing = _res
        else:
            _position_sensing = None
        _c_velocity_sensing = el.find("velocity_sensing")
        if _c_velocity_sensing is not None:
            _res = VelocitySensing._from_sdf(_c_velocity_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity_sensing")
            _velocity_sensing = _res
        else:
            _velocity_sensing = None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class EnableMetrics(BaseModel):
    def __init__(self, sdf_version: str, enable_metrics: bool = False):
        self.__version__ = sdf_version
        self.enable_metrics = enable_metrics

    def to_version(self, target_version: str) -> "EnableMetrics":
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_metrics"] = self.enable_metrics
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_metrics")
        if self.enable_metrics is not None:
            el.text = str(self.enable_metrics).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _enable_metrics = str(_text).strip().lower() == 'true'
        if isinstance(_enable_metrics, SDFError):
            return _enable_metrics
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            if _enable_metrics != False:
                return SDFError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, enable_metrics=_enable_metrics)


class AirSpeed(BaseModel):
    def __init__(self, sdf_version: str, pressure: "Pressure" = None):
        self.__version__ = sdf_version
        self.pressure = pressure

    def to_version(self, target_version: str) -> "AirSpeed":
        kwargs = {"sdf_version": target_version}
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("air_speed")
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_pressure = el.find("pressure")
        if _c_pressure is not None:
            _res = Pressure._from_sdf(_c_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("pressure")
            _pressure = _res
        else:
            _pressure = None
        return cls(sdf_version=version, pressure=_pressure)


class FrameId(BaseModel):
    def __init__(self, sdf_version: str, frame_id: str = ""):
        self.__version__ = sdf_version
        self.frame_id = frame_id

    def to_version(self, target_version: str) -> "FrameId":
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame_id"] = self.frame_id
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame_id")
        if self.frame_id is not None:
            el.text = self.frame_id
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _frame_id = _text
        if isinstance(_frame_id, SDFError):
            return _frame_id
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            if _frame_id != "":
                return SDFError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, frame_id=_frame_id)


class Sensor(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "__default__",
        always_on: bool = False,
        update_rate: float = 0,
        visualize: bool = False,
        plugin: List["Plugin"] = None,
        camera: "Camera" = None,
        ray: "Ray" = None,
        contact: "Contact" = None,
        rfidtag: "Rfidtag" = None,
        rfid: "Rfid" = None,
        origin: "Origin" = None,
        topic: "SensorTopic" = None,
        pose: "Pose" = None,
        imu: "Imu" = None,
        gps: "Gps" = None,
        sonar: "Sonar" = None,
        transceiver: "Transceiver" = None,
        force_torque: "ForceTorque" = None,
        frame: List["Frame"] = None,
        altimeter: "Altimeter" = None,
        magnetometer: "Magnetometer" = None,
        logical_camera: "LogicalCamera" = None,
        air_pressure: "AirPressure" = None,
        lidar: "Lidar" = None,
        navsat: "Navsat" = None,
        enable_metrics: "EnableMetrics" = None,
        air_speed: "AirSpeed" = None,
        frame_id: "FrameId" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.always_on = always_on
        self.update_rate = update_rate
        self.visualize = visualize
        self.plugin = plugin or []
        self.camera = camera
        self.ray = ray
        self.contact = contact
        self.rfidtag = rfidtag
        self.rfid = rfid
        self.origin = origin
        self.topic = topic
        self.pose = pose
        self.imu = imu
        self.gps = gps
        self.sonar = sonar
        self.transceiver = transceiver
        self.force_torque = force_torque
        self.frame = frame or []
        self.altimeter = altimeter
        self.magnetometer = magnetometer
        self.logical_camera = logical_camera
        self.air_pressure = air_pressure
        self.lidar = lidar
        self.navsat = navsat
        self.enable_metrics = enable_metrics
        self.air_speed = air_speed
        self.frame_id = frame_id

    def to_version(self, target_version: str) -> "Sensor":
        if self.always_on is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'always_on' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.update_rate is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'update_rate' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.visualize is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.imu is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'imu' is not supported in SDF version {target_version} (added in 1.3)")
        if self.gps is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gps' is not supported in SDF version {target_version} (added in 1.4)")
        if self.sonar is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'sonar' is not supported in SDF version {target_version} (added in 1.4)")
        if self.transceiver is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'transceiver' is not supported in SDF version {target_version} (added in 1.4)")
        if self.force_torque is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'force_torque' is not supported in SDF version {target_version} (added in 1.4)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.altimeter is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'altimeter' is not supported in SDF version {target_version} (added in 1.5)")
        if self.magnetometer is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'magnetometer' is not supported in SDF version {target_version} (added in 1.5)")
        if self.logical_camera is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'logical_camera' is not supported in SDF version {target_version} (added in 1.5)")
        if self.air_pressure is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'air_pressure' is not supported in SDF version {target_version} (added in 1.6)")
        if self.lidar is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'lidar' is not supported in SDF version {target_version} (added in 1.6)")
        if self.navsat is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'navsat' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        if self.air_speed is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'air_speed' is not supported in SDF version {target_version} (added in 1.10)")
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["always_on"] = self.always_on
        kwargs["update_rate"] = self.update_rate
        kwargs["visualize"] = self.visualize
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        kwargs["ray"] = self.ray.to_version(target_version) if self.ray is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["rfidtag"] = self.rfidtag.to_version(target_version) if self.rfidtag is not None else None
        kwargs["rfid"] = self.rfid.to_version(target_version) if self.rfid is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["imu"] = self.imu.to_version(target_version) if self.imu is not None else None
        kwargs["gps"] = self.gps.to_version(target_version) if self.gps is not None else None
        kwargs["sonar"] = self.sonar.to_version(target_version) if self.sonar is not None else None
        kwargs["transceiver"] = self.transceiver.to_version(target_version) if self.transceiver is not None else None
        kwargs["force_torque"] = self.force_torque.to_version(target_version) if self.force_torque is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["altimeter"] = self.altimeter.to_version(target_version) if self.altimeter is not None else None
        kwargs["magnetometer"] = self.magnetometer.to_version(target_version) if self.magnetometer is not None else None
        kwargs["logical_camera"] = self.logical_camera.to_version(target_version) if self.logical_camera is not None else None
        kwargs["air_pressure"] = self.air_pressure.to_version(target_version) if self.air_pressure is not None else None
        kwargs["lidar"] = self.lidar.to_version(target_version) if self.lidar is not None else None
        kwargs["navsat"] = self.navsat.to_version(target_version) if self.navsat is not None else None
        kwargs["enable_metrics"] = self.enable_metrics.to_version(target_version) if self.enable_metrics is not None else None
        kwargs["air_speed"] = self.air_speed.to_version(target_version) if self.air_speed is not None else None
        kwargs["frame_id"] = self.frame_id.to_version(target_version) if self.frame_id is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sensor")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.always_on is not None:
            el.set("always_on", str(self.always_on).lower())
        if self.update_rate is not None:
            el.set("update_rate", str(self.update_rate))
        if self.visualize is not None:
            el.set("visualize", str(self.visualize).lower())
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.camera is not None:
            el.append(self.camera.to_sdf(version))
        if self.ray is not None:
            el.append(self.ray.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        if self.rfidtag is not None:
            el.append(self.rfidtag.to_sdf(version))
        if self.rfid is not None:
            el.append(self.rfid.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.imu is not None:
            el.append(self.imu.to_sdf(version))
        if self.gps is not None:
            el.append(self.gps.to_sdf(version))
        if self.sonar is not None:
            el.append(self.sonar.to_sdf(version))
        if self.transceiver is not None:
            el.append(self.transceiver.to_sdf(version))
        if self.force_torque is not None:
            el.append(self.force_torque.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.altimeter is not None:
            el.append(self.altimeter.to_sdf(version))
        if self.magnetometer is not None:
            el.append(self.magnetometer.to_sdf(version))
        if self.logical_camera is not None:
            el.append(self.logical_camera.to_sdf(version))
        if self.air_pressure is not None:
            el.append(self.air_pressure.to_sdf(version))
        if self.lidar is not None:
            el.append(self.lidar.to_sdf(version))
        if self.navsat is not None:
            el.append(self.navsat.to_sdf(version))
        if self.enable_metrics is not None:
            el.append(self.enable_metrics.to_sdf(version))
        if self.air_speed is not None:
            el.append(self.air_speed.to_sdf(version))
        if self.frame_id is not None:
            el.append(self.frame_id.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _type = el.get("type", "__default__")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _always_on = str(el.get("always_on", False)).strip().lower() == 'true'
        if isinstance(_always_on, SDFError):
            return _always_on.extend("@always_on")
        _update_rate = _parse_double(el.get("update_rate", 0))
        if isinstance(_update_rate, SDFError):
            return _update_rate.extend("@update_rate")
        _visualize = str(el.get("visualize", False)).strip().lower() == 'true'
        if isinstance(_visualize, SDFError):
            return _visualize.extend("@visualize")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _c_camera = el.find("camera")
        if _c_camera is not None:
            _res = Camera._from_sdf(_c_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera")
            _camera = _res
        else:
            _camera = None
        _c_ray = el.find("ray")
        if _c_ray is not None:
            _res = Ray._from_sdf(_c_ray, version)
            if isinstance(_res, SDFError):
                return _res.extend("ray")
            _ray = _res
        else:
            _ray = None
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = Contact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _c_rfidtag = el.find("rfidtag")
        if _c_rfidtag is not None:
            _res = Rfidtag._from_sdf(_c_rfidtag, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfidtag")
            _rfidtag = _res
        else:
            _rfidtag = None
        _c_rfid = el.find("rfid")
        if _c_rfid is not None:
            _res = Rfid._from_sdf(_c_rfid, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfid")
            _rfid = _res
        else:
            _rfid = None
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = SensorTopic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _c_imu = el.find("imu")
        if _c_imu is not None:
            _res = Imu._from_sdf(_c_imu, version)
            if isinstance(_res, SDFError):
                return _res.extend("imu")
            _imu = _res
        else:
            _imu = None
        if _imu is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'imu' is not supported in SDF version {version} (added in 1.3)")
        _c_gps = el.find("gps")
        if _c_gps is not None:
            _res = Gps._from_sdf(_c_gps, version)
            if isinstance(_res, SDFError):
                return _res.extend("gps")
            _gps = _res
        else:
            _gps = None
        if _gps is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'gps' is not supported in SDF version {version} (added in 1.4)")
        _c_sonar = el.find("sonar")
        if _c_sonar is not None:
            _res = Sonar._from_sdf(_c_sonar, version)
            if isinstance(_res, SDFError):
                return _res.extend("sonar")
            _sonar = _res
        else:
            _sonar = None
        if _sonar is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'sonar' is not supported in SDF version {version} (added in 1.4)")
        _c_transceiver = el.find("transceiver")
        if _c_transceiver is not None:
            _res = Transceiver._from_sdf(_c_transceiver, version)
            if isinstance(_res, SDFError):
                return _res.extend("transceiver")
            _transceiver = _res
        else:
            _transceiver = None
        if _transceiver is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'transceiver' is not supported in SDF version {version} (added in 1.4)")
        _c_force_torque = el.find("force_torque")
        if _c_force_torque is not None:
            _res = ForceTorque._from_sdf(_c_force_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("force_torque")
            _force_torque = _res
        else:
            _force_torque = None
        if _force_torque is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'force_torque' is not supported in SDF version {version} (added in 1.4)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_altimeter = el.find("altimeter")
        if _c_altimeter is not None:
            _res = Altimeter._from_sdf(_c_altimeter, version)
            if isinstance(_res, SDFError):
                return _res.extend("altimeter")
            _altimeter = _res
        else:
            _altimeter = None
        if _altimeter is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'altimeter' is not supported in SDF version {version} (added in 1.5)")
        _c_magnetometer = el.find("magnetometer")
        if _c_magnetometer is not None:
            _res = Magnetometer._from_sdf(_c_magnetometer, version)
            if isinstance(_res, SDFError):
                return _res.extend("magnetometer")
            _magnetometer = _res
        else:
            _magnetometer = None
        if _magnetometer is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'magnetometer' is not supported in SDF version {version} (added in 1.5)")
        _c_logical_camera = el.find("logical_camera")
        if _c_logical_camera is not None:
            _res = LogicalCamera._from_sdf(_c_logical_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("logical_camera")
            _logical_camera = _res
        else:
            _logical_camera = None
        if _logical_camera is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'logical_camera' is not supported in SDF version {version} (added in 1.5)")
        _c_air_pressure = el.find("air_pressure")
        if _c_air_pressure is not None:
            _res = AirPressure._from_sdf(_c_air_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("air_pressure")
            _air_pressure = _res
        else:
            _air_pressure = None
        if _air_pressure is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'air_pressure' is not supported in SDF version {version} (added in 1.6)")
        _c_lidar = el.find("lidar")
        if _c_lidar is not None:
            _res = Lidar._from_sdf(_c_lidar, version)
            if isinstance(_res, SDFError):
                return _res.extend("lidar")
            _lidar = _res
        else:
            _lidar = None
        if _lidar is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'lidar' is not supported in SDF version {version} (added in 1.6)")
        _c_navsat = el.find("navsat")
        if _c_navsat is not None:
            _res = Navsat._from_sdf(_c_navsat, version)
            if isinstance(_res, SDFError):
                return _res.extend("navsat")
            _navsat = _res
        else:
            _navsat = None
        if _navsat is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'navsat' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_metrics = el.find("enable_metrics")
        if _c_enable_metrics is not None:
            _res = EnableMetrics._from_sdf(_c_enable_metrics, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_metrics")
            _enable_metrics = _res
        else:
            _enable_metrics = None
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        _c_air_speed = el.find("air_speed")
        if _c_air_speed is not None:
            _res = AirSpeed._from_sdf(_c_air_speed, version)
            if isinstance(_res, SDFError):
                return _res.extend("air_speed")
            _air_speed = _res
        else:
            _air_speed = None
        if _air_speed is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'air_speed' is not supported in SDF version {version} (added in 1.10)")
        _c_frame_id = el.find("frame_id")
        if _c_frame_id is not None:
            _res = FrameId._from_sdf(_c_frame_id, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame_id")
            _frame_id = _res
        else:
            _frame_id = None
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, name=_name, type=_type, always_on=_always_on, update_rate=_update_rate, visualize=_visualize, plugin=_plugin, camera=_camera, ray=_ray, contact=_contact, rfidtag=_rfidtag, rfid=_rfid, origin=_origin, topic=_topic, pose=_pose, imu=_imu, gps=_gps, sonar=_sonar, transceiver=_transceiver, force_torque=_force_torque, frame=_frame, altimeter=_altimeter, magnetometer=_magnetometer, logical_camera=_logical_camera, air_pressure=_air_pressure, lidar=_lidar, navsat=_navsat, enable_metrics=_enable_metrics, air_speed=_air_speed, frame_id=_frame_id)
