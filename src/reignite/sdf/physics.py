### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations


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



class Physics(BaseModel):
    class Bullet(BaseModel):
        class Constraints(BaseModel):
            class Cfm(BaseModel):
                def __init__(self, sdf_version: str | None = None, cfm: float = 0):
                    super().__init__(sdf_version)
                    self.cfm = cfm

                def to_version(self, target_version: str) -> "Physics.Bullet.Constraints.Cfm":
                    kwargs = {"sdf_version": target_version}
                    kwargs["cfm"] = self.cfm
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("cfm")
                    if self.cfm is not None:
                        el.text = str(self.cfm)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Constraints.Cfm | SDFError":
                    _text = el.text or 0
                    _cfm = _parse_double(_text)
                    if isinstance(_cfm, SDFError):
                        return _cfm
                    return cls(sdf_version=version, cfm=_cfm)

            class ContactSurfaceLayer(BaseModel):
                def __init__(self, sdf_version: str | None = None, contact_surface_layer: float = 0.001):
                    super().__init__(sdf_version)
                    self.contact_surface_layer = contact_surface_layer

                def to_version(self, target_version: str) -> "Physics.Bullet.Constraints.ContactSurfaceLayer":
                    kwargs = {"sdf_version": target_version}
                    kwargs["contact_surface_layer"] = self.contact_surface_layer
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("contact_surface_layer")
                    if self.contact_surface_layer is not None:
                        el.text = str(self.contact_surface_layer)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Constraints.ContactSurfaceLayer | SDFError":
                    _text = el.text or 0.001
                    _contact_surface_layer = _parse_double(_text)
                    if isinstance(_contact_surface_layer, SDFError):
                        return _contact_surface_layer
                    return cls(sdf_version=version, contact_surface_layer=_contact_surface_layer)

            class Erp(BaseModel):
                def __init__(self, sdf_version: str | None = None, erp: float = 0.2):
                    super().__init__(sdf_version)
                    self.erp = erp

                def to_version(self, target_version: str) -> "Physics.Bullet.Constraints.Erp":
                    kwargs = {"sdf_version": target_version}
                    kwargs["erp"] = self.erp
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("erp")
                    if self.erp is not None:
                        el.text = str(self.erp)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Constraints.Erp | SDFError":
                    _text = el.text or 0.2
                    _erp = _parse_double(_text)
                    if isinstance(_erp, SDFError):
                        return _erp
                    return cls(sdf_version=version, erp=_erp)

            class SplitImpulse(BaseModel):
                def __init__(self, sdf_version: str | None = None, split_impulse: bool = True):
                    super().__init__(sdf_version)
                    self.split_impulse = split_impulse

                def to_version(self, target_version: str) -> "Physics.Bullet.Constraints.SplitImpulse":
                    kwargs = {"sdf_version": target_version}
                    kwargs["split_impulse"] = self.split_impulse
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("split_impulse")
                    if self.split_impulse is not None:
                        el.text = str(self.split_impulse).lower()
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Constraints.SplitImpulse | SDFError":
                    _text = el.text or True
                    _split_impulse = str(_text).strip().lower() == 'true'
                    if isinstance(_split_impulse, SDFError):
                        return _split_impulse
                    return cls(sdf_version=version, split_impulse=_split_impulse)

            class SplitImpulsePenetrationThreshold(BaseModel):
                def __init__(
                    self,
                    sdf_version: str | None = None,
                    split_impulse_penetration_threshold: float = -0.01
                ):
                    super().__init__(sdf_version)
                    self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

                def to_version(self, target_version: str) -> "Physics.Bullet.Constraints.SplitImpulsePenetrationThreshold":
                    kwargs = {"sdf_version": target_version}
                    kwargs["split_impulse_penetration_threshold"] = self.split_impulse_penetration_threshold
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("split_impulse_penetration_threshold")
                    if self.split_impulse_penetration_threshold is not None:
                        el.text = str(self.split_impulse_penetration_threshold)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Constraints.SplitImpulsePenetrationThreshold | SDFError":
                    _text = el.text or -0.01
                    _split_impulse_penetration_threshold = _parse_double(_text)
                    if isinstance(_split_impulse_penetration_threshold, SDFError):
                        return _split_impulse_penetration_threshold
                    return cls(sdf_version=version, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)

            def __init__(
                self,
                sdf_version: str | None = None,
                cfm: "Physics.Bullet.Constraints.Cfm" = None,
                contact_surface_layer: "Physics.Bullet.Constraints.ContactSurfaceLayer" = None,
                erp: "Physics.Bullet.Constraints.Erp" = None,
                split_impulse: "Physics.Bullet.Constraints.SplitImpulse" = None,
                split_impulse_penetration_threshold: "Physics.Bullet.Constraints.SplitImpulsePenetrationThreshold" = None
            ):
                super().__init__(sdf_version)
                self.cfm = cfm
                self.contact_surface_layer = contact_surface_layer
                self.erp = erp
                self.split_impulse = split_impulse
                self.split_impulse_penetration_threshold = split_impulse_penetration_threshold
                if self.cfm is not None:
                    if getattr(self.cfm, '__version__', None) is None:
                        self.cfm.__version__ = self.__version__
                    elif getattr(self.cfm, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.cfm = self.cfm.to_version(self.__version__)
                if self.contact_surface_layer is not None:
                    if getattr(self.contact_surface_layer, '__version__', None) is None:
                        self.contact_surface_layer.__version__ = self.__version__
                    elif getattr(self.contact_surface_layer, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.contact_surface_layer = self.contact_surface_layer.to_version(self.__version__)
                if self.erp is not None:
                    if getattr(self.erp, '__version__', None) is None:
                        self.erp.__version__ = self.__version__
                    elif getattr(self.erp, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.erp = self.erp.to_version(self.__version__)
                if self.split_impulse is not None:
                    if getattr(self.split_impulse, '__version__', None) is None:
                        self.split_impulse.__version__ = self.__version__
                    elif getattr(self.split_impulse, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.split_impulse = self.split_impulse.to_version(self.__version__)
                if self.split_impulse_penetration_threshold is not None:
                    if getattr(self.split_impulse_penetration_threshold, '__version__', None) is None:
                        self.split_impulse_penetration_threshold.__version__ = self.__version__
                    elif getattr(self.split_impulse_penetration_threshold, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.split_impulse_penetration_threshold = self.split_impulse_penetration_threshold.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Physics.Bullet.Constraints":
                kwargs = {"sdf_version": target_version}
                kwargs["cfm"] = self.cfm.to_version(target_version) if self.cfm is not None else None
                kwargs["contact_surface_layer"] = self.contact_surface_layer.to_version(target_version) if self.contact_surface_layer is not None else None
                kwargs["erp"] = self.erp.to_version(target_version) if self.erp is not None else None
                kwargs["split_impulse"] = self.split_impulse.to_version(target_version) if self.split_impulse is not None else None
                kwargs["split_impulse_penetration_threshold"] = self.split_impulse_penetration_threshold.to_version(target_version) if self.split_impulse_penetration_threshold is not None else None
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("constraints")
                if self.cfm is not None:
                    el.append(self.cfm.to_sdf(version))
                if self.contact_surface_layer is not None:
                    el.append(self.contact_surface_layer.to_sdf(version))
                if self.erp is not None:
                    el.append(self.erp.to_sdf(version))
                if self.split_impulse is not None:
                    el.append(self.split_impulse.to_sdf(version))
                if self.split_impulse_penetration_threshold is not None:
                    el.append(self.split_impulse_penetration_threshold.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Constraints | SDFError":
                _c_cfm = el.find("cfm")
                if _c_cfm is not None:
                    _res = cls.Cfm._from_sdf(_c_cfm, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("cfm")
                    _cfm = _res
                else:
                    _cfm = None
                _c_contact_surface_layer = el.find("contact_surface_layer")
                if _c_contact_surface_layer is not None:
                    _res = cls.ContactSurfaceLayer._from_sdf(_c_contact_surface_layer, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("contact_surface_layer")
                    _contact_surface_layer = _res
                else:
                    _contact_surface_layer = None
                _c_erp = el.find("erp")
                if _c_erp is not None:
                    _res = cls.Erp._from_sdf(_c_erp, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("erp")
                    _erp = _res
                else:
                    _erp = None
                _c_split_impulse = el.find("split_impulse")
                if _c_split_impulse is not None:
                    _res = cls.SplitImpulse._from_sdf(_c_split_impulse, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("split_impulse")
                    _split_impulse = _res
                else:
                    _split_impulse = None
                _c_split_impulse_penetration_threshold = el.find("split_impulse_penetration_threshold")
                if _c_split_impulse_penetration_threshold is not None:
                    _res = cls.SplitImpulsePenetrationThreshold._from_sdf(_c_split_impulse_penetration_threshold, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("split_impulse_penetration_threshold")
                    _split_impulse_penetration_threshold = _res
                else:
                    _split_impulse_penetration_threshold = None
                return cls(sdf_version=version, cfm=_cfm, contact_surface_layer=_contact_surface_layer, erp=_erp, split_impulse=_split_impulse, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)

        class Dt(BaseModel):
            def __init__(self, sdf_version: str | None = None, dt: float = 0.003):
                super().__init__(sdf_version)
                self.dt = dt

            def to_version(self, target_version: str) -> "Physics.Bullet.Dt":
                if self.dt is not None and cmp_version(target_version, "1.4") >= 0:
                    raise ValueError(f"'dt' is not supported in SDF version {target_version} (removed in 1.4)")
                kwargs = {"sdf_version": target_version}
                kwargs["dt"] = self.dt
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("dt")
                if self.dt is not None:
                    el.text = str(self.dt)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Dt | SDFError":
                _text = el.text or 0.003
                _dt = _parse_double(_text)
                if isinstance(_dt, SDFError):
                    return _dt
                return cls(sdf_version=version, dt=_dt)

        class Solver(BaseModel):
            class Iters(BaseModel):
                def __init__(self, sdf_version: str | None = None, iters: int = 50):
                    super().__init__(sdf_version)
                    self.iters = iters

                def to_version(self, target_version: str) -> "Physics.Bullet.Solver.Iters":
                    kwargs = {"sdf_version": target_version}
                    kwargs["iters"] = self.iters
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("iters")
                    if self.iters is not None:
                        el.text = str(self.iters)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Solver.Iters | SDFError":
                    _text = el.text or 50
                    _iters = _parse_int32(_text)
                    if isinstance(_iters, SDFError):
                        return _iters
                    return cls(sdf_version=version, iters=_iters)

            class MinStepSize(BaseModel):
                def __init__(self, sdf_version: str | None = None, min_step_size: float = 0.0001):
                    super().__init__(sdf_version)
                    self.min_step_size = min_step_size

                def to_version(self, target_version: str) -> "Physics.Bullet.Solver.MinStepSize":
                    kwargs = {"sdf_version": target_version}
                    kwargs["min_step_size"] = self.min_step_size
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("min_step_size")
                    if self.min_step_size is not None:
                        el.text = str(self.min_step_size)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Solver.MinStepSize | SDFError":
                    _text = el.text or 0.0001
                    _min_step_size = _parse_double(_text)
                    if isinstance(_min_step_size, SDFError):
                        return _min_step_size
                    return cls(sdf_version=version, min_step_size=_min_step_size)

            class Sor(BaseModel):
                def __init__(self, sdf_version: str | None = None, sor: float = 1.3):
                    super().__init__(sdf_version)
                    self.sor = sor

                def to_version(self, target_version: str) -> "Physics.Bullet.Solver.Sor":
                    kwargs = {"sdf_version": target_version}
                    kwargs["sor"] = self.sor
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("sor")
                    if self.sor is not None:
                        el.text = str(self.sor)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Solver.Sor | SDFError":
                    _text = el.text or 1.3
                    _sor = _parse_double(_text)
                    if isinstance(_sor, SDFError):
                        return _sor
                    return cls(sdf_version=version, sor=_sor)

            class Type(BaseModel):
                def __init__(self, sdf_version: str | None = None, type: str = "sequential_impulse"):
                    super().__init__(sdf_version)
                    self.type = type

                def to_version(self, target_version: str) -> "Physics.Bullet.Solver.Type":
                    kwargs = {"sdf_version": target_version}
                    kwargs["type"] = self.type
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("type")
                    if self.type is not None:
                        el.text = self.type
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Solver.Type | SDFError":
                    _text = el.text or "sequential_impulse"
                    _type = _text
                    if isinstance(_type, SDFError):
                        return _type
                    return cls(sdf_version=version, type=_type)

            def __init__(
                self,
                sdf_version: str | None = None,
                iters: "Physics.Bullet.Solver.Iters" = None,
                min_step_size: "Physics.Bullet.Solver.MinStepSize" = None,
                sor: "Physics.Bullet.Solver.Sor" = None,
                type: "Physics.Bullet.Solver.Type" = None
            ):
                super().__init__(sdf_version)
                self.iters = iters
                self.min_step_size = min_step_size
                self.sor = sor
                self.type = type
                if self.iters is not None:
                    if getattr(self.iters, '__version__', None) is None:
                        self.iters.__version__ = self.__version__
                    elif getattr(self.iters, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.iters = self.iters.to_version(self.__version__)
                if self.min_step_size is not None:
                    if getattr(self.min_step_size, '__version__', None) is None:
                        self.min_step_size.__version__ = self.__version__
                    elif getattr(self.min_step_size, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.min_step_size = self.min_step_size.to_version(self.__version__)
                if self.sor is not None:
                    if getattr(self.sor, '__version__', None) is None:
                        self.sor.__version__ = self.__version__
                    elif getattr(self.sor, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.sor = self.sor.to_version(self.__version__)
                if self.type is not None:
                    if getattr(self.type, '__version__', None) is None:
                        self.type.__version__ = self.__version__
                    elif getattr(self.type, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.type = self.type.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Physics.Bullet.Solver":
                kwargs = {"sdf_version": target_version}
                kwargs["iters"] = self.iters.to_version(target_version) if self.iters is not None else None
                kwargs["min_step_size"] = self.min_step_size.to_version(target_version) if self.min_step_size is not None else None
                kwargs["sor"] = self.sor.to_version(target_version) if self.sor is not None else None
                kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("solver")
                if self.iters is not None:
                    el.append(self.iters.to_sdf(version))
                if self.min_step_size is not None:
                    el.append(self.min_step_size.to_sdf(version))
                if self.sor is not None:
                    el.append(self.sor.to_sdf(version))
                if self.type is not None:
                    el.append(self.type.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Bullet.Solver | SDFError":
                _c_iters = el.find("iters")
                if _c_iters is not None:
                    _res = cls.Iters._from_sdf(_c_iters, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("iters")
                    _iters = _res
                else:
                    _iters = None
                _c_min_step_size = el.find("min_step_size")
                if _c_min_step_size is not None:
                    _res = cls.MinStepSize._from_sdf(_c_min_step_size, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("min_step_size")
                    _min_step_size = _res
                else:
                    _min_step_size = None
                _c_sor = el.find("sor")
                if _c_sor is not None:
                    _res = cls.Sor._from_sdf(_c_sor, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("sor")
                    _sor = _res
                else:
                    _sor = None
                _c_type = el.find("type")
                if _c_type is not None:
                    _res = cls.Type._from_sdf(_c_type, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("type")
                    _type = _res
                else:
                    _type = None
                return cls(sdf_version=version, iters=_iters, min_step_size=_min_step_size, sor=_sor, type=_type)

        def __init__(
            self,
            sdf_version: str | None = None,
            constraints: "Physics.Bullet.Constraints" = None,
            dt: "Physics.Bullet.Dt" = None,
            solver: "Physics.Bullet.Solver" = None
        ):
            super().__init__(sdf_version)
            self.constraints = constraints
            self.dt = dt
            self.solver = solver
            if self.constraints is not None:
                if getattr(self.constraints, '__version__', None) is None:
                    self.constraints.__version__ = self.__version__
                elif getattr(self.constraints, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.constraints = self.constraints.to_version(self.__version__)
            if self.dt is not None:
                if getattr(self.dt, '__version__', None) is None:
                    self.dt.__version__ = self.__version__
                elif getattr(self.dt, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.dt = self.dt.to_version(self.__version__)
            if self.solver is not None:
                if getattr(self.solver, '__version__', None) is None:
                    self.solver.__version__ = self.__version__
                elif getattr(self.solver, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.solver = self.solver.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Physics.Bullet":
            if self.constraints is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'constraints' is not supported in SDF version {target_version} (added in 1.4)")
            if self.dt is not None and cmp_version(target_version, "1.4") >= 0:
                raise ValueError(f"'dt' is not supported in SDF version {target_version} (removed in 1.4)")
            if self.solver is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'solver' is not supported in SDF version {target_version} (added in 1.4)")
            kwargs = {"sdf_version": target_version}
            kwargs["constraints"] = self.constraints.to_version(target_version) if self.constraints is not None else None
            kwargs["dt"] = self.dt.to_version(target_version) if self.dt is not None else None
            kwargs["solver"] = self.solver.to_version(target_version) if self.solver is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("bullet")
            if cmp_version(version, "1.4") >= 0:
                if self.constraints is None:
                    self.constraints = self.__class__.Constraints(sdf_version=version)
            if self.constraints is not None:
                el.append(self.constraints.to_sdf(version))
            if self.dt is not None:
                el.append(self.dt.to_sdf(version))
            if cmp_version(version, "1.4") >= 0:
                if self.solver is None:
                    self.solver = self.__class__.Solver(sdf_version=version)
            if self.solver is not None:
                el.append(self.solver.to_sdf(version))
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
                _res = cls.Constraints._from_sdf(ET.Element("constraints"), version)
                if isinstance(_res, SDFError):
                    return _res.extend("constraints")
                _constraints = _res
            if _constraints is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'constraints' is not supported in SDF version {version} (added in 1.4)")
            _c_dt = el.find("dt")
            if _c_dt is not None:
                _res = cls.Dt._from_sdf(_c_dt, version)
                if isinstance(_res, SDFError):
                    return _res.extend("dt")
                _dt = _res
            else:
                _dt = None
            _c_solver = el.find("solver")
            if _c_solver is not None:
                _res = cls.Solver._from_sdf(_c_solver, version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            else:
                _res = cls.Solver._from_sdf(ET.Element("solver"), version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            if _solver is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'solver' is not supported in SDF version {version} (added in 1.4)")
            return cls(sdf_version=version, constraints=_constraints, dt=_dt, solver=_solver)

    class Dart(BaseModel):
        class CollisionDetector(BaseModel):
            def __init__(self, sdf_version: str | None = None, collision_detector: str = "fcl"):
                super().__init__(sdf_version)
                self.collision_detector = collision_detector

            def to_version(self, target_version: str) -> "Physics.Dart.CollisionDetector":
                kwargs = {"sdf_version": target_version}
                kwargs["collision_detector"] = self.collision_detector
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("collision_detector")
                if self.collision_detector is not None:
                    el.text = self.collision_detector
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Dart.CollisionDetector | SDFError":
                _text = el.text or "fcl"
                _collision_detector = _text
                if isinstance(_collision_detector, SDFError):
                    return _collision_detector
                return cls(sdf_version=version, collision_detector=_collision_detector)

        class DartSolver(BaseModel):
            class SolverType(BaseModel):
                def __init__(self, sdf_version: str | None = None, solver_type: str = "dantzig"):
                    super().__init__(sdf_version)
                    self.solver_type = solver_type

                def to_version(self, target_version: str) -> "Physics.Dart.DartSolver.SolverType":
                    kwargs = {"sdf_version": target_version}
                    kwargs["solver_type"] = self.solver_type
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("solver_type")
                    if self.solver_type is not None:
                        el.text = self.solver_type
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Dart.DartSolver.SolverType | SDFError":
                    _text = el.text or "dantzig"
                    _solver_type = _text
                    if isinstance(_solver_type, SDFError):
                        return _solver_type
                    return cls(sdf_version=version, solver_type=_solver_type)

            def __init__(
                self,
                sdf_version: str | None = None,
                solver_type: "Physics.Dart.DartSolver.SolverType" = None
            ):
                super().__init__(sdf_version)
                self.solver_type = solver_type
                if self.solver_type is not None:
                    if getattr(self.solver_type, '__version__', None) is None:
                        self.solver_type.__version__ = self.__version__
                    elif getattr(self.solver_type, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.solver_type = self.solver_type.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Physics.Dart.DartSolver":
                kwargs = {"sdf_version": target_version}
                kwargs["solver_type"] = self.solver_type.to_version(target_version) if self.solver_type is not None else None
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("solver")
                if self.solver_type is not None:
                    el.append(self.solver_type.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Dart.DartSolver | SDFError":
                _c_solver_type = el.find("solver_type")
                if _c_solver_type is not None:
                    _res = cls.SolverType._from_sdf(_c_solver_type, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("solver_type")
                    _solver_type = _res
                else:
                    _solver_type = None
                return cls(sdf_version=version, solver_type=_solver_type)

        def __init__(
            self,
            sdf_version: str | None = None,
            collision_detector: "Physics.Dart.CollisionDetector" = None,
            solver: "Physics.Dart.DartSolver" = None
        ):
            super().__init__(sdf_version)
            self.collision_detector = collision_detector
            self.solver = solver
            if self.collision_detector is not None:
                if getattr(self.collision_detector, '__version__', None) is None:
                    self.collision_detector.__version__ = self.__version__
                elif getattr(self.collision_detector, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.collision_detector = self.collision_detector.to_version(self.__version__)
            if self.solver is not None:
                if getattr(self.solver, '__version__', None) is None:
                    self.solver.__version__ = self.__version__
                elif getattr(self.solver, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.solver = self.solver.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Physics.Dart":
            kwargs = {"sdf_version": target_version}
            kwargs["collision_detector"] = self.collision_detector.to_version(target_version) if self.collision_detector is not None else None
            kwargs["solver"] = self.solver.to_version(target_version) if self.solver is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("dart")
            if self.collision_detector is not None:
                el.append(self.collision_detector.to_sdf(version))
            if self.solver is None:
                self.solver = self.__class__.DartSolver(sdf_version=version)
            if self.solver is not None:
                el.append(self.solver.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Dart | SDFError":
            _c_collision_detector = el.find("collision_detector")
            if _c_collision_detector is not None:
                _res = cls.CollisionDetector._from_sdf(_c_collision_detector, version)
                if isinstance(_res, SDFError):
                    return _res.extend("collision_detector")
                _collision_detector = _res
            else:
                _collision_detector = None
            _c_solver = el.find("solver")
            if _c_solver is not None:
                _res = cls.DartSolver._from_sdf(_c_solver, version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            else:
                _res = cls.DartSolver._from_sdf(ET.Element("solver"), version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            return cls(sdf_version=version, collision_detector=_collision_detector, solver=_solver)

    class Gravity(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            gravity: _SDFVector3 = None,
            xyz: _SDFVector3 = None
        ):
            super().__init__(sdf_version)
            if gravity is None:
                gravity = _SDFVector3.from_sdf("0 0 -9.8", version=sdf_version)
            if xyz is None:
                xyz = _SDFVector3.from_sdf("0 0 -9.8", version=sdf_version)
            self.gravity = gravity
            self.xyz = xyz

        def to_version(self, target_version: str) -> "Physics.Gravity":
            if self.gravity is not None and cmp_version(target_version, "1.6") >= 0:
                raise ValueError(f"'gravity' is not supported in SDF version {target_version} (removed in 1.6)")
            if self.xyz is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'xyz' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["gravity"] = self.gravity
            kwargs["xyz"] = self.xyz
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
                el.text = self.gravity.to_sdf(version)
            if self.xyz is not None:
                el.set("xyz", self.xyz.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Gravity | SDFError":
            _text = el.text or "0 0 -9.8"
            _gravity = _SDFVector3._from_sdf(_text, version)
            if isinstance(_gravity, SDFError):
                return _gravity
            _xyz = _SDFVector3._from_sdf(el.get("xyz", "0 0 -9.8"), version)
            if isinstance(_xyz, SDFError):
                return _xyz.extend("@xyz")
            return cls(sdf_version=version, gravity=_gravity, xyz=_xyz)

    class MagneticField(BaseModel):
        def __init__(self, sdf_version: str | None = None, magnetic_field: _SDFVector3 = None):
            super().__init__(sdf_version)
            if magnetic_field is None:
                magnetic_field = _SDFVector3.from_sdf("5.5645e-6 22.8758e-6 -42.3884e-6", version=sdf_version)
            self.magnetic_field = magnetic_field

        def to_version(self, target_version: str) -> "Physics.MagneticField":
            if self.magnetic_field is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (added in 1.5)")
            if self.magnetic_field is not None and cmp_version(target_version, "1.6") >= 0:
                raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (removed in 1.6)")
            kwargs = {"sdf_version": target_version}
            kwargs["magnetic_field"] = self.magnetic_field
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("magnetic_field")
            if self.magnetic_field is not None:
                el.text = self.magnetic_field.to_sdf(version)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.MagneticField | SDFError":
            _text = el.text or "5.5645e-6 22.8758e-6 -42.3884e-6"
            _magnetic_field = _SDFVector3._from_sdf(_text, version)
            if isinstance(_magnetic_field, SDFError):
                return _magnetic_field
            if _magnetic_field is not None and cmp_version(version, "1.5") < 0:
                if _magnetic_field != "5.5645e-6 22.8758e-6 -42.3884e-6":
                    return SDFError(f"'magnetic_field' is not supported in SDF version {version} (added in 1.5)")
            return cls(sdf_version=version, magnetic_field=_magnetic_field)

    class MaxContacts(BaseModel):
        def __init__(self, sdf_version: str | None = None, max_contacts: int = 20):
            super().__init__(sdf_version)
            self.max_contacts = max_contacts

        def to_version(self, target_version: str) -> "Physics.MaxContacts":
            kwargs = {"sdf_version": target_version}
            kwargs["max_contacts"] = self.max_contacts
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("max_contacts")
            if self.max_contacts is not None:
                el.text = str(self.max_contacts)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.MaxContacts | SDFError":
            _text = el.text or 20
            _max_contacts = _parse_int32(_text)
            if isinstance(_max_contacts, SDFError):
                return _max_contacts
            return cls(sdf_version=version, max_contacts=_max_contacts)

    class MaxStepSize(BaseModel):
        def __init__(self, sdf_version: str | None = None, max_step_size: float = 0.001):
            super().__init__(sdf_version)
            self.max_step_size = max_step_size

        def to_version(self, target_version: str) -> "Physics.MaxStepSize":
            if self.max_step_size is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'max_step_size' is not supported in SDF version {target_version} (added in 1.4)")
            kwargs = {"sdf_version": target_version}
            kwargs["max_step_size"] = self.max_step_size
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("max_step_size")
            if self.max_step_size is not None:
                el.text = str(self.max_step_size)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.MaxStepSize | SDFError":
            _text = el.text or 0.001
            _max_step_size = _parse_double(_text)
            if isinstance(_max_step_size, SDFError):
                return _max_step_size
            if _max_step_size is not None and cmp_version(version, "1.4") < 0:
                if _max_step_size != 0.001:
                    return SDFError(f"'max_step_size' is not supported in SDF version {version} (added in 1.4)")
            return cls(sdf_version=version, max_step_size=_max_step_size)

    class Ode(BaseModel):
        class OdeConstraints(BaseModel):
            class ContactMaxCorrectingVel(BaseModel):
                def __init__(self, sdf_version: str | None = None, contact_max_correcting_vel: float = 100.0):
                    super().__init__(sdf_version)
                    self.contact_max_correcting_vel = contact_max_correcting_vel

                def to_version(self, target_version: str) -> "Physics.Ode.OdeConstraints.ContactMaxCorrectingVel":
                    if self.contact_max_correcting_vel is not None and cmp_version(target_version, "1.2") < 0:
                        raise ValueError(f"'contact_max_correcting_vel' is not supported in SDF version {target_version} (added in 1.2)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["contact_max_correcting_vel"] = self.contact_max_correcting_vel
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("contact_max_correcting_vel")
                    if self.contact_max_correcting_vel is not None:
                        el.text = str(self.contact_max_correcting_vel)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeConstraints.ContactMaxCorrectingVel | SDFError":
                    _text = el.text or 100.0
                    _contact_max_correcting_vel = _parse_double(_text)
                    if isinstance(_contact_max_correcting_vel, SDFError):
                        return _contact_max_correcting_vel
                    if _contact_max_correcting_vel is not None and cmp_version(version, "1.2") < 0:
                        if _contact_max_correcting_vel != 100.0:
                            return SDFError(f"'contact_max_correcting_vel' is not supported in SDF version {version} (added in 1.2)")
                    return cls(sdf_version=version, contact_max_correcting_vel=_contact_max_correcting_vel)

            def __init__(
                self,
                sdf_version: str | None = None,
                cfm: float = 0,
                contact_max_correcting_vel: float = 100.0,
                contact_surface_layer: float = 0.001,
                erp: float = 0.2
            ):
                super().__init__(sdf_version)
                self.cfm = cfm
                self.contact_max_correcting_vel = contact_max_correcting_vel
                self.contact_surface_layer = contact_surface_layer
                self.erp = erp

            def to_version(self, target_version: str) -> "Physics.Ode.OdeConstraints":
                if self.cfm is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'cfm' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.contact_max_correcting_vel is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'contact_max_correcting_vel' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.contact_surface_layer is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'contact_surface_layer' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.erp is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'erp' is not supported in SDF version {target_version} (removed in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["cfm"] = self.cfm
                kwargs["contact_max_correcting_vel"] = self.contact_max_correcting_vel
                kwargs["contact_surface_layer"] = self.contact_surface_layer
                kwargs["erp"] = self.erp
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("constraints")
                if self.cfm is not None:
                    el.set("cfm", str(self.cfm))
                if self.contact_max_correcting_vel is not None:
                    el.set("contact_max_correcting_vel", str(self.contact_max_correcting_vel))
                if self.contact_surface_layer is not None:
                    el.set("contact_surface_layer", str(self.contact_surface_layer))
                if self.erp is not None:
                    el.set("erp", str(self.erp))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeConstraints | SDFError":
                _cfm = _parse_double(el.get("cfm", 0))
                if isinstance(_cfm, SDFError):
                    return _cfm.extend("@cfm")
                _contact_max_correcting_vel = _parse_double(el.get("contact_max_correcting_vel", 100.0))
                if isinstance(_contact_max_correcting_vel, SDFError):
                    return _contact_max_correcting_vel.extend("@contact_max_correcting_vel")
                _contact_surface_layer = _parse_double(el.get("contact_surface_layer", 0.001))
                if isinstance(_contact_surface_layer, SDFError):
                    return _contact_surface_layer.extend("@contact_surface_layer")
                _erp = _parse_double(el.get("erp", 0.2))
                if isinstance(_erp, SDFError):
                    return _erp.extend("@erp")
                return cls(sdf_version=version, cfm=_cfm, contact_max_correcting_vel=_contact_max_correcting_vel, contact_surface_layer=_contact_surface_layer, erp=_erp)

        class OdeSolver(BaseModel):
            class FrictionModel(BaseModel):
                def __init__(self, sdf_version: str | None = None, friction_model: str = "pyramid_model"):
                    super().__init__(sdf_version)
                    self.friction_model = friction_model

                def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver.FrictionModel":
                    if self.friction_model is not None and cmp_version(target_version, "1.6") < 0:
                        raise ValueError(f"'friction_model' is not supported in SDF version {target_version} (added in 1.6)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["friction_model"] = self.friction_model
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("friction_model")
                    if self.friction_model is not None:
                        el.text = self.friction_model
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver.FrictionModel | SDFError":
                    _text = el.text or "pyramid_model"
                    _friction_model = _text
                    if isinstance(_friction_model, SDFError):
                        return _friction_model
                    if _friction_model is not None and cmp_version(version, "1.6") < 0:
                        if _friction_model != "pyramid_model":
                            return SDFError(f"'friction_model' is not supported in SDF version {version} (added in 1.6)")
                    return cls(sdf_version=version, friction_model=_friction_model)

            class IslandThreads(BaseModel):
                def __init__(self, sdf_version: str | None = None, island_threads: int = 0):
                    super().__init__(sdf_version)
                    self.island_threads = island_threads

                def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver.IslandThreads":
                    if self.island_threads is not None and cmp_version(target_version, "1.6") < 0:
                        raise ValueError(f"'island_threads' is not supported in SDF version {target_version} (added in 1.6)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["island_threads"] = self.island_threads
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("island_threads")
                    if self.island_threads is not None:
                        el.text = str(self.island_threads)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver.IslandThreads | SDFError":
                    _text = el.text or 0
                    _island_threads = _parse_int32(_text)
                    if isinstance(_island_threads, SDFError):
                        return _island_threads
                    if _island_threads is not None and cmp_version(version, "1.6") < 0:
                        if _island_threads != 0:
                            return SDFError(f"'island_threads' is not supported in SDF version {version} (added in 1.6)")
                    return cls(sdf_version=version, island_threads=_island_threads)

            class PreconIters(BaseModel):
                def __init__(self, sdf_version: str | None = None, precon_iters: int = 0):
                    super().__init__(sdf_version)
                    self.precon_iters = precon_iters

                def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver.PreconIters":
                    if self.precon_iters is not None and cmp_version(target_version, "1.2") < 0:
                        raise ValueError(f"'precon_iters' is not supported in SDF version {target_version} (added in 1.2)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["precon_iters"] = self.precon_iters
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("precon_iters")
                    if self.precon_iters is not None:
                        el.text = str(self.precon_iters)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver.PreconIters | SDFError":
                    _text = el.text or 0
                    _precon_iters = _parse_int32(_text)
                    if isinstance(_precon_iters, SDFError):
                        return _precon_iters
                    if _precon_iters is not None and cmp_version(version, "1.2") < 0:
                        if _precon_iters != 0:
                            return SDFError(f"'precon_iters' is not supported in SDF version {version} (added in 1.2)")
                    return cls(sdf_version=version, precon_iters=_precon_iters)

            class SolverDt(BaseModel):
                def __init__(self, sdf_version: str | None = None, dt: float = 0.001):
                    super().__init__(sdf_version)
                    self.dt = dt

                def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver.SolverDt":
                    if self.dt is not None and cmp_version(target_version, "1.2") < 0:
                        raise ValueError(f"'dt' is not supported in SDF version {target_version} (added in 1.2)")
                    if self.dt is not None and cmp_version(target_version, "1.4") >= 0:
                        raise ValueError(f"'dt' is not supported in SDF version {target_version} (removed in 1.4)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["dt"] = self.dt
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("dt")
                    if self.dt is not None:
                        el.text = str(self.dt)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver.SolverDt | SDFError":
                    _text = el.text or 0.001
                    _dt = _parse_double(_text)
                    if isinstance(_dt, SDFError):
                        return _dt
                    if _dt is not None and cmp_version(version, "1.2") < 0:
                        if _dt != 0.001:
                            return SDFError(f"'dt' is not supported in SDF version {version} (added in 1.2)")
                    return cls(sdf_version=version, dt=_dt)

            class SolverType2(BaseModel):
                def __init__(self, sdf_version: str | None = None, type: str = "quick"):
                    super().__init__(sdf_version)
                    self.type = type

                def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver.SolverType2":
                    if self.type is not None and cmp_version(target_version, "1.2") < 0:
                        raise ValueError(f"'type' is not supported in SDF version {target_version} (added in 1.2)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["type"] = self.type
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("type")
                    if self.type is not None:
                        el.text = self.type
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver.SolverType2 | SDFError":
                    _text = el.text or "quick"
                    _type = _text
                    if isinstance(_type, SDFError):
                        return _type
                    if _type is not None and cmp_version(version, "1.2") < 0:
                        if _type != "quick":
                            return SDFError(f"'type' is not supported in SDF version {version} (added in 1.2)")
                    return cls(sdf_version=version, type=_type)

            class ThreadPositionCorrection(BaseModel):
                def __init__(self, sdf_version: str | None = None, thread_position_correction: bool = False):
                    super().__init__(sdf_version)
                    self.thread_position_correction = thread_position_correction

                def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver.ThreadPositionCorrection":
                    if self.thread_position_correction is not None and cmp_version(target_version, "1.6") < 0:
                        raise ValueError(f"'thread_position_correction' is not supported in SDF version {target_version} (added in 1.6)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["thread_position_correction"] = self.thread_position_correction
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("thread_position_correction")
                    if self.thread_position_correction is not None:
                        el.text = str(self.thread_position_correction).lower()
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver.ThreadPositionCorrection | SDFError":
                    _text = el.text or False
                    _thread_position_correction = str(_text).strip().lower() == 'true'
                    if isinstance(_thread_position_correction, SDFError):
                        return _thread_position_correction
                    if _thread_position_correction is not None and cmp_version(version, "1.6") < 0:
                        if _thread_position_correction != False:
                            return SDFError(f"'thread_position_correction' is not supported in SDF version {version} (added in 1.6)")
                    return cls(sdf_version=version, thread_position_correction=_thread_position_correction)

            class UseDynamicMoiRescaling(BaseModel):
                def __init__(self, sdf_version: str | None = None, use_dynamic_moi_rescaling: bool = False):
                    super().__init__(sdf_version)
                    self.use_dynamic_moi_rescaling = use_dynamic_moi_rescaling

                def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver.UseDynamicMoiRescaling":
                    if self.use_dynamic_moi_rescaling is not None and cmp_version(target_version, "1.4") < 0:
                        raise ValueError(f"'use_dynamic_moi_rescaling' is not supported in SDF version {target_version} (added in 1.4)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["use_dynamic_moi_rescaling"] = self.use_dynamic_moi_rescaling
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("use_dynamic_moi_rescaling")
                    if self.use_dynamic_moi_rescaling is not None:
                        el.text = str(self.use_dynamic_moi_rescaling).lower()
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver.UseDynamicMoiRescaling | SDFError":
                    _text = el.text or False
                    _use_dynamic_moi_rescaling = str(_text).strip().lower() == 'true'
                    if isinstance(_use_dynamic_moi_rescaling, SDFError):
                        return _use_dynamic_moi_rescaling
                    if _use_dynamic_moi_rescaling is not None and cmp_version(version, "1.4") < 0:
                        if _use_dynamic_moi_rescaling != False:
                            return SDFError(f"'use_dynamic_moi_rescaling' is not supported in SDF version {version} (added in 1.4)")
                    return cls(sdf_version=version, use_dynamic_moi_rescaling=_use_dynamic_moi_rescaling)

            def __init__(
                self,
                sdf_version: str | None = None,
                dt: float = 0.001,
                friction_model: "Physics.Ode.OdeSolver.FrictionModel" = None,
                island_threads: "Physics.Ode.OdeSolver.IslandThreads" = None,
                iters: int = 50,
                min_step_size: "MinStepSize" = None,
                precon_iters: int = 0,
                sor: float = 1.3,
                thread_position_correction: "Physics.Ode.OdeSolver.ThreadPositionCorrection" = None,
                type: str = "quick",
                use_dynamic_moi_rescaling: "Physics.Ode.OdeSolver.UseDynamicMoiRescaling" = None
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
                if self.friction_model is not None:
                    if getattr(self.friction_model, '__version__', None) is None:
                        self.friction_model.__version__ = self.__version__
                    elif getattr(self.friction_model, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.friction_model = self.friction_model.to_version(self.__version__)
                if self.island_threads is not None:
                    if getattr(self.island_threads, '__version__', None) is None:
                        self.island_threads.__version__ = self.__version__
                    elif getattr(self.island_threads, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.island_threads = self.island_threads.to_version(self.__version__)
                if self.min_step_size is not None:
                    if getattr(self.min_step_size, '__version__', None) is None:
                        self.min_step_size.__version__ = self.__version__
                    elif getattr(self.min_step_size, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.min_step_size = self.min_step_size.to_version(self.__version__)
                if self.thread_position_correction is not None:
                    if getattr(self.thread_position_correction, '__version__', None) is None:
                        self.thread_position_correction.__version__ = self.__version__
                    elif getattr(self.thread_position_correction, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.thread_position_correction = self.thread_position_correction.to_version(self.__version__)
                if self.use_dynamic_moi_rescaling is not None:
                    if getattr(self.use_dynamic_moi_rescaling, '__version__', None) is None:
                        self.use_dynamic_moi_rescaling.__version__ = self.__version__
                    elif getattr(self.use_dynamic_moi_rescaling, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.use_dynamic_moi_rescaling = self.use_dynamic_moi_rescaling.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Physics.Ode.OdeSolver":
                if self.dt is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'dt' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.friction_model is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'friction_model' is not supported in SDF version {target_version} (added in 1.6)")
                if self.island_threads is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'island_threads' is not supported in SDF version {target_version} (added in 1.6)")
                if self.iters is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'iters' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.min_step_size is not None and cmp_version(target_version, "1.4") < 0:
                    raise ValueError(f"'min_step_size' is not supported in SDF version {target_version} (added in 1.4)")
                if self.precon_iters is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'precon_iters' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.sor is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'sor' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.thread_position_correction is not None and cmp_version(target_version, "1.6") < 0:
                    raise ValueError(f"'thread_position_correction' is not supported in SDF version {target_version} (added in 1.6)")
                if self.type is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'type' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.use_dynamic_moi_rescaling is not None and cmp_version(target_version, "1.4") < 0:
                    raise ValueError(f"'use_dynamic_moi_rescaling' is not supported in SDF version {target_version} (added in 1.4)")
                kwargs = {"sdf_version": target_version}
                kwargs["dt"] = self.dt
                kwargs["friction_model"] = self.friction_model.to_version(target_version) if self.friction_model is not None else None
                kwargs["island_threads"] = self.island_threads.to_version(target_version) if self.island_threads is not None else None
                kwargs["iters"] = self.iters
                kwargs["min_step_size"] = self.min_step_size.to_version(target_version) if self.min_step_size is not None else None
                kwargs["precon_iters"] = self.precon_iters
                kwargs["sor"] = self.sor
                kwargs["thread_position_correction"] = self.thread_position_correction.to_version(target_version) if self.thread_position_correction is not None else None
                kwargs["type"] = self.type
                kwargs["use_dynamic_moi_rescaling"] = self.use_dynamic_moi_rescaling.to_version(target_version) if self.use_dynamic_moi_rescaling is not None else None
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("solver")
                if self.dt is not None:
                    el.set("dt", str(self.dt))
                if self.friction_model is not None:
                    el.append(self.friction_model.to_sdf(version))
                if self.island_threads is not None:
                    el.append(self.island_threads.to_sdf(version))
                if self.iters is not None:
                    el.set("iters", str(self.iters))
                if self.min_step_size is not None:
                    el.append(self.min_step_size.to_sdf(version))
                if self.precon_iters is not None:
                    el.set("precon_iters", str(self.precon_iters))
                if self.sor is not None:
                    el.set("sor", str(self.sor))
                if self.thread_position_correction is not None:
                    el.append(self.thread_position_correction.to_sdf(version))
                if self.type is not None:
                    el.set("type", self.type)
                if self.use_dynamic_moi_rescaling is not None:
                    el.append(self.use_dynamic_moi_rescaling.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Ode.OdeSolver | SDFError":
                _dt = _parse_double(el.get("dt", 0.001))
                if isinstance(_dt, SDFError):
                    return _dt.extend("@dt")
                _c_friction_model = el.find("friction_model")
                if _c_friction_model is not None:
                    _res = cls.FrictionModel._from_sdf(_c_friction_model, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("friction_model")
                    _friction_model = _res
                else:
                    _friction_model = None
                if _friction_model is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'friction_model' is not supported in SDF version {version} (added in 1.6)")
                _c_island_threads = el.find("island_threads")
                if _c_island_threads is not None:
                    _res = cls.IslandThreads._from_sdf(_c_island_threads, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("island_threads")
                    _island_threads = _res
                else:
                    _island_threads = None
                if _island_threads is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'island_threads' is not supported in SDF version {version} (added in 1.6)")
                _iters = _parse_int32(el.get("iters", 50))
                if isinstance(_iters, SDFError):
                    return _iters.extend("@iters")
                _c_min_step_size = el.find("min_step_size")
                if _c_min_step_size is not None:
                    _res = MinStepSize._from_sdf(_c_min_step_size, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("min_step_size")
                    _min_step_size = _res
                else:
                    _min_step_size = None
                if _min_step_size is not None and cmp_version(version, "1.4") < 0:
                    return SDFError(f"'min_step_size' is not supported in SDF version {version} (added in 1.4)")
                _precon_iters = _parse_int32(el.get("precon_iters", 0))
                if isinstance(_precon_iters, SDFError):
                    return _precon_iters.extend("@precon_iters")
                _sor = _parse_double(el.get("sor", 1.3))
                if isinstance(_sor, SDFError):
                    return _sor.extend("@sor")
                _c_thread_position_correction = el.find("thread_position_correction")
                if _c_thread_position_correction is not None:
                    _res = cls.ThreadPositionCorrection._from_sdf(_c_thread_position_correction, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("thread_position_correction")
                    _thread_position_correction = _res
                else:
                    _thread_position_correction = None
                if _thread_position_correction is not None and cmp_version(version, "1.6") < 0:
                    return SDFError(f"'thread_position_correction' is not supported in SDF version {version} (added in 1.6)")
                _type = el.get("type", "quick")
                if isinstance(_type, SDFError):
                    return _type.extend("@type")
                _c_use_dynamic_moi_rescaling = el.find("use_dynamic_moi_rescaling")
                if _c_use_dynamic_moi_rescaling is not None:
                    _res = cls.UseDynamicMoiRescaling._from_sdf(_c_use_dynamic_moi_rescaling, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("use_dynamic_moi_rescaling")
                    _use_dynamic_moi_rescaling = _res
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
            if self.constraints is not None:
                if getattr(self.constraints, '__version__', None) is None:
                    self.constraints.__version__ = self.__version__
                elif getattr(self.constraints, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.constraints = self.constraints.to_version(self.__version__)
            if self.solver is not None:
                if getattr(self.solver, '__version__', None) is None:
                    self.solver.__version__ = self.__version__
                elif getattr(self.solver, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.solver = self.solver.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Physics.Ode":
            kwargs = {"sdf_version": target_version}
            kwargs["constraints"] = self.constraints.to_version(target_version) if self.constraints is not None else None
            kwargs["solver"] = self.solver.to_version(target_version) if self.solver is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("ode")
            if self.constraints is None:
                self.constraints = self.__class__.OdeConstraints(sdf_version=version)
            if self.constraints is not None:
                el.append(self.constraints.to_sdf(version))
            if self.solver is None:
                self.solver = self.__class__.OdeSolver(sdf_version=version)
            if self.solver is not None:
                el.append(self.solver.to_sdf(version))
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
                _res = cls.OdeConstraints._from_sdf(ET.Element("constraints"), version)
                if isinstance(_res, SDFError):
                    return _res.extend("constraints")
                _constraints = _res
            _c_solver = el.find("solver")
            if _c_solver is not None:
                _res = cls.OdeSolver._from_sdf(_c_solver, version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            else:
                _res = cls.OdeSolver._from_sdf(ET.Element("solver"), version)
                if isinstance(_res, SDFError):
                    return _res.extend("solver")
                _solver = _res
            return cls(sdf_version=version, constraints=_constraints, solver=_solver)

    class RealTimeFactor(BaseModel):
        def __init__(self, sdf_version: str | None = None, real_time_factor: float = 1.0):
            super().__init__(sdf_version)
            self.real_time_factor = real_time_factor

        def to_version(self, target_version: str) -> "Physics.RealTimeFactor":
            if self.real_time_factor is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'real_time_factor' is not supported in SDF version {target_version} (added in 1.4)")
            kwargs = {"sdf_version": target_version}
            kwargs["real_time_factor"] = self.real_time_factor
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("real_time_factor")
            if self.real_time_factor is not None:
                el.text = str(self.real_time_factor)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.RealTimeFactor | SDFError":
            _text = el.text or 1.0
            _real_time_factor = _parse_double(_text)
            if isinstance(_real_time_factor, SDFError):
                return _real_time_factor
            if _real_time_factor is not None and cmp_version(version, "1.4") < 0:
                if _real_time_factor != 1.0:
                    return SDFError(f"'real_time_factor' is not supported in SDF version {version} (added in 1.4)")
            return cls(sdf_version=version, real_time_factor=_real_time_factor)

    class RealTimeUpdateRate(BaseModel):
        def __init__(self, sdf_version: str | None = None, real_time_update_rate: float = 1000):
            super().__init__(sdf_version)
            self.real_time_update_rate = real_time_update_rate

        def to_version(self, target_version: str) -> "Physics.RealTimeUpdateRate":
            if self.real_time_update_rate is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'real_time_update_rate' is not supported in SDF version {target_version} (added in 1.4)")
            kwargs = {"sdf_version": target_version}
            kwargs["real_time_update_rate"] = self.real_time_update_rate
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("real_time_update_rate")
            if self.real_time_update_rate is not None:
                el.text = str(self.real_time_update_rate)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.RealTimeUpdateRate | SDFError":
            _text = el.text or 1000
            _real_time_update_rate = _parse_double(_text)
            if isinstance(_real_time_update_rate, SDFError):
                return _real_time_update_rate
            if _real_time_update_rate is not None and cmp_version(version, "1.4") < 0:
                if _real_time_update_rate != 1000:
                    return SDFError(f"'real_time_update_rate' is not supported in SDF version {version} (added in 1.4)")
            return cls(sdf_version=version, real_time_update_rate=_real_time_update_rate)

    class Simbody(BaseModel):
        class Accuracy(BaseModel):
            def __init__(self, sdf_version: str | None = None, accuracy: float = 1e-3):
                super().__init__(sdf_version)
                self.accuracy = accuracy

            def to_version(self, target_version: str) -> "Physics.Simbody.Accuracy":
                kwargs = {"sdf_version": target_version}
                kwargs["accuracy"] = self.accuracy
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("accuracy")
                if self.accuracy is not None:
                    el.text = str(self.accuracy)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Accuracy | SDFError":
                _text = el.text or 1e-3
                _accuracy = _parse_double(_text)
                if isinstance(_accuracy, SDFError):
                    return _accuracy
                return cls(sdf_version=version, accuracy=_accuracy)

        class Contact(BaseModel):
            class Dissipation(BaseModel):
                def __init__(self, sdf_version: str | None = None, dissipation: float = 100):
                    super().__init__(sdf_version)
                    self.dissipation = dissipation

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.Dissipation":
                    kwargs = {"sdf_version": target_version}
                    kwargs["dissipation"] = self.dissipation
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("dissipation")
                    if self.dissipation is not None:
                        el.text = str(self.dissipation)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.Dissipation | SDFError":
                    _text = el.text or 100
                    _dissipation = _parse_double(_text)
                    if isinstance(_dissipation, SDFError):
                        return _dissipation
                    return cls(sdf_version=version, dissipation=_dissipation)

            class DynamicFriction(BaseModel):
                def __init__(self, sdf_version: str | None = None, dynamic_friction: float = 0.9):
                    super().__init__(sdf_version)
                    self.dynamic_friction = dynamic_friction

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.DynamicFriction":
                    kwargs = {"sdf_version": target_version}
                    kwargs["dynamic_friction"] = self.dynamic_friction
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("dynamic_friction")
                    if self.dynamic_friction is not None:
                        el.text = str(self.dynamic_friction)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.DynamicFriction | SDFError":
                    _text = el.text or 0.9
                    _dynamic_friction = _parse_double(_text)
                    if isinstance(_dynamic_friction, SDFError):
                        return _dynamic_friction
                    return cls(sdf_version=version, dynamic_friction=_dynamic_friction)

            class OverrideImpactCaptureVelocity(BaseModel):
                def __init__(
                    self,
                    sdf_version: str | None = None,
                    override_impact_capture_velocity: float = 0.001
                ):
                    super().__init__(sdf_version)
                    self.override_impact_capture_velocity = override_impact_capture_velocity

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.OverrideImpactCaptureVelocity":
                    kwargs = {"sdf_version": target_version}
                    kwargs["override_impact_capture_velocity"] = self.override_impact_capture_velocity
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("override_impact_capture_velocity")
                    if self.override_impact_capture_velocity is not None:
                        el.text = str(self.override_impact_capture_velocity)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.OverrideImpactCaptureVelocity | SDFError":
                    _text = el.text or 0.001
                    _override_impact_capture_velocity = _parse_double(_text)
                    if isinstance(_override_impact_capture_velocity, SDFError):
                        return _override_impact_capture_velocity
                    return cls(sdf_version=version, override_impact_capture_velocity=_override_impact_capture_velocity)

            class OverrideStictionTransitionVelocity(BaseModel):
                def __init__(
                    self,
                    sdf_version: str | None = None,
                    override_stiction_transition_velocity: float = 0.001
                ):
                    super().__init__(sdf_version)
                    self.override_stiction_transition_velocity = override_stiction_transition_velocity

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.OverrideStictionTransitionVelocity":
                    kwargs = {"sdf_version": target_version}
                    kwargs["override_stiction_transition_velocity"] = self.override_stiction_transition_velocity
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("override_stiction_transition_velocity")
                    if self.override_stiction_transition_velocity is not None:
                        el.text = str(self.override_stiction_transition_velocity)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.OverrideStictionTransitionVelocity | SDFError":
                    _text = el.text or 0.001
                    _override_stiction_transition_velocity = _parse_double(_text)
                    if isinstance(_override_stiction_transition_velocity, SDFError):
                        return _override_stiction_transition_velocity
                    return cls(sdf_version=version, override_stiction_transition_velocity=_override_stiction_transition_velocity)

            class PlasticCoefRestitution(BaseModel):
                def __init__(self, sdf_version: str | None = None, plastic_coef_restitution: float = 0.5):
                    super().__init__(sdf_version)
                    self.plastic_coef_restitution = plastic_coef_restitution

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.PlasticCoefRestitution":
                    kwargs = {"sdf_version": target_version}
                    kwargs["plastic_coef_restitution"] = self.plastic_coef_restitution
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("plastic_coef_restitution")
                    if self.plastic_coef_restitution is not None:
                        el.text = str(self.plastic_coef_restitution)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.PlasticCoefRestitution | SDFError":
                    _text = el.text or 0.5
                    _plastic_coef_restitution = _parse_double(_text)
                    if isinstance(_plastic_coef_restitution, SDFError):
                        return _plastic_coef_restitution
                    return cls(sdf_version=version, plastic_coef_restitution=_plastic_coef_restitution)

            class PlasticImpactVelocity(BaseModel):
                def __init__(self, sdf_version: str | None = None, plastic_impact_velocity: float = 0.5):
                    super().__init__(sdf_version)
                    self.plastic_impact_velocity = plastic_impact_velocity

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.PlasticImpactVelocity":
                    kwargs = {"sdf_version": target_version}
                    kwargs["plastic_impact_velocity"] = self.plastic_impact_velocity
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("plastic_impact_velocity")
                    if self.plastic_impact_velocity is not None:
                        el.text = str(self.plastic_impact_velocity)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.PlasticImpactVelocity | SDFError":
                    _text = el.text or 0.5
                    _plastic_impact_velocity = _parse_double(_text)
                    if isinstance(_plastic_impact_velocity, SDFError):
                        return _plastic_impact_velocity
                    return cls(sdf_version=version, plastic_impact_velocity=_plastic_impact_velocity)

            class StaticFriction(BaseModel):
                def __init__(self, sdf_version: str | None = None, static_friction: float = 0.9):
                    super().__init__(sdf_version)
                    self.static_friction = static_friction

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.StaticFriction":
                    kwargs = {"sdf_version": target_version}
                    kwargs["static_friction"] = self.static_friction
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("static_friction")
                    if self.static_friction is not None:
                        el.text = str(self.static_friction)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.StaticFriction | SDFError":
                    _text = el.text or 0.9
                    _static_friction = _parse_double(_text)
                    if isinstance(_static_friction, SDFError):
                        return _static_friction
                    return cls(sdf_version=version, static_friction=_static_friction)

            class Stiffness(BaseModel):
                def __init__(self, sdf_version: str | None = None, stiffness: float = 1e8):
                    super().__init__(sdf_version)
                    self.stiffness = stiffness

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.Stiffness":
                    kwargs = {"sdf_version": target_version}
                    kwargs["stiffness"] = self.stiffness
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("stiffness")
                    if self.stiffness is not None:
                        el.text = str(self.stiffness)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.Stiffness | SDFError":
                    _text = el.text or 1e8
                    _stiffness = _parse_double(_text)
                    if isinstance(_stiffness, SDFError):
                        return _stiffness
                    return cls(sdf_version=version, stiffness=_stiffness)

            class ViscousFriction(BaseModel):
                def __init__(self, sdf_version: str | None = None, viscous_friction: float = 0.0):
                    super().__init__(sdf_version)
                    self.viscous_friction = viscous_friction

                def to_version(self, target_version: str) -> "Physics.Simbody.Contact.ViscousFriction":
                    kwargs = {"sdf_version": target_version}
                    kwargs["viscous_friction"] = self.viscous_friction
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("viscous_friction")
                    if self.viscous_friction is not None:
                        el.text = str(self.viscous_friction)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact.ViscousFriction | SDFError":
                    _text = el.text or 0.0
                    _viscous_friction = _parse_double(_text)
                    if isinstance(_viscous_friction, SDFError):
                        return _viscous_friction
                    return cls(sdf_version=version, viscous_friction=_viscous_friction)

            def __init__(
                self,
                sdf_version: str | None = None,
                dissipation: "Physics.Simbody.Contact.Dissipation" = None,
                dynamic_friction: "Physics.Simbody.Contact.DynamicFriction" = None,
                override_impact_capture_velocity: "Physics.Simbody.Contact.OverrideImpactCaptureVelocity" = None,
                override_stiction_transition_velocity: "Physics.Simbody.Contact.OverrideStictionTransitionVelocity" = None,
                plastic_coef_restitution: "Physics.Simbody.Contact.PlasticCoefRestitution" = None,
                plastic_impact_velocity: "Physics.Simbody.Contact.PlasticImpactVelocity" = None,
                static_friction: "Physics.Simbody.Contact.StaticFriction" = None,
                stiffness: "Physics.Simbody.Contact.Stiffness" = None,
                viscous_friction: "Physics.Simbody.Contact.ViscousFriction" = None
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
                if self.dissipation is not None:
                    if getattr(self.dissipation, '__version__', None) is None:
                        self.dissipation.__version__ = self.__version__
                    elif getattr(self.dissipation, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.dissipation = self.dissipation.to_version(self.__version__)
                if self.dynamic_friction is not None:
                    if getattr(self.dynamic_friction, '__version__', None) is None:
                        self.dynamic_friction.__version__ = self.__version__
                    elif getattr(self.dynamic_friction, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.dynamic_friction = self.dynamic_friction.to_version(self.__version__)
                if self.override_impact_capture_velocity is not None:
                    if getattr(self.override_impact_capture_velocity, '__version__', None) is None:
                        self.override_impact_capture_velocity.__version__ = self.__version__
                    elif getattr(self.override_impact_capture_velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.override_impact_capture_velocity = self.override_impact_capture_velocity.to_version(self.__version__)
                if self.override_stiction_transition_velocity is not None:
                    if getattr(self.override_stiction_transition_velocity, '__version__', None) is None:
                        self.override_stiction_transition_velocity.__version__ = self.__version__
                    elif getattr(self.override_stiction_transition_velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.override_stiction_transition_velocity = self.override_stiction_transition_velocity.to_version(self.__version__)
                if self.plastic_coef_restitution is not None:
                    if getattr(self.plastic_coef_restitution, '__version__', None) is None:
                        self.plastic_coef_restitution.__version__ = self.__version__
                    elif getattr(self.plastic_coef_restitution, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.plastic_coef_restitution = self.plastic_coef_restitution.to_version(self.__version__)
                if self.plastic_impact_velocity is not None:
                    if getattr(self.plastic_impact_velocity, '__version__', None) is None:
                        self.plastic_impact_velocity.__version__ = self.__version__
                    elif getattr(self.plastic_impact_velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.plastic_impact_velocity = self.plastic_impact_velocity.to_version(self.__version__)
                if self.static_friction is not None:
                    if getattr(self.static_friction, '__version__', None) is None:
                        self.static_friction.__version__ = self.__version__
                    elif getattr(self.static_friction, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.static_friction = self.static_friction.to_version(self.__version__)
                if self.stiffness is not None:
                    if getattr(self.stiffness, '__version__', None) is None:
                        self.stiffness.__version__ = self.__version__
                    elif getattr(self.stiffness, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.stiffness = self.stiffness.to_version(self.__version__)
                if self.viscous_friction is not None:
                    if getattr(self.viscous_friction, '__version__', None) is None:
                        self.viscous_friction.__version__ = self.__version__
                    elif getattr(self.viscous_friction, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.viscous_friction = self.viscous_friction.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Physics.Simbody.Contact":
                kwargs = {"sdf_version": target_version}
                kwargs["dissipation"] = self.dissipation.to_version(target_version) if self.dissipation is not None else None
                kwargs["dynamic_friction"] = self.dynamic_friction.to_version(target_version) if self.dynamic_friction is not None else None
                kwargs["override_impact_capture_velocity"] = self.override_impact_capture_velocity.to_version(target_version) if self.override_impact_capture_velocity is not None else None
                kwargs["override_stiction_transition_velocity"] = self.override_stiction_transition_velocity.to_version(target_version) if self.override_stiction_transition_velocity is not None else None
                kwargs["plastic_coef_restitution"] = self.plastic_coef_restitution.to_version(target_version) if self.plastic_coef_restitution is not None else None
                kwargs["plastic_impact_velocity"] = self.plastic_impact_velocity.to_version(target_version) if self.plastic_impact_velocity is not None else None
                kwargs["static_friction"] = self.static_friction.to_version(target_version) if self.static_friction is not None else None
                kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
                kwargs["viscous_friction"] = self.viscous_friction.to_version(target_version) if self.viscous_friction is not None else None
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("contact")
                if self.dissipation is not None:
                    el.append(self.dissipation.to_sdf(version))
                if self.dynamic_friction is not None:
                    el.append(self.dynamic_friction.to_sdf(version))
                if self.override_impact_capture_velocity is not None:
                    el.append(self.override_impact_capture_velocity.to_sdf(version))
                if self.override_stiction_transition_velocity is not None:
                    el.append(self.override_stiction_transition_velocity.to_sdf(version))
                if self.plastic_coef_restitution is not None:
                    el.append(self.plastic_coef_restitution.to_sdf(version))
                if self.plastic_impact_velocity is not None:
                    el.append(self.plastic_impact_velocity.to_sdf(version))
                if self.static_friction is not None:
                    el.append(self.static_friction.to_sdf(version))
                if self.stiffness is not None:
                    el.append(self.stiffness.to_sdf(version))
                if self.viscous_friction is not None:
                    el.append(self.viscous_friction.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.Contact | SDFError":
                _c_dissipation = el.find("dissipation")
                if _c_dissipation is not None:
                    _res = cls.Dissipation._from_sdf(_c_dissipation, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("dissipation")
                    _dissipation = _res
                else:
                    _dissipation = None
                _c_dynamic_friction = el.find("dynamic_friction")
                if _c_dynamic_friction is not None:
                    _res = cls.DynamicFriction._from_sdf(_c_dynamic_friction, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("dynamic_friction")
                    _dynamic_friction = _res
                else:
                    _dynamic_friction = None
                _c_override_impact_capture_velocity = el.find("override_impact_capture_velocity")
                if _c_override_impact_capture_velocity is not None:
                    _res = cls.OverrideImpactCaptureVelocity._from_sdf(_c_override_impact_capture_velocity, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("override_impact_capture_velocity")
                    _override_impact_capture_velocity = _res
                else:
                    _override_impact_capture_velocity = None
                _c_override_stiction_transition_velocity = el.find("override_stiction_transition_velocity")
                if _c_override_stiction_transition_velocity is not None:
                    _res = cls.OverrideStictionTransitionVelocity._from_sdf(_c_override_stiction_transition_velocity, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("override_stiction_transition_velocity")
                    _override_stiction_transition_velocity = _res
                else:
                    _override_stiction_transition_velocity = None
                _c_plastic_coef_restitution = el.find("plastic_coef_restitution")
                if _c_plastic_coef_restitution is not None:
                    _res = cls.PlasticCoefRestitution._from_sdf(_c_plastic_coef_restitution, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("plastic_coef_restitution")
                    _plastic_coef_restitution = _res
                else:
                    _plastic_coef_restitution = None
                _c_plastic_impact_velocity = el.find("plastic_impact_velocity")
                if _c_plastic_impact_velocity is not None:
                    _res = cls.PlasticImpactVelocity._from_sdf(_c_plastic_impact_velocity, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("plastic_impact_velocity")
                    _plastic_impact_velocity = _res
                else:
                    _plastic_impact_velocity = None
                _c_static_friction = el.find("static_friction")
                if _c_static_friction is not None:
                    _res = cls.StaticFriction._from_sdf(_c_static_friction, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("static_friction")
                    _static_friction = _res
                else:
                    _static_friction = None
                _c_stiffness = el.find("stiffness")
                if _c_stiffness is not None:
                    _res = cls.Stiffness._from_sdf(_c_stiffness, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("stiffness")
                    _stiffness = _res
                else:
                    _stiffness = None
                _c_viscous_friction = el.find("viscous_friction")
                if _c_viscous_friction is not None:
                    _res = cls.ViscousFriction._from_sdf(_c_viscous_friction, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("viscous_friction")
                    _viscous_friction = _res
                else:
                    _viscous_friction = None
                return cls(sdf_version=version, dissipation=_dissipation, dynamic_friction=_dynamic_friction, override_impact_capture_velocity=_override_impact_capture_velocity, override_stiction_transition_velocity=_override_stiction_transition_velocity, plastic_coef_restitution=_plastic_coef_restitution, plastic_impact_velocity=_plastic_impact_velocity, static_friction=_static_friction, stiffness=_stiffness, viscous_friction=_viscous_friction)

        class MaxTransientVelocity(BaseModel):
            def __init__(self, sdf_version: str | None = None, max_transient_velocity: float = 0.01):
                super().__init__(sdf_version)
                self.max_transient_velocity = max_transient_velocity

            def to_version(self, target_version: str) -> "Physics.Simbody.MaxTransientVelocity":
                kwargs = {"sdf_version": target_version}
                kwargs["max_transient_velocity"] = self.max_transient_velocity
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("max_transient_velocity")
                if self.max_transient_velocity is not None:
                    el.text = str(self.max_transient_velocity)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody.MaxTransientVelocity | SDFError":
                _text = el.text or 0.01
                _max_transient_velocity = _parse_double(_text)
                if isinstance(_max_transient_velocity, SDFError):
                    return _max_transient_velocity
                return cls(sdf_version=version, max_transient_velocity=_max_transient_velocity)

        def __init__(
            self,
            sdf_version: str | None = None,
            accuracy: "Physics.Simbody.Accuracy" = None,
            contact: "Physics.Simbody.Contact" = None,
            max_transient_velocity: "Physics.Simbody.MaxTransientVelocity" = None,
            min_step_size: "MinStepSize" = None
        ):
            super().__init__(sdf_version)
            self.accuracy = accuracy
            self.contact = contact
            self.max_transient_velocity = max_transient_velocity
            self.min_step_size = min_step_size
            if self.accuracy is not None:
                if getattr(self.accuracy, '__version__', None) is None:
                    self.accuracy.__version__ = self.__version__
                elif getattr(self.accuracy, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.accuracy = self.accuracy.to_version(self.__version__)
            if self.contact is not None:
                if getattr(self.contact, '__version__', None) is None:
                    self.contact.__version__ = self.__version__
                elif getattr(self.contact, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.contact = self.contact.to_version(self.__version__)
            if self.max_transient_velocity is not None:
                if getattr(self.max_transient_velocity, '__version__', None) is None:
                    self.max_transient_velocity.__version__ = self.__version__
                elif getattr(self.max_transient_velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.max_transient_velocity = self.max_transient_velocity.to_version(self.__version__)
            if self.min_step_size is not None:
                if getattr(self.min_step_size, '__version__', None) is None:
                    self.min_step_size.__version__ = self.__version__
                elif getattr(self.min_step_size, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.min_step_size = self.min_step_size.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Physics.Simbody":
            kwargs = {"sdf_version": target_version}
            kwargs["accuracy"] = self.accuracy.to_version(target_version) if self.accuracy is not None else None
            kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
            kwargs["max_transient_velocity"] = self.max_transient_velocity.to_version(target_version) if self.max_transient_velocity is not None else None
            kwargs["min_step_size"] = self.min_step_size.to_version(target_version) if self.min_step_size is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("simbody")
            if self.accuracy is not None:
                el.append(self.accuracy.to_sdf(version))
            if self.contact is not None:
                el.append(self.contact.to_sdf(version))
            if self.max_transient_velocity is not None:
                el.append(self.max_transient_velocity.to_sdf(version))
            if self.min_step_size is not None:
                el.append(self.min_step_size.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.Simbody | SDFError":
            _c_accuracy = el.find("accuracy")
            if _c_accuracy is not None:
                _res = cls.Accuracy._from_sdf(_c_accuracy, version)
                if isinstance(_res, SDFError):
                    return _res.extend("accuracy")
                _accuracy = _res
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
            _c_max_transient_velocity = el.find("max_transient_velocity")
            if _c_max_transient_velocity is not None:
                _res = cls.MaxTransientVelocity._from_sdf(_c_max_transient_velocity, version)
                if isinstance(_res, SDFError):
                    return _res.extend("max_transient_velocity")
                _max_transient_velocity = _res
            else:
                _max_transient_velocity = None
            _c_min_step_size = el.find("min_step_size")
            if _c_min_step_size is not None:
                _res = MinStepSize._from_sdf(_c_min_step_size, version)
                if isinstance(_res, SDFError):
                    return _res.extend("min_step_size")
                _min_step_size = _res
            else:
                _min_step_size = None
            return cls(sdf_version=version, accuracy=_accuracy, contact=_contact, max_transient_velocity=_max_transient_velocity, min_step_size=_min_step_size)

    class UpdateRate(BaseModel):
        def __init__(self, sdf_version: str | None = None, update_rate: float = 1000):
            super().__init__(sdf_version)
            self.update_rate = update_rate

        def to_version(self, target_version: str) -> "Physics.UpdateRate":
            if self.update_rate is not None and cmp_version(target_version, "1.2") < 0:
                raise ValueError(f"'update_rate' is not supported in SDF version {target_version} (added in 1.2)")
            if self.update_rate is not None and cmp_version(target_version, "1.4") >= 0:
                raise ValueError(f"'update_rate' is not supported in SDF version {target_version} (removed in 1.4)")
            kwargs = {"sdf_version": target_version}
            kwargs["update_rate"] = self.update_rate
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("update_rate")
            if self.update_rate is not None:
                el.text = str(self.update_rate)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Physics.UpdateRate | SDFError":
            _text = el.text or 1000
            _update_rate = _parse_double(_text)
            if isinstance(_update_rate, SDFError):
                return _update_rate
            if _update_rate is not None and cmp_version(version, "1.2") < 0:
                if _update_rate != 1000:
                    return SDFError(f"'update_rate' is not supported in SDF version {version} (added in 1.2)")
            return cls(sdf_version=version, update_rate=_update_rate)

    _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

    def __init__(
        self,
        sdf_version: str | None = None,
        bullet: "Physics.Bullet" = None,
        dart: "Physics.Dart" = None,
        default: bool = False,
        gravity: "Physics.Gravity" = None,
        magnetic_field: "Physics.MagneticField" = None,
        max_contacts: "Physics.MaxContacts" = None,
        max_step_size: "Physics.MaxStepSize" = None,
        name: str = "default_physics",
        ode: "Physics.Ode" = None,
        real_time_factor: "Physics.RealTimeFactor" = None,
        real_time_update_rate: "Physics.RealTimeUpdateRate" = None,
        simbody: "Physics.Simbody" = None,
        type: str = "ode",
        update_rate: float = 0
    ):
        super().__init__(sdf_version)
        self.bullet = bullet
        self.dart = dart
        self.default = default
        self.gravity = gravity
        self.magnetic_field = magnetic_field
        self.max_contacts = max_contacts
        self.max_step_size = max_step_size
        self.name = name
        self.ode = ode
        self.real_time_factor = real_time_factor
        self.real_time_update_rate = real_time_update_rate
        self.simbody = simbody
        self.type = type
        self.update_rate = update_rate
        if self.bullet is not None:
            if getattr(self.bullet, '__version__', None) is None:
                self.bullet.__version__ = self.__version__
            elif getattr(self.bullet, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.bullet = self.bullet.to_version(self.__version__)
        if self.dart is not None:
            if getattr(self.dart, '__version__', None) is None:
                self.dart.__version__ = self.__version__
            elif getattr(self.dart, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.dart = self.dart.to_version(self.__version__)
        if self.gravity is not None:
            if getattr(self.gravity, '__version__', None) is None:
                self.gravity.__version__ = self.__version__
            elif getattr(self.gravity, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.gravity = self.gravity.to_version(self.__version__)
        if self.magnetic_field is not None:
            if getattr(self.magnetic_field, '__version__', None) is None:
                self.magnetic_field.__version__ = self.__version__
            elif getattr(self.magnetic_field, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.magnetic_field = self.magnetic_field.to_version(self.__version__)
        if self.max_contacts is not None:
            if getattr(self.max_contacts, '__version__', None) is None:
                self.max_contacts.__version__ = self.__version__
            elif getattr(self.max_contacts, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.max_contacts = self.max_contacts.to_version(self.__version__)
        if self.max_step_size is not None:
            if getattr(self.max_step_size, '__version__', None) is None:
                self.max_step_size.__version__ = self.__version__
            elif getattr(self.max_step_size, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.max_step_size = self.max_step_size.to_version(self.__version__)
        if self.ode is not None:
            if getattr(self.ode, '__version__', None) is None:
                self.ode.__version__ = self.__version__
            elif getattr(self.ode, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.ode = self.ode.to_version(self.__version__)
        if self.real_time_factor is not None:
            if getattr(self.real_time_factor, '__version__', None) is None:
                self.real_time_factor.__version__ = self.__version__
            elif getattr(self.real_time_factor, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.real_time_factor = self.real_time_factor.to_version(self.__version__)
        if self.real_time_update_rate is not None:
            if getattr(self.real_time_update_rate, '__version__', None) is None:
                self.real_time_update_rate.__version__ = self.__version__
            elif getattr(self.real_time_update_rate, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.real_time_update_rate = self.real_time_update_rate.to_version(self.__version__)
        if self.simbody is not None:
            if getattr(self.simbody, '__version__', None) is None:
                self.simbody.__version__ = self.__version__
            elif getattr(self.simbody, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.simbody = self.simbody.to_version(self.__version__)

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
        if self.update_rate is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'update_rate' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["dart"] = self.dart.to_version(target_version) if self.dart is not None else None
        kwargs["default"] = self.default
        kwargs["gravity"] = self.gravity.to_version(target_version) if self.gravity is not None else None
        kwargs["magnetic_field"] = self.magnetic_field.to_version(target_version) if self.magnetic_field is not None else None
        kwargs["max_contacts"] = self.max_contacts.to_version(target_version) if self.max_contacts is not None else None
        kwargs["max_step_size"] = self.max_step_size.to_version(target_version) if self.max_step_size is not None else None
        kwargs["name"] = self.name
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["real_time_factor"] = self.real_time_factor.to_version(target_version) if self.real_time_factor is not None else None
        kwargs["real_time_update_rate"] = self.real_time_update_rate.to_version(target_version) if self.real_time_update_rate is not None else None
        kwargs["simbody"] = self.simbody.to_version(target_version) if self.simbody is not None else None
        kwargs["type"] = self.type
        kwargs["update_rate"] = self.update_rate
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("physics")
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.dart is not None:
            el.append(self.dart.to_sdf(version))
        if self.default is not None:
            el.set("default", str(self.default).lower())
        if self.gravity is not None:
            el.append(self.gravity.to_sdf(version))
        if self.magnetic_field is not None:
            el.append(self.magnetic_field.to_sdf(version))
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf(version))
        if self.max_step_size is not None:
            el.append(self.max_step_size.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.real_time_factor is not None:
            el.append(self.real_time_factor.to_sdf(version))
        if self.real_time_update_rate is not None:
            el.append(self.real_time_update_rate.to_sdf(version))
        if self.simbody is not None:
            el.append(self.simbody.to_sdf(version))
        if self.type is not None:
            el.set("type", self.type)
        if self.update_rate is not None:
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
        _default = str(el.get("default", False)).strip().lower() == 'true'
        if isinstance(_default, SDFError):
            return _default.extend("@default")
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
        _c_magnetic_field = el.find("magnetic_field")
        if _c_magnetic_field is not None:
            _res = cls.MagneticField._from_sdf(_c_magnetic_field, version)
            if isinstance(_res, SDFError):
                return _res.extend("magnetic_field")
            _magnetic_field = _res
        else:
            _magnetic_field = None
        if _magnetic_field is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'magnetic_field' is not supported in SDF version {version} (added in 1.5)")
        _c_max_contacts = el.find("max_contacts")
        if _c_max_contacts is not None:
            _res = cls.MaxContacts._from_sdf(_c_max_contacts, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_contacts")
            _max_contacts = _res
        else:
            _max_contacts = None
        _c_max_step_size = el.find("max_step_size")
        if _c_max_step_size is not None:
            _res = cls.MaxStepSize._from_sdf(_c_max_step_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_step_size")
            _max_step_size = _res
        else:
            _max_step_size = None
        if _max_step_size is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'max_step_size' is not supported in SDF version {version} (added in 1.4)")
        _name = el.get("name", "default_physics")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
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
        _c_real_time_factor = el.find("real_time_factor")
        if _c_real_time_factor is not None:
            _res = cls.RealTimeFactor._from_sdf(_c_real_time_factor, version)
            if isinstance(_res, SDFError):
                return _res.extend("real_time_factor")
            _real_time_factor = _res
        else:
            _real_time_factor = None
        if _real_time_factor is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'real_time_factor' is not supported in SDF version {version} (added in 1.4)")
        _c_real_time_update_rate = el.find("real_time_update_rate")
        if _c_real_time_update_rate is not None:
            _res = cls.RealTimeUpdateRate._from_sdf(_c_real_time_update_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("real_time_update_rate")
            _real_time_update_rate = _res
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
        _type = el.get("type", "ode")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _update_rate = _parse_double(el.get("update_rate", 0))
        if isinstance(_update_rate, SDFError):
            return _update_rate.extend("@update_rate")
        return cls(sdf_version=version, bullet=_bullet, dart=_dart, default=_default, gravity=_gravity, magnetic_field=_magnetic_field, max_contacts=_max_contacts, max_step_size=_max_step_size, name=_name, ode=_ode, real_time_factor=_real_time_factor, real_time_update_rate=_real_time_update_rate, simbody=_simbody, type=_type, update_rate=_update_rate)
