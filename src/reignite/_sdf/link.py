### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
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



class Link(BaseModel):
    class Damping(BaseModel):
        def __init__(self, sdf_version: str | None = None, angular: float = 0.0, linear: float = 0.0):
            super().__init__(sdf_version)
            self.angular = angular
            self.linear = linear

        def to_version(self, target_version: str) -> "Link.Damping":
            kwargs = {"sdf_version": target_version}
            kwargs["angular"] = self.angular
            kwargs["linear"] = self.linear
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
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
        def __init__(self, sdf_version: str | None = None, pose: _SDFPose = None):
            super().__init__(sdf_version)
            if pose is None:
                pose = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
            self.pose = pose

        def to_version(self, target_version: str) -> "Link.Origin":
            kwargs = {"sdf_version": target_version}
            kwargs["pose"] = self.pose
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("origin")
            if self.pose is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("pose")
                    _c_tmp.text = self.pose.to_sdf(version)
                    el.append(_c_tmp)
                else:
                    el.set("pose", self.pose.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Link.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is None: _raw_pose = "0 0 0 0 0 0"
            _pose = _SDFPose._from_sdf(_raw_pose, version)
            if isinstance(_pose, SDFError):
                return _pose.extend("@pose")
            return cls(sdf_version=version, pose=_pose)

    class VelocityDecay(BaseModel):
        def __init__(self, sdf_version: str | None = None, angular: float = 0.0, linear: float = 0.0):
            super().__init__(sdf_version)
            self.angular = angular
            self.linear = linear

        def to_version(self, target_version: str) -> "Link.VelocityDecay":
            kwargs = {"sdf_version": target_version}
            kwargs["angular"] = self.angular
            kwargs["linear"] = self.linear
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
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
        acceleration: _SDFPose = None,
        audio_sinks: List["AudioSink"] = None,
        audio_sources: List["AudioSource"] = None,
        batterys: List["Battery"] = None,
        collisions: List["Collision"] = None,
        damping: "Link.Damping" = None,
        enable_wind: bool = False,
        frames: List["Frame"] = None,
        gravity: bool = True,
        inertial: "Inertial" = None,
        kinematic: bool = False,
        lights: List["Light"] = None,
        must_be_base_link: bool = False,
        name: str = "__default__",
        origin: "Link.Origin" = None,
        particle_emitters: List["ParticleEmitter"] = None,
        pose: "Pose" = None,
        projector: "Projector" = None,
        self_collide: bool = False,
        sensor: "Sensor" = None,
        velocity: _SDFPose = None,
        velocity_decay: "Link.VelocityDecay" = None,
        visuals: List["Visual"] = None,
        wrench: _SDFPose = None
    ):
        super().__init__(sdf_version)
        if acceleration is None:
            acceleration = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        if velocity is None:
            velocity = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        if wrench is None:
            wrench = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        self.acceleration = acceleration
        self.audio_sinks = audio_sinks or []
        self.audio_sources = audio_sources or []
        self.batterys = batterys or []
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
        self.velocity = velocity
        self.velocity_decay = velocity_decay
        self.visuals = visuals or []
        self.wrench = wrench
        for _i, _c in enumerate(self.audio_sinks):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.audio_sinks[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.audio_sources):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.audio_sources[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.batterys):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.batterys[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.collisions):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.collisions[_i] = _c.to_version(self.__version__)
        if self.damping is not None and hasattr(self.damping, 'to_version'):
            if getattr(self.damping, '__version__', None) is None:
                self.damping.__version__ = self.__version__
            elif getattr(self.damping, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.damping = self.damping.to_version(self.__version__)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        if self.inertial is not None and hasattr(self.inertial, 'to_version'):
            if getattr(self.inertial, '__version__', None) is None:
                self.inertial.__version__ = self.__version__
            elif getattr(self.inertial, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.inertial = self.inertial.to_version(self.__version__)
        for _i, _c in enumerate(self.lights):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.lights[_i] = _c.to_version(self.__version__)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, '__version__', None) is None:
                self.origin.__version__ = self.__version__
            elif getattr(self.origin, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.origin = self.origin.to_version(self.__version__)
        for _i, _c in enumerate(self.particle_emitters):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.particle_emitters[_i] = _c.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)
        if self.projector is not None and hasattr(self.projector, 'to_version'):
            if getattr(self.projector, '__version__', None) is None:
                self.projector.__version__ = self.__version__
            elif getattr(self.projector, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.projector = self.projector.to_version(self.__version__)
        if self.sensor is not None and hasattr(self.sensor, 'to_version'):
            if getattr(self.sensor, '__version__', None) is None:
                self.sensor.__version__ = self.__version__
            elif getattr(self.sensor, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.sensor = self.sensor.to_version(self.__version__)
        if self.velocity_decay is not None and hasattr(self.velocity_decay, 'to_version'):
            if getattr(self.velocity_decay, '__version__', None) is None:
                self.velocity_decay.__version__ = self.__version__
            elif getattr(self.velocity_decay, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.velocity_decay = self.velocity_decay.to_version(self.__version__)
        for _i, _c in enumerate(self.visuals):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.visuals[_i] = _c.to_version(self.__version__)

    def add_audio_sink(self, *items: "AudioSink"):
        if self.audio_sinks is None:
            self.audio_sinks = []
        self.audio_sinks.extend(items)

    def add_audio_source(self, *items: "AudioSource"):
        if self.audio_sources is None:
            self.audio_sources = []
        self.audio_sources.extend(items)

    def add_battery(self, *items: "Battery"):
        if self.batterys is None:
            self.batterys = []
        self.batterys.extend(items)

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
        if self.acceleration is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {target_version} (added in 1.5)")
        if self.acceleration is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.audio_sinks is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio_sinks' is not supported in SDF version {target_version} (added in 1.4)")
        if self.audio_sinks is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'audio_sinks' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.audio_sources is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio_sources' is not supported in SDF version {target_version} (added in 1.4)")
        if self.audio_sources is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'audio_sources' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.batterys is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'batterys' is not supported in SDF version {target_version} (added in 1.12)")
        if self.damping is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'damping' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.enable_wind is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.12)")
        if self.frames is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.gravity is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'gravity' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.inertial is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'inertial' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.kinematic is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'kinematic' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.lights is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'lights' is not supported in SDF version {target_version} (added in 1.12)")
        if self.must_be_base_link is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {target_version} (added in 1.4)")
        if self.must_be_base_link is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.particle_emitters is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'particle_emitters' is not supported in SDF version {target_version} (added in 1.12)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.projector is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'projector' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.self_collide is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.sensor is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'sensor' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.velocity is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (added in 1.5)")
        if self.velocity is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.velocity_decay is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'velocity_decay' is not supported in SDF version {target_version} (added in 1.2)")
        if self.velocity_decay is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'velocity_decay' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.visuals is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'visuals' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.wrench is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'wrench' is not supported in SDF version {target_version} (added in 1.5)")
        if self.wrench is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'wrench' is not supported in SDF version {target_version} (removed in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["acceleration"] = self.acceleration
        kwargs["audio_sinks"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.audio_sinks or [])]
        kwargs["audio_sources"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.audio_sources or [])]
        kwargs["batterys"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.batterys or [])]
        kwargs["collisions"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.collisions or [])]
        kwargs["damping"] = self.damping.to_version(target_version) if hasattr(self.damping, "to_version") else self.damping
        kwargs["enable_wind"] = self.enable_wind
        kwargs["frames"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])]
        kwargs["gravity"] = self.gravity
        kwargs["inertial"] = self.inertial.to_version(target_version) if hasattr(self.inertial, "to_version") else self.inertial
        kwargs["kinematic"] = self.kinematic
        kwargs["lights"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.lights or [])]
        kwargs["must_be_base_link"] = self.must_be_base_link
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if hasattr(self.origin, "to_version") else self.origin
        kwargs["particle_emitters"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.particle_emitters or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
        kwargs["projector"] = self.projector.to_version(target_version) if hasattr(self.projector, "to_version") else self.projector
        kwargs["self_collide"] = self.self_collide
        kwargs["sensor"] = self.sensor.to_version(target_version) if hasattr(self.sensor, "to_version") else self.sensor
        kwargs["velocity"] = self.velocity
        kwargs["velocity_decay"] = self.velocity_decay.to_version(target_version) if hasattr(self.velocity_decay, "to_version") else self.velocity_decay
        kwargs["visuals"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.visuals or [])]
        kwargs["wrench"] = self.wrench
        new_obj = self.__class__(**kwargs)
        return new_obj

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
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("link")
        if self.acceleration is not None:
            _c_tmp = ET.Element("acceleration")
            _c_tmp.text = self.acceleration.to_sdf(version)
            el.append(_c_tmp)
        for item in (self.audio_sinks or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('audio_sink')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.audio_sources or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('audio_source')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.batterys or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('battery')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.collisions or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('collision')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if cmp_version(version, "1.2") < 0:
            if self.damping is None:
                self.damping = self.__class__.Damping(sdf_version=version)
        if self.damping is not None:
            if hasattr(self.damping, 'to_sdf'):
                _child_res = self.damping.to_sdf(version)
            else:
                _child_res = str(self.damping)
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
        if self.gravity is not None:
            el.set("gravity", str(self.gravity).lower())
        if self.inertial is not None:
            if hasattr(self.inertial, 'to_sdf'):
                _child_res = self.inertial.to_sdf(version)
            else:
                _child_res = str(self.inertial)
            if isinstance(_child_res, str):
                _item_el = ET.Element('inertial')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.kinematic is not None:
            el.set("kinematic", str(self.kinematic).lower())
        for item in (self.lights or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
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
            if hasattr(self.origin, 'to_sdf'):
                _child_res = self.origin.to_sdf(version)
            else:
                _child_res = str(self.origin)
            if isinstance(_child_res, str):
                _item_el = ET.Element('origin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.particle_emitters or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('particle_emitter')
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
        if self.projector is not None:
            if hasattr(self.projector, 'to_sdf'):
                _child_res = self.projector.to_sdf(version)
            else:
                _child_res = str(self.projector)
            if isinstance(_child_res, str):
                _item_el = ET.Element('projector')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.self_collide is not None:
            el.set("self_collide", str(self.self_collide).lower())
        if self.sensor is not None:
            if hasattr(self.sensor, 'to_sdf'):
                _child_res = self.sensor.to_sdf(version)
            else:
                _child_res = str(self.sensor)
            if isinstance(_child_res, str):
                _item_el = ET.Element('sensor')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.velocity is not None:
            _c_tmp = ET.Element("velocity")
            _c_tmp.text = self.velocity.to_sdf(version)
            el.append(_c_tmp)
        if self.velocity_decay is not None:
            if hasattr(self.velocity_decay, 'to_sdf'):
                _child_res = self.velocity_decay.to_sdf(version)
            else:
                _child_res = str(self.velocity_decay)
            if isinstance(_child_res, str):
                _item_el = ET.Element('velocity_decay')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.visuals or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('visual')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.wrench is not None:
            _c_tmp = ET.Element("wrench")
            _c_tmp.text = self.wrench.to_sdf(version)
            el.append(_c_tmp)
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
        _c_tmp = el.find("acceleration")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _SDFPose._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("acceleration")
            _acceleration = _val
        else:
            _acceleration = None
        if _acceleration is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'acceleration' is not supported in SDF version {version} (added in 1.5)")
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
        _batterys = []
        for c in el.findall("battery"):
            _res = Battery._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("battery")
            _batterys.append(_res)
        if _batterys and cmp_version(version, "1.12") < 0:
            return SDFError(f"'batterys' is not supported in SDF version {version} (added in 1.12)")
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
            _res = cls.Damping._from_sdf(ET.Element("damping"), version)
            if isinstance(_res, SDFError):
                return _res.extend("damping")
            _damping = _res
        _c_tmp = el.find("enable_wind")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("enable_wind")
            _enable_wind = _val
        else:
            _enable_wind = None
        if _enable_wind is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.12)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _gravity = str(el.get("gravity", True)).strip().lower() == 'true'
        if isinstance(_gravity, SDFError):
            return _gravity.extend("@gravity")
        _c_inertial = el.find("inertial")
        if _c_inertial is not None:
            _res = Inertial._from_sdf(_c_inertial, version)
            if isinstance(_res, SDFError):
                return _res.extend("inertial")
            _inertial = _res
        else:
            _inertial = None
        _kinematic = str(el.get("kinematic", False)).strip().lower() == 'true'
        if isinstance(_kinematic, SDFError):
            return _kinematic.extend("@kinematic")
        _lights = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _lights.append(_res)
        if _lights and cmp_version(version, "1.12") < 0:
            return SDFError(f"'lights' is not supported in SDF version {version} (added in 1.12)")
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
        _particle_emitters = []
        for c in el.findall("particle_emitter"):
            _res = ParticleEmitter._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("particle_emitter")
            _particle_emitters.append(_res)
        if _particle_emitters and cmp_version(version, "1.12") < 0:
            return SDFError(f"'particle_emitters' is not supported in SDF version {version} (added in 1.12)")
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
        _self_collide = str(el.get("self_collide", False)).strip().lower() == 'true'
        if isinstance(_self_collide, SDFError):
            return _self_collide.extend("@self_collide")
        _c_sensor = el.find("sensor")
        if _c_sensor is not None:
            _res = Sensor._from_sdf(_c_sensor, version)
            if isinstance(_res, SDFError):
                return _res.extend("sensor")
            _sensor = _res
        else:
            _sensor = None
        _c_tmp = el.find("velocity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _SDFPose._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("velocity")
            _velocity = _val
        else:
            _velocity = None
        if _velocity is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'velocity' is not supported in SDF version {version} (added in 1.5)")
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
        _c_tmp = el.find("wrench")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _SDFPose._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("wrench")
            _wrench = _val
        else:
            _wrench = None
        if _wrench is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'wrench' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, acceleration=_acceleration, audio_sinks=_audio_sinks, audio_sources=_audio_sources, batterys=_batterys, collisions=_collisions, damping=_damping, enable_wind=_enable_wind, frames=_frames, gravity=_gravity, inertial=_inertial, kinematic=_kinematic, lights=_lights, must_be_base_link=_must_be_base_link, name=_name, origin=_origin, particle_emitters=_particle_emitters, pose=_pose, projector=_projector, self_collide=_self_collide, sensor=_sensor, velocity=_velocity, velocity_decay=_velocity_decay, visuals=_visuals, wrench=_wrench)
