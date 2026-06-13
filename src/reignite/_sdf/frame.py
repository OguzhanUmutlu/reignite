### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Frame(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        attached_to: str | None = None,
        name: str | None = None,
        pose: _PoseT | None = None
    ):
        super().__init__(sdf_version)
        self.attached_to = attached_to
        self.name = name
        self.pose = _pose(pose) if pose is not None else None

    def to_version(self, target_version: str) -> "Frame":
        if self.attached_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'attached_to' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "attached_to": self.attached_to, "name": self.name, "pose": self.pose}
        return Frame(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("frame")
        if self.attached_to is not None:
            el.set("attached_to", self.attached_to)
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = str(self.pose)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Frame | SDFError":
        _raw_attached_to = el.get("attached_to")
        if _raw_attached_to is not None:
            _attached_to = _raw_attached_to
            if isinstance(_attached_to, SDFError):
                return _attached_to.extend("@attached_to")
        else:
            _attached_to = None
        if _attached_to is not None and cmp_version(version, "1.7") < 0:
            if _attached_to != None:
                return SDFError(f"'attached_to' is not supported in SDF version {version} (added in 1.7)")
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        _c_tmp = el.find("pose")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text)
            if isinstance(_val, SDFError):
                return _val.extend("pose")
            _pose = _val
        else:
            _pose = None
        return cls(sdf_version=version, attached_to=_attached_to, name=_name, pose=_pose)
