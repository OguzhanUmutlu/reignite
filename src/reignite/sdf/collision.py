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
    from ..elements.frame import Frame
    from ..elements.geometry import Geometry
    from ..elements.pose import Pose
    from ..elements.surface import Surface


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



class AutoInertiaParams(BaseModel):
    def __init__(self, sdf_version: str | None = None):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "AutoInertiaParams":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("auto_inertia_params")
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Collision(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        auto_inertia_params: "AutoInertiaParams" = None,
        density: "Density" = None,
        frames: List["Frame"] = None,
        geometry: "Geometry" = None,
        laser_retro: float = 0,
        mass: "Mass" = None,
        max_contacts: "MaxContacts" = None,
        name: str = "__default__",
        origin: "Origin" = None,
        pose: "Pose" = None,
        surface: "Surface" = None
    ):
        self.__version__ = sdf_version
        self.auto_inertia_params = auto_inertia_params
        self.density = density
        self.frames = frames or []
        self.geometry = geometry
        self.laser_retro = laser_retro
        self.mass = mass
        self.max_contacts = max_contacts
        self.name = name
        self.origin = origin
        self.pose = pose
        self.surface = surface
        if self.auto_inertia_params is not None:
            if getattr(self.auto_inertia_params, '__version__', None) is None:
                self.auto_inertia_params.__version__ = self.__version__
            elif getattr(self.auto_inertia_params, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.auto_inertia_params = self.auto_inertia_params.to_version(self.__version__)
        if self.density is not None:
            if getattr(self.density, '__version__', None) is None:
                self.density.__version__ = self.__version__
            elif getattr(self.density, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.density = self.density.to_version(self.__version__)
        for _i, _c in enumerate(self.frames):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        if self.geometry is not None:
            if getattr(self.geometry, '__version__', None) is None:
                self.geometry.__version__ = self.__version__
            elif getattr(self.geometry, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.geometry = self.geometry.to_version(self.__version__)
        if self.mass is not None:
            if getattr(self.mass, '__version__', None) is None:
                self.mass.__version__ = self.__version__
            elif getattr(self.mass, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.mass = self.mass.to_version(self.__version__)
        if self.max_contacts is not None:
            if getattr(self.max_contacts, '__version__', None) is None:
                self.max_contacts.__version__ = self.__version__
            elif getattr(self.max_contacts, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.max_contacts = self.max_contacts.to_version(self.__version__)
        if self.origin is not None:
            if getattr(self.origin, '__version__', None) is None:
                self.origin.__version__ = self.__version__
            elif getattr(self.origin, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.origin = self.origin.to_version(self.__version__)
        if self.pose is not None:
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)
        if self.surface is not None:
            if getattr(self.surface, '__version__', None) is None:
                self.surface.__version__ = self.__version__
            elif getattr(self.surface, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.surface = self.surface.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Collision":
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.pose import Pose
        from ..elements.surface import Surface
        if self.auto_inertia_params is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'auto_inertia_params' is not supported in SDF version {target_version} (added in 1.11)")
        if self.density is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.11)")
        if self.frames is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.laser_retro is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'laser_retro' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.mass is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'mass' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["auto_inertia_params"] = self.auto_inertia_params.to_version(target_version) if self.auto_inertia_params is not None else None
        kwargs["density"] = self.density.to_version(target_version) if self.density is not None else None
        kwargs["frames"] = [c.to_version(target_version) for c in (self.frames or [])]
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["laser_retro"] = self.laser_retro
        kwargs["mass"] = self.mass.to_version(target_version) if self.mass is not None else None
        kwargs["max_contacts"] = self.max_contacts.to_version(target_version) if self.max_contacts is not None else None
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["surface"] = self.surface.to_version(target_version) if self.surface is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.pose import Pose
        from ..elements.surface import Surface
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("collision")
        if self.auto_inertia_params is not None:
            el.append(self.auto_inertia_params.to_sdf(version))
        if self.density is not None:
            el.append(self.density.to_sdf(version))
        for item in (self.frames or []):
            el.append(item.to_sdf(version))
        if self.geometry is None:
            self.geometry = Geometry(sdf_version=version)
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.laser_retro is not None:
            el.set("laser_retro", str(self.laser_retro))
        if self.mass is not None:
            el.append(self.mass.to_sdf(version))
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.surface is not None:
            el.append(self.surface.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.pose import Pose
        from ..elements.surface import Surface
        _c_auto_inertia_params = el.find("auto_inertia_params")
        if _c_auto_inertia_params is not None:
            _res = AutoInertiaParams._from_sdf(_c_auto_inertia_params, version)
            if isinstance(_res, SDFError):
                return _res.extend("auto_inertia_params")
            _auto_inertia_params = _res
        else:
            _auto_inertia_params = None
        if _auto_inertia_params is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'auto_inertia_params' is not supported in SDF version {version} (added in 1.11)")
        _c_density = el.find("density")
        if _c_density is not None:
            _res = Density._from_sdf(_c_density, version)
            if isinstance(_res, SDFError):
                return _res.extend("density")
            _density = _res
        else:
            _density = None
        if _density is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'density' is not supported in SDF version {version} (added in 1.11)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _c_geometry = el.find("geometry")
        if _c_geometry is not None:
            _res = Geometry._from_sdf(_c_geometry, version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        else:
            _res = Geometry._from_sdf(ET.Element("geometry"), version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        _laser_retro = _parse_double(el.get("laser_retro", 0))
        if isinstance(_laser_retro, SDFError):
            return _laser_retro.extend("@laser_retro")
        _c_mass = el.find("mass")
        if _c_mass is not None:
            _res = Mass._from_sdf(_c_mass, version)
            if isinstance(_res, SDFError):
                return _res.extend("mass")
            _mass = _res
        else:
            _mass = None
        _c_max_contacts = el.find("max_contacts")
        if _c_max_contacts is not None:
            _res = MaxContacts._from_sdf(_c_max_contacts, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_contacts")
            _max_contacts = _res
        else:
            _max_contacts = None
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
        _c_surface = el.find("surface")
        if _c_surface is not None:
            _res = Surface._from_sdf(_c_surface, version)
            if isinstance(_res, SDFError):
                return _res.extend("surface")
            _surface = _res
        else:
            _surface = None
        return cls(sdf_version=version, auto_inertia_params=_auto_inertia_params, density=_density, frames=_frames, geometry=_geometry, laser_retro=_laser_retro, mass=_mass, max_contacts=_max_contacts, name=_name, origin=_origin, pose=_pose, surface=_surface)


class Density(BaseModel):
    def __init__(self, sdf_version: str | None = None, density: float = 1000.0):
        self.__version__ = sdf_version
        self.density = density

    def to_version(self, target_version: str) -> "Density":
        if self.density is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["density"] = self.density
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("density")
        if self.density is not None:
            el.text = str(self.density)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1000.0
        _density = _parse_double(_text)
        if isinstance(_density, SDFError):
            return _density
        if _density is not None and cmp_version(version, "1.11") < 0:
            if _density != 1000.0:
                return SDFError(f"'density' is not supported in SDF version {version} (added in 1.11)")
        return cls(sdf_version=version, density=_density)


class LaserRetro(BaseModel):
    def __init__(self, sdf_version: str | None = None, laser_retro: float = 0):
        self.__version__ = sdf_version
        self.laser_retro = laser_retro

    def to_version(self, target_version: str) -> "LaserRetro":
        if self.laser_retro is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'laser_retro' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["laser_retro"] = self.laser_retro
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("laser_retro")
        if self.laser_retro is not None:
            el.text = str(self.laser_retro)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _laser_retro = _parse_double(_text)
        if isinstance(_laser_retro, SDFError):
            return _laser_retro
        if _laser_retro is not None and cmp_version(version, "1.2") < 0:
            if _laser_retro != 0:
                return SDFError(f"'laser_retro' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, laser_retro=_laser_retro)


class Mass(BaseModel):
    def __init__(self, sdf_version: str | None = None, mass: float = 0):
        self.__version__ = sdf_version
        self.mass = mass

    def to_version(self, target_version: str) -> "Mass":
        if self.mass is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'mass' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mass"] = self.mass
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("mass")
        if self.mass is not None:
            el.text = str(self.mass)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _mass = _parse_double(_text)
        if isinstance(_mass, SDFError):
            return _mass
        return cls(sdf_version=version, mass=_mass)


class MaxContacts(BaseModel):
    def __init__(self, sdf_version: str | None = None, max_contacts: int = 10):
        self.__version__ = sdf_version
        self.max_contacts = max_contacts

    def to_version(self, target_version: str) -> "MaxContacts":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _max_contacts = _parse_int32(_text)
        if isinstance(_max_contacts, SDFError):
            return _max_contacts
        return cls(sdf_version=version, max_contacts=_max_contacts)


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
