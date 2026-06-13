### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_uint32
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.plugin import Plugin

def _parse_pose(raw: str, el: ET.Element | None = None) -> _PoseT | SDFError:
    try:
        is_degrees = el is not None and str(el.get('degrees')).lower() == 'true'
        return _pose(raw, degrees=is_degrees)
    except ValueError as e:
        return SDFError(str(e))

def _pose_to_sdf(val: _PoseT, el: ET.Element | None = None) -> str:
    if el is not None:
        el.set('degrees', 'true')
    if isinstance(val, _Pose):
        return f'{val.x} {val.y} {val.z} {val.roll_deg} {val.pitch_deg} {val.yaw_deg}'
    p = _pose(val)
    return f'{p.x} {p.y} {p.z} {p.roll_deg} {p.pitch_deg} {p.yaw_deg}'


# noinspection PyUnusedImports
class Projector(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        far_clip: float | None = None,
        fov: float | None = None,
        frames: List["Frame"] = None,
        name: str | None = None,
        near_clip: float | None = None,
        plugins: List["Plugin"] = None,
        pose: _PoseT | None = None,
        texture: str | None = None,
        visibility_flags: int | None = None
    ):
        super().__init__(sdf_version)
        self.far_clip = far_clip
        self.fov = fov
        self.frames = frames or []
        self.name = name
        self.near_clip = near_clip
        self.plugins = plugins or []
        self.pose = _pose(pose) if pose is not None else None
        self.texture = texture
        self.visibility_flags = visibility_flags
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.plugins[_i] = _c.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_plugin(self, *items: "Plugin"):
        if self.plugins is None:
            self.plugins = []
        self.plugins.extend(items)

    def to_version(self, target_version: str) -> "Projector":
        from ..elements.frame import Frame
        from ..elements.plugin import Plugin
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "far_clip": self.far_clip, "fov": self.fov, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "name": self.name, "near_clip": self.near_clip, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])], "pose": self.pose, "texture": self.texture, "visibility_flags": self.visibility_flags}
        return Projector(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.plugin import Plugin
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("projector")
        if self.far_clip is not None:
            _c_tmp = ET.Element("far_clip")
            _c_tmp.text = str(self.far_clip)
            el.append(_c_tmp)
        if self.fov is not None:
            _c_tmp = ET.Element("fov")
            _c_tmp.text = str(self.fov)
            el.append(_c_tmp)
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
        if self.near_clip is not None:
            _c_tmp = ET.Element("near_clip")
            _c_tmp.text = str(self.near_clip)
            el.append(_c_tmp)
        for item in (self.plugins or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = _pose_to_sdf(self.pose, _c_tmp)
            el.append(_c_tmp)
        if self.texture is not None:
            _c_tmp = ET.Element("texture")
            _c_tmp.text = self.texture
            el.append(_c_tmp)
        if self.visibility_flags is not None:
            _c_tmp = ET.Element("visibility_flags")
            _c_tmp.text = str(self.visibility_flags)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Projector | SDFError":
        from ..elements.frame import Frame
        from ..elements.plugin import Plugin
        _c_tmp = el.find("far_clip")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 10.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("far_clip")
            _far_clip = _val
        else:
            _far_clip = None
        _c_tmp = el.find("fov")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.785
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("fov")
            _fov = _val
        else:
            _fov = None
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        _c_tmp = el.find("near_clip")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("near_clip")
            _near_clip = _val
        else:
            _near_clip = None
        _plugins = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugins.append(_res)
        _c_tmp = el.find("pose")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text, _c_tmp)
            if isinstance(_val, SDFError):
                return _val.extend("pose")
            _pose = _val
        else:
            _pose = None
        _c_tmp = el.find("texture")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("texture")
            _texture = _val
        else:
            _texture = None
        _c_tmp = el.find("visibility_flags")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 4294967295
            _val = _parse_uint32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("visibility_flags")
            _visibility_flags = _val
        else:
            _visibility_flags = None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, far_clip=_far_clip, fov=_fov, frames=_frames, name=_name, near_clip=_near_clip, plugins=_plugins, pose=_pose, texture=_texture, visibility_flags=_visibility_flags)
