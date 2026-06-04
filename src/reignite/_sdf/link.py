### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.audio_sink import AudioSink
    from ..elements.audio_source import AudioSource
    from ..elements.battery import Battery
    from ..elements.collision import Collision
    from ..elements.frame import Frame
    from ..elements.inertial import Inertial
    from ..elements.light import Light
    from ..elements.particle_emitter import ParticleEmitter
    from ..elements.pose import Pose
    from ..elements.projector import Projector
    from ..elements.sensor import Sensor
    from ..elements.visual import Visual

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Link(BaseModel):
    class Damping(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            angular: float | None = None,
            linear: float | None = None
        ):
            super().__init__(sdf_version)
            self.angular = angular
            self.linear = linear

        def to_version(self, target_version: str) -> "Link.Damping":
            kwargs: dict = {"sdf_version": target_version, "angular": self.angular, "linear": self.linear}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("damping")
            if self.angular is not None:
                _c_tmp = ET.Element("angular")
                _c_tmp.text = str(self.angular)
                el.append(_c_tmp)
            if self.linear is not None:
                _c_tmp = ET.Element("linear")
                _c_tmp.text = str(self.linear)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Link.Damping | SDFError":
            _c_tmp = el.find("angular")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("angular")
                _angular = _val
            else:
                _angular = None
            _c_tmp = el.find("linear")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("linear")
                _linear = _val
            else:
                _linear = None
            return cls(sdf_version=version, angular=_angular, linear=_linear)

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Link.Origin":
            kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
            return self.__class__(**kwargs)

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
                    _c_tmp.text = str(self.pose)
                    el.append(_c_tmp)
                else:
                    el.set("pose", str(self.pose))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Link.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is not None:
                _pose = _parse_pose(_raw_pose)
                if isinstance(_pose, SDFError):
                    return _pose.extend("@pose")
            else:
                _pose = None
            return cls(sdf_version=version, pose=_pose)

    class VelocityDecay(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            angular: float | None = None,
            linear: float | None = None
        ):
            super().__init__(sdf_version)
            self.angular = angular
            self.linear = linear

        def to_version(self, target_version: str) -> "Link.VelocityDecay":
            kwargs: dict = {"sdf_version": target_version, "angular": self.angular, "linear": self.linear}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("velocity_decay")
            if self.angular is not None:
                _c_tmp = ET.Element("angular")
                _c_tmp.text = str(self.angular)
                el.append(_c_tmp)
            if self.linear is not None:
                _c_tmp = ET.Element("linear")
                _c_tmp.text = str(self.linear)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Link.VelocityDecay | SDFError":
            _c_tmp = el.find("angular")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("angular")
                _angular = _val
            else:
                _angular = None
            _c_tmp = el.find("linear")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("linear")
                _linear = _val
            else:
                _linear = None
            return cls(sdf_version=version, angular=_angular, linear=_linear)

    def __init__(
        self,
        sdf_version: str | None = None,
        audio_sinks: List["AudioSink"] = None,
        audio_sources: List["AudioSource"] = None,
        batteries: List["Battery"] = None,
        collisions: List["Collision"] = None,
        damping: "Link.Damping" = None,
        enable_wind: bool | None = None,
        frames: List["Frame"] = None,
        gravity: bool | None = None,
        inertial: "Inertial" = None,
        kinematic: bool | None = None,
        lights: List["Light"] = None,
        must_be_base_link: bool | None = None,
        name: str | None = None,
        origin: "Link.Origin" = None,
        particle_emitters: List["ParticleEmitter"] = None,
        pose: "Pose" = None,
        projector: "Projector" = None,
        self_collide: bool | None = None,
        sensor: "Sensor" = None,
        velocity_decay: "Link.VelocityDecay" = None,
        visuals: List["Visual"] = None
    ):
        super().__init__(sdf_version)
        self.audio_sinks = audio_sinks or []
        self.audio_sources = audio_sources or []
        self.batteries = batteries or []
        self.collisions = collisions or []
        self.damping = damping
        self.enable_wind = enable_wind
        self.frames = frames or []
        self.gravity = gravity
        self.inertial = inertial
        self.kinematic = kinematic
        self.lights = lights or []
        self.must_be_base_link = must_be_base_link
        self.name = name
        self.origin = origin
        self.particle_emitters = particle_emitters or []
        self.pose = pose
        self.projector = projector
        self.self_collide = self_collide
        self.sensor = sensor
        self.velocity_decay = velocity_decay
        self.visuals = visuals or []
        for _i, _c in enumerate(self.audio_sinks):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.audio_sinks[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.audio_sources):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.audio_sources[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.batteries):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.batteries[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.collisions):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.collisions[_i] = _c.to_version(self.sdfversion)
        if self.damping is not None and hasattr(self.damping, 'to_version'):
            if getattr(self.damping, 'sdfversion', None) is None:
                self.damping.sdfversion = self.sdfversion
            elif getattr(self.damping, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.damping = self.damping.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.inertial is not None and hasattr(self.inertial, 'to_version'):
            if getattr(self.inertial, 'sdfversion', None) is None:
                self.inertial.sdfversion = self.sdfversion
            elif getattr(self.inertial, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.inertial = self.inertial.to_version(self.sdfversion)
        for _i, _c in enumerate(self.lights):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.lights[_i] = _c.to_version(self.sdfversion)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, 'sdfversion', None) is None:
                self.origin.sdfversion = self.sdfversion
            elif getattr(self.origin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.origin = self.origin.to_version(self.sdfversion)
        for _i, _c in enumerate(self.particle_emitters):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.particle_emitters[_i] = _c.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)
        if self.projector is not None and hasattr(self.projector, 'to_version'):
            if getattr(self.projector, 'sdfversion', None) is None:
                self.projector.sdfversion = self.sdfversion
            elif getattr(self.projector, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.projector = self.projector.to_version(self.sdfversion)
        if self.sensor is not None and hasattr(self.sensor, 'to_version'):
            if getattr(self.sensor, 'sdfversion', None) is None:
                self.sensor.sdfversion = self.sdfversion
            elif getattr(self.sensor, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.sensor = self.sensor.to_version(self.sdfversion)
        if self.velocity_decay is not None and hasattr(self.velocity_decay, 'to_version'):
            if getattr(self.velocity_decay, 'sdfversion', None) is None:
                self.velocity_decay.sdfversion = self.sdfversion
            elif getattr(self.velocity_decay, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.velocity_decay = self.velocity_decay.to_version(self.sdfversion)
        for _i, _c in enumerate(self.visuals):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.visuals[_i] = _c.to_version(self.sdfversion)

    def add_audio_sink(self, *items: "AudioSink"):
        if self.audio_sinks is None:
            self.audio_sinks = []
        self.audio_sinks.extend(items)

    def add_audio_source(self, *items: "AudioSource"):
        if self.audio_sources is None:
            self.audio_sources = []
        self.audio_sources.extend(items)

    def add_battery(self, *items: "Battery"):
        if self.batteries is None:
            self.batteries = []
        self.batteries.extend(items)

    def add_collision(self, *items: "Collision"):
        if self.collisions is None:
            self.collisions = []
        self.collisions.extend(items)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_light(self, *items: "Light"):
        if self.lights is None:
            self.lights = []
        self.lights.extend(items)

    def add_particle_emitter(self, *items: "ParticleEmitter"):
        if self.particle_emitters is None:
            self.particle_emitters = []
        self.particle_emitters.extend(items)

    def add_visual(self, *items: "Visual"):
        if self.visuals is None:
            self.visuals = []
        self.visuals.extend(items)

    def to_version(self, target_version: str) -> "Link":
        from ..elements.audio_sink import AudioSink
        from ..elements.audio_source import AudioSource
        from ..elements.battery import Battery
        from ..elements.collision import Collision
        from ..elements.frame import Frame
        from ..elements.inertial import Inertial
        from ..elements.light import Light
        from ..elements.particle_emitter import ParticleEmitter
        from ..elements.pose import Pose
        from ..elements.projector import Projector
        from ..elements.sensor import Sensor
        from ..elements.visual import Visual
        if self.audio_sinks and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio_sinks' is not supported in SDF version {target_version} (added in 1.4)")
        if self.audio_sources and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio_sources' is not supported in SDF version {target_version} (added in 1.4)")
        if self.batteries and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'batteries' is not supported in SDF version {target_version} (added in 1.5)")
        if self.enable_wind is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.6)")
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.lights and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'lights' is not supported in SDF version {target_version} (added in 1.6)")
        if self.must_be_base_link is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {target_version} (added in 1.4)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.particle_emitters and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'particle_emitters' is not supported in SDF version {target_version} (added in 1.6)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.velocity_decay is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'velocity_decay' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs: dict = {"sdf_version": target_version, "audio_sinks": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.audio_sinks or [])], "audio_sources": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.audio_sources or [])], "batteries": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.batteries or [])], "collisions": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.collisions or [])], "damping": self.damping.to_version(target_version) if self.damping is not None and hasattr(self.damping, "to_version") else self.damping, "enable_wind": self.enable_wind, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "gravity": self.gravity, "inertial": self.inertial.to_version(target_version) if self.inertial is not None and hasattr(self.inertial, "to_version") else self.inertial, "kinematic": self.kinematic, "lights": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.lights or [])], "must_be_base_link": self.must_be_base_link, "name": self.name, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "particle_emitters": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.particle_emitters or [])], "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "projector": self.projector.to_version(target_version) if self.projector is not None and hasattr(self.projector, "to_version") else self.projector, "self_collide": self.self_collide, "sensor": self.sensor.to_version(target_version) if self.sensor is not None and hasattr(self.sensor, "to_version") else self.sensor, "velocity_decay": self.velocity_decay.to_version(target_version) if self.velocity_decay is not None and hasattr(self.velocity_decay, "to_version") else self.velocity_decay, "visuals": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.visuals or [])]}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.audio_sink import AudioSink
        from ..elements.audio_source import AudioSource
        from ..elements.battery import Battery
        from ..elements.collision import Collision
        from ..elements.frame import Frame
        from ..elements.inertial import Inertial
        from ..elements.light import Light
        from ..elements.particle_emitter import ParticleEmitter
        from ..elements.pose import Pose
        from ..elements.projector import Projector
        from ..elements.sensor import Sensor
        from ..elements.visual import Visual
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("link")
        for item in (self.audio_sinks or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('audio_sink')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.audio_sources or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('audio_source')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.batteries or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('battery')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.collisions or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('collision')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.damping is not None:
            _child_res = self.damping.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('damping')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            if cmp_version(version, "1.2") >= 0:
                _item_el.tag = "velocity_decay"
            else:
                _item_el.tag = "damping"
            el.append(_item_el)
        if self.enable_wind is not None:
            _c_tmp = ET.Element("enable_wind")
            _c_tmp.text = str(self.enable_wind).lower()
            el.append(_c_tmp)
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.gravity is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("gravity")
                _c_tmp.text = str(self.gravity).lower()
                el.append(_c_tmp)
            else:
                el.set("gravity", str(self.gravity).lower())
        if self.inertial is not None:
            _child_res = self.inertial.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('inertial')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.kinematic is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("kinematic")
                _c_tmp.text = str(self.kinematic).lower()
                el.append(_c_tmp)
            else:
                el.set("kinematic", str(self.kinematic).lower())
        for item in (self.lights or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('light')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.must_be_base_link is not None:
            _c_tmp = ET.Element("must_be_base_link")
            _c_tmp.text = str(self.must_be_base_link).lower()
            el.append(_c_tmp)
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
        for item in (self.particle_emitters or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('particle_emitter')
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
        if self.projector is not None:
            _child_res = self.projector.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('projector')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.self_collide is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("self_collide")
                _c_tmp.text = str(self.self_collide).lower()
                el.append(_c_tmp)
            else:
                el.set("self_collide", str(self.self_collide).lower())
        if self.sensor is not None:
            _child_res = self.sensor.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('sensor')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.velocity_decay is not None:
            _child_res = self.velocity_decay.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('velocity_decay')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.visuals or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('visual')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Link | SDFError":
        from ..elements.audio_sink import AudioSink
        from ..elements.audio_source import AudioSource
        from ..elements.battery import Battery
        from ..elements.collision import Collision
        from ..elements.frame import Frame
        from ..elements.inertial import Inertial
        from ..elements.light import Light
        from ..elements.particle_emitter import ParticleEmitter
        from ..elements.pose import Pose
        from ..elements.projector import Projector
        from ..elements.sensor import Sensor
        from ..elements.visual import Visual
        _audio_sinks = []
        for c in el.findall("audio_sink"):
            _res = AudioSink._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("audio_sink")
            _audio_sinks.append(_res)
        if _audio_sinks and cmp_version(version, "1.4") < 0:
            return SDFError(f"'audio_sinks' is not supported in SDF version {version} (added in 1.4)")
        _audio_sources = []
        for c in el.findall("audio_source"):
            _res = AudioSource._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("audio_source")
            _audio_sources.append(_res)
        if _audio_sources and cmp_version(version, "1.4") < 0:
            return SDFError(f"'audio_sources' is not supported in SDF version {version} (added in 1.4)")
        _batteries = []
        for c in el.findall("battery"):
            _res = Battery._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("battery")
            _batteries.append(_res)
        if _batteries and cmp_version(version, "1.5") < 0:
            return SDFError(f"'batteries' is not supported in SDF version {version} (added in 1.5)")
        _collisions = []
        for c in el.findall("collision"):
            _res = Collision._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collisions.append(_res)
        _c_damping = None
        if cmp_version(version, "1.2") >= 0:
            _c_damping = el.find("velocity_decay")
        else:
            _c_damping = el.find("damping")
        if _c_damping is not None:
            _res = cls.Damping._from_sdf(_c_damping, version)
            if isinstance(_res, SDFError):
                return _res.extend("damping")
            _damping = _res
        else:
            _damping = None
        _c_tmp = el.find("enable_wind")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("enable_wind")
            _enable_wind = _val
        else:
            _enable_wind = None
        if _enable_wind is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.6)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _raw_gravity = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("gravity")
            if _c_tmp is not None: _raw_gravity = _c_tmp.text
        else:
            _raw_gravity = el.get("gravity")
        if _raw_gravity is not None:
            _gravity = str(_raw_gravity).strip().lower() == 'true'
            if isinstance(_gravity, SDFError):
                return _gravity.extend("@gravity")
        else:
            _gravity = None
        _c_inertial = el.find("inertial")
        if _c_inertial is not None:
            _res = Inertial._from_sdf(_c_inertial, version)
            if isinstance(_res, SDFError):
                return _res.extend("inertial")
            _inertial = _res
        else:
            _inertial = None
        _raw_kinematic = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("kinematic")
            if _c_tmp is not None: _raw_kinematic = _c_tmp.text
        else:
            _raw_kinematic = el.get("kinematic")
        if _raw_kinematic is not None:
            _kinematic = str(_raw_kinematic).strip().lower() == 'true'
            if isinstance(_kinematic, SDFError):
                return _kinematic.extend("@kinematic")
        else:
            _kinematic = None
        _lights = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _lights.append(_res)
        if _lights and cmp_version(version, "1.6") < 0:
            return SDFError(f"'lights' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("must_be_base_link")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("must_be_base_link")
            _must_be_base_link = _val
        else:
            _must_be_base_link = None
        if _must_be_base_link is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'must_be_base_link' is not supported in SDF version {version} (added in 1.4)")
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
        _particle_emitters = []
        for c in el.findall("particle_emitter"):
            _res = ParticleEmitter._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("particle_emitter")
            _particle_emitters.append(_res)
        if _particle_emitters and cmp_version(version, "1.6") < 0:
            return SDFError(f"'particle_emitters' is not supported in SDF version {version} (added in 1.6)")
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
        _c_projector = el.find("projector")
        if _c_projector is not None:
            _res = Projector._from_sdf(_c_projector, version)
            if isinstance(_res, SDFError):
                return _res.extend("projector")
            _projector = _res
        else:
            _projector = None
        _raw_self_collide = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("self_collide")
            if _c_tmp is not None: _raw_self_collide = _c_tmp.text
        else:
            _raw_self_collide = el.get("self_collide")
        if _raw_self_collide is not None:
            _self_collide = str(_raw_self_collide).strip().lower() == 'true'
            if isinstance(_self_collide, SDFError):
                return _self_collide.extend("@self_collide")
        else:
            _self_collide = None
        _c_sensor = el.find("sensor")
        if _c_sensor is not None:
            _res = Sensor._from_sdf(_c_sensor, version)
            if isinstance(_res, SDFError):
                return _res.extend("sensor")
            _sensor = _res
        else:
            _sensor = None
        _c_velocity_decay = el.find("velocity_decay")
        if _c_velocity_decay is not None:
            _res = cls.VelocityDecay._from_sdf(_c_velocity_decay, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity_decay")
            _velocity_decay = _res
        else:
            _velocity_decay = None
        if _velocity_decay is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'velocity_decay' is not supported in SDF version {version} (added in 1.2)")
        _visuals = []
        for c in el.findall("visual"):
            _res = Visual._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("visual")
            _visuals.append(_res)
        return cls(sdf_version=version, audio_sinks=_audio_sinks, audio_sources=_audio_sources, batteries=_batteries, collisions=_collisions, damping=_damping, enable_wind=_enable_wind, frames=_frames, gravity=_gravity, inertial=_inertial, kinematic=_kinematic, lights=_lights, must_be_base_link=_must_be_base_link, name=_name, origin=_origin, particle_emitters=_particle_emitters, pose=_pose, projector=_projector, self_collide=_self_collide, sensor=_sensor, velocity_decay=_velocity_decay, visuals=_visuals)
