### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations


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
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
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
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
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


class Frame(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        attached_to: str = "",
        name: str = "",
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.attached_to = attached_to
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "Frame":
        if self.attached_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'attached_to' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["attached_to"] = self.attached_to
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.attached_to is not None:
            el.set("attached_to", self.attached_to)
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _attached_to = el.get("attached_to", "")
        if isinstance(_attached_to, SDFError):
            return _attached_to.extend("@attached_to")
        if _attached_to is not None and cmp_version(version, "1.7") < 0:
            if _attached_to != "":
                return SDFError(f"'attached_to' is not supported in SDF version {version} (added in 1.7)")
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, attached_to=_attached_to, name=_name, pose=_pose)
