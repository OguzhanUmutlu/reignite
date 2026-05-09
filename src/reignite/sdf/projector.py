### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
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


class Texture(BaseModel):
    def __init__(self, sdf_version: str, texture: str = "__default__"):
        self.__version__ = sdf_version
        self.texture = texture

    def to_version(self, target_version: str) -> "Texture":
        kwargs = {"sdf_version": target_version}
        kwargs["texture"] = self.texture
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("texture")
        if self.texture is not None:
            el.text = self.texture
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _texture = _text
        if isinstance(_texture, SDFError):
            return _texture
        return cls(sdf_version=version, texture=_texture)


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


class Fov(BaseModel):
    def __init__(self, sdf_version: str, fov: float = 0.785):
        self.__version__ = sdf_version
        self.fov = fov

    def to_version(self, target_version: str) -> "Fov":
        kwargs = {"sdf_version": target_version}
        kwargs["fov"] = self.fov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fov")
        if self.fov is not None:
            el.text = str(self.fov)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.785
        _fov = _parse_double(_text)
        if isinstance(_fov, SDFError):
            return _fov
        return cls(sdf_version=version, fov=_fov)


class NearClip(BaseModel):
    def __init__(self, sdf_version: str, near_clip: float = 0.1):
        self.__version__ = sdf_version
        self.near_clip = near_clip

    def to_version(self, target_version: str) -> "NearClip":
        kwargs = {"sdf_version": target_version}
        kwargs["near_clip"] = self.near_clip
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("near_clip")
        if self.near_clip is not None:
            el.text = str(self.near_clip)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.1
        _near_clip = _parse_double(_text)
        if isinstance(_near_clip, SDFError):
            return _near_clip
        return cls(sdf_version=version, near_clip=_near_clip)


class FarClip(BaseModel):
    def __init__(self, sdf_version: str, far_clip: float = 10.0):
        self.__version__ = sdf_version
        self.far_clip = far_clip

    def to_version(self, target_version: str) -> "FarClip":
        kwargs = {"sdf_version": target_version}
        kwargs["far_clip"] = self.far_clip
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("far_clip")
        if self.far_clip is not None:
            el.text = str(self.far_clip)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10.0
        _far_clip = _parse_double(_text)
        if isinstance(_far_clip, SDFError):
            return _far_clip
        return cls(sdf_version=version, far_clip=_far_clip)


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


class VisibilityFlags(BaseModel):
    def __init__(self, sdf_version: str, visibility_flags: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "VisibilityFlags":
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_flags"] = self.visibility_flags
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visibility_flags")
        if self.visibility_flags is not None:
            el.text = str(self.visibility_flags)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4294967295
        _visibility_flags = _parse_uint32(_text)
        if isinstance(_visibility_flags, SDFError):
            return _visibility_flags
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            if _visibility_flags != 4294967295:
                return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_flags=_visibility_flags)


class Projector(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        plugin: List["Plugin"] = None,
        texture: "Texture" = None,
        pose: "Pose" = None,
        fov: "Fov" = None,
        near_clip: "NearClip" = None,
        far_clip: "FarClip" = None,
        frame: List["Frame"] = None,
        visibility_flags: "VisibilityFlags" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.plugin = plugin or []
        self.texture = texture
        self.pose = pose
        self.fov = fov
        self.near_clip = near_clip
        self.far_clip = far_clip
        self.frame = frame or []
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "Projector":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["texture"] = self.texture.to_version(target_version) if self.texture is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["fov"] = self.fov.to_version(target_version) if self.fov is not None else None
        kwargs["near_clip"] = self.near_clip.to_version(target_version) if self.near_clip is not None else None
        kwargs["far_clip"] = self.far_clip.to_version(target_version) if self.far_clip is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["visibility_flags"] = self.visibility_flags.to_version(target_version) if self.visibility_flags is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("projector")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.texture is not None:
            el.append(self.texture.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.fov is not None:
            el.append(self.fov.to_sdf(version))
        if self.near_clip is not None:
            el.append(self.near_clip.to_sdf(version))
        if self.far_clip is not None:
            el.append(self.far_clip.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.visibility_flags is not None:
            el.append(self.visibility_flags.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _c_texture = el.find("texture")
        if _c_texture is not None:
            _res = Texture._from_sdf(_c_texture, version)
            if isinstance(_res, SDFError):
                return _res.extend("texture")
            _texture = _res
        else:
            _texture = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_fov = el.find("fov")
        if _c_fov is not None:
            _res = Fov._from_sdf(_c_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("fov")
            _fov = _res
        else:
            _fov = None
        _c_near_clip = el.find("near_clip")
        if _c_near_clip is not None:
            _res = NearClip._from_sdf(_c_near_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("near_clip")
            _near_clip = _res
        else:
            _near_clip = None
        _c_far_clip = el.find("far_clip")
        if _c_far_clip is not None:
            _res = FarClip._from_sdf(_c_far_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("far_clip")
            _far_clip = _res
        else:
            _far_clip = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_visibility_flags = el.find("visibility_flags")
        if _c_visibility_flags is not None:
            _res = VisibilityFlags._from_sdf(_c_visibility_flags, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_flags")
            _visibility_flags = _res
        else:
            _visibility_flags = None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, name=_name, plugin=_plugin, texture=_texture, pose=_pose, fov=_fov, near_clip=_near_clip, far_clip=_far_clip, frame=_frame, visibility_flags=_visibility_flags)
