### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_int32
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.joint import Joint
    from ..elements.link import Link
    from ..elements.plugin import Plugin
    from ..elements.pose import Pose

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Actor(BaseModel):
    class Animation(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            filename: str | None = None,
            interpolate_x: bool | None = None,
            name: str | None = None,
            scale: float | None = None
        ):
            super().__init__(sdf_version)
            self.filename = filename
            self.interpolate_x = interpolate_x
            self.name = name
            self.scale = scale

        def to_version(self, target_version: str) -> "Actor.Animation":
            kwargs: dict = {"sdf_version": target_version, "filename": self.filename, "interpolate_x": self.interpolate_x, "name": self.name, "scale": self.scale}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("animation")
            if self.filename is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("filename")
                    _c_tmp.text = self.filename
                    el.append(_c_tmp)
                else:
                    el.set("filename", self.filename)
            if self.interpolate_x is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("interpolate_x")
                    _c_tmp.text = str(self.interpolate_x).lower()
                    el.append(_c_tmp)
                else:
                    el.set("interpolate_x", str(self.interpolate_x).lower())
            if self.name is not None:
                el.set("name", self.name)
            if self.scale is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("scale")
                    _c_tmp.text = str(self.scale)
                    el.append(_c_tmp)
                else:
                    el.set("scale", str(self.scale))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Actor.Animation | SDFError":
            _raw_filename = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("filename")
                if _c_tmp is not None: _raw_filename = _c_tmp.text
            else:
                _raw_filename = el.get("filename")
            if _raw_filename is None: _raw_filename = "__default__"
            _filename = _raw_filename
            if isinstance(_filename, SDFError):
                return _filename.extend("@filename")
            _raw_interpolate_x = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("interpolate_x")
                if _c_tmp is not None: _raw_interpolate_x = _c_tmp.text
            else:
                _raw_interpolate_x = el.get("interpolate_x")
            if _raw_interpolate_x is None: _raw_interpolate_x = False
            _interpolate_x = str(_raw_interpolate_x).strip().lower() == 'true'
            if isinstance(_interpolate_x, SDFError):
                return _interpolate_x.extend("@interpolate_x")
            _name = el.get("name", "__default__")
            if isinstance(_name, SDFError):
                return _name.extend("@name")
            _raw_scale = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("scale")
                if _c_tmp is not None: _raw_scale = _c_tmp.text
            else:
                _raw_scale = el.get("scale")
            if _raw_scale is None: _raw_scale = 1.0
            _scale = _parse_double(_raw_scale)
            if isinstance(_scale, SDFError):
                return _scale.extend("@scale")
            return cls(sdf_version=version, filename=_filename, interpolate_x=_interpolate_x, name=_name, scale=_scale)

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Actor.Origin":
            kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("origin")
            if self.pose is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("pose")
                    _c_tmp.text = str(self.pose)
                    el.append(_c_tmp)
                else:
                    el.set("pose", str(self.pose))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Actor.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is None: _raw_pose = "0 0 0 0 0 0"
            _pose = _parse_pose(_raw_pose)
            if isinstance(_pose, SDFError):
                return _pose.extend("@pose")
            return cls(sdf_version=version, pose=_pose)

    class Script(BaseModel):
        class Trajectory(BaseModel):
            class Waypoint(BaseModel):
                def __init__(
                    self,
                    sdf_version: str | None = None,
                    pose: _PoseT | None = None,
                    time: float | None = None
                ):
                    super().__init__(sdf_version)
                    self.pose = _pose(pose) if pose is not None else None
                    self.time = time

                def to_version(self, target_version: str) -> "Actor.Script.Trajectory.Waypoint":
                    kwargs: dict = {"sdf_version": target_version, "pose": self.pose, "time": self.time}
                    return self.__class__(**kwargs)

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.sdfversion is None and version is not None:
                        self.sdfversion = version
                    elif version is not None and version != self.sdfversion:
                        return self.to_version(str(version)).to_sdf()
                    el = ET.Element("waypoint")
                    if self.pose is not None:
                        if cmp_version(version, "1.2") >= 0:
                            _c_tmp = ET.Element("pose")
                            _c_tmp.text = str(self.pose)
                            el.append(_c_tmp)
                        else:
                            el.set("pose", str(self.pose))
                    if self.time is not None:
                        if cmp_version(version, "1.2") >= 0:
                            _c_tmp = ET.Element("time")
                            _c_tmp.text = str(self.time)
                            el.append(_c_tmp)
                        else:
                            el.set("time", str(self.time))
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Actor.Script.Trajectory.Waypoint | SDFError":
                    _raw_pose = None
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = el.find("pose")
                        if _c_tmp is not None: _raw_pose = _c_tmp.text
                    else:
                        _raw_pose = el.get("pose")
                    if _raw_pose is None: _raw_pose = "0 0 0 0 0 0"
                    _pose = _parse_pose(_raw_pose)
                    if isinstance(_pose, SDFError):
                        return _pose.extend("@pose")
                    _raw_time = None
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = el.find("time")
                        if _c_tmp is not None: _raw_time = _c_tmp.text
                    else:
                        _raw_time = el.get("time")
                    if _raw_time is None: _raw_time = 0.0
                    _time = _parse_double(_raw_time)
                    if isinstance(_time, SDFError):
                        return _time.extend("@time")
                    return cls(sdf_version=version, pose=_pose, time=_time)

            def __init__(
                self,
                sdf_version: str | None = None,
                id: int | None = None,
                tension: float | None = None,
                type: str | None = None,
                waypoints: List["Actor.Script.Trajectory.Waypoint"] = None
            ):
                super().__init__(sdf_version)
                self.id = id
                self.tension = tension
                self.type = type
                self.waypoints = waypoints or []
                for _i, _c in enumerate(self.waypoints):
                    if not hasattr(_c, 'to_version'): continue
                    if getattr(_c, 'sdfversion', None) is None:
                        _c.sdfversion = self.sdfversion
                    elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.waypoints[_i] = _c.to_version(self.sdfversion)

            def add_waypoint(self, *items: "Actor.Script.Trajectory.Waypoint"):
                if self.waypoints is None:
                    self.waypoints = []
                self.waypoints.extend(items)

            def to_version(self, target_version: str) -> "Actor.Script.Trajectory":
                if self.tension is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'tension' is not supported in SDF version {target_version} (added in 1.6)")
                kwargs: dict = {"sdf_version": target_version, "id": self.id, "tension": self.tension, "type": self.type, "waypoints": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.waypoints or [])]}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("trajectory")
                if self.id is not None:
                    el.set("id", str(self.id))
                if self.tension is not None:
                    el.set("tension", str(self.tension))
                if self.type is not None:
                    el.set("type", self.type)
                for item in (self.waypoints or []):
                    _child_res = item.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('waypoint')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Actor.Script.Trajectory | SDFError":
                _id = _parse_int32(el.get("id", 0))
                if isinstance(_id, SDFError):
                    return _id.extend("@id")
                _tension = _parse_double(el.get("tension", 0.0))
                if isinstance(_tension, SDFError):
                    return _tension.extend("@tension")
                if _tension is not None and cmp_version(version, "1.6") < 0:
                    if _tension != 0.0:
                        return SDFError(f"'tension' is not supported in SDF version {version} (added in 1.6)")
                _type = el.get("type", "__default__")
                if isinstance(_type, SDFError):
                    return _type.extend("@type")
                _waypoints = []
                for c in el.findall("waypoint"):
                    _res = cls.Waypoint._from_sdf(c, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("waypoint")
                    _waypoints.append(_res)
                return cls(sdf_version=version, id=_id, tension=_tension, type=_type, waypoints=_waypoints)

        def __init__(
            self,
            sdf_version: str | None = None,
            auto_start: bool | None = None,
            delay_start: float | None = None,
            loop: bool | None = None,
            trajectories: List["Actor.Script.Trajectory"] = None
        ):
            super().__init__(sdf_version)
            self.auto_start = auto_start
            self.delay_start = delay_start
            self.loop = loop
            self.trajectories = trajectories or []
            for _i, _c in enumerate(self.trajectories):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, 'sdfversion', None) is None:
                    _c.sdfversion = self.sdfversion
                elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.trajectories[_i] = _c.to_version(self.sdfversion)

        def add_trajectory(self, *items: "Actor.Script.Trajectory"):
            if self.trajectories is None:
                self.trajectories = []
            self.trajectories.extend(items)

        def to_version(self, target_version: str) -> "Actor.Script":
            kwargs: dict = {"sdf_version": target_version, "auto_start": self.auto_start, "delay_start": self.delay_start, "loop": self.loop, "trajectories": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.trajectories or [])]}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("script")
            if self.auto_start is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("auto_start")
                    _c_tmp.text = str(self.auto_start).lower()
                    el.append(_c_tmp)
                else:
                    el.set("auto_start", str(self.auto_start).lower())
            if self.delay_start is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("delay_start")
                    _c_tmp.text = str(self.delay_start)
                    el.append(_c_tmp)
                else:
                    el.set("delay_start", str(self.delay_start))
            if self.loop is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("loop")
                    _c_tmp.text = str(self.loop).lower()
                    el.append(_c_tmp)
                else:
                    el.set("loop", str(self.loop).lower())
            for item in (self.trajectories or []):
                _child_res = item.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('trajectory')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Actor.Script | SDFError":
            _raw_auto_start = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("auto_start")
                if _c_tmp is not None: _raw_auto_start = _c_tmp.text
            else:
                _raw_auto_start = el.get("auto_start")
            if _raw_auto_start is None: _raw_auto_start = True
            _auto_start = str(_raw_auto_start).strip().lower() == 'true'
            if isinstance(_auto_start, SDFError):
                return _auto_start.extend("@auto_start")
            _raw_delay_start = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("delay_start")
                if _c_tmp is not None: _raw_delay_start = _c_tmp.text
            else:
                _raw_delay_start = el.get("delay_start")
            if _raw_delay_start is None: _raw_delay_start = 0.0
            _delay_start = _parse_double(_raw_delay_start)
            if isinstance(_delay_start, SDFError):
                return _delay_start.extend("@delay_start")
            _raw_loop = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("loop")
                if _c_tmp is not None: _raw_loop = _c_tmp.text
            else:
                _raw_loop = el.get("loop")
            if _raw_loop is None: _raw_loop = True
            _loop = str(_raw_loop).strip().lower() == 'true'
            if isinstance(_loop, SDFError):
                return _loop.extend("@loop")
            _trajectories = []
            for c in el.findall("trajectory"):
                _res = cls.Trajectory._from_sdf(c, version)
                if isinstance(_res, SDFError):
                    return _res.extend("trajectory")
                _trajectories.append(_res)
            return cls(sdf_version=version, auto_start=_auto_start, delay_start=_delay_start, loop=_loop, trajectories=_trajectories)

    class Skin(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            filename: str | None = None,
            scale: float | None = None
        ):
            super().__init__(sdf_version)
            self.filename = filename
            self.scale = scale

        def to_version(self, target_version: str) -> "Actor.Skin":
            kwargs: dict = {"sdf_version": target_version, "filename": self.filename, "scale": self.scale}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("skin")
            if self.filename is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("filename")
                    _c_tmp.text = self.filename
                    el.append(_c_tmp)
                else:
                    el.set("filename", self.filename)
            if self.scale is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("scale")
                    _c_tmp.text = str(self.scale)
                    el.append(_c_tmp)
                else:
                    el.set("scale", str(self.scale))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Actor.Skin | SDFError":
            _raw_filename = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("filename")
                if _c_tmp is not None: _raw_filename = _c_tmp.text
            else:
                _raw_filename = el.get("filename")
            if _raw_filename is None: _raw_filename = "__default__"
            _filename = _raw_filename
            if isinstance(_filename, SDFError):
                return _filename.extend("@filename")
            _raw_scale = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("scale")
                if _c_tmp is not None: _raw_scale = _c_tmp.text
            else:
                _raw_scale = el.get("scale")
            if _raw_scale is None: _raw_scale = 1.0
            _scale = _parse_double(_raw_scale)
            if isinstance(_scale, SDFError):
                return _scale.extend("@scale")
            return cls(sdf_version=version, filename=_filename, scale=_scale)

    def __init__(
        self,
        sdf_version: str | None = None,
        animations: List["Actor.Animation"] = None,
        frames: List["Frame"] = None,
        joints: List["Joint"] = None,
        links: List["Link"] = None,
        name: str | None = None,
        origin: "Actor.Origin" = None,
        plugins: List["Plugin"] = None,
        pose: "Pose" = None,
        script: "Actor.Script" = None,
        skin: "Actor.Skin" = None,
        static: bool | None = None
    ):
        super().__init__(sdf_version)
        self.animations = animations or []
        self.frames = frames or []
        self.joints = joints or []
        self.links = links or []
        self.name = name
        self.origin = origin
        self.plugins = plugins or []
        self.pose = pose
        self.script = script
        self.skin = skin
        self.static = static
        for _i, _c in enumerate(self.animations):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.animations[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.joints):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.joints[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.links):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.links[_i] = _c.to_version(self.sdfversion)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, 'sdfversion', None) is None:
                self.origin.sdfversion = self.sdfversion
            elif getattr(self.origin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.origin = self.origin.to_version(self.sdfversion)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.plugins[_i] = _c.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)
        if self.script is not None and hasattr(self.script, 'to_version'):
            if getattr(self.script, 'sdfversion', None) is None:
                self.script.sdfversion = self.sdfversion
            elif getattr(self.script, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.script = self.script.to_version(self.sdfversion)
        if self.skin is not None and hasattr(self.skin, 'to_version'):
            if getattr(self.skin, 'sdfversion', None) is None:
                self.skin.sdfversion = self.sdfversion
            elif getattr(self.skin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.skin = self.skin.to_version(self.sdfversion)

    def add_animation(self, *items: "Actor.Animation"):
        if self.animations is None:
            self.animations = []
        self.animations.extend(items)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_joint(self, *items: "Joint"):
        if self.joints is None:
            self.joints = []
        self.joints.extend(items)

    def add_link(self, *items: "Link"):
        if self.links is None:
            self.links = []
        self.links.extend(items)

    def add_plugin(self, *items: "Plugin"):
        if self.plugins is None:
            self.plugins = []
        self.plugins.extend(items)

    def to_version(self, target_version: str) -> "Actor":
        from ..elements.frame import Frame
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.frames is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs: dict = {"sdf_version": target_version, "animations": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.animations or [])], "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "joints": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joints or [])], "links": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.links or [])], "name": self.name, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])], "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "script": self.script.to_version(target_version) if self.script is not None and hasattr(self.script, "to_version") else self.script, "skin": self.skin.to_version(target_version) if self.skin is not None and hasattr(self.skin, "to_version") else self.skin, "static": self.static}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("actor")
        for item in (self.animations or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('animation')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.joints or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('joint')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.links or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('link')
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
        for item in (self.plugins or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _child_res = self.pose.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.script is not None:
            _child_res = self.script.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('script')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.skin is not None:
            _child_res = self.skin.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('skin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.static is not None:
            if cmp_version(version, "1.5") >= 0:
                _c_tmp = ET.Element("static")
                _c_tmp.text = str(self.static).lower()
                el.append(_c_tmp)
            else:
                el.set("static", str(self.static).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Actor | SDFError":
        from ..elements.frame import Frame
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        _animations = []
        for c in el.findall("animation"):
            _res = cls.Animation._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("animation")
            _animations.append(_res)
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _joints = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joints.append(_res)
        _links = []
        for c in el.findall("link"):
            _res = Link._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link")
            _links.append(_res)
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = cls.Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
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
        if _pose is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _c_script = el.find("script")
        if _c_script is not None:
            _res = cls.Script._from_sdf(_c_script, version)
            if isinstance(_res, SDFError):
                return _res.extend("script")
            _script = _res
        else:
            _script = None
        _c_skin = el.find("skin")
        if _c_skin is not None:
            _res = cls.Skin._from_sdf(_c_skin, version)
            if isinstance(_res, SDFError):
                return _res.extend("skin")
            _skin = _res
        else:
            _skin = None
        _raw_static = None
        if cmp_version(version, "1.5") >= 0:
            _c_tmp = el.find("static")
            if _c_tmp is not None: _raw_static = _c_tmp.text
        else:
            _raw_static = el.get("static")
        if _raw_static is None: _raw_static = False
        _static = str(_raw_static).strip().lower() == 'true'
        if isinstance(_static, SDFError):
            return _static.extend("@static")
        return cls(sdf_version=version, animations=_animations, frames=_frames, joints=_joints, links=_links, name=_name, origin=_origin, plugins=_plugins, pose=_pose, script=_script, skin=_skin, static=_static)
