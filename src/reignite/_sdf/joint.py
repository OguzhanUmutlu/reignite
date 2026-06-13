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
from ..utils.migration import apply_migrations

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.mimic import Mimic
    from ..elements.sensor import Sensor

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
class Joint(BaseModel):
    class Axis(BaseModel):
        class Dynamics(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                damping: float | None = None,
                friction: float | None = None,
                spring_reference: float | None = None,
                spring_stiffness: float | None = None
            ):
                super().__init__(sdf_version)
                self.damping = damping
                self.friction = friction
                self.spring_reference = spring_reference
                self.spring_stiffness = spring_stiffness

            def to_version(self, target_version: str) -> "Joint.Axis.Dynamics":
                if self.spring_reference is not None and cmp_version(target_version, "1.5") < 0:
                    raise ValueError(f"'spring_reference' is not supported in SDF version {target_version} (added in 1.5)")
                if self.spring_stiffness is not None and cmp_version(target_version, "1.5") < 0:
                    raise ValueError(f"'spring_stiffness' is not supported in SDF version {target_version} (added in 1.5)")
                kwargs: dict = {"sdf_version": target_version, "damping": self.damping, "friction": self.friction, "spring_reference": self.spring_reference, "spring_stiffness": self.spring_stiffness}
                return Joint.Axis.Dynamics(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("dynamics")
                if self.damping is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("damping")
                        _c_tmp.text = str(self.damping)
                        el.append(_c_tmp)
                    else:
                        el.set("damping", str(self.damping))
                if self.friction is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("friction")
                        _c_tmp.text = str(self.friction)
                        el.append(_c_tmp)
                    else:
                        el.set("friction", str(self.friction))
                if self.spring_reference is not None:
                    _c_tmp = ET.Element("spring_reference")
                    _c_tmp.text = str(self.spring_reference)
                    el.append(_c_tmp)
                if self.spring_stiffness is not None:
                    _c_tmp = ET.Element("spring_stiffness")
                    _c_tmp.text = str(self.spring_stiffness)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Axis.Dynamics | SDFError":
                _raw_damping = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("damping")
                    if _c_tmp is not None: _raw_damping = _c_tmp.text
                else:
                    _raw_damping = el.get("damping")
                if _raw_damping is not None:
                    _damping = _parse_double(_raw_damping)
                    if isinstance(_damping, SDFError):
                        return _damping.extend("@damping")
                else:
                    _damping = None
                _raw_friction = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("friction")
                    if _c_tmp is not None: _raw_friction = _c_tmp.text
                else:
                    _raw_friction = el.get("friction")
                if _raw_friction is not None:
                    _friction = _parse_double(_raw_friction)
                    if isinstance(_friction, SDFError):
                        return _friction.extend("@friction")
                else:
                    _friction = None
                _c_tmp = el.find("spring_reference")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("spring_reference")
                    _spring_reference = _val
                else:
                    _spring_reference = None
                if _spring_reference is not None and cmp_version(version, "1.5") < 0:
                    return SDFError(f"'spring_reference' is not supported in SDF version {version} (added in 1.5)")
                _c_tmp = el.find("spring_stiffness")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("spring_stiffness")
                    _spring_stiffness = _val
                else:
                    _spring_stiffness = None
                if _spring_stiffness is not None and cmp_version(version, "1.5") < 0:
                    return SDFError(f"'spring_stiffness' is not supported in SDF version {version} (added in 1.5)")
                return cls(sdf_version=version, damping=_damping, friction=_friction, spring_reference=_spring_reference, spring_stiffness=_spring_stiffness)

        class Limit(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                dissipation: float | None = None,
                effort: float | None = None,
                lower: float | None = None,
                stiffness: float | None = None,
                upper: float | None = None,
                velocity: float | None = None
            ):
                super().__init__(sdf_version)
                self.dissipation = dissipation
                self.effort = effort
                self.lower = lower
                self.stiffness = stiffness
                self.upper = upper
                self.velocity = velocity

            def to_version(self, target_version: str) -> "Joint.Axis.Limit":
                if self.dissipation is not None and cmp_version(target_version, "1.4") < 0:
                    raise ValueError(f"'dissipation' is not supported in SDF version {target_version} (added in 1.4)")
                if self.stiffness is not None and cmp_version(target_version, "1.4") < 0:
                    raise ValueError(f"'stiffness' is not supported in SDF version {target_version} (added in 1.4)")
                kwargs: dict = {"sdf_version": target_version, "dissipation": self.dissipation, "effort": self.effort, "lower": self.lower, "stiffness": self.stiffness, "upper": self.upper, "velocity": self.velocity}
                return Joint.Axis.Limit(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("limit")
                if self.dissipation is not None:
                    _c_tmp = ET.Element("dissipation")
                    _c_tmp.text = str(self.dissipation)
                    el.append(_c_tmp)
                if self.effort is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("effort")
                        _c_tmp.text = str(self.effort)
                        el.append(_c_tmp)
                    else:
                        el.set("effort", str(self.effort))
                if self.lower is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("lower")
                        _c_tmp.text = str(self.lower)
                        el.append(_c_tmp)
                    else:
                        el.set("lower", str(self.lower))
                if self.stiffness is not None:
                    _c_tmp = ET.Element("stiffness")
                    _c_tmp.text = str(self.stiffness)
                    el.append(_c_tmp)
                if self.upper is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("upper")
                        _c_tmp.text = str(self.upper)
                        el.append(_c_tmp)
                    else:
                        el.set("upper", str(self.upper))
                if self.velocity is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("velocity")
                        _c_tmp.text = str(self.velocity)
                        el.append(_c_tmp)
                    else:
                        el.set("velocity", str(self.velocity))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Axis.Limit | SDFError":
                _c_tmp = el.find("dissipation")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("dissipation")
                    _dissipation = _val
                else:
                    _dissipation = None
                if _dissipation is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
                _raw_effort = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("effort")
                    if _c_tmp is not None: _raw_effort = _c_tmp.text
                else:
                    _raw_effort = el.get("effort")
                if _raw_effort is not None:
                    _effort = _parse_double(_raw_effort)
                    if isinstance(_effort, SDFError):
                        return _effort.extend("@effort")
                else:
                    _effort = None
                _raw_lower = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("lower")
                    if _c_tmp is not None: _raw_lower = _c_tmp.text
                else:
                    _raw_lower = el.get("lower")
                if _raw_lower is not None:
                    _lower = _parse_double(_raw_lower)
                    if isinstance(_lower, SDFError):
                        return _lower.extend("@lower")
                else:
                    _lower = None
                _c_tmp = el.find("stiffness")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1e8
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("stiffness")
                    _stiffness = _val
                else:
                    _stiffness = None
                if _stiffness is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
                _raw_upper = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("upper")
                    if _c_tmp is not None: _raw_upper = _c_tmp.text
                else:
                    _raw_upper = el.get("upper")
                if _raw_upper is not None:
                    _upper = _parse_double(_raw_upper)
                    if isinstance(_upper, SDFError):
                        return _upper.extend("@upper")
                else:
                    _upper = None
                _raw_velocity = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("velocity")
                    if _c_tmp is not None: _raw_velocity = _c_tmp.text
                else:
                    _raw_velocity = el.get("velocity")
                if _raw_velocity is not None:
                    _velocity = _parse_double(_raw_velocity)
                    if isinstance(_velocity, SDFError):
                        return _velocity.extend("@velocity")
                else:
                    _velocity = None
                return cls(sdf_version=version, dissipation=_dissipation, effort=_effort, lower=_lower, stiffness=_stiffness, upper=_upper, velocity=_velocity)

        class Xyz(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                expressed_in: str | None = None,
                xyz: _Vector3T | None = None
            ):
                super().__init__(sdf_version)
                self.expressed_in = expressed_in
                self.xyz = _vector3(xyz) if xyz is not None else None

            def to_version(self, target_version: str) -> "Joint.Axis.Xyz":
                if self.expressed_in is not None and cmp_version(target_version, "1.7") < 0:
                    raise ValueError(f"'expressed_in' is not supported in SDF version {target_version} (added in 1.7)")
                if self.xyz is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs: dict = {"sdf_version": target_version, "expressed_in": self.expressed_in, "xyz": self.xyz}
                return Joint.Axis.Xyz(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("xyz")
                if self.expressed_in is not None:
                    el.set("expressed_in", self.expressed_in)
                if self.xyz is not None:
                    el.text = str(self.xyz)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Axis.Xyz | SDFError":
                _raw_expressed_in = el.get("expressed_in")
                if _raw_expressed_in is not None:
                    _expressed_in = _raw_expressed_in
                    if isinstance(_expressed_in, SDFError):
                        return _expressed_in.extend("@expressed_in")
                else:
                    _expressed_in = None
                if _expressed_in is not None and cmp_version(version, "1.7") < 0:
                    if _expressed_in != None:
                        return SDFError(f"'expressed_in' is not supported in SDF version {version} (added in 1.7)")
                _raw_xyz = el.text
                if _raw_xyz is not None:
                    _xyz = _parse_vector3(_raw_xyz)
                    if isinstance(_xyz, SDFError):
                        return _xyz
                else:
                    _xyz = None
                if _xyz is not None and cmp_version(version, "1.2") < 0:
                    if _xyz != "0 0 1":
                        return SDFError(f"'xyz' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, expressed_in=_expressed_in, xyz=_xyz)

        _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

        def __init__(
            self,
            sdf_version: str | None = None,
            dynamics: "Joint.Axis.Dynamics" = None,
            initial_position: float | None = None,
            limit: "Joint.Axis.Limit" = None,
            mimic: "Mimic" = None,
            use_parent_model_frame: bool | None = None,
            xyz: _Vector3T | None = None
        ):
            super().__init__(sdf_version)
            self.dynamics = dynamics
            self.initial_position = initial_position
            self.limit = limit
            self.mimic = mimic
            self.use_parent_model_frame = use_parent_model_frame
            self.xyz = _vector3(xyz) if xyz is not None else None
            if self.dynamics is not None and hasattr(self.dynamics, 'to_version'):
                if getattr(self.dynamics, 'sdfversion', None) is None:
                    self.dynamics.sdfversion = self.sdfversion
                elif getattr(self.dynamics, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.dynamics = self.dynamics.to_version(self.sdfversion)
            if self.limit is not None and hasattr(self.limit, 'to_version'):
                if getattr(self.limit, 'sdfversion', None) is None:
                    self.limit.sdfversion = self.sdfversion
                elif getattr(self.limit, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.limit = self.limit.to_version(self.sdfversion)
            if self.mimic is not None and hasattr(self.mimic, 'to_version'):
                if getattr(self.mimic, 'sdfversion', None) is None:
                    self.mimic.sdfversion = self.sdfversion
                elif getattr(self.mimic, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.mimic = self.mimic.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Joint.Axis":
            from ..elements.mimic import Mimic
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
            kwargs: dict = {"sdf_version": target_version, "dynamics": self.dynamics.to_version(target_version) if self.dynamics is not None and hasattr(self.dynamics, "to_version") else self.dynamics, "initial_position": self.initial_position, "limit": self.limit.to_version(target_version) if self.limit is not None and hasattr(self.limit, "to_version") else self.limit, "mimic": self.mimic.to_version(target_version) if self.mimic is not None and hasattr(self.mimic, "to_version") else self.mimic, "use_parent_model_frame": self.use_parent_model_frame, "xyz": self.xyz}
            new_obj = Joint.Axis(**kwargs)
            apply_migrations(new_obj, target_version)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.mimic import Mimic
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("axis")
            if self.dynamics is not None:
                _child_res = self.dynamics.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('dynamics')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.initial_position is not None:
                _c_tmp = ET.Element("initial_position")
                _c_tmp.text = str(self.initial_position)
                el.append(_c_tmp)
            if self.limit is not None:
                _child_res = self.limit.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('limit')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.mimic is not None:
                _child_res = self.mimic.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('mimic')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.use_parent_model_frame is not None:
                _c_tmp = ET.Element("use_parent_model_frame")
                _c_tmp.text = str(self.use_parent_model_frame).lower()
                el.append(_c_tmp)
            if self.xyz is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("xyz")
                    _c_tmp.text = str(self.xyz)
                    el.append(_c_tmp)
                else:
                    el.set("xyz", str(self.xyz))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Axis | SDFError":
            from ..elements.mimic import Mimic
            _c_dynamics = el.find("dynamics")
            if _c_dynamics is not None:
                _res = cls.Dynamics._from_sdf(_c_dynamics, version)
                if isinstance(_res, SDFError):
                    return _res.extend("dynamics")
                _dynamics = _res
            else:
                _dynamics = None
            _c_tmp = el.find("initial_position")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("initial_position")
                _initial_position = _val
            else:
                _initial_position = None
            if _initial_position is not None and cmp_version(version, "1.6") < 0:
                return SDFError(f"'initial_position' is not supported in SDF version {version} (added in 1.6)")
            _c_limit = el.find("limit")
            if _c_limit is not None:
                _res = cls.Limit._from_sdf(_c_limit, version)
                if isinstance(_res, SDFError):
                    return _res.extend("limit")
                _limit = _res
            else:
                _limit = None
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
            _c_tmp = el.find("use_parent_model_frame")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else False
                _val = str(_text).strip().lower() == 'true'
                if isinstance(_val, SDFError):
                    return _val.extend("use_parent_model_frame")
                _use_parent_model_frame = _val
            else:
                _use_parent_model_frame = None
            if _use_parent_model_frame is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'use_parent_model_frame' is not supported in SDF version {version} (added in 1.5)")
            _raw_xyz = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("xyz")
                if _c_tmp is not None: _raw_xyz = _c_tmp.text
            else:
                _raw_xyz = el.get("xyz")
            if _raw_xyz is not None:
                _xyz = _parse_vector3(_raw_xyz)
                if isinstance(_xyz, SDFError):
                    return _xyz.extend("@xyz")
            else:
                _xyz = None
            return cls(sdf_version=version, dynamics=_dynamics, initial_position=_initial_position, limit=_limit, mimic=_mimic, use_parent_model_frame=_use_parent_model_frame, xyz=_xyz)

    class Axis2(BaseModel):
        class Axis2Limit(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                dissipation: float | None = None,
                effort: float | None = None,
                lower: float | None = None,
                stiffness: float | None = None,
                upper: float | None = None,
                velocity: float | None = None
            ):
                super().__init__(sdf_version)
                self.dissipation = dissipation
                self.effort = effort
                self.lower = lower
                self.stiffness = stiffness
                self.upper = upper
                self.velocity = velocity

            def to_version(self, target_version: str) -> "Joint.Axis2.Axis2Limit":
                if self.dissipation is not None and cmp_version(target_version, "1.4") < 0:
                    raise ValueError(f"'dissipation' is not supported in SDF version {target_version} (added in 1.4)")
                if self.stiffness is not None and cmp_version(target_version, "1.4") < 0:
                    raise ValueError(f"'stiffness' is not supported in SDF version {target_version} (added in 1.4)")
                kwargs: dict = {"sdf_version": target_version, "dissipation": self.dissipation, "effort": self.effort, "lower": self.lower, "stiffness": self.stiffness, "upper": self.upper, "velocity": self.velocity}
                return Joint.Axis2.Axis2Limit(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("limit")
                if self.dissipation is not None:
                    _c_tmp = ET.Element("dissipation")
                    _c_tmp.text = str(self.dissipation)
                    el.append(_c_tmp)
                if self.effort is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("effort")
                        _c_tmp.text = str(self.effort)
                        el.append(_c_tmp)
                    else:
                        el.set("effort", str(self.effort))
                if self.lower is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("lower")
                        _c_tmp.text = str(self.lower)
                        el.append(_c_tmp)
                    else:
                        el.set("lower", str(self.lower))
                if self.stiffness is not None:
                    _c_tmp = ET.Element("stiffness")
                    _c_tmp.text = str(self.stiffness)
                    el.append(_c_tmp)
                if self.upper is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("upper")
                        _c_tmp.text = str(self.upper)
                        el.append(_c_tmp)
                    else:
                        el.set("upper", str(self.upper))
                if self.velocity is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("velocity")
                        _c_tmp.text = str(self.velocity)
                        el.append(_c_tmp)
                    else:
                        el.set("velocity", str(self.velocity))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Axis2.Axis2Limit | SDFError":
                _c_tmp = el.find("dissipation")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("dissipation")
                    _dissipation = _val
                else:
                    _dissipation = None
                if _dissipation is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
                _raw_effort = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("effort")
                    if _c_tmp is not None: _raw_effort = _c_tmp.text
                else:
                    _raw_effort = el.get("effort")
                if _raw_effort is not None:
                    _effort = _parse_double(_raw_effort)
                    if isinstance(_effort, SDFError):
                        return _effort.extend("@effort")
                else:
                    _effort = None
                _raw_lower = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("lower")
                    if _c_tmp is not None: _raw_lower = _c_tmp.text
                else:
                    _raw_lower = el.get("lower")
                if _raw_lower is not None:
                    _lower = _parse_double(_raw_lower)
                    if isinstance(_lower, SDFError):
                        return _lower.extend("@lower")
                else:
                    _lower = None
                _c_tmp = el.find("stiffness")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1e8
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("stiffness")
                    _stiffness = _val
                else:
                    _stiffness = None
                if _stiffness is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
                _raw_upper = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("upper")
                    if _c_tmp is not None: _raw_upper = _c_tmp.text
                else:
                    _raw_upper = el.get("upper")
                if _raw_upper is not None:
                    _upper = _parse_double(_raw_upper)
                    if isinstance(_upper, SDFError):
                        return _upper.extend("@upper")
                else:
                    _upper = None
                _raw_velocity = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("velocity")
                    if _c_tmp is not None: _raw_velocity = _c_tmp.text
                else:
                    _raw_velocity = el.get("velocity")
                if _raw_velocity is not None:
                    _velocity = _parse_double(_raw_velocity)
                    if isinstance(_velocity, SDFError):
                        return _velocity.extend("@velocity")
                else:
                    _velocity = None
                return cls(sdf_version=version, dissipation=_dissipation, effort=_effort, lower=_lower, stiffness=_stiffness, upper=_upper, velocity=_velocity)

        _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

        def __init__(
            self,
            sdf_version: str | None = None,
            dynamics: "Dynamics" = None,
            initial_position: float | None = None,
            limit: "Joint.Axis2.Axis2Limit" = None,
            mimic: "Mimic" = None,
            use_parent_model_frame: bool | None = None,
            xyz: _Vector3T | None = None
        ):
            super().__init__(sdf_version)
            self.dynamics = dynamics
            self.initial_position = initial_position
            self.limit = limit
            self.mimic = mimic
            self.use_parent_model_frame = use_parent_model_frame
            self.xyz = _vector3(xyz) if xyz is not None else None
            if self.dynamics is not None and hasattr(self.dynamics, 'to_version'):
                if getattr(self.dynamics, 'sdfversion', None) is None:
                    self.dynamics.sdfversion = self.sdfversion
                elif getattr(self.dynamics, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.dynamics = self.dynamics.to_version(self.sdfversion)
            if self.limit is not None and hasattr(self.limit, 'to_version'):
                if getattr(self.limit, 'sdfversion', None) is None:
                    self.limit.sdfversion = self.sdfversion
                elif getattr(self.limit, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.limit = self.limit.to_version(self.sdfversion)
            if self.mimic is not None and hasattr(self.mimic, 'to_version'):
                if getattr(self.mimic, 'sdfversion', None) is None:
                    self.mimic.sdfversion = self.sdfversion
                elif getattr(self.mimic, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.mimic = self.mimic.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Joint.Axis2":
            from ..elements.mimic import Mimic
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
            kwargs: dict = {"sdf_version": target_version, "dynamics": self.dynamics.to_version(target_version) if self.dynamics is not None and hasattr(self.dynamics, "to_version") else self.dynamics, "initial_position": self.initial_position, "limit": self.limit.to_version(target_version) if self.limit is not None and hasattr(self.limit, "to_version") else self.limit, "mimic": self.mimic.to_version(target_version) if self.mimic is not None and hasattr(self.mimic, "to_version") else self.mimic, "use_parent_model_frame": self.use_parent_model_frame, "xyz": self.xyz}
            new_obj = Joint.Axis2(**kwargs)
            apply_migrations(new_obj, target_version)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.mimic import Mimic
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("axis2")
            if self.dynamics is not None:
                _child_res = self.dynamics.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('dynamics')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.initial_position is not None:
                _c_tmp = ET.Element("initial_position")
                _c_tmp.text = str(self.initial_position)
                el.append(_c_tmp)
            if self.limit is not None:
                _child_res = self.limit.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('limit')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.mimic is not None:
                _child_res = self.mimic.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('mimic')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.use_parent_model_frame is not None:
                _c_tmp = ET.Element("use_parent_model_frame")
                _c_tmp.text = str(self.use_parent_model_frame).lower()
                el.append(_c_tmp)
            if self.xyz is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("xyz")
                    _c_tmp.text = str(self.xyz)
                    el.append(_c_tmp)
                else:
                    el.set("xyz", str(self.xyz))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Axis2 | SDFError":
            from ..elements.mimic import Mimic
            _c_dynamics = el.find("dynamics")
            if _c_dynamics is not None:
                _res = Dynamics._from_sdf(_c_dynamics, version)
                if isinstance(_res, SDFError):
                    return _res.extend("dynamics")
                _dynamics = _res
            else:
                _dynamics = None
            _c_tmp = el.find("initial_position")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("initial_position")
                _initial_position = _val
            else:
                _initial_position = None
            if _initial_position is not None and cmp_version(version, "1.6") < 0:
                return SDFError(f"'initial_position' is not supported in SDF version {version} (added in 1.6)")
            _c_limit = el.find("limit")
            if _c_limit is not None:
                _res = cls.Axis2Limit._from_sdf(_c_limit, version)
                if isinstance(_res, SDFError):
                    return _res.extend("limit")
                _limit = _res
            else:
                _limit = None
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
            _c_tmp = el.find("use_parent_model_frame")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else False
                _val = str(_text).strip().lower() == 'true'
                if isinstance(_val, SDFError):
                    return _val.extend("use_parent_model_frame")
                _use_parent_model_frame = _val
            else:
                _use_parent_model_frame = None
            if _use_parent_model_frame is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'use_parent_model_frame' is not supported in SDF version {version} (added in 1.5)")
            _raw_xyz = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("xyz")
                if _c_tmp is not None: _raw_xyz = _c_tmp.text
            else:
                _raw_xyz = el.get("xyz")
            if _raw_xyz is not None:
                _xyz = _parse_vector3(_raw_xyz)
                if isinstance(_xyz, SDFError):
                    return _xyz.extend("@xyz")
            else:
                _xyz = None
            return cls(sdf_version=version, dynamics=_dynamics, initial_position=_initial_position, limit=_limit, mimic=_mimic, use_parent_model_frame=_use_parent_model_frame, xyz=_xyz)

    class Child(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            child: str | None = None,
            link: str | None = None
        ):
            super().__init__(sdf_version)
            self.child = child
            self.link = link

        def to_version(self, target_version: str) -> "Joint.Child":
            kwargs: dict = {"sdf_version": target_version, "child": self.child, "link": self.link}
            return Joint.Child(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("child")
            if self.child is not None:
                el.text = self.child
            if self.link is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = self.link
                else:
                    el.set("link", self.link)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Child | SDFError":
            _raw_child = el.text
            if _raw_child is not None:
                _child = _raw_child
                if isinstance(_child, SDFError):
                    return _child
            else:
                _child = None
            _raw_link = None
            if cmp_version(version, "1.2") >= 0:
                _raw_link = el.text
            else:
                _raw_link = el.get("link")
            if _raw_link is not None:
                _link = _raw_link
                if isinstance(_link, SDFError):
                    return _link.extend("@link")
            else:
                _link = None
            return cls(sdf_version=version, child=_child, link=_link)

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Joint.Origin":
            kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
            return Joint.Origin(**kwargs)

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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Origin | SDFError":
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

    class Parent(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            link: str | None = None,
            parent: str | None = None
        ):
            super().__init__(sdf_version)
            self.link = link
            self.parent = parent

        def to_version(self, target_version: str) -> "Joint.Parent":
            kwargs: dict = {"sdf_version": target_version, "link": self.link, "parent": self.parent}
            return Joint.Parent(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("parent")
            if self.link is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = self.link
                else:
                    el.set("link", self.link)
            if self.parent is not None:
                el.text = self.parent
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Parent | SDFError":
            _raw_link = None
            if cmp_version(version, "1.2") >= 0:
                _raw_link = el.text
            else:
                _raw_link = el.get("link")
            if _raw_link is not None:
                _link = _raw_link
                if isinstance(_link, SDFError):
                    return _link.extend("@link")
            else:
                _link = None
            _raw_parent = el.text
            if _raw_parent is not None:
                _parent = _raw_parent
                if isinstance(_parent, SDFError):
                    return _parent
            else:
                _parent = None
            return cls(sdf_version=version, link=_link, parent=_parent)

    class Physics(BaseModel):
        class Ode(BaseModel):
            class OdeLimit(BaseModel):
                def __init__(
                    self,
                    sdf_version: str | None = None,
                    cfm: float | None = None,
                    erp: float | None = None
                ):
                    super().__init__(sdf_version)
                    self.cfm = cfm
                    self.erp = erp

                def to_version(self, target_version: str) -> "Joint.Physics.Ode.OdeLimit":
                    kwargs: dict = {"sdf_version": target_version, "cfm": self.cfm, "erp": self.erp}
                    return Joint.Physics.Ode.OdeLimit(**kwargs)

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.sdfversion is None and version is not None:
                        self.sdfversion = version
                    elif version is not None and version != self.sdfversion:
                        return self.to_version(str(version)).to_sdf(version)
                    if version is None:
                        version = self.sdfversion or "1.12"
                    el = ET.Element("limit")
                    if self.cfm is not None:
                        if cmp_version(version, "1.2") >= 0:
                            _c_tmp = ET.Element("cfm")
                            _c_tmp.text = str(self.cfm)
                            el.append(_c_tmp)
                        else:
                            el.set("cfm", str(self.cfm))
                    if self.erp is not None:
                        if cmp_version(version, "1.2") >= 0:
                            _c_tmp = ET.Element("erp")
                            _c_tmp.text = str(self.erp)
                            el.append(_c_tmp)
                        else:
                            el.set("erp", str(self.erp))
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Physics.Ode.OdeLimit | SDFError":
                    _raw_cfm = None
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = el.find("cfm")
                        if _c_tmp is not None: _raw_cfm = _c_tmp.text
                    else:
                        _raw_cfm = el.get("cfm")
                    if _raw_cfm is not None:
                        _cfm = _parse_double(_raw_cfm)
                        if isinstance(_cfm, SDFError):
                            return _cfm.extend("@cfm")
                    else:
                        _cfm = None
                    _raw_erp = None
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = el.find("erp")
                        if _c_tmp is not None: _raw_erp = _c_tmp.text
                    else:
                        _raw_erp = el.get("erp")
                    if _raw_erp is not None:
                        _erp = _parse_double(_raw_erp)
                        if isinstance(_erp, SDFError):
                            return _erp.extend("@erp")
                    else:
                        _erp = None
                    return cls(sdf_version=version, cfm=_cfm, erp=_erp)

            class Suspension(BaseModel):
                def __init__(
                    self,
                    sdf_version: str | None = None,
                    cfm: float | None = None,
                    erp: float | None = None
                ):
                    super().__init__(sdf_version)
                    self.cfm = cfm
                    self.erp = erp

                def to_version(self, target_version: str) -> "Joint.Physics.Ode.Suspension":
                    kwargs: dict = {"sdf_version": target_version, "cfm": self.cfm, "erp": self.erp}
                    return Joint.Physics.Ode.Suspension(**kwargs)

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.sdfversion is None and version is not None:
                        self.sdfversion = version
                    elif version is not None and version != self.sdfversion:
                        return self.to_version(str(version)).to_sdf(version)
                    if version is None:
                        version = self.sdfversion or "1.12"
                    el = ET.Element("suspension")
                    if self.cfm is not None:
                        if cmp_version(version, "1.2") >= 0:
                            _c_tmp = ET.Element("cfm")
                            _c_tmp.text = str(self.cfm)
                            el.append(_c_tmp)
                        else:
                            el.set("cfm", str(self.cfm))
                    if self.erp is not None:
                        if cmp_version(version, "1.2") >= 0:
                            _c_tmp = ET.Element("erp")
                            _c_tmp.text = str(self.erp)
                            el.append(_c_tmp)
                        else:
                            el.set("erp", str(self.erp))
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Physics.Ode.Suspension | SDFError":
                    _raw_cfm = None
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = el.find("cfm")
                        if _c_tmp is not None: _raw_cfm = _c_tmp.text
                    else:
                        _raw_cfm = el.get("cfm")
                    if _raw_cfm is not None:
                        _cfm = _parse_double(_raw_cfm)
                        if isinstance(_cfm, SDFError):
                            return _cfm.extend("@cfm")
                    else:
                        _cfm = None
                    _raw_erp = None
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = el.find("erp")
                        if _c_tmp is not None: _raw_erp = _c_tmp.text
                    else:
                        _raw_erp = el.get("erp")
                    if _raw_erp is not None:
                        _erp = _parse_double(_raw_erp)
                        if isinstance(_erp, SDFError):
                            return _erp.extend("@erp")
                    else:
                        _erp = None
                    return cls(sdf_version=version, cfm=_cfm, erp=_erp)

            def __init__(
                self,
                sdf_version: str | None = None,
                bounce: float | None = None,
                cfm: float | None = None,
                cfm_damping: bool | None = None,
                erp: float | None = None,
                fudge_factor: float | None = None,
                implicit_spring_damper: bool | None = None,
                limit: "Joint.Physics.Ode.OdeLimit" = None,
                max_force: float | None = None,
                provide_feedback: bool | None = None,
                suspension: "Joint.Physics.Ode.Suspension" = None,
                velocity: float | None = None
            ):
                super().__init__(sdf_version)
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
                if self.limit is not None and hasattr(self.limit, 'to_version'):
                    if getattr(self.limit, 'sdfversion', None) is None:
                        self.limit.sdfversion = self.sdfversion
                    elif getattr(self.limit, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.limit = self.limit.to_version(self.sdfversion)
                if self.suspension is not None and hasattr(self.suspension, 'to_version'):
                    if getattr(self.suspension, 'sdfversion', None) is None:
                        self.suspension.sdfversion = self.sdfversion
                    elif getattr(self.suspension, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.suspension = self.suspension.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "Joint.Physics.Ode":
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
                kwargs: dict = {"sdf_version": target_version, "bounce": self.bounce, "cfm": self.cfm, "cfm_damping": self.cfm_damping, "erp": self.erp, "fudge_factor": self.fudge_factor, "implicit_spring_damper": self.implicit_spring_damper, "limit": self.limit.to_version(target_version) if self.limit is not None and hasattr(self.limit, "to_version") else self.limit, "max_force": self.max_force, "provide_feedback": self.provide_feedback, "suspension": self.suspension.to_version(target_version) if self.suspension is not None and hasattr(self.suspension, "to_version") else self.suspension, "velocity": self.velocity}
                return Joint.Physics.Ode(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("ode")
                if self.bounce is not None:
                    _c_tmp = ET.Element("bounce")
                    _c_tmp.text = str(self.bounce)
                    el.append(_c_tmp)
                if self.cfm is not None:
                    _c_tmp = ET.Element("cfm")
                    _c_tmp.text = str(self.cfm)
                    el.append(_c_tmp)
                if self.cfm_damping is not None:
                    _c_tmp = ET.Element("cfm_damping")
                    _c_tmp.text = str(self.cfm_damping).lower()
                    el.append(_c_tmp)
                if self.erp is not None:
                    _c_tmp = ET.Element("erp")
                    _c_tmp.text = str(self.erp)
                    el.append(_c_tmp)
                if self.fudge_factor is not None:
                    _c_tmp = ET.Element("fudge_factor")
                    _c_tmp.text = str(self.fudge_factor)
                    el.append(_c_tmp)
                if self.implicit_spring_damper is not None:
                    _c_tmp = ET.Element("implicit_spring_damper")
                    _c_tmp.text = str(self.implicit_spring_damper).lower()
                    el.append(_c_tmp)
                if self.limit is not None:
                    _child_res = self.limit.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('limit')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                if self.max_force is not None:
                    _c_tmp = ET.Element("max_force")
                    _c_tmp.text = str(self.max_force)
                    el.append(_c_tmp)
                if self.provide_feedback is not None:
                    _c_tmp = ET.Element("provide_feedback")
                    _c_tmp.text = str(self.provide_feedback).lower()
                    el.append(_c_tmp)
                if self.suspension is not None:
                    _child_res = self.suspension.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('suspension')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                if self.velocity is not None:
                    _c_tmp = ET.Element("velocity")
                    _c_tmp.text = str(self.velocity)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Physics.Ode | SDFError":
                _c_tmp = el.find("bounce")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("bounce")
                    _bounce = _val
                else:
                    _bounce = None
                _c_tmp = el.find("cfm")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("cfm")
                    _cfm = _val
                else:
                    _cfm = None
                _c_tmp = el.find("cfm_damping")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else False
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("cfm_damping")
                    _cfm_damping = _val
                else:
                    _cfm_damping = None
                if _cfm_damping is not None and cmp_version(version, "1.3") < 0:
                    return SDFError(f"'cfm_damping' is not supported in SDF version {version} (added in 1.3)")
                _c_tmp = el.find("erp")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.2
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("erp")
                    _erp = _val
                else:
                    _erp = None
                if _erp is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'erp' is not supported in SDF version {version} (added in 1.4)")
                _c_tmp = el.find("fudge_factor")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("fudge_factor")
                    _fudge_factor = _val
                else:
                    _fudge_factor = None
                _c_tmp = el.find("implicit_spring_damper")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else False
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("implicit_spring_damper")
                    _implicit_spring_damper = _val
                else:
                    _implicit_spring_damper = None
                if _implicit_spring_damper is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'implicit_spring_damper' is not supported in SDF version {version} (added in 1.4)")
                _c_limit = el.find("limit")
                if _c_limit is not None:
                    _res = cls.OdeLimit._from_sdf(_c_limit, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("limit")
                    _limit = _res
                else:
                    _limit = None
                _c_tmp = el.find("max_force")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("max_force")
                    _max_force = _val
                else:
                    _max_force = None
                _c_tmp = el.find("provide_feedback")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else False
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("provide_feedback")
                    _provide_feedback = _val
                else:
                    _provide_feedback = None
                if _provide_feedback is not None and cmp_version(version, "1.3") < 0:
                    return SDFError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.3)")
                _c_suspension = el.find("suspension")
                if _c_suspension is not None:
                    _res = cls.Suspension._from_sdf(_c_suspension, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("suspension")
                    _suspension = _res
                else:
                    _suspension = None
                _c_tmp = el.find("velocity")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("velocity")
                    _velocity = _val
                else:
                    _velocity = None
                return cls(sdf_version=version, bounce=_bounce, cfm=_cfm, cfm_damping=_cfm_damping, erp=_erp, fudge_factor=_fudge_factor, implicit_spring_damper=_implicit_spring_damper, limit=_limit, max_force=_max_force, provide_feedback=_provide_feedback, suspension=_suspension, velocity=_velocity)

        class Simbody(BaseModel):
            def __init__(self, sdf_version: str | None = None, must_be_loop_joint: bool | None = None):
                super().__init__(sdf_version)
                self.must_be_loop_joint = must_be_loop_joint

            def to_version(self, target_version: str) -> "Joint.Physics.Simbody":
                kwargs: dict = {"sdf_version": target_version, "must_be_loop_joint": self.must_be_loop_joint}
                return Joint.Physics.Simbody(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("simbody")
                if self.must_be_loop_joint is not None:
                    _c_tmp = ET.Element("must_be_loop_joint")
                    _c_tmp.text = str(self.must_be_loop_joint).lower()
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Physics.Simbody | SDFError":
                _c_tmp = el.find("must_be_loop_joint")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else False
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("must_be_loop_joint")
                    _must_be_loop_joint = _val
                else:
                    _must_be_loop_joint = None
                return cls(sdf_version=version, must_be_loop_joint=_must_be_loop_joint)

        _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

        def __init__(
            self,
            sdf_version: str | None = None,
            ode: "Joint.Physics.Ode" = None,
            provide_feedback: bool | None = None,
            simbody: "Joint.Physics.Simbody" = None
        ):
            super().__init__(sdf_version)
            self.ode = ode
            self.provide_feedback = provide_feedback
            self.simbody = simbody
            if self.ode is not None and hasattr(self.ode, 'to_version'):
                if getattr(self.ode, 'sdfversion', None) is None:
                    self.ode.sdfversion = self.sdfversion
                elif getattr(self.ode, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.ode = self.ode.to_version(self.sdfversion)
            if self.simbody is not None and hasattr(self.simbody, 'to_version'):
                if getattr(self.simbody, 'sdfversion', None) is None:
                    self.simbody.sdfversion = self.sdfversion
                elif getattr(self.simbody, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.simbody = self.simbody.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Joint.Physics":
            if self.provide_feedback is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.4)")
            if self.simbody is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'simbody' is not supported in SDF version {target_version} (added in 1.4)")
            kwargs: dict = {"sdf_version": target_version, "ode": self.ode.to_version(target_version) if self.ode is not None and hasattr(self.ode, "to_version") else self.ode, "provide_feedback": self.provide_feedback, "simbody": self.simbody.to_version(target_version) if self.simbody is not None and hasattr(self.simbody, "to_version") else self.simbody}
            new_obj = Joint.Physics(**kwargs)
            apply_migrations(new_obj, target_version)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("physics")
            if self.ode is not None:
                _child_res = self.ode.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('ode')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.provide_feedback is not None:
                _c_tmp = ET.Element("provide_feedback")
                _c_tmp.text = str(self.provide_feedback).lower()
                el.append(_c_tmp)
            if self.simbody is not None:
                _child_res = self.simbody.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('simbody')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Joint.Physics | SDFError":
            _c_ode = el.find("ode")
            if _c_ode is not None:
                _res = cls.Ode._from_sdf(_c_ode, version)
                if isinstance(_res, SDFError):
                    return _res.extend("ode")
                _ode = _res
            else:
                _ode = None
            _c_tmp = el.find("provide_feedback")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else False
                _val = str(_text).strip().lower() == 'true'
                if isinstance(_val, SDFError):
                    return _val.extend("provide_feedback")
                _provide_feedback = _val
            else:
                _provide_feedback = None
            if _provide_feedback is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.4)")
            _c_simbody = el.find("simbody")
            if _c_simbody is not None:
                _res = cls.Simbody._from_sdf(_c_simbody, version)
                if isinstance(_res, SDFError):
                    return _res.extend("simbody")
                _simbody = _res
            else:
                _simbody = None
            if _simbody is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'simbody' is not supported in SDF version {version} (added in 1.4)")
            return cls(sdf_version=version, ode=_ode, provide_feedback=_provide_feedback, simbody=_simbody)

    def __init__(
        self,
        sdf_version: str | None = None,
        axis: "Joint.Axis" = None,
        axis2: "Joint.Axis2" = None,
        child: "Joint.Child" = None,
        frames: List["Frame"] = None,
        gearbox_ratio: float | None = None,
        gearbox_reference_body: str | None = None,
        name: str | None = None,
        origin: "Joint.Origin" = None,
        parent: "Joint.Parent" = None,
        physics: "Joint.Physics" = None,
        pose: _PoseT | None = None,
        screw_thread_pitch: float | None = None,
        sensor: "Sensor" = None,
        thread_pitch: float | None = None,
        type: str | None = None
    ):
        super().__init__(sdf_version)
        self.axis = axis
        self.axis2 = axis2
        self.child = child
        self.frames = frames or []
        self.gearbox_ratio = gearbox_ratio
        self.gearbox_reference_body = gearbox_reference_body
        self.name = name
        self.origin = origin
        self.parent = parent
        self.physics = physics
        self.pose = _pose(pose) if pose is not None else None
        self.screw_thread_pitch = screw_thread_pitch
        self.sensor = sensor
        self.thread_pitch = thread_pitch
        self.type = type
        if self.axis is not None and hasattr(self.axis, 'to_version'):
            if getattr(self.axis, 'sdfversion', None) is None:
                self.axis.sdfversion = self.sdfversion
            elif getattr(self.axis, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.axis = self.axis.to_version(self.sdfversion)
        if self.axis2 is not None and hasattr(self.axis2, 'to_version'):
            if getattr(self.axis2, 'sdfversion', None) is None:
                self.axis2.sdfversion = self.sdfversion
            elif getattr(self.axis2, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.axis2 = self.axis2.to_version(self.sdfversion)
        if self.child is not None and hasattr(self.child, 'to_version'):
            if getattr(self.child, 'sdfversion', None) is None:
                self.child.sdfversion = self.sdfversion
            elif getattr(self.child, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.child = self.child.to_version(self.sdfversion)
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
        if self.parent is not None and hasattr(self.parent, 'to_version'):
            if getattr(self.parent, 'sdfversion', None) is None:
                self.parent.sdfversion = self.sdfversion
            elif getattr(self.parent, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.parent = self.parent.to_version(self.sdfversion)
        if self.physics is not None and hasattr(self.physics, 'to_version'):
            if getattr(self.physics, 'sdfversion', None) is None:
                self.physics.sdfversion = self.sdfversion
            elif getattr(self.physics, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.physics = self.physics.to_version(self.sdfversion)
        if self.sensor is not None and hasattr(self.sensor, 'to_version'):
            if getattr(self.sensor, 'sdfversion', None) is None:
                self.sensor.sdfversion = self.sdfversion
            elif getattr(self.sensor, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.sensor = self.sensor.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def to_version(self, target_version: str) -> "Joint":
        from ..elements.frame import Frame
        from ..elements.sensor import Sensor
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
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
        kwargs: dict = {"sdf_version": target_version, "axis": self.axis.to_version(target_version) if self.axis is not None and hasattr(self.axis, "to_version") else self.axis, "axis2": self.axis2.to_version(target_version) if self.axis2 is not None and hasattr(self.axis2, "to_version") else self.axis2, "child": self.child.to_version(target_version) if self.child is not None and hasattr(self.child, "to_version") else self.child, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "gearbox_ratio": self.gearbox_ratio, "gearbox_reference_body": self.gearbox_reference_body, "name": self.name, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "parent": self.parent.to_version(target_version) if self.parent is not None and hasattr(self.parent, "to_version") else self.parent, "physics": self.physics.to_version(target_version) if self.physics is not None and hasattr(self.physics, "to_version") else self.physics, "pose": self.pose, "screw_thread_pitch": self.screw_thread_pitch, "sensor": self.sensor.to_version(target_version) if self.sensor is not None and hasattr(self.sensor, "to_version") else self.sensor, "thread_pitch": self.thread_pitch, "type": self.type}
        return Joint(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.sensor import Sensor
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("joint")
        if self.axis is not None:
            _child_res = self.axis.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('axis')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.axis2 is not None:
            _child_res = self.axis2.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('axis2')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.child is not None:
            _child_res = self.child.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('child')
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
        if self.gearbox_ratio is not None:
            _c_tmp = ET.Element("gearbox_ratio")
            _c_tmp.text = str(self.gearbox_ratio)
            el.append(_c_tmp)
        if self.gearbox_reference_body is not None:
            _c_tmp = ET.Element("gearbox_reference_body")
            _c_tmp.text = self.gearbox_reference_body
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
        if self.parent is not None:
            _child_res = self.parent.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('parent')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.physics is not None:
            _child_res = self.physics.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('physics')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = _pose_to_sdf(self.pose, _c_tmp)
            el.append(_c_tmp)
        if self.screw_thread_pitch is not None:
            _c_tmp = ET.Element("screw_thread_pitch")
            _c_tmp.text = str(self.screw_thread_pitch)
            el.append(_c_tmp)
        if self.sensor is not None:
            _child_res = self.sensor.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('sensor')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.thread_pitch is not None:
            _c_tmp = ET.Element("thread_pitch")
            _c_tmp.text = str(self.thread_pitch)
            el.append(_c_tmp)
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Joint | SDFError":
        from ..elements.frame import Frame
        from ..elements.sensor import Sensor
        _c_axis = el.find("axis")
        if _c_axis is not None:
            _res = cls.Axis._from_sdf(_c_axis, version)
            if isinstance(_res, SDFError):
                return _res.extend("axis")
            _axis = _res
        else:
            _axis = None
        _c_axis2 = el.find("axis2")
        if _c_axis2 is not None:
            _res = cls.Axis2._from_sdf(_c_axis2, version)
            if isinstance(_res, SDFError):
                return _res.extend("axis2")
            _axis2 = _res
        else:
            _axis2 = None
        _c_child = el.find("child")
        if _c_child is not None:
            _res = cls.Child._from_sdf(_c_child, version)
            if isinstance(_res, SDFError):
                return _res.extend("child")
            _child = _res
        else:
            _child = None
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _c_tmp = el.find("gearbox_ratio")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("gearbox_ratio")
            _gearbox_ratio = _val
        else:
            _gearbox_ratio = None
        if _gearbox_ratio is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'gearbox_ratio' is not supported in SDF version {version} (added in 1.4)")
        _c_tmp = el.find("gearbox_reference_body")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("gearbox_reference_body")
            _gearbox_reference_body = _val
        else:
            _gearbox_reference_body = None
        if _gearbox_reference_body is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'gearbox_reference_body' is not supported in SDF version {version} (added in 1.4)")
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
        _c_parent = el.find("parent")
        if _c_parent is not None:
            _res = cls.Parent._from_sdf(_c_parent, version)
            if isinstance(_res, SDFError):
                return _res.extend("parent")
            _parent = _res
        else:
            _parent = None
        _c_physics = el.find("physics")
        if _c_physics is not None:
            _res = cls.Physics._from_sdf(_c_physics, version)
            if isinstance(_res, SDFError):
                return _res.extend("physics")
            _physics = _res
        else:
            _physics = None
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
        _c_tmp = el.find("screw_thread_pitch")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("screw_thread_pitch")
            _screw_thread_pitch = _val
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
        _c_tmp = el.find("thread_pitch")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("thread_pitch")
            _thread_pitch = _val
        else:
            _thread_pitch = None
        _raw_type = el.get("type")
        if _raw_type is not None:
            _type = _raw_type
            if isinstance(_type, SDFError):
                return _type.extend("@type")
        else:
            _type = None
        return cls(sdf_version=version, axis=_axis, axis2=_axis2, child=_child, frames=_frames, gearbox_ratio=_gearbox_ratio, gearbox_reference_body=_gearbox_reference_body, name=_name, origin=_origin, parent=_parent, physics=_physics, pose=_pose, screw_thread_pitch=_screw_thread_pitch, sensor=_sensor, thread_pitch=_thread_pitch, type=_type)
