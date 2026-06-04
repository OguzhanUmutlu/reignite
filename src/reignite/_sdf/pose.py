### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str | None = None,
        degrees: bool | None = None,
        frame: str | None = None,
        pose: _PoseT | None = None,
        relative_to: str | None = None,
        rotation_format: str | None = None
    ):
        super().__init__(sdf_version)
        self.degrees = degrees
        self.frame = frame
        self.pose = _pose(pose) if pose is not None else None
        self.relative_to = relative_to
        self.rotation_format = rotation_format

    def to_version(self, target_version: str) -> "Pose":
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.pose is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.5)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs: dict = {"sdf_version": target_version, "degrees": self.degrees, "frame": self.frame, "pose": self.pose, "relative_to": self.relative_to, "rotation_format": self.rotation_format}
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("pose")
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.pose is not None:
            el.text = str(self.pose)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Pose | SDFError":
        _raw_degrees = el.get("degrees")
        if _raw_degrees is not None:
            _degrees = str(_raw_degrees).strip().lower() == 'true'
            if isinstance(_degrees, SDFError):
                return _degrees.extend("@degrees")
        else:
            _degrees = None
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        _raw_frame = el.get("frame")
        if _raw_frame is not None:
            _frame = _raw_frame
            if isinstance(_frame, SDFError):
                return _frame.extend("@frame")
        else:
            _frame = None
        _raw_pose = el.text
        if _raw_pose is not None:
            _pose = _parse_pose(_raw_pose)
            if isinstance(_pose, SDFError):
                return _pose
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.5") < 0:
            if _pose != "0 0 0 0 0 0":
                return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.5)")
        _raw_relative_to = el.get("relative_to")
        if _raw_relative_to is not None:
            _relative_to = _raw_relative_to
            if isinstance(_relative_to, SDFError):
                return _relative_to.extend("@relative_to")
        else:
            _relative_to = None
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != None:
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _raw_rotation_format = el.get("rotation_format")
        if _raw_rotation_format is not None:
            _rotation_format = _raw_rotation_format
            if isinstance(_rotation_format, SDFError):
                return _rotation_format.extend("@rotation_format")
        else:
            _rotation_format = None
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, degrees=_degrees, frame=_frame, pose=_pose, relative_to=_relative_to, rotation_format=_rotation_format)
