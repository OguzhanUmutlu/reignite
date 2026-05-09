from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ._base import Model
from ..utils.color import Color
from ..utils.pose import Pose
from ..utils.vector3 import Vector3
from ..utils.version import cmp_version


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



class ViewController(Model):
    def __init__(self, sdf_version: str, view_controller: str = "oribit"):
        self.__version__ = sdf_version
        self.view_controller = view_controller

    def to_version(self, target_version: str) -> "ViewController":
        kwargs = {"sdf_version": target_version}
        kwargs["view_controller"] = self.view_controller
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("view_controller")
        if self.view_controller is not None:
            el.text = self.view_controller
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ViewController":
        _text = el.text or "oribit"
        _view_controller = _text
        return cls(sdf_version=version, view_controller=_view_controller)


class Origin(Model):
    def __init__(self, sdf_version: str, pose: Pose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Origin":
        _pose = Pose.from_sdf(el.get("pose", "0 0 0 0 0 0"))
        return cls(sdf_version=version, pose=_pose)


class Name(Model):
    def __init__(self, sdf_version: str, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "Name":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Name":
        _text = el.text or "__default__"
        _name = _text
        return cls(sdf_version=version, name=_name)


class MinDist(Model):
    def __init__(self, sdf_version: str, min_dist: float = 0):
        self.__version__ = sdf_version
        self.min_dist = min_dist

    def to_version(self, target_version: str) -> "MinDist":
        kwargs = {"sdf_version": target_version}
        kwargs["min_dist"] = self.min_dist
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_dist")
        if self.min_dist is not None:
            el.text = str(self.min_dist)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinDist":
        _text = el.text or 0
        _min_dist = _parse_double(_text)
        return cls(sdf_version=version, min_dist=_min_dist)


class MaxDist(Model):
    def __init__(self, sdf_version: str, max_dist: float = 0):
        self.__version__ = sdf_version
        self.max_dist = max_dist

    def to_version(self, target_version: str) -> "MaxDist":
        kwargs = {"sdf_version": target_version}
        kwargs["max_dist"] = self.max_dist
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_dist")
        if self.max_dist is not None:
            el.text = str(self.max_dist)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxDist":
        _text = el.text or 0
        _max_dist = _parse_double(_text)
        return cls(sdf_version=version, max_dist=_max_dist)


class TrackVisual(Model):
    def __init__(
        self,
        sdf_version: str,
        name: "Name" = None,
        min_dist: "MinDist" = None,
        max_dist: "MaxDist" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.min_dist = min_dist
        self.max_dist = max_dist

    def to_version(self, target_version: str) -> "TrackVisual":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["min_dist"] = self.min_dist.to_version(target_version) if self.min_dist is not None else None
        kwargs["max_dist"] = self.max_dist.to_version(target_version) if self.max_dist is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("track_visual")
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        if self.min_dist is not None:
            el.append(self.min_dist.to_sdf(version))
        if self.max_dist is not None:
            el.append(self.max_dist.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "TrackVisual":
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name, version) if _c_name is not None else None
        _c_min_dist = el.find("min_dist")
        _min_dist = MinDist.from_sdf(_c_min_dist, version) if _c_min_dist is not None else None
        _c_max_dist = el.find("max_dist")
        _max_dist = MaxDist.from_sdf(_c_max_dist, version) if _c_max_dist is not None else None
        return cls(sdf_version=version, name=_name, min_dist=_min_dist, max_dist=_max_dist)


class Pose(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(self, sdf_version: str, pose: Pose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "Pose":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        if _pose is not None and cmp_version(version, "1.2") < 0:
            if _pose != "0 0 0 0 0 0":
                raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, pose=_pose)


class Camera(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "user_camera",
        view_controller: "ViewController" = None,
        origin: "Origin" = None,
        track_visual: "TrackVisual" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.view_controller = view_controller
        self.origin = origin
        self.track_visual = track_visual
        self.pose = pose

    def to_version(self, target_version: str) -> "Camera":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["view_controller"] = self.view_controller.to_version(target_version) if self.view_controller is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["track_visual"] = self.track_visual.to_version(target_version) if self.track_visual is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera")
        if self.name is not None:
            el.set("name", self.name)
        if self.view_controller is not None:
            el.append(self.view_controller.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.track_visual is not None:
            el.append(self.track_visual.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Camera":
        _name = el.get("name", "user_camera")
        _c_view_controller = el.find("view_controller")
        _view_controller = ViewController.from_sdf(_c_view_controller, version) if _c_view_controller is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_track_visual = el.find("track_visual")
        _track_visual = TrackVisual.from_sdf(_c_track_visual, version) if _c_track_visual is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, view_controller=_view_controller, origin=_origin, track_visual=_track_visual, pose=_pose)


class Gui(Model):
    def __init__(self, sdf_version: str, fullscreen: bool = False, camera: "Camera" = None):
        self.__version__ = sdf_version
        self.fullscreen = fullscreen
        self.camera = camera

    def to_version(self, target_version: str) -> "Gui":
        kwargs = {"sdf_version": target_version}
        kwargs["fullscreen"] = self.fullscreen
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gui")
        if self.fullscreen is not None:
            el.set("fullscreen", str(self.fullscreen).lower())
        if self.camera is not None:
            el.append(self.camera.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gui":
        _fullscreen = el.get("fullscreen", False).strip().lower() == 'true'
        _c_camera = el.find("camera")
        _camera = Camera.from_sdf(_c_camera, version) if _c_camera is not None else None
        return cls(sdf_version=version, fullscreen=_fullscreen, camera=_camera)


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


class Bullet(Model):
    def __init__(self, sdf_version: str, dt: "Dt" = None):
        self.__version__ = sdf_version
        self.dt = dt

    def to_version(self, target_version: str) -> "Bullet":
        kwargs = {"sdf_version": target_version}
        kwargs["dt"] = self.dt.to_version(target_version) if self.dt is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bullet")
        if self.dt is not None:
            el.append(self.dt.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Bullet":
        _c_dt = el.find("dt")
        _dt = Dt.from_sdf(_c_dt, version) if _c_dt is not None else None
        return cls(sdf_version=version, dt=_dt)


class Type(Model):
    def __init__(self, sdf_version: str, type: str = "quick"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Type":
        if self.type is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'type' is not supported in SDF version {target_version} (added in 1.2)")
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
        _text = el.text or "quick"
        _type = _text
        if _type is not None and cmp_version(version, "1.2") < 0:
            if _type != "quick":
                raise ValueError(f"'type' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, type=_type)


class Iters(Model):
    def __init__(self, sdf_version: str, iters: int = 50):
        self.__version__ = sdf_version
        self.iters = iters

    def to_version(self, target_version: str) -> "Iters":
        if self.iters is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'iters' is not supported in SDF version {target_version} (added in 1.2)")
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
        if _iters is not None and cmp_version(version, "1.2") < 0:
            if _iters != 50:
                raise ValueError(f"'iters' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, iters=_iters)


class PreconIters(Model):
    def __init__(self, sdf_version: str, precon_iters: int = 0):
        self.__version__ = sdf_version
        self.precon_iters = precon_iters

    def to_version(self, target_version: str) -> "PreconIters":
        if self.precon_iters is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'precon_iters' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["precon_iters"] = self.precon_iters
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("precon_iters")
        if self.precon_iters is not None:
            el.text = str(self.precon_iters)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PreconIters":
        _text = el.text or 0
        _precon_iters = _parse_int32(_text)
        if _precon_iters is not None and cmp_version(version, "1.2") < 0:
            if _precon_iters != 0:
                raise ValueError(f"'precon_iters' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, precon_iters=_precon_iters)


class Sor(Model):
    def __init__(self, sdf_version: str, sor: float = 1.3):
        self.__version__ = sdf_version
        self.sor = sor

    def to_version(self, target_version: str) -> "Sor":
        if self.sor is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'sor' is not supported in SDF version {target_version} (added in 1.2)")
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
        if _sor is not None and cmp_version(version, "1.2") < 0:
            if _sor != 1.3:
                raise ValueError(f"'sor' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, sor=_sor)


class Solver(Model):
    def __init__(
        self,
        sdf_version: str,
        type: str = "quick",
        dt: float = 0.001,
        iters: int = 50,
        precon_iters: int = 0,
        sor: float = 1.3
    ):
        self.__version__ = sdf_version
        self.type = type
        self.dt = dt
        self.iters = iters
        self.precon_iters = precon_iters
        self.sor = sor

    def to_version(self, target_version: str) -> "Solver":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["dt"] = self.dt
        kwargs["iters"] = self.iters
        kwargs["precon_iters"] = self.precon_iters
        kwargs["sor"] = self.sor
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("solver")
        if self.type is not None:
            el.set("type", self.type)
        if self.dt is not None:
            el.set("dt", str(self.dt))
        if self.iters is not None:
            el.set("iters", str(self.iters))
        if self.precon_iters is not None:
            el.set("precon_iters", str(self.precon_iters))
        if self.sor is not None:
            el.set("sor", str(self.sor))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Solver":
        _type = el.get("type", "quick")
        _dt = _parse_double(el.get("dt", 0.001))
        _iters = _parse_int32(el.get("iters", 50))
        _precon_iters = _parse_int32(el.get("precon_iters", 0))
        _sor = _parse_double(el.get("sor", 1.3))
        return cls(sdf_version=version, type=_type, dt=_dt, iters=_iters, precon_iters=_precon_iters, sor=_sor)


class Cfm(Model):
    def __init__(self, sdf_version: str, cfm: float = 0):
        self.__version__ = sdf_version
        self.cfm = cfm

    def to_version(self, target_version: str) -> "Cfm":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Cfm":
        _text = el.text or 0
        _cfm = _parse_double(_text)
        if _cfm is not None and cmp_version(version, "1.2") < 0:
            if _cfm != 0:
                raise ValueError(f"'cfm' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, cfm=_cfm)


class Erp(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Erp":
        _text = el.text or 0.2
        _erp = _parse_double(_text)
        if _erp is not None and cmp_version(version, "1.2") < 0:
            if _erp != 0.2:
                raise ValueError(f"'erp' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, erp=_erp)


class ContactMaxCorrectingVel(Model):
    def __init__(self, sdf_version: str, contact_max_correcting_vel: float = 100.0):
        self.__version__ = sdf_version
        self.contact_max_correcting_vel = contact_max_correcting_vel

    def to_version(self, target_version: str) -> "ContactMaxCorrectingVel":
        if self.contact_max_correcting_vel is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'contact_max_correcting_vel' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["contact_max_correcting_vel"] = self.contact_max_correcting_vel
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact_max_correcting_vel")
        if self.contact_max_correcting_vel is not None:
            el.text = str(self.contact_max_correcting_vel)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ContactMaxCorrectingVel":
        _text = el.text or 100.0
        _contact_max_correcting_vel = _parse_double(_text)
        if _contact_max_correcting_vel is not None and cmp_version(version, "1.2") < 0:
            if _contact_max_correcting_vel != 100.0:
                raise ValueError(f"'contact_max_correcting_vel' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, contact_max_correcting_vel=_contact_max_correcting_vel)


class ContactSurfaceLayer(Model):
    def __init__(self, sdf_version: str, contact_surface_layer: float = 0.001):
        self.__version__ = sdf_version
        self.contact_surface_layer = contact_surface_layer

    def to_version(self, target_version: str) -> "ContactSurfaceLayer":
        if self.contact_surface_layer is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'contact_surface_layer' is not supported in SDF version {target_version} (added in 1.2)")
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
        if _contact_surface_layer is not None and cmp_version(version, "1.2") < 0:
            if _contact_surface_layer != 0.001:
                raise ValueError(f"'contact_surface_layer' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, contact_surface_layer=_contact_surface_layer)


class Constraints(Model):
    def __init__(
        self,
        sdf_version: str,
        cfm: float = 0,
        erp: float = 0.2,
        contact_max_correcting_vel: float = 100.0,
        contact_surface_layer: float = 0.001
    ):
        self.__version__ = sdf_version
        self.cfm = cfm
        self.erp = erp
        self.contact_max_correcting_vel = contact_max_correcting_vel
        self.contact_surface_layer = contact_surface_layer

    def to_version(self, target_version: str) -> "Constraints":
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm
        kwargs["erp"] = self.erp
        kwargs["contact_max_correcting_vel"] = self.contact_max_correcting_vel
        kwargs["contact_surface_layer"] = self.contact_surface_layer
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("constraints")
        if self.cfm is not None:
            el.set("cfm", str(self.cfm))
        if self.erp is not None:
            el.set("erp", str(self.erp))
        if self.contact_max_correcting_vel is not None:
            el.set("contact_max_correcting_vel", str(self.contact_max_correcting_vel))
        if self.contact_surface_layer is not None:
            el.set("contact_surface_layer", str(self.contact_surface_layer))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Constraints":
        _cfm = _parse_double(el.get("cfm", 0))
        _erp = _parse_double(el.get("erp", 0.2))
        _contact_max_correcting_vel = _parse_double(el.get("contact_max_correcting_vel", 100.0))
        _contact_surface_layer = _parse_double(el.get("contact_surface_layer", 0.001))
        return cls(sdf_version=version, cfm=_cfm, erp=_erp, contact_max_correcting_vel=_contact_max_correcting_vel, contact_surface_layer=_contact_surface_layer)


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


class Physics(Model):
    _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

    def __init__(
        self,
        sdf_version: str,
        type: str = "ode",
        update_rate: float = 0,
        max_contacts: "MaxContacts" = None,
        gravity: "Gravity" = None,
        bullet: "Bullet" = None,
        ode: "Ode" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.update_rate = update_rate
        self.max_contacts = max_contacts
        self.gravity = gravity
        self.bullet = bullet
        self.ode = ode

    def to_version(self, target_version: str) -> "Physics":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["update_rate"] = self.update_rate
        kwargs["max_contacts"] = self.max_contacts.to_version(target_version) if self.max_contacts is not None else None
        kwargs["gravity"] = self.gravity.to_version(target_version) if self.gravity is not None else None
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
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
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf(version))
        if self.gravity is not None:
            el.append(self.gravity.to_sdf(version))
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Physics":
        _type = el.get("type", "ode")
        _update_rate = _parse_double(el.get("update_rate", 0))
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts, version) if _c_max_contacts is not None else None
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity, version) if _c_gravity is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet, version) if _c_bullet is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        return cls(sdf_version=version, type=_type, update_rate=_update_rate, max_contacts=_max_contacts, gravity=_gravity, bullet=_bullet, ode=_ode)


class Ambient(Model):
    def __init__(self, sdf_version: str, ambient: Color = None, rgba: Color = None):
        self.__version__ = sdf_version
        if ambient is None:
            ambient = Color.from_sdf("0.0 0.0 0.0 1.0")
        if rgba is None:
            rgba = Color.from_sdf("0.0 0.0 0.0 1.0")
        self.ambient = ambient
        self.rgba = rgba

    def to_version(self, target_version: str) -> "Ambient":
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ambient":
        _text = el.text or "0.0 0.0 0.0 1.0"
        _ambient = Color.from_sdf(_text)
        _rgba = Color.from_sdf(el.get("rgba", "0.0 0.0 0.0 1.0"))
        return cls(sdf_version=version, ambient=_ambient, rgba=_rgba)


class Sky(Model):
    def __init__(self, sdf_version: str, material: str = "Gazebo/CloudySky"):
        self.__version__ = sdf_version
        self.material = material

    def to_version(self, target_version: str) -> "Sky":
        kwargs = {"sdf_version": target_version}
        kwargs["material"] = self.material
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sky")
        if self.material is not None:
            el.set("material", self.material)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sky":
        _material = el.get("material", "Gazebo/CloudySky")
        return cls(sdf_version=version, material=_material)


class Background(Model):
    def __init__(self, sdf_version: str, rgba: Color = None, sky: "Sky" = None):
        self.__version__ = sdf_version
        if rgba is None:
            rgba = Color.from_sdf(".7 .7 .7 1")
        self.rgba = rgba
        self.sky = sky

    def to_version(self, target_version: str) -> "Background":
        kwargs = {"sdf_version": target_version}
        kwargs["rgba"] = self.rgba
        kwargs["sky"] = self.sky.to_version(target_version) if self.sky is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("background")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        if self.sky is not None:
            el.append(self.sky.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Background":
        _rgba = Color.from_sdf(el.get("rgba", ".7 .7 .7 1"))
        _c_sky = el.find("sky")
        _sky = Sky.from_sdf(_c_sky, version) if _c_sky is not None else None
        return cls(sdf_version=version, rgba=_rgba, sky=_sky)


class Shadows(Model):
    def __init__(self, sdf_version: str, shadows: bool = True, enabled: bool = True):
        self.__version__ = sdf_version
        self.shadows = shadows
        self.enabled = enabled

    def to_version(self, target_version: str) -> "Shadows":
        kwargs = {"sdf_version": target_version}
        kwargs["shadows"] = self.shadows
        kwargs["enabled"] = self.enabled
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("shadows")
        if self.shadows is not None:
            el.text = str(self.shadows).lower()
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Shadows":
        _text = el.text or True
        _shadows = _text.strip().lower() == 'true'
        _enabled = el.get("enabled", True).strip().lower() == 'true'
        return cls(sdf_version=version, shadows=_shadows, enabled=_enabled)


class Color(Model):
    def __init__(self, sdf_version: str, color: Color = None):
        self.__version__ = sdf_version
        if color is None:
            color = Color.from_sdf("1 1 1 1")
        self.color = color

    def to_version(self, target_version: str) -> "Color":
        if self.color is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'color' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["color"] = self.color
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("color")
        if self.color is not None:
            el.text = self.color.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Color":
        _text = el.text or "1 1 1 1"
        _color = Color.from_sdf(_text)
        if _color is not None and cmp_version(version, "1.2") < 0:
            if _color != "1 1 1 1":
                raise ValueError(f"'color' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, color=_color)


class Start(Model):
    def __init__(self, sdf_version: str, start: float = 1.0):
        self.__version__ = sdf_version
        self.start = start

    def to_version(self, target_version: str) -> "Start":
        if self.start is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'start' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["start"] = self.start
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("start")
        if self.start is not None:
            el.text = str(self.start)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Start":
        _text = el.text or 1.0
        _start = _parse_double(_text)
        if _start is not None and cmp_version(version, "1.2") < 0:
            if _start != 1.0:
                raise ValueError(f"'start' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, start=_start)


class End(Model):
    def __init__(self, sdf_version: str, end: float = 100.0):
        self.__version__ = sdf_version
        self.end = end

    def to_version(self, target_version: str) -> "End":
        if self.end is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'end' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["end"] = self.end
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("end")
        if self.end is not None:
            el.text = str(self.end)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "End":
        _text = el.text or 100.0
        _end = _parse_double(_text)
        if _end is not None and cmp_version(version, "1.2") < 0:
            if _end != 100.0:
                raise ValueError(f"'end' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, end=_end)


class Density(Model):
    def __init__(self, sdf_version: str, density: float = 1.0):
        self.__version__ = sdf_version
        self.density = density

    def to_version(self, target_version: str) -> "Density":
        if self.density is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["density"] = self.density
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("density")
        if self.density is not None:
            el.text = str(self.density)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Density":
        _text = el.text or 1.0
        _density = _parse_double(_text)
        if _density is not None and cmp_version(version, "1.2") < 0:
            if _density != 1.0:
                raise ValueError(f"'density' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, density=_density)


class Fog(Model):
    def __init__(
        self,
        sdf_version: str,
        rgba: Color = None,
        type: str = "linear",
        start: float = 1.0,
        end: float = 100.0,
        density: float = 1.0,
        color: "Color" = None
    ):
        self.__version__ = sdf_version
        if rgba is None:
            rgba = Color.from_sdf("1 1 1 1")
        self.rgba = rgba
        self.type = type
        self.start = start
        self.end = end
        self.density = density
        self.color = color

    def to_version(self, target_version: str) -> "Fog":
        if self.color is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'color' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["rgba"] = self.rgba
        kwargs["type"] = self.type
        kwargs["start"] = self.start
        kwargs["end"] = self.end
        kwargs["density"] = self.density
        kwargs["color"] = self.color.to_version(target_version) if self.color is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fog")
        if self.rgba is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("color")
                _c_tmp.text = self.rgba.to_sdf()
                el.append(_c_tmp)
            else:
                el.set("rgba", self.rgba.to_sdf())
        if self.type is not None:
            el.set("type", self.type)
        if self.start is not None:
            el.set("start", str(self.start))
        if self.end is not None:
            el.set("end", str(self.end))
        if self.density is not None:
            el.set("density", str(self.density))
        if self.color is not None:
            el.append(self.color.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fog":
        _raw_rgba = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("color")
            if _c_tmp is not None: _raw_rgba = _c_tmp.text
        else:
            _raw_rgba = el.get("rgba")
        if _raw_rgba is None: _raw_rgba = "1 1 1 1"
        _rgba = Color.from_sdf(_raw_rgba)
        _type = el.get("type", "linear")
        _start = _parse_double(el.get("start", 1.0))
        _end = _parse_double(el.get("end", 100.0))
        _density = _parse_double(el.get("density", 1.0))
        _c_color = el.find("color")
        _color = Color.from_sdf(_c_color, version) if _c_color is not None else None
        if _color is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'color' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, rgba=_rgba, type=_type, start=_start, end=_end, density=_density, color=_color)


class Grid(Model):
    def __init__(self, sdf_version: str, grid: bool = True, enabled: bool = True):
        self.__version__ = sdf_version
        self.grid = grid
        self.enabled = enabled

    def to_version(self, target_version: str) -> "Grid":
        kwargs = {"sdf_version": target_version}
        kwargs["grid"] = self.grid
        kwargs["enabled"] = self.enabled
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grid")
        if self.grid is not None:
            el.text = str(self.grid).lower()
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Grid":
        _text = el.text or True
        _grid = _text.strip().lower() == 'true'
        _enabled = el.get("enabled", True).strip().lower() == 'true'
        return cls(sdf_version=version, grid=_grid, enabled=_enabled)


class Scene(Model):
    def __init__(
        self,
        sdf_version: str,
        ambient: "Ambient" = None,
        background: "Background" = None,
        shadows: "Shadows" = None,
        fog: "Fog" = None,
        grid: "Grid" = None,
        sky: "Sky" = None
    ):
        self.__version__ = sdf_version
        self.ambient = ambient
        self.background = background
        self.shadows = shadows
        self.fog = fog
        self.grid = grid
        self.sky = sky

    def to_version(self, target_version: str) -> "Scene":
        if self.sky is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'sky' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
        kwargs["background"] = self.background.to_version(target_version) if self.background is not None else None
        kwargs["shadows"] = self.shadows.to_version(target_version) if self.shadows is not None else None
        kwargs["fog"] = self.fog.to_version(target_version) if self.fog is not None else None
        kwargs["grid"] = self.grid.to_version(target_version) if self.grid is not None else None
        kwargs["sky"] = self.sky.to_version(target_version) if self.sky is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scene")
        if self.ambient is not None:
            el.append(self.ambient.to_sdf(version))
        if self.background is not None:
            el.append(self.background.to_sdf(version))
        if self.shadows is not None:
            el.append(self.shadows.to_sdf(version))
        if self.fog is not None:
            el.append(self.fog.to_sdf(version))
        if self.grid is not None:
            el.append(self.grid.to_sdf(version))
        if self.sky is not None:
            el.append(self.sky.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Scene":
        _c_ambient = el.find("ambient")
        _ambient = Ambient.from_sdf(_c_ambient, version) if _c_ambient is not None else None
        _c_background = el.find("background")
        _background = Background.from_sdf(_c_background, version) if _c_background is not None else None
        _c_shadows = el.find("shadows")
        _shadows = Shadows.from_sdf(_c_shadows, version) if _c_shadows is not None else None
        _c_fog = el.find("fog")
        _fog = Fog.from_sdf(_c_fog, version) if _c_fog is not None else None
        _c_grid = el.find("grid")
        _grid = Grid.from_sdf(_c_grid, version) if _c_grid is not None else None
        _c_sky = el.find("sky")
        _sky = Sky.from_sdf(_c_sky, version) if _c_sky is not None else None
        if _sky is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'sky' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, ambient=_ambient, background=_background, shadows=_shadows, fog=_fog, grid=_grid, sky=_sky)


class Diffuse(Model):
    def __init__(self, sdf_version: str, diffuse: Color = None, rgba: Color = None):
        self.__version__ = sdf_version
        if diffuse is None:
            diffuse = Color.from_sdf("1 1 1 1")
        if rgba is None:
            rgba = Color.from_sdf("1 1 1 1")
        self.diffuse = diffuse
        self.rgba = rgba

    def to_version(self, target_version: str) -> "Diffuse":
        kwargs = {"sdf_version": target_version}
        kwargs["diffuse"] = self.diffuse
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse.to_sdf()
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Diffuse":
        _text = el.text or "1 1 1 1"
        _diffuse = Color.from_sdf(_text)
        _rgba = Color.from_sdf(el.get("rgba", "1 1 1 1"))
        return cls(sdf_version=version, diffuse=_diffuse, rgba=_rgba)


class Specular(Model):
    def __init__(self, sdf_version: str, specular: Color = None, rgba: Color = None):
        self.__version__ = sdf_version
        if specular is None:
            specular = Color.from_sdf(".1 .1 .1 1")
        if rgba is None:
            rgba = Color.from_sdf(".1 .1 .1 1")
        self.specular = specular
        self.rgba = rgba

    def to_version(self, target_version: str) -> "Specular":
        kwargs = {"sdf_version": target_version}
        kwargs["specular"] = self.specular
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular")
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Specular":
        _text = el.text or ".1 .1 .1 1"
        _specular = Color.from_sdf(_text)
        _rgba = Color.from_sdf(el.get("rgba", ".1 .1 .1 1"))
        return cls(sdf_version=version, specular=_specular, rgba=_rgba)


class Range(Model):
    def __init__(self, sdf_version: str, range: float = 10):
        self.__version__ = sdf_version
        self.range = range

    def to_version(self, target_version: str) -> "Range":
        if self.range is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'range' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["range"] = self.range
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.range is not None:
            el.text = str(self.range)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Range":
        _text = el.text or 10
        _range = _parse_double(_text)
        if _range is not None and cmp_version(version, "1.2") < 0:
            if _range != 10:
                raise ValueError(f"'range' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, range=_range)


class Linear(Model):
    def __init__(self, sdf_version: str, linear: float = 1):
        self.__version__ = sdf_version
        self.linear = linear

    def to_version(self, target_version: str) -> "Linear":
        if self.linear is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'linear' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["linear"] = self.linear
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear")
        if self.linear is not None:
            el.text = str(self.linear)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Linear":
        _text = el.text or 1
        _linear = _parse_double(_text)
        if _linear is not None and cmp_version(version, "1.2") < 0:
            if _linear != 1:
                raise ValueError(f"'linear' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, linear=_linear)


class Constant(Model):
    def __init__(self, sdf_version: str, constant: float = 1):
        self.__version__ = sdf_version
        self.constant = constant

    def to_version(self, target_version: str) -> "Constant":
        if self.constant is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'constant' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["constant"] = self.constant
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("constant")
        if self.constant is not None:
            el.text = str(self.constant)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Constant":
        _text = el.text or 1
        _constant = _parse_double(_text)
        if _constant is not None and cmp_version(version, "1.2") < 0:
            if _constant != 1:
                raise ValueError(f"'constant' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, constant=_constant)


class Quadratic(Model):
    def __init__(self, sdf_version: str, quadratic: float = 0):
        self.__version__ = sdf_version
        self.quadratic = quadratic

    def to_version(self, target_version: str) -> "Quadratic":
        if self.quadratic is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'quadratic' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["quadratic"] = self.quadratic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("quadratic")
        if self.quadratic is not None:
            el.text = str(self.quadratic)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Quadratic":
        _text = el.text or 0
        _quadratic = _parse_double(_text)
        if _quadratic is not None and cmp_version(version, "1.2") < 0:
            if _quadratic != 0:
                raise ValueError(f"'quadratic' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, quadratic=_quadratic)


class Attenuation(Model):
    def __init__(
        self,
        sdf_version: str,
        range: float = 10,
        linear: float = 1,
        constant: float = 1,
        quadratic: float = 0
    ):
        self.__version__ = sdf_version
        self.range = range
        self.linear = linear
        self.constant = constant
        self.quadratic = quadratic

    def to_version(self, target_version: str) -> "Attenuation":
        kwargs = {"sdf_version": target_version}
        kwargs["range"] = self.range
        kwargs["linear"] = self.linear
        kwargs["constant"] = self.constant
        kwargs["quadratic"] = self.quadratic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("attenuation")
        if self.range is not None:
            el.set("range", str(self.range))
        if self.linear is not None:
            el.set("linear", str(self.linear))
        if self.constant is not None:
            el.set("constant", str(self.constant))
        if self.quadratic is not None:
            el.set("quadratic", str(self.quadratic))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Attenuation":
        _range = _parse_double(el.get("range", 10))
        _linear = _parse_double(el.get("linear", 1))
        _constant = _parse_double(el.get("constant", 1))
        _quadratic = _parse_double(el.get("quadratic", 0))
        return cls(sdf_version=version, range=_range, linear=_linear, constant=_constant, quadratic=_quadratic)


class Direction(Model):
    def __init__(self, sdf_version: str, direction: Vector3 = None, xyz: Vector3 = None):
        self.__version__ = sdf_version
        if direction is None:
            direction = Vector3.from_sdf("0 0 -1")
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 -1")
        self.direction = direction
        self.xyz = xyz

    def to_version(self, target_version: str) -> "Direction":
        kwargs = {"sdf_version": target_version}
        kwargs["direction"] = self.direction
        kwargs["xyz"] = self.xyz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("direction")
        if self.direction is not None:
            el.text = self.direction.to_sdf()
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Direction":
        _text = el.text or "0 0 -1"
        _direction = Vector3.from_sdf(_text)
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 -1"))
        return cls(sdf_version=version, direction=_direction, xyz=_xyz)


class InnerAngle(Model):
    def __init__(self, sdf_version: str, inner_angle: float = 0):
        self.__version__ = sdf_version
        self.inner_angle = inner_angle

    def to_version(self, target_version: str) -> "InnerAngle":
        if self.inner_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'inner_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["inner_angle"] = self.inner_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inner_angle")
        if self.inner_angle is not None:
            el.text = str(self.inner_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "InnerAngle":
        _text = el.text or 0
        _inner_angle = _parse_double(_text)
        if _inner_angle is not None and cmp_version(version, "1.2") < 0:
            if _inner_angle != 0:
                raise ValueError(f"'inner_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, inner_angle=_inner_angle)


class OuterAngle(Model):
    def __init__(self, sdf_version: str, outer_angle: float = 0):
        self.__version__ = sdf_version
        self.outer_angle = outer_angle

    def to_version(self, target_version: str) -> "OuterAngle":
        if self.outer_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'outer_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["outer_angle"] = self.outer_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("outer_angle")
        if self.outer_angle is not None:
            el.text = str(self.outer_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "OuterAngle":
        _text = el.text or 0
        _outer_angle = _parse_double(_text)
        if _outer_angle is not None and cmp_version(version, "1.2") < 0:
            if _outer_angle != 0:
                raise ValueError(f"'outer_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, outer_angle=_outer_angle)


class Falloff(Model):
    def __init__(self, sdf_version: str, falloff: float = 0):
        self.__version__ = sdf_version
        self.falloff = falloff

    def to_version(self, target_version: str) -> "Falloff":
        if self.falloff is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'falloff' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["falloff"] = self.falloff
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("falloff")
        if self.falloff is not None:
            el.text = str(self.falloff)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Falloff":
        _text = el.text or 0
        _falloff = _parse_double(_text)
        if _falloff is not None and cmp_version(version, "1.2") < 0:
            if _falloff != 0:
                raise ValueError(f"'falloff' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, falloff=_falloff)


class Spot(Model):
    def __init__(
        self,
        sdf_version: str,
        inner_angle: float = 0,
        outer_angle: float = 0,
        falloff: float = 0
    ):
        self.__version__ = sdf_version
        self.inner_angle = inner_angle
        self.outer_angle = outer_angle
        self.falloff = falloff

    def to_version(self, target_version: str) -> "Spot":
        kwargs = {"sdf_version": target_version}
        kwargs["inner_angle"] = self.inner_angle
        kwargs["outer_angle"] = self.outer_angle
        kwargs["falloff"] = self.falloff
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spot")
        if self.inner_angle is not None:
            el.set("inner_angle", str(self.inner_angle))
        if self.outer_angle is not None:
            el.set("outer_angle", str(self.outer_angle))
        if self.falloff is not None:
            el.set("falloff", str(self.falloff))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Spot":
        _inner_angle = _parse_double(el.get("inner_angle", 0))
        _outer_angle = _parse_double(el.get("outer_angle", 0))
        _falloff = _parse_double(el.get("falloff", 0))
        return cls(sdf_version=version, inner_angle=_inner_angle, outer_angle=_outer_angle, falloff=_falloff)


class CastShadows(Model):
    def __init__(self, sdf_version: str, cast_shadows: bool = False):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows

    def to_version(self, target_version: str) -> "CastShadows":
        if self.cast_shadows is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'cast_shadows' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["cast_shadows"] = self.cast_shadows
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cast_shadows")
        if self.cast_shadows is not None:
            el.text = str(self.cast_shadows).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CastShadows":
        _text = el.text or False
        _cast_shadows = _text.strip().lower() == 'true'
        if _cast_shadows is not None and cmp_version(version, "1.2") < 0:
            if _cast_shadows != False:
                raise ValueError(f"'cast_shadows' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, cast_shadows=_cast_shadows)


class Light(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "point",
        cast_shadows: bool = False,
        origin: "Origin" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        attenuation: "Attenuation" = None,
        direction: "Direction" = None,
        spot: "Spot" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.cast_shadows = cast_shadows
        self.origin = origin
        self.diffuse = diffuse
        self.specular = specular
        self.attenuation = attenuation
        self.direction = direction
        self.spot = spot
        self.pose = pose

    def to_version(self, target_version: str) -> "Light":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["cast_shadows"] = self.cast_shadows
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["attenuation"] = self.attenuation.to_version(target_version) if self.attenuation is not None else None
        kwargs["direction"] = self.direction.to_version(target_version) if self.direction is not None else None
        kwargs["spot"] = self.spot.to_version(target_version) if self.spot is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.cast_shadows is not None:
            el.set("cast_shadows", str(self.cast_shadows).lower())
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.specular is not None:
            el.append(self.specular.to_sdf(version))
        if self.attenuation is not None:
            el.append(self.attenuation.to_sdf(version))
        if self.direction is not None:
            el.append(self.direction.to_sdf(version))
        if self.spot is not None:
            el.append(self.spot.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Light":
        _name = el.get("name", "__default__")
        _type = el.get("type", "point")
        _cast_shadows = el.get("cast_shadows", False).strip().lower() == 'true'
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse, version) if _c_diffuse is not None else None
        _c_specular = el.find("specular")
        _specular = Specular.from_sdf(_c_specular, version) if _c_specular is not None else None
        _c_attenuation = el.find("attenuation")
        _attenuation = Attenuation.from_sdf(_c_attenuation, version) if _c_attenuation is not None else None
        _c_direction = el.find("direction")
        _direction = Direction.from_sdf(_c_direction, version) if _c_direction is not None else None
        _c_spot = el.find("spot")
        _spot = Spot.from_sdf(_c_spot, version) if _c_spot is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, type=_type, cast_shadows=_cast_shadows, origin=_origin, diffuse=_diffuse, specular=_specular, attenuation=_attenuation, direction=_direction, spot=_spot, pose=_pose)


class Ixx(Model):
    def __init__(self, sdf_version: str, ixx: float = 1.0):
        self.__version__ = sdf_version
        self.ixx = ixx

    def to_version(self, target_version: str) -> "Ixx":
        if self.ixx is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'ixx' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ixx"] = self.ixx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ixx")
        if self.ixx is not None:
            el.text = str(self.ixx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ixx":
        _text = el.text or 1.0
        _ixx = _parse_double(_text)
        if _ixx is not None and cmp_version(version, "1.2") < 0:
            if _ixx != 1.0:
                raise ValueError(f"'ixx' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, ixx=_ixx)


class Ixy(Model):
    def __init__(self, sdf_version: str, ixy: float = 0.0):
        self.__version__ = sdf_version
        self.ixy = ixy

    def to_version(self, target_version: str) -> "Ixy":
        if self.ixy is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'ixy' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ixy"] = self.ixy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ixy")
        if self.ixy is not None:
            el.text = str(self.ixy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ixy":
        _text = el.text or 0.0
        _ixy = _parse_double(_text)
        if _ixy is not None and cmp_version(version, "1.2") < 0:
            if _ixy != 0.0:
                raise ValueError(f"'ixy' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, ixy=_ixy)


class Ixz(Model):
    def __init__(self, sdf_version: str, ixz: float = 0.0):
        self.__version__ = sdf_version
        self.ixz = ixz

    def to_version(self, target_version: str) -> "Ixz":
        if self.ixz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'ixz' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ixz"] = self.ixz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ixz")
        if self.ixz is not None:
            el.text = str(self.ixz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ixz":
        _text = el.text or 0.0
        _ixz = _parse_double(_text)
        if _ixz is not None and cmp_version(version, "1.2") < 0:
            if _ixz != 0.0:
                raise ValueError(f"'ixz' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, ixz=_ixz)


class Iyy(Model):
    def __init__(self, sdf_version: str, iyy: float = 1.0):
        self.__version__ = sdf_version
        self.iyy = iyy

    def to_version(self, target_version: str) -> "Iyy":
        if self.iyy is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'iyy' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["iyy"] = self.iyy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("iyy")
        if self.iyy is not None:
            el.text = str(self.iyy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Iyy":
        _text = el.text or 1.0
        _iyy = _parse_double(_text)
        if _iyy is not None and cmp_version(version, "1.2") < 0:
            if _iyy != 1.0:
                raise ValueError(f"'iyy' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, iyy=_iyy)


class Iyz(Model):
    def __init__(self, sdf_version: str, iyz: float = 0.0):
        self.__version__ = sdf_version
        self.iyz = iyz

    def to_version(self, target_version: str) -> "Iyz":
        if self.iyz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'iyz' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["iyz"] = self.iyz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("iyz")
        if self.iyz is not None:
            el.text = str(self.iyz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Iyz":
        _text = el.text or 0.0
        _iyz = _parse_double(_text)
        if _iyz is not None and cmp_version(version, "1.2") < 0:
            if _iyz != 0.0:
                raise ValueError(f"'iyz' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, iyz=_iyz)


class Izz(Model):
    def __init__(self, sdf_version: str, izz: float = 1.0):
        self.__version__ = sdf_version
        self.izz = izz

    def to_version(self, target_version: str) -> "Izz":
        if self.izz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'izz' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["izz"] = self.izz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("izz")
        if self.izz is not None:
            el.text = str(self.izz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Izz":
        _text = el.text or 1.0
        _izz = _parse_double(_text)
        if _izz is not None and cmp_version(version, "1.2") < 0:
            if _izz != 1.0:
                raise ValueError(f"'izz' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, izz=_izz)


class Inertia(Model):
    def __init__(
        self,
        sdf_version: str,
        ixx: float = 0.0,
        ixy: float = 0.0,
        ixz: float = 0.0,
        iyy: float = 0.0,
        iyz: float = 0.0,
        izz: float = 0.0
    ):
        self.__version__ = sdf_version
        self.ixx = ixx
        self.ixy = ixy
        self.ixz = ixz
        self.iyy = iyy
        self.iyz = iyz
        self.izz = izz

    def to_version(self, target_version: str) -> "Inertia":
        kwargs = {"sdf_version": target_version}
        kwargs["ixx"] = self.ixx
        kwargs["ixy"] = self.ixy
        kwargs["ixz"] = self.ixz
        kwargs["iyy"] = self.iyy
        kwargs["iyz"] = self.iyz
        kwargs["izz"] = self.izz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inertia")
        if self.ixx is not None:
            el.set("ixx", str(self.ixx))
        if self.ixy is not None:
            el.set("ixy", str(self.ixy))
        if self.ixz is not None:
            el.set("ixz", str(self.ixz))
        if self.iyy is not None:
            el.set("iyy", str(self.iyy))
        if self.iyz is not None:
            el.set("iyz", str(self.iyz))
        if self.izz is not None:
            el.set("izz", str(self.izz))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Inertia":
        _ixx = _parse_double(el.get("ixx", 0.0))
        _ixy = _parse_double(el.get("ixy", 0.0))
        _ixz = _parse_double(el.get("ixz", 0.0))
        _iyy = _parse_double(el.get("iyy", 0.0))
        _iyz = _parse_double(el.get("iyz", 0.0))
        _izz = _parse_double(el.get("izz", 0.0))
        return cls(sdf_version=version, ixx=_ixx, ixy=_ixy, ixz=_ixz, iyy=_iyy, iyz=_iyz, izz=_izz)


class Mass(Model):
    def __init__(self, sdf_version: str, mass: float = 1.0):
        self.__version__ = sdf_version
        self.mass = mass

    def to_version(self, target_version: str) -> "Mass":
        if self.mass is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'mass' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mass"] = self.mass
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mass")
        if self.mass is not None:
            el.text = str(self.mass)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mass":
        _text = el.text or 1.0
        _mass = _parse_double(_text)
        if _mass is not None and cmp_version(version, "1.2") < 0:
            if _mass != 1.0:
                raise ValueError(f"'mass' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mass=_mass)


class Inertial(Model):
    def __init__(
        self,
        sdf_version: str,
        mass: float = 1.0,
        density: float = 1.0,
        origin: "Origin" = None,
        inertia: "Inertia" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.mass = mass
        self.density = density
        self.origin = origin
        self.inertia = inertia
        self.pose = pose

    def to_version(self, target_version: str) -> "Inertial":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mass"] = self.mass
        kwargs["density"] = self.density
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["inertia"] = self.inertia.to_version(target_version) if self.inertia is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inertial")
        if self.mass is not None:
            el.set("mass", str(self.mass))
        if self.density is not None:
            el.set("density", str(self.density))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.inertia is not None:
            el.append(self.inertia.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Inertial":
        _mass = _parse_double(el.get("mass", 1.0))
        _density = _parse_double(el.get("density", 1.0))
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_inertia = el.find("inertia")
        _inertia = Inertia.from_sdf(_c_inertia, version) if _c_inertia is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mass=_mass, density=_density, origin=_origin, inertia=_inertia, pose=_pose)


class Size(Model):
    def __init__(self, sdf_version: str, size: Vector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        self.size = size

    def to_version(self, target_version: str) -> "Size":
        if self.size is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'size' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("size")
        if self.size is not None:
            el.text = self.size.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Size":
        _text = el.text or "1 1 1"
        _size = Vector3.from_sdf(_text)
        if _size is not None and cmp_version(version, "1.2") < 0:
            if _size != "1 1 1":
                raise ValueError(f"'size' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, size=_size)


class Box(Model):
    def __init__(self, sdf_version: str, size: Vector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        self.size = size

    def to_version(self, target_version: str) -> "Box":
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("box")
        if self.size is not None:
            el.set("size", self.size.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Box":
        _size = Vector3.from_sdf(el.get("size", "1 1 1"))
        return cls(sdf_version=version, size=_size)


class Radius(Model):
    def __init__(self, sdf_version: str, radius: float = 1):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Radius":
        if self.radius is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'radius' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("radius")
        if self.radius is not None:
            el.text = str(self.radius)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Radius":
        _text = el.text or 1
        _radius = _parse_double(_text)
        if _radius is not None and cmp_version(version, "1.2") < 0:
            if _radius != 1:
                raise ValueError(f"'radius' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, radius=_radius)


class Sphere(Model):
    def __init__(self, sdf_version: str, radius: float = 1):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Sphere":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sphere")
        if self.radius is not None:
            el.set("radius", str(self.radius))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sphere":
        _radius = _parse_double(el.get("radius", 1))
        return cls(sdf_version=version, radius=_radius)


class Length(Model):
    def __init__(self, sdf_version: str, length: float = 1):
        self.__version__ = sdf_version
        self.length = length

    def to_version(self, target_version: str) -> "Length":
        if self.length is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'length' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["length"] = self.length
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("length")
        if self.length is not None:
            el.text = str(self.length)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Length":
        _text = el.text or 1
        _length = _parse_double(_text)
        if _length is not None and cmp_version(version, "1.2") < 0:
            if _length != 1:
                raise ValueError(f"'length' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, length=_length)


class Cylinder(Model):
    def __init__(self, sdf_version: str, radius: float = 1, length: float = 1):
        self.__version__ = sdf_version
        self.radius = radius
        self.length = length

    def to_version(self, target_version: str) -> "Cylinder":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        kwargs["length"] = self.length
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cylinder")
        if self.radius is not None:
            el.set("radius", str(self.radius))
        if self.length is not None:
            el.set("length", str(self.length))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cylinder":
        _radius = _parse_double(el.get("radius", 1))
        _length = _parse_double(el.get("length", 1))
        return cls(sdf_version=version, radius=_radius, length=_length)


class Filename(Model):
    def __init__(self, sdf_version: str, filename: str = "__default__"):
        self.__version__ = sdf_version
        self.filename = filename

    def to_version(self, target_version: str) -> "Filename":
        if self.filename is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("filename")
        if self.filename is not None:
            el.text = self.filename
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Filename":
        _text = el.text or "__default__"
        _filename = _text
        if _filename is not None and cmp_version(version, "1.2") < 0:
            if _filename != "__default__":
                raise ValueError(f"'filename' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, filename=_filename)


class Uri(Model):
    def __init__(self, sdf_version: str, uri: str = "__default__"):
        self.__version__ = sdf_version
        self.uri = uri

    def to_version(self, target_version: str) -> "Uri":
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("uri")
        if self.uri is not None:
            el.text = self.uri
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Uri":
        _text = el.text or "__default__"
        _uri = _text
        if _uri is not None and cmp_version(version, "1.2") < 0:
            if _uri != "__default__":
                raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, uri=_uri)


class Scale(Model):
    def __init__(self, sdf_version: str, scale: Vector3 = None):
        self.__version__ = sdf_version
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        self.scale = scale

    def to_version(self, target_version: str) -> "Scale":
        if self.scale is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["scale"] = self.scale
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = self.scale.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Scale":
        _text = el.text or "1 1 1"
        _scale = Vector3.from_sdf(_text)
        if _scale is not None and cmp_version(version, "1.2") < 0:
            if _scale != "1 1 1":
                raise ValueError(f"'scale' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, scale=_scale)


class Mesh(Model):
    def __init__(
        self,
        sdf_version: str,
        filename: str = "__default__",
        scale: Vector3 = None,
        uri: "Uri" = None
    ):
        self.__version__ = sdf_version
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        self.filename = filename
        self.scale = scale
        self.uri = uri

    def to_version(self, target_version: str) -> "Mesh":
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["scale"] = self.scale
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mesh")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.scale is not None:
            el.set("scale", self.scale.to_sdf())
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mesh":
        _filename = el.get("filename", "__default__")
        _scale = Vector3.from_sdf(el.get("scale", "1 1 1"))
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, filename=_filename, scale=_scale, uri=_uri)


class Normal(Model):
    def __init__(self, sdf_version: str, normal: Vector3 = None):
        self.__version__ = sdf_version
        if normal is None:
            normal = Vector3.from_sdf("0 0 1")
        self.normal = normal

    def to_version(self, target_version: str) -> "Normal":
        if self.normal is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'normal' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["normal"] = self.normal
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal")
        if self.normal is not None:
            el.text = self.normal.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Normal":
        _text = el.text or "0 0 1"
        _normal = Vector3.from_sdf(_text)
        if _normal is not None and cmp_version(version, "1.2") < 0:
            if _normal != "0 0 1":
                raise ValueError(f"'normal' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, normal=_normal)


class Plane(Model):
    def __init__(self, sdf_version: str, normal: Vector3 = None, size: "Size" = None):
        self.__version__ = sdf_version
        if normal is None:
            normal = Vector3.from_sdf("0 0 1")
        self.normal = normal
        self.size = size

    def to_version(self, target_version: str) -> "Plane":
        if self.size is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'size' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["normal"] = self.normal
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plane")
        if self.normal is not None:
            el.set("normal", self.normal.to_sdf())
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Plane":
        _normal = Vector3.from_sdf(el.get("normal", "0 0 1"))
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size, version) if _c_size is not None else None
        if _size is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'size' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, normal=_normal, size=_size)


class Threshold(Model):
    def __init__(self, sdf_version: str, threshold: int = 200):
        self.__version__ = sdf_version
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Threshold":
        if self.threshold is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'threshold' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["threshold"] = self.threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("threshold")
        if self.threshold is not None:
            el.text = str(self.threshold)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Threshold":
        _text = el.text or 200
        _threshold = _parse_int32(_text)
        if _threshold is not None and cmp_version(version, "1.2") < 0:
            if _threshold != 200:
                raise ValueError(f"'threshold' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, threshold=_threshold)


class Height(Model):
    def __init__(self, sdf_version: str, height: float = 1):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
        if self.height is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'height' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("height")
        if self.height is not None:
            el.text = str(self.height)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Height":
        _text = el.text or 1
        _height = _parse_double(_text)
        if _height is not None and cmp_version(version, "1.2") < 0:
            if _height != 1:
                raise ValueError(f"'height' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, height=_height)


class Granularity(Model):
    def __init__(self, sdf_version: str, granularity: int = 1):
        self.__version__ = sdf_version
        self.granularity = granularity

    def to_version(self, target_version: str) -> "Granularity":
        if self.granularity is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'granularity' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["granularity"] = self.granularity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("granularity")
        if self.granularity is not None:
            el.text = str(self.granularity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Granularity":
        _text = el.text or 1
        _granularity = _parse_int32(_text)
        if _granularity is not None and cmp_version(version, "1.2") < 0:
            if _granularity != 1:
                raise ValueError(f"'granularity' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, granularity=_granularity)


class Image(Model):
    def __init__(
        self,
        sdf_version: str,
        filename: str = "__default__",
        scale: float = 1,
        threshold: int = 200,
        height: float = 1,
        granularity: int = 1,
        uri: "Uri" = None
    ):
        self.__version__ = sdf_version
        self.filename = filename
        self.scale = scale
        self.threshold = threshold
        self.height = height
        self.granularity = granularity
        self.uri = uri

    def to_version(self, target_version: str) -> "Image":
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["scale"] = self.scale
        kwargs["threshold"] = self.threshold
        kwargs["height"] = self.height
        kwargs["granularity"] = self.granularity
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("image")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.scale is not None:
            el.set("scale", str(self.scale))
        if self.threshold is not None:
            el.set("threshold", str(self.threshold))
        if self.height is not None:
            el.set("height", str(self.height))
        if self.granularity is not None:
            el.set("granularity", str(self.granularity))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Image":
        _filename = el.get("filename", "__default__")
        _scale = _parse_double(el.get("scale", 1))
        _threshold = _parse_int32(el.get("threshold", 200))
        _height = _parse_double(el.get("height", 1))
        _granularity = _parse_int32(el.get("granularity", 1))
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, filename=_filename, scale=_scale, threshold=_threshold, height=_height, granularity=_granularity, uri=_uri)


class Texture(Model):
    def __init__(
        self,
        sdf_version: str,
        size: "Size" = None,
        diffuse: "Diffuse" = None,
        normal: "Normal" = None
    ):
        self.__version__ = sdf_version
        self.size = size
        self.diffuse = diffuse
        self.normal = normal

    def to_version(self, target_version: str) -> "Texture":
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["normal"] = self.normal.to_version(target_version) if self.normal is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("texture")
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.normal is not None:
            el.append(self.normal.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Texture":
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size, version) if _c_size is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse, version) if _c_diffuse is not None else None
        _c_normal = el.find("normal")
        _normal = Normal.from_sdf(_c_normal, version) if _c_normal is not None else None
        return cls(sdf_version=version, size=_size, diffuse=_diffuse, normal=_normal)


class MinHeight(Model):
    def __init__(self, sdf_version: str, min_height: float = 0):
        self.__version__ = sdf_version
        self.min_height = min_height

    def to_version(self, target_version: str) -> "MinHeight":
        kwargs = {"sdf_version": target_version}
        kwargs["min_height"] = self.min_height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_height")
        if self.min_height is not None:
            el.text = str(self.min_height)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinHeight":
        _text = el.text or 0
        _min_height = _parse_double(_text)
        return cls(sdf_version=version, min_height=_min_height)


class FadeDist(Model):
    def __init__(self, sdf_version: str, fade_dist: float = 0):
        self.__version__ = sdf_version
        self.fade_dist = fade_dist

    def to_version(self, target_version: str) -> "FadeDist":
        kwargs = {"sdf_version": target_version}
        kwargs["fade_dist"] = self.fade_dist
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fade_dist")
        if self.fade_dist is not None:
            el.text = str(self.fade_dist)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "FadeDist":
        _text = el.text or 0
        _fade_dist = _parse_double(_text)
        return cls(sdf_version=version, fade_dist=_fade_dist)


class Blend(Model):
    def __init__(
        self,
        sdf_version: str,
        min_height: "MinHeight" = None,
        fade_dist: "FadeDist" = None
    ):
        self.__version__ = sdf_version
        self.min_height = min_height
        self.fade_dist = fade_dist

    def to_version(self, target_version: str) -> "Blend":
        kwargs = {"sdf_version": target_version}
        kwargs["min_height"] = self.min_height.to_version(target_version) if self.min_height is not None else None
        kwargs["fade_dist"] = self.fade_dist.to_version(target_version) if self.fade_dist is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("blend")
        if self.min_height is not None:
            el.append(self.min_height.to_sdf(version))
        if self.fade_dist is not None:
            el.append(self.fade_dist.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Blend":
        _c_min_height = el.find("min_height")
        _min_height = MinHeight.from_sdf(_c_min_height, version) if _c_min_height is not None else None
        _c_fade_dist = el.find("fade_dist")
        _fade_dist = FadeDist.from_sdf(_c_fade_dist, version) if _c_fade_dist is not None else None
        return cls(sdf_version=version, min_height=_min_height, fade_dist=_fade_dist)


class Pos(Model):
    def __init__(self, sdf_version: str, pos: Vector3 = None):
        self.__version__ = sdf_version
        if pos is None:
            pos = Vector3.from_sdf("0 0 0")
        self.pos = pos

    def to_version(self, target_version: str) -> "Pos":
        if self.pos is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pos' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["pos"] = self.pos
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pos")
        if self.pos is not None:
            el.text = self.pos.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pos":
        _text = el.text or "0 0 0"
        _pos = Vector3.from_sdf(_text)
        if _pos is not None and cmp_version(version, "1.2") < 0:
            if _pos != "0 0 0":
                raise ValueError(f"'pos' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, pos=_pos)


class Heightmap(Model):
    def __init__(
        self,
        sdf_version: str,
        filename: str = "__default__",
        size: Vector3 = None,
        origin: Vector3 = None,
        texture: List["Texture"] = None,
        blend: List["Blend"] = None,
        uri: "Uri" = None,
        pos: "Pos" = None
    ):
        self.__version__ = sdf_version
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        if origin is None:
            origin = Vector3.from_sdf("0 0 0")
        self.filename = filename
        self.size = size
        self.origin = origin
        self.texture = texture or []
        self.blend = blend or []
        self.uri = uri
        self.pos = pos

    def to_version(self, target_version: str) -> "Heightmap":
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        if self.pos is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pos' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["size"] = self.size
        kwargs["origin"] = self.origin
        kwargs["texture"] = [c.to_version(target_version) for c in (self.texture or [])]
        kwargs["blend"] = [c.to_version(target_version) for c in (self.blend or [])]
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["pos"] = self.pos.to_version(target_version) if self.pos is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("heightmap")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.size is not None:
            el.set("size", self.size.to_sdf())
        if self.origin is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("pos")
                _c_tmp.text = self.origin.to_sdf()
                el.append(_c_tmp)
            else:
                el.set("origin", self.origin.to_sdf())
        for item in (self.texture or []):
            el.append(item.to_sdf(version))
        for item in (self.blend or []):
            el.append(item.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.pos is not None:
            el.append(self.pos.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Heightmap":
        _filename = el.get("filename", "__default__")
        _size = Vector3.from_sdf(el.get("size", "1 1 1"))
        _raw_origin = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("pos")
            if _c_tmp is not None: _raw_origin = _c_tmp.text
        else:
            _raw_origin = el.get("origin")
        if _raw_origin is None: _raw_origin = "0 0 0"
        _origin = Vector3.from_sdf(_raw_origin)
        _texture = [Texture.from_sdf(c, version) for c in el.findall("texture")]
        _blend = [Blend.from_sdf(c, version) for c in el.findall("blend")]
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        _c_pos = el.find("pos")
        _pos = Pos.from_sdf(_c_pos, version) if _c_pos is not None else None
        if _pos is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pos' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, filename=_filename, size=_size, origin=_origin, texture=_texture, blend=_blend, uri=_uri, pos=_pos)


class Geometry(Model):
    def __init__(
        self,
        sdf_version: str,
        box: "Box" = None,
        sphere: "Sphere" = None,
        cylinder: "Cylinder" = None,
        mesh: "Mesh" = None,
        plane: "Plane" = None,
        image: "Image" = None,
        heightmap: "Heightmap" = None
    ):
        self.__version__ = sdf_version
        self.box = box
        self.sphere = sphere
        self.cylinder = cylinder
        self.mesh = mesh
        self.plane = plane
        self.image = image
        self.heightmap = heightmap

    def to_version(self, target_version: str) -> "Geometry":
        kwargs = {"sdf_version": target_version}
        kwargs["box"] = self.box.to_version(target_version) if self.box is not None else None
        kwargs["sphere"] = self.sphere.to_version(target_version) if self.sphere is not None else None
        kwargs["cylinder"] = self.cylinder.to_version(target_version) if self.cylinder is not None else None
        kwargs["mesh"] = self.mesh.to_version(target_version) if self.mesh is not None else None
        kwargs["plane"] = self.plane.to_version(target_version) if self.plane is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["heightmap"] = self.heightmap.to_version(target_version) if self.heightmap is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("geometry")
        if self.box is not None:
            el.append(self.box.to_sdf(version))
        if self.sphere is not None:
            el.append(self.sphere.to_sdf(version))
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf(version))
        if self.mesh is not None:
            el.append(self.mesh.to_sdf(version))
        if self.plane is not None:
            el.append(self.plane.to_sdf(version))
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.heightmap is not None:
            el.append(self.heightmap.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Geometry":
        _c_box = el.find("box")
        _box = Box.from_sdf(_c_box, version) if _c_box is not None else None
        _c_sphere = el.find("sphere")
        _sphere = Sphere.from_sdf(_c_sphere, version) if _c_sphere is not None else None
        _c_cylinder = el.find("cylinder")
        _cylinder = Cylinder.from_sdf(_c_cylinder, version) if _c_cylinder is not None else None
        _c_mesh = el.find("mesh")
        _mesh = Mesh.from_sdf(_c_mesh, version) if _c_mesh is not None else None
        _c_plane = el.find("plane")
        _plane = Plane.from_sdf(_c_plane, version) if _c_plane is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image, version) if _c_image is not None else None
        _c_heightmap = el.find("heightmap")
        _heightmap = Heightmap.from_sdf(_c_heightmap, version) if _c_heightmap is not None else None
        return cls(sdf_version=version, box=_box, sphere=_sphere, cylinder=_cylinder, mesh=_mesh, plane=_plane, image=_image, heightmap=_heightmap)


class RestitutionCoefficient(Model):
    def __init__(self, sdf_version: str, restitution_coefficient: float = 0):
        self.__version__ = sdf_version
        self.restitution_coefficient = restitution_coefficient

    def to_version(self, target_version: str) -> "RestitutionCoefficient":
        if self.restitution_coefficient is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'restitution_coefficient' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["restitution_coefficient"] = self.restitution_coefficient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("restitution_coefficient")
        if self.restitution_coefficient is not None:
            el.text = str(self.restitution_coefficient)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "RestitutionCoefficient":
        _text = el.text or 0
        _restitution_coefficient = _parse_double(_text)
        if _restitution_coefficient is not None and cmp_version(version, "1.2") < 0:
            if _restitution_coefficient != 0:
                raise ValueError(f"'restitution_coefficient' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient)


class Bounce(Model):
    def __init__(
        self,
        sdf_version: str,
        restitution_coefficient: float = 0,
        threshold: float = 100000
    ):
        self.__version__ = sdf_version
        self.restitution_coefficient = restitution_coefficient
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Bounce":
        kwargs = {"sdf_version": target_version}
        kwargs["restitution_coefficient"] = self.restitution_coefficient
        kwargs["threshold"] = self.threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bounce")
        if self.restitution_coefficient is not None:
            el.set("restitution_coefficient", str(self.restitution_coefficient))
        if self.threshold is not None:
            el.set("threshold", str(self.threshold))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Bounce":
        _restitution_coefficient = _parse_double(el.get("restitution_coefficient", 0))
        _threshold = _parse_double(el.get("threshold", 100000))
        return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient, threshold=_threshold)


class Friction(Model):
    def __init__(self, sdf_version: str, ode: "Ode" = None):
        self.__version__ = sdf_version
        self.ode = ode

    def to_version(self, target_version: str) -> "Friction":
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Friction":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        return cls(sdf_version=version, ode=_ode)


class Contact(Model):
    def __init__(self, sdf_version: str, ode: "Ode" = None):
        self.__version__ = sdf_version
        self.ode = ode

    def to_version(self, target_version: str) -> "Contact":
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Contact":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        return cls(sdf_version=version, ode=_ode)


class Surface(Model):
    def __init__(
        self,
        sdf_version: str,
        bounce: "Bounce" = None,
        friction: "Friction" = None,
        contact: "Contact" = None
    ):
        self.__version__ = sdf_version
        self.bounce = bounce
        self.friction = friction
        self.contact = contact

    def to_version(self, target_version: str) -> "Surface":
        kwargs = {"sdf_version": target_version}
        kwargs["bounce"] = self.bounce.to_version(target_version) if self.bounce is not None else None
        kwargs["friction"] = self.friction.to_version(target_version) if self.friction is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface")
        if self.bounce is not None:
            el.append(self.bounce.to_sdf(version))
        if self.friction is not None:
            el.append(self.friction.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Surface":
        _c_bounce = el.find("bounce")
        _bounce = Bounce.from_sdf(_c_bounce, version) if _c_bounce is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction, version) if _c_friction is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact, version) if _c_contact is not None else None
        return cls(sdf_version=version, bounce=_bounce, friction=_friction, contact=_contact)


class LaserRetro(Model):
    def __init__(self, sdf_version: str, laser_retro: float = 0):
        self.__version__ = sdf_version
        self.laser_retro = laser_retro

    def to_version(self, target_version: str) -> "LaserRetro":
        if self.laser_retro is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'laser_retro' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["laser_retro"] = self.laser_retro
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("laser_retro")
        if self.laser_retro is not None:
            el.text = str(self.laser_retro)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LaserRetro":
        _text = el.text or 0
        _laser_retro = _parse_double(_text)
        if _laser_retro is not None and cmp_version(version, "1.2") < 0:
            if _laser_retro != 0:
                raise ValueError(f"'laser_retro' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, laser_retro=_laser_retro)


class Collision(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        laser_retro: float = 0,
        geometry: "Geometry" = None,
        surface: "Surface" = None,
        max_contacts: "MaxContacts" = None,
        mass: "Mass" = None,
        origin: "Origin" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.laser_retro = laser_retro
        self.geometry = geometry
        self.surface = surface
        self.max_contacts = max_contacts
        self.mass = mass
        self.origin = origin
        self.pose = pose

    def to_version(self, target_version: str) -> "Collision":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["laser_retro"] = self.laser_retro
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["surface"] = self.surface.to_version(target_version) if self.surface is not None else None
        kwargs["max_contacts"] = self.max_contacts.to_version(target_version) if self.max_contacts is not None else None
        kwargs["mass"] = self.mass.to_version(target_version) if self.mass is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision")
        if self.name is not None:
            el.set("name", self.name)
        if self.laser_retro is not None:
            el.set("laser_retro", str(self.laser_retro))
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.surface is not None:
            el.append(self.surface.to_sdf(version))
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf(version))
        if self.mass is not None:
            el.append(self.mass.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Collision":
        _name = el.get("name", "__default__")
        _laser_retro = _parse_double(el.get("laser_retro", 0))
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry, version) if _c_geometry is not None else None
        _c_surface = el.find("surface")
        _surface = Surface.from_sdf(_c_surface, version) if _c_surface is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts, version) if _c_max_contacts is not None else None
        _c_mass = el.find("mass")
        _mass = Mass.from_sdf(_c_mass, version) if _c_mass is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, laser_retro=_laser_retro, geometry=_geometry, surface=_surface, max_contacts=_max_contacts, mass=_mass, origin=_origin, pose=_pose)


class NormalMap(Model):
    def __init__(self, sdf_version: str, normal_map: str = "__default__"):
        self.__version__ = sdf_version
        self.normal_map = normal_map

    def to_version(self, target_version: str) -> "NormalMap":
        kwargs = {"sdf_version": target_version}
        kwargs["normal_map"] = self.normal_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal_map")
        if self.normal_map is not None:
            el.text = self.normal_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "NormalMap":
        _text = el.text or "__default__"
        _normal_map = _text
        return cls(sdf_version=version, normal_map=_normal_map)


class Shader(Model):
    def __init__(self, sdf_version: str, type: str = "pixel", normal_map: "NormalMap" = None):
        self.__version__ = sdf_version
        self.type = type
        self.normal_map = normal_map

    def to_version(self, target_version: str) -> "Shader":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["normal_map"] = self.normal_map.to_version(target_version) if self.normal_map is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("shader")
        if self.type is not None:
            el.set("type", self.type)
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Shader":
        _type = el.get("type", "pixel")
        _c_normal_map = el.find("normal_map")
        _normal_map = NormalMap.from_sdf(_c_normal_map, version) if _c_normal_map is not None else None
        return cls(sdf_version=version, type=_type, normal_map=_normal_map)


class Emissive(Model):
    def __init__(self, sdf_version: str, emissive: Color = None, rgba: Color = None):
        self.__version__ = sdf_version
        if emissive is None:
            emissive = Color.from_sdf("0 0 0 1")
        if rgba is None:
            rgba = Color.from_sdf("0 0 0 1")
        self.emissive = emissive
        self.rgba = rgba

    def to_version(self, target_version: str) -> "Emissive":
        kwargs = {"sdf_version": target_version}
        kwargs["emissive"] = self.emissive
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("emissive")
        if self.emissive is not None:
            el.text = self.emissive.to_sdf()
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Emissive":
        _text = el.text or "0 0 0 1"
        _emissive = Color.from_sdf(_text)
        _rgba = Color.from_sdf(el.get("rgba", "0 0 0 1"))
        return cls(sdf_version=version, emissive=_emissive, rgba=_rgba)


class Script(Model):
    def __init__(self, sdf_version: str, uri: "Uri" = None, name: "Name" = None):
        self.__version__ = sdf_version
        self.uri = uri
        self.name = name

    def to_version(self, target_version: str) -> "Script":
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("script")
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Script":
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name, version) if _c_name is not None else None
        return cls(sdf_version=version, uri=_uri, name=_name)


class Material(Model):
    def __init__(
        self,
        sdf_version: str,
        script: str = "__default__",
        shader: "Shader" = None,
        ambient: "Ambient" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        emissive: "Emissive" = None
    ):
        self.__version__ = sdf_version
        self.script = script
        self.shader = shader
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.emissive = emissive

    def to_version(self, target_version: str) -> "Material":
        kwargs = {"sdf_version": target_version}
        kwargs["script"] = self.script
        kwargs["shader"] = self.shader.to_version(target_version) if self.shader is not None else None
        kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["emissive"] = self.emissive.to_version(target_version) if self.emissive is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("material")
        if self.script is not None:
            el.set("script", self.script)
        if self.shader is not None:
            el.append(self.shader.to_sdf(version))
        if self.ambient is not None:
            el.append(self.ambient.to_sdf(version))
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.specular is not None:
            el.append(self.specular.to_sdf(version))
        if self.emissive is not None:
            el.append(self.emissive.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Material":
        _script = el.get("script", "__default__")
        _c_shader = el.find("shader")
        _shader = Shader.from_sdf(_c_shader, version) if _c_shader is not None else None
        _c_ambient = el.find("ambient")
        _ambient = Ambient.from_sdf(_c_ambient, version) if _c_ambient is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse, version) if _c_diffuse is not None else None
        _c_specular = el.find("specular")
        _specular = Specular.from_sdf(_c_specular, version) if _c_specular is not None else None
        _c_emissive = el.find("emissive")
        _emissive = Emissive.from_sdf(_c_emissive, version) if _c_emissive is not None else None
        return cls(sdf_version=version, script=_script, shader=_shader, ambient=_ambient, diffuse=_diffuse, specular=_specular, emissive=_emissive)


class Transparency(Model):
    def __init__(self, sdf_version: str, transparency: float = 0.0):
        self.__version__ = sdf_version
        self.transparency = transparency

    def to_version(self, target_version: str) -> "Transparency":
        if self.transparency is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'transparency' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["transparency"] = self.transparency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("transparency")
        if self.transparency is not None:
            el.text = str(self.transparency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Transparency":
        _text = el.text or 0.0
        _transparency = _parse_double(_text)
        if _transparency is not None and cmp_version(version, "1.2") < 0:
            if _transparency != 0.0:
                raise ValueError(f"'transparency' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, transparency=_transparency)


class Visual(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        cast_shadows: bool = True,
        laser_retro: float = 0.0,
        transparency: float = 0.0,
        geometry: "Geometry" = None,
        origin: "Origin" = None,
        material: "Material" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.cast_shadows = cast_shadows
        self.laser_retro = laser_retro
        self.transparency = transparency
        self.geometry = geometry
        self.origin = origin
        self.material = material
        self.pose = pose

    def to_version(self, target_version: str) -> "Visual":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["cast_shadows"] = self.cast_shadows
        kwargs["laser_retro"] = self.laser_retro
        kwargs["transparency"] = self.transparency
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visual")
        if self.name is not None:
            el.set("name", self.name)
        if self.cast_shadows is not None:
            el.set("cast_shadows", str(self.cast_shadows).lower())
        if self.laser_retro is not None:
            el.set("laser_retro", str(self.laser_retro))
        if self.transparency is not None:
            el.set("transparency", str(self.transparency))
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.material is not None:
            el.append(self.material.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Visual":
        _name = el.get("name", "__default__")
        _cast_shadows = el.get("cast_shadows", True).strip().lower() == 'true'
        _laser_retro = _parse_double(el.get("laser_retro", 0.0))
        _transparency = _parse_double(el.get("transparency", 0.0))
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry, version) if _c_geometry is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_material = el.find("material")
        _material = Material.from_sdf(_c_material, version) if _c_material is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, cast_shadows=_cast_shadows, laser_retro=_laser_retro, transparency=_transparency, geometry=_geometry, origin=_origin, material=_material, pose=_pose)


class Plugin(Model):
    def __init__(self, sdf_version: str, name: str = "__default__", filename: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name
        self.filename = filename

    def to_version(self, target_version: str) -> "Plugin":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["filename"] = self.filename
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plugin")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.set("filename", self.filename)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Plugin":
        _name = el.get("name", "__default__")
        _filename = el.get("filename", "__default__")
        return cls(sdf_version=version, name=_name, filename=_filename)


class Samples(Model):
    def __init__(self, sdf_version: str, samples: int = 640):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "Samples":
        if self.samples is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'samples' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("samples")
        if self.samples is not None:
            el.text = str(self.samples)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Samples":
        _text = el.text or 640
        _samples = _parse_uint32(_text)
        if _samples is not None and cmp_version(version, "1.2") < 0:
            if _samples != 640:
                raise ValueError(f"'samples' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, samples=_samples)


class Resolution(Model):
    def __init__(self, sdf_version: str, resolution: float = 1):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Resolution":
        if self.resolution is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'resolution' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["resolution"] = self.resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("resolution")
        if self.resolution is not None:
            el.text = str(self.resolution)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Resolution":
        _text = el.text or 1
        _resolution = _parse_double(_text)
        if _resolution is not None and cmp_version(version, "1.2") < 0:
            if _resolution != 1:
                raise ValueError(f"'resolution' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, resolution=_resolution)


class MinAngle(Model):
    def __init__(self, sdf_version: str, min_angle: float = 0):
        self.__version__ = sdf_version
        self.min_angle = min_angle

    def to_version(self, target_version: str) -> "MinAngle":
        if self.min_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["min_angle"] = self.min_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_angle")
        if self.min_angle is not None:
            el.text = str(self.min_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinAngle":
        _text = el.text or 0
        _min_angle = _parse_double(_text)
        if _min_angle is not None and cmp_version(version, "1.2") < 0:
            if _min_angle != 0:
                raise ValueError(f"'min_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min_angle=_min_angle)


class MaxAngle(Model):
    def __init__(self, sdf_version: str, max_angle: float = 0):
        self.__version__ = sdf_version
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "MaxAngle":
        if self.max_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_angle")
        if self.max_angle is not None:
            el.text = str(self.max_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxAngle":
        _text = el.text or 0
        _max_angle = _parse_double(_text)
        if _max_angle is not None and cmp_version(version, "1.2") < 0:
            if _max_angle != 0:
                raise ValueError(f"'max_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max_angle=_max_angle)


class Horizontal(Model):
    def __init__(
        self,
        sdf_version: str,
        samples: int = 1,
        resolution: float = 1,
        min_angle: float = 0,
        max_angle: float = 0
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "Horizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        kwargs["resolution"] = self.resolution
        kwargs["min_angle"] = self.min_angle
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.samples is not None:
            el.set("samples", str(self.samples))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        if self.min_angle is not None:
            el.set("min_angle", str(self.min_angle))
        if self.max_angle is not None:
            el.set("max_angle", str(self.max_angle))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Horizontal":
        _samples = _parse_uint32(el.get("samples", 1))
        _resolution = _parse_double(el.get("resolution", 1))
        _min_angle = _parse_double(el.get("min_angle", 0))
        _max_angle = _parse_double(el.get("max_angle", 0))
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class Vertical(Model):
    def __init__(
        self,
        sdf_version: str,
        samples: int = 1,
        resolution: float = 1,
        min_angle: float = 0,
        max_angle: float = 0
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "Vertical":
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples
        kwargs["resolution"] = self.resolution
        kwargs["min_angle"] = self.min_angle
        kwargs["max_angle"] = self.max_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.samples is not None:
            el.set("samples", str(self.samples))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        if self.min_angle is not None:
            el.set("min_angle", str(self.min_angle))
        if self.max_angle is not None:
            el.set("max_angle", str(self.max_angle))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Vertical":
        _samples = _parse_uint32(el.get("samples", 1))
        _resolution = _parse_double(el.get("resolution", 1))
        _min_angle = _parse_double(el.get("min_angle", 0))
        _max_angle = _parse_double(el.get("max_angle", 0))
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class Scan(Model):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "Horizontal" = None,
        vertical: "Vertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "Scan":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scan")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Scan":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal, version) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical, version) if _c_vertical is not None else None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Ray(Model):
    def __init__(self, sdf_version: str, scan: "Scan" = None, range: "Range" = None):
        self.__version__ = sdf_version
        self.scan = scan
        self.range = range

    def to_version(self, target_version: str) -> "Ray":
        kwargs = {"sdf_version": target_version}
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ray")
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ray":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan, version) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range, version) if _c_range is not None else None
        return cls(sdf_version=version, scan=_scan, range=_range)


class Rfidtag(Model):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "Rfidtag":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rfidtag")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Rfidtag":
        return cls(sdf_version=version)


class Rfid(Model):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "Rfid":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rfid")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Rfid":
        return cls(sdf_version=version)


class Topic(Model):
    def __init__(self, sdf_version: str, topic: str = "__default"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "Topic":
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Topic":
        _text = el.text or "__default"
        _topic = _text
        return cls(sdf_version=version, topic=_topic)


class AlwaysOn(Model):
    def __init__(self, sdf_version: str, always_on: bool = False):
        self.__version__ = sdf_version
        self.always_on = always_on

    def to_version(self, target_version: str) -> "AlwaysOn":
        if self.always_on is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'always_on' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["always_on"] = self.always_on
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("always_on")
        if self.always_on is not None:
            el.text = str(self.always_on).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AlwaysOn":
        _text = el.text or False
        _always_on = _text.strip().lower() == 'true'
        if _always_on is not None and cmp_version(version, "1.2") < 0:
            if _always_on != False:
                raise ValueError(f"'always_on' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, always_on=_always_on)


class Visualize(Model):
    def __init__(self, sdf_version: str, visualize: bool = False):
        self.__version__ = sdf_version
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Visualize":
        if self.visualize is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["visualize"] = self.visualize
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visualize")
        if self.visualize is not None:
            el.text = str(self.visualize).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Visualize":
        _text = el.text or False
        _visualize = _text.strip().lower() == 'true'
        if _visualize is not None and cmp_version(version, "1.2") < 0:
            if _visualize != False:
                raise ValueError(f"'visualize' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, visualize=_visualize)


class Sensor(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "__default__",
        always_on: bool = False,
        update_rate: float = 0,
        visualize: bool = False,
        plugin: List["Plugin"] = None,
        camera: "Camera" = None,
        ray: "Ray" = None,
        contact: "Contact" = None,
        rfidtag: "Rfidtag" = None,
        rfid: "Rfid" = None,
        origin: "Origin" = None,
        topic: "Topic" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.always_on = always_on
        self.update_rate = update_rate
        self.visualize = visualize
        self.plugin = plugin or []
        self.camera = camera
        self.ray = ray
        self.contact = contact
        self.rfidtag = rfidtag
        self.rfid = rfid
        self.origin = origin
        self.topic = topic
        self.pose = pose

    def to_version(self, target_version: str) -> "Sensor":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["always_on"] = self.always_on
        kwargs["update_rate"] = self.update_rate
        kwargs["visualize"] = self.visualize
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        kwargs["ray"] = self.ray.to_version(target_version) if self.ray is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["rfidtag"] = self.rfidtag.to_version(target_version) if self.rfidtag is not None else None
        kwargs["rfid"] = self.rfid.to_version(target_version) if self.rfid is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sensor")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.always_on is not None:
            el.set("always_on", str(self.always_on).lower())
        if self.update_rate is not None:
            el.set("update_rate", str(self.update_rate))
        if self.visualize is not None:
            el.set("visualize", str(self.visualize).lower())
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.camera is not None:
            el.append(self.camera.to_sdf(version))
        if self.ray is not None:
            el.append(self.ray.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        if self.rfidtag is not None:
            el.append(self.rfidtag.to_sdf(version))
        if self.rfid is not None:
            el.append(self.rfid.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sensor":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _always_on = el.get("always_on", False).strip().lower() == 'true'
        _update_rate = _parse_double(el.get("update_rate", 0))
        _visualize = el.get("visualize", False).strip().lower() == 'true'
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        _c_camera = el.find("camera")
        _camera = Camera.from_sdf(_c_camera, version) if _c_camera is not None else None
        _c_ray = el.find("ray")
        _ray = Ray.from_sdf(_c_ray, version) if _c_ray is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact, version) if _c_contact is not None else None
        _c_rfidtag = el.find("rfidtag")
        _rfidtag = Rfidtag.from_sdf(_c_rfidtag, version) if _c_rfidtag is not None else None
        _c_rfid = el.find("rfid")
        _rfid = Rfid.from_sdf(_c_rfid, version) if _c_rfid is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic, version) if _c_topic is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, type=_type, always_on=_always_on, update_rate=_update_rate, visualize=_visualize, plugin=_plugin, camera=_camera, ray=_ray, contact=_contact, rfidtag=_rfidtag, rfid=_rfid, origin=_origin, topic=_topic, pose=_pose)


class Fov(Model):
    def __init__(self, sdf_version: str, fov: float = 0.785):
        self.__version__ = sdf_version
        self.fov = fov

    def to_version(self, target_version: str) -> "Fov":
        kwargs = {"sdf_version": target_version}
        kwargs["fov"] = self.fov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fov")
        if self.fov is not None:
            el.text = str(self.fov)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fov":
        _text = el.text or 0.785
        _fov = _parse_double(_text)
        return cls(sdf_version=version, fov=_fov)


class NearClip(Model):
    def __init__(self, sdf_version: str, near_clip: float = 0.1):
        self.__version__ = sdf_version
        self.near_clip = near_clip

    def to_version(self, target_version: str) -> "NearClip":
        kwargs = {"sdf_version": target_version}
        kwargs["near_clip"] = self.near_clip
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("near_clip")
        if self.near_clip is not None:
            el.text = str(self.near_clip)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "NearClip":
        _text = el.text or 0.1
        _near_clip = _parse_double(_text)
        return cls(sdf_version=version, near_clip=_near_clip)


class FarClip(Model):
    def __init__(self, sdf_version: str, far_clip: float = 10.0):
        self.__version__ = sdf_version
        self.far_clip = far_clip

    def to_version(self, target_version: str) -> "FarClip":
        kwargs = {"sdf_version": target_version}
        kwargs["far_clip"] = self.far_clip
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("far_clip")
        if self.far_clip is not None:
            el.text = str(self.far_clip)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "FarClip":
        _text = el.text or 10.0
        _far_clip = _parse_double(_text)
        return cls(sdf_version=version, far_clip=_far_clip)


class Projector(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        plugin: List["Plugin"] = None,
        texture: "Texture" = None,
        pose: "Pose" = None,
        fov: "Fov" = None,
        near_clip: "NearClip" = None,
        far_clip: "FarClip" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.plugin = plugin or []
        self.texture = texture
        self.pose = pose
        self.fov = fov
        self.near_clip = near_clip
        self.far_clip = far_clip

    def to_version(self, target_version: str) -> "Projector":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["texture"] = self.texture.to_version(target_version) if self.texture is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["fov"] = self.fov.to_version(target_version) if self.fov is not None else None
        kwargs["near_clip"] = self.near_clip.to_version(target_version) if self.near_clip is not None else None
        kwargs["far_clip"] = self.far_clip.to_version(target_version) if self.far_clip is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("projector")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.texture is not None:
            el.append(self.texture.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.fov is not None:
            el.append(self.fov.to_sdf(version))
        if self.near_clip is not None:
            el.append(self.near_clip.to_sdf(version))
        if self.far_clip is not None:
            el.append(self.far_clip.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Projector":
        _name = el.get("name", "__default__")
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        _c_texture = el.find("texture")
        _texture = Texture.from_sdf(_c_texture, version) if _c_texture is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        _c_fov = el.find("fov")
        _fov = Fov.from_sdf(_c_fov, version) if _c_fov is not None else None
        _c_near_clip = el.find("near_clip")
        _near_clip = NearClip.from_sdf(_c_near_clip, version) if _c_near_clip is not None else None
        _c_far_clip = el.find("far_clip")
        _far_clip = FarClip.from_sdf(_c_far_clip, version) if _c_far_clip is not None else None
        return cls(sdf_version=version, name=_name, plugin=_plugin, texture=_texture, pose=_pose, fov=_fov, near_clip=_near_clip, far_clip=_far_clip)


class Angular(Model):
    def __init__(self, sdf_version: str, angular: float = 0.0):
        self.__version__ = sdf_version
        self.angular = angular

    def to_version(self, target_version: str) -> "Angular":
        kwargs = {"sdf_version": target_version}
        kwargs["angular"] = self.angular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angular")
        if self.angular is not None:
            el.text = str(self.angular)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Angular":
        _text = el.text or 0.0
        _angular = _parse_double(_text)
        return cls(sdf_version=version, angular=_angular)


class Damping(Model):
    def __init__(self, sdf_version: str, linear: "Linear" = None, angular: "Angular" = None):
        self.__version__ = sdf_version
        self.linear = linear
        self.angular = angular

    def to_version(self, target_version: str) -> "Damping":
        kwargs = {"sdf_version": target_version}
        kwargs["linear"] = self.linear.to_version(target_version) if self.linear is not None else None
        kwargs["angular"] = self.angular.to_version(target_version) if self.angular is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("damping")
        if self.linear is not None:
            el.append(self.linear.to_sdf(version))
        if self.angular is not None:
            el.append(self.angular.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Damping":
        _c_linear = el.find("linear")
        _linear = Linear.from_sdf(_c_linear, version) if _c_linear is not None else None
        _c_angular = el.find("angular")
        _angular = Angular.from_sdf(_c_angular, version) if _c_angular is not None else None
        return cls(sdf_version=version, linear=_linear, angular=_angular)


class SelfCollide(Model):
    def __init__(self, sdf_version: str, self_collide: bool = False):
        self.__version__ = sdf_version
        self.self_collide = self_collide

    def to_version(self, target_version: str) -> "SelfCollide":
        if self.self_collide is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["self_collide"] = self.self_collide
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("self_collide")
        if self.self_collide is not None:
            el.text = str(self.self_collide).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SelfCollide":
        _text = el.text or False
        _self_collide = _text.strip().lower() == 'true'
        if _self_collide is not None and cmp_version(version, "1.2") < 0:
            if _self_collide != False:
                raise ValueError(f"'self_collide' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, self_collide=_self_collide)


class Kinematic(Model):
    def __init__(self, sdf_version: str, kinematic: bool = False):
        self.__version__ = sdf_version
        self.kinematic = kinematic

    def to_version(self, target_version: str) -> "Kinematic":
        if self.kinematic is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'kinematic' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["kinematic"] = self.kinematic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("kinematic")
        if self.kinematic is not None:
            el.text = str(self.kinematic).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Kinematic":
        _text = el.text or False
        _kinematic = _text.strip().lower() == 'true'
        if _kinematic is not None and cmp_version(version, "1.2") < 0:
            if _kinematic != False:
                raise ValueError(f"'kinematic' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, kinematic=_kinematic)


class VelocityDecay(Model):
    def __init__(self, sdf_version: str, linear: "Linear" = None, angular: "Angular" = None):
        self.__version__ = sdf_version
        self.linear = linear
        self.angular = angular

    def to_version(self, target_version: str) -> "VelocityDecay":
        kwargs = {"sdf_version": target_version}
        kwargs["linear"] = self.linear.to_version(target_version) if self.linear is not None else None
        kwargs["angular"] = self.angular.to_version(target_version) if self.angular is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("velocity_decay")
        if self.linear is not None:
            el.append(self.linear.to_sdf(version))
        if self.angular is not None:
            el.append(self.angular.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VelocityDecay":
        _c_linear = el.find("linear")
        _linear = Linear.from_sdf(_c_linear, version) if _c_linear is not None else None
        _c_angular = el.find("angular")
        _angular = Angular.from_sdf(_c_angular, version) if _c_angular is not None else None
        return cls(sdf_version=version, linear=_linear, angular=_angular)


class Link(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        gravity: bool = True,
        self_collide: bool = False,
        kinematic: bool = False,
        inertial: "Inertial" = None,
        collision: List["Collision"] = None,
        visual: List["Visual"] = None,
        sensor: List["Sensor"] = None,
        projector: List["Projector"] = None,
        origin: "Origin" = None,
        damping: "Damping" = None,
        pose: "Pose" = None,
        velocity_decay: "VelocityDecay" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.gravity = gravity
        self.self_collide = self_collide
        self.kinematic = kinematic
        self.inertial = inertial
        self.collision = collision or []
        self.visual = visual or []
        self.sensor = sensor or []
        self.projector = projector or []
        self.origin = origin
        self.damping = damping
        self.pose = pose
        self.velocity_decay = velocity_decay

    def to_version(self, target_version: str) -> "Link":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.velocity_decay is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'velocity_decay' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["gravity"] = self.gravity
        kwargs["self_collide"] = self.self_collide
        kwargs["kinematic"] = self.kinematic
        kwargs["inertial"] = self.inertial.to_version(target_version) if self.inertial is not None else None
        kwargs["collision"] = [c.to_version(target_version) for c in (self.collision or [])]
        kwargs["visual"] = [c.to_version(target_version) for c in (self.visual or [])]
        kwargs["sensor"] = [c.to_version(target_version) for c in (self.sensor or [])]
        kwargs["projector"] = [c.to_version(target_version) for c in (self.projector or [])]
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["damping"] = self.damping.to_version(target_version) if self.damping is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["velocity_decay"] = self.velocity_decay.to_version(target_version) if self.velocity_decay is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("link")
        if self.name is not None:
            el.set("name", self.name)
        if self.gravity is not None:
            el.set("gravity", str(self.gravity).lower())
        if self.self_collide is not None:
            el.set("self_collide", str(self.self_collide).lower())
        if self.kinematic is not None:
            el.set("kinematic", str(self.kinematic).lower())
        if self.inertial is not None:
            el.append(self.inertial.to_sdf(version))
        for item in (self.collision or []):
            el.append(item.to_sdf(version))
        for item in (self.visual or []):
            el.append(item.to_sdf(version))
        for item in (self.sensor or []):
            el.append(item.to_sdf(version))
        for item in (self.projector or []):
            el.append(item.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.damping is not None:
            _item_el = self.damping.to_sdf(version)
            if cmp_version(version, "1.2") >= 0:
                _item_el.tag = "velocity_decay"
            else:
                _item_el.tag = "damping"
            el.append(_item_el)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.velocity_decay is not None:
            el.append(self.velocity_decay.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Link":
        _name = el.get("name", "__default__")
        _gravity = el.get("gravity", True).strip().lower() == 'true'
        _self_collide = el.get("self_collide", False).strip().lower() == 'true'
        _kinematic = el.get("kinematic", False).strip().lower() == 'true'
        _c_inertial = el.find("inertial")
        _inertial = Inertial.from_sdf(_c_inertial, version) if _c_inertial is not None else None
        _collision = [Collision.from_sdf(c, version) for c in el.findall("collision")]
        _visual = [Visual.from_sdf(c, version) for c in el.findall("visual")]
        _sensor = [Sensor.from_sdf(c, version) for c in el.findall("sensor")]
        _projector = [Projector.from_sdf(c, version) for c in el.findall("projector")]
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_damping = None
        if cmp_version(version, "1.2") >= 0:
            _c_damping = el.find("velocity_decay")
        else:
            _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping, version) if _c_damping is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _c_velocity_decay = el.find("velocity_decay")
        _velocity_decay = VelocityDecay.from_sdf(_c_velocity_decay, version) if _c_velocity_decay is not None else None
        if _velocity_decay is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'velocity_decay' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, gravity=_gravity, self_collide=_self_collide, kinematic=_kinematic, inertial=_inertial, collision=_collision, visual=_visual, sensor=_sensor, projector=_projector, origin=_origin, damping=_damping, pose=_pose, velocity_decay=_velocity_decay)


class Parent(Model):
    def __init__(self, sdf_version: str, parent: str = "__default__", link: str = "__default__"):
        self.__version__ = sdf_version
        self.parent = parent
        self.link = link

    def to_version(self, target_version: str) -> "Parent":
        kwargs = {"sdf_version": target_version}
        kwargs["parent"] = self.parent
        kwargs["link"] = self.link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("parent")
        if self.parent is not None:
            el.text = self.parent
        if self.link is not None:
            el.set("link", self.link)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Parent":
        _text = el.text or "__default__"
        _parent = _text
        _link = el.get("link", "__default__")
        return cls(sdf_version=version, parent=_parent, link=_link)


class Child(Model):
    def __init__(self, sdf_version: str, child: str = "__default__", link: str = "__default__"):
        self.__version__ = sdf_version
        self.child = child
        self.link = link

    def to_version(self, target_version: str) -> "Child":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Child":
        _text = el.text or "__default__"
        _child = _text
        _link = el.get("link", "__default__")
        return cls(sdf_version=version, child=_child, link=_link)


class ThreadPitch(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "ThreadPitch":
        _text = el.text or 1.0
        _thread_pitch = _parse_double(_text)
        return cls(sdf_version=version, thread_pitch=_thread_pitch)


class Dynamics(Model):
    def __init__(self, sdf_version: str, damping: float = 0, friction: float = 0):
        self.__version__ = sdf_version
        self.damping = damping
        self.friction = friction

    def to_version(self, target_version: str) -> "Dynamics":
        kwargs = {"sdf_version": target_version}
        kwargs["damping"] = self.damping
        kwargs["friction"] = self.friction
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
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Dynamics":
        _damping = _parse_double(el.get("damping", 0))
        _friction = _parse_double(el.get("friction", 0))
        return cls(sdf_version=version, damping=_damping, friction=_friction)


class Lower(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Lower":
        _text = el.text or -1e16
        _lower = _parse_double(_text)
        if _lower is not None and cmp_version(version, "1.2") < 0:
            if _lower != -1e16:
                raise ValueError(f"'lower' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, lower=_lower)


class Upper(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Upper":
        _text = el.text or 1e16
        _upper = _parse_double(_text)
        if _upper is not None and cmp_version(version, "1.2") < 0:
            if _upper != 1e16:
                raise ValueError(f"'upper' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, upper=_upper)


class Effort(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Effort":
        _text = el.text or 0
        _effort = _parse_double(_text)
        if _effort is not None and cmp_version(version, "1.2") < 0:
            if _effort != 0:
                raise ValueError(f"'effort' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, effort=_effort)


class Velocity(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Velocity":
        _text = el.text or 0
        _velocity = _parse_double(_text)
        if _velocity is not None and cmp_version(version, "1.2") < 0:
            if _velocity != 0:
                raise ValueError(f"'velocity' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, velocity=_velocity)


class Limit(Model):
    def __init__(
        self,
        sdf_version: str,
        lower: float = -1e16,
        upper: float = 1e16,
        effort: float = 0,
        velocity: float = 0
    ):
        self.__version__ = sdf_version
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Limit":
        kwargs = {"sdf_version": target_version}
        kwargs["lower"] = self.lower
        kwargs["upper"] = self.upper
        kwargs["effort"] = self.effort
        kwargs["velocity"] = self.velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("limit")
        if self.lower is not None:
            el.set("lower", str(self.lower))
        if self.upper is not None:
            el.set("upper", str(self.upper))
        if self.effort is not None:
            el.set("effort", str(self.effort))
        if self.velocity is not None:
            el.set("velocity", str(self.velocity))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Limit":
        _lower = _parse_double(el.get("lower", -1e16))
        _upper = _parse_double(el.get("upper", 1e16))
        _effort = _parse_double(el.get("effort", 0))
        _velocity = _parse_double(el.get("velocity", 0))
        return cls(sdf_version=version, lower=_lower, upper=_upper, effort=_effort, velocity=_velocity)


class Xyz(Model):
    def __init__(self, sdf_version: str, xyz: Vector3 = None):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz

    def to_version(self, target_version: str) -> "Xyz":
        if self.xyz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xyz")
        if self.xyz is not None:
            el.text = self.xyz.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xyz":
        _text = el.text or "0 0 1"
        _xyz = Vector3.from_sdf(_text)
        if _xyz is not None and cmp_version(version, "1.2") < 0:
            if _xyz != "0 0 1":
                raise ValueError(f"'xyz' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, xyz=_xyz)


class Axis(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        xyz: Vector3 = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None
    ):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit

    def to_version(self, target_version: str) -> "Axis":
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis")
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf(version))
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Axis":
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 1"))
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics, version) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit, version) if _c_limit is not None else None
        return cls(sdf_version=version, xyz=_xyz, dynamics=_dynamics, limit=_limit)


class Axis2(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        xyz: Vector3 = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None
    ):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit

    def to_version(self, target_version: str) -> "Axis2":
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis2")
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf(version))
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Axis2":
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 1"))
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics, version) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit, version) if _c_limit is not None else None
        return cls(sdf_version=version, xyz=_xyz, dynamics=_dynamics, limit=_limit)


class Joint(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "__default__",
        parent: "Parent" = None,
        child: "Child" = None,
        origin: "Origin" = None,
        thread_pitch: "ThreadPitch" = None,
        axis: "Axis" = None,
        axis2: "Axis2" = None,
        physics: "Physics" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.parent = parent
        self.child = child
        self.origin = origin
        self.thread_pitch = thread_pitch
        self.axis = axis
        self.axis2 = axis2
        self.physics = physics
        self.pose = pose

    def to_version(self, target_version: str) -> "Joint":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["parent"] = self.parent.to_version(target_version) if self.parent is not None else None
        kwargs["child"] = self.child.to_version(target_version) if self.child is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["thread_pitch"] = self.thread_pitch.to_version(target_version) if self.thread_pitch is not None else None
        kwargs["axis"] = self.axis.to_version(target_version) if self.axis is not None else None
        kwargs["axis2"] = self.axis2.to_version(target_version) if self.axis2 is not None else None
        kwargs["physics"] = self.physics.to_version(target_version) if self.physics is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("joint")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.parent is not None:
            el.append(self.parent.to_sdf(version))
        if self.child is not None:
            el.append(self.child.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.thread_pitch is not None:
            el.append(self.thread_pitch.to_sdf(version))
        if self.axis is not None:
            el.append(self.axis.to_sdf(version))
        if self.axis2 is not None:
            el.append(self.axis2.to_sdf(version))
        if self.physics is not None:
            el.append(self.physics.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Joint":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _c_parent = el.find("parent")
        _parent = Parent.from_sdf(_c_parent, version) if _c_parent is not None else None
        _c_child = el.find("child")
        _child = Child.from_sdf(_c_child, version) if _c_child is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_thread_pitch = el.find("thread_pitch")
        _thread_pitch = ThreadPitch.from_sdf(_c_thread_pitch, version) if _c_thread_pitch is not None else None
        _c_axis = el.find("axis")
        _axis = Axis.from_sdf(_c_axis, version) if _c_axis is not None else None
        _c_axis2 = el.find("axis2")
        _axis2 = Axis2.from_sdf(_c_axis2, version) if _c_axis2 is not None else None
        _c_physics = el.find("physics")
        _physics = Physics.from_sdf(_c_physics, version) if _c_physics is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, type=_type, parent=_parent, child=_child, origin=_origin, thread_pitch=_thread_pitch, axis=_axis, axis2=_axis2, physics=_physics, pose=_pose)


class DetachSteps(Model):
    def __init__(self, sdf_version: str, detach_steps: int = 40):
        self.__version__ = sdf_version
        self.detach_steps = detach_steps

    def to_version(self, target_version: str) -> "DetachSteps":
        if self.detach_steps is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'detach_steps' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["detach_steps"] = self.detach_steps
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("detach_steps")
        if self.detach_steps is not None:
            el.text = str(self.detach_steps)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "DetachSteps":
        _text = el.text or 40
        _detach_steps = _parse_int32(_text)
        if _detach_steps is not None and cmp_version(version, "1.2") < 0:
            if _detach_steps != 40:
                raise ValueError(f"'detach_steps' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, detach_steps=_detach_steps)


class AttachSteps(Model):
    def __init__(self, sdf_version: str, attach_steps: int = 20):
        self.__version__ = sdf_version
        self.attach_steps = attach_steps

    def to_version(self, target_version: str) -> "AttachSteps":
        if self.attach_steps is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'attach_steps' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["attach_steps"] = self.attach_steps
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("attach_steps")
        if self.attach_steps is not None:
            el.text = str(self.attach_steps)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AttachSteps":
        _text = el.text or 20
        _attach_steps = _parse_int32(_text)
        if _attach_steps is not None and cmp_version(version, "1.2") < 0:
            if _attach_steps != 20:
                raise ValueError(f"'attach_steps' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, attach_steps=_attach_steps)


class MinContactCount(Model):
    def __init__(self, sdf_version: str, min_contact_count: int = 2):
        self.__version__ = sdf_version
        self.min_contact_count = min_contact_count

    def to_version(self, target_version: str) -> "MinContactCount":
        if self.min_contact_count is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'min_contact_count' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["min_contact_count"] = self.min_contact_count
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_contact_count")
        if self.min_contact_count is not None:
            el.text = str(self.min_contact_count)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinContactCount":
        _text = el.text or 2
        _min_contact_count = _parse_uint32(_text)
        if _min_contact_count is not None and cmp_version(version, "1.2") < 0:
            if _min_contact_count != 2:
                raise ValueError(f"'min_contact_count' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min_contact_count=_min_contact_count)


class GraspCheck(Model):
    def __init__(
        self,
        sdf_version: str,
        detach_steps: int = 40,
        attach_steps: int = 20,
        min_contact_count: int = 2
    ):
        self.__version__ = sdf_version
        self.detach_steps = detach_steps
        self.attach_steps = attach_steps
        self.min_contact_count = min_contact_count

    def to_version(self, target_version: str) -> "GraspCheck":
        kwargs = {"sdf_version": target_version}
        kwargs["detach_steps"] = self.detach_steps
        kwargs["attach_steps"] = self.attach_steps
        kwargs["min_contact_count"] = self.min_contact_count
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grasp_check")
        if self.detach_steps is not None:
            el.set("detach_steps", str(self.detach_steps))
        if self.attach_steps is not None:
            el.set("attach_steps", str(self.attach_steps))
        if self.min_contact_count is not None:
            el.set("min_contact_count", str(self.min_contact_count))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "GraspCheck":
        _detach_steps = _parse_int32(el.get("detach_steps", 40))
        _attach_steps = _parse_int32(el.get("attach_steps", 20))
        _min_contact_count = _parse_uint32(el.get("min_contact_count", 2))
        return cls(sdf_version=version, detach_steps=_detach_steps, attach_steps=_attach_steps, min_contact_count=_min_contact_count)


class GripperLink(Model):
    def __init__(self, sdf_version: str, gripper_link: str = "__default__"):
        self.__version__ = sdf_version
        self.gripper_link = gripper_link

    def to_version(self, target_version: str) -> "GripperLink":
        kwargs = {"sdf_version": target_version}
        kwargs["gripper_link"] = self.gripper_link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gripper_link")
        if self.gripper_link is not None:
            el.text = self.gripper_link
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "GripperLink":
        _text = el.text or "__default__"
        _gripper_link = _text
        return cls(sdf_version=version, gripper_link=_gripper_link)


class PalmLink(Model):
    def __init__(self, sdf_version: str, palm_link: str = "__default__"):
        self.__version__ = sdf_version
        self.palm_link = palm_link

    def to_version(self, target_version: str) -> "PalmLink":
        kwargs = {"sdf_version": target_version}
        kwargs["palm_link"] = self.palm_link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("palm_link")
        if self.palm_link is not None:
            el.text = self.palm_link
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PalmLink":
        _text = el.text or "__default__"
        _palm_link = _text
        return cls(sdf_version=version, palm_link=_palm_link)


class Gripper(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        grasp_check: "GraspCheck" = None,
        gripper_link: List["GripperLink"] = None,
        palm_link: "PalmLink" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.grasp_check = grasp_check
        self.gripper_link = gripper_link or []
        self.palm_link = palm_link

    def to_version(self, target_version: str) -> "Gripper":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["grasp_check"] = self.grasp_check.to_version(target_version) if self.grasp_check is not None else None
        kwargs["gripper_link"] = [c.to_version(target_version) for c in (self.gripper_link or [])]
        kwargs["palm_link"] = self.palm_link.to_version(target_version) if self.palm_link is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gripper")
        if self.name is not None:
            el.set("name", self.name)
        if self.grasp_check is not None:
            el.append(self.grasp_check.to_sdf(version))
        for item in (self.gripper_link or []):
            el.append(item.to_sdf(version))
        if self.palm_link is not None:
            el.append(self.palm_link.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gripper":
        _name = el.get("name", "__default__")
        _c_grasp_check = el.find("grasp_check")
        _grasp_check = GraspCheck.from_sdf(_c_grasp_check, version) if _c_grasp_check is not None else None
        _gripper_link = [GripperLink.from_sdf(c, version) for c in el.findall("gripper_link")]
        _c_palm_link = el.find("palm_link")
        _palm_link = PalmLink.from_sdf(_c_palm_link, version) if _c_palm_link is not None else None
        return cls(sdf_version=version, name=_name, grasp_check=_grasp_check, gripper_link=_gripper_link, palm_link=_palm_link)


class Static(Model):
    def __init__(self, sdf_version: str, static: bool = False):
        self.__version__ = sdf_version
        self.static = static

    def to_version(self, target_version: str) -> "Static":
        if self.static is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["static"] = self.static
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("static")
        if self.static is not None:
            el.text = str(self.static).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Static":
        _text = el.text or False
        _static = _text.strip().lower() == 'true'
        if _static is not None and cmp_version(version, "1.2") < 0:
            if _static != False:
                raise ValueError(f"'static' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, static=_static)


class AllowAutoDisable(Model):
    def __init__(self, sdf_version: str, allow_auto_disable: bool = True):
        self.__version__ = sdf_version
        self.allow_auto_disable = allow_auto_disable

    def to_version(self, target_version: str) -> "AllowAutoDisable":
        if self.allow_auto_disable is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'allow_auto_disable' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["allow_auto_disable"] = self.allow_auto_disable
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("allow_auto_disable")
        if self.allow_auto_disable is not None:
            el.text = str(self.allow_auto_disable).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AllowAutoDisable":
        _text = el.text or True
        _allow_auto_disable = _text.strip().lower() == 'true'
        if _allow_auto_disable is not None and cmp_version(version, "1.2") < 0:
            if _allow_auto_disable != True:
                raise ValueError(f"'allow_auto_disable' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, allow_auto_disable=_allow_auto_disable)


class Model(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        static: bool = False,
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        gripper: List["Gripper"] = None,
        origin: "Origin" = None,
        allow_auto_disable: "AllowAutoDisable" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.static = static
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.gripper = gripper or []
        self.origin = origin
        self.allow_auto_disable = allow_auto_disable
        self.pose = pose

    def to_version(self, target_version: str) -> "Model":
        if self.allow_auto_disable is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'allow_auto_disable' is not supported in SDF version {target_version} (added in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["static"] = self.static
        kwargs["link"] = [c.to_version(target_version) for c in (self.link or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["gripper"] = [c.to_version(target_version) for c in (self.gripper or [])]
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["allow_auto_disable"] = self.allow_auto_disable.to_version(target_version) if self.allow_auto_disable is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("model")
        if self.name is not None:
            el.set("name", self.name)
        if self.static is not None:
            el.set("static", str(self.static).lower())
        for item in (self.link or []):
            el.append(item.to_sdf(version))
        for item in (self.joint or []):
            el.append(item.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        for item in (self.gripper or []):
            el.append(item.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.allow_auto_disable is not None:
            el.append(self.allow_auto_disable.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Model":
        _name = el.get("name", "__default__")
        _static = el.get("static", False).strip().lower() == 'true'
        _link = [Link.from_sdf(c, version) for c in el.findall("link")]
        _joint = [Joint.from_sdf(c, version) for c in el.findall("joint")]
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        _gripper = [Gripper.from_sdf(c, version) for c in el.findall("gripper")]
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_allow_auto_disable = el.find("allow_auto_disable")
        _allow_auto_disable = AllowAutoDisable.from_sdf(_c_allow_auto_disable, version) if _c_allow_auto_disable is not None else None
        if _allow_auto_disable is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'allow_auto_disable' is not supported in SDF version {version} (added in 1.2)")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, static=_static, link=_link, joint=_joint, plugin=_plugin, gripper=_gripper, origin=_origin, allow_auto_disable=_allow_auto_disable, pose=_pose)


class Skin(Model):
    def __init__(self, sdf_version: str, filename: str = "__default__", scale: float = 1.0):
        self.__version__ = sdf_version
        self.filename = filename
        self.scale = scale

    def to_version(self, target_version: str) -> "Skin":
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["scale"] = self.scale
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("skin")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.scale is not None:
            el.set("scale", str(self.scale))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Skin":
        _filename = el.get("filename", "__default__")
        _scale = _parse_double(el.get("scale", 1.0))
        return cls(sdf_version=version, filename=_filename, scale=_scale)


class InterpolateX(Model):
    def __init__(self, sdf_version: str, interpolate_x: bool = False):
        self.__version__ = sdf_version
        self.interpolate_x = interpolate_x

    def to_version(self, target_version: str) -> "InterpolateX":
        if self.interpolate_x is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'interpolate_x' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["interpolate_x"] = self.interpolate_x
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("interpolate_x")
        if self.interpolate_x is not None:
            el.text = str(self.interpolate_x).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "InterpolateX":
        _text = el.text or False
        _interpolate_x = _text.strip().lower() == 'true'
        if _interpolate_x is not None and cmp_version(version, "1.2") < 0:
            if _interpolate_x != False:
                raise ValueError(f"'interpolate_x' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, interpolate_x=_interpolate_x)


class Animation(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        filename: str = "__default__",
        scale: float = 1.0,
        interpolate_x: bool = False
    ):
        self.__version__ = sdf_version
        self.name = name
        self.filename = filename
        self.scale = scale
        self.interpolate_x = interpolate_x

    def to_version(self, target_version: str) -> "Animation":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["filename"] = self.filename
        kwargs["scale"] = self.scale
        kwargs["interpolate_x"] = self.interpolate_x
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("animation")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.scale is not None:
            el.set("scale", str(self.scale))
        if self.interpolate_x is not None:
            el.set("interpolate_x", str(self.interpolate_x).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Animation":
        _name = el.get("name", "__default__")
        _filename = el.get("filename", "__default__")
        _scale = _parse_double(el.get("scale", 1.0))
        _interpolate_x = el.get("interpolate_x", False).strip().lower() == 'true'
        return cls(sdf_version=version, name=_name, filename=_filename, scale=_scale, interpolate_x=_interpolate_x)


class Actor(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        static: bool = False,
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        origin: "Origin" = None,
        skin: "Skin" = None,
        animation: List["Animation"] = None,
        script: "Script" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.static = static
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.origin = origin
        self.skin = skin
        self.animation = animation or []
        self.script = script
        self.pose = pose

    def to_version(self, target_version: str) -> "Actor":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["static"] = self.static
        kwargs["link"] = [c.to_version(target_version) for c in (self.link or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["skin"] = self.skin.to_version(target_version) if self.skin is not None else None
        kwargs["animation"] = [c.to_version(target_version) for c in (self.animation or [])]
        kwargs["script"] = self.script.to_version(target_version) if self.script is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("actor")
        if self.name is not None:
            el.set("name", self.name)
        if self.static is not None:
            el.set("static", str(self.static).lower())
        for item in (self.link or []):
            el.append(item.to_sdf(version))
        for item in (self.joint or []):
            el.append(item.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.skin is not None:
            el.append(self.skin.to_sdf(version))
        for item in (self.animation or []):
            el.append(item.to_sdf(version))
        if self.script is not None:
            el.append(self.script.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Actor":
        _name = el.get("name", "__default__")
        _static = el.get("static", False).strip().lower() == 'true'
        _link = [Link.from_sdf(c, version) for c in el.findall("link")]
        _joint = [Joint.from_sdf(c, version) for c in el.findall("joint")]
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_skin = el.find("skin")
        _skin = Skin.from_sdf(_c_skin, version) if _c_skin is not None else None
        _animation = [Animation.from_sdf(c, version) for c in el.findall("animation")]
        _c_script = el.find("script")
        _script = Script.from_sdf(_c_script, version) if _c_script is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, name=_name, static=_static, link=_link, joint=_joint, plugin=_plugin, origin=_origin, skin=_skin, animation=_animation, script=_script, pose=_pose)


class Width(Model):
    def __init__(self, sdf_version: str, width: float = 1.0):
        self.__version__ = sdf_version
        self.width = width

    def to_version(self, target_version: str) -> "Width":
        kwargs = {"sdf_version": target_version}
        kwargs["width"] = self.width
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("width")
        if self.width is not None:
            el.text = str(self.width)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Width":
        _text = el.text or 1.0
        _width = _parse_double(_text)
        return cls(sdf_version=version, width=_width)


class Point(Model):
    def __init__(self, sdf_version: str, point: Vector3 = None):
        self.__version__ = sdf_version
        if point is None:
            point = Vector3.from_sdf("0 0 0")
        self.point = point

    def to_version(self, target_version: str) -> "Point":
        kwargs = {"sdf_version": target_version}
        kwargs["point"] = self.point
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("point")
        if self.point is not None:
            el.text = self.point.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Point":
        _text = el.text or "0 0 0"
        _point = Vector3.from_sdf(_text)
        return cls(sdf_version=version, point=_point)


class Road(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        width: "Width" = None,
        point: List["Point"] = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.width = width
        self.point = point or []

    def to_version(self, target_version: str) -> "Road":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["width"] = self.width.to_version(target_version) if self.width is not None else None
        kwargs["point"] = [c.to_version(target_version) for c in (self.point or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("road")
        if self.name is not None:
            el.set("name", self.name)
        if self.width is not None:
            el.append(self.width.to_sdf(version))
        for item in (self.point or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Road":
        _name = el.get("name", "__default__")
        _c_width = el.find("width")
        _width = Width.from_sdf(_c_width, version) if _c_width is not None else None
        _point = [Point.from_sdf(c, version) for c in el.findall("point")]
        return cls(sdf_version=version, name=_name, width=_width, point=_point)


class Time(Model):
    def __init__(self, sdf_version: str, time: float = "0 0"):
        self.__version__ = sdf_version
        self.time = time

    def to_version(self, target_version: str) -> "Time":
        if self.time is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'time' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["time"] = self.time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("time")
        if self.time is not None:
            el.text = str(self.time)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Time":
        _text = el.text or "0 0"
        _time = _parse_double(_text)
        if _time is not None and cmp_version(version, "1.2") < 0:
            if _time != "0 0":
                raise ValueError(f"'time' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, time=_time)


class State(Model):
    def __init__(
        self,
        sdf_version: str,
        world_name: str = "__default__",
        time: float = "0 0",
        model: List["Model"] = None
    ):
        self.__version__ = sdf_version
        self.world_name = world_name
        self.time = time
        self.model = model or []

    def to_version(self, target_version: str) -> "State":
        kwargs = {"sdf_version": target_version}
        kwargs["world_name"] = self.world_name
        kwargs["time"] = self.time
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("state")
        if self.world_name is not None:
            el.set("world_name", self.world_name)
        if self.time is not None:
            el.set("time", str(self.time))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "State":
        _world_name = el.get("world_name", "__default__")
        _time = _parse_double(el.get("time", "0 0"))
        _model = [Model.from_sdf(c, version) for c in el.findall("model")]
        return cls(sdf_version=version, world_name=_world_name, time=_time, model=_model)


class World(Model):
    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "physics::gravity", "to": "gravity"}, {"type": "move", "from": "physics::magnetic_field", "to": "magnetic_field"}]}]

    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        gui: "Gui" = None,
        physics: "Physics" = None,
        scene: "Scene" = None,
        light: List["Light"] = None,
        model: List["Model"] = None,
        actor: List["Actor"] = None,
        plugin: List["Plugin"] = None,
        joint: List["Joint"] = None,
        road: List["Road"] = None,
        state: List["State"] = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.gui = gui
        self.physics = physics
        self.scene = scene
        self.light = light or []
        self.model = model or []
        self.actor = actor or []
        self.plugin = plugin or []
        self.joint = joint or []
        self.road = road or []
        self.state = state or []

    def to_version(self, target_version: str) -> "World":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["gui"] = self.gui.to_version(target_version) if self.gui is not None else None
        kwargs["physics"] = self.physics.to_version(target_version) if self.physics is not None else None
        kwargs["scene"] = self.scene.to_version(target_version) if self.scene is not None else None
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["actor"] = [c.to_version(target_version) for c in (self.actor or [])]
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        kwargs["road"] = [c.to_version(target_version) for c in (self.road or [])]
        kwargs["state"] = [c.to_version(target_version) for c in (self.state or [])]
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("world")
        if self.name is not None:
            el.set("name", self.name)
        if self.gui is not None:
            el.append(self.gui.to_sdf(version))
        if self.physics is not None:
            el.append(self.physics.to_sdf(version))
        if self.scene is not None:
            el.append(self.scene.to_sdf(version))
        for item in (self.light or []):
            el.append(item.to_sdf(version))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        for item in (self.actor or []):
            el.append(item.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        for item in (self.joint or []):
            el.append(item.to_sdf(version))
        for item in (self.road or []):
            el.append(item.to_sdf(version))
        for item in (self.state or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "World":
        _name = el.get("name", "__default__")
        _c_gui = el.find("gui")
        _gui = Gui.from_sdf(_c_gui, version) if _c_gui is not None else None
        _c_physics = el.find("physics")
        _physics = Physics.from_sdf(_c_physics, version) if _c_physics is not None else None
        _c_scene = el.find("scene")
        _scene = Scene.from_sdf(_c_scene, version) if _c_scene is not None else None
        _light = [Light.from_sdf(c, version) for c in el.findall("light")]
        _model = [Model.from_sdf(c, version) for c in el.findall("model")]
        _actor = [Actor.from_sdf(c, version) for c in el.findall("actor")]
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        _joint = [Joint.from_sdf(c, version) for c in el.findall("joint")]
        _road = [Road.from_sdf(c, version) for c in el.findall("road")]
        _state = [State.from_sdf(c, version) for c in el.findall("state")]
        return cls(sdf_version=version, name=_name, gui=_gui, physics=_physics, scene=_scene, light=_light, model=_model, actor=_actor, plugin=_plugin, joint=_joint, road=_road, state=_state)


class Gazebo(Model):
    def __init__(
        self,
        sdf_version: str,
        version: str = "1.0",
        world: List["World"] = None,
        model: List["Model"] = None,
        actor: List["Actor"] = None,
        light: List["Light"] = None
    ):
        self.__version__ = sdf_version
        self.version = version
        self.world = world or []
        self.model = model or []
        self.actor = actor or []
        self.light = light or []

    def to_version(self, target_version: str) -> "Gazebo":
        kwargs = {"sdf_version": target_version}
        kwargs["version"] = self.version
        kwargs["world"] = [c.to_version(target_version) for c in (self.world or [])]
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["actor"] = [c.to_version(target_version) for c in (self.actor or [])]
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gazebo")
        if self.version is not None:
            el.set("version", self.version)
        for item in (self.world or []):
            el.append(item.to_sdf(version))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        for item in (self.actor or []):
            el.append(item.to_sdf(version))
        for item in (self.light or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gazebo":
        _version = el.get("version", "1.0")
        _world = [World.from_sdf(c, version) for c in el.findall("world")]
        _model = [Model.from_sdf(c, version) for c in el.findall("model")]
        _actor = [Actor.from_sdf(c, version) for c in el.findall("actor")]
        _light = [Light.from_sdf(c, version) for c in el.findall("light")]
        return cls(sdf_version=version, version=_version, world=_world, model=_model, actor=_actor, light=_light)
