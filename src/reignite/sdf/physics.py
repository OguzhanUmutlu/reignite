from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model
from ..utils.vector3 import Vector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations


import math

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > math.inf:
        raise ValueError(f"double out of range: {raw}")
    return v



class MaxContacts(Model):
    def __init__(self, sdf_version: str, max_contacts: int = 20):
        self.__version__ = sdf_version
        self.max_contacts = max_contacts

    def to_version(self, target_version: str) -> "MaxContacts":
        kwargs = {"sdf_version": target_version}
        kwargs["max_contacts"] = self.max_contacts
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_contacts")
        if self.max_contacts is not None:
            el.text = str(self.max_contacts)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxContacts":
        _text = el.text or 20
        _max_contacts = _parse_int32(_text)
        return cls(sdf_version=version, max_contacts=_max_contacts)


class Gravity(Model):
    def __init__(self, sdf_version: str, gravity: Vector3 = None, xyz: Vector3 = None):
        self.__version__ = sdf_version
        if gravity is None:
            gravity = Vector3.from_sdf("0 0 -9.8")
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 -9.8")
        self.gravity = gravity
        self.xyz = xyz

    def to_version(self, target_version: str) -> "Gravity":
        kwargs = {"sdf_version": target_version}
        kwargs["gravity"] = self.gravity
        kwargs["xyz"] = self.xyz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gravity")
        if self.gravity is not None:
            el.text = self.gravity.to_sdf()
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gravity":
        _text = el.text or "0 0 -9.8"
        _gravity = Vector3.from_sdf(_text)
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 -9.8"))
        return cls(sdf_version=version, gravity=_gravity, xyz=_xyz)


class Dt(Model):
    def __init__(self, sdf_version: str, dt: float = 0.003):
        self.__version__ = sdf_version
        self.dt = dt

    def to_version(self, target_version: str) -> "Dt":
        kwargs = {"sdf_version": target_version}
        kwargs["dt"] = self.dt
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dt")
        if self.dt is not None:
            el.text = str(self.dt)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Dt":
        _text = el.text or 0.003
        _dt = _parse_double(_text)
        return cls(sdf_version=version, dt=_dt)


class Type(Model):
    def __init__(self, sdf_version: str, type: str = "sequential_impulse"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Type":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Type":
        _text = el.text or "sequential_impulse"
        _type = _text
        return cls(sdf_version=version, type=_type)


class MinStepSize(Model):
    def __init__(self, sdf_version: str, min_step_size: float = 0.0001):
        self.__version__ = sdf_version
        self.min_step_size = min_step_size

    def to_version(self, target_version: str) -> "MinStepSize":
        kwargs = {"sdf_version": target_version}
        kwargs["min_step_size"] = self.min_step_size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_step_size")
        if self.min_step_size is not None:
            el.text = str(self.min_step_size)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinStepSize":
        _text = el.text or 0.0001
        _min_step_size = _parse_double(_text)
        return cls(sdf_version=version, min_step_size=_min_step_size)


class Iters(Model):
    def __init__(self, sdf_version: str, iters: int = 50):
        self.__version__ = sdf_version
        self.iters = iters

    def to_version(self, target_version: str) -> "Iters":
        kwargs = {"sdf_version": target_version}
        kwargs["iters"] = self.iters
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("iters")
        if self.iters is not None:
            el.text = str(self.iters)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Iters":
        _text = el.text or 50
        _iters = _parse_int32(_text)
        return cls(sdf_version=version, iters=_iters)


class Sor(Model):
    def __init__(self, sdf_version: str, sor: float = 1.3):
        self.__version__ = sdf_version
        self.sor = sor

    def to_version(self, target_version: str) -> "Sor":
        kwargs = {"sdf_version": target_version}
        kwargs["sor"] = self.sor
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sor")
        if self.sor is not None:
            el.text = str(self.sor)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sor":
        _text = el.text or 1.3
        _sor = _parse_double(_text)
        return cls(sdf_version=version, sor=_sor)


class Solver(Model):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        min_step_size: "MinStepSize" = None,
        iters: "Iters" = None,
        sor: "Sor" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.min_step_size = min_step_size
        self.iters = iters
        self.sor = sor

    def to_version(self, target_version: str) -> "Solver":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["min_step_size"] = self.min_step_size.to_version(target_version) if self.min_step_size is not None else None
        kwargs["iters"] = self.iters.to_version(target_version) if self.iters is not None else None
        kwargs["sor"] = self.sor.to_version(target_version) if self.sor is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("solver")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.min_step_size is not None:
            el.append(self.min_step_size.to_sdf(version))
        if self.iters is not None:
            el.append(self.iters.to_sdf(version))
        if self.sor is not None:
            el.append(self.sor.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Solver":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type, version) if _c_type is not None else None
        _c_min_step_size = el.find("min_step_size")
        _min_step_size = MinStepSize.from_sdf(_c_min_step_size, version) if _c_min_step_size is not None else None
        _c_iters = el.find("iters")
        _iters = Iters.from_sdf(_c_iters, version) if _c_iters is not None else None
        _c_sor = el.find("sor")
        _sor = Sor.from_sdf(_c_sor, version) if _c_sor is not None else None
        return cls(sdf_version=version, type=_type, min_step_size=_min_step_size, iters=_iters, sor=_sor)


class Cfm(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Cfm":
        _text = el.text or 0
        _cfm = _parse_double(_text)
        return cls(sdf_version=version, cfm=_cfm)


class Erp(Model):
    def __init__(self, sdf_version: str, erp: float = 0.2):
        self.__version__ = sdf_version
        self.erp = erp

    def to_version(self, target_version: str) -> "Erp":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Erp":
        _text = el.text or 0.2
        _erp = _parse_double(_text)
        return cls(sdf_version=version, erp=_erp)


class ContactSurfaceLayer(Model):
    def __init__(self, sdf_version: str, contact_surface_layer: float = 0.001):
        self.__version__ = sdf_version
        self.contact_surface_layer = contact_surface_layer

    def to_version(self, target_version: str) -> "ContactSurfaceLayer":
        kwargs = {"sdf_version": target_version}
        kwargs["contact_surface_layer"] = self.contact_surface_layer
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact_surface_layer")
        if self.contact_surface_layer is not None:
            el.text = str(self.contact_surface_layer)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ContactSurfaceLayer":
        _text = el.text or 0.001
        _contact_surface_layer = _parse_double(_text)
        return cls(sdf_version=version, contact_surface_layer=_contact_surface_layer)


class SplitImpulse(Model):
    def __init__(self, sdf_version: str, split_impulse: bool = True):
        self.__version__ = sdf_version
        self.split_impulse = split_impulse

    def to_version(self, target_version: str) -> "SplitImpulse":
        kwargs = {"sdf_version": target_version}
        kwargs["split_impulse"] = self.split_impulse
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("split_impulse")
        if self.split_impulse is not None:
            el.text = str(self.split_impulse).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SplitImpulse":
        _text = el.text or True
        _split_impulse = _text.strip().lower() == 'true'
        return cls(sdf_version=version, split_impulse=_split_impulse)


class SplitImpulsePenetrationThreshold(Model):
    def __init__(self, sdf_version: str, split_impulse_penetration_threshold: float = -0.01):
        self.__version__ = sdf_version
        self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

    def to_version(self, target_version: str) -> "SplitImpulsePenetrationThreshold":
        kwargs = {"sdf_version": target_version}
        kwargs["split_impulse_penetration_threshold"] = self.split_impulse_penetration_threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("split_impulse_penetration_threshold")
        if self.split_impulse_penetration_threshold is not None:
            el.text = str(self.split_impulse_penetration_threshold)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SplitImpulsePenetrationThreshold":
        _text = el.text or -0.01
        _split_impulse_penetration_threshold = _parse_double(_text)
        return cls(sdf_version=version, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)


class Constraints(Model):
    def __init__(
        self,
        sdf_version: str,
        cfm: "Cfm" = None,
        erp: "Erp" = None,
        contact_surface_layer: "ContactSurfaceLayer" = None,
        split_impulse: "SplitImpulse" = None,
        split_impulse_penetration_threshold: "SplitImpulsePenetrationThreshold" = None
    ):
        self.__version__ = sdf_version
        self.cfm = cfm
        self.erp = erp
        self.contact_surface_layer = contact_surface_layer
        self.split_impulse = split_impulse
        self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

    def to_version(self, target_version: str) -> "Constraints":
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm.to_version(target_version) if self.cfm is not None else None
        kwargs["erp"] = self.erp.to_version(target_version) if self.erp is not None else None
        kwargs["contact_surface_layer"] = self.contact_surface_layer.to_version(target_version) if self.contact_surface_layer is not None else None
        kwargs["split_impulse"] = self.split_impulse.to_version(target_version) if self.split_impulse is not None else None
        kwargs["split_impulse_penetration_threshold"] = self.split_impulse_penetration_threshold.to_version(target_version) if self.split_impulse_penetration_threshold is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("constraints")
        if self.cfm is not None:
            el.append(self.cfm.to_sdf(version))
        if self.erp is not None:
            el.append(self.erp.to_sdf(version))
        if self.contact_surface_layer is not None:
            el.append(self.contact_surface_layer.to_sdf(version))
        if self.split_impulse is not None:
            el.append(self.split_impulse.to_sdf(version))
        if self.split_impulse_penetration_threshold is not None:
            el.append(self.split_impulse_penetration_threshold.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Constraints":
        _c_cfm = el.find("cfm")
        _cfm = Cfm.from_sdf(_c_cfm, version) if _c_cfm is not None else None
        _c_erp = el.find("erp")
        _erp = Erp.from_sdf(_c_erp, version) if _c_erp is not None else None
        _c_contact_surface_layer = el.find("contact_surface_layer")
        _contact_surface_layer = ContactSurfaceLayer.from_sdf(_c_contact_surface_layer, version) if _c_contact_surface_layer is not None else None
        _c_split_impulse = el.find("split_impulse")
        _split_impulse = SplitImpulse.from_sdf(_c_split_impulse, version) if _c_split_impulse is not None else None
        _c_split_impulse_penetration_threshold = el.find("split_impulse_penetration_threshold")
        _split_impulse_penetration_threshold = SplitImpulsePenetrationThreshold.from_sdf(_c_split_impulse_penetration_threshold, version) if _c_split_impulse_penetration_threshold is not None else None
        return cls(sdf_version=version, cfm=_cfm, erp=_erp, contact_surface_layer=_contact_surface_layer, split_impulse=_split_impulse, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)


class Bullet(Model):
    def __init__(
        self,
        sdf_version: str,
        dt: "Dt" = None,
        solver: "Solver" = None,
        constraints: "Constraints" = None
    ):
        self.__version__ = sdf_version
        self.dt = dt
        self.solver = solver
        self.constraints = constraints

    def to_version(self, target_version: str) -> "Bullet":
        if self.solver is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'solver' is not supported in SDF version {target_version} (added in 1.4)")
        if self.constraints is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'constraints' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["dt"] = self.dt.to_version(target_version) if self.dt is not None else None
        kwargs["solver"] = self.solver.to_version(target_version) if self.solver is not None else None
        kwargs["constraints"] = self.constraints.to_version(target_version) if self.constraints is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bullet")
        if self.dt is not None:
            el.append(self.dt.to_sdf(version))
        if self.solver is not None:
            el.append(self.solver.to_sdf(version))
        if self.constraints is not None:
            el.append(self.constraints.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Bullet":
        _c_dt = el.find("dt")
        _dt = Dt.from_sdf(_c_dt, version) if _c_dt is not None else None
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver, version) if _c_solver is not None else None
        if _solver is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'solver' is not supported in SDF version {version} (added in 1.4)")
        _c_constraints = el.find("constraints")
        _constraints = Constraints.from_sdf(_c_constraints, version) if _c_constraints is not None else None
        if _constraints is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'constraints' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, dt=_dt, solver=_solver, constraints=_constraints)


class Ode(Model):
    def __init__(
        self,
        sdf_version: str,
        solver: "Solver" = None,
        constraints: "Constraints" = None
    ):
        self.__version__ = sdf_version
        self.solver = solver
        self.constraints = constraints

    def to_version(self, target_version: str) -> "Ode":
        kwargs = {"sdf_version": target_version}
        kwargs["solver"] = self.solver.to_version(target_version) if self.solver is not None else None
        kwargs["constraints"] = self.constraints.to_version(target_version) if self.constraints is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.solver is not None:
            el.append(self.solver.to_sdf(version))
        if self.constraints is not None:
            el.append(self.constraints.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ode":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver, version) if _c_solver is not None else None
        _c_constraints = el.find("constraints")
        _constraints = Constraints.from_sdf(_c_constraints, version) if _c_constraints is not None else None
        return cls(sdf_version=version, solver=_solver, constraints=_constraints)


class UpdateRate(Model):
    def __init__(self, sdf_version: str, update_rate: float = 1000):
        self.__version__ = sdf_version
        self.update_rate = update_rate

    def to_version(self, target_version: str) -> "UpdateRate":
        if self.update_rate is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'update_rate' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["update_rate"] = self.update_rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("update_rate")
        if self.update_rate is not None:
            el.text = str(self.update_rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "UpdateRate":
        _text = el.text or 1000
        _update_rate = _parse_double(_text)
        if _update_rate is not None and cmp_version(version, "1.2") < 0:
            if _update_rate != 1000:
                raise ValueError(f"'update_rate' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, update_rate=_update_rate)


class MaxStepSize(Model):
    def __init__(self, sdf_version: str, max_step_size: float = 0.001):
        self.__version__ = sdf_version
        self.max_step_size = max_step_size

    def to_version(self, target_version: str) -> "MaxStepSize":
        if self.max_step_size is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'max_step_size' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["max_step_size"] = self.max_step_size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_step_size")
        if self.max_step_size is not None:
            el.text = str(self.max_step_size)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxStepSize":
        _text = el.text or 0.001
        _max_step_size = _parse_double(_text)
        if _max_step_size is not None and cmp_version(version, "1.4") < 0:
            if _max_step_size != 0.001:
                raise ValueError(f"'max_step_size' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, max_step_size=_max_step_size)


class RealTimeFactor(Model):
    def __init__(self, sdf_version: str, real_time_factor: float = 1.0):
        self.__version__ = sdf_version
        self.real_time_factor = real_time_factor

    def to_version(self, target_version: str) -> "RealTimeFactor":
        if self.real_time_factor is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'real_time_factor' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["real_time_factor"] = self.real_time_factor
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("real_time_factor")
        if self.real_time_factor is not None:
            el.text = str(self.real_time_factor)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "RealTimeFactor":
        _text = el.text or 1.0
        _real_time_factor = _parse_double(_text)
        if _real_time_factor is not None and cmp_version(version, "1.4") < 0:
            if _real_time_factor != 1.0:
                raise ValueError(f"'real_time_factor' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, real_time_factor=_real_time_factor)


class RealTimeUpdateRate(Model):
    def __init__(self, sdf_version: str, real_time_update_rate: float = 1000):
        self.__version__ = sdf_version
        self.real_time_update_rate = real_time_update_rate

    def to_version(self, target_version: str) -> "RealTimeUpdateRate":
        if self.real_time_update_rate is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'real_time_update_rate' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["real_time_update_rate"] = self.real_time_update_rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("real_time_update_rate")
        if self.real_time_update_rate is not None:
            el.text = str(self.real_time_update_rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "RealTimeUpdateRate":
        _text = el.text or 1000
        _real_time_update_rate = _parse_double(_text)
        if _real_time_update_rate is not None and cmp_version(version, "1.4") < 0:
            if _real_time_update_rate != 1000:
                raise ValueError(f"'real_time_update_rate' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, real_time_update_rate=_real_time_update_rate)


class Accuracy(Model):
    def __init__(self, sdf_version: str, accuracy: float = 1e-3):
        self.__version__ = sdf_version
        self.accuracy = accuracy

    def to_version(self, target_version: str) -> "Accuracy":
        kwargs = {"sdf_version": target_version}
        kwargs["accuracy"] = self.accuracy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("accuracy")
        if self.accuracy is not None:
            el.text = str(self.accuracy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Accuracy":
        _text = el.text or 1e-3
        _accuracy = _parse_double(_text)
        return cls(sdf_version=version, accuracy=_accuracy)


class MaxTransientVelocity(Model):
    def __init__(self, sdf_version: str, max_transient_velocity: float = 0.01):
        self.__version__ = sdf_version
        self.max_transient_velocity = max_transient_velocity

    def to_version(self, target_version: str) -> "MaxTransientVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["max_transient_velocity"] = self.max_transient_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_transient_velocity")
        if self.max_transient_velocity is not None:
            el.text = str(self.max_transient_velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxTransientVelocity":
        _text = el.text or 0.01
        _max_transient_velocity = _parse_double(_text)
        return cls(sdf_version=version, max_transient_velocity=_max_transient_velocity)


class Stiffness(Model):
    def __init__(self, sdf_version: str, stiffness: float = 1e8):
        self.__version__ = sdf_version
        self.stiffness = stiffness

    def to_version(self, target_version: str) -> "Stiffness":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Stiffness":
        _text = el.text or 1e8
        _stiffness = _parse_double(_text)
        return cls(sdf_version=version, stiffness=_stiffness)


class Dissipation(Model):
    def __init__(self, sdf_version: str, dissipation: float = 100):
        self.__version__ = sdf_version
        self.dissipation = dissipation

    def to_version(self, target_version: str) -> "Dissipation":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Dissipation":
        _text = el.text or 100
        _dissipation = _parse_double(_text)
        return cls(sdf_version=version, dissipation=_dissipation)


class PlasticCoefRestitution(Model):
    def __init__(self, sdf_version: str, plastic_coef_restitution: float = 0.5):
        self.__version__ = sdf_version
        self.plastic_coef_restitution = plastic_coef_restitution

    def to_version(self, target_version: str) -> "PlasticCoefRestitution":
        kwargs = {"sdf_version": target_version}
        kwargs["plastic_coef_restitution"] = self.plastic_coef_restitution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plastic_coef_restitution")
        if self.plastic_coef_restitution is not None:
            el.text = str(self.plastic_coef_restitution)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PlasticCoefRestitution":
        _text = el.text or 0.5
        _plastic_coef_restitution = _parse_double(_text)
        return cls(sdf_version=version, plastic_coef_restitution=_plastic_coef_restitution)


class PlasticImpactVelocity(Model):
    def __init__(self, sdf_version: str, plastic_impact_velocity: float = 0.5):
        self.__version__ = sdf_version
        self.plastic_impact_velocity = plastic_impact_velocity

    def to_version(self, target_version: str) -> "PlasticImpactVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["plastic_impact_velocity"] = self.plastic_impact_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plastic_impact_velocity")
        if self.plastic_impact_velocity is not None:
            el.text = str(self.plastic_impact_velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PlasticImpactVelocity":
        _text = el.text or 0.5
        _plastic_impact_velocity = _parse_double(_text)
        return cls(sdf_version=version, plastic_impact_velocity=_plastic_impact_velocity)


class StaticFriction(Model):
    def __init__(self, sdf_version: str, static_friction: float = 0.9):
        self.__version__ = sdf_version
        self.static_friction = static_friction

    def to_version(self, target_version: str) -> "StaticFriction":
        kwargs = {"sdf_version": target_version}
        kwargs["static_friction"] = self.static_friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("static_friction")
        if self.static_friction is not None:
            el.text = str(self.static_friction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "StaticFriction":
        _text = el.text or 0.9
        _static_friction = _parse_double(_text)
        return cls(sdf_version=version, static_friction=_static_friction)


class DynamicFriction(Model):
    def __init__(self, sdf_version: str, dynamic_friction: float = 0.9):
        self.__version__ = sdf_version
        self.dynamic_friction = dynamic_friction

    def to_version(self, target_version: str) -> "DynamicFriction":
        kwargs = {"sdf_version": target_version}
        kwargs["dynamic_friction"] = self.dynamic_friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamic_friction")
        if self.dynamic_friction is not None:
            el.text = str(self.dynamic_friction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "DynamicFriction":
        _text = el.text or 0.9
        _dynamic_friction = _parse_double(_text)
        return cls(sdf_version=version, dynamic_friction=_dynamic_friction)


class ViscousFriction(Model):
    def __init__(self, sdf_version: str, viscous_friction: float = 0.0):
        self.__version__ = sdf_version
        self.viscous_friction = viscous_friction

    def to_version(self, target_version: str) -> "ViscousFriction":
        kwargs = {"sdf_version": target_version}
        kwargs["viscous_friction"] = self.viscous_friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("viscous_friction")
        if self.viscous_friction is not None:
            el.text = str(self.viscous_friction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ViscousFriction":
        _text = el.text or 0.0
        _viscous_friction = _parse_double(_text)
        return cls(sdf_version=version, viscous_friction=_viscous_friction)


class OverrideImpactCaptureVelocity(Model):
    def __init__(self, sdf_version: str, override_impact_capture_velocity: float = 0.001):
        self.__version__ = sdf_version
        self.override_impact_capture_velocity = override_impact_capture_velocity

    def to_version(self, target_version: str) -> "OverrideImpactCaptureVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["override_impact_capture_velocity"] = self.override_impact_capture_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("override_impact_capture_velocity")
        if self.override_impact_capture_velocity is not None:
            el.text = str(self.override_impact_capture_velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "OverrideImpactCaptureVelocity":
        _text = el.text or 0.001
        _override_impact_capture_velocity = _parse_double(_text)
        return cls(sdf_version=version, override_impact_capture_velocity=_override_impact_capture_velocity)


class OverrideStictionTransitionVelocity(Model):
    def __init__(self, sdf_version: str, override_stiction_transition_velocity: float = 0.001):
        self.__version__ = sdf_version
        self.override_stiction_transition_velocity = override_stiction_transition_velocity

    def to_version(self, target_version: str) -> "OverrideStictionTransitionVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["override_stiction_transition_velocity"] = self.override_stiction_transition_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("override_stiction_transition_velocity")
        if self.override_stiction_transition_velocity is not None:
            el.text = str(self.override_stiction_transition_velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "OverrideStictionTransitionVelocity":
        _text = el.text or 0.001
        _override_stiction_transition_velocity = _parse_double(_text)
        return cls(sdf_version=version, override_stiction_transition_velocity=_override_stiction_transition_velocity)


class Contact(Model):
    def __init__(
        self,
        sdf_version: str,
        stiffness: "Stiffness" = None,
        dissipation: "Dissipation" = None,
        plastic_coef_restitution: "PlasticCoefRestitution" = None,
        plastic_impact_velocity: "PlasticImpactVelocity" = None,
        static_friction: "StaticFriction" = None,
        dynamic_friction: "DynamicFriction" = None,
        viscous_friction: "ViscousFriction" = None,
        override_impact_capture_velocity: "OverrideImpactCaptureVelocity" = None,
        override_stiction_transition_velocity: "OverrideStictionTransitionVelocity" = None
    ):
        self.__version__ = sdf_version
        self.stiffness = stiffness
        self.dissipation = dissipation
        self.plastic_coef_restitution = plastic_coef_restitution
        self.plastic_impact_velocity = plastic_impact_velocity
        self.static_friction = static_friction
        self.dynamic_friction = dynamic_friction
        self.viscous_friction = viscous_friction
        self.override_impact_capture_velocity = override_impact_capture_velocity
        self.override_stiction_transition_velocity = override_stiction_transition_velocity

    def to_version(self, target_version: str) -> "Contact":
        kwargs = {"sdf_version": target_version}
        kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
        kwargs["dissipation"] = self.dissipation.to_version(target_version) if self.dissipation is not None else None
        kwargs["plastic_coef_restitution"] = self.plastic_coef_restitution.to_version(target_version) if self.plastic_coef_restitution is not None else None
        kwargs["plastic_impact_velocity"] = self.plastic_impact_velocity.to_version(target_version) if self.plastic_impact_velocity is not None else None
        kwargs["static_friction"] = self.static_friction.to_version(target_version) if self.static_friction is not None else None
        kwargs["dynamic_friction"] = self.dynamic_friction.to_version(target_version) if self.dynamic_friction is not None else None
        kwargs["viscous_friction"] = self.viscous_friction.to_version(target_version) if self.viscous_friction is not None else None
        kwargs["override_impact_capture_velocity"] = self.override_impact_capture_velocity.to_version(target_version) if self.override_impact_capture_velocity is not None else None
        kwargs["override_stiction_transition_velocity"] = self.override_stiction_transition_velocity.to_version(target_version) if self.override_stiction_transition_velocity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf(version))
        if self.plastic_coef_restitution is not None:
            el.append(self.plastic_coef_restitution.to_sdf(version))
        if self.plastic_impact_velocity is not None:
            el.append(self.plastic_impact_velocity.to_sdf(version))
        if self.static_friction is not None:
            el.append(self.static_friction.to_sdf(version))
        if self.dynamic_friction is not None:
            el.append(self.dynamic_friction.to_sdf(version))
        if self.viscous_friction is not None:
            el.append(self.viscous_friction.to_sdf(version))
        if self.override_impact_capture_velocity is not None:
            el.append(self.override_impact_capture_velocity.to_sdf(version))
        if self.override_stiction_transition_velocity is not None:
            el.append(self.override_stiction_transition_velocity.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Contact":
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness, version) if _c_stiffness is not None else None
        _c_dissipation = el.find("dissipation")
        _dissipation = Dissipation.from_sdf(_c_dissipation, version) if _c_dissipation is not None else None
        _c_plastic_coef_restitution = el.find("plastic_coef_restitution")
        _plastic_coef_restitution = PlasticCoefRestitution.from_sdf(_c_plastic_coef_restitution, version) if _c_plastic_coef_restitution is not None else None
        _c_plastic_impact_velocity = el.find("plastic_impact_velocity")
        _plastic_impact_velocity = PlasticImpactVelocity.from_sdf(_c_plastic_impact_velocity, version) if _c_plastic_impact_velocity is not None else None
        _c_static_friction = el.find("static_friction")
        _static_friction = StaticFriction.from_sdf(_c_static_friction, version) if _c_static_friction is not None else None
        _c_dynamic_friction = el.find("dynamic_friction")
        _dynamic_friction = DynamicFriction.from_sdf(_c_dynamic_friction, version) if _c_dynamic_friction is not None else None
        _c_viscous_friction = el.find("viscous_friction")
        _viscous_friction = ViscousFriction.from_sdf(_c_viscous_friction, version) if _c_viscous_friction is not None else None
        _c_override_impact_capture_velocity = el.find("override_impact_capture_velocity")
        _override_impact_capture_velocity = OverrideImpactCaptureVelocity.from_sdf(_c_override_impact_capture_velocity, version) if _c_override_impact_capture_velocity is not None else None
        _c_override_stiction_transition_velocity = el.find("override_stiction_transition_velocity")
        _override_stiction_transition_velocity = OverrideStictionTransitionVelocity.from_sdf(_c_override_stiction_transition_velocity, version) if _c_override_stiction_transition_velocity is not None else None
        return cls(sdf_version=version, stiffness=_stiffness, dissipation=_dissipation, plastic_coef_restitution=_plastic_coef_restitution, plastic_impact_velocity=_plastic_impact_velocity, static_friction=_static_friction, dynamic_friction=_dynamic_friction, viscous_friction=_viscous_friction, override_impact_capture_velocity=_override_impact_capture_velocity, override_stiction_transition_velocity=_override_stiction_transition_velocity)


class Simbody(Model):
    def __init__(
        self,
        sdf_version: str,
        min_step_size: "MinStepSize" = None,
        accuracy: "Accuracy" = None,
        max_transient_velocity: "MaxTransientVelocity" = None,
        contact: "Contact" = None
    ):
        self.__version__ = sdf_version
        self.min_step_size = min_step_size
        self.accuracy = accuracy
        self.max_transient_velocity = max_transient_velocity
        self.contact = contact

    def to_version(self, target_version: str) -> "Simbody":
        kwargs = {"sdf_version": target_version}
        kwargs["min_step_size"] = self.min_step_size.to_version(target_version) if self.min_step_size is not None else None
        kwargs["accuracy"] = self.accuracy.to_version(target_version) if self.accuracy is not None else None
        kwargs["max_transient_velocity"] = self.max_transient_velocity.to_version(target_version) if self.max_transient_velocity is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("simbody")
        if self.min_step_size is not None:
            el.append(self.min_step_size.to_sdf(version))
        if self.accuracy is not None:
            el.append(self.accuracy.to_sdf(version))
        if self.max_transient_velocity is not None:
            el.append(self.max_transient_velocity.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Simbody":
        _c_min_step_size = el.find("min_step_size")
        _min_step_size = MinStepSize.from_sdf(_c_min_step_size, version) if _c_min_step_size is not None else None
        _c_accuracy = el.find("accuracy")
        _accuracy = Accuracy.from_sdf(_c_accuracy, version) if _c_accuracy is not None else None
        _c_max_transient_velocity = el.find("max_transient_velocity")
        _max_transient_velocity = MaxTransientVelocity.from_sdf(_c_max_transient_velocity, version) if _c_max_transient_velocity is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact, version) if _c_contact is not None else None
        return cls(sdf_version=version, min_step_size=_min_step_size, accuracy=_accuracy, max_transient_velocity=_max_transient_velocity, contact=_contact)


class MagneticField(Model):
    def __init__(self, sdf_version: str, magnetic_field: Vector3 = None):
        self.__version__ = sdf_version
        if magnetic_field is None:
            magnetic_field = Vector3.from_sdf("5.5645e-6 22.8758e-6 -42.3884e-6")
        self.magnetic_field = magnetic_field

    def to_version(self, target_version: str) -> "MagneticField":
        if self.magnetic_field is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["magnetic_field"] = self.magnetic_field
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("magnetic_field")
        if self.magnetic_field is not None:
            el.text = self.magnetic_field.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MagneticField":
        _text = el.text or "5.5645e-6 22.8758e-6 -42.3884e-6"
        _magnetic_field = Vector3.from_sdf(_text)
        if _magnetic_field is not None and cmp_version(version, "1.5") < 0:
            if _magnetic_field != "5.5645e-6 22.8758e-6 -42.3884e-6":
                raise ValueError(f"'magnetic_field' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, magnetic_field=_magnetic_field)


class CollisionDetector(Model):
    def __init__(self, sdf_version: str, collision_detector: str = "fcl"):
        self.__version__ = sdf_version
        self.collision_detector = collision_detector

    def to_version(self, target_version: str) -> "CollisionDetector":
        kwargs = {"sdf_version": target_version}
        kwargs["collision_detector"] = self.collision_detector
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision_detector")
        if self.collision_detector is not None:
            el.text = self.collision_detector
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CollisionDetector":
        _text = el.text or "fcl"
        _collision_detector = _text
        return cls(sdf_version=version, collision_detector=_collision_detector)


class Dart(Model):
    def __init__(
        self,
        sdf_version: str,
        solver: "Solver" = None,
        collision_detector: "CollisionDetector" = None
    ):
        self.__version__ = sdf_version
        self.solver = solver
        self.collision_detector = collision_detector

    def to_version(self, target_version: str) -> "Dart":
        kwargs = {"sdf_version": target_version}
        kwargs["solver"] = self.solver.to_version(target_version) if self.solver is not None else None
        kwargs["collision_detector"] = self.collision_detector.to_version(target_version) if self.collision_detector is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dart")
        if self.solver is not None:
            el.append(self.solver.to_sdf(version))
        if self.collision_detector is not None:
            el.append(self.collision_detector.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Dart":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver, version) if _c_solver is not None else None
        _c_collision_detector = el.find("collision_detector")
        _collision_detector = CollisionDetector.from_sdf(_c_collision_detector, version) if _c_collision_detector is not None else None
        return cls(sdf_version=version, solver=_solver, collision_detector=_collision_detector)


class Physics(Model):
    _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

    def __init__(
        self,
        sdf_version: str,
        type: str = "ode",
        update_rate: float = 0,
        name: str = "default_physics",
        default: bool = False,
        max_contacts: "MaxContacts" = None,
        gravity: "Gravity" = None,
        bullet: "Bullet" = None,
        ode: "Ode" = None,
        max_step_size: "MaxStepSize" = None,
        real_time_factor: "RealTimeFactor" = None,
        real_time_update_rate: "RealTimeUpdateRate" = None,
        simbody: "Simbody" = None,
        magnetic_field: "MagneticField" = None,
        dart: "Dart" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.update_rate = update_rate
        self.name = name
        self.default = default
        self.max_contacts = max_contacts
        self.gravity = gravity
        self.bullet = bullet
        self.ode = ode
        self.max_step_size = max_step_size
        self.real_time_factor = real_time_factor
        self.real_time_update_rate = real_time_update_rate
        self.simbody = simbody
        self.magnetic_field = magnetic_field
        self.dart = dart

    def to_version(self, target_version: str) -> "Physics":
        if self.name is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.5)")
        if self.default is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'default' is not supported in SDF version {target_version} (added in 1.5)")
        if self.max_step_size is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'max_step_size' is not supported in SDF version {target_version} (added in 1.4)")
        if self.real_time_factor is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'real_time_factor' is not supported in SDF version {target_version} (added in 1.4)")
        if self.real_time_update_rate is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'real_time_update_rate' is not supported in SDF version {target_version} (added in 1.4)")
        if self.simbody is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'simbody' is not supported in SDF version {target_version} (added in 1.4)")
        if self.magnetic_field is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (added in 1.5)")
        if self.dart is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dart' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["update_rate"] = self.update_rate
        kwargs["name"] = self.name
        kwargs["default"] = self.default
        kwargs["max_contacts"] = self.max_contacts.to_version(target_version) if self.max_contacts is not None else None
        kwargs["gravity"] = self.gravity.to_version(target_version) if self.gravity is not None else None
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["max_step_size"] = self.max_step_size.to_version(target_version) if self.max_step_size is not None else None
        kwargs["real_time_factor"] = self.real_time_factor.to_version(target_version) if self.real_time_factor is not None else None
        kwargs["real_time_update_rate"] = self.real_time_update_rate.to_version(target_version) if self.real_time_update_rate is not None else None
        kwargs["simbody"] = self.simbody.to_version(target_version) if self.simbody is not None else None
        kwargs["magnetic_field"] = self.magnetic_field.to_version(target_version) if self.magnetic_field is not None else None
        kwargs["dart"] = self.dart.to_version(target_version) if self.dart is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("physics")
        if self.type is not None:
            el.set("type", self.type)
        if self.update_rate is not None:
            el.set("update_rate", str(self.update_rate))
        if self.name is not None:
            el.set("name", self.name)
        if self.default is not None:
            el.set("default", str(self.default).lower())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf(version))
        if self.gravity is not None:
            el.append(self.gravity.to_sdf(version))
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.max_step_size is not None:
            el.append(self.max_step_size.to_sdf(version))
        if self.real_time_factor is not None:
            el.append(self.real_time_factor.to_sdf(version))
        if self.real_time_update_rate is not None:
            el.append(self.real_time_update_rate.to_sdf(version))
        if self.simbody is not None:
            el.append(self.simbody.to_sdf(version))
        if self.magnetic_field is not None:
            el.append(self.magnetic_field.to_sdf(version))
        if self.dart is not None:
            el.append(self.dart.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Physics":
        _type = el.get("type", "ode")
        _update_rate = _parse_double(el.get("update_rate", 0))
        _name = el.get("name", "default_physics")
        if _name is not None and cmp_version(version, "1.5") < 0:
            if _name != "default_physics":
                raise ValueError(f"'name' is not supported in SDF version {version} (added in 1.5)")
        _default = el.get("default", False).strip().lower() == 'true'
        if _default is not None and cmp_version(version, "1.5") < 0:
            if _default != False:
                raise ValueError(f"'default' is not supported in SDF version {version} (added in 1.5)")
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts, version) if _c_max_contacts is not None else None
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity, version) if _c_gravity is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet, version) if _c_bullet is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        _c_max_step_size = el.find("max_step_size")
        _max_step_size = MaxStepSize.from_sdf(_c_max_step_size, version) if _c_max_step_size is not None else None
        if _max_step_size is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'max_step_size' is not supported in SDF version {version} (added in 1.4)")
        _c_real_time_factor = el.find("real_time_factor")
        _real_time_factor = RealTimeFactor.from_sdf(_c_real_time_factor, version) if _c_real_time_factor is not None else None
        if _real_time_factor is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'real_time_factor' is not supported in SDF version {version} (added in 1.4)")
        _c_real_time_update_rate = el.find("real_time_update_rate")
        _real_time_update_rate = RealTimeUpdateRate.from_sdf(_c_real_time_update_rate, version) if _c_real_time_update_rate is not None else None
        if _real_time_update_rate is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'real_time_update_rate' is not supported in SDF version {version} (added in 1.4)")
        _c_simbody = el.find("simbody")
        _simbody = Simbody.from_sdf(_c_simbody, version) if _c_simbody is not None else None
        if _simbody is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'simbody' is not supported in SDF version {version} (added in 1.4)")
        _c_magnetic_field = el.find("magnetic_field")
        _magnetic_field = MagneticField.from_sdf(_c_magnetic_field, version) if _c_magnetic_field is not None else None
        if _magnetic_field is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'magnetic_field' is not supported in SDF version {version} (added in 1.5)")
        _c_dart = el.find("dart")
        _dart = Dart.from_sdf(_c_dart, version) if _c_dart is not None else None
        if _dart is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'dart' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, update_rate=_update_rate, name=_name, default=_default, max_contacts=_max_contacts, gravity=_gravity, bullet=_bullet, ode=_ode, max_step_size=_max_step_size, real_time_factor=_real_time_factor, real_time_update_rate=_real_time_update_rate, simbody=_simbody, magnetic_field=_magnetic_field, dart=_dart)
