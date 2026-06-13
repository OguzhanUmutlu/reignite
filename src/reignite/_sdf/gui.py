### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose, Pose
from ..utils.vector3 import _Vector3T, _vector3
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
        el.attrib.pop('degrees', None)
    if isinstance(val, Pose):
        return val.to_sdf()
    p = _pose(val)
    return p.to_sdf()

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Gui(BaseModel):
    class Camera(BaseModel):
        class Origin(BaseModel):
            def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
                super().__init__(sdf_version)
                self.pose = _pose(pose) if pose is not None else None

            def to_version(self, target_version: str) -> "Gui.Camera.Origin":
                kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
                return Gui.Camera.Origin(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("origin")
                if self.pose is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("pose")
                        _c_tmp.text = _pose_to_sdf(self.pose, el)
                        el.append(_c_tmp)
                    else:
                        el.set("pose", _pose_to_sdf(self.pose, el))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Gui.Camera.Origin | SDFError":
                _raw_pose = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("pose")
                    if _c_tmp is not None: _raw_pose = _c_tmp.text
                else:
                    _raw_pose = el.get("pose")
                if _raw_pose is not None:
                    _pose = _parse_pose(_raw_pose, el)
                    if isinstance(_pose, SDFError):
                        return _pose.extend("@pose")
                else:
                    _pose = None
                return cls(sdf_version=version, pose=_pose)

        class TrackVisual(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                inherit_yaw: bool | None = None,
                max_dist: float | None = None,
                min_dist: float | None = None,
                name: str | None = None,
                static: bool | None = None,
                use_model_frame: bool | None = None,
                xyz: _Vector3T | None = None
            ):
                super().__init__(sdf_version)
                self.inherit_yaw = inherit_yaw
                self.max_dist = max_dist
                self.min_dist = min_dist
                self.name = name
                self.static = static
                self.use_model_frame = use_model_frame
                self.xyz = _vector3(xyz) if xyz is not None else None

            def to_version(self, target_version: str) -> "Gui.Camera.TrackVisual":
                if self.inherit_yaw is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'inherit_yaw' is not supported in SDF version {target_version} (added in 1.6)")
                if self.static is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.6)")
                if self.use_model_frame is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'use_model_frame' is not supported in SDF version {target_version} (added in 1.6)")
                if self.xyz is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.6)")
                kwargs: dict = {"sdf_version": target_version, "inherit_yaw": self.inherit_yaw, "max_dist": self.max_dist, "min_dist": self.min_dist, "name": self.name, "static": self.static, "use_model_frame": self.use_model_frame, "xyz": self.xyz}
                return Gui.Camera.TrackVisual(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("track_visual")
                if self.inherit_yaw is not None:
                    _c_tmp = ET.Element("inherit_yaw")
                    _c_tmp.text = str(self.inherit_yaw).lower()
                    el.append(_c_tmp)
                if self.max_dist is not None:
                    _c_tmp = ET.Element("max_dist")
                    _c_tmp.text = str(self.max_dist)
                    el.append(_c_tmp)
                if self.min_dist is not None:
                    _c_tmp = ET.Element("min_dist")
                    _c_tmp.text = str(self.min_dist)
                    el.append(_c_tmp)
                if self.name is not None:
                    _c_tmp = ET.Element("name")
                    _c_tmp.text = self.name
                    el.append(_c_tmp)
                if self.static is not None:
                    _c_tmp = ET.Element("static")
                    _c_tmp.text = str(self.static).lower()
                    el.append(_c_tmp)
                if self.use_model_frame is not None:
                    _c_tmp = ET.Element("use_model_frame")
                    _c_tmp.text = str(self.use_model_frame).lower()
                    el.append(_c_tmp)
                if self.xyz is not None:
                    _c_tmp = ET.Element("xyz")
                    _c_tmp.text = str(self.xyz)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Gui.Camera.TrackVisual | SDFError":
                _c_tmp = el.find("inherit_yaw")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else False
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("inherit_yaw")
                    _inherit_yaw = _val
                else:
                    _inherit_yaw = None
                if _inherit_yaw is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'inherit_yaw' is not supported in SDF version {version} (added in 1.6)")
                _c_tmp = el.find("max_dist")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("max_dist")
                    _max_dist = _val
                else:
                    _max_dist = None
                _c_tmp = el.find("min_dist")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("min_dist")
                    _min_dist = _val
                else:
                    _min_dist = None
                _c_tmp = el.find("name")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("name")
                    _name = _val
                else:
                    _name = None
                _c_tmp = el.find("static")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else False
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("static")
                    _static = _val
                else:
                    _static = None
                if _static is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'static' is not supported in SDF version {version} (added in 1.6)")
                _c_tmp = el.find("use_model_frame")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else True
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("use_model_frame")
                    _use_model_frame = _val
                else:
                    _use_model_frame = None
                if _use_model_frame is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'use_model_frame' is not supported in SDF version {version} (added in 1.6)")
                _c_tmp = el.find("xyz")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "-5.0 0.0 3.0"
                    _val = _parse_vector3(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("xyz")
                    _xyz = _val
                else:
                    _xyz = None
                if _xyz is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'xyz' is not supported in SDF version {version} (added in 1.6)")
                return cls(sdf_version=version, inherit_yaw=_inherit_yaw, max_dist=_max_dist, min_dist=_min_dist, name=_name, static=_static, use_model_frame=_use_model_frame, xyz=_xyz)

        def __init__(
            self,
            sdf_version: str | None = None,
            frames: List["Frame"] = None,
            name: str | None = None,
            origin: "Gui.Camera.Origin" = None,
            pose: _PoseT | None = None,
            projection_type: str | None = None,
            track_visual: "Gui.Camera.TrackVisual" = None,
            view_controller: str | None = None
        ):
            super().__init__(sdf_version)
            self.frames = frames or []
            self.name = name
            self.origin = origin
            self.pose = _pose(pose) if pose is not None else None
            self.projection_type = projection_type
            self.track_visual = track_visual
            self.view_controller = view_controller
            for _i, _c in enumerate(self.frames):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, 'sdfversion', None) is None:
                    _c.sdfversion = self.sdfversion
                elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.frames[_i] = _c.to_version(self.sdfversion)
            if self.origin is not None and hasattr(self.origin, 'to_version'):
                if getattr(self.origin, 'sdfversion', None) is None:
                    self.origin.sdfversion = self.sdfversion
                elif getattr(self.origin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.origin = self.origin.to_version(self.sdfversion)
            if self.track_visual is not None and hasattr(self.track_visual, 'to_version'):
                if getattr(self.track_visual, 'sdfversion', None) is None:
                    self.track_visual.sdfversion = self.sdfversion
                elif getattr(self.track_visual, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.track_visual = self.track_visual.to_version(self.sdfversion)

        def add_frame(self, *items: "Frame"):
            if self.frames is None:
                self.frames = []
            self.frames.extend(items)

        def to_version(self, target_version: str) -> "Gui.Camera":
            from ..elements.frame import Frame
            if self.frames and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
            if self.frames and cmp_version(target_version, "1.7") >= 0:
                raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
            if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.pose is not None and cmp_version(target_version, "1.2") < 0:
                raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
            if self.projection_type is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'projection_type' is not supported in SDF version {target_version} (added in 1.5)")
            kwargs: dict = {"sdf_version": target_version, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "name": self.name, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "pose": self.pose, "projection_type": self.projection_type, "track_visual": self.track_visual.to_version(target_version) if self.track_visual is not None and hasattr(self.track_visual, "to_version") else self.track_visual, "view_controller": self.view_controller}
            return Gui.Camera(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.frame import Frame
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("camera")
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
            if self.origin is not None:
                _child_res = self.origin.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('origin')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.pose is not None:
                _c_tmp = ET.Element("pose")
                _c_tmp.text = _pose_to_sdf(self.pose, _c_tmp)
                el.append(_c_tmp)
            if self.projection_type is not None:
                _c_tmp = ET.Element("projection_type")
                _c_tmp.text = self.projection_type
                el.append(_c_tmp)
            if self.track_visual is not None:
                _child_res = self.track_visual.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('track_visual')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.view_controller is not None:
                _c_tmp = ET.Element("view_controller")
                _c_tmp.text = self.view_controller
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Gui.Camera | SDFError":
            from ..elements.frame import Frame
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
            _c_origin = el.find("origin")
            if _c_origin is not None:
                _res = cls.Origin._from_sdf(_c_origin, version)
                if isinstance(_res, SDFError):
                    return _res.extend("origin")
                _origin = _res
            else:
                _origin = None
            _c_tmp = el.find("pose")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
                _val = _parse_pose(_text, _c_tmp)
                if isinstance(_val, SDFError):
                    return _val.extend("pose")
                _pose = _val
            else:
                _pose = None
            if _pose is not None and cmp_version(version, "1.2") < 0:
                return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
            _c_tmp = el.find("projection_type")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "perspective"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("projection_type")
                _projection_type = _val
            else:
                _projection_type = None
            if _projection_type is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'projection_type' is not supported in SDF version {version} (added in 1.5)")
            _c_track_visual = el.find("track_visual")
            if _c_track_visual is not None:
                _res = cls.TrackVisual._from_sdf(_c_track_visual, version)
                if isinstance(_res, SDFError):
                    return _res.extend("track_visual")
                _track_visual = _res
            else:
                _track_visual = None
            _c_tmp = el.find("view_controller")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "oribit"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("view_controller")
                _view_controller = _val
            else:
                _view_controller = None
            return cls(sdf_version=version, frames=_frames, name=_name, origin=_origin, pose=_pose, projection_type=_projection_type, track_visual=_track_visual, view_controller=_view_controller)

    def __init__(
        self,
        sdf_version: str | None = None,
        camera: "Gui.Camera" = None,
        fullscreen: bool | None = None,
        plugins: List["Plugin"] = None
    ):
        super().__init__(sdf_version)
        self.camera = camera
        self.fullscreen = fullscreen
        self.plugins = plugins or []
        if self.camera is not None and hasattr(self.camera, 'to_version'):
            if getattr(self.camera, 'sdfversion', None) is None:
                self.camera.sdfversion = self.sdfversion
            elif getattr(self.camera, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.camera = self.camera.to_version(self.sdfversion)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.plugins[_i] = _c.to_version(self.sdfversion)

    def add_plugin(self, *items: "Plugin"):
        if self.plugins is None:
            self.plugins = []
        self.plugins.extend(items)

    def to_version(self, target_version: str) -> "Gui":
        from ..elements.plugin import Plugin
        if self.plugins and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'plugins' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs: dict = {"sdf_version": target_version, "camera": self.camera.to_version(target_version) if self.camera is not None and hasattr(self.camera, "to_version") else self.camera, "fullscreen": self.fullscreen, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])]}
        return Gui(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.plugin import Plugin
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("gui")
        if self.camera is not None:
            _child_res = self.camera.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('camera')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.fullscreen is not None:
            el.set("fullscreen", str(self.fullscreen).lower())
        for item in (self.plugins or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Gui | SDFError":
        from ..elements.plugin import Plugin
        _c_camera = el.find("camera")
        if _c_camera is not None:
            _res = cls.Camera._from_sdf(_c_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera")
            _camera = _res
        else:
            _camera = None
        _raw_fullscreen = el.get("fullscreen")
        if _raw_fullscreen is not None:
            _fullscreen = str(_raw_fullscreen).strip().lower() == 'true'
            if isinstance(_fullscreen, SDFError):
                return _fullscreen.extend("@fullscreen")
        else:
            _fullscreen = None
        _plugins = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugins.append(_res)
        if _plugins and cmp_version(version, "1.5") < 0:
            return SDFError(f"'plugins' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, camera=_camera, fullscreen=_fullscreen, plugins=_plugins)
