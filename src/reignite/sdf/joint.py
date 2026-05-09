### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations

from .frame import Frame
from .mimic import Mimic
from .pose import Pose
from .sensor import Sensor


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



class Axis(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        dynamics: "Dynamics" = None,
        initial_position: "InitialPosition" = None,
        limit: "Limit" = None,
        mimic: "Mimic" = None,
        use_parent_model_frame: "UseParentModelFrame" = None,
        xyz: _SDFVector3 = None
    ):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = _SDFVector3.from_sdf("0 0 1")
        self.dynamics = dynamics
        self.initial_position = initial_position
        self.limit = limit
        self.mimic = mimic
        self.use_parent_model_frame = use_parent_model_frame
        self.xyz = xyz

    def to_version(self, target_version: str) -> "Axis":
        if self.initial_position is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.6)")
        if self.initial_position is not None and cmp_version(target_version, "1.9") >= 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (removed in 1.9)")
        if self.mimic is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {target_version} (added in 1.11)")
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.xyz is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["initial_position"] = self.initial_position.to_version(target_version) if self.initial_position is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["mimic"] = self.mimic.to_version(target_version) if self.mimic is not None else None
        kwargs["use_parent_model_frame"] = self.use_parent_model_frame.to_version(target_version) if self.use_parent_model_frame is not None else None
        kwargs["xyz"] = self.xyz
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis")
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf(version))
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf(version))
        if self.limit is None:
            self.limit = Limit(sdf_version=version)
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.mimic is not None:
            el.append(self.mimic.to_sdf(version))
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf(version))
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_dynamics = el.find("dynamics")
        if _c_dynamics is not None:
            _res = Dynamics._from_sdf(_c_dynamics, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamics")
            _dynamics = _res
        else:
            _dynamics = None
        _c_initial_position = el.find("initial_position")
        if _c_initial_position is not None:
            _res = InitialPosition._from_sdf(_c_initial_position, version)
            if isinstance(_res, SDFError):
                return _res.extend("initial_position")
            _initial_position = _res
        else:
            _initial_position = None
        if _initial_position is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'initial_position' is not supported in SDF version {version} (added in 1.6)")
        _c_limit = el.find("limit")
        if _c_limit is not None:
            _res = Limit._from_sdf(_c_limit, version)
            if isinstance(_res, SDFError):
                return _res.extend("limit")
            _limit = _res
        else:
            _res = Limit._from_sdf(ET.Element("limit"), version)
            if isinstance(_res, SDFError):
                return _res.extend("limit")
            _limit = _res
        _c_mimic = el.find("mimic")
        if _c_mimic is not None:
            _res = Mimic._from_sdf(_c_mimic, version)
            if isinstance(_res, SDFError):
                return _res.extend("mimic")
            _mimic = _res
        else:
            _mimic = None
        if _mimic is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'mimic' is not supported in SDF version {version} (added in 1.11)")
        _c_use_parent_model_frame = el.find("use_parent_model_frame")
        if _c_use_parent_model_frame is not None:
            _res = UseParentModelFrame._from_sdf(_c_use_parent_model_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("use_parent_model_frame")
            _use_parent_model_frame = _res
        else:
            _use_parent_model_frame = None
        if _use_parent_model_frame is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'use_parent_model_frame' is not supported in SDF version {version} (added in 1.5)")
        _xyz = _SDFVector3._from_sdf(el.get("xyz", "0 0 1"), version)
        if isinstance(_xyz, SDFError):
            return _xyz.extend("@xyz")
        return cls(sdf_version=version, dynamics=_dynamics, initial_position=_initial_position, limit=_limit, mimic=_mimic, use_parent_model_frame=_use_parent_model_frame, xyz=_xyz)


class Axis2(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        dynamics: "Dynamics" = None,
        initial_position: "InitialPosition" = None,
        limit: "Axis2Limit" = None,
        mimic: "Mimic" = None,
        use_parent_model_frame: "UseParentModelFrame" = None,
        xyz: _SDFVector3 = None
    ):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = _SDFVector3.from_sdf("0 0 1")
        self.dynamics = dynamics
        self.initial_position = initial_position
        self.limit = limit
        self.mimic = mimic
        self.use_parent_model_frame = use_parent_model_frame
        self.xyz = xyz

    def to_version(self, target_version: str) -> "Axis2":
        if self.initial_position is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.6)")
        if self.initial_position is not None and cmp_version(target_version, "1.9") >= 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (removed in 1.9)")
        if self.mimic is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {target_version} (added in 1.11)")
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.xyz is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["initial_position"] = self.initial_position.to_version(target_version) if self.initial_position is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["mimic"] = self.mimic.to_version(target_version) if self.mimic is not None else None
        kwargs["use_parent_model_frame"] = self.use_parent_model_frame.to_version(target_version) if self.use_parent_model_frame is not None else None
        kwargs["xyz"] = self.xyz
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis2")
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf(version))
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf(version))
        if cmp_version(version, "1.6") >= 0:
            if self.limit is None:
                self.limit = Axis2Limit(sdf_version=version)
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.mimic is not None:
            el.append(self.mimic.to_sdf(version))
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf(version))
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_dynamics = el.find("dynamics")
        if _c_dynamics is not None:
            _res = Dynamics._from_sdf(_c_dynamics, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamics")
            _dynamics = _res
        else:
            _dynamics = None
        _c_initial_position = el.find("initial_position")
        if _c_initial_position is not None:
            _res = InitialPosition._from_sdf(_c_initial_position, version)
            if isinstance(_res, SDFError):
                return _res.extend("initial_position")
            _initial_position = _res
        else:
            _initial_position = None
        if _initial_position is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'initial_position' is not supported in SDF version {version} (added in 1.6)")
        _c_limit = el.find("limit")
        if _c_limit is not None:
            _res = Axis2Limit._from_sdf(_c_limit, version)
            if isinstance(_res, SDFError):
                return _res.extend("limit")
            _limit = _res
        else:
            _res = Axis2Limit._from_sdf(ET.Element("limit"), version)
            if isinstance(_res, SDFError):
                return _res.extend("limit")
            _limit = _res
        _c_mimic = el.find("mimic")
        if _c_mimic is not None:
            _res = Mimic._from_sdf(_c_mimic, version)
            if isinstance(_res, SDFError):
                return _res.extend("mimic")
            _mimic = _res
        else:
            _mimic = None
        if _mimic is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'mimic' is not supported in SDF version {version} (added in 1.11)")
        _c_use_parent_model_frame = el.find("use_parent_model_frame")
        if _c_use_parent_model_frame is not None:
            _res = UseParentModelFrame._from_sdf(_c_use_parent_model_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("use_parent_model_frame")
            _use_parent_model_frame = _res
        else:
            _use_parent_model_frame = None
        if _use_parent_model_frame is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'use_parent_model_frame' is not supported in SDF version {version} (added in 1.5)")
        _xyz = _SDFVector3._from_sdf(el.get("xyz", "0 0 1"), version)
        if isinstance(_xyz, SDFError):
            return _xyz.extend("@xyz")
        return cls(sdf_version=version, dynamics=_dynamics, initial_position=_initial_position, limit=_limit, mimic=_mimic, use_parent_model_frame=_use_parent_model_frame, xyz=_xyz)


class Axis2Limit(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        dissipation: "Dissipation" = None,
        effort: float = 0,
        lower: float = -1e16,
        stiffness: "Stiffness" = None,
        upper: float = 1e16,
        velocity: float = 0
    ):
        self.__version__ = sdf_version
        self.dissipation = dissipation
        self.effort = effort
        self.lower = lower
        self.stiffness = stiffness
        self.upper = upper
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Axis2Limit":
        if self.dissipation is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'dissipation' is not supported in SDF version {target_version} (added in 1.4)")
        if self.effort is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'effort' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.lower is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'lower' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.stiffness is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'stiffness' is not supported in SDF version {target_version} (added in 1.4)")
        if self.upper is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'upper' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.velocity is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["dissipation"] = self.dissipation.to_version(target_version) if self.dissipation is not None else None
        kwargs["effort"] = self.effort
        kwargs["lower"] = self.lower
        kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
        kwargs["upper"] = self.upper
        kwargs["velocity"] = self.velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("limit")
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf(version))
        if self.effort is not None:
            el.set("effort", str(self.effort))
        if self.lower is not None:
            el.set("lower", str(self.lower))
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        if self.upper is not None:
            el.set("upper", str(self.upper))
        if self.velocity is not None:
            el.set("velocity", str(self.velocity))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_dissipation = el.find("dissipation")
        if _c_dissipation is not None:
            _res = Dissipation._from_sdf(_c_dissipation, version)
            if isinstance(_res, SDFError):
                return _res.extend("dissipation")
            _dissipation = _res
        else:
            _dissipation = None
        if _dissipation is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
        _effort = _parse_double(el.get("effort", 0))
        if isinstance(_effort, SDFError):
            return _effort.extend("@effort")
        _lower = _parse_double(el.get("lower", -1e16))
        if isinstance(_lower, SDFError):
            return _lower.extend("@lower")
        _c_stiffness = el.find("stiffness")
        if _c_stiffness is not None:
            _res = Stiffness._from_sdf(_c_stiffness, version)
            if isinstance(_res, SDFError):
                return _res.extend("stiffness")
            _stiffness = _res
        else:
            _stiffness = None
        if _stiffness is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
        _upper = _parse_double(el.get("upper", 1e16))
        if isinstance(_upper, SDFError):
            return _upper.extend("@upper")
        _velocity = _parse_double(el.get("velocity", 0))
        if isinstance(_velocity, SDFError):
            return _velocity.extend("@velocity")
        return cls(sdf_version=version, dissipation=_dissipation, effort=_effort, lower=_lower, stiffness=_stiffness, upper=_upper, velocity=_velocity)


class Bounce(BaseModel):
    def __init__(self, sdf_version: str, bounce: float = 0):
        self.__version__ = sdf_version
        self.bounce = bounce

    def to_version(self, target_version: str) -> "Bounce":
        kwargs = {"sdf_version": target_version}
        kwargs["bounce"] = self.bounce
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bounce")
        if self.bounce is not None:
            el.text = str(self.bounce)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _bounce = _parse_double(_text)
        if isinstance(_bounce, SDFError):
            return _bounce
        return cls(sdf_version=version, bounce=_bounce)


class Cfm(BaseModel):
    def __init__(self, sdf_version: str, cfm: float = 0):
        self.__version__ = sdf_version
        self.cfm = cfm

    def to_version(self, target_version: str) -> "Cfm":
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cfm")
        if self.cfm is not None:
            el.text = str(self.cfm)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _cfm = _parse_double(_text)
        if isinstance(_cfm, SDFError):
            return _cfm
        return cls(sdf_version=version, cfm=_cfm)


class CfmDamping(BaseModel):
    def __init__(self, sdf_version: str, cfm_damping: bool = False):
        self.__version__ = sdf_version
        self.cfm_damping = cfm_damping

    def to_version(self, target_version: str) -> "CfmDamping":
        if self.cfm_damping is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'cfm_damping' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["cfm_damping"] = self.cfm_damping
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cfm_damping")
        if self.cfm_damping is not None:
            el.text = str(self.cfm_damping).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _cfm_damping = str(_text).strip().lower() == 'true'
        if isinstance(_cfm_damping, SDFError):
            return _cfm_damping
        if _cfm_damping is not None and cmp_version(version, "1.3") < 0:
            if _cfm_damping != False:
                return SDFError(f"'cfm_damping' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, cfm_damping=_cfm_damping)


class Child(BaseModel):
    def __init__(self, sdf_version: str, child: str = "__default__", link: str = "__default__"):
        self.__version__ = sdf_version
        self.child = child
        self.link = link

    def to_version(self, target_version: str) -> "Child":
        if self.link is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'link' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["child"] = self.child
        kwargs["link"] = self.link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("child")
        if self.child is not None:
            el.text = self.child
        if self.link is not None:
            el.set("link", self.link)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _child = _text
        if isinstance(_child, SDFError):
            return _child
        _link = el.get("link", "__default__")
        if isinstance(_link, SDFError):
            return _link.extend("@link")
        return cls(sdf_version=version, child=_child, link=_link)


class Damping(BaseModel):
    def __init__(self, sdf_version: str, damping: float = 0):
        self.__version__ = sdf_version
        self.damping = damping

    def to_version(self, target_version: str) -> "Damping":
        if self.damping is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'damping' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["damping"] = self.damping
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("damping")
        if self.damping is not None:
            el.text = str(self.damping)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _damping = _parse_double(_text)
        if isinstance(_damping, SDFError):
            return _damping
        if _damping is not None and cmp_version(version, "1.2") < 0:
            if _damping != 0:
                return SDFError(f"'damping' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, damping=_damping)


class Dissipation(BaseModel):
    def __init__(self, sdf_version: str, dissipation: float = 1.0):
        self.__version__ = sdf_version
        self.dissipation = dissipation

    def to_version(self, target_version: str) -> "Dissipation":
        if self.dissipation is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'dissipation' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["dissipation"] = self.dissipation
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dissipation")
        if self.dissipation is not None:
            el.text = str(self.dissipation)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _dissipation = _parse_double(_text)
        if isinstance(_dissipation, SDFError):
            return _dissipation
        if _dissipation is not None and cmp_version(version, "1.4") < 0:
            if _dissipation != 1.0:
                return SDFError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, dissipation=_dissipation)


class Dynamics(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        damping: float = 0,
        friction: float = 0,
        spring_reference: "SpringReference" = None,
        spring_stiffness: "SpringStiffness" = None
    ):
        self.__version__ = sdf_version
        self.damping = damping
        self.friction = friction
        self.spring_reference = spring_reference
        self.spring_stiffness = spring_stiffness

    def to_version(self, target_version: str) -> "Dynamics":
        if self.damping is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'damping' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.friction is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'friction' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.spring_reference is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {target_version} (added in 1.5)")
        if self.spring_stiffness is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["damping"] = self.damping
        kwargs["friction"] = self.friction
        kwargs["spring_reference"] = self.spring_reference.to_version(target_version) if self.spring_reference is not None else None
        kwargs["spring_stiffness"] = self.spring_stiffness.to_version(target_version) if self.spring_stiffness is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamics")
        if self.damping is not None:
            el.set("damping", str(self.damping))
        if self.friction is not None:
            el.set("friction", str(self.friction))
        if self.spring_reference is not None:
            el.append(self.spring_reference.to_sdf(version))
        if self.spring_stiffness is not None:
            el.append(self.spring_stiffness.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _damping = _parse_double(el.get("damping", 0))
        if isinstance(_damping, SDFError):
            return _damping.extend("@damping")
        _friction = _parse_double(el.get("friction", 0))
        if isinstance(_friction, SDFError):
            return _friction.extend("@friction")
        _c_spring_reference = el.find("spring_reference")
        if _c_spring_reference is not None:
            _res = SpringReference._from_sdf(_c_spring_reference, version)
            if isinstance(_res, SDFError):
                return _res.extend("spring_reference")
            _spring_reference = _res
        else:
            _spring_reference = None
        if _spring_reference is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'spring_reference' is not supported in SDF version {version} (added in 1.5)")
        _c_spring_stiffness = el.find("spring_stiffness")
        if _c_spring_stiffness is not None:
            _res = SpringStiffness._from_sdf(_c_spring_stiffness, version)
            if isinstance(_res, SDFError):
                return _res.extend("spring_stiffness")
            _spring_stiffness = _res
        else:
            _spring_stiffness = None
        if _spring_stiffness is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'spring_stiffness' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, damping=_damping, friction=_friction, spring_reference=_spring_reference, spring_stiffness=_spring_stiffness)


class Effort(BaseModel):
    def __init__(self, sdf_version: str, effort: float = 0):
        self.__version__ = sdf_version
        self.effort = effort

    def to_version(self, target_version: str) -> "Effort":
        if self.effort is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'effort' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["effort"] = self.effort
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("effort")
        if self.effort is not None:
            el.text = str(self.effort)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _effort = _parse_double(_text)
        if isinstance(_effort, SDFError):
            return _effort
        if _effort is not None and cmp_version(version, "1.2") < 0:
            if _effort != 0:
                return SDFError(f"'effort' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, effort=_effort)


class Erp(BaseModel):
    def __init__(self, sdf_version: str, erp: float = 0.2):
        self.__version__ = sdf_version
        self.erp = erp

    def to_version(self, target_version: str) -> "Erp":
        if self.erp is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'erp' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["erp"] = self.erp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("erp")
        if self.erp is not None:
            el.text = str(self.erp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.2
        _erp = _parse_double(_text)
        if isinstance(_erp, SDFError):
            return _erp
        if _erp is not None and cmp_version(version, "1.2") < 0:
            if _erp != 0.2:
                return SDFError(f"'erp' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, erp=_erp)


class Friction(BaseModel):
    def __init__(self, sdf_version: str, friction: float = 0):
        self.__version__ = sdf_version
        self.friction = friction

    def to_version(self, target_version: str) -> "Friction":
        if self.friction is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'friction' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["friction"] = self.friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction")
        if self.friction is not None:
            el.text = str(self.friction)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _friction = _parse_double(_text)
        if isinstance(_friction, SDFError):
            return _friction
        if _friction is not None and cmp_version(version, "1.2") < 0:
            if _friction != 0:
                return SDFError(f"'friction' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, friction=_friction)


class FudgeFactor(BaseModel):
    def __init__(self, sdf_version: str, fudge_factor: float = 0):
        self.__version__ = sdf_version
        self.fudge_factor = fudge_factor

    def to_version(self, target_version: str) -> "FudgeFactor":
        kwargs = {"sdf_version": target_version}
        kwargs["fudge_factor"] = self.fudge_factor
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fudge_factor")
        if self.fudge_factor is not None:
            el.text = str(self.fudge_factor)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _fudge_factor = _parse_double(_text)
        if isinstance(_fudge_factor, SDFError):
            return _fudge_factor
        return cls(sdf_version=version, fudge_factor=_fudge_factor)


class GearboxRatio(BaseModel):
    def __init__(self, sdf_version: str, gearbox_ratio: float = 1.0):
        self.__version__ = sdf_version
        self.gearbox_ratio = gearbox_ratio

    def to_version(self, target_version: str) -> "GearboxRatio":
        if self.gearbox_ratio is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_ratio' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["gearbox_ratio"] = self.gearbox_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gearbox_ratio")
        if self.gearbox_ratio is not None:
            el.text = str(self.gearbox_ratio)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _gearbox_ratio = _parse_double(_text)
        if isinstance(_gearbox_ratio, SDFError):
            return _gearbox_ratio
        if _gearbox_ratio is not None and cmp_version(version, "1.4") < 0:
            if _gearbox_ratio != 1.0:
                return SDFError(f"'gearbox_ratio' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, gearbox_ratio=_gearbox_ratio)


class GearboxReferenceBody(BaseModel):
    def __init__(self, sdf_version: str, gearbox_reference_body: str = "__default__"):
        self.__version__ = sdf_version
        self.gearbox_reference_body = gearbox_reference_body

    def to_version(self, target_version: str) -> "GearboxReferenceBody":
        if self.gearbox_reference_body is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["gearbox_reference_body"] = self.gearbox_reference_body
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gearbox_reference_body")
        if self.gearbox_reference_body is not None:
            el.text = self.gearbox_reference_body
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _gearbox_reference_body = _text
        if isinstance(_gearbox_reference_body, SDFError):
            return _gearbox_reference_body
        if _gearbox_reference_body is not None and cmp_version(version, "1.4") < 0:
            if _gearbox_reference_body != "__default__":
                return SDFError(f"'gearbox_reference_body' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, gearbox_reference_body=_gearbox_reference_body)


class ImplicitSpringDamper(BaseModel):
    def __init__(self, sdf_version: str, implicit_spring_damper: bool = False):
        self.__version__ = sdf_version
        self.implicit_spring_damper = implicit_spring_damper

    def to_version(self, target_version: str) -> "ImplicitSpringDamper":
        if self.implicit_spring_damper is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'implicit_spring_damper' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["implicit_spring_damper"] = self.implicit_spring_damper
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("implicit_spring_damper")
        if self.implicit_spring_damper is not None:
            el.text = str(self.implicit_spring_damper).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _implicit_spring_damper = str(_text).strip().lower() == 'true'
        if isinstance(_implicit_spring_damper, SDFError):
            return _implicit_spring_damper
        if _implicit_spring_damper is not None and cmp_version(version, "1.4") < 0:
            if _implicit_spring_damper != False:
                return SDFError(f"'implicit_spring_damper' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, implicit_spring_damper=_implicit_spring_damper)


class InitialPosition(BaseModel):
    def __init__(self, sdf_version: str, initial_position: float = 0):
        self.__version__ = sdf_version
        self.initial_position = initial_position

    def to_version(self, target_version: str) -> "InitialPosition":
        if self.initial_position is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.6)")
        if self.initial_position is not None and cmp_version(target_version, "1.9") >= 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (removed in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["initial_position"] = self.initial_position
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("initial_position")
        if self.initial_position is not None:
            el.text = str(self.initial_position)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _initial_position = _parse_double(_text)
        if isinstance(_initial_position, SDFError):
            return _initial_position
        if _initial_position is not None and cmp_version(version, "1.6") < 0:
            if _initial_position != 0:
                return SDFError(f"'initial_position' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, initial_position=_initial_position)


class Joint(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        axis: "Axis" = None,
        axis2: "Axis2" = None,
        child: "Child" = None,
        frame: List["Frame"] = None,
        gearbox_ratio: "GearboxRatio" = None,
        gearbox_reference_body: "GearboxReferenceBody" = None,
        name: str = "__default__",
        origin: "Origin" = None,
        parent: "Parent" = None,
        physics: "Physics" = None,
        pose: "Pose" = None,
        screw_thread_pitch: "ScrewThreadPitch" = None,
        sensor: "Sensor" = None,
        thread_pitch: "ThreadPitch" = None,
        type: str = "__default__"
    ):
        self.__version__ = sdf_version
        self.axis = axis
        self.axis2 = axis2
        self.child = child
        self.frame = frame or []
        self.gearbox_ratio = gearbox_ratio
        self.gearbox_reference_body = gearbox_reference_body
        self.name = name
        self.origin = origin
        self.parent = parent
        self.physics = physics
        self.pose = pose
        self.screw_thread_pitch = screw_thread_pitch
        self.sensor = sensor
        self.thread_pitch = thread_pitch
        self.type = type

    def to_version(self, target_version: str) -> "Joint":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.gearbox_ratio is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_ratio' is not supported in SDF version {target_version} (added in 1.4)")
        if self.gearbox_reference_body is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {target_version} (added in 1.4)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.screw_thread_pitch is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {target_version} (added in 1.10)")
        if self.sensor is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'sensor' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["axis"] = self.axis.to_version(target_version) if self.axis is not None else None
        kwargs["axis2"] = self.axis2.to_version(target_version) if self.axis2 is not None else None
        kwargs["child"] = self.child.to_version(target_version) if self.child is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["gearbox_ratio"] = self.gearbox_ratio.to_version(target_version) if self.gearbox_ratio is not None else None
        kwargs["gearbox_reference_body"] = self.gearbox_reference_body.to_version(target_version) if self.gearbox_reference_body is not None else None
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["parent"] = self.parent.to_version(target_version) if self.parent is not None else None
        kwargs["physics"] = self.physics.to_version(target_version) if self.physics is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["screw_thread_pitch"] = self.screw_thread_pitch.to_version(target_version) if self.screw_thread_pitch is not None else None
        kwargs["sensor"] = self.sensor.to_version(target_version) if self.sensor is not None else None
        kwargs["thread_pitch"] = self.thread_pitch.to_version(target_version) if self.thread_pitch is not None else None
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("joint")
        if self.axis is not None:
            el.append(self.axis.to_sdf(version))
        if self.axis2 is not None:
            el.append(self.axis2.to_sdf(version))
        if self.child is not None:
            el.append(self.child.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.gearbox_ratio is not None:
            el.append(self.gearbox_ratio.to_sdf(version))
        if self.gearbox_reference_body is not None:
            el.append(self.gearbox_reference_body.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.parent is not None:
            el.append(self.parent.to_sdf(version))
        if self.physics is not None:
            el.append(self.physics.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.screw_thread_pitch is not None:
            el.append(self.screw_thread_pitch.to_sdf(version))
        if self.sensor is not None:
            el.append(self.sensor.to_sdf(version))
        if self.thread_pitch is not None:
            el.append(self.thread_pitch.to_sdf(version))
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_axis = el.find("axis")
        if _c_axis is not None:
            _res = Axis._from_sdf(_c_axis, version)
            if isinstance(_res, SDFError):
                return _res.extend("axis")
            _axis = _res
        else:
            _axis = None
        _c_axis2 = el.find("axis2")
        if _c_axis2 is not None:
            _res = Axis2._from_sdf(_c_axis2, version)
            if isinstance(_res, SDFError):
                return _res.extend("axis2")
            _axis2 = _res
        else:
            _axis2 = None
        _c_child = el.find("child")
        if _c_child is not None:
            _res = Child._from_sdf(_c_child, version)
            if isinstance(_res, SDFError):
                return _res.extend("child")
            _child = _res
        else:
            _child = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_gearbox_ratio = el.find("gearbox_ratio")
        if _c_gearbox_ratio is not None:
            _res = GearboxRatio._from_sdf(_c_gearbox_ratio, version)
            if isinstance(_res, SDFError):
                return _res.extend("gearbox_ratio")
            _gearbox_ratio = _res
        else:
            _gearbox_ratio = None
        if _gearbox_ratio is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'gearbox_ratio' is not supported in SDF version {version} (added in 1.4)")
        _c_gearbox_reference_body = el.find("gearbox_reference_body")
        if _c_gearbox_reference_body is not None:
            _res = GearboxReferenceBody._from_sdf(_c_gearbox_reference_body, version)
            if isinstance(_res, SDFError):
                return _res.extend("gearbox_reference_body")
            _gearbox_reference_body = _res
        else:
            _gearbox_reference_body = None
        if _gearbox_reference_body is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'gearbox_reference_body' is not supported in SDF version {version} (added in 1.4)")
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
        _c_parent = el.find("parent")
        if _c_parent is not None:
            _res = Parent._from_sdf(_c_parent, version)
            if isinstance(_res, SDFError):
                return _res.extend("parent")
            _parent = _res
        else:
            _parent = None
        _c_physics = el.find("physics")
        if _c_physics is not None:
            _res = Physics._from_sdf(_c_physics, version)
            if isinstance(_res, SDFError):
                return _res.extend("physics")
            _physics = _res
        else:
            _physics = None
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
        _c_screw_thread_pitch = el.find("screw_thread_pitch")
        if _c_screw_thread_pitch is not None:
            _res = ScrewThreadPitch._from_sdf(_c_screw_thread_pitch, version)
            if isinstance(_res, SDFError):
                return _res.extend("screw_thread_pitch")
            _screw_thread_pitch = _res
        else:
            _screw_thread_pitch = None
        if _screw_thread_pitch is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'screw_thread_pitch' is not supported in SDF version {version} (added in 1.10)")
        _c_sensor = el.find("sensor")
        if _c_sensor is not None:
            _res = Sensor._from_sdf(_c_sensor, version)
            if isinstance(_res, SDFError):
                return _res.extend("sensor")
            _sensor = _res
        else:
            _sensor = None
        if _sensor is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'sensor' is not supported in SDF version {version} (added in 1.4)")
        _c_thread_pitch = el.find("thread_pitch")
        if _c_thread_pitch is not None:
            _res = ThreadPitch._from_sdf(_c_thread_pitch, version)
            if isinstance(_res, SDFError):
                return _res.extend("thread_pitch")
            _thread_pitch = _res
        else:
            _thread_pitch = None
        _type = el.get("type", "__default__")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, axis=_axis, axis2=_axis2, child=_child, frame=_frame, gearbox_ratio=_gearbox_ratio, gearbox_reference_body=_gearbox_reference_body, name=_name, origin=_origin, parent=_parent, physics=_physics, pose=_pose, screw_thread_pitch=_screw_thread_pitch, sensor=_sensor, thread_pitch=_thread_pitch, type=_type)


class Limit(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        dissipation: "Dissipation" = None,
        effort: float = 0,
        lower: float = -1e16,
        stiffness: "Stiffness" = None,
        upper: float = 1e16,
        velocity: float = 0
    ):
        self.__version__ = sdf_version
        self.dissipation = dissipation
        self.effort = effort
        self.lower = lower
        self.stiffness = stiffness
        self.upper = upper
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Limit":
        if self.dissipation is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'dissipation' is not supported in SDF version {target_version} (added in 1.4)")
        if self.effort is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'effort' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.lower is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'lower' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.stiffness is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'stiffness' is not supported in SDF version {target_version} (added in 1.4)")
        if self.upper is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'upper' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.velocity is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["dissipation"] = self.dissipation.to_version(target_version) if self.dissipation is not None else None
        kwargs["effort"] = self.effort
        kwargs["lower"] = self.lower
        kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
        kwargs["upper"] = self.upper
        kwargs["velocity"] = self.velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("limit")
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf(version))
        if self.effort is not None:
            el.set("effort", str(self.effort))
        if self.lower is not None:
            el.set("lower", str(self.lower))
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        if self.upper is not None:
            el.set("upper", str(self.upper))
        if self.velocity is not None:
            el.set("velocity", str(self.velocity))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_dissipation = el.find("dissipation")
        if _c_dissipation is not None:
            _res = Dissipation._from_sdf(_c_dissipation, version)
            if isinstance(_res, SDFError):
                return _res.extend("dissipation")
            _dissipation = _res
        else:
            _dissipation = None
        if _dissipation is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
        _effort = _parse_double(el.get("effort", 0))
        if isinstance(_effort, SDFError):
            return _effort.extend("@effort")
        _lower = _parse_double(el.get("lower", -1e16))
        if isinstance(_lower, SDFError):
            return _lower.extend("@lower")
        _c_stiffness = el.find("stiffness")
        if _c_stiffness is not None:
            _res = Stiffness._from_sdf(_c_stiffness, version)
            if isinstance(_res, SDFError):
                return _res.extend("stiffness")
            _stiffness = _res
        else:
            _stiffness = None
        if _stiffness is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
        _upper = _parse_double(el.get("upper", 1e16))
        if isinstance(_upper, SDFError):
            return _upper.extend("@upper")
        _velocity = _parse_double(el.get("velocity", 0))
        if isinstance(_velocity, SDFError):
            return _velocity.extend("@velocity")
        return cls(sdf_version=version, dissipation=_dissipation, effort=_effort, lower=_lower, stiffness=_stiffness, upper=_upper, velocity=_velocity)


class LimitCfm(BaseModel):
    def __init__(self, sdf_version: str, cfm: float = 0.0):
        self.__version__ = sdf_version
        self.cfm = cfm

    def to_version(self, target_version: str) -> "LimitCfm":
        if self.cfm is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'cfm' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cfm")
        if self.cfm is not None:
            el.text = str(self.cfm)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _cfm = _parse_double(_text)
        if isinstance(_cfm, SDFError):
            return _cfm
        if _cfm is not None and cmp_version(version, "1.2") < 0:
            if _cfm != 0.0:
                return SDFError(f"'cfm' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, cfm=_cfm)


class Lower(BaseModel):
    def __init__(self, sdf_version: str, lower: float = -1e16):
        self.__version__ = sdf_version
        self.lower = lower

    def to_version(self, target_version: str) -> "Lower":
        if self.lower is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'lower' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["lower"] = self.lower
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lower")
        if self.lower is not None:
            el.text = str(self.lower)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -1e16
        _lower = _parse_double(_text)
        if isinstance(_lower, SDFError):
            return _lower
        if _lower is not None and cmp_version(version, "1.2") < 0:
            if _lower != -1e16:
                return SDFError(f"'lower' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, lower=_lower)


class MaxForce(BaseModel):
    def __init__(self, sdf_version: str, max_force: float = 0):
        self.__version__ = sdf_version
        self.max_force = max_force

    def to_version(self, target_version: str) -> "MaxForce":
        kwargs = {"sdf_version": target_version}
        kwargs["max_force"] = self.max_force
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_force")
        if self.max_force is not None:
            el.text = str(self.max_force)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max_force = _parse_double(_text)
        if isinstance(_max_force, SDFError):
            return _max_force
        return cls(sdf_version=version, max_force=_max_force)


class MustBeLoopJoint(BaseModel):
    def __init__(self, sdf_version: str, must_be_loop_joint: bool = False):
        self.__version__ = sdf_version
        self.must_be_loop_joint = must_be_loop_joint

    def to_version(self, target_version: str) -> "MustBeLoopJoint":
        kwargs = {"sdf_version": target_version}
        kwargs["must_be_loop_joint"] = self.must_be_loop_joint
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("must_be_loop_joint")
        if self.must_be_loop_joint is not None:
            el.text = str(self.must_be_loop_joint).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _must_be_loop_joint = str(_text).strip().lower() == 'true'
        if isinstance(_must_be_loop_joint, SDFError):
            return _must_be_loop_joint
        return cls(sdf_version=version, must_be_loop_joint=_must_be_loop_joint)


class Ode(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        bounce: "Bounce" = None,
        cfm: "Cfm" = None,
        cfm_damping: "CfmDamping" = None,
        erp: "Erp" = None,
        fudge_factor: "FudgeFactor" = None,
        implicit_spring_damper: "ImplicitSpringDamper" = None,
        limit: "OdeLimit" = None,
        max_force: "MaxForce" = None,
        provide_feedback: "ProvideFeedback" = None,
        suspension: "Suspension" = None,
        velocity: "Velocity" = None
    ):
        self.__version__ = sdf_version
        self.bounce = bounce
        self.cfm = cfm
        self.cfm_damping = cfm_damping
        self.erp = erp
        self.fudge_factor = fudge_factor
        self.implicit_spring_damper = implicit_spring_damper
        self.limit = limit
        self.max_force = max_force
        self.provide_feedback = provide_feedback
        self.suspension = suspension
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Ode":
        if self.cfm_damping is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'cfm_damping' is not supported in SDF version {target_version} (added in 1.3)")
        if self.erp is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'erp' is not supported in SDF version {target_version} (added in 1.4)")
        if self.implicit_spring_damper is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'implicit_spring_damper' is not supported in SDF version {target_version} (added in 1.4)")
        if self.provide_feedback is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.3)")
        if self.provide_feedback is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["bounce"] = self.bounce.to_version(target_version) if self.bounce is not None else None
        kwargs["cfm"] = self.cfm.to_version(target_version) if self.cfm is not None else None
        kwargs["cfm_damping"] = self.cfm_damping.to_version(target_version) if self.cfm_damping is not None else None
        kwargs["erp"] = self.erp.to_version(target_version) if self.erp is not None else None
        kwargs["fudge_factor"] = self.fudge_factor.to_version(target_version) if self.fudge_factor is not None else None
        kwargs["implicit_spring_damper"] = self.implicit_spring_damper.to_version(target_version) if self.implicit_spring_damper is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["max_force"] = self.max_force.to_version(target_version) if self.max_force is not None else None
        kwargs["provide_feedback"] = self.provide_feedback.to_version(target_version) if self.provide_feedback is not None else None
        kwargs["suspension"] = self.suspension.to_version(target_version) if self.suspension is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.bounce is not None:
            el.append(self.bounce.to_sdf(version))
        if self.cfm is not None:
            el.append(self.cfm.to_sdf(version))
        if self.cfm_damping is not None:
            el.append(self.cfm_damping.to_sdf(version))
        if self.erp is not None:
            el.append(self.erp.to_sdf(version))
        if self.fudge_factor is not None:
            el.append(self.fudge_factor.to_sdf(version))
        if self.implicit_spring_damper is not None:
            el.append(self.implicit_spring_damper.to_sdf(version))
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.max_force is not None:
            el.append(self.max_force.to_sdf(version))
        if self.provide_feedback is not None:
            el.append(self.provide_feedback.to_sdf(version))
        if self.suspension is not None:
            el.append(self.suspension.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_bounce = el.find("bounce")
        if _c_bounce is not None:
            _res = Bounce._from_sdf(_c_bounce, version)
            if isinstance(_res, SDFError):
                return _res.extend("bounce")
            _bounce = _res
        else:
            _bounce = None
        _c_cfm = el.find("cfm")
        if _c_cfm is not None:
            _res = Cfm._from_sdf(_c_cfm, version)
            if isinstance(_res, SDFError):
                return _res.extend("cfm")
            _cfm = _res
        else:
            _cfm = None
        _c_cfm_damping = el.find("cfm_damping")
        if _c_cfm_damping is not None:
            _res = CfmDamping._from_sdf(_c_cfm_damping, version)
            if isinstance(_res, SDFError):
                return _res.extend("cfm_damping")
            _cfm_damping = _res
        else:
            _cfm_damping = None
        if _cfm_damping is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'cfm_damping' is not supported in SDF version {version} (added in 1.3)")
        _c_erp = el.find("erp")
        if _c_erp is not None:
            _res = Erp._from_sdf(_c_erp, version)
            if isinstance(_res, SDFError):
                return _res.extend("erp")
            _erp = _res
        else:
            _erp = None
        if _erp is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'erp' is not supported in SDF version {version} (added in 1.4)")
        _c_fudge_factor = el.find("fudge_factor")
        if _c_fudge_factor is not None:
            _res = FudgeFactor._from_sdf(_c_fudge_factor, version)
            if isinstance(_res, SDFError):
                return _res.extend("fudge_factor")
            _fudge_factor = _res
        else:
            _fudge_factor = None
        _c_implicit_spring_damper = el.find("implicit_spring_damper")
        if _c_implicit_spring_damper is not None:
            _res = ImplicitSpringDamper._from_sdf(_c_implicit_spring_damper, version)
            if isinstance(_res, SDFError):
                return _res.extend("implicit_spring_damper")
            _implicit_spring_damper = _res
        else:
            _implicit_spring_damper = None
        if _implicit_spring_damper is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'implicit_spring_damper' is not supported in SDF version {version} (added in 1.4)")
        _c_limit = el.find("limit")
        if _c_limit is not None:
            _res = OdeLimit._from_sdf(_c_limit, version)
            if isinstance(_res, SDFError):
                return _res.extend("limit")
            _limit = _res
        else:
            _limit = None
        _c_max_force = el.find("max_force")
        if _c_max_force is not None:
            _res = MaxForce._from_sdf(_c_max_force, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_force")
            _max_force = _res
        else:
            _max_force = None
        _c_provide_feedback = el.find("provide_feedback")
        if _c_provide_feedback is not None:
            _res = ProvideFeedback._from_sdf(_c_provide_feedback, version)
            if isinstance(_res, SDFError):
                return _res.extend("provide_feedback")
            _provide_feedback = _res
        else:
            _provide_feedback = None
        if _provide_feedback is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.3)")
        _c_suspension = el.find("suspension")
        if _c_suspension is not None:
            _res = Suspension._from_sdf(_c_suspension, version)
            if isinstance(_res, SDFError):
                return _res.extend("suspension")
            _suspension = _res
        else:
            _suspension = None
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        return cls(sdf_version=version, bounce=_bounce, cfm=_cfm, cfm_damping=_cfm_damping, erp=_erp, fudge_factor=_fudge_factor, implicit_spring_damper=_implicit_spring_damper, limit=_limit, max_force=_max_force, provide_feedback=_provide_feedback, suspension=_suspension, velocity=_velocity)


class OdeLimit(BaseModel):
    def __init__(self, sdf_version: str, cfm: float = 0.0, erp: float = 0.2):
        self.__version__ = sdf_version
        self.cfm = cfm
        self.erp = erp

    def to_version(self, target_version: str) -> "OdeLimit":
        if self.cfm is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'cfm' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.erp is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'erp' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm
        kwargs["erp"] = self.erp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("limit")
        if self.cfm is not None:
            el.set("cfm", str(self.cfm))
        if self.erp is not None:
            el.set("erp", str(self.erp))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _cfm = _parse_double(el.get("cfm", 0.0))
        if isinstance(_cfm, SDFError):
            return _cfm.extend("@cfm")
        _erp = _parse_double(el.get("erp", 0.2))
        if isinstance(_erp, SDFError):
            return _erp.extend("@erp")
        return cls(sdf_version=version, cfm=_cfm, erp=_erp)


class Origin(BaseModel):
    def __init__(self, sdf_version: str, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "Origin":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("origin")
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _pose = _SDFPose._from_sdf(el.get("pose", "0 0 0 0 0 0"), version)
        if isinstance(_pose, SDFError):
            return _pose.extend("@pose")
        return cls(sdf_version=version, pose=_pose)


class Parent(BaseModel):
    def __init__(self, sdf_version: str, link: str = "__default__", parent: str = "__default__"):
        self.__version__ = sdf_version
        self.link = link
        self.parent = parent

    def to_version(self, target_version: str) -> "Parent":
        if self.link is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'link' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["link"] = self.link
        kwargs["parent"] = self.parent
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("parent")
        if self.link is not None:
            el.set("link", self.link)
        if self.parent is not None:
            el.text = self.parent
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _link = el.get("link", "__default__")
        if isinstance(_link, SDFError):
            return _link.extend("@link")
        _text = el.text or "__default__"
        _parent = _text
        if isinstance(_parent, SDFError):
            return _parent
        return cls(sdf_version=version, link=_link, parent=_parent)


class Physics(BaseModel):
    _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

    def __init__(
        self,
        sdf_version: str,
        ode: "Ode" = None,
        provide_feedback: "ProvideFeedback" = None,
        simbody: "Simbody" = None
    ):
        self.__version__ = sdf_version
        self.ode = ode
        self.provide_feedback = provide_feedback
        self.simbody = simbody

    def to_version(self, target_version: str) -> "Physics":
        if self.provide_feedback is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.4)")
        if self.simbody is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'simbody' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["provide_feedback"] = self.provide_feedback.to_version(target_version) if self.provide_feedback is not None else None
        kwargs["simbody"] = self.simbody.to_version(target_version) if self.simbody is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("physics")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.provide_feedback is not None:
            el.append(self.provide_feedback.to_sdf(version))
        if self.simbody is not None:
            el.append(self.simbody.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = Ode._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        _c_provide_feedback = el.find("provide_feedback")
        if _c_provide_feedback is not None:
            _res = ProvideFeedback._from_sdf(_c_provide_feedback, version)
            if isinstance(_res, SDFError):
                return _res.extend("provide_feedback")
            _provide_feedback = _res
        else:
            _provide_feedback = None
        if _provide_feedback is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.4)")
        _c_simbody = el.find("simbody")
        if _c_simbody is not None:
            _res = Simbody._from_sdf(_c_simbody, version)
            if isinstance(_res, SDFError):
                return _res.extend("simbody")
            _simbody = _res
        else:
            _simbody = None
        if _simbody is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'simbody' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, ode=_ode, provide_feedback=_provide_feedback, simbody=_simbody)


class ProvideFeedback(BaseModel):
    def __init__(self, sdf_version: str, provide_feedback: bool = False):
        self.__version__ = sdf_version
        self.provide_feedback = provide_feedback

    def to_version(self, target_version: str) -> "ProvideFeedback":
        if self.provide_feedback is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.3)")
        if self.provide_feedback is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["provide_feedback"] = self.provide_feedback
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("provide_feedback")
        if self.provide_feedback is not None:
            el.text = str(self.provide_feedback).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _provide_feedback = str(_text).strip().lower() == 'true'
        if isinstance(_provide_feedback, SDFError):
            return _provide_feedback
        if _provide_feedback is not None and cmp_version(version, "1.3") < 0:
            if _provide_feedback != False:
                return SDFError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, provide_feedback=_provide_feedback)


class ScrewThreadPitch(BaseModel):
    def __init__(self, sdf_version: str, screw_thread_pitch: float = 1.0):
        self.__version__ = sdf_version
        self.screw_thread_pitch = screw_thread_pitch

    def to_version(self, target_version: str) -> "ScrewThreadPitch":
        if self.screw_thread_pitch is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {target_version} (added in 1.10)")
        kwargs = {"sdf_version": target_version}
        kwargs["screw_thread_pitch"] = self.screw_thread_pitch
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("screw_thread_pitch")
        if self.screw_thread_pitch is not None:
            el.text = str(self.screw_thread_pitch)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _screw_thread_pitch = _parse_double(_text)
        if isinstance(_screw_thread_pitch, SDFError):
            return _screw_thread_pitch
        if _screw_thread_pitch is not None and cmp_version(version, "1.10") < 0:
            if _screw_thread_pitch != 1.0:
                return SDFError(f"'screw_thread_pitch' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, screw_thread_pitch=_screw_thread_pitch)


class Simbody(BaseModel):
    def __init__(self, sdf_version: str, must_be_loop_joint: "MustBeLoopJoint" = None):
        self.__version__ = sdf_version
        self.must_be_loop_joint = must_be_loop_joint

    def to_version(self, target_version: str) -> "Simbody":
        kwargs = {"sdf_version": target_version}
        kwargs["must_be_loop_joint"] = self.must_be_loop_joint.to_version(target_version) if self.must_be_loop_joint is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("simbody")
        if self.must_be_loop_joint is not None:
            el.append(self.must_be_loop_joint.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_must_be_loop_joint = el.find("must_be_loop_joint")
        if _c_must_be_loop_joint is not None:
            _res = MustBeLoopJoint._from_sdf(_c_must_be_loop_joint, version)
            if isinstance(_res, SDFError):
                return _res.extend("must_be_loop_joint")
            _must_be_loop_joint = _res
        else:
            _must_be_loop_joint = None
        return cls(sdf_version=version, must_be_loop_joint=_must_be_loop_joint)


class SpringReference(BaseModel):
    def __init__(self, sdf_version: str, spring_reference: float = 0):
        self.__version__ = sdf_version
        self.spring_reference = spring_reference

    def to_version(self, target_version: str) -> "SpringReference":
        if self.spring_reference is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["spring_reference"] = self.spring_reference
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spring_reference")
        if self.spring_reference is not None:
            el.text = str(self.spring_reference)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _spring_reference = _parse_double(_text)
        if isinstance(_spring_reference, SDFError):
            return _spring_reference
        if _spring_reference is not None and cmp_version(version, "1.5") < 0:
            if _spring_reference != 0:
                return SDFError(f"'spring_reference' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, spring_reference=_spring_reference)


class SpringStiffness(BaseModel):
    def __init__(self, sdf_version: str, spring_stiffness: float = 0):
        self.__version__ = sdf_version
        self.spring_stiffness = spring_stiffness

    def to_version(self, target_version: str) -> "SpringStiffness":
        if self.spring_stiffness is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["spring_stiffness"] = self.spring_stiffness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spring_stiffness")
        if self.spring_stiffness is not None:
            el.text = str(self.spring_stiffness)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _spring_stiffness = _parse_double(_text)
        if isinstance(_spring_stiffness, SDFError):
            return _spring_stiffness
        if _spring_stiffness is not None and cmp_version(version, "1.5") < 0:
            if _spring_stiffness != 0:
                return SDFError(f"'spring_stiffness' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, spring_stiffness=_spring_stiffness)


class Stiffness(BaseModel):
    def __init__(self, sdf_version: str, stiffness: float = 1e8):
        self.__version__ = sdf_version
        self.stiffness = stiffness

    def to_version(self, target_version: str) -> "Stiffness":
        if self.stiffness is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'stiffness' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["stiffness"] = self.stiffness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("stiffness")
        if self.stiffness is not None:
            el.text = str(self.stiffness)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1e8
        _stiffness = _parse_double(_text)
        if isinstance(_stiffness, SDFError):
            return _stiffness
        if _stiffness is not None and cmp_version(version, "1.4") < 0:
            if _stiffness != 1e8:
                return SDFError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, stiffness=_stiffness)


class Suspension(BaseModel):
    def __init__(self, sdf_version: str, cfm: float = 0.0, erp: float = 0.2):
        self.__version__ = sdf_version
        self.cfm = cfm
        self.erp = erp

    def to_version(self, target_version: str) -> "Suspension":
        if self.cfm is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'cfm' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.erp is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'erp' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm
        kwargs["erp"] = self.erp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("suspension")
        if self.cfm is not None:
            el.set("cfm", str(self.cfm))
        if self.erp is not None:
            el.set("erp", str(self.erp))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _cfm = _parse_double(el.get("cfm", 0.0))
        if isinstance(_cfm, SDFError):
            return _cfm.extend("@cfm")
        _erp = _parse_double(el.get("erp", 0.2))
        if isinstance(_erp, SDFError):
            return _erp.extend("@erp")
        return cls(sdf_version=version, cfm=_cfm, erp=_erp)


class SuspensionCfm(BaseModel):
    def __init__(self, sdf_version: str, cfm: float = 0.0):
        self.__version__ = sdf_version
        self.cfm = cfm

    def to_version(self, target_version: str) -> "SuspensionCfm":
        if self.cfm is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'cfm' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cfm")
        if self.cfm is not None:
            el.text = str(self.cfm)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _cfm = _parse_double(_text)
        if isinstance(_cfm, SDFError):
            return _cfm
        if _cfm is not None and cmp_version(version, "1.2") < 0:
            if _cfm != 0.0:
                return SDFError(f"'cfm' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, cfm=_cfm)


class ThreadPitch(BaseModel):
    def __init__(self, sdf_version: str, thread_pitch: float = 1.0):
        self.__version__ = sdf_version
        self.thread_pitch = thread_pitch

    def to_version(self, target_version: str) -> "ThreadPitch":
        kwargs = {"sdf_version": target_version}
        kwargs["thread_pitch"] = self.thread_pitch
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("thread_pitch")
        if self.thread_pitch is not None:
            el.text = str(self.thread_pitch)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _thread_pitch = _parse_double(_text)
        if isinstance(_thread_pitch, SDFError):
            return _thread_pitch
        return cls(sdf_version=version, thread_pitch=_thread_pitch)


class Upper(BaseModel):
    def __init__(self, sdf_version: str, upper: float = 1e16):
        self.__version__ = sdf_version
        self.upper = upper

    def to_version(self, target_version: str) -> "Upper":
        if self.upper is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'upper' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["upper"] = self.upper
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("upper")
        if self.upper is not None:
            el.text = str(self.upper)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1e16
        _upper = _parse_double(_text)
        if isinstance(_upper, SDFError):
            return _upper
        if _upper is not None and cmp_version(version, "1.2") < 0:
            if _upper != 1e16:
                return SDFError(f"'upper' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, upper=_upper)


class UseParentModelFrame(BaseModel):
    def __init__(self, sdf_version: str, use_parent_model_frame: bool = False):
        self.__version__ = sdf_version
        self.use_parent_model_frame = use_parent_model_frame

    def to_version(self, target_version: str) -> "UseParentModelFrame":
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["use_parent_model_frame"] = self.use_parent_model_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("use_parent_model_frame")
        if self.use_parent_model_frame is not None:
            el.text = str(self.use_parent_model_frame).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _use_parent_model_frame = str(_text).strip().lower() == 'true'
        if isinstance(_use_parent_model_frame, SDFError):
            return _use_parent_model_frame
        if _use_parent_model_frame is not None and cmp_version(version, "1.5") < 0:
            if _use_parent_model_frame != False:
                return SDFError(f"'use_parent_model_frame' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, use_parent_model_frame=_use_parent_model_frame)


class Velocity(BaseModel):
    def __init__(self, sdf_version: str, velocity: float = 0):
        self.__version__ = sdf_version
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Velocity":
        if self.velocity is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["velocity"] = self.velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = str(self.velocity)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _velocity = _parse_double(_text)
        if isinstance(_velocity, SDFError):
            return _velocity
        if _velocity is not None and cmp_version(version, "1.2") < 0:
            if _velocity != 0:
                return SDFError(f"'velocity' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, velocity=_velocity)


class Xyz(BaseModel):
    def __init__(self, sdf_version: str, expressed_in: str = "", xyz: _SDFVector3 = None):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = _SDFVector3.from_sdf("0 0 1")
        self.expressed_in = expressed_in
        self.xyz = xyz

    def to_version(self, target_version: str) -> "Xyz":
        if self.expressed_in is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'expressed_in' is not supported in SDF version {target_version} (added in 1.7)")
        if self.xyz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["expressed_in"] = self.expressed_in
        kwargs["xyz"] = self.xyz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xyz")
        if self.expressed_in is not None:
            el.set("expressed_in", self.expressed_in)
        if self.xyz is not None:
            el.text = self.xyz.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _expressed_in = el.get("expressed_in", "")
        if isinstance(_expressed_in, SDFError):
            return _expressed_in.extend("@expressed_in")
        if _expressed_in is not None and cmp_version(version, "1.7") < 0:
            if _expressed_in != "":
                return SDFError(f"'expressed_in' is not supported in SDF version {version} (added in 1.7)")
        _text = el.text or "0 0 1"
        _xyz = _SDFVector3._from_sdf(_text, version)
        if isinstance(_xyz, SDFError):
            return _xyz
        if _xyz is not None and cmp_version(version, "1.2") < 0:
            if _xyz != "0 0 1":
                return SDFError(f"'xyz' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, expressed_in=_expressed_in, xyz=_xyz)
