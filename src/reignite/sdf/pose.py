from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model
from ..utils.pose import Pose
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations


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
        if self.pose is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.5)")
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
        if _pose is not None and cmp_version(version, "1.5") < 0:
            if _pose != "0 0 0 0 0 0":
                raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.5)")
        _frame = el.get("frame", "")
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
