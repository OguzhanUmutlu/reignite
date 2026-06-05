### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_int32
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.geometry import Geometry
    from ..elements.pose import Pose
    from ..elements.surface import Surface

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Collision(BaseModel):
    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Collision.Origin":
            kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
            return Collision.Origin(**kwargs)

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
                    _c_tmp.text = str(self.pose)
                    el.append(_c_tmp)
                else:
                    el.set("pose", str(self.pose))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Collision.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is not None:
                _pose = _parse_pose(_raw_pose)
                if isinstance(_pose, SDFError):
                    return _pose.extend("@pose")
            else:
                _pose = None
            return cls(sdf_version=version, pose=_pose)

    def __init__(
        self,
        sdf_version: str | None = None,
        auto_inertia_params: None | None = None,
        density: float | None = None,
        frames: List["Frame"] = None,
        geometry: "Geometry" = None,
        laser_retro: float | None = None,
        mass: float | None = None,
        max_contacts: int | None = None,
        name: str | None = None,
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
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.geometry is not None and hasattr(self.geometry, 'to_version'):
            if getattr(self.geometry, 'sdfversion', None) is None:
                self.geometry.sdfversion = self.sdfversion
            elif getattr(self.geometry, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.geometry = self.geometry.to_version(self.sdfversion)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, 'sdfversion', None) is None:
                self.origin.sdfversion = self.sdfversion
            elif getattr(self.origin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.origin = self.origin.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)
        if self.surface is not None and hasattr(self.surface, 'to_version'):
            if getattr(self.surface, 'sdfversion', None) is None:
                self.surface.sdfversion = self.sdfversion
            elif getattr(self.surface, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.surface = self.surface.to_version(self.sdfversion)

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
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.mass is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'mass' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs: dict = {"sdf_version": target_version, "auto_inertia_params": self.auto_inertia_params, "density": self.density, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "geometry": self.geometry.to_version(target_version) if self.geometry is not None and hasattr(self.geometry, "to_version") else self.geometry, "laser_retro": self.laser_retro, "mass": self.mass, "max_contacts": self.max_contacts, "name": self.name, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "surface": self.surface.to_version(target_version) if self.surface is not None and hasattr(self.surface, "to_version") else self.surface}
        return Collision(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.pose import Pose
        from ..elements.surface import Surface
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
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
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.geometry is not None:
            _child_res = self.geometry.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('geometry')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.laser_retro is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("laser_retro")
                _c_tmp.text = str(self.laser_retro)
                el.append(_c_tmp)
            else:
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
            _child_res = self.origin.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('origin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _child_res = self.pose.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.surface is not None:
            _child_res = self.surface.to_sdf(version)
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
            _geometry = None
        _raw_laser_retro = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("laser_retro")
            if _c_tmp is not None: _raw_laser_retro = _c_tmp.text
        else:
            _raw_laser_retro = el.get("laser_retro")
        if _raw_laser_retro is not None:
            _laser_retro = _parse_double(_raw_laser_retro)
            if isinstance(_laser_retro, SDFError):
                return _laser_retro.extend("@laser_retro")
        else:
            _laser_retro = None
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
