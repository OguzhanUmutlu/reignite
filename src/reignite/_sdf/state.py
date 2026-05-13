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



class State(BaseModel):
    class Deletions(BaseModel):
        def __init__(self, sdf_version: str | None = None, names: List[str] = None):
            super().__init__(sdf_version)
            self.names = names or []

        def add_name(self, *items: str):
            if self.names is None:
                self.names = []
            self.names.extend(items)

        def to_version(self, target_version: str) -> "State.Deletions":
            kwargs = {"sdf_version": target_version}
            kwargs["names"] = self.names
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("deletions")
            for _v in (self.names or []):
                _c_tmp = ET.Element("name")
                _c_tmp.text = _v
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "State.Deletions | SDFError":
            _names = []
            for c in el.findall("name"):
                _text = c.text if c.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("name")
                _names.append(_val)
            return cls(sdf_version=version, names=_names)

    class Insertions(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            joints: List["Joint"] = None,
            lights: List["Light"] = None,
            models: List["Model"] = None
        ):
            super().__init__(sdf_version)
            self.joints = joints or []
            self.lights = lights or []
            self.models = models or []
            for _i, _c in enumerate(self.joints):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, '__version__', None) is None:
                    _c.__version__ = self.__version__
                elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.joints[_i] = _c.to_version(self.__version__)
            for _i, _c in enumerate(self.lights):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, '__version__', None) is None:
                    _c.__version__ = self.__version__
                elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.lights[_i] = _c.to_version(self.__version__)
            for _i, _c in enumerate(self.models):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, '__version__', None) is None:
                    _c.__version__ = self.__version__
                elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.models[_i] = _c.to_version(self.__version__)

        def add_joint(self, *items: "Joint"):
            if self.joints is None:
                self.joints = []
            self.joints.extend(items)

        def add_light(self, *items: "Light"):
            if self.lights is None:
                self.lights = []
            self.lights.extend(items)

        def add_model(self, *items: "Model"):
            if self.models is None:
                self.models = []
            self.models.extend(items)

        def to_version(self, target_version: str) -> "State.Insertions":
            from ..elements.joint import Joint
            from ..elements.light import Light
            from ..elements.model import Model
            if self.joints is not None and cmp_version(target_version, "1.12") < 0:
                raise ValueError(f"'joints' is not supported in SDF version {target_version} (added in 1.12)")
            if self.lights is not None and cmp_version(target_version, "1.6") < 0:
                raise ValueError(f"'lights' is not supported in SDF version {target_version} (added in 1.6)")
            kwargs = {"sdf_version": target_version}
            kwargs["joints"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joints or [])]
            kwargs["lights"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.lights or [])]
            kwargs["models"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])]
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
                if hasattr(item, 'to_sdf'):
                    _child_res = item.to_sdf(version)
                else:
                    _child_res = str(item)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('joint')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
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
            for item in (self.models or []):
                if hasattr(item, 'to_sdf'):
                    _child_res = item.to_sdf(version)
                else:
                    _child_res = str(item)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('model')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "State.Insertions | SDFError":
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

    def __init__(
        self,
        sdf_version: str | None = None,
        deletions: "State.Deletions" = None,
        insertions: "State.Insertions" = None,
        iterations: int = 0,
        joint_states: List["JointState"] = None,
        light_states: List["LightState"] = None,
        lights: List["Light"] = None,
        model_states: List["ModelState"] = None,
        models: List["Model"] = None,
        real_time: float = "0 0",
        sim_time: float = "0 0",
        time: float = "0 0",
        wall_time: float = "0 0",
        world_name: str = "__default__"
    ):
        super().__init__(sdf_version)
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
        if self.deletions is not None and hasattr(self.deletions, 'to_version'):
            if getattr(self.deletions, '__version__', None) is None:
                self.deletions.__version__ = self.__version__
            elif getattr(self.deletions, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.deletions = self.deletions.to_version(self.__version__)
        if self.insertions is not None and hasattr(self.insertions, 'to_version'):
            if getattr(self.insertions, '__version__', None) is None:
                self.insertions.__version__ = self.__version__
            elif getattr(self.insertions, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.insertions = self.insertions.to_version(self.__version__)
        for _i, _c in enumerate(self.joint_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.joint_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.light_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.light_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.lights):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.lights[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.model_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.model_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.models):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.models[_i] = _c.to_version(self.__version__)

    def add_joint_state(self, *items: "JointState"):
        if self.joint_states is None:
            self.joint_states = []
        self.joint_states.extend(items)

    def add_light_state(self, *items: "LightState"):
        if self.light_states is None:
            self.light_states = []
        self.light_states.extend(items)

    def add_light(self, *items: "Light"):
        if self.lights is None:
            self.lights = []
        self.lights.extend(items)

    def add_model_state(self, *items: "ModelState"):
        if self.model_states is None:
            self.model_states = []
        self.model_states.extend(items)

    def add_model(self, *items: "Model"):
        if self.models is None:
            self.models = []
        self.models.extend(items)

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
        kwargs["deletions"] = self.deletions.to_version(target_version) if hasattr(self.deletions, "to_version") else self.deletions
        kwargs["insertions"] = self.insertions.to_version(target_version) if hasattr(self.insertions, "to_version") else self.insertions
        kwargs["iterations"] = self.iterations
        kwargs["joint_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joint_states or [])]
        kwargs["light_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.light_states or [])]
        kwargs["lights"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.lights or [])]
        kwargs["model_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.model_states or [])]
        kwargs["models"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])]
        kwargs["real_time"] = self.real_time
        kwargs["sim_time"] = self.sim_time
        kwargs["time"] = self.time
        kwargs["wall_time"] = self.wall_time
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
            if hasattr(self.deletions, 'to_sdf'):
                _child_res = self.deletions.to_sdf(version)
            else:
                _child_res = str(self.deletions)
            if isinstance(_child_res, str):
                _item_el = ET.Element('deletions')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.insertions is not None:
            if hasattr(self.insertions, 'to_sdf'):
                _child_res = self.insertions.to_sdf(version)
            else:
                _child_res = str(self.insertions)
            if isinstance(_child_res, str):
                _item_el = ET.Element('insertions')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.iterations is not None:
            _c_tmp = ET.Element("iterations")
            _c_tmp.text = str(self.iterations)
            el.append(_c_tmp)
        for item in (self.joint_states or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('joint_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.light_states or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('light_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
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
        for item in (self.model_states or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('model_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.models or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('model')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.real_time is not None:
            _c_tmp = ET.Element("real_time")
            _c_tmp.text = str(self.real_time)
            el.append(_c_tmp)
        if self.sim_time is not None:
            _c_tmp = ET.Element("sim_time")
            _c_tmp.text = str(self.sim_time)
            el.append(_c_tmp)
        if self.time is not None:
            el.set("time", str(self.time))
        if self.wall_time is not None:
            _c_tmp = ET.Element("wall_time")
            _c_tmp.text = str(self.wall_time)
            el.append(_c_tmp)
        if self.world_name is not None:
            el.set("world_name", self.world_name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "State | SDFError":
        from ..elements.joint_state import JointState
        from ..elements.light_state import LightState
        from ..elements.light import Light
        from ..elements.model_state import ModelState
        from ..elements.model import Model
        _c_deletions = el.find("deletions")
        if _c_deletions is not None:
            _res = cls.Deletions._from_sdf(_c_deletions, version)
            if isinstance(_res, SDFError):
                return _res.extend("deletions")
            _deletions = _res
        else:
            _deletions = None
        if _deletions is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'deletions' is not supported in SDF version {version} (added in 1.3)")
        _c_insertions = el.find("insertions")
        if _c_insertions is not None:
            _res = cls.Insertions._from_sdf(_c_insertions, version)
            if isinstance(_res, SDFError):
                return _res.extend("insertions")
            _insertions = _res
        else:
            _insertions = None
        if _insertions is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'insertions' is not supported in SDF version {version} (added in 1.3)")
        _c_tmp = el.find("iterations")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_uint32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("iterations")
            _iterations = _val
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
        _c_tmp = el.find("real_time")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0"
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("real_time")
            _real_time = _val
        else:
            _real_time = None
        if _real_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'real_time' is not supported in SDF version {version} (added in 1.3)")
        _c_tmp = el.find("sim_time")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0"
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("sim_time")
            _sim_time = _val
        else:
            _sim_time = None
        if _sim_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'sim_time' is not supported in SDF version {version} (added in 1.3)")
        _time = _parse_double(el.get("time", "0 0"))
        if isinstance(_time, SDFError):
            return _time.extend("@time")
        _c_tmp = el.find("wall_time")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0"
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("wall_time")
            _wall_time = _val
        else:
            _wall_time = None
        if _wall_time is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'wall_time' is not supported in SDF version {version} (added in 1.3)")
        _world_name = el.get("world_name", "__default__")
        if isinstance(_world_name, SDFError):
            return _world_name.extend("@world_name")
        return cls(sdf_version=version, deletions=_deletions, insertions=_insertions, iterations=_iterations, joint_states=_joint_states, light_states=_light_states, lights=_lights, model_states=_model_states, models=_models, real_time=_real_time, sim_time=_sim_time, time=_time, wall_time=_wall_time, world_name=_world_name)
