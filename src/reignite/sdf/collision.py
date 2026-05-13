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



class Collision(BaseModel):
    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _SDFPose = None):
            super().__init__(sdf_version)
            if pose is None:
                pose = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
            self.pose = pose

        def to_version(self, target_version: str) -> "Collision.Origin":
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Collision.Origin | SDFError":
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

    def __init__(
        self,
        sdf_version: str | None = None,
        auto_inertia_params: None = None,
        density: float = 1000.0,
        frames: List["Frame"] = None,
        geometry: "Geometry" = None,
        laser_retro: float = 0,
        mass: float = 0,
        max_contacts: int = 10,
        name: str = "__default__",
        origin: "Collision.Origin" = None,
        pose: "Pose" = None,
        surface: "Surface" = None
    ):
        super().__init__(sdf_version)
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
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        if self.geometry is not None and hasattr(self.geometry, 'to_version'):
            if getattr(self.geometry, '__version__', None) is None:
                self.geometry.__version__ = self.__version__
            elif getattr(self.geometry, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.geometry = self.geometry.to_version(self.__version__)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, '__version__', None) is None:
                self.origin.__version__ = self.__version__
            elif getattr(self.origin, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.origin = self.origin.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)
        if self.surface is not None and hasattr(self.surface, 'to_version'):
            if getattr(self.surface, '__version__', None) is None:
                self.surface.__version__ = self.__version__
            elif getattr(self.surface, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.surface = self.surface.to_version(self.__version__)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

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
        kwargs["auto_inertia_params"] = self.auto_inertia_params
        kwargs["density"] = self.density
        kwargs["frames"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])]
        kwargs["geometry"] = self.geometry.to_version(target_version) if hasattr(self.geometry, "to_version") else self.geometry
        kwargs["laser_retro"] = self.laser_retro
        kwargs["mass"] = self.mass
        kwargs["max_contacts"] = self.max_contacts
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if hasattr(self.origin, "to_version") else self.origin
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
        kwargs["surface"] = self.surface.to_version(target_version) if hasattr(self.surface, "to_version") else self.surface
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
            _c_tmp = ET.Element("auto_inertia_params")
            _c_tmp.text = str(self.auto_inertia_params)
            el.append(_c_tmp)
        if self.density is not None:
            _c_tmp = ET.Element("density")
            _c_tmp.text = str(self.density)
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
        if self.geometry is None:
            self.geometry = Geometry(sdf_version=version)
        if self.geometry is not None:
            if hasattr(self.geometry, 'to_sdf'):
                _child_res = self.geometry.to_sdf(version)
            else:
                _child_res = str(self.geometry)
            if isinstance(_child_res, str):
                _item_el = ET.Element('geometry')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.laser_retro is not None:
            el.set("laser_retro", str(self.laser_retro))
        if self.mass is not None:
            _c_tmp = ET.Element("mass")
            _c_tmp.text = str(self.mass)
            el.append(_c_tmp)
        if self.max_contacts is not None:
            _c_tmp = ET.Element("max_contacts")
            _c_tmp.text = str(self.max_contacts)
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
        if self.surface is not None:
            if hasattr(self.surface, 'to_sdf'):
                _child_res = self.surface.to_sdf(version)
            else:
                _child_res = str(self.surface)
            if isinstance(_child_res, str):
                _item_el = ET.Element('surface')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Collision | SDFError":
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.pose import Pose
        from ..elements.surface import Surface
        _c_tmp = el.find("auto_inertia_params")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else None
            _val = str(_text)
            if isinstance(_val, SDFError):
                return _val.extend("auto_inertia_params")
            _auto_inertia_params = _val
        else:
            _auto_inertia_params = None
        if _auto_inertia_params is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'auto_inertia_params' is not supported in SDF version {version} (added in 1.11)")
        _c_tmp = el.find("density")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1000.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("density")
            _density = _val
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
        _c_tmp = el.find("mass")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("mass")
            _mass = _val
        else:
            _mass = None
        _c_tmp = el.find("max_contacts")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 10
            _val = _parse_int32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("max_contacts")
            _max_contacts = _val
        else:
            _max_contacts = None
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
