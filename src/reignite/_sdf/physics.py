### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_int32
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Physics(BaseModel):
    class Bullet(BaseModel):
        class Constraints(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                cfm: float | None = None,
                contact_surface_layer: float | None = None,
                erp: float | None = None,
                split_impulse: bool | None = None,
                split_impulse_penetration_threshold: float | None = None
            ):
                super().__init__(sdf_version)
                self.cfm = cfm
                self.contact_surface_layer = contact_surface_layer
                self.erp = erp
                self.split_impulse = split_impulse
                self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

            def to_version(self, target_version: str) -> "Physics.Bullet.Constraints":
                kwargs: dict = {"sdf_version": target_version, "cfm": self.cfm, "contact_surface_layer": self.contact_surface_layer, "erp": self.erp, "split_impulse": self.split_impulse, "split_impulse_penetration_threshold": self.split_impulse_penetration_threshold}
                return Physics.Bullet.Constraints(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("constraints")
                if self.cfm is not None:
                    _c_tmp = ET.Element("cfm")
                    _c_tmp.text = str(self.cfm)
                    el.append(_c_tmp)
                if self.contact_surface_layer is not None:
                    _c_tmp = ET.Element("contact_surface_layer")
                    _c_tmp.text = str(self.contact_surface_layer)
                    el.append(_c_tmp)
                if self.erp is not None:
                    _c_tmp = ET.Element("erp")
                    _c_tmp.text = str(self.erp)
                    el.append(_c_tmp)
                if self.split_impulse is not None:
                    _c_tmp = ET.Element("split_impulse")
                    _c_tmp.text = str(self.split_impulse).lower()
                    el.append(_c_tmp)
                if self.split_impulse_penetration_threshold is not None:
                    _c_tmp = ET.Element("split_impulse_penetration_threshold")
                    _c_tmp.text = str(self.split_impulse_penetration_threshold)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Constraints | SDFError":
                _c_tmp = el.find("cfm")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("cfm")
                    _cfm = _val
                else:
                    _cfm = None
                _c_tmp = el.find("contact_surface_layer")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.001
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("contact_surface_layer")
                    _contact_surface_layer = _val
                else:
                    _contact_surface_layer = None
                _c_tmp = el.find("erp")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.2
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("erp")
                    _erp = _val
                else:
                    _erp = None
                _c_tmp = el.find("split_impulse")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else True
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("split_impulse")
                    _split_impulse = _val
                else:
                    _split_impulse = None
                _c_tmp = el.find("split_impulse_penetration_threshold")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else -0.01
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("split_impulse_penetration_threshold")
                    _split_impulse_penetration_threshold = _val
                else:
                    _split_impulse_penetration_threshold = None
                return cls(sdf_version=version, cfm=_cfm, contact_surface_layer=_contact_surface_layer, erp=_erp, split_impulse=_split_impulse, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)

        class Solver(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                iters: int | None = None,
                min_step_size: float | None = None,
                sor: float | None = None,
                type: str | None = None
            ):
                super().__init__(sdf_version)
                self.iters = iters
                self.min_step_size = min_step_size
                self.sor = sor
                self.type = type

            def to_version(self, target_version: str) -> "Physics.Bullet.Solver":
                kwargs: dict = {"sdf_version": target_version, "iters": self.iters, "min_step_size": self.min_step_size, "sor": self.sor, "type": self.type}
                return Physics.Bullet.Solver(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("solver")
                if self.iters is not None:
                    _c_tmp = ET.Element("iters")
                    _c_tmp.text = str(self.iters)
                    el.append(_c_tmp)
                if self.min_step_size is not None:
                    _c_tmp = ET.Element("min_step_size")
                    _c_tmp.text = str(self.min_step_size)
                    el.append(_c_tmp)
                if self.sor is not None:
                    _c_tmp = ET.Element("sor")
                    _c_tmp.text = str(self.sor)
                    el.append(_c_tmp)
                if self.type is not None:
                    _c_tmp = ET.Element("type")
                    _c_tmp.text = self.type
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Solver | SDFError":
                _c_tmp = el.find("iters")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 50
                    _val = _parse_int32(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("iters")
                    _iters = _val
                else:
                    _iters = None
                _c_tmp = el.find("min_step_size")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0001
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("min_step_size")
                    _min_step_size = _val
                else:
                    _min_step_size = None
                _c_tmp = el.find("sor")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1.3
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("sor")
                    _sor = _val
                else:
                    _sor = None
                _c_tmp = el.find("type")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "sequential_impulse"
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("type")
                    _type = _val
                else:
                    _type = None
                return cls(sdf_version=version, iters=_iters, min_step_size=_min_step_size, sor=_sor, type=_type)

        def __init__(
            self,
            sdf_version: str | None = None,
            constraints: "Physics.Bullet.Constraints" = None,
            dt: float | None = None,
            solver: "Physics.Bullet.Solver" = None
        ):
            super().__init__(sdf_version)
            self.constraints = constraints
            self.dt = dt
            self.solver = solver
            if self.constraints is not None and hasattr(self.constraints, 'to_version'):
                if getattr(self.constraints, 'sdfversion', None) is None:
                    self.constraints.sdfversion = self.sdfversion
                elif getattr(self.constraints, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.constraints = self.constraints.to_version(self.sdfversion)
            if self.solver is not None and hasattr(self.solver, 'to_version'):
                if getattr(self.solver, 'sdfversion', None) is None:
                    self.solver.sdfversion = self.sdfversion
                elif getattr(self.solver, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.solver = self.solver.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Physics.Bullet":
            if self.constraints is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'constraints' is not supported in SDF version {target_version} (added in 1.4)")
            if self.dt is not None and cmp_version(target_version, "1.4") >= 0:
                raise ValueError(f"'dt' is not supported in SDF version {target_version} (removed in 1.4)")
            if self.solver is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'solver' is not supported in SDF version {target_version} (added in 1.4)")
            kwargs: dict = {"sdf_version": target_version, "constraints": self.constraints.to_version(target_version) if self.constraints is not None and hasattr(self.constraints, "to_version") else self.constraints, "dt": self.dt, "solver": self.solver.to_version(target_version) if self.solver is not None and hasattr(self.solver, "to_version") else self.solver}
            return Physics.Bullet(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("bullet")
            if self.constraints is not None:
                _child_res = self.constraints.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('constraints')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.dt is not None:
                _c_tmp = ET.Element("dt")
                _c_tmp.text = str(self.dt)
                el.append(_c_tmp)
            if self.solver is not None:
                _child_res = self.solver.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('solver')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet | SDFError":
            _c_constraints = el.find("constraints")
            if _c_constraints is not None:
                _res = cls.Constraints._from_sdf(_c_constraints, version)
                if isinstance(_res, SDFError):
                    return _res.extend("constraints")
                _constraints = _res
            else:
                _constraints = None
            if _constraints is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'constraints' is not supported in SDF version {version} (added in 1.4)")
            _c_tmp = el.find("dt")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.003
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("dt")
                _dt = _val
            else:
                _dt = None
            _c_solver = el.find("solver")
            if _c_solver is not None:
                _res = cls.Solver._from_sdf(_c_solver, version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            else:
                _solver = None
            if _solver is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'solver' is not supported in SDF version {version} (added in 1.4)")
            return cls(sdf_version=version, constraints=_constraints, dt=_dt, solver=_solver)

    class Dart(BaseModel):
        class DartSolver(BaseModel):
            def __init__(self, sdf_version: str | None = None, solver_type: str | None = None):
                super().__init__(sdf_version)
                self.solver_type = solver_type

            def to_version(self, target_version: str) -> "Physics.Dart.DartSolver":
                kwargs: dict = {"sdf_version": target_version, "solver_type": self.solver_type}
                return Physics.Dart.DartSolver(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("solver")
                if self.solver_type is not None:
                    _c_tmp = ET.Element("solver_type")
                    _c_tmp.text = self.solver_type
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Dart.DartSolver | SDFError":
                _c_tmp = el.find("solver_type")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "dantzig"
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("solver_type")
                    _solver_type = _val
                else:
                    _solver_type = None
                return cls(sdf_version=version, solver_type=_solver_type)

        def __init__(
            self,
            sdf_version: str | None = None,
            collision_detector: str | None = None,
            solver: "Physics.Dart.DartSolver" = None
        ):
            super().__init__(sdf_version)
            self.collision_detector = collision_detector
            self.solver = solver
            if self.solver is not None and hasattr(self.solver, 'to_version'):
                if getattr(self.solver, 'sdfversion', None) is None:
                    self.solver.sdfversion = self.sdfversion
                elif getattr(self.solver, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.solver = self.solver.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Physics.Dart":
            kwargs: dict = {"sdf_version": target_version, "collision_detector": self.collision_detector, "solver": self.solver.to_version(target_version) if self.solver is not None and hasattr(self.solver, "to_version") else self.solver}
            return Physics.Dart(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("dart")
            if self.collision_detector is not None:
                _c_tmp = ET.Element("collision_detector")
                _c_tmp.text = self.collision_detector
                el.append(_c_tmp)
            if self.solver is not None:
                _child_res = self.solver.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('solver')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Dart | SDFError":
            _c_tmp = el.find("collision_detector")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "fcl"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("collision_detector")
                _collision_detector = _val
            else:
                _collision_detector = None
            _c_solver = el.find("solver")
            if _c_solver is not None:
                _res = cls.DartSolver._from_sdf(_c_solver, version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            else:
                _solver = None
            return cls(sdf_version=version, collision_detector=_collision_detector, solver=_solver)

    class Gravity(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            gravity: _Vector3T | None = None,
            xyz: _Vector3T | None = None
        ):
            super().__init__(sdf_version)
            self.gravity = _vector3(gravity) if gravity is not None else None
            self.xyz = _vector3(xyz) if xyz is not None else None

        def to_version(self, target_version: str) -> "Physics.Gravity":
            if self.gravity is not None and cmp_version(target_version, "1.6") >= 0:
                raise ValueError(f"'gravity' is not supported in SDF version {target_version} (removed in 1.6)")
            kwargs: dict = {"sdf_version": target_version, "gravity": self.gravity, "xyz": self.xyz}
            return Physics.Gravity(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("gravity")
            if self.gravity is not None:
                el.text = str(self.gravity)
            if self.xyz is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.xyz)
                else:
                    el.set("xyz", str(self.xyz))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Gravity | SDFError":
            _raw_gravity = el.text
            if _raw_gravity is not None:
                _gravity = _parse_vector3(_raw_gravity)
                if isinstance(_gravity, SDFError):
                    return _gravity
            else:
                _gravity = None
            _raw_xyz = None
            if cmp_version(version, "1.2") >= 0:
                _raw_xyz = el.text
            else:
                _raw_xyz = el.get("xyz")
            if _raw_xyz is not None:
                _xyz = _parse_vector3(_raw_xyz)
                if isinstance(_xyz, SDFError):
                    return _xyz.extend("@xyz")
            else:
                _xyz = None
            return cls(sdf_version=version, gravity=_gravity, xyz=_xyz)

    class Ode(BaseModel):
        class OdeConstraints(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                cfm: float | None = None,
                contact_max_correcting_vel: float | None = None,
                contact_surface_layer: float | None = None,
                erp: float | None = None
            ):
                super().__init__(sdf_version)
                self.cfm = cfm
                self.contact_max_correcting_vel = contact_max_correcting_vel
                self.contact_surface_layer = contact_surface_layer
                self.erp = erp

            def to_version(self, target_version: str) -> "Physics.Ode.OdeConstraints":
                kwargs: dict = {"sdf_version": target_version, "cfm": self.cfm, "contact_max_correcting_vel": self.contact_max_correcting_vel, "contact_surface_layer": self.contact_surface_layer, "erp": self.erp}
                return Physics.Ode.OdeConstraints(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("constraints")
                if self.cfm is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("cfm")
                        _c_tmp.text = str(self.cfm)
                        el.append(_c_tmp)
                    else:
                        el.set("cfm", str(self.cfm))
                if self.contact_max_correcting_vel is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("contact_max_correcting_vel")
                        _c_tmp.text = str(self.contact_max_correcting_vel)
                        el.append(_c_tmp)
                    else:
                        el.set("contact_max_correcting_vel", str(self.contact_max_correcting_vel))
                if self.contact_surface_layer is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("contact_surface_layer")
                        _c_tmp.text = str(self.contact_surface_layer)
                        el.append(_c_tmp)
                    else:
                        el.set("contact_surface_layer", str(self.contact_surface_layer))
                if self.erp is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("erp")
                        _c_tmp.text = str(self.erp)
                        el.append(_c_tmp)
                    else:
                        el.set("erp", str(self.erp))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeConstraints | SDFError":
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
                _raw_contact_max_correcting_vel = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("contact_max_correcting_vel")
                    if _c_tmp is not None: _raw_contact_max_correcting_vel = _c_tmp.text
                else:
                    _raw_contact_max_correcting_vel = el.get("contact_max_correcting_vel")
                if _raw_contact_max_correcting_vel is not None:
                    _contact_max_correcting_vel = _parse_double(_raw_contact_max_correcting_vel)
                    if isinstance(_contact_max_correcting_vel, SDFError):
                        return _contact_max_correcting_vel.extend("@contact_max_correcting_vel")
                else:
                    _contact_max_correcting_vel = None
                _raw_contact_surface_layer = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("contact_surface_layer")
                    if _c_tmp is not None: _raw_contact_surface_layer = _c_tmp.text
                else:
                    _raw_contact_surface_layer = el.get("contact_surface_layer")
                if _raw_contact_surface_layer is not None:
                    _contact_surface_layer = _parse_double(_raw_contact_surface_layer)
                    if isinstance(_contact_surface_layer, SDFError):
                        return _contact_surface_layer.extend("@contact_surface_layer")
                else:
                    _contact_surface_layer = None
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
                return cls(sdf_version=version, cfm=_cfm, contact_max_correcting_vel=_contact_max_correcting_vel, contact_surface_layer=_contact_surface_layer, erp=_erp)

        class OdeSolver(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                dt: float | None = None,
                friction_model: str | None = None,
                island_threads: int | None = None,
                iters: int | None = None,
                min_step_size: float | None = None,
                precon_iters: int | None = None,
                sor: float | None = None,
                thread_position_correction: bool | None = None,
                type: str | None = None,
                use_dynamic_moi_rescaling: bool | None = None
            ):
                super().__init__(sdf_version)
                self.dt = dt
                self.friction_model = friction_model
                self.island_threads = island_threads
                self.iters = iters
                self.min_step_size = min_step_size
                self.precon_iters = precon_iters
                self.sor = sor
                self.thread_position_correction = thread_position_correction
                self.type = type
                self.use_dynamic_moi_rescaling = use_dynamic_moi_rescaling

            def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver":
                if self.friction_model is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'friction_model' is not supported in SDF version {target_version} (added in 1.6)")
                if self.island_threads is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'island_threads' is not supported in SDF version {target_version} (added in 1.6)")
                if self.min_step_size is not None and cmp_version(target_version, "1.4") < 0:
                    raise ValueError(f"'min_step_size' is not supported in SDF version {target_version} (added in 1.4)")
                if self.thread_position_correction is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'thread_position_correction' is not supported in SDF version {target_version} (added in 1.6)")
                if self.use_dynamic_moi_rescaling is not None and cmp_version(target_version, "1.4") < 0:
                    raise ValueError(f"'use_dynamic_moi_rescaling' is not supported in SDF version {target_version} (added in 1.4)")
                kwargs: dict = {"sdf_version": target_version, "dt": self.dt, "friction_model": self.friction_model, "island_threads": self.island_threads, "iters": self.iters, "min_step_size": self.min_step_size, "precon_iters": self.precon_iters, "sor": self.sor, "thread_position_correction": self.thread_position_correction, "type": self.type, "use_dynamic_moi_rescaling": self.use_dynamic_moi_rescaling}
                return Physics.Ode.OdeSolver(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("solver")
                if self.dt is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("dt")
                        _c_tmp.text = str(self.dt)
                        el.append(_c_tmp)
                    else:
                        el.set("dt", str(self.dt))
                if self.friction_model is not None:
                    _c_tmp = ET.Element("friction_model")
                    _c_tmp.text = self.friction_model
                    el.append(_c_tmp)
                if self.island_threads is not None:
                    _c_tmp = ET.Element("island_threads")
                    _c_tmp.text = str(self.island_threads)
                    el.append(_c_tmp)
                if self.iters is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("iters")
                        _c_tmp.text = str(self.iters)
                        el.append(_c_tmp)
                    else:
                        el.set("iters", str(self.iters))
                if self.min_step_size is not None:
                    _c_tmp = ET.Element("min_step_size")
                    _c_tmp.text = str(self.min_step_size)
                    el.append(_c_tmp)
                if self.precon_iters is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("precon_iters")
                        _c_tmp.text = str(self.precon_iters)
                        el.append(_c_tmp)
                    else:
                        el.set("precon_iters", str(self.precon_iters))
                if self.sor is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("sor")
                        _c_tmp.text = str(self.sor)
                        el.append(_c_tmp)
                    else:
                        el.set("sor", str(self.sor))
                if self.thread_position_correction is not None:
                    _c_tmp = ET.Element("thread_position_correction")
                    _c_tmp.text = str(self.thread_position_correction).lower()
                    el.append(_c_tmp)
                if self.type is not None:
                    if cmp_version(version, "1.2") >= 0:
                        _c_tmp = ET.Element("type")
                        _c_tmp.text = self.type
                        el.append(_c_tmp)
                    else:
                        el.set("type", self.type)
                if self.use_dynamic_moi_rescaling is not None:
                    _c_tmp = ET.Element("use_dynamic_moi_rescaling")
                    _c_tmp.text = str(self.use_dynamic_moi_rescaling).lower()
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver | SDFError":
                _raw_dt = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("dt")
                    if _c_tmp is not None: _raw_dt = _c_tmp.text
                else:
                    _raw_dt = el.get("dt")
                if _raw_dt is not None:
                    _dt = _parse_double(_raw_dt)
                    if isinstance(_dt, SDFError):
                        return _dt.extend("@dt")
                else:
                    _dt = None
                _c_tmp = el.find("friction_model")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "pyramid_model"
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("friction_model")
                    _friction_model = _val
                else:
                    _friction_model = None
                if _friction_model is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'friction_model' is not supported in SDF version {version} (added in 1.6)")
                _c_tmp = el.find("island_threads")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_int32(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("island_threads")
                    _island_threads = _val
                else:
                    _island_threads = None
                if _island_threads is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'island_threads' is not supported in SDF version {version} (added in 1.6)")
                _raw_iters = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("iters")
                    if _c_tmp is not None: _raw_iters = _c_tmp.text
                else:
                    _raw_iters = el.get("iters")
                if _raw_iters is not None:
                    _iters = _parse_int32(_raw_iters)
                    if isinstance(_iters, SDFError):
                        return _iters.extend("@iters")
                else:
                    _iters = None
                _c_tmp = el.find("min_step_size")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0001
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("min_step_size")
                    _min_step_size = _val
                else:
                    _min_step_size = None
                if _min_step_size is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'min_step_size' is not supported in SDF version {version} (added in 1.4)")
                _raw_precon_iters = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("precon_iters")
                    if _c_tmp is not None: _raw_precon_iters = _c_tmp.text
                else:
                    _raw_precon_iters = el.get("precon_iters")
                if _raw_precon_iters is not None:
                    _precon_iters = _parse_int32(_raw_precon_iters)
                    if isinstance(_precon_iters, SDFError):
                        return _precon_iters.extend("@precon_iters")
                else:
                    _precon_iters = None
                _raw_sor = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("sor")
                    if _c_tmp is not None: _raw_sor = _c_tmp.text
                else:
                    _raw_sor = el.get("sor")
                if _raw_sor is not None:
                    _sor = _parse_double(_raw_sor)
                    if isinstance(_sor, SDFError):
                        return _sor.extend("@sor")
                else:
                    _sor = None
                _c_tmp = el.find("thread_position_correction")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else False
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("thread_position_correction")
                    _thread_position_correction = _val
                else:
                    _thread_position_correction = None
                if _thread_position_correction is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'thread_position_correction' is not supported in SDF version {version} (added in 1.6)")
                _raw_type = None
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = el.find("type")
                    if _c_tmp is not None: _raw_type = _c_tmp.text
                else:
                    _raw_type = el.get("type")
                if _raw_type is not None:
                    _type = _raw_type
                    if isinstance(_type, SDFError):
                        return _type.extend("@type")
                else:
                    _type = None
                _c_tmp = el.find("use_dynamic_moi_rescaling")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else False
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("use_dynamic_moi_rescaling")
                    _use_dynamic_moi_rescaling = _val
                else:
                    _use_dynamic_moi_rescaling = None
                if _use_dynamic_moi_rescaling is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'use_dynamic_moi_rescaling' is not supported in SDF version {version} (added in 1.4)")
                return cls(sdf_version=version, dt=_dt, friction_model=_friction_model, island_threads=_island_threads, iters=_iters, min_step_size=_min_step_size, precon_iters=_precon_iters, sor=_sor, thread_position_correction=_thread_position_correction, type=_type, use_dynamic_moi_rescaling=_use_dynamic_moi_rescaling)

        def __init__(
            self,
            sdf_version: str | None = None,
            constraints: "Physics.Ode.OdeConstraints" = None,
            solver: "Physics.Ode.OdeSolver" = None
        ):
            super().__init__(sdf_version)
            self.constraints = constraints
            self.solver = solver
            if self.constraints is not None and hasattr(self.constraints, 'to_version'):
                if getattr(self.constraints, 'sdfversion', None) is None:
                    self.constraints.sdfversion = self.sdfversion
                elif getattr(self.constraints, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.constraints = self.constraints.to_version(self.sdfversion)
            if self.solver is not None and hasattr(self.solver, 'to_version'):
                if getattr(self.solver, 'sdfversion', None) is None:
                    self.solver.sdfversion = self.sdfversion
                elif getattr(self.solver, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.solver = self.solver.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Physics.Ode":
            kwargs: dict = {"sdf_version": target_version, "constraints": self.constraints.to_version(target_version) if self.constraints is not None and hasattr(self.constraints, "to_version") else self.constraints, "solver": self.solver.to_version(target_version) if self.solver is not None and hasattr(self.solver, "to_version") else self.solver}
            return Physics.Ode(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("ode")
            if self.constraints is not None:
                _child_res = self.constraints.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('constraints')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.solver is not None:
                _child_res = self.solver.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('solver')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode | SDFError":
            _c_constraints = el.find("constraints")
            if _c_constraints is not None:
                _res = cls.OdeConstraints._from_sdf(_c_constraints, version)
                if isinstance(_res, SDFError):
                    return _res.extend("constraints")
                _constraints = _res
            else:
                _constraints = None
            _c_solver = el.find("solver")
            if _c_solver is not None:
                _res = cls.OdeSolver._from_sdf(_c_solver, version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            else:
                _solver = None
            return cls(sdf_version=version, constraints=_constraints, solver=_solver)

    class Simbody(BaseModel):
        class Contact(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                dissipation: float | None = None,
                dynamic_friction: float | None = None,
                override_impact_capture_velocity: float | None = None,
                override_stiction_transition_velocity: float | None = None,
                plastic_coef_restitution: float | None = None,
                plastic_impact_velocity: float | None = None,
                static_friction: float | None = None,
                stiffness: float | None = None,
                viscous_friction: float | None = None
            ):
                super().__init__(sdf_version)
                self.dissipation = dissipation
                self.dynamic_friction = dynamic_friction
                self.override_impact_capture_velocity = override_impact_capture_velocity
                self.override_stiction_transition_velocity = override_stiction_transition_velocity
                self.plastic_coef_restitution = plastic_coef_restitution
                self.plastic_impact_velocity = plastic_impact_velocity
                self.static_friction = static_friction
                self.stiffness = stiffness
                self.viscous_friction = viscous_friction

            def to_version(self, target_version: str) -> "Physics.Simbody.Contact":
                kwargs: dict = {"sdf_version": target_version, "dissipation": self.dissipation, "dynamic_friction": self.dynamic_friction, "override_impact_capture_velocity": self.override_impact_capture_velocity, "override_stiction_transition_velocity": self.override_stiction_transition_velocity, "plastic_coef_restitution": self.plastic_coef_restitution, "plastic_impact_velocity": self.plastic_impact_velocity, "static_friction": self.static_friction, "stiffness": self.stiffness, "viscous_friction": self.viscous_friction}
                return Physics.Simbody.Contact(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("contact")
                if self.dissipation is not None:
                    _c_tmp = ET.Element("dissipation")
                    _c_tmp.text = str(self.dissipation)
                    el.append(_c_tmp)
                if self.dynamic_friction is not None:
                    _c_tmp = ET.Element("dynamic_friction")
                    _c_tmp.text = str(self.dynamic_friction)
                    el.append(_c_tmp)
                if self.override_impact_capture_velocity is not None:
                    _c_tmp = ET.Element("override_impact_capture_velocity")
                    _c_tmp.text = str(self.override_impact_capture_velocity)
                    el.append(_c_tmp)
                if self.override_stiction_transition_velocity is not None:
                    _c_tmp = ET.Element("override_stiction_transition_velocity")
                    _c_tmp.text = str(self.override_stiction_transition_velocity)
                    el.append(_c_tmp)
                if self.plastic_coef_restitution is not None:
                    _c_tmp = ET.Element("plastic_coef_restitution")
                    _c_tmp.text = str(self.plastic_coef_restitution)
                    el.append(_c_tmp)
                if self.plastic_impact_velocity is not None:
                    _c_tmp = ET.Element("plastic_impact_velocity")
                    _c_tmp.text = str(self.plastic_impact_velocity)
                    el.append(_c_tmp)
                if self.static_friction is not None:
                    _c_tmp = ET.Element("static_friction")
                    _c_tmp.text = str(self.static_friction)
                    el.append(_c_tmp)
                if self.stiffness is not None:
                    _c_tmp = ET.Element("stiffness")
                    _c_tmp.text = str(self.stiffness)
                    el.append(_c_tmp)
                if self.viscous_friction is not None:
                    _c_tmp = ET.Element("viscous_friction")
                    _c_tmp.text = str(self.viscous_friction)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact | SDFError":
                _c_tmp = el.find("dissipation")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 100
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("dissipation")
                    _dissipation = _val
                else:
                    _dissipation = None
                _c_tmp = el.find("dynamic_friction")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.9
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("dynamic_friction")
                    _dynamic_friction = _val
                else:
                    _dynamic_friction = None
                _c_tmp = el.find("override_impact_capture_velocity")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.001
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("override_impact_capture_velocity")
                    _override_impact_capture_velocity = _val
                else:
                    _override_impact_capture_velocity = None
                _c_tmp = el.find("override_stiction_transition_velocity")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.001
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("override_stiction_transition_velocity")
                    _override_stiction_transition_velocity = _val
                else:
                    _override_stiction_transition_velocity = None
                _c_tmp = el.find("plastic_coef_restitution")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.5
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("plastic_coef_restitution")
                    _plastic_coef_restitution = _val
                else:
                    _plastic_coef_restitution = None
                _c_tmp = el.find("plastic_impact_velocity")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.5
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("plastic_impact_velocity")
                    _plastic_impact_velocity = _val
                else:
                    _plastic_impact_velocity = None
                _c_tmp = el.find("static_friction")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.9
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("static_friction")
                    _static_friction = _val
                else:
                    _static_friction = None
                _c_tmp = el.find("stiffness")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1e8
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("stiffness")
                    _stiffness = _val
                else:
                    _stiffness = None
                _c_tmp = el.find("viscous_friction")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("viscous_friction")
                    _viscous_friction = _val
                else:
                    _viscous_friction = None
                return cls(sdf_version=version, dissipation=_dissipation, dynamic_friction=_dynamic_friction, override_impact_capture_velocity=_override_impact_capture_velocity, override_stiction_transition_velocity=_override_stiction_transition_velocity, plastic_coef_restitution=_plastic_coef_restitution, plastic_impact_velocity=_plastic_impact_velocity, static_friction=_static_friction, stiffness=_stiffness, viscous_friction=_viscous_friction)

        def __init__(
            self,
            sdf_version: str | None = None,
            accuracy: float | None = None,
            contact: "Physics.Simbody.Contact" = None,
            max_transient_velocity: float | None = None,
            min_step_size: float | None = None
        ):
            super().__init__(sdf_version)
            self.accuracy = accuracy
            self.contact = contact
            self.max_transient_velocity = max_transient_velocity
            self.min_step_size = min_step_size
            if self.contact is not None and hasattr(self.contact, 'to_version'):
                if getattr(self.contact, 'sdfversion', None) is None:
                    self.contact.sdfversion = self.sdfversion
                elif getattr(self.contact, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.contact = self.contact.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Physics.Simbody":
            kwargs: dict = {"sdf_version": target_version, "accuracy": self.accuracy, "contact": self.contact.to_version(target_version) if self.contact is not None and hasattr(self.contact, "to_version") else self.contact, "max_transient_velocity": self.max_transient_velocity, "min_step_size": self.min_step_size}
            return Physics.Simbody(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("simbody")
            if self.accuracy is not None:
                _c_tmp = ET.Element("accuracy")
                _c_tmp.text = str(self.accuracy)
                el.append(_c_tmp)
            if self.contact is not None:
                _child_res = self.contact.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('contact')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.max_transient_velocity is not None:
                _c_tmp = ET.Element("max_transient_velocity")
                _c_tmp.text = str(self.max_transient_velocity)
                el.append(_c_tmp)
            if self.min_step_size is not None:
                _c_tmp = ET.Element("min_step_size")
                _c_tmp.text = str(self.min_step_size)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody | SDFError":
            _c_tmp = el.find("accuracy")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 1e-3
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("accuracy")
                _accuracy = _val
            else:
                _accuracy = None
            _c_contact = el.find("contact")
            if _c_contact is not None:
                _res = cls.Contact._from_sdf(_c_contact, version)
                if isinstance(_res, SDFError):
                    return _res.extend("contact")
                _contact = _res
            else:
                _contact = None
            _c_tmp = el.find("max_transient_velocity")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.01
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("max_transient_velocity")
                _max_transient_velocity = _val
            else:
                _max_transient_velocity = None
            _c_tmp = el.find("min_step_size")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0001
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("min_step_size")
                _min_step_size = _val
            else:
                _min_step_size = None
            return cls(sdf_version=version, accuracy=_accuracy, contact=_contact, max_transient_velocity=_max_transient_velocity, min_step_size=_min_step_size)

    _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

    def __init__(
        self,
        sdf_version: str | None = None,
        bullet: "Physics.Bullet" = None,
        dart: "Physics.Dart" = None,
        default: bool | None = None,
        gravity: "Physics.Gravity" = None,
        magnetic_field: _Vector3T | None = None,
        max_contacts: int | None = None,
        max_step_size: float | None = None,
        name: str | None = None,
        ode: "Physics.Ode" = None,
        real_time_factor: float | None = None,
        real_time_update_rate: float | None = None,
        simbody: "Physics.Simbody" = None,
        type: str | None = None,
        update_rate: float | None = None
    ):
        super().__init__(sdf_version)
        self.bullet = bullet
        self.dart = dart
        self.default = default
        self.gravity = gravity
        self.magnetic_field = _vector3(magnetic_field) if magnetic_field is not None else None
        self.max_contacts = max_contacts
        self.max_step_size = max_step_size
        self.name = name
        self.ode = ode
        self.real_time_factor = real_time_factor
        self.real_time_update_rate = real_time_update_rate
        self.simbody = simbody
        self.type = type
        self.update_rate = update_rate
        if self.bullet is not None and hasattr(self.bullet, 'to_version'):
            if getattr(self.bullet, 'sdfversion', None) is None:
                self.bullet.sdfversion = self.sdfversion
            elif getattr(self.bullet, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.bullet = self.bullet.to_version(self.sdfversion)
        if self.dart is not None and hasattr(self.dart, 'to_version'):
            if getattr(self.dart, 'sdfversion', None) is None:
                self.dart.sdfversion = self.sdfversion
            elif getattr(self.dart, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.dart = self.dart.to_version(self.sdfversion)
        if self.gravity is not None and hasattr(self.gravity, 'to_version'):
            if getattr(self.gravity, 'sdfversion', None) is None:
                self.gravity.sdfversion = self.sdfversion
            elif getattr(self.gravity, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.gravity = self.gravity.to_version(self.sdfversion)
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

    def to_version(self, target_version: str) -> "Physics":
        if self.dart is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dart' is not supported in SDF version {target_version} (added in 1.6)")
        if self.default is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'default' is not supported in SDF version {target_version} (added in 1.5)")
        if self.gravity is not None and cmp_version(target_version, "1.6") >= 0:
            raise ValueError(f"'gravity' is not supported in SDF version {target_version} (removed in 1.6)")
        if self.magnetic_field is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (added in 1.5)")
        if self.magnetic_field is not None and cmp_version(target_version, "1.6") >= 0:
            raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (removed in 1.6)")
        if self.max_step_size is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'max_step_size' is not supported in SDF version {target_version} (added in 1.4)")
        if self.name is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.5)")
        if self.real_time_factor is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'real_time_factor' is not supported in SDF version {target_version} (added in 1.4)")
        if self.real_time_update_rate is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'real_time_update_rate' is not supported in SDF version {target_version} (added in 1.4)")
        if self.simbody is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'simbody' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs: dict = {"sdf_version": target_version, "bullet": self.bullet.to_version(target_version) if self.bullet is not None and hasattr(self.bullet, "to_version") else self.bullet, "dart": self.dart.to_version(target_version) if self.dart is not None and hasattr(self.dart, "to_version") else self.dart, "default": self.default, "gravity": self.gravity.to_version(target_version) if self.gravity is not None and hasattr(self.gravity, "to_version") else self.gravity, "magnetic_field": self.magnetic_field, "max_contacts": self.max_contacts, "max_step_size": self.max_step_size, "name": self.name, "ode": self.ode.to_version(target_version) if self.ode is not None and hasattr(self.ode, "to_version") else self.ode, "real_time_factor": self.real_time_factor, "real_time_update_rate": self.real_time_update_rate, "simbody": self.simbody.to_version(target_version) if self.simbody is not None and hasattr(self.simbody, "to_version") else self.simbody, "type": self.type, "update_rate": self.update_rate}
        new_obj = Physics(**kwargs)
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
        if self.bullet is not None:
            _child_res = self.bullet.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('bullet')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.dart is not None:
            _child_res = self.dart.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('dart')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.default is not None:
            el.set("default", str(self.default).lower())
        if self.gravity is not None:
            _child_res = self.gravity.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('gravity')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.magnetic_field is not None:
            _c_tmp = ET.Element("magnetic_field")
            _c_tmp.text = str(self.magnetic_field)
            el.append(_c_tmp)
        if self.max_contacts is not None:
            _c_tmp = ET.Element("max_contacts")
            _c_tmp.text = str(self.max_contacts)
            el.append(_c_tmp)
        if self.max_step_size is not None:
            _c_tmp = ET.Element("max_step_size")
            _c_tmp.text = str(self.max_step_size)
            el.append(_c_tmp)
        if self.name is not None:
            el.set("name", self.name)
        if self.ode is not None:
            _child_res = self.ode.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('ode')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.real_time_factor is not None:
            _c_tmp = ET.Element("real_time_factor")
            _c_tmp.text = str(self.real_time_factor)
            el.append(_c_tmp)
        if self.real_time_update_rate is not None:
            _c_tmp = ET.Element("real_time_update_rate")
            _c_tmp.text = str(self.real_time_update_rate)
            el.append(_c_tmp)
        if self.simbody is not None:
            _child_res = self.simbody.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('simbody')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.type is not None:
            el.set("type", self.type)
        if self.update_rate is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("update_rate")
                _c_tmp.text = str(self.update_rate)
                el.append(_c_tmp)
            else:
                el.set("update_rate", str(self.update_rate))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Physics | SDFError":
        _c_bullet = el.find("bullet")
        if _c_bullet is not None:
            _res = cls.Bullet._from_sdf(_c_bullet, version)
            if isinstance(_res, SDFError):
                return _res.extend("bullet")
            _bullet = _res
        else:
            _bullet = None
        _c_dart = el.find("dart")
        if _c_dart is not None:
            _res = cls.Dart._from_sdf(_c_dart, version)
            if isinstance(_res, SDFError):
                return _res.extend("dart")
            _dart = _res
        else:
            _dart = None
        if _dart is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dart' is not supported in SDF version {version} (added in 1.6)")
        _raw_default = el.get("default")
        if _raw_default is not None:
            _default = str(_raw_default).strip().lower() == 'true'
            if isinstance(_default, SDFError):
                return _default.extend("@default")
        else:
            _default = None
        if _default is not None and cmp_version(version, "1.5") < 0:
            if _default != False:
                return SDFError(f"'default' is not supported in SDF version {version} (added in 1.5)")
        _c_gravity = el.find("gravity")
        if _c_gravity is not None:
            _res = cls.Gravity._from_sdf(_c_gravity, version)
            if isinstance(_res, SDFError):
                return _res.extend("gravity")
            _gravity = _res
        else:
            _gravity = None
        _c_tmp = el.find("magnetic_field")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "5.5645e-6 22.8758e-6 -42.3884e-6"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("magnetic_field")
            _magnetic_field = _val
        else:
            _magnetic_field = None
        if _magnetic_field is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'magnetic_field' is not supported in SDF version {version} (added in 1.5)")
        _c_tmp = el.find("max_contacts")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 20
            _val = _parse_int32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("max_contacts")
            _max_contacts = _val
        else:
            _max_contacts = None
        _c_tmp = el.find("max_step_size")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.001
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("max_step_size")
            _max_step_size = _val
        else:
            _max_step_size = None
        if _max_step_size is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'max_step_size' is not supported in SDF version {version} (added in 1.4)")
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        if _name is not None and cmp_version(version, "1.5") < 0:
            if _name != "default_physics":
                return SDFError(f"'name' is not supported in SDF version {version} (added in 1.5)")
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = cls.Ode._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        _c_tmp = el.find("real_time_factor")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("real_time_factor")
            _real_time_factor = _val
        else:
            _real_time_factor = None
        if _real_time_factor is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'real_time_factor' is not supported in SDF version {version} (added in 1.4)")
        _c_tmp = el.find("real_time_update_rate")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1000
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("real_time_update_rate")
            _real_time_update_rate = _val
        else:
            _real_time_update_rate = None
        if _real_time_update_rate is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'real_time_update_rate' is not supported in SDF version {version} (added in 1.4)")
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
        _raw_type = el.get("type")
        if _raw_type is not None:
            _type = _raw_type
            if isinstance(_type, SDFError):
                return _type.extend("@type")
        else:
            _type = None
        _raw_update_rate = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("update_rate")
            if _c_tmp is not None: _raw_update_rate = _c_tmp.text
        else:
            _raw_update_rate = el.get("update_rate")
        if _raw_update_rate is not None:
            _update_rate = _parse_double(_raw_update_rate)
            if isinstance(_update_rate, SDFError):
                return _update_rate.extend("@update_rate")
        else:
            _update_rate = None
        return cls(sdf_version=version, bullet=_bullet, dart=_dart, default=_default, gravity=_gravity, magnetic_field=_magnetic_field, max_contacts=_max_contacts, max_step_size=_max_step_size, name=_name, ode=_ode, real_time_factor=_real_time_factor, real_time_update_rate=_real_time_update_rate, simbody=_simbody, type=_type, update_rate=_update_rate)
