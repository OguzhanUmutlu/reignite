### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.plugin import Plugin
    from ..elements.pose import Pose


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



class Projector(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        far_clip: float = 10.0,
        fov: float = 0.785,
        frames: List["Frame"] = None,
        name: str = "__default__",
        near_clip: float = 0.1,
        plugins: List["Plugin"] = None,
        pose: "Pose" = None,
        texture: str = "__default__",
        visibility_flags: int = 4294967295
    ):
        super().__init__(sdf_version)
        self.far_clip = far_clip
        self.fov = fov
        self.frames = frames or []
        self.name = name
        self.near_clip = near_clip
        self.plugins = plugins or []
        self.pose = pose
        self.texture = texture
        self.visibility_flags = visibility_flags
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.plugins[_i] = _c.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

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
        from ..elements.pose import Pose
        if self.frames is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["far_clip"] = self.far_clip
        kwargs["fov"] = self.fov
        kwargs["frames"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])]
        kwargs["name"] = self.name
        kwargs["near_clip"] = self.near_clip
        kwargs["plugins"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
        kwargs["texture"] = self.texture
        kwargs["visibility_flags"] = self.visibility_flags
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
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
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
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
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            if hasattr(self.pose, 'to_sdf'):
                _child_res = self.pose.to_sdf(version)
            else:
                _child_res = str(self.pose)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
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
        from ..elements.pose import Pose
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
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
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
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
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
