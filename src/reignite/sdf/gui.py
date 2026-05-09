### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
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



class Camera(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        frame: List["Frame"] = None,
        name: str = "user_camera",
        origin: "Origin" = None,
        pose: "Pose" = None,
        projection_type: "ProjectionType" = None,
        track_visual: "TrackVisual" = None,
        view_controller: "ViewController" = None
    ):
        self.__version__ = sdf_version
        self.frame = frame or []
        self.name = name
        self.origin = origin
        self.pose = pose
        self.projection_type = projection_type
        self.track_visual = track_visual
        self.view_controller = view_controller

    def to_version(self, target_version: str) -> "Camera":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.projection_type is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'projection_type' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["projection_type"] = self.projection_type.to_version(target_version) if self.projection_type is not None else None
        kwargs["track_visual"] = self.track_visual.to_version(target_version) if self.track_visual is not None else None
        kwargs["view_controller"] = self.view_controller.to_version(target_version) if self.view_controller is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera")
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.projection_type is not None:
            el.append(self.projection_type.to_sdf(version))
        if self.track_visual is not None:
            el.append(self.track_visual.to_sdf(version))
        if self.view_controller is not None:
            el.append(self.view_controller.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _name = el.get("name", "user_camera")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
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
        _c_projection_type = el.find("projection_type")
        if _c_projection_type is not None:
            _res = ProjectionType._from_sdf(_c_projection_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("projection_type")
            _projection_type = _res
        else:
            _projection_type = None
        if _projection_type is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'projection_type' is not supported in SDF version {version} (added in 1.5)")
        _c_track_visual = el.find("track_visual")
        if _c_track_visual is not None:
            _res = TrackVisual._from_sdf(_c_track_visual, version)
            if isinstance(_res, SDFError):
                return _res.extend("track_visual")
            _track_visual = _res
        else:
            _track_visual = None
        _c_view_controller = el.find("view_controller")
        if _c_view_controller is not None:
            _res = ViewController._from_sdf(_c_view_controller, version)
            if isinstance(_res, SDFError):
                return _res.extend("view_controller")
            _view_controller = _res
        else:
            _view_controller = None
        return cls(sdf_version=version, frame=_frame, name=_name, origin=_origin, pose=_pose, projection_type=_projection_type, track_visual=_track_visual, view_controller=_view_controller)


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


class FramePose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(self, sdf_version: str, frame: str = "", pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.frame = frame
        self.pose = pose

    def to_version(self, target_version: str) -> "FramePose":
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        return cls(sdf_version=version, frame=_frame, pose=_pose)


class Gui(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        camera: "Camera" = None,
        fullscreen: bool = False,
        plugin: List["Plugin"] = None
    ):
        self.__version__ = sdf_version
        self.camera = camera
        self.fullscreen = fullscreen
        self.plugin = plugin or []

    def to_version(self, target_version: str) -> "Gui":
        if self.plugin is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        kwargs["fullscreen"] = self.fullscreen
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gui")
        if self.camera is not None:
            el.append(self.camera.to_sdf(version))
        if self.fullscreen is not None:
            el.set("fullscreen", str(self.fullscreen).lower())
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_camera = el.find("camera")
        if _c_camera is not None:
            _res = Camera._from_sdf(_c_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera")
            _camera = _res
        else:
            _camera = None
        _fullscreen = str(el.get("fullscreen", False)).strip().lower() == 'true'
        if isinstance(_fullscreen, SDFError):
            return _fullscreen.extend("@fullscreen")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        if _plugin and cmp_version(version, "1.5") < 0:
            return SDFError(f"'plugin' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, camera=_camera, fullscreen=_fullscreen, plugin=_plugin)


class InheritYaw(BaseModel):
    def __init__(self, sdf_version: str, inherit_yaw: bool = False):
        self.__version__ = sdf_version
        self.inherit_yaw = inherit_yaw

    def to_version(self, target_version: str) -> "InheritYaw":
        if self.inherit_yaw is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'inherit_yaw' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["inherit_yaw"] = self.inherit_yaw
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inherit_yaw")
        if self.inherit_yaw is not None:
            el.text = str(self.inherit_yaw).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _inherit_yaw = str(_text).strip().lower() == 'true'
        if isinstance(_inherit_yaw, SDFError):
            return _inherit_yaw
        if _inherit_yaw is not None and cmp_version(version, "1.6") < 0:
            if _inherit_yaw != False:
                return SDFError(f"'inherit_yaw' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, inherit_yaw=_inherit_yaw)


class MaxDist(BaseModel):
    def __init__(self, sdf_version: str, max_dist: float = 0):
        self.__version__ = sdf_version
        self.max_dist = max_dist

    def to_version(self, target_version: str) -> "MaxDist":
        kwargs = {"sdf_version": target_version}
        kwargs["max_dist"] = self.max_dist
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_dist")
        if self.max_dist is not None:
            el.text = str(self.max_dist)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max_dist = _parse_double(_text)
        if isinstance(_max_dist, SDFError):
            return _max_dist
        return cls(sdf_version=version, max_dist=_max_dist)


class MinDist(BaseModel):
    def __init__(self, sdf_version: str, min_dist: float = 0):
        self.__version__ = sdf_version
        self.min_dist = min_dist

    def to_version(self, target_version: str) -> "MinDist":
        kwargs = {"sdf_version": target_version}
        kwargs["min_dist"] = self.min_dist
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_dist")
        if self.min_dist is not None:
            el.text = str(self.min_dist)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min_dist = _parse_double(_text)
        if isinstance(_min_dist, SDFError):
            return _min_dist
        return cls(sdf_version=version, min_dist=_min_dist)


class Name(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "Name":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _name = _text
        if isinstance(_name, SDFError):
            return _name
        return cls(sdf_version=version, name=_name)


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


class Plugin(BaseModel):
    def __init__(self, sdf_version: str, filename: str = "__default__", name: str = "__default__"):
        self.__version__ = sdf_version
        self.filename = filename
        self.name = name

    def to_version(self, target_version: str) -> "Plugin":
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plugin")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, filename=_filename, name=_name)


class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        degrees: bool = False,
        frame: str = "",
        pose: _SDFPose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy"
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.degrees = degrees
        self.frame = frame
        self.pose = pose
        self.relative_to = relative_to
        self.rotation_format = rotation_format

    def to_version(self, target_version: str) -> "Pose":
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["degrees"] = self.degrees
        kwargs["frame"] = self.frame
        kwargs["pose"] = self.pose
        kwargs["relative_to"] = self.relative_to
        kwargs["rotation_format"] = self.rotation_format
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        if _pose is not None and cmp_version(version, "1.2") < 0:
            if _pose != "0 0 0 0 0 0":
                return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
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
        return cls(sdf_version=version, degrees=_degrees, frame=_frame, pose=_pose, relative_to=_relative_to, rotation_format=_rotation_format)


class ProjectionType(BaseModel):
    def __init__(self, sdf_version: str, projection_type: str = "perspective"):
        self.__version__ = sdf_version
        self.projection_type = projection_type

    def to_version(self, target_version: str) -> "ProjectionType":
        if self.projection_type is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'projection_type' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["projection_type"] = self.projection_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("projection_type")
        if self.projection_type is not None:
            el.text = self.projection_type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "perspective"
        _projection_type = _text
        if isinstance(_projection_type, SDFError):
            return _projection_type
        if _projection_type is not None and cmp_version(version, "1.5") < 0:
            if _projection_type != "perspective":
                return SDFError(f"'projection_type' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, projection_type=_projection_type)


class Static(BaseModel):
    def __init__(self, sdf_version: str, static: bool = False):
        self.__version__ = sdf_version
        self.static = static

    def to_version(self, target_version: str) -> "Static":
        if self.static is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["static"] = self.static
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("static")
        if self.static is not None:
            el.text = str(self.static).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _static = str(_text).strip().lower() == 'true'
        if isinstance(_static, SDFError):
            return _static
        if _static is not None and cmp_version(version, "1.6") < 0:
            if _static != False:
                return SDFError(f"'static' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, static=_static)


class TrackVisual(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        inherit_yaw: "InheritYaw" = None,
        max_dist: "MaxDist" = None,
        min_dist: "MinDist" = None,
        name: "Name" = None,
        static: "Static" = None,
        use_model_frame: "UseModelFrame" = None,
        xyz: "Xyz" = None
    ):
        self.__version__ = sdf_version
        self.inherit_yaw = inherit_yaw
        self.max_dist = max_dist
        self.min_dist = min_dist
        self.name = name
        self.static = static
        self.use_model_frame = use_model_frame
        self.xyz = xyz

    def to_version(self, target_version: str) -> "TrackVisual":
        if self.inherit_yaw is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'inherit_yaw' is not supported in SDF version {target_version} (added in 1.6)")
        if self.static is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.6)")
        if self.use_model_frame is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'use_model_frame' is not supported in SDF version {target_version} (added in 1.6)")
        if self.xyz is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["inherit_yaw"] = self.inherit_yaw.to_version(target_version) if self.inherit_yaw is not None else None
        kwargs["max_dist"] = self.max_dist.to_version(target_version) if self.max_dist is not None else None
        kwargs["min_dist"] = self.min_dist.to_version(target_version) if self.min_dist is not None else None
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["static"] = self.static.to_version(target_version) if self.static is not None else None
        kwargs["use_model_frame"] = self.use_model_frame.to_version(target_version) if self.use_model_frame is not None else None
        kwargs["xyz"] = self.xyz.to_version(target_version) if self.xyz is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("track_visual")
        if self.inherit_yaw is not None:
            el.append(self.inherit_yaw.to_sdf(version))
        if self.max_dist is not None:
            el.append(self.max_dist.to_sdf(version))
        if self.min_dist is not None:
            el.append(self.min_dist.to_sdf(version))
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        if self.static is not None:
            el.append(self.static.to_sdf(version))
        if self.use_model_frame is not None:
            el.append(self.use_model_frame.to_sdf(version))
        if self.xyz is not None:
            el.append(self.xyz.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_inherit_yaw = el.find("inherit_yaw")
        if _c_inherit_yaw is not None:
            _res = InheritYaw._from_sdf(_c_inherit_yaw, version)
            if isinstance(_res, SDFError):
                return _res.extend("inherit_yaw")
            _inherit_yaw = _res
        else:
            _inherit_yaw = None
        if _inherit_yaw is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'inherit_yaw' is not supported in SDF version {version} (added in 1.6)")
        _c_max_dist = el.find("max_dist")
        if _c_max_dist is not None:
            _res = MaxDist._from_sdf(_c_max_dist, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_dist")
            _max_dist = _res
        else:
            _max_dist = None
        _c_min_dist = el.find("min_dist")
        if _c_min_dist is not None:
            _res = MinDist._from_sdf(_c_min_dist, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_dist")
            _min_dist = _res
        else:
            _min_dist = None
        _c_name = el.find("name")
        if _c_name is not None:
            _res = Name._from_sdf(_c_name, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _name = _res
        else:
            _name = None
        _c_static = el.find("static")
        if _c_static is not None:
            _res = Static._from_sdf(_c_static, version)
            if isinstance(_res, SDFError):
                return _res.extend("static")
            _static = _res
        else:
            _static = None
        if _static is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'static' is not supported in SDF version {version} (added in 1.6)")
        _c_use_model_frame = el.find("use_model_frame")
        if _c_use_model_frame is not None:
            _res = UseModelFrame._from_sdf(_c_use_model_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("use_model_frame")
            _use_model_frame = _res
        else:
            _use_model_frame = None
        if _use_model_frame is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'use_model_frame' is not supported in SDF version {version} (added in 1.6)")
        _c_xyz = el.find("xyz")
        if _c_xyz is not None:
            _res = Xyz._from_sdf(_c_xyz, version)
            if isinstance(_res, SDFError):
                return _res.extend("xyz")
            _xyz = _res
        else:
            _xyz = None
        if _xyz is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'xyz' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, inherit_yaw=_inherit_yaw, max_dist=_max_dist, min_dist=_min_dist, name=_name, static=_static, use_model_frame=_use_model_frame, xyz=_xyz)


class UseModelFrame(BaseModel):
    def __init__(self, sdf_version: str, use_model_frame: bool = True):
        self.__version__ = sdf_version
        self.use_model_frame = use_model_frame

    def to_version(self, target_version: str) -> "UseModelFrame":
        if self.use_model_frame is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'use_model_frame' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["use_model_frame"] = self.use_model_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("use_model_frame")
        if self.use_model_frame is not None:
            el.text = str(self.use_model_frame).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _use_model_frame = str(_text).strip().lower() == 'true'
        if isinstance(_use_model_frame, SDFError):
            return _use_model_frame
        if _use_model_frame is not None and cmp_version(version, "1.6") < 0:
            if _use_model_frame != True:
                return SDFError(f"'use_model_frame' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, use_model_frame=_use_model_frame)


class ViewController(BaseModel):
    def __init__(self, sdf_version: str, view_controller: str = "oribit"):
        self.__version__ = sdf_version
        self.view_controller = view_controller

    def to_version(self, target_version: str) -> "ViewController":
        kwargs = {"sdf_version": target_version}
        kwargs["view_controller"] = self.view_controller
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("view_controller")
        if self.view_controller is not None:
            el.text = self.view_controller
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "oribit"
        _view_controller = _text
        if isinstance(_view_controller, SDFError):
            return _view_controller
        return cls(sdf_version=version, view_controller=_view_controller)


class Xyz(BaseModel):
    def __init__(self, sdf_version: str, xyz: _SDFVector3 = None):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = _SDFVector3.from_sdf("-5.0 0.0 3.0")
        self.xyz = xyz

    def to_version(self, target_version: str) -> "Xyz":
        if self.xyz is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xyz")
        if self.xyz is not None:
            el.text = self.xyz.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "-5.0 0.0 3.0"
        _xyz = _SDFVector3._from_sdf(_text, version)
        if isinstance(_xyz, SDFError):
            return _xyz
        if _xyz is not None and cmp_version(version, "1.6") < 0:
            if _xyz != "-5.0 0.0 3.0":
                return SDFError(f"'xyz' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, xyz=_xyz)
