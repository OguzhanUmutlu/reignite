from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ._base import Model
from ..utils.pose import Pose
from ..utils.vector3 import Vector3
from ..utils.version import cmp_version


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



class ViewController(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "ViewController":
        _text = el.text or "oribit"
        _view_controller = _text
        return cls(sdf_version=version, view_controller=_view_controller)


class Origin(Model):
    def __init__(self, sdf_version: str, pose: Pose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Origin":
        _pose = Pose.from_sdf(el.get("pose", "0 0 0 0 0 0"))
        return cls(sdf_version=version, pose=_pose)


class Name(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Name":
        _text = el.text or "__default__"
        _name = _text
        return cls(sdf_version=version, name=_name)


class MinDist(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "MinDist":
        _text = el.text or 0
        _min_dist = _parse_double(_text)
        return cls(sdf_version=version, min_dist=_min_dist)


class MaxDist(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxDist":
        _text = el.text or 0
        _max_dist = _parse_double(_text)
        return cls(sdf_version=version, max_dist=_max_dist)


class Static(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Static":
        _text = el.text or False
        _static = _text.strip().lower() == 'true'
        if _static is not None and cmp_version(version, "1.6") < 0:
            if _static != False:
                raise ValueError(f"'static' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, static=_static)


class UseModelFrame(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "UseModelFrame":
        _text = el.text or True
        _use_model_frame = _text.strip().lower() == 'true'
        if _use_model_frame is not None and cmp_version(version, "1.6") < 0:
            if _use_model_frame != True:
                raise ValueError(f"'use_model_frame' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, use_model_frame=_use_model_frame)


class Xyz(Model):
    def __init__(self, sdf_version: str, xyz: Vector3 = None):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("-5.0 0.0 3.0")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Xyz":
        _text = el.text or "-5.0 0.0 3.0"
        _xyz = Vector3.from_sdf(_text)
        if _xyz is not None and cmp_version(version, "1.6") < 0:
            if _xyz != "-5.0 0.0 3.0":
                raise ValueError(f"'xyz' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, xyz=_xyz)


class InheritYaw(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "InheritYaw":
        _text = el.text or False
        _inherit_yaw = _text.strip().lower() == 'true'
        if _inherit_yaw is not None and cmp_version(version, "1.6") < 0:
            if _inherit_yaw != False:
                raise ValueError(f"'inherit_yaw' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, inherit_yaw=_inherit_yaw)


class TrackVisual(Model):
    def __init__(
        self,
        sdf_version: str,
        name: "Name" = None,
        min_dist: "MinDist" = None,
        max_dist: "MaxDist" = None,
        static: "Static" = None,
        use_model_frame: "UseModelFrame" = None,
        xyz: "Xyz" = None,
        inherit_yaw: "InheritYaw" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.min_dist = min_dist
        self.max_dist = max_dist
        self.static = static
        self.use_model_frame = use_model_frame
        self.xyz = xyz
        self.inherit_yaw = inherit_yaw

    def to_version(self, target_version: str) -> "TrackVisual":
        if self.static is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.6)")
        if self.use_model_frame is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'use_model_frame' is not supported in SDF version {target_version} (added in 1.6)")
        if self.xyz is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.6)")
        if self.inherit_yaw is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'inherit_yaw' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["min_dist"] = self.min_dist.to_version(target_version) if self.min_dist is not None else None
        kwargs["max_dist"] = self.max_dist.to_version(target_version) if self.max_dist is not None else None
        kwargs["static"] = self.static.to_version(target_version) if self.static is not None else None
        kwargs["use_model_frame"] = self.use_model_frame.to_version(target_version) if self.use_model_frame is not None else None
        kwargs["xyz"] = self.xyz.to_version(target_version) if self.xyz is not None else None
        kwargs["inherit_yaw"] = self.inherit_yaw.to_version(target_version) if self.inherit_yaw is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("track_visual")
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        if self.min_dist is not None:
            el.append(self.min_dist.to_sdf(version))
        if self.max_dist is not None:
            el.append(self.max_dist.to_sdf(version))
        if self.static is not None:
            el.append(self.static.to_sdf(version))
        if self.use_model_frame is not None:
            el.append(self.use_model_frame.to_sdf(version))
        if self.xyz is not None:
            el.append(self.xyz.to_sdf(version))
        if self.inherit_yaw is not None:
            el.append(self.inherit_yaw.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "TrackVisual":
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name, version) if _c_name is not None else None
        _c_min_dist = el.find("min_dist")
        _min_dist = MinDist.from_sdf(_c_min_dist, version) if _c_min_dist is not None else None
        _c_max_dist = el.find("max_dist")
        _max_dist = MaxDist.from_sdf(_c_max_dist, version) if _c_max_dist is not None else None
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static, version) if _c_static is not None else None
        if _static is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'static' is not supported in SDF version {version} (added in 1.6)")
        _c_use_model_frame = el.find("use_model_frame")
        _use_model_frame = UseModelFrame.from_sdf(_c_use_model_frame, version) if _c_use_model_frame is not None else None
        if _use_model_frame is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'use_model_frame' is not supported in SDF version {version} (added in 1.6)")
        _c_xyz = el.find("xyz")
        _xyz = Xyz.from_sdf(_c_xyz, version) if _c_xyz is not None else None
        if _xyz is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'xyz' is not supported in SDF version {version} (added in 1.6)")
        _c_inherit_yaw = el.find("inherit_yaw")
        _inherit_yaw = InheritYaw.from_sdf(_c_inherit_yaw, version) if _c_inherit_yaw is not None else None
        if _inherit_yaw is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'inherit_yaw' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, name=_name, min_dist=_min_dist, max_dist=_max_dist, static=_static, use_model_frame=_use_model_frame, xyz=_xyz, inherit_yaw=_inherit_yaw)


class Pose(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: Pose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Pose":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        if _pose is not None and cmp_version(version, "1.2") < 0:
            if _pose != "0 0 0 0 0 0":
                raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _frame = el.get("frame", "")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                raise ValueError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                raise ValueError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                raise ValueError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Frame(Model):
    def __init__(self, sdf_version: str, name: str = "", pose: "Pose" = None):
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
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Frame":
        _name = el.get("name", "")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        return cls(sdf_version=version, name=_name, pose=_pose)


class ProjectionType(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "ProjectionType":
        _text = el.text or "perspective"
        _projection_type = _text
        if _projection_type is not None and cmp_version(version, "1.5") < 0:
            if _projection_type != "perspective":
                raise ValueError(f"'projection_type' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, projection_type=_projection_type)


class Camera(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "user_camera",
        view_controller: "ViewController" = None,
        origin: "Origin" = None,
        track_visual: "TrackVisual" = None,
        pose: "Pose" = None,
        frame: List["Frame"] = None,
        projection_type: "ProjectionType" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.view_controller = view_controller
        self.origin = origin
        self.track_visual = track_visual
        self.pose = pose
        self.frame = frame or []
        self.projection_type = projection_type

    def to_version(self, target_version: str) -> "Camera":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.projection_type is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'projection_type' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["view_controller"] = self.view_controller.to_version(target_version) if self.view_controller is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["track_visual"] = self.track_visual.to_version(target_version) if self.track_visual is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["projection_type"] = self.projection_type.to_version(target_version) if self.projection_type is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera")
        if self.name is not None:
            el.set("name", self.name)
        if self.view_controller is not None:
            el.append(self.view_controller.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.track_visual is not None:
            el.append(self.track_visual.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.projection_type is not None:
            el.append(self.projection_type.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Camera":
        _name = el.get("name", "user_camera")
        _c_view_controller = el.find("view_controller")
        _view_controller = ViewController.from_sdf(_c_view_controller, version) if _c_view_controller is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_track_visual = el.find("track_visual")
        _track_visual = TrackVisual.from_sdf(_c_track_visual, version) if _c_track_visual is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _frame = [Frame.from_sdf(c, version) for c in el.findall("frame")]
        if _frame and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_projection_type = el.find("projection_type")
        _projection_type = ProjectionType.from_sdf(_c_projection_type, version) if _c_projection_type is not None else None
        if _projection_type is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'projection_type' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, name=_name, view_controller=_view_controller, origin=_origin, track_visual=_track_visual, pose=_pose, frame=_frame, projection_type=_projection_type)


class Plugin(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Plugin":
        _name = el.get("name", "__default__")
        _filename = el.get("filename", "__default__")
        return cls(sdf_version=version, name=_name, filename=_filename)


class Gui(Model):
    def __init__(
        self,
        sdf_version: str,
        fullscreen: bool = False,
        camera: "Camera" = None,
        plugin: List["Plugin"] = None
    ):
        self.__version__ = sdf_version
        self.fullscreen = fullscreen
        self.camera = camera
        self.plugin = plugin or []

    def to_version(self, target_version: str) -> "Gui":
        if self.plugin is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["fullscreen"] = self.fullscreen
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gui")
        if self.fullscreen is not None:
            el.set("fullscreen", str(self.fullscreen).lower())
        if self.camera is not None:
            el.append(self.camera.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gui":
        _fullscreen = el.get("fullscreen", False).strip().lower() == 'true'
        _c_camera = el.find("camera")
        _camera = Camera.from_sdf(_c_camera, version) if _c_camera is not None else None
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        if _plugin and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, fullscreen=_fullscreen, camera=_camera, plugin=_plugin)
