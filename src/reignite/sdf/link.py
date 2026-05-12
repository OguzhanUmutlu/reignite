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



class Acceleration(BaseModel):
    def __init__(self, sdf_version: str | None = None, acceleration: _SDFPose = None):
        self.__version__ = sdf_version
        if acceleration is None:
            acceleration = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        self.acceleration = acceleration

    def to_version(self, target_version: str) -> "Acceleration":
        if self.acceleration is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {target_version} (added in 1.5)")
        if self.acceleration is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {target_version} (removed in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["acceleration"] = self.acceleration
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("acceleration")
        if self.acceleration is not None:
            el.text = self.acceleration.to_sdf(version)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _acceleration = _SDFPose._from_sdf(_text, version)
        if isinstance(_acceleration, SDFError):
            return _acceleration
        if _acceleration is not None and cmp_version(version, "1.5") < 0:
            if _acceleration != "0 0 0 0 0 0":
                return SDFError(f"'acceleration' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, acceleration=_acceleration)


class Angular(BaseModel):
    def __init__(self, sdf_version: str | None = None, angular: float = 0.0):
        self.__version__ = sdf_version
        self.angular = angular

    def to_version(self, target_version: str) -> "Angular":
        kwargs = {"sdf_version": target_version}
        kwargs["angular"] = self.angular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("angular")
        if self.angular is not None:
            el.text = str(self.angular)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _angular = _parse_double(_text)
        if isinstance(_angular, SDFError):
            return _angular
        return cls(sdf_version=version, angular=_angular)


class Damping(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        angular: "Angular" = None,
        linear: "Linear" = None
    ):
        self.__version__ = sdf_version
        self.angular = angular
        self.linear = linear
        if self.angular is not None:
            if getattr(self.angular, '__version__', None) is None:
                self.angular.__version__ = self.__version__
            elif getattr(self.angular, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.angular = self.angular.to_version(self.__version__)
        if self.linear is not None:
            if getattr(self.linear, '__version__', None) is None:
                self.linear.__version__ = self.__version__
            elif getattr(self.linear, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.linear = self.linear.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Damping":
        kwargs = {"sdf_version": target_version}
        kwargs["angular"] = self.angular.to_version(target_version) if self.angular is not None else None
        kwargs["linear"] = self.linear.to_version(target_version) if self.linear is not None else None
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
            el.append(self.angular.to_sdf(version))
        if self.linear is not None:
            el.append(self.linear.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_angular = el.find("angular")
        if _c_angular is not None:
            _res = Angular._from_sdf(_c_angular, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular")
            _angular = _res
        else:
            _angular = None
        _c_linear = el.find("linear")
        if _c_linear is not None:
            _res = Linear._from_sdf(_c_linear, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear")
            _linear = _res
        else:
            _linear = None
        return cls(sdf_version=version, angular=_angular, linear=_linear)


class EnableWind(BaseModel):
    def __init__(self, sdf_version: str | None = None, enable_wind: bool = False):
        self.__version__ = sdf_version
        self.enable_wind = enable_wind

    def to_version(self, target_version: str) -> "EnableWind":
        if self.enable_wind is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_wind"] = self.enable_wind
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("enable_wind")
        if self.enable_wind is not None:
            el.text = str(self.enable_wind).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _enable_wind = str(_text).strip().lower() == 'true'
        if isinstance(_enable_wind, SDFError):
            return _enable_wind
        if _enable_wind is not None and cmp_version(version, "1.12") < 0:
            if _enable_wind != False:
                return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, enable_wind=_enable_wind)


class Gravity(BaseModel):
    def __init__(self, sdf_version: str | None = None, gravity: bool = True):
        self.__version__ = sdf_version
        self.gravity = gravity

    def to_version(self, target_version: str) -> "Gravity":
        if self.gravity is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'gravity' is not supported in SDF version {target_version} (added in 1.2)")
        if self.gravity is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'gravity' is not supported in SDF version {target_version} (removed in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["gravity"] = self.gravity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("gravity")
        if self.gravity is not None:
            el.text = str(self.gravity).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _gravity = str(_text).strip().lower() == 'true'
        if isinstance(_gravity, SDFError):
            return _gravity
        if _gravity is not None and cmp_version(version, "1.2") < 0:
            if _gravity != True:
                return SDFError(f"'gravity' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, gravity=_gravity)


class Kinematic(BaseModel):
    def __init__(self, sdf_version: str | None = None, kinematic: bool = False):
        self.__version__ = sdf_version
        self.kinematic = kinematic

    def to_version(self, target_version: str) -> "Kinematic":
        if self.kinematic is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'kinematic' is not supported in SDF version {target_version} (added in 1.2)")
        if self.kinematic is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'kinematic' is not supported in SDF version {target_version} (removed in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["kinematic"] = self.kinematic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("kinematic")
        if self.kinematic is not None:
            el.text = str(self.kinematic).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _kinematic = str(_text).strip().lower() == 'true'
        if isinstance(_kinematic, SDFError):
            return _kinematic
        if _kinematic is not None and cmp_version(version, "1.2") < 0:
            if _kinematic != False:
                return SDFError(f"'kinematic' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, kinematic=_kinematic)


class Linear(BaseModel):
    def __init__(self, sdf_version: str | None = None, linear: float = 0.0):
        self.__version__ = sdf_version
        self.linear = linear

    def to_version(self, target_version: str) -> "Linear":
        kwargs = {"sdf_version": target_version}
        kwargs["linear"] = self.linear
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("linear")
        if self.linear is not None:
            el.text = str(self.linear)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _linear = _parse_double(_text)
        if isinstance(_linear, SDFError):
            return _linear
        return cls(sdf_version=version, linear=_linear)


class Link(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        acceleration: "Acceleration" = None,
        audio_sinks: List["AudioSink"] = None,
        audio_sources: List["AudioSource"] = None,
        batterys: List["Battery"] = None,
        collisions: List["Collision"] = None,
        damping: "Damping" = None,
        enable_wind: "EnableWind" = None,
        frames: List["Frame"] = None,
        gravity: bool = True,
        inertial: "Inertial" = None,
        kinematic: bool = False,
        lights: List["Light"] = None,
        must_be_base_link: "MustBeBaseLink" = None,
        name: str = "__default__",
        origin: "Origin" = None,
        particle_emitters: List["ParticleEmitter"] = None,
        pose: "Pose" = None,
        projector: "Projector" = None,
        self_collide: bool = False,
        sensor: "Sensor" = None,
        velocity: "Velocity" = None,
        velocity_decay: "VelocityDecay" = None,
        visuals: List["Visual"] = None,
        wrench: "Wrench" = None
    ):
        self.__version__ = sdf_version
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
        if self.acceleration is not None:
            if getattr(self.acceleration, '__version__', None) is None:
                self.acceleration.__version__ = self.__version__
            elif getattr(self.acceleration, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.acceleration = self.acceleration.to_version(self.__version__)
        for _i, _c in enumerate(self.audio_sinks):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.audio_sinks[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.audio_sources):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.audio_sources[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.batterys):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.batterys[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.collisions):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.collisions[_i] = _c.to_version(self.__version__)
        if self.damping is not None:
            if getattr(self.damping, '__version__', None) is None:
                self.damping.__version__ = self.__version__
            elif getattr(self.damping, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.damping = self.damping.to_version(self.__version__)
        if self.enable_wind is not None:
            if getattr(self.enable_wind, '__version__', None) is None:
                self.enable_wind.__version__ = self.__version__
            elif getattr(self.enable_wind, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.enable_wind = self.enable_wind.to_version(self.__version__)
        for _i, _c in enumerate(self.frames):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        if self.inertial is not None:
            if getattr(self.inertial, '__version__', None) is None:
                self.inertial.__version__ = self.__version__
            elif getattr(self.inertial, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.inertial = self.inertial.to_version(self.__version__)
        for _i, _c in enumerate(self.lights):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.lights[_i] = _c.to_version(self.__version__)
        if self.must_be_base_link is not None:
            if getattr(self.must_be_base_link, '__version__', None) is None:
                self.must_be_base_link.__version__ = self.__version__
            elif getattr(self.must_be_base_link, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.must_be_base_link = self.must_be_base_link.to_version(self.__version__)
        if self.origin is not None:
            if getattr(self.origin, '__version__', None) is None:
                self.origin.__version__ = self.__version__
            elif getattr(self.origin, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.origin = self.origin.to_version(self.__version__)
        for _i, _c in enumerate(self.particle_emitters):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.particle_emitters[_i] = _c.to_version(self.__version__)
        if self.pose is not None:
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)
        if self.projector is not None:
            if getattr(self.projector, '__version__', None) is None:
                self.projector.__version__ = self.__version__
            elif getattr(self.projector, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.projector = self.projector.to_version(self.__version__)
        if self.sensor is not None:
            if getattr(self.sensor, '__version__', None) is None:
                self.sensor.__version__ = self.__version__
            elif getattr(self.sensor, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.sensor = self.sensor.to_version(self.__version__)
        if self.velocity is not None:
            if getattr(self.velocity, '__version__', None) is None:
                self.velocity.__version__ = self.__version__
            elif getattr(self.velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.velocity = self.velocity.to_version(self.__version__)
        if self.velocity_decay is not None:
            if getattr(self.velocity_decay, '__version__', None) is None:
                self.velocity_decay.__version__ = self.__version__
            elif getattr(self.velocity_decay, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.velocity_decay = self.velocity_decay.to_version(self.__version__)
        for _i, _c in enumerate(self.visuals):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.visuals[_i] = _c.to_version(self.__version__)
        if self.wrench is not None:
            if getattr(self.wrench, '__version__', None) is None:
                self.wrench.__version__ = self.__version__
            elif getattr(self.wrench, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.wrench = self.wrench.to_version(self.__version__)

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
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["audio_sinks"] = [c.to_version(target_version) for c in (self.audio_sinks or [])]
        kwargs["audio_sources"] = [c.to_version(target_version) for c in (self.audio_sources or [])]
        kwargs["batterys"] = [c.to_version(target_version) for c in (self.batterys or [])]
        kwargs["collisions"] = [c.to_version(target_version) for c in (self.collisions or [])]
        kwargs["damping"] = self.damping.to_version(target_version) if self.damping is not None else None
        kwargs["enable_wind"] = self.enable_wind.to_version(target_version) if self.enable_wind is not None else None
        kwargs["frames"] = [c.to_version(target_version) for c in (self.frames or [])]
        kwargs["gravity"] = self.gravity
        kwargs["inertial"] = self.inertial.to_version(target_version) if self.inertial is not None else None
        kwargs["kinematic"] = self.kinematic
        kwargs["lights"] = [c.to_version(target_version) for c in (self.lights or [])]
        kwargs["must_be_base_link"] = self.must_be_base_link.to_version(target_version) if self.must_be_base_link is not None else None
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["particle_emitters"] = [c.to_version(target_version) for c in (self.particle_emitters or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["projector"] = self.projector.to_version(target_version) if self.projector is not None else None
        kwargs["self_collide"] = self.self_collide
        kwargs["sensor"] = self.sensor.to_version(target_version) if self.sensor is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["velocity_decay"] = self.velocity_decay.to_version(target_version) if self.velocity_decay is not None else None
        kwargs["visuals"] = [c.to_version(target_version) for c in (self.visuals or [])]
        kwargs["wrench"] = self.wrench.to_version(target_version) if self.wrench is not None else None
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
            el.append(self.acceleration.to_sdf(version))
        for item in (self.audio_sinks or []):
            el.append(item.to_sdf(version))
        for item in (self.audio_sources or []):
            el.append(item.to_sdf(version))
        for item in (self.batterys or []):
            el.append(item.to_sdf(version))
        for item in (self.collisions or []):
            el.append(item.to_sdf(version))
        if cmp_version(version, "1.2") < 0:
            if self.damping is None:
                self.damping = Damping(sdf_version=version)
        if self.damping is not None:
            _item_el = self.damping.to_sdf(version)
            if cmp_version(version, "1.2") >= 0:
                _item_el.tag = "velocity_decay"
            else:
                _item_el.tag = "damping"
            el.append(_item_el)
        if self.enable_wind is not None:
            el.append(self.enable_wind.to_sdf(version))
        for item in (self.frames or []):
            el.append(item.to_sdf(version))
        if self.gravity is not None:
            el.set("gravity", str(self.gravity).lower())
        if self.inertial is not None:
            el.append(self.inertial.to_sdf(version))
        if self.kinematic is not None:
            el.set("kinematic", str(self.kinematic).lower())
        for item in (self.lights or []):
            el.append(item.to_sdf(version))
        if self.must_be_base_link is not None:
            el.append(self.must_be_base_link.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        for item in (self.particle_emitters or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.projector is not None:
            el.append(self.projector.to_sdf(version))
        if self.self_collide is not None:
            el.set("self_collide", str(self.self_collide).lower())
        if self.sensor is not None:
            el.append(self.sensor.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.velocity_decay is not None:
            el.append(self.velocity_decay.to_sdf(version))
        for item in (self.visuals or []):
            el.append(item.to_sdf(version))
        if self.wrench is not None:
            el.append(self.wrench.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        _c_acceleration = el.find("acceleration")
        if _c_acceleration is not None:
            _res = Acceleration._from_sdf(_c_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("acceleration")
            _acceleration = _res
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
            _res = Damping._from_sdf(_c_damping, version)
            if isinstance(_res, SDFError):
                return _res.extend("damping")
            _damping = _res
        else:
            _res = Damping._from_sdf(ET.Element("damping"), version)
            if isinstance(_res, SDFError):
                return _res.extend("damping")
            _damping = _res
        _c_enable_wind = el.find("enable_wind")
        if _c_enable_wind is not None:
            _res = EnableWind._from_sdf(_c_enable_wind, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_wind")
            _enable_wind = _res
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
        _c_must_be_base_link = el.find("must_be_base_link")
        if _c_must_be_base_link is not None:
            _res = MustBeBaseLink._from_sdf(_c_must_be_base_link, version)
            if isinstance(_res, SDFError):
                return _res.extend("must_be_base_link")
            _must_be_base_link = _res
        else:
            _must_be_base_link = None
        if _must_be_base_link is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'must_be_base_link' is not supported in SDF version {version} (added in 1.4)")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = Origin._from_sdf(_c_origin, version)
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
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        if _velocity is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'velocity' is not supported in SDF version {version} (added in 1.5)")
        _c_velocity_decay = el.find("velocity_decay")
        if _c_velocity_decay is not None:
            _res = VelocityDecay._from_sdf(_c_velocity_decay, version)
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
        _c_wrench = el.find("wrench")
        if _c_wrench is not None:
            _res = Wrench._from_sdf(_c_wrench, version)
            if isinstance(_res, SDFError):
                return _res.extend("wrench")
            _wrench = _res
        else:
            _wrench = None
        if _wrench is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'wrench' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, acceleration=_acceleration, audio_sinks=_audio_sinks, audio_sources=_audio_sources, batterys=_batterys, collisions=_collisions, damping=_damping, enable_wind=_enable_wind, frames=_frames, gravity=_gravity, inertial=_inertial, kinematic=_kinematic, lights=_lights, must_be_base_link=_must_be_base_link, name=_name, origin=_origin, particle_emitters=_particle_emitters, pose=_pose, projector=_projector, self_collide=_self_collide, sensor=_sensor, velocity=_velocity, velocity_decay=_velocity_decay, visuals=_visuals, wrench=_wrench)


class MustBeBaseLink(BaseModel):
    def __init__(self, sdf_version: str | None = None, must_be_base_link: bool = False):
        self.__version__ = sdf_version
        self.must_be_base_link = must_be_base_link

    def to_version(self, target_version: str) -> "MustBeBaseLink":
        if self.must_be_base_link is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {target_version} (added in 1.4)")
        if self.must_be_base_link is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {target_version} (removed in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["must_be_base_link"] = self.must_be_base_link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("must_be_base_link")
        if self.must_be_base_link is not None:
            el.text = str(self.must_be_base_link).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _must_be_base_link = str(_text).strip().lower() == 'true'
        if isinstance(_must_be_base_link, SDFError):
            return _must_be_base_link
        if _must_be_base_link is not None and cmp_version(version, "1.4") < 0:
            if _must_be_base_link != False:
                return SDFError(f"'must_be_base_link' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, must_be_base_link=_must_be_base_link)


class Origin(BaseModel):
    def __init__(self, sdf_version: str | None = None, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        self.pose = pose

    def to_version(self, target_version: str) -> "Origin":
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
            el.set("pose", self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _pose = _SDFPose._from_sdf(el.get("pose", "0 0 0 0 0 0"), version)
        if isinstance(_pose, SDFError):
            return _pose.extend("@pose")
        return cls(sdf_version=version, pose=_pose)


class SelfCollide(BaseModel):
    def __init__(self, sdf_version: str | None = None, self_collide: bool = False):
        self.__version__ = sdf_version
        self.self_collide = self_collide

    def to_version(self, target_version: str) -> "SelfCollide":
        if self.self_collide is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (added in 1.2)")
        if self.self_collide is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (removed in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["self_collide"] = self.self_collide
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("self_collide")
        if self.self_collide is not None:
            el.text = str(self.self_collide).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _self_collide = str(_text).strip().lower() == 'true'
        if isinstance(_self_collide, SDFError):
            return _self_collide
        if _self_collide is not None and cmp_version(version, "1.2") < 0:
            if _self_collide != False:
                return SDFError(f"'self_collide' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, self_collide=_self_collide)


class Velocity(BaseModel):
    def __init__(self, sdf_version: str | None = None, velocity: _SDFPose = None):
        self.__version__ = sdf_version
        if velocity is None:
            velocity = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Velocity":
        if self.velocity is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (added in 1.5)")
        if self.velocity is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (removed in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["velocity"] = self.velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = self.velocity.to_sdf(version)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _velocity = _SDFPose._from_sdf(_text, version)
        if isinstance(_velocity, SDFError):
            return _velocity
        if _velocity is not None and cmp_version(version, "1.5") < 0:
            if _velocity != "0 0 0 0 0 0":
                return SDFError(f"'velocity' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, velocity=_velocity)


class VelocityDecay(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        angular: "Angular" = None,
        linear: "Linear" = None
    ):
        self.__version__ = sdf_version
        self.angular = angular
        self.linear = linear
        if self.angular is not None:
            if getattr(self.angular, '__version__', None) is None:
                self.angular.__version__ = self.__version__
            elif getattr(self.angular, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.angular = self.angular.to_version(self.__version__)
        if self.linear is not None:
            if getattr(self.linear, '__version__', None) is None:
                self.linear.__version__ = self.__version__
            elif getattr(self.linear, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.linear = self.linear.to_version(self.__version__)

    def to_version(self, target_version: str) -> "VelocityDecay":
        kwargs = {"sdf_version": target_version}
        kwargs["angular"] = self.angular.to_version(target_version) if self.angular is not None else None
        kwargs["linear"] = self.linear.to_version(target_version) if self.linear is not None else None
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
            el.append(self.angular.to_sdf(version))
        if self.linear is not None:
            el.append(self.linear.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_angular = el.find("angular")
        if _c_angular is not None:
            _res = Angular._from_sdf(_c_angular, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular")
            _angular = _res
        else:
            _angular = None
        _c_linear = el.find("linear")
        if _c_linear is not None:
            _res = Linear._from_sdf(_c_linear, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear")
            _linear = _res
        else:
            _linear = None
        return cls(sdf_version=version, angular=_angular, linear=_linear)


class Wrench(BaseModel):
    def __init__(self, sdf_version: str | None = None, wrench: _SDFPose = None):
        self.__version__ = sdf_version
        if wrench is None:
            wrench = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        self.wrench = wrench

    def to_version(self, target_version: str) -> "Wrench":
        if self.wrench is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'wrench' is not supported in SDF version {target_version} (added in 1.5)")
        if self.wrench is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'wrench' is not supported in SDF version {target_version} (removed in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["wrench"] = self.wrench
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("wrench")
        if self.wrench is not None:
            el.text = self.wrench.to_sdf(version)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _wrench = _SDFPose._from_sdf(_text, version)
        if isinstance(_wrench, SDFError):
            return _wrench
        if _wrench is not None and cmp_version(version, "1.5") < 0:
            if _wrench != "0 0 0 0 0 0":
                return SDFError(f"'wrench' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, wrench=_wrench)
