### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose, Pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame

def _parse_pose(raw: str, el: ET.Element | None = None) -> _PoseT | SDFError:
    try:
        is_degrees = el is not None and str(el.get('degrees')).lower() == 'true'
        return _pose(raw, degrees=is_degrees)
    except ValueError as e:
        return SDFError(str(e))

def _pose_to_sdf(val: _PoseT, el: ET.Element | None = None) -> str:
    if el is not None:
        el.attrib.pop('degrees', None)
    if isinstance(val, Pose):
        return val.to_sdf()
    p = _pose(val)
    return p.to_sdf()


# noinspection PyUnusedImports
class LightState(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        frames: List["Frame"] = None,
        name: str | None = None,
        pose: _PoseT | None = None
    ):
        super().__init__(sdf_version)
        self.frames = frames or []
        self.name = name
        self.pose = _pose(pose) if pose is not None else None
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def to_version(self, target_version: str) -> "LightState":
        from ..elements.frame import Frame
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "name": self.name, "pose": self.pose}
        return LightState(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("light_state")
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = _pose_to_sdf(self.pose, _c_tmp)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "LightState | SDFError":
        from ..elements.frame import Frame
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
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
            _val = _parse_pose(_text, _c_tmp)
            if isinstance(_val, SDFError):
                return _val.extend("pose")
            _pose = _val
        else:
            _pose = None
        return cls(sdf_version=version, frames=_frames, name=_name, pose=_pose)
