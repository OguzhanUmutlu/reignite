### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.joint import Joint
    from ..elements.joint_state import JointState
    from ..elements.light import Light
    from ..elements.light_state import LightState
    from ..elements.model import Model
    from ..elements.model_state import ModelState


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



class Deletions(BaseModel):
    def __init__(self, sdf_version: str | None = None, names: List["Name"] = None):
        self.__version__ = sdf_version
        self.names = names or []
        for _i, _c in enumerate(self.names):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.names[_i] = _c.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Deletions":
        kwargs = {"sdf_version": target_version}
        kwargs["names"] = [c.to_version(target_version) for c in (self.names or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("deletions")
        for item in (self.names or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _names = []
        for c in el.findall("name"):
            _res = Name._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _names.append(_res)
        return cls(sdf_version=version, names=_names)


class Insertions(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        joints: List["Joint"] = None,
        lights: List["Light"] = None,
        models: List["Model"] = None
    ):
        self.__version__ = sdf_version
        self.joints = joints or []
        self.lights = lights or []
        self.models = models or []
        for _i, _c in enumerate(self.joints):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.joints[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.lights):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.lights[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.models):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.models[_i] = _c.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Insertions":
        from ..elements.joint import Joint
        from ..elements.light import Light
        from ..elements.model import Model
        if self.joints is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'joints' is not supported in SDF version {target_version} (added in 1.12)")
        if self.lights is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'lights' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["joints"] = [c.to_version(target_version) for c in (self.joints or [])]
        kwargs["lights"] = [c.to_version(target_version) for c in (self.lights or [])]
        kwargs["models"] = [c.to_version(target_version) for c in (self.models or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.joint import Joint
        from ..elements.light import Light
        from ..elements.model import Model
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("insertions")
        for item in (self.joints or []):
            el.append(item.to_sdf(version))
        for item in (self.lights or []):
            el.append(item.to_sdf(version))
        for item in (self.models or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.joint import Joint
        from ..elements.light import Light
        from ..elements.model import Model
        _joints = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joints.append(_res)
        if _joints and cmp_version(version, "1.12") < 0:
            return SDFError(f"'joints' is not supported in SDF version {version} (added in 1.12)")
        _lights = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _lights.append(_res)
        if _lights and cmp_version(version, "1.6") < 0:
            return SDFError(f"'lights' is not supported in SDF version {version} (added in 1.6)")
        _models = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _models.append(_res)
        return cls(sdf_version=version, joints=_joints, lights=_lights, models=_models)


class Iterations(BaseModel):
    def __init__(self, sdf_version: str | None = None, iterations: int = 0):
        self.__version__ = sdf_version
        self.iterations = iterations

    def to_version(self, target_version: str) -> "Iterations":
        if self.iterations is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'iterations' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["iterations"] = self.iterations
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("iterations")
        if self.iterations is not None:
            el.text = str(self.iterations)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _iterations = _parse_uint32(_text)
        if isinstance(_iterations, SDFError):
            return _iterations
        if _iterations is not None and cmp_version(version, "1.5") < 0:
            if _iterations != 0:
                return SDFError(f"'iterations' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, iterations=_iterations)


class Name(BaseModel):
    def __init__(self, sdf_version: str | None = None, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "Name":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _name = _text
        if isinstance(_name, SDFError):
            return _name
        return cls(sdf_version=version, name=_name)


class RealTime(BaseModel):
    def __init__(self, sdf_version: str | None = None, real_time: float = "0 0"):
        self.__version__ = sdf_version
        self.real_time = real_time

    def to_version(self, target_version: str) -> "RealTime":
        if self.real_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'real_time' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["real_time"] = self.real_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("real_time")
        if self.real_time is not None:
            el.text = str(self.real_time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _real_time = _parse_double(_text)
        if isinstance(_real_time, SDFError):
            return _real_time
        if _real_time is not None and cmp_version(version, "1.3") < 0:
            if _real_time != "0 0":
                return SDFError(f"'real_time' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, real_time=_real_time)


class SimTime(BaseModel):
    def __init__(self, sdf_version: str | None = None, sim_time: float = "0 0"):
        self.__version__ = sdf_version
        self.sim_time = sim_time

    def to_version(self, target_version: str) -> "SimTime":
        if self.sim_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'sim_time' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["sim_time"] = self.sim_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("sim_time")
        if self.sim_time is not None:
            el.text = str(self.sim_time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _sim_time = _parse_double(_text)
        if isinstance(_sim_time, SDFError):
            return _sim_time
        if _sim_time is not None and cmp_version(version, "1.3") < 0:
            if _sim_time != "0 0":
                return SDFError(f"'sim_time' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, sim_time=_sim_time)


class State(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        deletions: "Deletions" = None,
        insertions: "Insertions" = None,
        iterations: "Iterations" = None,
        joint_states: List["JointState"] = None,
        light_states: List["LightState"] = None,
        lights: List["Light"] = None,
        model_states: List["ModelState"] = None,
        models: List["Model"] = None,
        real_time: "RealTime" = None,
        sim_time: "SimTime" = None,
        time: float = "0 0",
        wall_time: "WallTime" = None,
        world_name: str = "__default__"
    ):
        self.__version__ = sdf_version
        self.deletions = deletions
        self.insertions = insertions
        self.iterations = iterations
        self.joint_states = joint_states or []
        self.light_states = light_states or []
        self.lights = lights or []
        self.model_states = model_states or []
        self.models = models or []
        self.real_time = real_time
        self.sim_time = sim_time
        self.time = time
        self.wall_time = wall_time
        self.world_name = world_name
        if self.deletions is not None:
            if getattr(self.deletions, '__version__', None) is None:
                self.deletions.__version__ = self.__version__
            elif getattr(self.deletions, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.deletions = self.deletions.to_version(self.__version__)
        if self.insertions is not None:
            if getattr(self.insertions, '__version__', None) is None:
                self.insertions.__version__ = self.__version__
            elif getattr(self.insertions, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.insertions = self.insertions.to_version(self.__version__)
        if self.iterations is not None:
            if getattr(self.iterations, '__version__', None) is None:
                self.iterations.__version__ = self.__version__
            elif getattr(self.iterations, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.iterations = self.iterations.to_version(self.__version__)
        for _i, _c in enumerate(self.joint_states):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.joint_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.light_states):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.light_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.lights):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.lights[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.model_states):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.model_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.models):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.models[_i] = _c.to_version(self.__version__)
        if self.real_time is not None:
            if getattr(self.real_time, '__version__', None) is None:
                self.real_time.__version__ = self.__version__
            elif getattr(self.real_time, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.real_time = self.real_time.to_version(self.__version__)
        if self.sim_time is not None:
            if getattr(self.sim_time, '__version__', None) is None:
                self.sim_time.__version__ = self.__version__
            elif getattr(self.sim_time, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.sim_time = self.sim_time.to_version(self.__version__)
        if self.wall_time is not None:
            if getattr(self.wall_time, '__version__', None) is None:
                self.wall_time.__version__ = self.__version__
            elif getattr(self.wall_time, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.wall_time = self.wall_time.to_version(self.__version__)

    def to_version(self, target_version: str) -> "State":
        from ..elements.joint_state import JointState
        from ..elements.light_state import LightState
        from ..elements.light import Light
        from ..elements.model_state import ModelState
        from ..elements.model import Model
        if self.deletions is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'deletions' is not supported in SDF version {target_version} (added in 1.3)")
        if self.insertions is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'insertions' is not supported in SDF version {target_version} (added in 1.3)")
        if self.iterations is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'iterations' is not supported in SDF version {target_version} (added in 1.5)")
        if self.joint_states is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'joint_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.light_states is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'light_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.lights is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'lights' is not supported in SDF version {target_version} (added in 1.5)")
        if self.lights is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'lights' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.model_states is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.models is not None and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'models' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.real_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'real_time' is not supported in SDF version {target_version} (added in 1.3)")
        if self.sim_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'sim_time' is not supported in SDF version {target_version} (added in 1.3)")
        if self.time is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'time' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.wall_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'wall_time' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["deletions"] = self.deletions.to_version(target_version) if self.deletions is not None else None
        kwargs["insertions"] = self.insertions.to_version(target_version) if self.insertions is not None else None
        kwargs["iterations"] = self.iterations.to_version(target_version) if self.iterations is not None else None
        kwargs["joint_states"] = [c.to_version(target_version) for c in (self.joint_states or [])]
        kwargs["light_states"] = [c.to_version(target_version) for c in (self.light_states or [])]
        kwargs["lights"] = [c.to_version(target_version) for c in (self.lights or [])]
        kwargs["model_states"] = [c.to_version(target_version) for c in (self.model_states or [])]
        kwargs["models"] = [c.to_version(target_version) for c in (self.models or [])]
        kwargs["real_time"] = self.real_time.to_version(target_version) if self.real_time is not None else None
        kwargs["sim_time"] = self.sim_time.to_version(target_version) if self.sim_time is not None else None
        kwargs["time"] = self.time
        kwargs["wall_time"] = self.wall_time.to_version(target_version) if self.wall_time is not None else None
        kwargs["world_name"] = self.world_name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.joint_state import JointState
        from ..elements.light_state import LightState
        from ..elements.light import Light
        from ..elements.model_state import ModelState
        from ..elements.model import Model
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("state")
        if self.deletions is not None:
            el.append(self.deletions.to_sdf(version))
        if self.insertions is not None:
            el.append(self.insertions.to_sdf(version))
        if self.iterations is not None:
            el.append(self.iterations.to_sdf(version))
        for item in (self.joint_states or []):
            el.append(item.to_sdf(version))
        for item in (self.light_states or []):
            el.append(item.to_sdf(version))
        for item in (self.lights or []):
            el.append(item.to_sdf(version))
        for item in (self.model_states or []):
            el.append(item.to_sdf(version))
        for item in (self.models or []):
            el.append(item.to_sdf(version))
        if self.real_time is not None:
            el.append(self.real_time.to_sdf(version))
        if self.sim_time is not None:
            el.append(self.sim_time.to_sdf(version))
        if self.time is not None:
            el.set("time", str(self.time))
        if self.wall_time is not None:
            el.append(self.wall_time.to_sdf(version))
        if self.world_name is not None:
            el.set("world_name", self.world_name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.joint_state import JointState
        from ..elements.light_state import LightState
        from ..elements.light import Light
        from ..elements.model_state import ModelState
        from ..elements.model import Model
        _c_deletions = el.find("deletions")
        if _c_deletions is not None:
            _res = Deletions._from_sdf(_c_deletions, version)
            if isinstance(_res, SDFError):
                return _res.extend("deletions")
            _deletions = _res
        else:
            _deletions = None
        if _deletions is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'deletions' is not supported in SDF version {version} (added in 1.3)")
        _c_insertions = el.find("insertions")
        if _c_insertions is not None:
            _res = Insertions._from_sdf(_c_insertions, version)
            if isinstance(_res, SDFError):
                return _res.extend("insertions")
            _insertions = _res
        else:
            _insertions = None
        if _insertions is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'insertions' is not supported in SDF version {version} (added in 1.3)")
        _c_iterations = el.find("iterations")
        if _c_iterations is not None:
            _res = Iterations._from_sdf(_c_iterations, version)
            if isinstance(_res, SDFError):
                return _res.extend("iterations")
            _iterations = _res
        else:
            _iterations = None
        if _iterations is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'iterations' is not supported in SDF version {version} (added in 1.5)")
        _joint_states = []
        for c in el.findall("joint_state"):
            _res = JointState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint_state")
            _joint_states.append(_res)
        if _joint_states and cmp_version(version, "1.12") < 0:
            return SDFError(f"'joint_states' is not supported in SDF version {version} (added in 1.12)")
        _light_states = []
        for c in el.findall("light_state"):
            _res = LightState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_state")
            _light_states.append(_res)
        if _light_states and cmp_version(version, "1.12") < 0:
            return SDFError(f"'light_states' is not supported in SDF version {version} (added in 1.12)")
        _lights = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _lights.append(_res)
        if _lights and cmp_version(version, "1.5") < 0:
            return SDFError(f"'lights' is not supported in SDF version {version} (added in 1.5)")
        _model_states = []
        for c in el.findall("model_state"):
            _res = ModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_state")
            _model_states.append(_res)
        if _model_states and cmp_version(version, "1.12") < 0:
            return SDFError(f"'model_states' is not supported in SDF version {version} (added in 1.12)")
        _models = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _models.append(_res)
        _c_real_time = el.find("real_time")
        if _c_real_time is not None:
            _res = RealTime._from_sdf(_c_real_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("real_time")
            _real_time = _res
        else:
            _real_time = None
        if _real_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'real_time' is not supported in SDF version {version} (added in 1.3)")
        _c_sim_time = el.find("sim_time")
        if _c_sim_time is not None:
            _res = SimTime._from_sdf(_c_sim_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("sim_time")
            _sim_time = _res
        else:
            _sim_time = None
        if _sim_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'sim_time' is not supported in SDF version {version} (added in 1.3)")
        _time = _parse_double(el.get("time", "0 0"))
        if isinstance(_time, SDFError):
            return _time.extend("@time")
        _c_wall_time = el.find("wall_time")
        if _c_wall_time is not None:
            _res = WallTime._from_sdf(_c_wall_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("wall_time")
            _wall_time = _res
        else:
            _wall_time = None
        if _wall_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'wall_time' is not supported in SDF version {version} (added in 1.3)")
        _world_name = el.get("world_name", "__default__")
        if isinstance(_world_name, SDFError):
            return _world_name.extend("@world_name")
        return cls(sdf_version=version, deletions=_deletions, insertions=_insertions, iterations=_iterations, joint_states=_joint_states, light_states=_light_states, lights=_lights, model_states=_model_states, models=_models, real_time=_real_time, sim_time=_sim_time, time=_time, wall_time=_wall_time, world_name=_world_name)


class Time(BaseModel):
    def __init__(self, sdf_version: str | None = None, time: float = "0 0"):
        self.__version__ = sdf_version
        self.time = time

    def to_version(self, target_version: str) -> "Time":
        if self.time is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'time' is not supported in SDF version {target_version} (added in 1.2)")
        if self.time is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'time' is not supported in SDF version {target_version} (removed in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["time"] = self.time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("time")
        if self.time is not None:
            el.text = str(self.time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _time = _parse_double(_text)
        if isinstance(_time, SDFError):
            return _time
        if _time is not None and cmp_version(version, "1.2") < 0:
            if _time != "0 0":
                return SDFError(f"'time' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, time=_time)


class WallTime(BaseModel):
    def __init__(self, sdf_version: str | None = None, wall_time: float = "0 0"):
        self.__version__ = sdf_version
        self.wall_time = wall_time

    def to_version(self, target_version: str) -> "WallTime":
        if self.wall_time is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'wall_time' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["wall_time"] = self.wall_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("wall_time")
        if self.wall_time is not None:
            el.text = str(self.wall_time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _wall_time = _parse_double(_text)
        if isinstance(_wall_time, SDFError):
            return _wall_time
        if _wall_time is not None and cmp_version(version, "1.3") < 0:
            if _wall_time != "0 0":
                return SDFError(f"'wall_time' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, wall_time=_wall_time)
