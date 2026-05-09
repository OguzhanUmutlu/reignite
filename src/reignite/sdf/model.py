from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ._base import Model
from ..utils.color import Color
from ..utils.pose import Pose
from ..utils.vector2d import Vector2d
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


class Pose(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: Pose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Pose":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.12)")
        if self.degrees is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["relative_to"] = self.relative_to
        kwargs["rotation_format"] = self.rotation_format
        kwargs["degrees"] = self.degrees
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
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        if _pose is not None and cmp_version(version, "1.2") < 0:
            if _pose != "0 0 0 0 0 0":
                raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _relative_to = el.get("relative_to", "")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                raise ValueError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if _rotation_format is not None and cmp_version(version, "1.12") < 0:
            if _rotation_format != "euler_rpy":
                raise ValueError(f"'rotation_format' is not supported in SDF version {version} (added in 1.12)")
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        if _degrees is not None and cmp_version(version, "1.12") < 0:
            if _degrees != False:
                raise ValueError(f"'degrees' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, pose=_pose, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Density(Model):
    def __init__(self, sdf_version: str, density: float = 1000.0):
        self.__version__ = sdf_version
        self.density = density

    def to_version(self, target_version: str) -> "Density":
        if self.density is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.12)")
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
        _text = el.text or 1000.0
        _density = _parse_double(_text)
        if _density is not None and cmp_version(version, "1.12") < 0:
            if _density != 1000.0:
                raise ValueError(f"'density' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, density=_density)


class AutoInertiaParams(Model):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "AutoInertiaParams":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("auto_inertia_params")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AutoInertiaParams":
        return cls(sdf_version=version)


class Xx(Model):
    def __init__(self, sdf_version: str, xx: float = 0.0):
        self.__version__ = sdf_version
        self.xx = xx

    def to_version(self, target_version: str) -> "Xx":
        kwargs = {"sdf_version": target_version}
        kwargs["xx"] = self.xx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xx")
        if self.xx is not None:
            el.text = str(self.xx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xx":
        _text = el.text or 0.0
        _xx = _parse_double(_text)
        return cls(sdf_version=version, xx=_xx)


class Xy(Model):
    def __init__(self, sdf_version: str, xy: float = 0.0):
        self.__version__ = sdf_version
        self.xy = xy

    def to_version(self, target_version: str) -> "Xy":
        kwargs = {"sdf_version": target_version}
        kwargs["xy"] = self.xy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xy")
        if self.xy is not None:
            el.text = str(self.xy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xy":
        _text = el.text or 0.0
        _xy = _parse_double(_text)
        return cls(sdf_version=version, xy=_xy)


class Xz(Model):
    def __init__(self, sdf_version: str, xz: float = 0.0):
        self.__version__ = sdf_version
        self.xz = xz

    def to_version(self, target_version: str) -> "Xz":
        kwargs = {"sdf_version": target_version}
        kwargs["xz"] = self.xz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xz")
        if self.xz is not None:
            el.text = str(self.xz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xz":
        _text = el.text or 0.0
        _xz = _parse_double(_text)
        return cls(sdf_version=version, xz=_xz)


class Xp(Model):
    def __init__(self, sdf_version: str, xp: float = 0.0):
        self.__version__ = sdf_version
        self.xp = xp

    def to_version(self, target_version: str) -> "Xp":
        kwargs = {"sdf_version": target_version}
        kwargs["xp"] = self.xp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xp")
        if self.xp is not None:
            el.text = str(self.xp)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xp":
        _text = el.text or 0.0
        _xp = _parse_double(_text)
        return cls(sdf_version=version, xp=_xp)


class Xq(Model):
    def __init__(self, sdf_version: str, xq: float = 0.0):
        self.__version__ = sdf_version
        self.xq = xq

    def to_version(self, target_version: str) -> "Xq":
        kwargs = {"sdf_version": target_version}
        kwargs["xq"] = self.xq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xq")
        if self.xq is not None:
            el.text = str(self.xq)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xq":
        _text = el.text or 0.0
        _xq = _parse_double(_text)
        return cls(sdf_version=version, xq=_xq)


class Xr(Model):
    def __init__(self, sdf_version: str, xr: float = 0.0):
        self.__version__ = sdf_version
        self.xr = xr

    def to_version(self, target_version: str) -> "Xr":
        kwargs = {"sdf_version": target_version}
        kwargs["xr"] = self.xr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xr")
        if self.xr is not None:
            el.text = str(self.xr)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xr":
        _text = el.text or 0.0
        _xr = _parse_double(_text)
        return cls(sdf_version=version, xr=_xr)


class Yy(Model):
    def __init__(self, sdf_version: str, yy: float = 0.0):
        self.__version__ = sdf_version
        self.yy = yy

    def to_version(self, target_version: str) -> "Yy":
        kwargs = {"sdf_version": target_version}
        kwargs["yy"] = self.yy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yy")
        if self.yy is not None:
            el.text = str(self.yy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Yy":
        _text = el.text or 0.0
        _yy = _parse_double(_text)
        return cls(sdf_version=version, yy=_yy)


class Yz(Model):
    def __init__(self, sdf_version: str, yz: float = 0.0):
        self.__version__ = sdf_version
        self.yz = yz

    def to_version(self, target_version: str) -> "Yz":
        kwargs = {"sdf_version": target_version}
        kwargs["yz"] = self.yz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yz")
        if self.yz is not None:
            el.text = str(self.yz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Yz":
        _text = el.text or 0.0
        _yz = _parse_double(_text)
        return cls(sdf_version=version, yz=_yz)


class Yp(Model):
    def __init__(self, sdf_version: str, yp: float = 0.0):
        self.__version__ = sdf_version
        self.yp = yp

    def to_version(self, target_version: str) -> "Yp":
        kwargs = {"sdf_version": target_version}
        kwargs["yp"] = self.yp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yp")
        if self.yp is not None:
            el.text = str(self.yp)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Yp":
        _text = el.text or 0.0
        _yp = _parse_double(_text)
        return cls(sdf_version=version, yp=_yp)


class Yq(Model):
    def __init__(self, sdf_version: str, yq: float = 0.0):
        self.__version__ = sdf_version
        self.yq = yq

    def to_version(self, target_version: str) -> "Yq":
        kwargs = {"sdf_version": target_version}
        kwargs["yq"] = self.yq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yq")
        if self.yq is not None:
            el.text = str(self.yq)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Yq":
        _text = el.text or 0.0
        _yq = _parse_double(_text)
        return cls(sdf_version=version, yq=_yq)


class Yr(Model):
    def __init__(self, sdf_version: str, yr: float = 0.0):
        self.__version__ = sdf_version
        self.yr = yr

    def to_version(self, target_version: str) -> "Yr":
        kwargs = {"sdf_version": target_version}
        kwargs["yr"] = self.yr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("yr")
        if self.yr is not None:
            el.text = str(self.yr)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Yr":
        _text = el.text or 0.0
        _yr = _parse_double(_text)
        return cls(sdf_version=version, yr=_yr)


class Zz(Model):
    def __init__(self, sdf_version: str, zz: float = 0.0):
        self.__version__ = sdf_version
        self.zz = zz

    def to_version(self, target_version: str) -> "Zz":
        kwargs = {"sdf_version": target_version}
        kwargs["zz"] = self.zz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("zz")
        if self.zz is not None:
            el.text = str(self.zz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Zz":
        _text = el.text or 0.0
        _zz = _parse_double(_text)
        return cls(sdf_version=version, zz=_zz)


class Zp(Model):
    def __init__(self, sdf_version: str, zp: float = 0.0):
        self.__version__ = sdf_version
        self.zp = zp

    def to_version(self, target_version: str) -> "Zp":
        kwargs = {"sdf_version": target_version}
        kwargs["zp"] = self.zp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("zp")
        if self.zp is not None:
            el.text = str(self.zp)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Zp":
        _text = el.text or 0.0
        _zp = _parse_double(_text)
        return cls(sdf_version=version, zp=_zp)


class Zq(Model):
    def __init__(self, sdf_version: str, zq: float = 0.0):
        self.__version__ = sdf_version
        self.zq = zq

    def to_version(self, target_version: str) -> "Zq":
        kwargs = {"sdf_version": target_version}
        kwargs["zq"] = self.zq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("zq")
        if self.zq is not None:
            el.text = str(self.zq)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Zq":
        _text = el.text or 0.0
        _zq = _parse_double(_text)
        return cls(sdf_version=version, zq=_zq)


class Zr(Model):
    def __init__(self, sdf_version: str, zr: float = 0.0):
        self.__version__ = sdf_version
        self.zr = zr

    def to_version(self, target_version: str) -> "Zr":
        kwargs = {"sdf_version": target_version}
        kwargs["zr"] = self.zr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("zr")
        if self.zr is not None:
            el.text = str(self.zr)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Zr":
        _text = el.text or 0.0
        _zr = _parse_double(_text)
        return cls(sdf_version=version, zr=_zr)


class Pp(Model):
    def __init__(self, sdf_version: str, pp: float = 0.0):
        self.__version__ = sdf_version
        self.pp = pp

    def to_version(self, target_version: str) -> "Pp":
        kwargs = {"sdf_version": target_version}
        kwargs["pp"] = self.pp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pp")
        if self.pp is not None:
            el.text = str(self.pp)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pp":
        _text = el.text or 0.0
        _pp = _parse_double(_text)
        return cls(sdf_version=version, pp=_pp)


class Pq(Model):
    def __init__(self, sdf_version: str, pq: float = 0.0):
        self.__version__ = sdf_version
        self.pq = pq

    def to_version(self, target_version: str) -> "Pq":
        kwargs = {"sdf_version": target_version}
        kwargs["pq"] = self.pq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pq")
        if self.pq is not None:
            el.text = str(self.pq)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pq":
        _text = el.text or 0.0
        _pq = _parse_double(_text)
        return cls(sdf_version=version, pq=_pq)


class Pr(Model):
    def __init__(self, sdf_version: str, pr: float = 0.0):
        self.__version__ = sdf_version
        self.pr = pr

    def to_version(self, target_version: str) -> "Pr":
        kwargs = {"sdf_version": target_version}
        kwargs["pr"] = self.pr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pr")
        if self.pr is not None:
            el.text = str(self.pr)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pr":
        _text = el.text or 0.0
        _pr = _parse_double(_text)
        return cls(sdf_version=version, pr=_pr)


class Qq(Model):
    def __init__(self, sdf_version: str, qq: float = 0.0):
        self.__version__ = sdf_version
        self.qq = qq

    def to_version(self, target_version: str) -> "Qq":
        kwargs = {"sdf_version": target_version}
        kwargs["qq"] = self.qq
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("qq")
        if self.qq is not None:
            el.text = str(self.qq)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Qq":
        _text = el.text or 0.0
        _qq = _parse_double(_text)
        return cls(sdf_version=version, qq=_qq)


class Qr(Model):
    def __init__(self, sdf_version: str, qr: float = 0.0):
        self.__version__ = sdf_version
        self.qr = qr

    def to_version(self, target_version: str) -> "Qr":
        kwargs = {"sdf_version": target_version}
        kwargs["qr"] = self.qr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("qr")
        if self.qr is not None:
            el.text = str(self.qr)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Qr":
        _text = el.text or 0.0
        _qr = _parse_double(_text)
        return cls(sdf_version=version, qr=_qr)


class Rr(Model):
    def __init__(self, sdf_version: str, rr: float = 0.0):
        self.__version__ = sdf_version
        self.rr = rr

    def to_version(self, target_version: str) -> "Rr":
        kwargs = {"sdf_version": target_version}
        kwargs["rr"] = self.rr
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rr")
        if self.rr is not None:
            el.text = str(self.rr)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Rr":
        _text = el.text or 0.0
        _rr = _parse_double(_text)
        return cls(sdf_version=version, rr=_rr)


class FluidAddedMass(Model):
    def __init__(
        self,
        sdf_version: str,
        xx: "Xx" = None,
        xy: "Xy" = None,
        xz: "Xz" = None,
        xp: "Xp" = None,
        xq: "Xq" = None,
        xr: "Xr" = None,
        yy: "Yy" = None,
        yz: "Yz" = None,
        yp: "Yp" = None,
        yq: "Yq" = None,
        yr: "Yr" = None,
        zz: "Zz" = None,
        zp: "Zp" = None,
        zq: "Zq" = None,
        zr: "Zr" = None,
        pp: "Pp" = None,
        pq: "Pq" = None,
        pr: "Pr" = None,
        qq: "Qq" = None,
        qr: "Qr" = None,
        rr: "Rr" = None
    ):
        self.__version__ = sdf_version
        self.xx = xx
        self.xy = xy
        self.xz = xz
        self.xp = xp
        self.xq = xq
        self.xr = xr
        self.yy = yy
        self.yz = yz
        self.yp = yp
        self.yq = yq
        self.yr = yr
        self.zz = zz
        self.zp = zp
        self.zq = zq
        self.zr = zr
        self.pp = pp
        self.pq = pq
        self.pr = pr
        self.qq = qq
        self.qr = qr
        self.rr = rr

    def to_version(self, target_version: str) -> "FluidAddedMass":
        kwargs = {"sdf_version": target_version}
        kwargs["xx"] = self.xx.to_version(target_version) if self.xx is not None else None
        kwargs["xy"] = self.xy.to_version(target_version) if self.xy is not None else None
        kwargs["xz"] = self.xz.to_version(target_version) if self.xz is not None else None
        kwargs["xp"] = self.xp.to_version(target_version) if self.xp is not None else None
        kwargs["xq"] = self.xq.to_version(target_version) if self.xq is not None else None
        kwargs["xr"] = self.xr.to_version(target_version) if self.xr is not None else None
        kwargs["yy"] = self.yy.to_version(target_version) if self.yy is not None else None
        kwargs["yz"] = self.yz.to_version(target_version) if self.yz is not None else None
        kwargs["yp"] = self.yp.to_version(target_version) if self.yp is not None else None
        kwargs["yq"] = self.yq.to_version(target_version) if self.yq is not None else None
        kwargs["yr"] = self.yr.to_version(target_version) if self.yr is not None else None
        kwargs["zz"] = self.zz.to_version(target_version) if self.zz is not None else None
        kwargs["zp"] = self.zp.to_version(target_version) if self.zp is not None else None
        kwargs["zq"] = self.zq.to_version(target_version) if self.zq is not None else None
        kwargs["zr"] = self.zr.to_version(target_version) if self.zr is not None else None
        kwargs["pp"] = self.pp.to_version(target_version) if self.pp is not None else None
        kwargs["pq"] = self.pq.to_version(target_version) if self.pq is not None else None
        kwargs["pr"] = self.pr.to_version(target_version) if self.pr is not None else None
        kwargs["qq"] = self.qq.to_version(target_version) if self.qq is not None else None
        kwargs["qr"] = self.qr.to_version(target_version) if self.qr is not None else None
        kwargs["rr"] = self.rr.to_version(target_version) if self.rr is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fluid_added_mass")
        if self.xx is not None:
            el.append(self.xx.to_sdf(version))
        if self.xy is not None:
            el.append(self.xy.to_sdf(version))
        if self.xz is not None:
            el.append(self.xz.to_sdf(version))
        if self.xp is not None:
            el.append(self.xp.to_sdf(version))
        if self.xq is not None:
            el.append(self.xq.to_sdf(version))
        if self.xr is not None:
            el.append(self.xr.to_sdf(version))
        if self.yy is not None:
            el.append(self.yy.to_sdf(version))
        if self.yz is not None:
            el.append(self.yz.to_sdf(version))
        if self.yp is not None:
            el.append(self.yp.to_sdf(version))
        if self.yq is not None:
            el.append(self.yq.to_sdf(version))
        if self.yr is not None:
            el.append(self.yr.to_sdf(version))
        if self.zz is not None:
            el.append(self.zz.to_sdf(version))
        if self.zp is not None:
            el.append(self.zp.to_sdf(version))
        if self.zq is not None:
            el.append(self.zq.to_sdf(version))
        if self.zr is not None:
            el.append(self.zr.to_sdf(version))
        if self.pp is not None:
            el.append(self.pp.to_sdf(version))
        if self.pq is not None:
            el.append(self.pq.to_sdf(version))
        if self.pr is not None:
            el.append(self.pr.to_sdf(version))
        if self.qq is not None:
            el.append(self.qq.to_sdf(version))
        if self.qr is not None:
            el.append(self.qr.to_sdf(version))
        if self.rr is not None:
            el.append(self.rr.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "FluidAddedMass":
        _c_xx = el.find("xx")
        _xx = Xx.from_sdf(_c_xx, version) if _c_xx is not None else None
        _c_xy = el.find("xy")
        _xy = Xy.from_sdf(_c_xy, version) if _c_xy is not None else None
        _c_xz = el.find("xz")
        _xz = Xz.from_sdf(_c_xz, version) if _c_xz is not None else None
        _c_xp = el.find("xp")
        _xp = Xp.from_sdf(_c_xp, version) if _c_xp is not None else None
        _c_xq = el.find("xq")
        _xq = Xq.from_sdf(_c_xq, version) if _c_xq is not None else None
        _c_xr = el.find("xr")
        _xr = Xr.from_sdf(_c_xr, version) if _c_xr is not None else None
        _c_yy = el.find("yy")
        _yy = Yy.from_sdf(_c_yy, version) if _c_yy is not None else None
        _c_yz = el.find("yz")
        _yz = Yz.from_sdf(_c_yz, version) if _c_yz is not None else None
        _c_yp = el.find("yp")
        _yp = Yp.from_sdf(_c_yp, version) if _c_yp is not None else None
        _c_yq = el.find("yq")
        _yq = Yq.from_sdf(_c_yq, version) if _c_yq is not None else None
        _c_yr = el.find("yr")
        _yr = Yr.from_sdf(_c_yr, version) if _c_yr is not None else None
        _c_zz = el.find("zz")
        _zz = Zz.from_sdf(_c_zz, version) if _c_zz is not None else None
        _c_zp = el.find("zp")
        _zp = Zp.from_sdf(_c_zp, version) if _c_zp is not None else None
        _c_zq = el.find("zq")
        _zq = Zq.from_sdf(_c_zq, version) if _c_zq is not None else None
        _c_zr = el.find("zr")
        _zr = Zr.from_sdf(_c_zr, version) if _c_zr is not None else None
        _c_pp = el.find("pp")
        _pp = Pp.from_sdf(_c_pp, version) if _c_pp is not None else None
        _c_pq = el.find("pq")
        _pq = Pq.from_sdf(_c_pq, version) if _c_pq is not None else None
        _c_pr = el.find("pr")
        _pr = Pr.from_sdf(_c_pr, version) if _c_pr is not None else None
        _c_qq = el.find("qq")
        _qq = Qq.from_sdf(_c_qq, version) if _c_qq is not None else None
        _c_qr = el.find("qr")
        _qr = Qr.from_sdf(_c_qr, version) if _c_qr is not None else None
        _c_rr = el.find("rr")
        _rr = Rr.from_sdf(_c_rr, version) if _c_rr is not None else None
        return cls(sdf_version=version, xx=_xx, xy=_xy, xz=_xz, xp=_xp, xq=_xq, xr=_xr, yy=_yy, yz=_yz, yp=_yp, yq=_yq, yr=_yr, zz=_zz, zp=_zp, zq=_zq, zr=_zr, pp=_pp, pq=_pq, pr=_pr, qq=_qq, qr=_qr, rr=_rr)


class Inertial(Model):
    def __init__(
        self,
        sdf_version: str,
        mass: float = 1.0,
        density: float = 1.0,
        auto: bool = False,
        origin: "Origin" = None,
        inertia: "Inertia" = None,
        pose: "Pose" = None,
        auto_inertia_params: "AutoInertiaParams" = None,
        fluid_added_mass: "FluidAddedMass" = None
    ):
        self.__version__ = sdf_version
        self.mass = mass
        self.density = density
        self.auto = auto
        self.origin = origin
        self.inertia = inertia
        self.pose = pose
        self.auto_inertia_params = auto_inertia_params
        self.fluid_added_mass = fluid_added_mass

    def to_version(self, target_version: str) -> "Inertial":
        if self.auto is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'auto' is not supported in SDF version {target_version} (added in 1.12)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.auto_inertia_params is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'auto_inertia_params' is not supported in SDF version {target_version} (added in 1.12)")
        if self.fluid_added_mass is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'fluid_added_mass' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["mass"] = self.mass
        kwargs["density"] = self.density
        kwargs["auto"] = self.auto
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["inertia"] = self.inertia.to_version(target_version) if self.inertia is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["auto_inertia_params"] = self.auto_inertia_params.to_version(target_version) if self.auto_inertia_params is not None else None
        kwargs["fluid_added_mass"] = self.fluid_added_mass.to_version(target_version) if self.fluid_added_mass is not None else None
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
        if self.auto is not None:
            el.set("auto", str(self.auto).lower())
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.inertia is not None:
            el.append(self.inertia.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.auto_inertia_params is not None:
            el.append(self.auto_inertia_params.to_sdf(version))
        if self.fluid_added_mass is not None:
            el.append(self.fluid_added_mass.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Inertial":
        _mass = _parse_double(el.get("mass", 1.0))
        _density = _parse_double(el.get("density", 1.0))
        _auto = el.get("auto", False).strip().lower() == 'true'
        if _auto is not None and cmp_version(version, "1.12") < 0:
            if _auto != False:
                raise ValueError(f"'auto' is not supported in SDF version {version} (added in 1.12)")
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_inertia = el.find("inertia")
        _inertia = Inertia.from_sdf(_c_inertia, version) if _c_inertia is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _c_auto_inertia_params = el.find("auto_inertia_params")
        _auto_inertia_params = AutoInertiaParams.from_sdf(_c_auto_inertia_params, version) if _c_auto_inertia_params is not None else None
        if _auto_inertia_params is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'auto_inertia_params' is not supported in SDF version {version} (added in 1.12)")
        _c_fluid_added_mass = el.find("fluid_added_mass")
        _fluid_added_mass = FluidAddedMass.from_sdf(_c_fluid_added_mass, version) if _c_fluid_added_mass is not None else None
        if _fluid_added_mass is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'fluid_added_mass' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, mass=_mass, density=_density, auto=_auto, origin=_origin, inertia=_inertia, pose=_pose, auto_inertia_params=_auto_inertia_params, fluid_added_mass=_fluid_added_mass)


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


class Center(Model):
    def __init__(self, sdf_version: str, center: bool = False):
        self.__version__ = sdf_version
        self.center = center

    def to_version(self, target_version: str) -> "Center":
        kwargs = {"sdf_version": target_version}
        kwargs["center"] = self.center
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("center")
        if self.center is not None:
            el.text = str(self.center).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Center":
        _text = el.text or False
        _center = _text.strip().lower() == 'true'
        return cls(sdf_version=version, center=_center)


class Submesh(Model):
    def __init__(self, sdf_version: str, name: "Name" = None, center: "Center" = None):
        self.__version__ = sdf_version
        self.name = name
        self.center = center

    def to_version(self, target_version: str) -> "Submesh":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["center"] = self.center.to_version(target_version) if self.center is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("submesh")
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        if self.center is not None:
            el.append(self.center.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Submesh":
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name, version) if _c_name is not None else None
        _c_center = el.find("center")
        _center = Center.from_sdf(_c_center, version) if _c_center is not None else None
        return cls(sdf_version=version, name=_name, center=_center)


class MaxConvexHulls(Model):
    def __init__(self, sdf_version: str, max_convex_hulls: int = 16):
        self.__version__ = sdf_version
        self.max_convex_hulls = max_convex_hulls

    def to_version(self, target_version: str) -> "MaxConvexHulls":
        kwargs = {"sdf_version": target_version}
        kwargs["max_convex_hulls"] = self.max_convex_hulls
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_convex_hulls")
        if self.max_convex_hulls is not None:
            el.text = str(self.max_convex_hulls)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxConvexHulls":
        _text = el.text or 16
        _max_convex_hulls = _parse_uint32(_text)
        return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls)


class VoxelResolution(Model):
    def __init__(self, sdf_version: str, voxel_resolution: int = 200000):
        self.__version__ = sdf_version
        self.voxel_resolution = voxel_resolution

    def to_version(self, target_version: str) -> "VoxelResolution":
        kwargs = {"sdf_version": target_version}
        kwargs["voxel_resolution"] = self.voxel_resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("voxel_resolution")
        if self.voxel_resolution is not None:
            el.text = str(self.voxel_resolution)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VoxelResolution":
        _text = el.text or 200000
        _voxel_resolution = _parse_uint32(_text)
        return cls(sdf_version=version, voxel_resolution=_voxel_resolution)


class ConvexDecomposition(Model):
    def __init__(
        self,
        sdf_version: str,
        max_convex_hulls: "MaxConvexHulls" = None,
        voxel_resolution: "VoxelResolution" = None
    ):
        self.__version__ = sdf_version
        self.max_convex_hulls = max_convex_hulls
        self.voxel_resolution = voxel_resolution

    def to_version(self, target_version: str) -> "ConvexDecomposition":
        kwargs = {"sdf_version": target_version}
        kwargs["max_convex_hulls"] = self.max_convex_hulls.to_version(target_version) if self.max_convex_hulls is not None else None
        kwargs["voxel_resolution"] = self.voxel_resolution.to_version(target_version) if self.voxel_resolution is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("convex_decomposition")
        if self.max_convex_hulls is not None:
            el.append(self.max_convex_hulls.to_sdf(version))
        if self.voxel_resolution is not None:
            el.append(self.voxel_resolution.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ConvexDecomposition":
        _c_max_convex_hulls = el.find("max_convex_hulls")
        _max_convex_hulls = MaxConvexHulls.from_sdf(_c_max_convex_hulls, version) if _c_max_convex_hulls is not None else None
        _c_voxel_resolution = el.find("voxel_resolution")
        _voxel_resolution = VoxelResolution.from_sdf(_c_voxel_resolution, version) if _c_voxel_resolution is not None else None
        return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls, voxel_resolution=_voxel_resolution)


class Mesh(Model):
    def __init__(
        self,
        sdf_version: str,
        filename: str = "__default__",
        scale: Vector3 = None,
        optimization: str = "",
        uri: "Uri" = None,
        submesh: "Submesh" = None,
        convex_decomposition: "ConvexDecomposition" = None
    ):
        self.__version__ = sdf_version
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        self.filename = filename
        self.scale = scale
        self.optimization = optimization
        self.uri = uri
        self.submesh = submesh
        self.convex_decomposition = convex_decomposition

    def to_version(self, target_version: str) -> "Mesh":
        if self.optimization is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'optimization' is not supported in SDF version {target_version} (added in 1.12)")
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        if self.submesh is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'submesh' is not supported in SDF version {target_version} (added in 1.3)")
        if self.convex_decomposition is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["scale"] = self.scale
        kwargs["optimization"] = self.optimization
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["submesh"] = self.submesh.to_version(target_version) if self.submesh is not None else None
        kwargs["convex_decomposition"] = self.convex_decomposition.to_version(target_version) if self.convex_decomposition is not None else None
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
        if self.optimization is not None:
            el.set("optimization", self.optimization)
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.submesh is not None:
            el.append(self.submesh.to_sdf(version))
        if self.convex_decomposition is not None:
            el.append(self.convex_decomposition.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mesh":
        _filename = el.get("filename", "__default__")
        _scale = Vector3.from_sdf(el.get("scale", "1 1 1"))
        _optimization = el.get("optimization", "")
        if _optimization is not None and cmp_version(version, "1.12") < 0:
            if _optimization != "":
                raise ValueError(f"'optimization' is not supported in SDF version {version} (added in 1.12)")
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        _c_submesh = el.find("submesh")
        _submesh = Submesh.from_sdf(_c_submesh, version) if _c_submesh is not None else None
        if _submesh is not None and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'submesh' is not supported in SDF version {version} (added in 1.3)")
        _c_convex_decomposition = el.find("convex_decomposition")
        _convex_decomposition = ConvexDecomposition.from_sdf(_c_convex_decomposition, version) if _c_convex_decomposition is not None else None
        if _convex_decomposition is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, filename=_filename, scale=_scale, optimization=_optimization, uri=_uri, submesh=_submesh, convex_decomposition=_convex_decomposition)


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


class Diffuse(Model):
    def __init__(self, sdf_version: str, diffuse: str = "__default__"):
        self.__version__ = sdf_version
        self.diffuse = diffuse

    def to_version(self, target_version: str) -> "Diffuse":
        kwargs = {"sdf_version": target_version}
        kwargs["diffuse"] = self.diffuse
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Diffuse":
        _text = el.text or "__default__"
        _diffuse = _text
        return cls(sdf_version=version, diffuse=_diffuse)


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


class UseTerrainPaging(Model):
    def __init__(self, sdf_version: str, use_terrain_paging: bool = False):
        self.__version__ = sdf_version
        self.use_terrain_paging = use_terrain_paging

    def to_version(self, target_version: str) -> "UseTerrainPaging":
        if self.use_terrain_paging is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'use_terrain_paging' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["use_terrain_paging"] = self.use_terrain_paging
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("use_terrain_paging")
        if self.use_terrain_paging is not None:
            el.text = str(self.use_terrain_paging).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "UseTerrainPaging":
        _text = el.text or False
        _use_terrain_paging = _text.strip().lower() == 'true'
        if _use_terrain_paging is not None and cmp_version(version, "1.4") < 0:
            if _use_terrain_paging != False:
                raise ValueError(f"'use_terrain_paging' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, use_terrain_paging=_use_terrain_paging)


class Sampling(Model):
    def __init__(self, sdf_version: str, sampling: int = 2):
        self.__version__ = sdf_version
        self.sampling = sampling

    def to_version(self, target_version: str) -> "Sampling":
        if self.sampling is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["sampling"] = self.sampling
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sampling")
        if self.sampling is not None:
            el.text = str(self.sampling)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sampling":
        _text = el.text or 2
        _sampling = _parse_uint32(_text)
        if _sampling is not None and cmp_version(version, "1.7") < 0:
            if _sampling != 2:
                raise ValueError(f"'sampling' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, sampling=_sampling)


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
        pos: "Pos" = None,
        use_terrain_paging: "UseTerrainPaging" = None,
        sampling: "Sampling" = None
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
        self.use_terrain_paging = use_terrain_paging
        self.sampling = sampling

    def to_version(self, target_version: str) -> "Heightmap":
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        if self.pos is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pos' is not supported in SDF version {target_version} (added in 1.2)")
        if self.use_terrain_paging is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'use_terrain_paging' is not supported in SDF version {target_version} (added in 1.4)")
        if self.sampling is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["size"] = self.size
        kwargs["origin"] = self.origin
        kwargs["texture"] = [c.to_version(target_version) for c in (self.texture or [])]
        kwargs["blend"] = [c.to_version(target_version) for c in (self.blend or [])]
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["pos"] = self.pos.to_version(target_version) if self.pos is not None else None
        kwargs["use_terrain_paging"] = self.use_terrain_paging.to_version(target_version) if self.use_terrain_paging is not None else None
        kwargs["sampling"] = self.sampling.to_version(target_version) if self.sampling is not None else None
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
        if self.use_terrain_paging is not None:
            el.append(self.use_terrain_paging.to_sdf(version))
        if self.sampling is not None:
            el.append(self.sampling.to_sdf(version))
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
        _c_use_terrain_paging = el.find("use_terrain_paging")
        _use_terrain_paging = UseTerrainPaging.from_sdf(_c_use_terrain_paging, version) if _c_use_terrain_paging is not None else None
        if _use_terrain_paging is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'use_terrain_paging' is not supported in SDF version {version} (added in 1.4)")
        _c_sampling = el.find("sampling")
        _sampling = Sampling.from_sdf(_c_sampling, version) if _c_sampling is not None else None
        if _sampling is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, filename=_filename, size=_size, origin=_origin, texture=_texture, blend=_blend, uri=_uri, pos=_pos, use_terrain_paging=_use_terrain_paging, sampling=_sampling)


class Empty(Model):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "Empty":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("empty")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Empty":
        return cls(sdf_version=version)


class Point(Model):
    def __init__(self, sdf_version: str, point: Vector2d = None):
        self.__version__ = sdf_version
        if point is None:
            point = Vector2d.from_sdf("0 0")
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
        _text = el.text or "0 0"
        _point = Vector2d.from_sdf(_text)
        return cls(sdf_version=version, point=_point)


class Polyline(Model):
    def __init__(self, sdf_version: str, point: List["Point"] = None, height: "Height" = None):
        self.__version__ = sdf_version
        self.point = point or []
        self.height = height

    def to_version(self, target_version: str) -> "Polyline":
        kwargs = {"sdf_version": target_version}
        kwargs["point"] = [c.to_version(target_version) for c in (self.point or [])]
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("polyline")
        for item in (self.point or []):
            el.append(item.to_sdf(version))
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Polyline":
        _point = [Point.from_sdf(c, version) for c in el.findall("point")]
        _c_height = el.find("height")
        _height = Height.from_sdf(_c_height, version) if _c_height is not None else None
        return cls(sdf_version=version, point=_point, height=_height)


class Capsule(Model):
    def __init__(self, sdf_version: str, radius: "Radius" = None, length: "Length" = None):
        self.__version__ = sdf_version
        self.radius = radius
        self.length = length

    def to_version(self, target_version: str) -> "Capsule":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["length"] = self.length.to_version(target_version) if self.length is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("capsule")
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.length is not None:
            el.append(self.length.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Capsule":
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius, version) if _c_radius is not None else None
        _c_length = el.find("length")
        _length = Length.from_sdf(_c_length, version) if _c_length is not None else None
        return cls(sdf_version=version, radius=_radius, length=_length)


class Cone(Model):
    def __init__(self, sdf_version: str, radius: "Radius" = None, length: "Length" = None):
        self.__version__ = sdf_version
        self.radius = radius
        self.length = length

    def to_version(self, target_version: str) -> "Cone":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["length"] = self.length.to_version(target_version) if self.length is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cone")
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.length is not None:
            el.append(self.length.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cone":
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius, version) if _c_radius is not None else None
        _c_length = el.find("length")
        _length = Length.from_sdf(_c_length, version) if _c_length is not None else None
        return cls(sdf_version=version, radius=_radius, length=_length)


class Radii(Model):
    def __init__(self, sdf_version: str, radii: Vector3 = None):
        self.__version__ = sdf_version
        if radii is None:
            radii = Vector3.from_sdf("1 1 1")
        self.radii = radii

    def to_version(self, target_version: str) -> "Radii":
        kwargs = {"sdf_version": target_version}
        kwargs["radii"] = self.radii
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("radii")
        if self.radii is not None:
            el.text = self.radii.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Radii":
        _text = el.text or "1 1 1"
        _radii = Vector3.from_sdf(_text)
        return cls(sdf_version=version, radii=_radii)


class Ellipsoid(Model):
    def __init__(self, sdf_version: str, radii: "Radii" = None):
        self.__version__ = sdf_version
        self.radii = radii

    def to_version(self, target_version: str) -> "Ellipsoid":
        kwargs = {"sdf_version": target_version}
        kwargs["radii"] = self.radii.to_version(target_version) if self.radii is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ellipsoid")
        if self.radii is not None:
            el.append(self.radii.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ellipsoid":
        _c_radii = el.find("radii")
        _radii = Radii.from_sdf(_c_radii, version) if _c_radii is not None else None
        return cls(sdf_version=version, radii=_radii)


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
        heightmap: "Heightmap" = None,
        empty: "Empty" = None,
        polyline: "Polyline" = None,
        capsule: "Capsule" = None,
        cone: "Cone" = None,
        ellipsoid: "Ellipsoid" = None
    ):
        self.__version__ = sdf_version
        self.box = box
        self.sphere = sphere
        self.cylinder = cylinder
        self.mesh = mesh
        self.plane = plane
        self.image = image
        self.heightmap = heightmap
        self.empty = empty
        self.polyline = polyline
        self.capsule = capsule
        self.cone = cone
        self.ellipsoid = ellipsoid

    def to_version(self, target_version: str) -> "Geometry":
        if self.empty is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'empty' is not supported in SDF version {target_version} (added in 1.3)")
        if self.polyline is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'polyline' is not supported in SDF version {target_version} (added in 1.7)")
        if self.capsule is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'capsule' is not supported in SDF version {target_version} (added in 1.12)")
        if self.cone is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'cone' is not supported in SDF version {target_version} (added in 1.12)")
        if self.ellipsoid is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'ellipsoid' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["box"] = self.box.to_version(target_version) if self.box is not None else None
        kwargs["sphere"] = self.sphere.to_version(target_version) if self.sphere is not None else None
        kwargs["cylinder"] = self.cylinder.to_version(target_version) if self.cylinder is not None else None
        kwargs["mesh"] = self.mesh.to_version(target_version) if self.mesh is not None else None
        kwargs["plane"] = self.plane.to_version(target_version) if self.plane is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["heightmap"] = self.heightmap.to_version(target_version) if self.heightmap is not None else None
        kwargs["empty"] = self.empty.to_version(target_version) if self.empty is not None else None
        kwargs["polyline"] = self.polyline.to_version(target_version) if self.polyline is not None else None
        kwargs["capsule"] = self.capsule.to_version(target_version) if self.capsule is not None else None
        kwargs["cone"] = self.cone.to_version(target_version) if self.cone is not None else None
        kwargs["ellipsoid"] = self.ellipsoid.to_version(target_version) if self.ellipsoid is not None else None
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
        if self.empty is not None:
            el.append(self.empty.to_sdf(version))
        if self.polyline is not None:
            el.append(self.polyline.to_sdf(version))
        if self.capsule is not None:
            el.append(self.capsule.to_sdf(version))
        if self.cone is not None:
            el.append(self.cone.to_sdf(version))
        if self.ellipsoid is not None:
            el.append(self.ellipsoid.to_sdf(version))
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
        _c_empty = el.find("empty")
        _empty = Empty.from_sdf(_c_empty, version) if _c_empty is not None else None
        if _empty is not None and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'empty' is not supported in SDF version {version} (added in 1.3)")
        _c_polyline = el.find("polyline")
        _polyline = Polyline.from_sdf(_c_polyline, version) if _c_polyline is not None else None
        if _polyline is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'polyline' is not supported in SDF version {version} (added in 1.7)")
        _c_capsule = el.find("capsule")
        _capsule = Capsule.from_sdf(_c_capsule, version) if _c_capsule is not None else None
        if _capsule is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'capsule' is not supported in SDF version {version} (added in 1.12)")
        _c_cone = el.find("cone")
        _cone = Cone.from_sdf(_c_cone, version) if _c_cone is not None else None
        if _cone is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'cone' is not supported in SDF version {version} (added in 1.12)")
        _c_ellipsoid = el.find("ellipsoid")
        _ellipsoid = Ellipsoid.from_sdf(_c_ellipsoid, version) if _c_ellipsoid is not None else None
        if _ellipsoid is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'ellipsoid' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, box=_box, sphere=_sphere, cylinder=_cylinder, mesh=_mesh, plane=_plane, image=_image, heightmap=_heightmap, empty=_empty, polyline=_polyline, capsule=_capsule, cone=_cone, ellipsoid=_ellipsoid)


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


class Mu(Model):
    def __init__(self, sdf_version: str, mu: float = -1):
        self.__version__ = sdf_version
        self.mu = mu

    def to_version(self, target_version: str) -> "Mu":
        if self.mu is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'mu' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mu"] = self.mu
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mu")
        if self.mu is not None:
            el.text = str(self.mu)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mu":
        _text = el.text or -1
        _mu = _parse_double(_text)
        if _mu is not None and cmp_version(version, "1.2") < 0:
            if _mu != -1:
                raise ValueError(f"'mu' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mu=_mu)


class Mu2(Model):
    def __init__(self, sdf_version: str, mu2: float = -1):
        self.__version__ = sdf_version
        self.mu2 = mu2

    def to_version(self, target_version: str) -> "Mu2":
        if self.mu2 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'mu2' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mu2"] = self.mu2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mu2")
        if self.mu2 is not None:
            el.text = str(self.mu2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mu2":
        _text = el.text or -1
        _mu2 = _parse_double(_text)
        if _mu2 is not None and cmp_version(version, "1.2") < 0:
            if _mu2 != -1:
                raise ValueError(f"'mu2' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mu2=_mu2)


class Fdir1(Model):
    def __init__(self, sdf_version: str, fdir1: Vector3 = None):
        self.__version__ = sdf_version
        if fdir1 is None:
            fdir1 = Vector3.from_sdf("0 0 0")
        self.fdir1 = fdir1

    def to_version(self, target_version: str) -> "Fdir1":
        if self.fdir1 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'fdir1' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["fdir1"] = self.fdir1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fdir1")
        if self.fdir1 is not None:
            el.text = self.fdir1.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fdir1":
        _text = el.text or "0 0 0"
        _fdir1 = Vector3.from_sdf(_text)
        if _fdir1 is not None and cmp_version(version, "1.2") < 0:
            if _fdir1 != "0 0 0":
                raise ValueError(f"'fdir1' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, fdir1=_fdir1)


class Slip1(Model):
    def __init__(self, sdf_version: str, slip1: float = 0.0):
        self.__version__ = sdf_version
        self.slip1 = slip1

    def to_version(self, target_version: str) -> "Slip1":
        if self.slip1 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'slip1' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["slip1"] = self.slip1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("slip1")
        if self.slip1 is not None:
            el.text = str(self.slip1)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Slip1":
        _text = el.text or 0.0
        _slip1 = _parse_double(_text)
        if _slip1 is not None and cmp_version(version, "1.2") < 0:
            if _slip1 != 0.0:
                raise ValueError(f"'slip1' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, slip1=_slip1)


class Slip2(Model):
    def __init__(self, sdf_version: str, slip2: float = 0.0):
        self.__version__ = sdf_version
        self.slip2 = slip2

    def to_version(self, target_version: str) -> "Slip2":
        if self.slip2 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'slip2' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["slip2"] = self.slip2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("slip2")
        if self.slip2 is not None:
            el.text = str(self.slip2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Slip2":
        _text = el.text or 0.0
        _slip2 = _parse_double(_text)
        if _slip2 is not None and cmp_version(version, "1.2") < 0:
            if _slip2 != 0.0:
                raise ValueError(f"'slip2' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, slip2=_slip2)


class Ode(Model):
    def __init__(
        self,
        sdf_version: str,
        mu: float = -1,
        mu2: float = -1,
        fdir1: Vector3 = None,
        slip1: float = 0.0,
        slip2: float = 0.0
    ):
        self.__version__ = sdf_version
        if fdir1 is None:
            fdir1 = Vector3.from_sdf("0 0 0")
        self.mu = mu
        self.mu2 = mu2
        self.fdir1 = fdir1
        self.slip1 = slip1
        self.slip2 = slip2

    def to_version(self, target_version: str) -> "Ode":
        kwargs = {"sdf_version": target_version}
        kwargs["mu"] = self.mu
        kwargs["mu2"] = self.mu2
        kwargs["fdir1"] = self.fdir1
        kwargs["slip1"] = self.slip1
        kwargs["slip2"] = self.slip2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.mu is not None:
            el.set("mu", str(self.mu))
        if self.mu2 is not None:
            el.set("mu2", str(self.mu2))
        if self.fdir1 is not None:
            el.set("fdir1", self.fdir1.to_sdf())
        if self.slip1 is not None:
            el.set("slip1", str(self.slip1))
        if self.slip2 is not None:
            el.set("slip2", str(self.slip2))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ode":
        _mu = _parse_double(el.get("mu", -1))
        _mu2 = _parse_double(el.get("mu2", -1))
        _fdir1 = Vector3.from_sdf(el.get("fdir1", "0 0 0"))
        _slip1 = _parse_double(el.get("slip1", 0.0))
        _slip2 = _parse_double(el.get("slip2", 0.0))
        return cls(sdf_version=version, mu=_mu, mu2=_mu2, fdir1=_fdir1, slip1=_slip1, slip2=_slip2)


class Friction2(Model):
    def __init__(self, sdf_version: str, friction2: float = 1):
        self.__version__ = sdf_version
        self.friction2 = friction2

    def to_version(self, target_version: str) -> "Friction2":
        kwargs = {"sdf_version": target_version}
        kwargs["friction2"] = self.friction2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction2")
        if self.friction2 is not None:
            el.text = str(self.friction2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Friction2":
        _text = el.text or 1
        _friction2 = _parse_double(_text)
        return cls(sdf_version=version, friction2=_friction2)


class RollingFriction(Model):
    def __init__(self, sdf_version: str, rolling_friction: float = 1):
        self.__version__ = sdf_version
        self.rolling_friction = rolling_friction

    def to_version(self, target_version: str) -> "RollingFriction":
        kwargs = {"sdf_version": target_version}
        kwargs["rolling_friction"] = self.rolling_friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rolling_friction")
        if self.rolling_friction is not None:
            el.text = str(self.rolling_friction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "RollingFriction":
        _text = el.text or 1
        _rolling_friction = _parse_double(_text)
        return cls(sdf_version=version, rolling_friction=_rolling_friction)


class Bullet(Model):
    def __init__(
        self,
        sdf_version: str,
        friction: "Friction" = None,
        friction2: "Friction2" = None,
        fdir1: "Fdir1" = None,
        rolling_friction: "RollingFriction" = None
    ):
        self.__version__ = sdf_version
        self.friction = friction
        self.friction2 = friction2
        self.fdir1 = fdir1
        self.rolling_friction = rolling_friction

    def to_version(self, target_version: str) -> "Bullet":
        kwargs = {"sdf_version": target_version}
        kwargs["friction"] = self.friction.to_version(target_version) if self.friction is not None else None
        kwargs["friction2"] = self.friction2.to_version(target_version) if self.friction2 is not None else None
        kwargs["fdir1"] = self.fdir1.to_version(target_version) if self.fdir1 is not None else None
        kwargs["rolling_friction"] = self.rolling_friction.to_version(target_version) if self.rolling_friction is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bullet")
        if self.friction is not None:
            el.append(self.friction.to_sdf(version))
        if self.friction2 is not None:
            el.append(self.friction2.to_sdf(version))
        if self.fdir1 is not None:
            el.append(self.fdir1.to_sdf(version))
        if self.rolling_friction is not None:
            el.append(self.rolling_friction.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Bullet":
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction, version) if _c_friction is not None else None
        _c_friction2 = el.find("friction2")
        _friction2 = Friction2.from_sdf(_c_friction2, version) if _c_friction2 is not None else None
        _c_fdir1 = el.find("fdir1")
        _fdir1 = Fdir1.from_sdf(_c_fdir1, version) if _c_fdir1 is not None else None
        _c_rolling_friction = el.find("rolling_friction")
        _rolling_friction = RollingFriction.from_sdf(_c_rolling_friction, version) if _c_rolling_friction is not None else None
        return cls(sdf_version=version, friction=_friction, friction2=_friction2, fdir1=_fdir1, rolling_friction=_rolling_friction)


class Coefficient(Model):
    def __init__(self, sdf_version: str, coefficient: float = 1.0):
        self.__version__ = sdf_version
        self.coefficient = coefficient

    def to_version(self, target_version: str) -> "Coefficient":
        kwargs = {"sdf_version": target_version}
        kwargs["coefficient"] = self.coefficient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("coefficient")
        if self.coefficient is not None:
            el.text = str(self.coefficient)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Coefficient":
        _text = el.text or 1.0
        _coefficient = _parse_double(_text)
        return cls(sdf_version=version, coefficient=_coefficient)


class UsePatchRadius(Model):
    def __init__(self, sdf_version: str, use_patch_radius: bool = True):
        self.__version__ = sdf_version
        self.use_patch_radius = use_patch_radius

    def to_version(self, target_version: str) -> "UsePatchRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["use_patch_radius"] = self.use_patch_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("use_patch_radius")
        if self.use_patch_radius is not None:
            el.text = str(self.use_patch_radius).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "UsePatchRadius":
        _text = el.text or True
        _use_patch_radius = _text.strip().lower() == 'true'
        return cls(sdf_version=version, use_patch_radius=_use_patch_radius)


class PatchRadius(Model):
    def __init__(self, sdf_version: str, patch_radius: float = 0):
        self.__version__ = sdf_version
        self.patch_radius = patch_radius

    def to_version(self, target_version: str) -> "PatchRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["patch_radius"] = self.patch_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("patch_radius")
        if self.patch_radius is not None:
            el.text = str(self.patch_radius)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PatchRadius":
        _text = el.text or 0
        _patch_radius = _parse_double(_text)
        return cls(sdf_version=version, patch_radius=_patch_radius)


class SurfaceRadius(Model):
    def __init__(self, sdf_version: str, surface_radius: float = 0.0):
        self.__version__ = sdf_version
        self.surface_radius = surface_radius

    def to_version(self, target_version: str) -> "SurfaceRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["surface_radius"] = self.surface_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface_radius")
        if self.surface_radius is not None:
            el.text = str(self.surface_radius)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SurfaceRadius":
        _text = el.text or 0.0
        _surface_radius = _parse_double(_text)
        return cls(sdf_version=version, surface_radius=_surface_radius)


class Torsional(Model):
    def __init__(
        self,
        sdf_version: str,
        coefficient: "Coefficient" = None,
        use_patch_radius: "UsePatchRadius" = None,
        patch_radius: "PatchRadius" = None,
        surface_radius: "SurfaceRadius" = None,
        ode: "Ode" = None
    ):
        self.__version__ = sdf_version
        self.coefficient = coefficient
        self.use_patch_radius = use_patch_radius
        self.patch_radius = patch_radius
        self.surface_radius = surface_radius
        self.ode = ode

    def to_version(self, target_version: str) -> "Torsional":
        kwargs = {"sdf_version": target_version}
        kwargs["coefficient"] = self.coefficient.to_version(target_version) if self.coefficient is not None else None
        kwargs["use_patch_radius"] = self.use_patch_radius.to_version(target_version) if self.use_patch_radius is not None else None
        kwargs["patch_radius"] = self.patch_radius.to_version(target_version) if self.patch_radius is not None else None
        kwargs["surface_radius"] = self.surface_radius.to_version(target_version) if self.surface_radius is not None else None
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("torsional")
        if self.coefficient is not None:
            el.append(self.coefficient.to_sdf(version))
        if self.use_patch_radius is not None:
            el.append(self.use_patch_radius.to_sdf(version))
        if self.patch_radius is not None:
            el.append(self.patch_radius.to_sdf(version))
        if self.surface_radius is not None:
            el.append(self.surface_radius.to_sdf(version))
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Torsional":
        _c_coefficient = el.find("coefficient")
        _coefficient = Coefficient.from_sdf(_c_coefficient, version) if _c_coefficient is not None else None
        _c_use_patch_radius = el.find("use_patch_radius")
        _use_patch_radius = UsePatchRadius.from_sdf(_c_use_patch_radius, version) if _c_use_patch_radius is not None else None
        _c_patch_radius = el.find("patch_radius")
        _patch_radius = PatchRadius.from_sdf(_c_patch_radius, version) if _c_patch_radius is not None else None
        _c_surface_radius = el.find("surface_radius")
        _surface_radius = SurfaceRadius.from_sdf(_c_surface_radius, version) if _c_surface_radius is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        return cls(sdf_version=version, coefficient=_coefficient, use_patch_radius=_use_patch_radius, patch_radius=_patch_radius, surface_radius=_surface_radius, ode=_ode)


class Friction(Model):
    def __init__(
        self,
        sdf_version: str,
        ode: "Ode" = None,
        bullet: "Bullet" = None,
        torsional: "Torsional" = None
    ):
        self.__version__ = sdf_version
        self.ode = ode
        self.bullet = bullet
        self.torsional = torsional

    def to_version(self, target_version: str) -> "Friction":
        if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
        if self.torsional is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'torsional' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["torsional"] = self.torsional.to_version(target_version) if self.torsional is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.torsional is not None:
            el.append(self.torsional.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Friction":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet, version) if _c_bullet is not None else None
        if _bullet is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
        _c_torsional = el.find("torsional")
        _torsional = Torsional.from_sdf(_c_torsional, version) if _c_torsional is not None else None
        if _torsional is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'torsional' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, ode=_ode, bullet=_bullet, torsional=_torsional)


class CollideWithoutContact(Model):
    def __init__(self, sdf_version: str, collide_without_contact: bool = False):
        self.__version__ = sdf_version
        self.collide_without_contact = collide_without_contact

    def to_version(self, target_version: str) -> "CollideWithoutContact":
        if self.collide_without_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_without_contact"] = self.collide_without_contact
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_without_contact")
        if self.collide_without_contact is not None:
            el.text = str(self.collide_without_contact).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CollideWithoutContact":
        _text = el.text or False
        _collide_without_contact = _text.strip().lower() == 'true'
        if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
            if _collide_without_contact != False:
                raise ValueError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_without_contact=_collide_without_contact)


class CollideWithoutContactBitmask(Model):
    def __init__(self, sdf_version: str, collide_without_contact_bitmask: int = 1):
        self.__version__ = sdf_version
        self.collide_without_contact_bitmask = collide_without_contact_bitmask

    def to_version(self, target_version: str) -> "CollideWithoutContactBitmask":
        if self.collide_without_contact_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_without_contact_bitmask"] = self.collide_without_contact_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_without_contact_bitmask")
        if self.collide_without_contact_bitmask is not None:
            el.text = str(self.collide_without_contact_bitmask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CollideWithoutContactBitmask":
        _text = el.text or 1
        _collide_without_contact_bitmask = _parse_uint32(_text)
        if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
            if _collide_without_contact_bitmask != 1:
                raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_without_contact_bitmask=_collide_without_contact_bitmask)


class CollideBitmask(Model):
    def __init__(self, sdf_version: str, collide_bitmask: int = 1):
        self.__version__ = sdf_version
        self.collide_bitmask = collide_bitmask

    def to_version(self, target_version: str) -> "CollideBitmask":
        if self.collide_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_bitmask"] = self.collide_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_bitmask")
        if self.collide_bitmask is not None:
            el.text = str(self.collide_bitmask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CollideBitmask":
        _text = el.text or 1
        _collide_bitmask = _parse_uint32(_text)
        if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
            if _collide_bitmask != 1:
                raise ValueError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_bitmask=_collide_bitmask)


class CategoryBitmask(Model):
    def __init__(self, sdf_version: str, category_bitmask: int = 65535):
        self.__version__ = sdf_version
        self.category_bitmask = category_bitmask

    def to_version(self, target_version: str) -> "CategoryBitmask":
        if self.category_bitmask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["category_bitmask"] = self.category_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("category_bitmask")
        if self.category_bitmask is not None:
            el.text = str(self.category_bitmask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CategoryBitmask":
        _text = el.text or 65535
        _category_bitmask = _parse_uint32(_text)
        if _category_bitmask is not None and cmp_version(version, "1.7") < 0:
            if _category_bitmask != 65535:
                raise ValueError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, category_bitmask=_category_bitmask)


class PoissonsRatio(Model):
    def __init__(self, sdf_version: str, poissons_ratio: float = 0.3):
        self.__version__ = sdf_version
        self.poissons_ratio = poissons_ratio

    def to_version(self, target_version: str) -> "PoissonsRatio":
        if self.poissons_ratio is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["poissons_ratio"] = self.poissons_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("poissons_ratio")
        if self.poissons_ratio is not None:
            el.text = str(self.poissons_ratio)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PoissonsRatio":
        _text = el.text or 0.3
        _poissons_ratio = _parse_double(_text)
        if _poissons_ratio is not None and cmp_version(version, "1.7") < 0:
            if _poissons_ratio != 0.3:
                raise ValueError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, poissons_ratio=_poissons_ratio)


class ElasticModulus(Model):
    def __init__(self, sdf_version: str, elastic_modulus: float = -1):
        self.__version__ = sdf_version
        self.elastic_modulus = elastic_modulus

    def to_version(self, target_version: str) -> "ElasticModulus":
        if self.elastic_modulus is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["elastic_modulus"] = self.elastic_modulus
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("elastic_modulus")
        if self.elastic_modulus is not None:
            el.text = str(self.elastic_modulus)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ElasticModulus":
        _text = el.text or -1
        _elastic_modulus = _parse_double(_text)
        if _elastic_modulus is not None and cmp_version(version, "1.7") < 0:
            if _elastic_modulus != -1:
                raise ValueError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, elastic_modulus=_elastic_modulus)


class Contact(Model):
    def __init__(
        self,
        sdf_version: str,
        ode: "Ode" = None,
        collide_without_contact: "CollideWithoutContact" = None,
        collide_without_contact_bitmask: "CollideWithoutContactBitmask" = None,
        collide_bitmask: "CollideBitmask" = None,
        bullet: "Bullet" = None,
        category_bitmask: "CategoryBitmask" = None,
        poissons_ratio: "PoissonsRatio" = None,
        elastic_modulus: "ElasticModulus" = None
    ):
        self.__version__ = sdf_version
        self.ode = ode
        self.collide_without_contact = collide_without_contact
        self.collide_without_contact_bitmask = collide_without_contact_bitmask
        self.collide_bitmask = collide_bitmask
        self.bullet = bullet
        self.category_bitmask = category_bitmask
        self.poissons_ratio = poissons_ratio
        self.elastic_modulus = elastic_modulus

    def to_version(self, target_version: str) -> "Contact":
        if self.collide_without_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {target_version} (added in 1.4)")
        if self.collide_without_contact_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        if self.collide_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
        if self.category_bitmask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.7)")
        if self.poissons_ratio is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.7)")
        if self.elastic_modulus is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["collide_without_contact"] = self.collide_without_contact.to_version(target_version) if self.collide_without_contact is not None else None
        kwargs["collide_without_contact_bitmask"] = self.collide_without_contact_bitmask.to_version(target_version) if self.collide_without_contact_bitmask is not None else None
        kwargs["collide_bitmask"] = self.collide_bitmask.to_version(target_version) if self.collide_bitmask is not None else None
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["category_bitmask"] = self.category_bitmask.to_version(target_version) if self.category_bitmask is not None else None
        kwargs["poissons_ratio"] = self.poissons_ratio.to_version(target_version) if self.poissons_ratio is not None else None
        kwargs["elastic_modulus"] = self.elastic_modulus.to_version(target_version) if self.elastic_modulus is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.collide_without_contact is not None:
            el.append(self.collide_without_contact.to_sdf(version))
        if self.collide_without_contact_bitmask is not None:
            el.append(self.collide_without_contact_bitmask.to_sdf(version))
        if self.collide_bitmask is not None:
            el.append(self.collide_bitmask.to_sdf(version))
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.category_bitmask is not None:
            el.append(self.category_bitmask.to_sdf(version))
        if self.poissons_ratio is not None:
            el.append(self.poissons_ratio.to_sdf(version))
        if self.elastic_modulus is not None:
            el.append(self.elastic_modulus.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Contact":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        _c_collide_without_contact = el.find("collide_without_contact")
        _collide_without_contact = CollideWithoutContact.from_sdf(_c_collide_without_contact, version) if _c_collide_without_contact is not None else None
        if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
        _c_collide_without_contact_bitmask = el.find("collide_without_contact_bitmask")
        _collide_without_contact_bitmask = CollideWithoutContactBitmask.from_sdf(_c_collide_without_contact_bitmask, version) if _c_collide_without_contact_bitmask is not None else None
        if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
        _c_collide_bitmask = el.find("collide_bitmask")
        _collide_bitmask = CollideBitmask.from_sdf(_c_collide_bitmask, version) if _c_collide_bitmask is not None else None
        if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet, version) if _c_bullet is not None else None
        if _bullet is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
        _c_category_bitmask = el.find("category_bitmask")
        _category_bitmask = CategoryBitmask.from_sdf(_c_category_bitmask, version) if _c_category_bitmask is not None else None
        if _category_bitmask is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.7)")
        _c_poissons_ratio = el.find("poissons_ratio")
        _poissons_ratio = PoissonsRatio.from_sdf(_c_poissons_ratio, version) if _c_poissons_ratio is not None else None
        if _poissons_ratio is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.7)")
        _c_elastic_modulus = el.find("elastic_modulus")
        _elastic_modulus = ElasticModulus.from_sdf(_c_elastic_modulus, version) if _c_elastic_modulus is not None else None
        if _elastic_modulus is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, ode=_ode, collide_without_contact=_collide_without_contact, collide_without_contact_bitmask=_collide_without_contact_bitmask, collide_bitmask=_collide_bitmask, bullet=_bullet, category_bitmask=_category_bitmask, poissons_ratio=_poissons_ratio, elastic_modulus=_elastic_modulus)


class BoneAttachment(Model):
    def __init__(self, sdf_version: str, bone_attachment: float = 100.0):
        self.__version__ = sdf_version
        self.bone_attachment = bone_attachment

    def to_version(self, target_version: str) -> "BoneAttachment":
        kwargs = {"sdf_version": target_version}
        kwargs["bone_attachment"] = self.bone_attachment
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bone_attachment")
        if self.bone_attachment is not None:
            el.text = str(self.bone_attachment)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "BoneAttachment":
        _text = el.text or 100.0
        _bone_attachment = _parse_double(_text)
        return cls(sdf_version=version, bone_attachment=_bone_attachment)


class Stiffness(Model):
    def __init__(self, sdf_version: str, stiffness: float = 100.0):
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
        _text = el.text or 100.0
        _stiffness = _parse_double(_text)
        return cls(sdf_version=version, stiffness=_stiffness)


class Damping(Model):
    def __init__(self, sdf_version: str, damping: float = 10.0):
        self.__version__ = sdf_version
        self.damping = damping

    def to_version(self, target_version: str) -> "Damping":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Damping":
        _text = el.text or 10.0
        _damping = _parse_double(_text)
        return cls(sdf_version=version, damping=_damping)


class FleshMassFraction(Model):
    def __init__(self, sdf_version: str, flesh_mass_fraction: float = 0.05):
        self.__version__ = sdf_version
        self.flesh_mass_fraction = flesh_mass_fraction

    def to_version(self, target_version: str) -> "FleshMassFraction":
        kwargs = {"sdf_version": target_version}
        kwargs["flesh_mass_fraction"] = self.flesh_mass_fraction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("flesh_mass_fraction")
        if self.flesh_mass_fraction is not None:
            el.text = str(self.flesh_mass_fraction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "FleshMassFraction":
        _text = el.text or 0.05
        _flesh_mass_fraction = _parse_double(_text)
        return cls(sdf_version=version, flesh_mass_fraction=_flesh_mass_fraction)


class Dart(Model):
    def __init__(
        self,
        sdf_version: str,
        bone_attachment: "BoneAttachment" = None,
        stiffness: "Stiffness" = None,
        damping: "Damping" = None,
        flesh_mass_fraction: "FleshMassFraction" = None
    ):
        self.__version__ = sdf_version
        self.bone_attachment = bone_attachment
        self.stiffness = stiffness
        self.damping = damping
        self.flesh_mass_fraction = flesh_mass_fraction

    def to_version(self, target_version: str) -> "Dart":
        kwargs = {"sdf_version": target_version}
        kwargs["bone_attachment"] = self.bone_attachment.to_version(target_version) if self.bone_attachment is not None else None
        kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
        kwargs["damping"] = self.damping.to_version(target_version) if self.damping is not None else None
        kwargs["flesh_mass_fraction"] = self.flesh_mass_fraction.to_version(target_version) if self.flesh_mass_fraction is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dart")
        if self.bone_attachment is not None:
            el.append(self.bone_attachment.to_sdf(version))
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        if self.damping is not None:
            el.append(self.damping.to_sdf(version))
        if self.flesh_mass_fraction is not None:
            el.append(self.flesh_mass_fraction.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Dart":
        _c_bone_attachment = el.find("bone_attachment")
        _bone_attachment = BoneAttachment.from_sdf(_c_bone_attachment, version) if _c_bone_attachment is not None else None
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness, version) if _c_stiffness is not None else None
        _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping, version) if _c_damping is not None else None
        _c_flesh_mass_fraction = el.find("flesh_mass_fraction")
        _flesh_mass_fraction = FleshMassFraction.from_sdf(_c_flesh_mass_fraction, version) if _c_flesh_mass_fraction is not None else None
        return cls(sdf_version=version, bone_attachment=_bone_attachment, stiffness=_stiffness, damping=_damping, flesh_mass_fraction=_flesh_mass_fraction)


class SoftContact(Model):
    def __init__(self, sdf_version: str, dart: "Dart" = None):
        self.__version__ = sdf_version
        self.dart = dart

    def to_version(self, target_version: str) -> "SoftContact":
        kwargs = {"sdf_version": target_version}
        kwargs["dart"] = self.dart.to_version(target_version) if self.dart is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("soft_contact")
        if self.dart is not None:
            el.append(self.dart.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SoftContact":
        _c_dart = el.find("dart")
        _dart = Dart.from_sdf(_c_dart, version) if _c_dart is not None else None
        return cls(sdf_version=version, dart=_dart)


class Surface(Model):
    def __init__(
        self,
        sdf_version: str,
        bounce: "Bounce" = None,
        friction: "Friction" = None,
        contact: "Contact" = None,
        soft_contact: "SoftContact" = None
    ):
        self.__version__ = sdf_version
        self.bounce = bounce
        self.friction = friction
        self.contact = contact
        self.soft_contact = soft_contact

    def to_version(self, target_version: str) -> "Surface":
        if self.soft_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'soft_contact' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["bounce"] = self.bounce.to_version(target_version) if self.bounce is not None else None
        kwargs["friction"] = self.friction.to_version(target_version) if self.friction is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["soft_contact"] = self.soft_contact.to_version(target_version) if self.soft_contact is not None else None
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
        if self.soft_contact is not None:
            el.append(self.soft_contact.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Surface":
        _c_bounce = el.find("bounce")
        _bounce = Bounce.from_sdf(_c_bounce, version) if _c_bounce is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction, version) if _c_friction is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact, version) if _c_contact is not None else None
        _c_soft_contact = el.find("soft_contact")
        _soft_contact = SoftContact.from_sdf(_c_soft_contact, version) if _c_soft_contact is not None else None
        if _soft_contact is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'soft_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, bounce=_bounce, friction=_friction, contact=_contact, soft_contact=_soft_contact)


class MaxContacts(Model):
    def __init__(self, sdf_version: str, max_contacts: int = 10):
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
        _text = el.text or 10
        _max_contacts = _parse_int32(_text)
        return cls(sdf_version=version, max_contacts=_max_contacts)


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
        pose: "Pose" = None,
        density: "Density" = None,
        auto_inertia_params: "AutoInertiaParams" = None
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
        self.density = density
        self.auto_inertia_params = auto_inertia_params

    def to_version(self, target_version: str) -> "Collision":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.density is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.12)")
        if self.auto_inertia_params is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'auto_inertia_params' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["laser_retro"] = self.laser_retro
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["surface"] = self.surface.to_version(target_version) if self.surface is not None else None
        kwargs["max_contacts"] = self.max_contacts.to_version(target_version) if self.max_contacts is not None else None
        kwargs["mass"] = self.mass.to_version(target_version) if self.mass is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["density"] = self.density.to_version(target_version) if self.density is not None else None
        kwargs["auto_inertia_params"] = self.auto_inertia_params.to_version(target_version) if self.auto_inertia_params is not None else None
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
        if self.density is not None:
            el.append(self.density.to_sdf(version))
        if self.auto_inertia_params is not None:
            el.append(self.auto_inertia_params.to_sdf(version))
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
        _c_density = el.find("density")
        _density = Density.from_sdf(_c_density, version) if _c_density is not None else None
        if _density is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'density' is not supported in SDF version {version} (added in 1.12)")
        _c_auto_inertia_params = el.find("auto_inertia_params")
        _auto_inertia_params = AutoInertiaParams.from_sdf(_c_auto_inertia_params, version) if _c_auto_inertia_params is not None else None
        if _auto_inertia_params is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'auto_inertia_params' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, name=_name, laser_retro=_laser_retro, geometry=_geometry, surface=_surface, max_contacts=_max_contacts, mass=_mass, origin=_origin, pose=_pose, density=_density, auto_inertia_params=_auto_inertia_params)


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


class Ambient(Model):
    def __init__(self, sdf_version: str, ambient: Color = None, rgba: Color = None):
        self.__version__ = sdf_version
        if ambient is None:
            ambient = Color.from_sdf("0 0 0 1")
        if rgba is None:
            rgba = Color.from_sdf("0 0 0 1")
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
        _text = el.text or "0 0 0 1"
        _ambient = Color.from_sdf(_text)
        _rgba = Color.from_sdf(el.get("rgba", "0 0 0 1"))
        return cls(sdf_version=version, ambient=_ambient, rgba=_rgba)


class Specular(Model):
    def __init__(self, sdf_version: str, specular: Color = None, rgba: Color = None):
        self.__version__ = sdf_version
        if specular is None:
            specular = Color.from_sdf("0 0 0 1")
        if rgba is None:
            rgba = Color.from_sdf("0 0 0 1")
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
        _text = el.text or "0 0 0 1"
        _specular = Color.from_sdf(_text)
        _rgba = Color.from_sdf(el.get("rgba", "0 0 0 1"))
        return cls(sdf_version=version, specular=_specular, rgba=_rgba)


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


class Lighting(Model):
    def __init__(self, sdf_version: str, lighting: bool = True):
        self.__version__ = sdf_version
        self.lighting = lighting

    def to_version(self, target_version: str) -> "Lighting":
        if self.lighting is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'lighting' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["lighting"] = self.lighting
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lighting")
        if self.lighting is not None:
            el.text = str(self.lighting).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Lighting":
        _text = el.text or True
        _lighting = _text.strip().lower() == 'true'
        if _lighting is not None and cmp_version(version, "1.4") < 0:
            if _lighting != True:
                raise ValueError(f"'lighting' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, lighting=_lighting)


class RenderOrder(Model):
    def __init__(self, sdf_version: str, render_order: float = 0.0):
        self.__version__ = sdf_version
        self.render_order = render_order

    def to_version(self, target_version: str) -> "RenderOrder":
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["render_order"] = self.render_order
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("render_order")
        if self.render_order is not None:
            el.text = str(self.render_order)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "RenderOrder":
        _text = el.text or 0.0
        _render_order = _parse_double(_text)
        if _render_order is not None and cmp_version(version, "1.7") < 0:
            if _render_order != 0.0:
                raise ValueError(f"'render_order' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, render_order=_render_order)


class Shininess(Model):
    def __init__(self, sdf_version: str, shininess: float = 0):
        self.__version__ = sdf_version
        self.shininess = shininess

    def to_version(self, target_version: str) -> "Shininess":
        if self.shininess is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["shininess"] = self.shininess
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("shininess")
        if self.shininess is not None:
            el.text = str(self.shininess)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Shininess":
        _text = el.text or 0
        _shininess = _parse_double(_text)
        if _shininess is not None and cmp_version(version, "1.7") < 0:
            if _shininess != 0:
                raise ValueError(f"'shininess' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, shininess=_shininess)


class DoubleSided(Model):
    def __init__(self, sdf_version: str, double_sided: bool = False):
        self.__version__ = sdf_version
        self.double_sided = double_sided

    def to_version(self, target_version: str) -> "DoubleSided":
        if self.double_sided is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["double_sided"] = self.double_sided
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("double_sided")
        if self.double_sided is not None:
            el.text = str(self.double_sided).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "DoubleSided":
        _text = el.text or False
        _double_sided = _text.strip().lower() == 'true'
        if _double_sided is not None and cmp_version(version, "1.7") < 0:
            if _double_sided != False:
                raise ValueError(f"'double_sided' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, double_sided=_double_sided)


class AlbedoMap(Model):
    def __init__(self, sdf_version: str, albedo_map: str = ""):
        self.__version__ = sdf_version
        self.albedo_map = albedo_map

    def to_version(self, target_version: str) -> "AlbedoMap":
        kwargs = {"sdf_version": target_version}
        kwargs["albedo_map"] = self.albedo_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("albedo_map")
        if self.albedo_map is not None:
            el.text = self.albedo_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AlbedoMap":
        _text = el.text or ""
        _albedo_map = _text
        return cls(sdf_version=version, albedo_map=_albedo_map)


class RoughnessMap(Model):
    def __init__(self, sdf_version: str, roughness_map: str = ""):
        self.__version__ = sdf_version
        self.roughness_map = roughness_map

    def to_version(self, target_version: str) -> "RoughnessMap":
        kwargs = {"sdf_version": target_version}
        kwargs["roughness_map"] = self.roughness_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("roughness_map")
        if self.roughness_map is not None:
            el.text = self.roughness_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "RoughnessMap":
        _text = el.text or ""
        _roughness_map = _text
        return cls(sdf_version=version, roughness_map=_roughness_map)


class Roughness(Model):
    def __init__(self, sdf_version: str, roughness: str = "0.5"):
        self.__version__ = sdf_version
        self.roughness = roughness

    def to_version(self, target_version: str) -> "Roughness":
        kwargs = {"sdf_version": target_version}
        kwargs["roughness"] = self.roughness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("roughness")
        if self.roughness is not None:
            el.text = self.roughness
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Roughness":
        _text = el.text or "0.5"
        _roughness = _text
        return cls(sdf_version=version, roughness=_roughness)


class MetalnessMap(Model):
    def __init__(self, sdf_version: str, metalness_map: str = ""):
        self.__version__ = sdf_version
        self.metalness_map = metalness_map

    def to_version(self, target_version: str) -> "MetalnessMap":
        kwargs = {"sdf_version": target_version}
        kwargs["metalness_map"] = self.metalness_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("metalness_map")
        if self.metalness_map is not None:
            el.text = self.metalness_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MetalnessMap":
        _text = el.text or ""
        _metalness_map = _text
        return cls(sdf_version=version, metalness_map=_metalness_map)


class Metalness(Model):
    def __init__(self, sdf_version: str, metalness: str = "0.5"):
        self.__version__ = sdf_version
        self.metalness = metalness

    def to_version(self, target_version: str) -> "Metalness":
        kwargs = {"sdf_version": target_version}
        kwargs["metalness"] = self.metalness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("metalness")
        if self.metalness is not None:
            el.text = self.metalness
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Metalness":
        _text = el.text or "0.5"
        _metalness = _text
        return cls(sdf_version=version, metalness=_metalness)


class EnvironmentMap(Model):
    def __init__(self, sdf_version: str, environment_map: str = ""):
        self.__version__ = sdf_version
        self.environment_map = environment_map

    def to_version(self, target_version: str) -> "EnvironmentMap":
        kwargs = {"sdf_version": target_version}
        kwargs["environment_map"] = self.environment_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("environment_map")
        if self.environment_map is not None:
            el.text = self.environment_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EnvironmentMap":
        _text = el.text or ""
        _environment_map = _text
        return cls(sdf_version=version, environment_map=_environment_map)


class AmbientOcclusionMap(Model):
    def __init__(self, sdf_version: str, ambient_occlusion_map: str = ""):
        self.__version__ = sdf_version
        self.ambient_occlusion_map = ambient_occlusion_map

    def to_version(self, target_version: str) -> "AmbientOcclusionMap":
        kwargs = {"sdf_version": target_version}
        kwargs["ambient_occlusion_map"] = self.ambient_occlusion_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ambient_occlusion_map")
        if self.ambient_occlusion_map is not None:
            el.text = self.ambient_occlusion_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AmbientOcclusionMap":
        _text = el.text or ""
        _ambient_occlusion_map = _text
        return cls(sdf_version=version, ambient_occlusion_map=_ambient_occlusion_map)


class EmissiveMap(Model):
    def __init__(self, sdf_version: str, emissive_map: str = ""):
        self.__version__ = sdf_version
        self.emissive_map = emissive_map

    def to_version(self, target_version: str) -> "EmissiveMap":
        kwargs = {"sdf_version": target_version}
        kwargs["emissive_map"] = self.emissive_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("emissive_map")
        if self.emissive_map is not None:
            el.text = self.emissive_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EmissiveMap":
        _text = el.text or ""
        _emissive_map = _text
        return cls(sdf_version=version, emissive_map=_emissive_map)


class LightMap(Model):
    def __init__(self, sdf_version: str, light_map: str = "", uv_set: int = 0):
        self.__version__ = sdf_version
        self.light_map = light_map
        self.uv_set = uv_set

    def to_version(self, target_version: str) -> "LightMap":
        kwargs = {"sdf_version": target_version}
        kwargs["light_map"] = self.light_map
        kwargs["uv_set"] = self.uv_set
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light_map")
        if self.light_map is not None:
            el.text = self.light_map
        if self.uv_set is not None:
            el.set("uv_set", str(self.uv_set))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LightMap":
        _text = el.text or ""
        _light_map = _text
        _uv_set = _parse_uint32(el.get("uv_set", 0))
        return cls(sdf_version=version, light_map=_light_map, uv_set=_uv_set)


class Metal(Model):
    def __init__(
        self,
        sdf_version: str,
        albedo_map: "AlbedoMap" = None,
        roughness_map: "RoughnessMap" = None,
        roughness: "Roughness" = None,
        metalness_map: "MetalnessMap" = None,
        metalness: "Metalness" = None,
        environment_map: "EnvironmentMap" = None,
        ambient_occlusion_map: "AmbientOcclusionMap" = None,
        normal_map: "NormalMap" = None,
        emissive_map: "EmissiveMap" = None,
        light_map: "LightMap" = None
    ):
        self.__version__ = sdf_version
        self.albedo_map = albedo_map
        self.roughness_map = roughness_map
        self.roughness = roughness
        self.metalness_map = metalness_map
        self.metalness = metalness
        self.environment_map = environment_map
        self.ambient_occlusion_map = ambient_occlusion_map
        self.normal_map = normal_map
        self.emissive_map = emissive_map
        self.light_map = light_map

    def to_version(self, target_version: str) -> "Metal":
        kwargs = {"sdf_version": target_version}
        kwargs["albedo_map"] = self.albedo_map.to_version(target_version) if self.albedo_map is not None else None
        kwargs["roughness_map"] = self.roughness_map.to_version(target_version) if self.roughness_map is not None else None
        kwargs["roughness"] = self.roughness.to_version(target_version) if self.roughness is not None else None
        kwargs["metalness_map"] = self.metalness_map.to_version(target_version) if self.metalness_map is not None else None
        kwargs["metalness"] = self.metalness.to_version(target_version) if self.metalness is not None else None
        kwargs["environment_map"] = self.environment_map.to_version(target_version) if self.environment_map is not None else None
        kwargs["ambient_occlusion_map"] = self.ambient_occlusion_map.to_version(target_version) if self.ambient_occlusion_map is not None else None
        kwargs["normal_map"] = self.normal_map.to_version(target_version) if self.normal_map is not None else None
        kwargs["emissive_map"] = self.emissive_map.to_version(target_version) if self.emissive_map is not None else None
        kwargs["light_map"] = self.light_map.to_version(target_version) if self.light_map is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("metal")
        if self.albedo_map is not None:
            el.append(self.albedo_map.to_sdf(version))
        if self.roughness_map is not None:
            el.append(self.roughness_map.to_sdf(version))
        if self.roughness is not None:
            el.append(self.roughness.to_sdf(version))
        if self.metalness_map is not None:
            el.append(self.metalness_map.to_sdf(version))
        if self.metalness is not None:
            el.append(self.metalness.to_sdf(version))
        if self.environment_map is not None:
            el.append(self.environment_map.to_sdf(version))
        if self.ambient_occlusion_map is not None:
            el.append(self.ambient_occlusion_map.to_sdf(version))
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf(version))
        if self.emissive_map is not None:
            el.append(self.emissive_map.to_sdf(version))
        if self.light_map is not None:
            el.append(self.light_map.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Metal":
        _c_albedo_map = el.find("albedo_map")
        _albedo_map = AlbedoMap.from_sdf(_c_albedo_map, version) if _c_albedo_map is not None else None
        _c_roughness_map = el.find("roughness_map")
        _roughness_map = RoughnessMap.from_sdf(_c_roughness_map, version) if _c_roughness_map is not None else None
        _c_roughness = el.find("roughness")
        _roughness = Roughness.from_sdf(_c_roughness, version) if _c_roughness is not None else None
        _c_metalness_map = el.find("metalness_map")
        _metalness_map = MetalnessMap.from_sdf(_c_metalness_map, version) if _c_metalness_map is not None else None
        _c_metalness = el.find("metalness")
        _metalness = Metalness.from_sdf(_c_metalness, version) if _c_metalness is not None else None
        _c_environment_map = el.find("environment_map")
        _environment_map = EnvironmentMap.from_sdf(_c_environment_map, version) if _c_environment_map is not None else None
        _c_ambient_occlusion_map = el.find("ambient_occlusion_map")
        _ambient_occlusion_map = AmbientOcclusionMap.from_sdf(_c_ambient_occlusion_map, version) if _c_ambient_occlusion_map is not None else None
        _c_normal_map = el.find("normal_map")
        _normal_map = NormalMap.from_sdf(_c_normal_map, version) if _c_normal_map is not None else None
        _c_emissive_map = el.find("emissive_map")
        _emissive_map = EmissiveMap.from_sdf(_c_emissive_map, version) if _c_emissive_map is not None else None
        _c_light_map = el.find("light_map")
        _light_map = LightMap.from_sdf(_c_light_map, version) if _c_light_map is not None else None
        return cls(sdf_version=version, albedo_map=_albedo_map, roughness_map=_roughness_map, roughness=_roughness, metalness_map=_metalness_map, metalness=_metalness, environment_map=_environment_map, ambient_occlusion_map=_ambient_occlusion_map, normal_map=_normal_map, emissive_map=_emissive_map, light_map=_light_map)


class Pbr(Model):
    def __init__(self, sdf_version: str, metal: "Metal" = None, specular: "Specular" = None):
        self.__version__ = sdf_version
        self.metal = metal
        self.specular = specular

    def to_version(self, target_version: str) -> "Pbr":
        kwargs = {"sdf_version": target_version}
        kwargs["metal"] = self.metal.to_version(target_version) if self.metal is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pbr")
        if self.metal is not None:
            el.append(self.metal.to_sdf(version))
        if self.specular is not None:
            el.append(self.specular.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pbr":
        _c_metal = el.find("metal")
        _metal = Metal.from_sdf(_c_metal, version) if _c_metal is not None else None
        _c_specular = el.find("specular")
        _specular = Specular.from_sdf(_c_specular, version) if _c_specular is not None else None
        return cls(sdf_version=version, metal=_metal, specular=_specular)


class Material(Model):
    def __init__(
        self,
        sdf_version: str,
        script: str = "__default__",
        shader: "Shader" = None,
        ambient: "Ambient" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        emissive: "Emissive" = None,
        lighting: "Lighting" = None,
        render_order: "RenderOrder" = None,
        shininess: "Shininess" = None,
        double_sided: "DoubleSided" = None,
        pbr: "Pbr" = None
    ):
        self.__version__ = sdf_version
        self.script = script
        self.shader = shader
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.emissive = emissive
        self.lighting = lighting
        self.render_order = render_order
        self.shininess = shininess
        self.double_sided = double_sided
        self.pbr = pbr

    def to_version(self, target_version: str) -> "Material":
        if self.lighting is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'lighting' is not supported in SDF version {target_version} (added in 1.4)")
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        if self.shininess is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {target_version} (added in 1.7)")
        if self.double_sided is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {target_version} (added in 1.7)")
        if self.pbr is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'pbr' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["script"] = self.script
        kwargs["shader"] = self.shader.to_version(target_version) if self.shader is not None else None
        kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["emissive"] = self.emissive.to_version(target_version) if self.emissive is not None else None
        kwargs["lighting"] = self.lighting.to_version(target_version) if self.lighting is not None else None
        kwargs["render_order"] = self.render_order.to_version(target_version) if self.render_order is not None else None
        kwargs["shininess"] = self.shininess.to_version(target_version) if self.shininess is not None else None
        kwargs["double_sided"] = self.double_sided.to_version(target_version) if self.double_sided is not None else None
        kwargs["pbr"] = self.pbr.to_version(target_version) if self.pbr is not None else None
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
        if self.lighting is not None:
            el.append(self.lighting.to_sdf(version))
        if self.render_order is not None:
            el.append(self.render_order.to_sdf(version))
        if self.shininess is not None:
            el.append(self.shininess.to_sdf(version))
        if self.double_sided is not None:
            el.append(self.double_sided.to_sdf(version))
        if self.pbr is not None:
            el.append(self.pbr.to_sdf(version))
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
        _c_lighting = el.find("lighting")
        _lighting = Lighting.from_sdf(_c_lighting, version) if _c_lighting is not None else None
        if _lighting is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'lighting' is not supported in SDF version {version} (added in 1.4)")
        _c_render_order = el.find("render_order")
        _render_order = RenderOrder.from_sdf(_c_render_order, version) if _c_render_order is not None else None
        if _render_order is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {version} (added in 1.7)")
        _c_shininess = el.find("shininess")
        _shininess = Shininess.from_sdf(_c_shininess, version) if _c_shininess is not None else None
        if _shininess is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {version} (added in 1.7)")
        _c_double_sided = el.find("double_sided")
        _double_sided = DoubleSided.from_sdf(_c_double_sided, version) if _c_double_sided is not None else None
        if _double_sided is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {version} (added in 1.7)")
        _c_pbr = el.find("pbr")
        _pbr = Pbr.from_sdf(_c_pbr, version) if _c_pbr is not None else None
        if _pbr is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'pbr' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, script=_script, shader=_shader, ambient=_ambient, diffuse=_diffuse, specular=_specular, emissive=_emissive, lighting=_lighting, render_order=_render_order, shininess=_shininess, double_sided=_double_sided, pbr=_pbr)


class CastShadows(Model):
    def __init__(self, sdf_version: str, cast_shadows: bool = True):
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
        _text = el.text or True
        _cast_shadows = _text.strip().lower() == 'true'
        if _cast_shadows is not None and cmp_version(version, "1.2") < 0:
            if _cast_shadows != True:
                raise ValueError(f"'cast_shadows' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, cast_shadows=_cast_shadows)


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


class VisibilityFlags(Model):
    def __init__(self, sdf_version: str, visibility_flags: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "VisibilityFlags":
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_flags"] = self.visibility_flags
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visibility_flags")
        if self.visibility_flags is not None:
            el.text = str(self.visibility_flags)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VisibilityFlags":
        _text = el.text or 4294967295
        _visibility_flags = _parse_uint32(_text)
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            if _visibility_flags != 4294967295:
                raise ValueError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_flags=_visibility_flags)


class Layer(Model):
    def __init__(self, sdf_version: str, layer: int = 0):
        self.__version__ = sdf_version
        self.layer = layer

    def to_version(self, target_version: str) -> "Layer":
        kwargs = {"sdf_version": target_version}
        kwargs["layer"] = self.layer
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("layer")
        if self.layer is not None:
            el.text = str(self.layer)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Layer":
        _text = el.text or 0
        _layer = _parse_int32(_text)
        return cls(sdf_version=version, layer=_layer)


class Meta(Model):
    def __init__(self, sdf_version: str, layer: "Layer" = None):
        self.__version__ = sdf_version
        self.layer = layer

    def to_version(self, target_version: str) -> "Meta":
        kwargs = {"sdf_version": target_version}
        kwargs["layer"] = self.layer.to_version(target_version) if self.layer is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("meta")
        if self.layer is not None:
            el.append(self.layer.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Meta":
        _c_layer = el.find("layer")
        _layer = Layer.from_sdf(_c_layer, version) if _c_layer is not None else None
        return cls(sdf_version=version, layer=_layer)


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
        pose: "Pose" = None,
        plugin: List["Plugin"] = None,
        visibility_flags: "VisibilityFlags" = None,
        meta: "Meta" = None
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
        self.plugin = plugin or []
        self.visibility_flags = visibility_flags
        self.meta = meta

    def to_version(self, target_version: str) -> "Visual":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.plugin is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {target_version} (added in 1.3)")
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        if self.meta is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'meta' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["cast_shadows"] = self.cast_shadows
        kwargs["laser_retro"] = self.laser_retro
        kwargs["transparency"] = self.transparency
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["visibility_flags"] = self.visibility_flags.to_version(target_version) if self.visibility_flags is not None else None
        kwargs["meta"] = self.meta.to_version(target_version) if self.meta is not None else None
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
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.visibility_flags is not None:
            el.append(self.visibility_flags.to_sdf(version))
        if self.meta is not None:
            el.append(self.meta.to_sdf(version))
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
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        if _plugin and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {version} (added in 1.3)")
        _c_visibility_flags = el.find("visibility_flags")
        _visibility_flags = VisibilityFlags.from_sdf(_c_visibility_flags, version) if _c_visibility_flags is not None else None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        _c_meta = el.find("meta")
        _meta = Meta.from_sdf(_c_meta, version) if _c_meta is not None else None
        if _meta is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'meta' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, name=_name, cast_shadows=_cast_shadows, laser_retro=_laser_retro, transparency=_transparency, geometry=_geometry, origin=_origin, material=_material, pose=_pose, plugin=_plugin, visibility_flags=_visibility_flags, meta=_meta)


class HorizontalFov(Model):
    def __init__(self, sdf_version: str, horizontal_fov: float = 1.047, angle: float = 1.047):
        self.__version__ = sdf_version
        self.horizontal_fov = horizontal_fov
        self.angle = angle

    def to_version(self, target_version: str) -> "HorizontalFov":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal_fov"] = self.horizontal_fov
        kwargs["angle"] = self.angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal_fov")
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        if self.angle is not None:
            el.set("angle", str(self.angle))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "HorizontalFov":
        _text = el.text or 1.047
        _horizontal_fov = _parse_double(_text)
        _angle = _parse_double(el.get("angle", 1.047))
        return cls(sdf_version=version, horizontal_fov=_horizontal_fov, angle=_angle)


class Near(Model):
    def __init__(self, sdf_version: str, near: float = .1):
        self.__version__ = sdf_version
        self.near = near

    def to_version(self, target_version: str) -> "Near":
        if self.near is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'near' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("near")
        if self.near is not None:
            el.text = str(self.near)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Near":
        _text = el.text or .1
        _near = _parse_double(_text)
        if _near is not None and cmp_version(version, "1.2") < 0:
            if _near != .1:
                raise ValueError(f"'near' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, near=_near)


class Far(Model):
    def __init__(self, sdf_version: str, far: float = 100):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "Far":
        if self.far is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'far' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("far")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Far":
        _text = el.text or 100
        _far = _parse_double(_text)
        if _far is not None and cmp_version(version, "1.2") < 0:
            if _far != 100:
                raise ValueError(f"'far' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, far=_far)


class Clip(Model):
    def __init__(self, sdf_version: str, near: float = .1, far: float = 100):
        self.__version__ = sdf_version
        self.near = near
        self.far = far

    def to_version(self, target_version: str) -> "Clip":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("clip")
        if self.near is not None:
            el.set("near", str(self.near))
        if self.far is not None:
            el.set("far", str(self.far))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Clip":
        _near = _parse_double(el.get("near", .1))
        _far = _parse_double(el.get("far", 100))
        return cls(sdf_version=version, near=_near, far=_far)


class Path(Model):
    def __init__(self, sdf_version: str, path: str = "__default__"):
        self.__version__ = sdf_version
        self.path = path

    def to_version(self, target_version: str) -> "Path":
        if self.path is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'path' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["path"] = self.path
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("path")
        if self.path is not None:
            el.text = self.path
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Path":
        _text = el.text or "__default__"
        _path = _text
        if _path is not None and cmp_version(version, "1.2") < 0:
            if _path != "__default__":
                raise ValueError(f"'path' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, path=_path)


class Save(Model):
    def __init__(self, sdf_version: str, enabled: bool = False, path: str = "__default__"):
        self.__version__ = sdf_version
        self.enabled = enabled
        self.path = path

    def to_version(self, target_version: str) -> "Save":
        kwargs = {"sdf_version": target_version}
        kwargs["enabled"] = self.enabled
        kwargs["path"] = self.path
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("save")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        if self.path is not None:
            el.set("path", self.path)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Save":
        _enabled = el.get("enabled", False).strip().lower() == 'true'
        _path = el.get("path", "__default__")
        return cls(sdf_version=version, enabled=_enabled, path=_path)


class Output(Model):
    def __init__(self, sdf_version: str, output: str = "depths"):
        self.__version__ = sdf_version
        self.output = output

    def to_version(self, target_version: str) -> "Output":
        if self.output is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'output' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["output"] = self.output
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("output")
        if self.output is not None:
            el.text = self.output
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Output":
        _text = el.text or "depths"
        _output = _text
        if _output is not None and cmp_version(version, "1.2") < 0:
            if _output != "depths":
                raise ValueError(f"'output' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, output=_output)


class DepthCamera(Model):
    def __init__(self, sdf_version: str, output: str = "depths", clip: "Clip" = None):
        self.__version__ = sdf_version
        self.output = output
        self.clip = clip

    def to_version(self, target_version: str) -> "DepthCamera":
        if self.clip is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'clip' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["output"] = self.output
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("depth_camera")
        if self.output is not None:
            el.set("output", self.output)
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "DepthCamera":
        _output = el.get("output", "depths")
        _c_clip = el.find("clip")
        _clip = Clip.from_sdf(_c_clip, version) if _c_clip is not None else None
        if _clip is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'clip' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, output=_output, clip=_clip)


class Type(Model):
    def __init__(self, sdf_version: str, type: str = "gaussian"):
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
        _text = el.text or "gaussian"
        _type = _text
        return cls(sdf_version=version, type=_type)


class Mean(Model):
    def __init__(self, sdf_version: str, mean: float = 0.0):
        self.__version__ = sdf_version
        self.mean = mean

    def to_version(self, target_version: str) -> "Mean":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mean")
        if self.mean is not None:
            el.text = str(self.mean)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mean":
        _text = el.text or 0.0
        _mean = _parse_double(_text)
        return cls(sdf_version=version, mean=_mean)


class Stddev(Model):
    def __init__(self, sdf_version: str, stddev: float = 0.0):
        self.__version__ = sdf_version
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Stddev":
        kwargs = {"sdf_version": target_version}
        kwargs["stddev"] = self.stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("stddev")
        if self.stddev is not None:
            el.text = str(self.stddev)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Stddev":
        _text = el.text or 0.0
        _stddev = _parse_double(_text)
        return cls(sdf_version=version, stddev=_stddev)


class Noise(Model):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        mean: "Mean" = None,
        stddev: "Stddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Noise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Noise":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type, version) if _c_type is not None else None
        _c_mean = el.find("mean")
        _mean = Mean.from_sdf(_c_mean, version) if _c_mean is not None else None
        _c_stddev = el.find("stddev")
        _stddev = Stddev.from_sdf(_c_stddev, version) if _c_stddev is not None else None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev)


class CameraInfoTopic(Model):
    def __init__(self, sdf_version: str, camera_info_topic: str = "__default__"):
        self.__version__ = sdf_version
        self.camera_info_topic = camera_info_topic

    def to_version(self, target_version: str) -> "CameraInfoTopic":
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["camera_info_topic"] = self.camera_info_topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera_info_topic")
        if self.camera_info_topic is not None:
            el.text = self.camera_info_topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CameraInfoTopic":
        _text = el.text or "__default__"
        _camera_info_topic = _text
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            if _camera_info_topic != "__default__":
                raise ValueError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, camera_info_topic=_camera_info_topic)


class K1(Model):
    def __init__(self, sdf_version: str, k1: float = 0.0):
        self.__version__ = sdf_version
        self.k1 = k1

    def to_version(self, target_version: str) -> "K1":
        kwargs = {"sdf_version": target_version}
        kwargs["k1"] = self.k1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k1")
        if self.k1 is not None:
            el.text = str(self.k1)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "K1":
        _text = el.text or 0.0
        _k1 = _parse_double(_text)
        return cls(sdf_version=version, k1=_k1)


class K2(Model):
    def __init__(self, sdf_version: str, k2: float = 0.0):
        self.__version__ = sdf_version
        self.k2 = k2

    def to_version(self, target_version: str) -> "K2":
        kwargs = {"sdf_version": target_version}
        kwargs["k2"] = self.k2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k2")
        if self.k2 is not None:
            el.text = str(self.k2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "K2":
        _text = el.text or 0.0
        _k2 = _parse_double(_text)
        return cls(sdf_version=version, k2=_k2)


class K3(Model):
    def __init__(self, sdf_version: str, k3: float = 0.0):
        self.__version__ = sdf_version
        self.k3 = k3

    def to_version(self, target_version: str) -> "K3":
        kwargs = {"sdf_version": target_version}
        kwargs["k3"] = self.k3
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k3")
        if self.k3 is not None:
            el.text = str(self.k3)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "K3":
        _text = el.text or 0.0
        _k3 = _parse_double(_text)
        return cls(sdf_version=version, k3=_k3)


class P1(Model):
    def __init__(self, sdf_version: str, p1: float = 0.0):
        self.__version__ = sdf_version
        self.p1 = p1

    def to_version(self, target_version: str) -> "P1":
        kwargs = {"sdf_version": target_version}
        kwargs["p1"] = self.p1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p1")
        if self.p1 is not None:
            el.text = str(self.p1)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "P1":
        _text = el.text or 0.0
        _p1 = _parse_double(_text)
        return cls(sdf_version=version, p1=_p1)


class P2(Model):
    def __init__(self, sdf_version: str, p2: float = 0.0):
        self.__version__ = sdf_version
        self.p2 = p2

    def to_version(self, target_version: str) -> "P2":
        kwargs = {"sdf_version": target_version}
        kwargs["p2"] = self.p2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p2")
        if self.p2 is not None:
            el.text = str(self.p2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "P2":
        _text = el.text or 0.0
        _p2 = _parse_double(_text)
        return cls(sdf_version=version, p2=_p2)


class Distortion(Model):
    def __init__(
        self,
        sdf_version: str,
        k1: "K1" = None,
        k2: "K2" = None,
        k3: "K3" = None,
        p1: "P1" = None,
        p2: "P2" = None,
        center: "Center" = None
    ):
        self.__version__ = sdf_version
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.p1 = p1
        self.p2 = p2
        self.center = center

    def to_version(self, target_version: str) -> "Distortion":
        kwargs = {"sdf_version": target_version}
        kwargs["k1"] = self.k1.to_version(target_version) if self.k1 is not None else None
        kwargs["k2"] = self.k2.to_version(target_version) if self.k2 is not None else None
        kwargs["k3"] = self.k3.to_version(target_version) if self.k3 is not None else None
        kwargs["p1"] = self.p1.to_version(target_version) if self.p1 is not None else None
        kwargs["p2"] = self.p2.to_version(target_version) if self.p2 is not None else None
        kwargs["center"] = self.center.to_version(target_version) if self.center is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("distortion")
        if self.k1 is not None:
            el.append(self.k1.to_sdf(version))
        if self.k2 is not None:
            el.append(self.k2.to_sdf(version))
        if self.k3 is not None:
            el.append(self.k3.to_sdf(version))
        if self.p1 is not None:
            el.append(self.p1.to_sdf(version))
        if self.p2 is not None:
            el.append(self.p2.to_sdf(version))
        if self.center is not None:
            el.append(self.center.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Distortion":
        _c_k1 = el.find("k1")
        _k1 = K1.from_sdf(_c_k1, version) if _c_k1 is not None else None
        _c_k2 = el.find("k2")
        _k2 = K2.from_sdf(_c_k2, version) if _c_k2 is not None else None
        _c_k3 = el.find("k3")
        _k3 = K3.from_sdf(_c_k3, version) if _c_k3 is not None else None
        _c_p1 = el.find("p1")
        _p1 = P1.from_sdf(_c_p1, version) if _c_p1 is not None else None
        _c_p2 = el.find("p2")
        _p2 = P2.from_sdf(_c_p2, version) if _c_p2 is not None else None
        _c_center = el.find("center")
        _center = Center.from_sdf(_c_center, version) if _c_center is not None else None
        return cls(sdf_version=version, k1=_k1, k2=_k2, k3=_k3, p1=_p1, p2=_p2, center=_center)


class ScaleToHfov(Model):
    def __init__(self, sdf_version: str, scale_to_hfov: bool = True):
        self.__version__ = sdf_version
        self.scale_to_hfov = scale_to_hfov

    def to_version(self, target_version: str) -> "ScaleToHfov":
        kwargs = {"sdf_version": target_version}
        kwargs["scale_to_hfov"] = self.scale_to_hfov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale_to_hfov")
        if self.scale_to_hfov is not None:
            el.text = str(self.scale_to_hfov).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ScaleToHfov":
        _text = el.text or True
        _scale_to_hfov = _text.strip().lower() == 'true'
        return cls(sdf_version=version, scale_to_hfov=_scale_to_hfov)


class C1(Model):
    def __init__(self, sdf_version: str, c1: float = 1):
        self.__version__ = sdf_version
        self.c1 = c1

    def to_version(self, target_version: str) -> "C1":
        kwargs = {"sdf_version": target_version}
        kwargs["c1"] = self.c1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c1")
        if self.c1 is not None:
            el.text = str(self.c1)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "C1":
        _text = el.text or 1
        _c1 = _parse_double(_text)
        return cls(sdf_version=version, c1=_c1)


class C2(Model):
    def __init__(self, sdf_version: str, c2: float = 1):
        self.__version__ = sdf_version
        self.c2 = c2

    def to_version(self, target_version: str) -> "C2":
        kwargs = {"sdf_version": target_version}
        kwargs["c2"] = self.c2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c2")
        if self.c2 is not None:
            el.text = str(self.c2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "C2":
        _text = el.text or 1
        _c2 = _parse_double(_text)
        return cls(sdf_version=version, c2=_c2)


class C3(Model):
    def __init__(self, sdf_version: str, c3: float = 0):
        self.__version__ = sdf_version
        self.c3 = c3

    def to_version(self, target_version: str) -> "C3":
        kwargs = {"sdf_version": target_version}
        kwargs["c3"] = self.c3
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c3")
        if self.c3 is not None:
            el.text = str(self.c3)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "C3":
        _text = el.text or 0
        _c3 = _parse_double(_text)
        return cls(sdf_version=version, c3=_c3)


class F(Model):
    def __init__(self, sdf_version: str, f: float = 1):
        self.__version__ = sdf_version
        self.f = f

    def to_version(self, target_version: str) -> "F":
        kwargs = {"sdf_version": target_version}
        kwargs["f"] = self.f
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("f")
        if self.f is not None:
            el.text = str(self.f)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "F":
        _text = el.text or 1
        _f = _parse_double(_text)
        return cls(sdf_version=version, f=_f)


class Fun(Model):
    def __init__(self, sdf_version: str, fun: str = "tan"):
        self.__version__ = sdf_version
        self.fun = fun

    def to_version(self, target_version: str) -> "Fun":
        kwargs = {"sdf_version": target_version}
        kwargs["fun"] = self.fun
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fun")
        if self.fun is not None:
            el.text = self.fun
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fun":
        _text = el.text or "tan"
        _fun = _text
        return cls(sdf_version=version, fun=_fun)


class CustomFunction(Model):
    def __init__(
        self,
        sdf_version: str,
        c1: "C1" = None,
        c2: "C2" = None,
        c3: "C3" = None,
        f: "F" = None,
        fun: "Fun" = None
    ):
        self.__version__ = sdf_version
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.f = f
        self.fun = fun

    def to_version(self, target_version: str) -> "CustomFunction":
        kwargs = {"sdf_version": target_version}
        kwargs["c1"] = self.c1.to_version(target_version) if self.c1 is not None else None
        kwargs["c2"] = self.c2.to_version(target_version) if self.c2 is not None else None
        kwargs["c3"] = self.c3.to_version(target_version) if self.c3 is not None else None
        kwargs["f"] = self.f.to_version(target_version) if self.f is not None else None
        kwargs["fun"] = self.fun.to_version(target_version) if self.fun is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("custom_function")
        if self.c1 is not None:
            el.append(self.c1.to_sdf(version))
        if self.c2 is not None:
            el.append(self.c2.to_sdf(version))
        if self.c3 is not None:
            el.append(self.c3.to_sdf(version))
        if self.f is not None:
            el.append(self.f.to_sdf(version))
        if self.fun is not None:
            el.append(self.fun.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CustomFunction":
        _c_c1 = el.find("c1")
        _c1 = C1.from_sdf(_c_c1, version) if _c_c1 is not None else None
        _c_c2 = el.find("c2")
        _c2 = C2.from_sdf(_c_c2, version) if _c_c2 is not None else None
        _c_c3 = el.find("c3")
        _c3 = C3.from_sdf(_c_c3, version) if _c_c3 is not None else None
        _c_f = el.find("f")
        _f = F.from_sdf(_c_f, version) if _c_f is not None else None
        _c_fun = el.find("fun")
        _fun = Fun.from_sdf(_c_fun, version) if _c_fun is not None else None
        return cls(sdf_version=version, c1=_c1, c2=_c2, c3=_c3, f=_f, fun=_fun)


class CutoffAngle(Model):
    def __init__(self, sdf_version: str, cutoff_angle: float = 1.5707):
        self.__version__ = sdf_version
        self.cutoff_angle = cutoff_angle

    def to_version(self, target_version: str) -> "CutoffAngle":
        kwargs = {"sdf_version": target_version}
        kwargs["cutoff_angle"] = self.cutoff_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cutoff_angle")
        if self.cutoff_angle is not None:
            el.text = str(self.cutoff_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CutoffAngle":
        _text = el.text or 1.5707
        _cutoff_angle = _parse_double(_text)
        return cls(sdf_version=version, cutoff_angle=_cutoff_angle)


class EnvTextureSize(Model):
    def __init__(self, sdf_version: str, env_texture_size: int = 256):
        self.__version__ = sdf_version
        self.env_texture_size = env_texture_size

    def to_version(self, target_version: str) -> "EnvTextureSize":
        kwargs = {"sdf_version": target_version}
        kwargs["env_texture_size"] = self.env_texture_size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("env_texture_size")
        if self.env_texture_size is not None:
            el.text = str(self.env_texture_size)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EnvTextureSize":
        _text = el.text or 256
        _env_texture_size = _parse_int32(_text)
        return cls(sdf_version=version, env_texture_size=_env_texture_size)


class Fx(Model):
    def __init__(self, sdf_version: str, fx: float = 277):
        self.__version__ = sdf_version
        self.fx = fx

    def to_version(self, target_version: str) -> "Fx":
        kwargs = {"sdf_version": target_version}
        kwargs["fx"] = self.fx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fx")
        if self.fx is not None:
            el.text = str(self.fx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fx":
        _text = el.text or 277
        _fx = _parse_double(_text)
        return cls(sdf_version=version, fx=_fx)


class Fy(Model):
    def __init__(self, sdf_version: str, fy: float = 277):
        self.__version__ = sdf_version
        self.fy = fy

    def to_version(self, target_version: str) -> "Fy":
        kwargs = {"sdf_version": target_version}
        kwargs["fy"] = self.fy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fy")
        if self.fy is not None:
            el.text = str(self.fy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fy":
        _text = el.text or 277
        _fy = _parse_double(_text)
        return cls(sdf_version=version, fy=_fy)


class Cx(Model):
    def __init__(self, sdf_version: str, cx: float = 160):
        self.__version__ = sdf_version
        self.cx = cx

    def to_version(self, target_version: str) -> "Cx":
        kwargs = {"sdf_version": target_version}
        kwargs["cx"] = self.cx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cx")
        if self.cx is not None:
            el.text = str(self.cx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cx":
        _text = el.text or 160
        _cx = _parse_double(_text)
        return cls(sdf_version=version, cx=_cx)


class Cy(Model):
    def __init__(self, sdf_version: str, cy: float = 120):
        self.__version__ = sdf_version
        self.cy = cy

    def to_version(self, target_version: str) -> "Cy":
        kwargs = {"sdf_version": target_version}
        kwargs["cy"] = self.cy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cy")
        if self.cy is not None:
            el.text = str(self.cy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cy":
        _text = el.text or 120
        _cy = _parse_double(_text)
        return cls(sdf_version=version, cy=_cy)


class S(Model):
    def __init__(self, sdf_version: str, s: float = 0.0):
        self.__version__ = sdf_version
        self.s = s

    def to_version(self, target_version: str) -> "S":
        kwargs = {"sdf_version": target_version}
        kwargs["s"] = self.s
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("s")
        if self.s is not None:
            el.text = str(self.s)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "S":
        _text = el.text or 0.0
        _s = _parse_double(_text)
        return cls(sdf_version=version, s=_s)


class Intrinsics(Model):
    def __init__(
        self,
        sdf_version: str,
        fx: "Fx" = None,
        fy: "Fy" = None,
        cx: "Cx" = None,
        cy: "Cy" = None,
        s: "S" = None
    ):
        self.__version__ = sdf_version
        self.fx = fx
        self.fy = fy
        self.cx = cx
        self.cy = cy
        self.s = s

    def to_version(self, target_version: str) -> "Intrinsics":
        kwargs = {"sdf_version": target_version}
        kwargs["fx"] = self.fx.to_version(target_version) if self.fx is not None else None
        kwargs["fy"] = self.fy.to_version(target_version) if self.fy is not None else None
        kwargs["cx"] = self.cx.to_version(target_version) if self.cx is not None else None
        kwargs["cy"] = self.cy.to_version(target_version) if self.cy is not None else None
        kwargs["s"] = self.s.to_version(target_version) if self.s is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("intrinsics")
        if self.fx is not None:
            el.append(self.fx.to_sdf(version))
        if self.fy is not None:
            el.append(self.fy.to_sdf(version))
        if self.cx is not None:
            el.append(self.cx.to_sdf(version))
        if self.cy is not None:
            el.append(self.cy.to_sdf(version))
        if self.s is not None:
            el.append(self.s.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Intrinsics":
        _c_fx = el.find("fx")
        _fx = Fx.from_sdf(_c_fx, version) if _c_fx is not None else None
        _c_fy = el.find("fy")
        _fy = Fy.from_sdf(_c_fy, version) if _c_fy is not None else None
        _c_cx = el.find("cx")
        _cx = Cx.from_sdf(_c_cx, version) if _c_cx is not None else None
        _c_cy = el.find("cy")
        _cy = Cy.from_sdf(_c_cy, version) if _c_cy is not None else None
        _c_s = el.find("s")
        _s = S.from_sdf(_c_s, version) if _c_s is not None else None
        return cls(sdf_version=version, fx=_fx, fy=_fy, cx=_cx, cy=_cy, s=_s)


class PFx(Model):
    def __init__(self, sdf_version: str, p_fx: float = 277):
        self.__version__ = sdf_version
        self.p_fx = p_fx

    def to_version(self, target_version: str) -> "PFx":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fx"] = self.p_fx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_fx")
        if self.p_fx is not None:
            el.text = str(self.p_fx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PFx":
        _text = el.text or 277
        _p_fx = _parse_double(_text)
        return cls(sdf_version=version, p_fx=_p_fx)


class PFy(Model):
    def __init__(self, sdf_version: str, p_fy: float = 277):
        self.__version__ = sdf_version
        self.p_fy = p_fy

    def to_version(self, target_version: str) -> "PFy":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fy"] = self.p_fy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_fy")
        if self.p_fy is not None:
            el.text = str(self.p_fy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PFy":
        _text = el.text or 277
        _p_fy = _parse_double(_text)
        return cls(sdf_version=version, p_fy=_p_fy)


class PCx(Model):
    def __init__(self, sdf_version: str, p_cx: float = 160):
        self.__version__ = sdf_version
        self.p_cx = p_cx

    def to_version(self, target_version: str) -> "PCx":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cx"] = self.p_cx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_cx")
        if self.p_cx is not None:
            el.text = str(self.p_cx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PCx":
        _text = el.text or 160
        _p_cx = _parse_double(_text)
        return cls(sdf_version=version, p_cx=_p_cx)


class PCy(Model):
    def __init__(self, sdf_version: str, p_cy: float = 120):
        self.__version__ = sdf_version
        self.p_cy = p_cy

    def to_version(self, target_version: str) -> "PCy":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cy"] = self.p_cy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_cy")
        if self.p_cy is not None:
            el.text = str(self.p_cy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PCy":
        _text = el.text or 120
        _p_cy = _parse_double(_text)
        return cls(sdf_version=version, p_cy=_p_cy)


class Tx(Model):
    def __init__(self, sdf_version: str, tx: float = 0.0):
        self.__version__ = sdf_version
        self.tx = tx

    def to_version(self, target_version: str) -> "Tx":
        kwargs = {"sdf_version": target_version}
        kwargs["tx"] = self.tx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("tx")
        if self.tx is not None:
            el.text = str(self.tx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Tx":
        _text = el.text or 0.0
        _tx = _parse_double(_text)
        return cls(sdf_version=version, tx=_tx)


class Ty(Model):
    def __init__(self, sdf_version: str, ty: float = 0.0):
        self.__version__ = sdf_version
        self.ty = ty

    def to_version(self, target_version: str) -> "Ty":
        kwargs = {"sdf_version": target_version}
        kwargs["ty"] = self.ty
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ty")
        if self.ty is not None:
            el.text = str(self.ty)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ty":
        _text = el.text or 0.0
        _ty = _parse_double(_text)
        return cls(sdf_version=version, ty=_ty)


class Projection(Model):
    def __init__(
        self,
        sdf_version: str,
        p_fx: "PFx" = None,
        p_fy: "PFy" = None,
        p_cx: "PCx" = None,
        p_cy: "PCy" = None,
        tx: "Tx" = None,
        ty: "Ty" = None
    ):
        self.__version__ = sdf_version
        self.p_fx = p_fx
        self.p_fy = p_fy
        self.p_cx = p_cx
        self.p_cy = p_cy
        self.tx = tx
        self.ty = ty

    def to_version(self, target_version: str) -> "Projection":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fx"] = self.p_fx.to_version(target_version) if self.p_fx is not None else None
        kwargs["p_fy"] = self.p_fy.to_version(target_version) if self.p_fy is not None else None
        kwargs["p_cx"] = self.p_cx.to_version(target_version) if self.p_cx is not None else None
        kwargs["p_cy"] = self.p_cy.to_version(target_version) if self.p_cy is not None else None
        kwargs["tx"] = self.tx.to_version(target_version) if self.tx is not None else None
        kwargs["ty"] = self.ty.to_version(target_version) if self.ty is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("projection")
        if self.p_fx is not None:
            el.append(self.p_fx.to_sdf(version))
        if self.p_fy is not None:
            el.append(self.p_fy.to_sdf(version))
        if self.p_cx is not None:
            el.append(self.p_cx.to_sdf(version))
        if self.p_cy is not None:
            el.append(self.p_cy.to_sdf(version))
        if self.tx is not None:
            el.append(self.tx.to_sdf(version))
        if self.ty is not None:
            el.append(self.ty.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Projection":
        _c_p_fx = el.find("p_fx")
        _p_fx = PFx.from_sdf(_c_p_fx, version) if _c_p_fx is not None else None
        _c_p_fy = el.find("p_fy")
        _p_fy = PFy.from_sdf(_c_p_fy, version) if _c_p_fy is not None else None
        _c_p_cx = el.find("p_cx")
        _p_cx = PCx.from_sdf(_c_p_cx, version) if _c_p_cx is not None else None
        _c_p_cy = el.find("p_cy")
        _p_cy = PCy.from_sdf(_c_p_cy, version) if _c_p_cy is not None else None
        _c_tx = el.find("tx")
        _tx = Tx.from_sdf(_c_tx, version) if _c_tx is not None else None
        _c_ty = el.find("ty")
        _ty = Ty.from_sdf(_c_ty, version) if _c_ty is not None else None
        return cls(sdf_version=version, p_fx=_p_fx, p_fy=_p_fy, p_cx=_p_cx, p_cy=_p_cy, tx=_tx, ty=_ty)


class Lens(Model):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        scale_to_hfov: "ScaleToHfov" = None,
        custom_function: "CustomFunction" = None,
        cutoff_angle: "CutoffAngle" = None,
        env_texture_size: "EnvTextureSize" = None,
        intrinsics: "Intrinsics" = None,
        projection: "Projection" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.scale_to_hfov = scale_to_hfov
        self.custom_function = custom_function
        self.cutoff_angle = cutoff_angle
        self.env_texture_size = env_texture_size
        self.intrinsics = intrinsics
        self.projection = projection

    def to_version(self, target_version: str) -> "Lens":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["scale_to_hfov"] = self.scale_to_hfov.to_version(target_version) if self.scale_to_hfov is not None else None
        kwargs["custom_function"] = self.custom_function.to_version(target_version) if self.custom_function is not None else None
        kwargs["cutoff_angle"] = self.cutoff_angle.to_version(target_version) if self.cutoff_angle is not None else None
        kwargs["env_texture_size"] = self.env_texture_size.to_version(target_version) if self.env_texture_size is not None else None
        kwargs["intrinsics"] = self.intrinsics.to_version(target_version) if self.intrinsics is not None else None
        kwargs["projection"] = self.projection.to_version(target_version) if self.projection is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lens")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.scale_to_hfov is not None:
            el.append(self.scale_to_hfov.to_sdf(version))
        if self.custom_function is not None:
            el.append(self.custom_function.to_sdf(version))
        if self.cutoff_angle is not None:
            el.append(self.cutoff_angle.to_sdf(version))
        if self.env_texture_size is not None:
            el.append(self.env_texture_size.to_sdf(version))
        if self.intrinsics is not None:
            el.append(self.intrinsics.to_sdf(version))
        if self.projection is not None:
            el.append(self.projection.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Lens":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type, version) if _c_type is not None else None
        _c_scale_to_hfov = el.find("scale_to_hfov")
        _scale_to_hfov = ScaleToHfov.from_sdf(_c_scale_to_hfov, version) if _c_scale_to_hfov is not None else None
        _c_custom_function = el.find("custom_function")
        _custom_function = CustomFunction.from_sdf(_c_custom_function, version) if _c_custom_function is not None else None
        _c_cutoff_angle = el.find("cutoff_angle")
        _cutoff_angle = CutoffAngle.from_sdf(_c_cutoff_angle, version) if _c_cutoff_angle is not None else None
        _c_env_texture_size = el.find("env_texture_size")
        _env_texture_size = EnvTextureSize.from_sdf(_c_env_texture_size, version) if _c_env_texture_size is not None else None
        _c_intrinsics = el.find("intrinsics")
        _intrinsics = Intrinsics.from_sdf(_c_intrinsics, version) if _c_intrinsics is not None else None
        _c_projection = el.find("projection")
        _projection = Projection.from_sdf(_c_projection, version) if _c_projection is not None else None
        return cls(sdf_version=version, type=_type, scale_to_hfov=_scale_to_hfov, custom_function=_custom_function, cutoff_angle=_cutoff_angle, env_texture_size=_env_texture_size, intrinsics=_intrinsics, projection=_projection)


class VisibilityMask(Model):
    def __init__(self, sdf_version: str, visibility_mask: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "VisibilityMask":
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_mask"] = self.visibility_mask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visibility_mask")
        if self.visibility_mask is not None:
            el.text = str(self.visibility_mask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VisibilityMask":
        _text = el.text or 4294967295
        _visibility_mask = _parse_uint32(_text)
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            if _visibility_mask != 4294967295:
                raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_mask=_visibility_mask)


class OpticalFrameId(Model):
    def __init__(self, sdf_version: str, optical_frame_id: str = ""):
        self.__version__ = sdf_version
        self.optical_frame_id = optical_frame_id

    def to_version(self, target_version: str) -> "OpticalFrameId":
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["optical_frame_id"] = self.optical_frame_id
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("optical_frame_id")
        if self.optical_frame_id is not None:
            el.text = self.optical_frame_id
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "OpticalFrameId":
        _text = el.text or ""
        _optical_frame_id = _text
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            if _optical_frame_id != "":
                raise ValueError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, optical_frame_id=_optical_frame_id)


class Triggered(Model):
    def __init__(self, sdf_version: str, triggered: bool = False):
        self.__version__ = sdf_version
        self.triggered = triggered

    def to_version(self, target_version: str) -> "Triggered":
        if self.triggered is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["triggered"] = self.triggered
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("triggered")
        if self.triggered is not None:
            el.text = str(self.triggered).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Triggered":
        _text = el.text or False
        _triggered = _text.strip().lower() == 'true'
        if _triggered is not None and cmp_version(version, "1.12") < 0:
            if _triggered != False:
                raise ValueError(f"'triggered' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, triggered=_triggered)


class TriggerTopic(Model):
    def __init__(self, sdf_version: str, trigger_topic: str = ""):
        self.__version__ = sdf_version
        self.trigger_topic = trigger_topic

    def to_version(self, target_version: str) -> "TriggerTopic":
        if self.trigger_topic is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["trigger_topic"] = self.trigger_topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("trigger_topic")
        if self.trigger_topic is not None:
            el.text = self.trigger_topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "TriggerTopic":
        _text = el.text or ""
        _trigger_topic = _text
        if _trigger_topic is not None and cmp_version(version, "1.12") < 0:
            if _trigger_topic != "":
                raise ValueError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, trigger_topic=_trigger_topic)


class SegmentationType(Model):
    def __init__(self, sdf_version: str, segmentation_type: str = "semantic"):
        self.__version__ = sdf_version
        self.segmentation_type = segmentation_type

    def to_version(self, target_version: str) -> "SegmentationType":
        if self.segmentation_type is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["segmentation_type"] = self.segmentation_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("segmentation_type")
        if self.segmentation_type is not None:
            el.text = self.segmentation_type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SegmentationType":
        _text = el.text or "semantic"
        _segmentation_type = _text
        if _segmentation_type is not None and cmp_version(version, "1.12") < 0:
            if _segmentation_type != "semantic":
                raise ValueError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, segmentation_type=_segmentation_type)


class BoxType(Model):
    def __init__(self, sdf_version: str, box_type: str = "2d"):
        self.__version__ = sdf_version
        self.box_type = box_type

    def to_version(self, target_version: str) -> "BoxType":
        if self.box_type is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["box_type"] = self.box_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("box_type")
        if self.box_type is not None:
            el.text = self.box_type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "BoxType":
        _text = el.text or "2d"
        _box_type = _text
        if _box_type is not None and cmp_version(version, "1.12") < 0:
            if _box_type != "2d":
                raise ValueError(f"'box_type' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, box_type=_box_type)


class Camera(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        horizontal_fov: "HorizontalFov" = None,
        image: "Image" = None,
        clip: "Clip" = None,
        save: "Save" = None,
        depth_camera: "DepthCamera" = None,
        pose: "Pose" = None,
        noise: "Noise" = None,
        camera_info_topic: "CameraInfoTopic" = None,
        distortion: "Distortion" = None,
        lens: "Lens" = None,
        visibility_mask: "VisibilityMask" = None,
        optical_frame_id: "OpticalFrameId" = None,
        triggered: "Triggered" = None,
        trigger_topic: "TriggerTopic" = None,
        segmentation_type: "SegmentationType" = None,
        box_type: "BoxType" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.horizontal_fov = horizontal_fov
        self.image = image
        self.clip = clip
        self.save = save
        self.depth_camera = depth_camera
        self.pose = pose
        self.noise = noise
        self.camera_info_topic = camera_info_topic
        self.distortion = distortion
        self.lens = lens
        self.visibility_mask = visibility_mask
        self.optical_frame_id = optical_frame_id
        self.triggered = triggered
        self.trigger_topic = trigger_topic
        self.segmentation_type = segmentation_type
        self.box_type = box_type

    def to_version(self, target_version: str) -> "Camera":
        if self.name is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.3)")
        if self.pose is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.3)")
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        if self.distortion is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'distortion' is not supported in SDF version {target_version} (added in 1.7)")
        if self.lens is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'lens' is not supported in SDF version {target_version} (added in 1.7)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        if self.triggered is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.12)")
        if self.trigger_topic is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.12)")
        if self.segmentation_type is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.12)")
        if self.box_type is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["horizontal_fov"] = self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        kwargs["save"] = self.save.to_version(target_version) if self.save is not None else None
        kwargs["depth_camera"] = self.depth_camera.to_version(target_version) if self.depth_camera is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["camera_info_topic"] = self.camera_info_topic.to_version(target_version) if self.camera_info_topic is not None else None
        kwargs["distortion"] = self.distortion.to_version(target_version) if self.distortion is not None else None
        kwargs["lens"] = self.lens.to_version(target_version) if self.lens is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        kwargs["optical_frame_id"] = self.optical_frame_id.to_version(target_version) if self.optical_frame_id is not None else None
        kwargs["triggered"] = self.triggered.to_version(target_version) if self.triggered is not None else None
        kwargs["trigger_topic"] = self.trigger_topic.to_version(target_version) if self.trigger_topic is not None else None
        kwargs["segmentation_type"] = self.segmentation_type.to_version(target_version) if self.segmentation_type is not None else None
        kwargs["box_type"] = self.box_type.to_version(target_version) if self.box_type is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera")
        if self.name is not None:
            el.set("name", self.name)
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf(version))
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        if self.save is not None:
            el.append(self.save.to_sdf(version))
        if self.depth_camera is not None:
            el.append(self.depth_camera.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.camera_info_topic is not None:
            el.append(self.camera_info_topic.to_sdf(version))
        if self.distortion is not None:
            el.append(self.distortion.to_sdf(version))
        if self.lens is not None:
            el.append(self.lens.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        if self.optical_frame_id is not None:
            el.append(self.optical_frame_id.to_sdf(version))
        if self.triggered is not None:
            el.append(self.triggered.to_sdf(version))
        if self.trigger_topic is not None:
            el.append(self.trigger_topic.to_sdf(version))
        if self.segmentation_type is not None:
            el.append(self.segmentation_type.to_sdf(version))
        if self.box_type is not None:
            el.append(self.box_type.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Camera":
        _name = el.get("name", "__default__")
        if _name is not None and cmp_version(version, "1.3") < 0:
            if _name != "__default__":
                raise ValueError(f"'name' is not supported in SDF version {version} (added in 1.3)")
        _c_horizontal_fov = el.find("horizontal_fov")
        _horizontal_fov = HorizontalFov.from_sdf(_c_horizontal_fov, version) if _c_horizontal_fov is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image, version) if _c_image is not None else None
        _c_clip = el.find("clip")
        _clip = Clip.from_sdf(_c_clip, version) if _c_clip is not None else None
        _c_save = el.find("save")
        _save = Save.from_sdf(_c_save, version) if _c_save is not None else None
        _c_depth_camera = el.find("depth_camera")
        _depth_camera = DepthCamera.from_sdf(_c_depth_camera, version) if _c_depth_camera is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.3)")
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_camera_info_topic = el.find("camera_info_topic")
        _camera_info_topic = CameraInfoTopic.from_sdf(_c_camera_info_topic, version) if _c_camera_info_topic is not None else None
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        _c_distortion = el.find("distortion")
        _distortion = Distortion.from_sdf(_c_distortion, version) if _c_distortion is not None else None
        if _distortion is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'distortion' is not supported in SDF version {version} (added in 1.7)")
        _c_lens = el.find("lens")
        _lens = Lens.from_sdf(_c_lens, version) if _c_lens is not None else None
        if _lens is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'lens' is not supported in SDF version {version} (added in 1.7)")
        _c_visibility_mask = el.find("visibility_mask")
        _visibility_mask = VisibilityMask.from_sdf(_c_visibility_mask, version) if _c_visibility_mask is not None else None
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        _c_optical_frame_id = el.find("optical_frame_id")
        _optical_frame_id = OpticalFrameId.from_sdf(_c_optical_frame_id, version) if _c_optical_frame_id is not None else None
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        _c_triggered = el.find("triggered")
        _triggered = Triggered.from_sdf(_c_triggered, version) if _c_triggered is not None else None
        if _triggered is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {version} (added in 1.12)")
        _c_trigger_topic = el.find("trigger_topic")
        _trigger_topic = TriggerTopic.from_sdf(_c_trigger_topic, version) if _c_trigger_topic is not None else None
        if _trigger_topic is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.12)")
        _c_segmentation_type = el.find("segmentation_type")
        _segmentation_type = SegmentationType.from_sdf(_c_segmentation_type, version) if _c_segmentation_type is not None else None
        if _segmentation_type is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.12)")
        _c_box_type = el.find("box_type")
        _box_type = BoxType.from_sdf(_c_box_type, version) if _c_box_type is not None else None
        if _box_type is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, name=_name, horizontal_fov=_horizontal_fov, image=_image, clip=_clip, save=_save, depth_camera=_depth_camera, pose=_pose, noise=_noise, camera_info_topic=_camera_info_topic, distortion=_distortion, lens=_lens, visibility_mask=_visibility_mask, optical_frame_id=_optical_frame_id, triggered=_triggered, trigger_topic=_trigger_topic, segmentation_type=_segmentation_type, box_type=_box_type)


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


class Min(Model):
    def __init__(self, sdf_version: str, min: float = 0):
        self.__version__ = sdf_version
        self.min = min

    def to_version(self, target_version: str) -> "Min":
        if self.min is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'min' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min")
        if self.min is not None:
            el.text = str(self.min)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Min":
        _text = el.text or 0
        _min = _parse_double(_text)
        if _min is not None and cmp_version(version, "1.2") < 0:
            if _min != 0:
                raise ValueError(f"'min' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min=_min)


class Max(Model):
    def __init__(self, sdf_version: str, max: float = 0):
        self.__version__ = sdf_version
        self.max = max

    def to_version(self, target_version: str) -> "Max":
        if self.max is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'max' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["max"] = self.max
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max")
        if self.max is not None:
            el.text = str(self.max)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Max":
        _text = el.text or 0
        _max = _parse_double(_text)
        if _max is not None and cmp_version(version, "1.2") < 0:
            if _max != 0:
                raise ValueError(f"'max' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max=_max)


class Range(Model):
    def __init__(self, sdf_version: str, min: float = 0, max: float = 0, resolution: float = 0):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Range":
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min
        kwargs["max"] = self.max
        kwargs["resolution"] = self.resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.min is not None:
            el.set("min", str(self.min))
        if self.max is not None:
            el.set("max", str(self.max))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Range":
        _min = _parse_double(el.get("min", 0))
        _max = _parse_double(el.get("max", 0))
        _resolution = _parse_double(el.get("resolution", 0))
        return cls(sdf_version=version, min=_min, max=_max, resolution=_resolution)


class Ray(Model):
    def __init__(
        self,
        sdf_version: str,
        scan: "Scan" = None,
        range: "Range" = None,
        noise: "Noise" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.scan = scan
        self.range = range
        self.noise = noise
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "Ray":
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
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
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ray":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan, version) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range, version) if _c_range is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_visibility_mask = el.find("visibility_mask")
        _visibility_mask = VisibilityMask.from_sdf(_c_visibility_mask, version) if _c_visibility_mask is not None else None
        if _visibility_mask is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)


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


class UpdateRate(Model):
    def __init__(self, sdf_version: str, update_rate: float = 0):
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
        _text = el.text or 0
        _update_rate = _parse_double(_text)
        if _update_rate is not None and cmp_version(version, "1.2") < 0:
            if _update_rate != 0:
                raise ValueError(f"'update_rate' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, update_rate=_update_rate)


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


class Localization(Model):
    def __init__(self, sdf_version: str, localization: str = "CUSTOM"):
        self.__version__ = sdf_version
        self.localization = localization

    def to_version(self, target_version: str) -> "Localization":
        kwargs = {"sdf_version": target_version}
        kwargs["localization"] = self.localization
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("localization")
        if self.localization is not None:
            el.text = self.localization
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Localization":
        _text = el.text or "CUSTOM"
        _localization = _text
        return cls(sdf_version=version, localization=_localization)


class CustomRpy(Model):
    def __init__(self, sdf_version: str, custom_rpy: Vector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if custom_rpy is None:
            custom_rpy = Vector3.from_sdf("0 0 0")
        self.custom_rpy = custom_rpy
        self.parent_frame = parent_frame

    def to_version(self, target_version: str) -> "CustomRpy":
        kwargs = {"sdf_version": target_version}
        kwargs["custom_rpy"] = self.custom_rpy
        kwargs["parent_frame"] = self.parent_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("custom_rpy")
        if self.custom_rpy is not None:
            el.text = self.custom_rpy.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CustomRpy":
        _text = el.text or "0 0 0"
        _custom_rpy = Vector3.from_sdf(_text)
        _parent_frame = el.get("parent_frame", "")
        return cls(sdf_version=version, custom_rpy=_custom_rpy, parent_frame=_parent_frame)


class GravDirX(Model):
    def __init__(self, sdf_version: str, grav_dir_x: Vector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if grav_dir_x is None:
            grav_dir_x = Vector3.from_sdf("1 0 0")
        self.grav_dir_x = grav_dir_x
        self.parent_frame = parent_frame

    def to_version(self, target_version: str) -> "GravDirX":
        kwargs = {"sdf_version": target_version}
        kwargs["grav_dir_x"] = self.grav_dir_x
        kwargs["parent_frame"] = self.parent_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grav_dir_x")
        if self.grav_dir_x is not None:
            el.text = self.grav_dir_x.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "GravDirX":
        _text = el.text or "1 0 0"
        _grav_dir_x = Vector3.from_sdf(_text)
        _parent_frame = el.get("parent_frame", "")
        return cls(sdf_version=version, grav_dir_x=_grav_dir_x, parent_frame=_parent_frame)


class OrientationReferenceFrame(Model):
    def __init__(
        self,
        sdf_version: str,
        localization: "Localization" = None,
        custom_rpy: "CustomRpy" = None,
        grav_dir_x: "GravDirX" = None
    ):
        self.__version__ = sdf_version
        self.localization = localization
        self.custom_rpy = custom_rpy
        self.grav_dir_x = grav_dir_x

    def to_version(self, target_version: str) -> "OrientationReferenceFrame":
        kwargs = {"sdf_version": target_version}
        kwargs["localization"] = self.localization.to_version(target_version) if self.localization is not None else None
        kwargs["custom_rpy"] = self.custom_rpy.to_version(target_version) if self.custom_rpy is not None else None
        kwargs["grav_dir_x"] = self.grav_dir_x.to_version(target_version) if self.grav_dir_x is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("orientation_reference_frame")
        if self.localization is not None:
            el.append(self.localization.to_sdf(version))
        if self.custom_rpy is not None:
            el.append(self.custom_rpy.to_sdf(version))
        if self.grav_dir_x is not None:
            el.append(self.grav_dir_x.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "OrientationReferenceFrame":
        _c_localization = el.find("localization")
        _localization = Localization.from_sdf(_c_localization, version) if _c_localization is not None else None
        _c_custom_rpy = el.find("custom_rpy")
        _custom_rpy = CustomRpy.from_sdf(_c_custom_rpy, version) if _c_custom_rpy is not None else None
        _c_grav_dir_x = el.find("grav_dir_x")
        _grav_dir_x = GravDirX.from_sdf(_c_grav_dir_x, version) if _c_grav_dir_x is not None else None
        return cls(sdf_version=version, localization=_localization, custom_rpy=_custom_rpy, grav_dir_x=_grav_dir_x)


class X(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "X":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("x")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "X":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Y(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Y":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("y")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Y":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Z(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Z":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("z")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Z":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class AngularVelocity(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "AngularVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angular_velocity")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AngularVelocity":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class LinearAcceleration(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "LinearAcceleration":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear_acceleration")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LinearAcceleration":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class EnableOrientation(Model):
    def __init__(self, sdf_version: str, enable_orientation: bool = True):
        self.__version__ = sdf_version
        self.enable_orientation = enable_orientation

    def to_version(self, target_version: str) -> "EnableOrientation":
        if self.enable_orientation is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_orientation"] = self.enable_orientation
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_orientation")
        if self.enable_orientation is not None:
            el.text = str(self.enable_orientation).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EnableOrientation":
        _text = el.text or True
        _enable_orientation = _text.strip().lower() == 'true'
        if _enable_orientation is not None and cmp_version(version, "1.7") < 0:
            if _enable_orientation != True:
                raise ValueError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, enable_orientation=_enable_orientation)


class Imu(Model):
    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}, {"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}]}]

    def __init__(
        self,
        sdf_version: str,
        topic: "Topic" = None,
        noise: "Noise" = None,
        orientation_reference_frame: "OrientationReferenceFrame" = None,
        angular_velocity: "AngularVelocity" = None,
        linear_acceleration: "LinearAcceleration" = None,
        enable_orientation: "EnableOrientation" = None
    ):
        self.__version__ = sdf_version
        self.topic = topic
        self.noise = noise
        self.orientation_reference_frame = orientation_reference_frame
        self.angular_velocity = angular_velocity
        self.linear_acceleration = linear_acceleration
        self.enable_orientation = enable_orientation

    def to_version(self, target_version: str) -> "Imu":
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.orientation_reference_frame is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'orientation_reference_frame' is not supported in SDF version {target_version} (added in 1.7)")
        if self.angular_velocity is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'angular_velocity' is not supported in SDF version {target_version} (added in 1.7)")
        if self.linear_acceleration is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'linear_acceleration' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_orientation is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["orientation_reference_frame"] = self.orientation_reference_frame.to_version(target_version) if self.orientation_reference_frame is not None else None
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if self.angular_velocity is not None else None
        kwargs["linear_acceleration"] = self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None else None
        kwargs["enable_orientation"] = self.enable_orientation.to_version(target_version) if self.enable_orientation is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("imu")
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.orientation_reference_frame is not None:
            el.append(self.orientation_reference_frame.to_sdf(version))
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf(version))
        if self.enable_orientation is not None:
            el.append(self.enable_orientation.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Imu":
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic, version) if _c_topic is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_orientation_reference_frame = el.find("orientation_reference_frame")
        _orientation_reference_frame = OrientationReferenceFrame.from_sdf(_c_orientation_reference_frame, version) if _c_orientation_reference_frame is not None else None
        if _orientation_reference_frame is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'orientation_reference_frame' is not supported in SDF version {version} (added in 1.7)")
        _c_angular_velocity = el.find("angular_velocity")
        _angular_velocity = AngularVelocity.from_sdf(_c_angular_velocity, version) if _c_angular_velocity is not None else None
        if _angular_velocity is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'angular_velocity' is not supported in SDF version {version} (added in 1.7)")
        _c_linear_acceleration = el.find("linear_acceleration")
        _linear_acceleration = LinearAcceleration.from_sdf(_c_linear_acceleration, version) if _c_linear_acceleration is not None else None
        if _linear_acceleration is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'linear_acceleration' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_orientation = el.find("enable_orientation")
        _enable_orientation = EnableOrientation.from_sdf(_c_enable_orientation, version) if _c_enable_orientation is not None else None
        if _enable_orientation is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, topic=_topic, noise=_noise, orientation_reference_frame=_orientation_reference_frame, angular_velocity=_angular_velocity, linear_acceleration=_linear_acceleration, enable_orientation=_enable_orientation)


class Frame(Model):
    def __init__(self, sdf_version: str, frame: str = "parent"):
        self.__version__ = sdf_version
        self.frame = frame

    def to_version(self, target_version: str) -> "Frame":
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.frame is not None:
            el.text = self.frame
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Frame":
        _text = el.text or "parent"
        _frame = _text
        return cls(sdf_version=version, frame=_frame)


class MeasureDirection(Model):
    def __init__(self, sdf_version: str, measure_direction: str = "child_to_parent"):
        self.__version__ = sdf_version
        self.measure_direction = measure_direction

    def to_version(self, target_version: str) -> "MeasureDirection":
        if self.measure_direction is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["measure_direction"] = self.measure_direction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("measure_direction")
        if self.measure_direction is not None:
            el.text = self.measure_direction
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MeasureDirection":
        _text = el.text or "child_to_parent"
        _measure_direction = _text
        if _measure_direction is not None and cmp_version(version, "1.7") < 0:
            if _measure_direction != "child_to_parent":
                raise ValueError(f"'measure_direction' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, measure_direction=_measure_direction)


class Force(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Force":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("force")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Force":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class Torque(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Torque":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("torque")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Torque":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class ForceTorque(Model):
    def __init__(
        self,
        sdf_version: str,
        frame: "Frame" = None,
        measure_direction: "MeasureDirection" = None,
        force: "Force" = None,
        torque: "Torque" = None
    ):
        self.__version__ = sdf_version
        self.frame = frame
        self.measure_direction = measure_direction
        self.force = force
        self.torque = torque

    def to_version(self, target_version: str) -> "ForceTorque":
        if self.measure_direction is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.7)")
        if self.force is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {target_version} (added in 1.7)")
        if self.torque is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame.to_version(target_version) if self.frame is not None else None
        kwargs["measure_direction"] = self.measure_direction.to_version(target_version) if self.measure_direction is not None else None
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("force_torque")
        if self.frame is not None:
            el.append(self.frame.to_sdf(version))
        if self.measure_direction is not None:
            el.append(self.measure_direction.to_sdf(version))
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque":
        _c_frame = el.find("frame")
        _frame = Frame.from_sdf(_c_frame, version) if _c_frame is not None else None
        _c_measure_direction = el.find("measure_direction")
        _measure_direction = MeasureDirection.from_sdf(_c_measure_direction, version) if _c_measure_direction is not None else None
        if _measure_direction is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {version} (added in 1.7)")
        _c_force = el.find("force")
        _force = Force.from_sdf(_c_force, version) if _c_force is not None else None
        if _force is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {version} (added in 1.7)")
        _c_torque = el.find("torque")
        _torque = Torque.from_sdf(_c_torque, version) if _c_torque is not None else None
        if _torque is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, frame=_frame, measure_direction=_measure_direction, force=_force, torque=_torque)


class PositionSensing(Model):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "Horizontal" = None,
        vertical: "Vertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "PositionSensing":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("position_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PositionSensing":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal, version) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical, version) if _c_vertical is not None else None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class VelocitySensing(Model):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "Horizontal" = None,
        vertical: "Vertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "VelocitySensing":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("velocity_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VelocitySensing":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal, version) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical, version) if _c_vertical is not None else None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Gps(Model):
    def __init__(
        self,
        sdf_version: str,
        position_sensing: "PositionSensing" = None,
        velocity_sensing: "VelocitySensing" = None
    ):
        self.__version__ = sdf_version
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_version(self, target_version: str) -> "Gps":
        kwargs = {"sdf_version": target_version}
        kwargs["position_sensing"] = self.position_sensing.to_version(target_version) if self.position_sensing is not None else None
        kwargs["velocity_sensing"] = self.velocity_sensing.to_version(target_version) if self.velocity_sensing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gps")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf(version))
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gps":
        _c_position_sensing = el.find("position_sensing")
        _position_sensing = PositionSensing.from_sdf(_c_position_sensing, version) if _c_position_sensing is not None else None
        _c_velocity_sensing = el.find("velocity_sensing")
        _velocity_sensing = VelocitySensing.from_sdf(_c_velocity_sensing, version) if _c_velocity_sensing is not None else None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class Sonar(Model):
    def __init__(
        self,
        sdf_version: str,
        min: "Min" = None,
        max: "Max" = None,
        radius: "Radius" = None,
        geometry: "Geometry" = None
    ):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.radius = radius
        self.geometry = geometry

    def to_version(self, target_version: str) -> "Sonar":
        if self.geometry is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min.to_version(target_version) if self.min is not None else None
        kwargs["max"] = self.max.to_version(target_version) if self.max is not None else None
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sonar")
        if self.min is not None:
            el.append(self.min.to_sdf(version))
        if self.max is not None:
            el.append(self.max.to_sdf(version))
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sonar":
        _c_min = el.find("min")
        _min = Min.from_sdf(_c_min, version) if _c_min is not None else None
        _c_max = el.find("max")
        _max = Max.from_sdf(_c_max, version) if _c_max is not None else None
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius, version) if _c_radius is not None else None
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry, version) if _c_geometry is not None else None
        if _geometry is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, min=_min, max=_max, radius=_radius, geometry=_geometry)


class Essid(Model):
    def __init__(self, sdf_version: str, essid: str = "wireless"):
        self.__version__ = sdf_version
        self.essid = essid

    def to_version(self, target_version: str) -> "Essid":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("essid")
        if self.essid is not None:
            el.text = self.essid
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Essid":
        _text = el.text or "wireless"
        _essid = _text
        return cls(sdf_version=version, essid=_essid)


class Frequency(Model):
    def __init__(self, sdf_version: str, frequency: float = 2442):
        self.__version__ = sdf_version
        self.frequency = frequency

    def to_version(self, target_version: str) -> "Frequency":
        kwargs = {"sdf_version": target_version}
        kwargs["frequency"] = self.frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frequency")
        if self.frequency is not None:
            el.text = str(self.frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Frequency":
        _text = el.text or 2442
        _frequency = _parse_double(_text)
        return cls(sdf_version=version, frequency=_frequency)


class MinFrequency(Model):
    def __init__(self, sdf_version: str, min_frequency: float = 2412):
        self.__version__ = sdf_version
        self.min_frequency = min_frequency

    def to_version(self, target_version: str) -> "MinFrequency":
        kwargs = {"sdf_version": target_version}
        kwargs["min_frequency"] = self.min_frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_frequency")
        if self.min_frequency is not None:
            el.text = str(self.min_frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinFrequency":
        _text = el.text or 2412
        _min_frequency = _parse_double(_text)
        return cls(sdf_version=version, min_frequency=_min_frequency)


class MaxFrequency(Model):
    def __init__(self, sdf_version: str, max_frequency: float = 2484):
        self.__version__ = sdf_version
        self.max_frequency = max_frequency

    def to_version(self, target_version: str) -> "MaxFrequency":
        kwargs = {"sdf_version": target_version}
        kwargs["max_frequency"] = self.max_frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_frequency")
        if self.max_frequency is not None:
            el.text = str(self.max_frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxFrequency":
        _text = el.text or 2484
        _max_frequency = _parse_double(_text)
        return cls(sdf_version=version, max_frequency=_max_frequency)


class Gain(Model):
    def __init__(self, sdf_version: str, gain: float = 2.5):
        self.__version__ = sdf_version
        self.gain = gain

    def to_version(self, target_version: str) -> "Gain":
        kwargs = {"sdf_version": target_version}
        kwargs["gain"] = self.gain
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gain")
        if self.gain is not None:
            el.text = str(self.gain)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gain":
        _text = el.text or 2.5
        _gain = _parse_double(_text)
        return cls(sdf_version=version, gain=_gain)


class Power(Model):
    def __init__(self, sdf_version: str, power: float = 14.50):
        self.__version__ = sdf_version
        self.power = power

    def to_version(self, target_version: str) -> "Power":
        kwargs = {"sdf_version": target_version}
        kwargs["power"] = self.power
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("power")
        if self.power is not None:
            el.text = str(self.power)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Power":
        _text = el.text or 14.50
        _power = _parse_double(_text)
        return cls(sdf_version=version, power=_power)


class Sensitivity(Model):
    def __init__(self, sdf_version: str, sensitivity: float = -90):
        self.__version__ = sdf_version
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Sensitivity":
        kwargs = {"sdf_version": target_version}
        kwargs["sensitivity"] = self.sensitivity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sensitivity")
        if self.sensitivity is not None:
            el.text = str(self.sensitivity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sensitivity":
        _text = el.text or -90
        _sensitivity = _parse_double(_text)
        return cls(sdf_version=version, sensitivity=_sensitivity)


class Transceiver(Model):
    def __init__(
        self,
        sdf_version: str,
        essid: "Essid" = None,
        frequency: "Frequency" = None,
        min_frequency: "MinFrequency" = None,
        max_frequency: "MaxFrequency" = None,
        gain: "Gain" = None,
        power: "Power" = None,
        sensitivity: "Sensitivity" = None
    ):
        self.__version__ = sdf_version
        self.essid = essid
        self.frequency = frequency
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.gain = gain
        self.power = power
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Transceiver":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid.to_version(target_version) if self.essid is not None else None
        kwargs["frequency"] = self.frequency.to_version(target_version) if self.frequency is not None else None
        kwargs["min_frequency"] = self.min_frequency.to_version(target_version) if self.min_frequency is not None else None
        kwargs["max_frequency"] = self.max_frequency.to_version(target_version) if self.max_frequency is not None else None
        kwargs["gain"] = self.gain.to_version(target_version) if self.gain is not None else None
        kwargs["power"] = self.power.to_version(target_version) if self.power is not None else None
        kwargs["sensitivity"] = self.sensitivity.to_version(target_version) if self.sensitivity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("transceiver")
        if self.essid is not None:
            el.append(self.essid.to_sdf(version))
        if self.frequency is not None:
            el.append(self.frequency.to_sdf(version))
        if self.min_frequency is not None:
            el.append(self.min_frequency.to_sdf(version))
        if self.max_frequency is not None:
            el.append(self.max_frequency.to_sdf(version))
        if self.gain is not None:
            el.append(self.gain.to_sdf(version))
        if self.power is not None:
            el.append(self.power.to_sdf(version))
        if self.sensitivity is not None:
            el.append(self.sensitivity.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Transceiver":
        _c_essid = el.find("essid")
        _essid = Essid.from_sdf(_c_essid, version) if _c_essid is not None else None
        _c_frequency = el.find("frequency")
        _frequency = Frequency.from_sdf(_c_frequency, version) if _c_frequency is not None else None
        _c_min_frequency = el.find("min_frequency")
        _min_frequency = MinFrequency.from_sdf(_c_min_frequency, version) if _c_min_frequency is not None else None
        _c_max_frequency = el.find("max_frequency")
        _max_frequency = MaxFrequency.from_sdf(_c_max_frequency, version) if _c_max_frequency is not None else None
        _c_gain = el.find("gain")
        _gain = Gain.from_sdf(_c_gain, version) if _c_gain is not None else None
        _c_power = el.find("power")
        _power = Power.from_sdf(_c_power, version) if _c_power is not None else None
        _c_sensitivity = el.find("sensitivity")
        _sensitivity = Sensitivity.from_sdf(_c_sensitivity, version) if _c_sensitivity is not None else None
        return cls(sdf_version=version, essid=_essid, frequency=_frequency, min_frequency=_min_frequency, max_frequency=_max_frequency, gain=_gain, power=_power, sensitivity=_sensitivity)


class ReferenceAltitude(Model):
    def __init__(self, sdf_version: str, reference_altitude: float = 0.0):
        self.__version__ = sdf_version
        self.reference_altitude = reference_altitude

    def to_version(self, target_version: str) -> "ReferenceAltitude":
        kwargs = {"sdf_version": target_version}
        kwargs["reference_altitude"] = self.reference_altitude
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("reference_altitude")
        if self.reference_altitude is not None:
            el.text = str(self.reference_altitude)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ReferenceAltitude":
        _text = el.text or 0.0
        _reference_altitude = _parse_double(_text)
        return cls(sdf_version=version, reference_altitude=_reference_altitude)


class Pressure(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Pressure":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pressure")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pressure":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class AirPressure(Model):
    def __init__(
        self,
        sdf_version: str,
        reference_altitude: "ReferenceAltitude" = None,
        pressure: "Pressure" = None
    ):
        self.__version__ = sdf_version
        self.reference_altitude = reference_altitude
        self.pressure = pressure

    def to_version(self, target_version: str) -> "AirPressure":
        kwargs = {"sdf_version": target_version}
        kwargs["reference_altitude"] = self.reference_altitude.to_version(target_version) if self.reference_altitude is not None else None
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("air_pressure")
        if self.reference_altitude is not None:
            el.append(self.reference_altitude.to_sdf(version))
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AirPressure":
        _c_reference_altitude = el.find("reference_altitude")
        _reference_altitude = ReferenceAltitude.from_sdf(_c_reference_altitude, version) if _c_reference_altitude is not None else None
        _c_pressure = el.find("pressure")
        _pressure = Pressure.from_sdf(_c_pressure, version) if _c_pressure is not None else None
        return cls(sdf_version=version, reference_altitude=_reference_altitude, pressure=_pressure)


class VerticalPosition(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VerticalPosition":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical_position")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VerticalPosition":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class VerticalVelocity(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VerticalVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical_velocity")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VerticalVelocity":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Altimeter(Model):
    def __init__(
        self,
        sdf_version: str,
        vertical_position: "VerticalPosition" = None,
        vertical_velocity: "VerticalVelocity" = None
    ):
        self.__version__ = sdf_version
        self.vertical_position = vertical_position
        self.vertical_velocity = vertical_velocity

    def to_version(self, target_version: str) -> "Altimeter":
        kwargs = {"sdf_version": target_version}
        kwargs["vertical_position"] = self.vertical_position.to_version(target_version) if self.vertical_position is not None else None
        kwargs["vertical_velocity"] = self.vertical_velocity.to_version(target_version) if self.vertical_velocity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("altimeter")
        if self.vertical_position is not None:
            el.append(self.vertical_position.to_sdf(version))
        if self.vertical_velocity is not None:
            el.append(self.vertical_velocity.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Altimeter":
        _c_vertical_position = el.find("vertical_position")
        _vertical_position = VerticalPosition.from_sdf(_c_vertical_position, version) if _c_vertical_position is not None else None
        _c_vertical_velocity = el.find("vertical_velocity")
        _vertical_velocity = VerticalVelocity.from_sdf(_c_vertical_velocity, version) if _c_vertical_velocity is not None else None
        return cls(sdf_version=version, vertical_position=_vertical_position, vertical_velocity=_vertical_velocity)


class Lidar(Model):
    def __init__(
        self,
        sdf_version: str,
        scan: "Scan" = None,
        range: "Range" = None,
        noise: "Noise" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.scan = scan
        self.range = range
        self.noise = noise
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "Lidar":
        if self.visibility_mask is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lidar")
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Lidar":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan, version) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range, version) if _c_range is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        _c_visibility_mask = el.find("visibility_mask")
        _visibility_mask = VisibilityMask.from_sdf(_c_visibility_mask, version) if _c_visibility_mask is not None else None
        if _visibility_mask is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)


class AspectRatio(Model):
    def __init__(self, sdf_version: str, aspect_ratio: float = 1):
        self.__version__ = sdf_version
        self.aspect_ratio = aspect_ratio

    def to_version(self, target_version: str) -> "AspectRatio":
        kwargs = {"sdf_version": target_version}
        kwargs["aspect_ratio"] = self.aspect_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("aspect_ratio")
        if self.aspect_ratio is not None:
            el.text = str(self.aspect_ratio)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AspectRatio":
        _text = el.text or 1
        _aspect_ratio = _parse_double(_text)
        return cls(sdf_version=version, aspect_ratio=_aspect_ratio)


class LogicalCamera(Model):
    def __init__(
        self,
        sdf_version: str,
        near: "Near" = None,
        far: "Far" = None,
        aspect_ratio: "AspectRatio" = None,
        horizontal_fov: "HorizontalFov" = None
    ):
        self.__version__ = sdf_version
        self.near = near
        self.far = far
        self.aspect_ratio = aspect_ratio
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "LogicalCamera":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near.to_version(target_version) if self.near is not None else None
        kwargs["far"] = self.far.to_version(target_version) if self.far is not None else None
        kwargs["aspect_ratio"] = self.aspect_ratio.to_version(target_version) if self.aspect_ratio is not None else None
        kwargs["horizontal_fov"] = self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("logical_camera")
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        if self.far is not None:
            el.append(self.far.to_sdf(version))
        if self.aspect_ratio is not None:
            el.append(self.aspect_ratio.to_sdf(version))
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LogicalCamera":
        _c_near = el.find("near")
        _near = Near.from_sdf(_c_near, version) if _c_near is not None else None
        _c_far = el.find("far")
        _far = Far.from_sdf(_c_far, version) if _c_far is not None else None
        _c_aspect_ratio = el.find("aspect_ratio")
        _aspect_ratio = AspectRatio.from_sdf(_c_aspect_ratio, version) if _c_aspect_ratio is not None else None
        _c_horizontal_fov = el.find("horizontal_fov")
        _horizontal_fov = HorizontalFov.from_sdf(_c_horizontal_fov, version) if _c_horizontal_fov is not None else None
        return cls(sdf_version=version, near=_near, far=_far, aspect_ratio=_aspect_ratio, horizontal_fov=_horizontal_fov)


class Magnetometer(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Magnetometer":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("magnetometer")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class Navsat(Model):
    def __init__(
        self,
        sdf_version: str,
        position_sensing: "PositionSensing" = None,
        velocity_sensing: "VelocitySensing" = None
    ):
        self.__version__ = sdf_version
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_version(self, target_version: str) -> "Navsat":
        kwargs = {"sdf_version": target_version}
        kwargs["position_sensing"] = self.position_sensing.to_version(target_version) if self.position_sensing is not None else None
        kwargs["velocity_sensing"] = self.velocity_sensing.to_version(target_version) if self.velocity_sensing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("navsat")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf(version))
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Navsat":
        _c_position_sensing = el.find("position_sensing")
        _position_sensing = PositionSensing.from_sdf(_c_position_sensing, version) if _c_position_sensing is not None else None
        _c_velocity_sensing = el.find("velocity_sensing")
        _velocity_sensing = VelocitySensing.from_sdf(_c_velocity_sensing, version) if _c_velocity_sensing is not None else None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class EnableMetrics(Model):
    def __init__(self, sdf_version: str, enable_metrics: bool = False):
        self.__version__ = sdf_version
        self.enable_metrics = enable_metrics

    def to_version(self, target_version: str) -> "EnableMetrics":
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_metrics"] = self.enable_metrics
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_metrics")
        if self.enable_metrics is not None:
            el.text = str(self.enable_metrics).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EnableMetrics":
        _text = el.text or False
        _enable_metrics = _text.strip().lower() == 'true'
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            if _enable_metrics != False:
                raise ValueError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, enable_metrics=_enable_metrics)


class AirSpeed(Model):
    def __init__(self, sdf_version: str, pressure: "Pressure" = None):
        self.__version__ = sdf_version
        self.pressure = pressure

    def to_version(self, target_version: str) -> "AirSpeed":
        kwargs = {"sdf_version": target_version}
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("air_speed")
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AirSpeed":
        _c_pressure = el.find("pressure")
        _pressure = Pressure.from_sdf(_c_pressure, version) if _c_pressure is not None else None
        return cls(sdf_version=version, pressure=_pressure)


class FrameId(Model):
    def __init__(self, sdf_version: str, frame_id: str = ""):
        self.__version__ = sdf_version
        self.frame_id = frame_id

    def to_version(self, target_version: str) -> "FrameId":
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame_id"] = self.frame_id
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame_id")
        if self.frame_id is not None:
            el.text = self.frame_id
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "FrameId":
        _text = el.text or ""
        _frame_id = _text
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            if _frame_id != "":
                raise ValueError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, frame_id=_frame_id)


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
        pose: "Pose" = None,
        imu: "Imu" = None,
        force_torque: "ForceTorque" = None,
        gps: "Gps" = None,
        sonar: "Sonar" = None,
        transceiver: "Transceiver" = None,
        air_pressure: "AirPressure" = None,
        altimeter: "Altimeter" = None,
        lidar: "Lidar" = None,
        logical_camera: "LogicalCamera" = None,
        magnetometer: "Magnetometer" = None,
        navsat: "Navsat" = None,
        enable_metrics: "EnableMetrics" = None,
        air_speed: "AirSpeed" = None,
        frame_id: "FrameId" = None
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
        self.imu = imu
        self.force_torque = force_torque
        self.gps = gps
        self.sonar = sonar
        self.transceiver = transceiver
        self.air_pressure = air_pressure
        self.altimeter = altimeter
        self.lidar = lidar
        self.logical_camera = logical_camera
        self.magnetometer = magnetometer
        self.navsat = navsat
        self.enable_metrics = enable_metrics
        self.air_speed = air_speed
        self.frame_id = frame_id

    def to_version(self, target_version: str) -> "Sensor":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.imu is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'imu' is not supported in SDF version {target_version} (added in 1.3)")
        if self.force_torque is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'force_torque' is not supported in SDF version {target_version} (added in 1.4)")
        if self.gps is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gps' is not supported in SDF version {target_version} (added in 1.4)")
        if self.sonar is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'sonar' is not supported in SDF version {target_version} (added in 1.4)")
        if self.transceiver is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'transceiver' is not supported in SDF version {target_version} (added in 1.4)")
        if self.air_pressure is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'air_pressure' is not supported in SDF version {target_version} (added in 1.7)")
        if self.altimeter is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'altimeter' is not supported in SDF version {target_version} (added in 1.7)")
        if self.lidar is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'lidar' is not supported in SDF version {target_version} (added in 1.7)")
        if self.logical_camera is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'logical_camera' is not supported in SDF version {target_version} (added in 1.7)")
        if self.magnetometer is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'magnetometer' is not supported in SDF version {target_version} (added in 1.7)")
        if self.navsat is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'navsat' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        if self.air_speed is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'air_speed' is not supported in SDF version {target_version} (added in 1.12)")
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
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
        kwargs["imu"] = self.imu.to_version(target_version) if self.imu is not None else None
        kwargs["force_torque"] = self.force_torque.to_version(target_version) if self.force_torque is not None else None
        kwargs["gps"] = self.gps.to_version(target_version) if self.gps is not None else None
        kwargs["sonar"] = self.sonar.to_version(target_version) if self.sonar is not None else None
        kwargs["transceiver"] = self.transceiver.to_version(target_version) if self.transceiver is not None else None
        kwargs["air_pressure"] = self.air_pressure.to_version(target_version) if self.air_pressure is not None else None
        kwargs["altimeter"] = self.altimeter.to_version(target_version) if self.altimeter is not None else None
        kwargs["lidar"] = self.lidar.to_version(target_version) if self.lidar is not None else None
        kwargs["logical_camera"] = self.logical_camera.to_version(target_version) if self.logical_camera is not None else None
        kwargs["magnetometer"] = self.magnetometer.to_version(target_version) if self.magnetometer is not None else None
        kwargs["navsat"] = self.navsat.to_version(target_version) if self.navsat is not None else None
        kwargs["enable_metrics"] = self.enable_metrics.to_version(target_version) if self.enable_metrics is not None else None
        kwargs["air_speed"] = self.air_speed.to_version(target_version) if self.air_speed is not None else None
        kwargs["frame_id"] = self.frame_id.to_version(target_version) if self.frame_id is not None else None
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
        if self.imu is not None:
            el.append(self.imu.to_sdf(version))
        if self.force_torque is not None:
            el.append(self.force_torque.to_sdf(version))
        if self.gps is not None:
            el.append(self.gps.to_sdf(version))
        if self.sonar is not None:
            el.append(self.sonar.to_sdf(version))
        if self.transceiver is not None:
            el.append(self.transceiver.to_sdf(version))
        if self.air_pressure is not None:
            el.append(self.air_pressure.to_sdf(version))
        if self.altimeter is not None:
            el.append(self.altimeter.to_sdf(version))
        if self.lidar is not None:
            el.append(self.lidar.to_sdf(version))
        if self.logical_camera is not None:
            el.append(self.logical_camera.to_sdf(version))
        if self.magnetometer is not None:
            el.append(self.magnetometer.to_sdf(version))
        if self.navsat is not None:
            el.append(self.navsat.to_sdf(version))
        if self.enable_metrics is not None:
            el.append(self.enable_metrics.to_sdf(version))
        if self.air_speed is not None:
            el.append(self.air_speed.to_sdf(version))
        if self.frame_id is not None:
            el.append(self.frame_id.to_sdf(version))
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
        _c_imu = el.find("imu")
        _imu = Imu.from_sdf(_c_imu, version) if _c_imu is not None else None
        if _imu is not None and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'imu' is not supported in SDF version {version} (added in 1.3)")
        _c_force_torque = el.find("force_torque")
        _force_torque = ForceTorque.from_sdf(_c_force_torque, version) if _c_force_torque is not None else None
        if _force_torque is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'force_torque' is not supported in SDF version {version} (added in 1.4)")
        _c_gps = el.find("gps")
        _gps = Gps.from_sdf(_c_gps, version) if _c_gps is not None else None
        if _gps is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'gps' is not supported in SDF version {version} (added in 1.4)")
        _c_sonar = el.find("sonar")
        _sonar = Sonar.from_sdf(_c_sonar, version) if _c_sonar is not None else None
        if _sonar is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'sonar' is not supported in SDF version {version} (added in 1.4)")
        _c_transceiver = el.find("transceiver")
        _transceiver = Transceiver.from_sdf(_c_transceiver, version) if _c_transceiver is not None else None
        if _transceiver is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'transceiver' is not supported in SDF version {version} (added in 1.4)")
        _c_air_pressure = el.find("air_pressure")
        _air_pressure = AirPressure.from_sdf(_c_air_pressure, version) if _c_air_pressure is not None else None
        if _air_pressure is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'air_pressure' is not supported in SDF version {version} (added in 1.7)")
        _c_altimeter = el.find("altimeter")
        _altimeter = Altimeter.from_sdf(_c_altimeter, version) if _c_altimeter is not None else None
        if _altimeter is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'altimeter' is not supported in SDF version {version} (added in 1.7)")
        _c_lidar = el.find("lidar")
        _lidar = Lidar.from_sdf(_c_lidar, version) if _c_lidar is not None else None
        if _lidar is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'lidar' is not supported in SDF version {version} (added in 1.7)")
        _c_logical_camera = el.find("logical_camera")
        _logical_camera = LogicalCamera.from_sdf(_c_logical_camera, version) if _c_logical_camera is not None else None
        if _logical_camera is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'logical_camera' is not supported in SDF version {version} (added in 1.7)")
        _c_magnetometer = el.find("magnetometer")
        _magnetometer = Magnetometer.from_sdf(_c_magnetometer, version) if _c_magnetometer is not None else None
        if _magnetometer is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'magnetometer' is not supported in SDF version {version} (added in 1.7)")
        _c_navsat = el.find("navsat")
        _navsat = Navsat.from_sdf(_c_navsat, version) if _c_navsat is not None else None
        if _navsat is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'navsat' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_metrics = el.find("enable_metrics")
        _enable_metrics = EnableMetrics.from_sdf(_c_enable_metrics, version) if _c_enable_metrics is not None else None
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        _c_air_speed = el.find("air_speed")
        _air_speed = AirSpeed.from_sdf(_c_air_speed, version) if _c_air_speed is not None else None
        if _air_speed is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'air_speed' is not supported in SDF version {version} (added in 1.12)")
        _c_frame_id = el.find("frame_id")
        _frame_id = FrameId.from_sdf(_c_frame_id, version) if _c_frame_id is not None else None
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, name=_name, type=_type, always_on=_always_on, update_rate=_update_rate, visualize=_visualize, plugin=_plugin, camera=_camera, ray=_ray, contact=_contact, rfidtag=_rfidtag, rfid=_rfid, origin=_origin, topic=_topic, pose=_pose, imu=_imu, force_torque=_force_torque, gps=_gps, sonar=_sonar, transceiver=_transceiver, air_pressure=_air_pressure, altimeter=_altimeter, lidar=_lidar, logical_camera=_logical_camera, magnetometer=_magnetometer, navsat=_navsat, enable_metrics=_enable_metrics, air_speed=_air_speed, frame_id=_frame_id)


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
        far_clip: "FarClip" = None,
        visibility_flags: "VisibilityFlags" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.plugin = plugin or []
        self.texture = texture
        self.pose = pose
        self.fov = fov
        self.near_clip = near_clip
        self.far_clip = far_clip
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "Projector":
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["texture"] = self.texture.to_version(target_version) if self.texture is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["fov"] = self.fov.to_version(target_version) if self.fov is not None else None
        kwargs["near_clip"] = self.near_clip.to_version(target_version) if self.near_clip is not None else None
        kwargs["far_clip"] = self.far_clip.to_version(target_version) if self.far_clip is not None else None
        kwargs["visibility_flags"] = self.visibility_flags.to_version(target_version) if self.visibility_flags is not None else None
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
        if self.visibility_flags is not None:
            el.append(self.visibility_flags.to_sdf(version))
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
        _c_visibility_flags = el.find("visibility_flags")
        _visibility_flags = VisibilityFlags.from_sdf(_c_visibility_flags, version) if _c_visibility_flags is not None else None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, name=_name, plugin=_plugin, texture=_texture, pose=_pose, fov=_fov, near_clip=_near_clip, far_clip=_far_clip, visibility_flags=_visibility_flags)


class Gravity(Model):
    def __init__(self, sdf_version: str, gravity: bool = True):
        self.__version__ = sdf_version
        self.gravity = gravity

    def to_version(self, target_version: str) -> "Gravity":
        if self.gravity is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'gravity' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["gravity"] = self.gravity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gravity")
        if self.gravity is not None:
            el.text = str(self.gravity).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gravity":
        _text = el.text or True
        _gravity = _text.strip().lower() == 'true'
        if _gravity is not None and cmp_version(version, "1.2") < 0:
            if _gravity != True:
                raise ValueError(f"'gravity' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, gravity=_gravity)


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


class Linear(Model):
    def __init__(self, sdf_version: str, linear: float = 0.0):
        self.__version__ = sdf_version
        self.linear = linear

    def to_version(self, target_version: str) -> "Linear":
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
        _text = el.text or 0.0
        _linear = _parse_double(_text)
        return cls(sdf_version=version, linear=_linear)


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


class AudioSink(Model):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "AudioSink":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("audio_sink")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AudioSink":
        return cls(sdf_version=version)


class Pitch(Model):
    def __init__(self, sdf_version: str, pitch: float = 1.0):
        self.__version__ = sdf_version
        self.pitch = pitch

    def to_version(self, target_version: str) -> "Pitch":
        kwargs = {"sdf_version": target_version}
        kwargs["pitch"] = self.pitch
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pitch")
        if self.pitch is not None:
            el.text = str(self.pitch)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pitch":
        _text = el.text or 1.0
        _pitch = _parse_double(_text)
        return cls(sdf_version=version, pitch=_pitch)


class Loop(Model):
    def __init__(self, sdf_version: str, loop: bool = False):
        self.__version__ = sdf_version
        self.loop = loop

    def to_version(self, target_version: str) -> "Loop":
        kwargs = {"sdf_version": target_version}
        kwargs["loop"] = self.loop
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("loop")
        if self.loop is not None:
            el.text = str(self.loop).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Loop":
        _text = el.text or False
        _loop = _text.strip().lower() == 'true'
        return cls(sdf_version=version, loop=_loop)


class AudioSource(Model):
    def __init__(
        self,
        sdf_version: str,
        uri: "Uri" = None,
        pitch: "Pitch" = None,
        gain: "Gain" = None,
        contact: "Contact" = None,
        loop: "Loop" = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.uri = uri
        self.pitch = pitch
        self.gain = gain
        self.contact = contact
        self.loop = loop
        self.pose = pose

    def to_version(self, target_version: str) -> "AudioSource":
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["pitch"] = self.pitch.to_version(target_version) if self.pitch is not None else None
        kwargs["gain"] = self.gain.to_version(target_version) if self.gain is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["loop"] = self.loop.to_version(target_version) if self.loop is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("audio_source")
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.pitch is not None:
            el.append(self.pitch.to_sdf(version))
        if self.gain is not None:
            el.append(self.gain.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        if self.loop is not None:
            el.append(self.loop.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AudioSource":
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        _c_pitch = el.find("pitch")
        _pitch = Pitch.from_sdf(_c_pitch, version) if _c_pitch is not None else None
        _c_gain = el.find("gain")
        _gain = Gain.from_sdf(_c_gain, version) if _c_gain is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact, version) if _c_contact is not None else None
        _c_loop = el.find("loop")
        _loop = Loop.from_sdf(_c_loop, version) if _c_loop is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        return cls(sdf_version=version, uri=_uri, pitch=_pitch, gain=_gain, contact=_contact, loop=_loop, pose=_pose)


class MustBeBaseLink(Model):
    def __init__(self, sdf_version: str, must_be_base_link: bool = False):
        self.__version__ = sdf_version
        self.must_be_base_link = must_be_base_link

    def to_version(self, target_version: str) -> "MustBeBaseLink":
        if self.must_be_base_link is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["must_be_base_link"] = self.must_be_base_link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("must_be_base_link")
        if self.must_be_base_link is not None:
            el.text = str(self.must_be_base_link).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MustBeBaseLink":
        _text = el.text or False
        _must_be_base_link = _text.strip().lower() == 'true'
        if _must_be_base_link is not None and cmp_version(version, "1.4") < 0:
            if _must_be_base_link != False:
                raise ValueError(f"'must_be_base_link' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, must_be_base_link=_must_be_base_link)


class Velocity(Model):
    def __init__(self, sdf_version: str, velocity: Pose = None):
        self.__version__ = sdf_version
        if velocity is None:
            velocity = Pose.from_sdf("0 0 0 0 0 0")
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Velocity":
        if self.velocity is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (added in 1.5)")
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
            el.text = self.velocity.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Velocity":
        _text = el.text or "0 0 0 0 0 0"
        _velocity = Pose.from_sdf(_text)
        if _velocity is not None and cmp_version(version, "1.5") < 0:
            if _velocity != "0 0 0 0 0 0":
                raise ValueError(f"'velocity' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, velocity=_velocity)


class Acceleration(Model):
    def __init__(self, sdf_version: str, acceleration: Pose = None):
        self.__version__ = sdf_version
        if acceleration is None:
            acceleration = Pose.from_sdf("0 0 0 0 0 0")
        self.acceleration = acceleration

    def to_version(self, target_version: str) -> "Acceleration":
        if self.acceleration is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["acceleration"] = self.acceleration
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("acceleration")
        if self.acceleration is not None:
            el.text = self.acceleration.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Acceleration":
        _text = el.text or "0 0 0 0 0 0"
        _acceleration = Pose.from_sdf(_text)
        if _acceleration is not None and cmp_version(version, "1.5") < 0:
            if _acceleration != "0 0 0 0 0 0":
                raise ValueError(f"'acceleration' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, acceleration=_acceleration)


class Wrench(Model):
    def __init__(self, sdf_version: str, wrench: Pose = None):
        self.__version__ = sdf_version
        if wrench is None:
            wrench = Pose.from_sdf("0 0 0 0 0 0")
        self.wrench = wrench

    def to_version(self, target_version: str) -> "Wrench":
        if self.wrench is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'wrench' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["wrench"] = self.wrench
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("wrench")
        if self.wrench is not None:
            el.text = self.wrench.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Wrench":
        _text = el.text or "0 0 0 0 0 0"
        _wrench = Pose.from_sdf(_text)
        if _wrench is not None and cmp_version(version, "1.5") < 0:
            if _wrench != "0 0 0 0 0 0":
                raise ValueError(f"'wrench' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, wrench=_wrench)


class Voltage(Model):
    def __init__(self, sdf_version: str, voltage: float = 0.0):
        self.__version__ = sdf_version
        self.voltage = voltage

    def to_version(self, target_version: str) -> "Voltage":
        kwargs = {"sdf_version": target_version}
        kwargs["voltage"] = self.voltage
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("voltage")
        if self.voltage is not None:
            el.text = str(self.voltage)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Voltage":
        _text = el.text or 0.0
        _voltage = _parse_double(_text)
        return cls(sdf_version=version, voltage=_voltage)


class Battery(Model):
    def __init__(self, sdf_version: str, name: str = "__default__", voltage: "Voltage" = None):
        self.__version__ = sdf_version
        self.name = name
        self.voltage = voltage

    def to_version(self, target_version: str) -> "Battery":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["voltage"] = self.voltage.to_version(target_version) if self.voltage is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("battery")
        if self.name is not None:
            el.set("name", self.name)
        if self.voltage is not None:
            el.append(self.voltage.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Battery":
        _name = el.get("name", "__default__")
        _c_voltage = el.find("voltage")
        _voltage = Voltage.from_sdf(_c_voltage, version) if _c_voltage is not None else None
        return cls(sdf_version=version, name=_name, voltage=_voltage)


class Constant(Model):
    def __init__(self, sdf_version: str, constant: float = 1):
        self.__version__ = sdf_version
        self.constant = constant

    def to_version(self, target_version: str) -> "Constant":
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
        return cls(sdf_version=version, constant=_constant)


class Quadratic(Model):
    def __init__(self, sdf_version: str, quadratic: float = 0):
        self.__version__ = sdf_version
        self.quadratic = quadratic

    def to_version(self, target_version: str) -> "Quadratic":
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
        return cls(sdf_version=version, quadratic=_quadratic)


class Attenuation(Model):
    def __init__(
        self,
        sdf_version: str,
        range: "Range" = None,
        linear: "Linear" = None,
        constant: "Constant" = None,
        quadratic: "Quadratic" = None
    ):
        self.__version__ = sdf_version
        self.range = range
        self.linear = linear
        self.constant = constant
        self.quadratic = quadratic

    def to_version(self, target_version: str) -> "Attenuation":
        kwargs = {"sdf_version": target_version}
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["linear"] = self.linear.to_version(target_version) if self.linear is not None else None
        kwargs["constant"] = self.constant.to_version(target_version) if self.constant is not None else None
        kwargs["quadratic"] = self.quadratic.to_version(target_version) if self.quadratic is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("attenuation")
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.linear is not None:
            el.append(self.linear.to_sdf(version))
        if self.constant is not None:
            el.append(self.constant.to_sdf(version))
        if self.quadratic is not None:
            el.append(self.quadratic.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Attenuation":
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range, version) if _c_range is not None else None
        _c_linear = el.find("linear")
        _linear = Linear.from_sdf(_c_linear, version) if _c_linear is not None else None
        _c_constant = el.find("constant")
        _constant = Constant.from_sdf(_c_constant, version) if _c_constant is not None else None
        _c_quadratic = el.find("quadratic")
        _quadratic = Quadratic.from_sdf(_c_quadratic, version) if _c_quadratic is not None else None
        return cls(sdf_version=version, range=_range, linear=_linear, constant=_constant, quadratic=_quadratic)


class Direction(Model):
    def __init__(self, sdf_version: str, direction: Vector3 = None):
        self.__version__ = sdf_version
        if direction is None:
            direction = Vector3.from_sdf("0 0 -1")
        self.direction = direction

    def to_version(self, target_version: str) -> "Direction":
        kwargs = {"sdf_version": target_version}
        kwargs["direction"] = self.direction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("direction")
        if self.direction is not None:
            el.text = self.direction.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Direction":
        _text = el.text or "0 0 -1"
        _direction = Vector3.from_sdf(_text)
        return cls(sdf_version=version, direction=_direction)


class InnerAngle(Model):
    def __init__(self, sdf_version: str, inner_angle: float = 0):
        self.__version__ = sdf_version
        self.inner_angle = inner_angle

    def to_version(self, target_version: str) -> "InnerAngle":
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
        return cls(sdf_version=version, inner_angle=_inner_angle)


class OuterAngle(Model):
    def __init__(self, sdf_version: str, outer_angle: float = 0):
        self.__version__ = sdf_version
        self.outer_angle = outer_angle

    def to_version(self, target_version: str) -> "OuterAngle":
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
        return cls(sdf_version=version, outer_angle=_outer_angle)


class Falloff(Model):
    def __init__(self, sdf_version: str, falloff: float = 0):
        self.__version__ = sdf_version
        self.falloff = falloff

    def to_version(self, target_version: str) -> "Falloff":
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
        return cls(sdf_version=version, falloff=_falloff)


class Spot(Model):
    def __init__(
        self,
        sdf_version: str,
        inner_angle: "InnerAngle" = None,
        outer_angle: "OuterAngle" = None,
        falloff: "Falloff" = None
    ):
        self.__version__ = sdf_version
        self.inner_angle = inner_angle
        self.outer_angle = outer_angle
        self.falloff = falloff

    def to_version(self, target_version: str) -> "Spot":
        kwargs = {"sdf_version": target_version}
        kwargs["inner_angle"] = self.inner_angle.to_version(target_version) if self.inner_angle is not None else None
        kwargs["outer_angle"] = self.outer_angle.to_version(target_version) if self.outer_angle is not None else None
        kwargs["falloff"] = self.falloff.to_version(target_version) if self.falloff is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spot")
        if self.inner_angle is not None:
            el.append(self.inner_angle.to_sdf(version))
        if self.outer_angle is not None:
            el.append(self.outer_angle.to_sdf(version))
        if self.falloff is not None:
            el.append(self.falloff.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Spot":
        _c_inner_angle = el.find("inner_angle")
        _inner_angle = InnerAngle.from_sdf(_c_inner_angle, version) if _c_inner_angle is not None else None
        _c_outer_angle = el.find("outer_angle")
        _outer_angle = OuterAngle.from_sdf(_c_outer_angle, version) if _c_outer_angle is not None else None
        _c_falloff = el.find("falloff")
        _falloff = Falloff.from_sdf(_c_falloff, version) if _c_falloff is not None else None
        return cls(sdf_version=version, inner_angle=_inner_angle, outer_angle=_outer_angle, falloff=_falloff)


class LightOn(Model):
    def __init__(self, sdf_version: str, light_on: bool = True):
        self.__version__ = sdf_version
        self.light_on = light_on

    def to_version(self, target_version: str) -> "LightOn":
        if self.light_on is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["light_on"] = self.light_on
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light_on")
        if self.light_on is not None:
            el.text = str(self.light_on).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LightOn":
        _text = el.text or True
        _light_on = _text.strip().lower() == 'true'
        if _light_on is not None and cmp_version(version, "1.12") < 0:
            if _light_on != True:
                raise ValueError(f"'light_on' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, light_on=_light_on)


class Intensity(Model):
    def __init__(self, sdf_version: str, intensity: float = 1):
        self.__version__ = sdf_version
        self.intensity = intensity

    def to_version(self, target_version: str) -> "Intensity":
        if self.intensity is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["intensity"] = self.intensity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("intensity")
        if self.intensity is not None:
            el.text = str(self.intensity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Intensity":
        _text = el.text or 1
        _intensity = _parse_double(_text)
        if _intensity is not None and cmp_version(version, "1.12") < 0:
            if _intensity != 1:
                raise ValueError(f"'intensity' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, intensity=_intensity)


class Light(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "point",
        pose: "Pose" = None,
        cast_shadows: "CastShadows" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        attenuation: "Attenuation" = None,
        direction: "Direction" = None,
        spot: "Spot" = None,
        light_on: "LightOn" = None,
        visualize: "Visualize" = None,
        intensity: "Intensity" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.pose = pose
        self.cast_shadows = cast_shadows
        self.diffuse = diffuse
        self.specular = specular
        self.attenuation = attenuation
        self.direction = direction
        self.spot = spot
        self.light_on = light_on
        self.visualize = visualize
        self.intensity = intensity

    def to_version(self, target_version: str) -> "Light":
        if self.light_on is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.12)")
        if self.visualize is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.12)")
        if self.intensity is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["cast_shadows"] = self.cast_shadows.to_version(target_version) if self.cast_shadows is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["attenuation"] = self.attenuation.to_version(target_version) if self.attenuation is not None else None
        kwargs["direction"] = self.direction.to_version(target_version) if self.direction is not None else None
        kwargs["spot"] = self.spot.to_version(target_version) if self.spot is not None else None
        kwargs["light_on"] = self.light_on.to_version(target_version) if self.light_on is not None else None
        kwargs["visualize"] = self.visualize.to_version(target_version) if self.visualize is not None else None
        kwargs["intensity"] = self.intensity.to_version(target_version) if self.intensity is not None else None
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
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.cast_shadows is not None:
            el.append(self.cast_shadows.to_sdf(version))
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
        if self.light_on is not None:
            el.append(self.light_on.to_sdf(version))
        if self.visualize is not None:
            el.append(self.visualize.to_sdf(version))
        if self.intensity is not None:
            el.append(self.intensity.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Light":
        _name = el.get("name", "__default__")
        _type = el.get("type", "point")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        _c_cast_shadows = el.find("cast_shadows")
        _cast_shadows = CastShadows.from_sdf(_c_cast_shadows, version) if _c_cast_shadows is not None else None
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
        _c_light_on = el.find("light_on")
        _light_on = LightOn.from_sdf(_c_light_on, version) if _c_light_on is not None else None
        if _light_on is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {version} (added in 1.12)")
        _c_visualize = el.find("visualize")
        _visualize = Visualize.from_sdf(_c_visualize, version) if _c_visualize is not None else None
        if _visualize is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {version} (added in 1.12)")
        _c_intensity = el.find("intensity")
        _intensity = Intensity.from_sdf(_c_intensity, version) if _c_intensity is not None else None
        if _intensity is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, name=_name, type=_type, pose=_pose, cast_shadows=_cast_shadows, diffuse=_diffuse, specular=_specular, attenuation=_attenuation, direction=_direction, spot=_spot, light_on=_light_on, visualize=_visualize, intensity=_intensity)


class Emitting(Model):
    def __init__(self, sdf_version: str, emitting: bool = True):
        self.__version__ = sdf_version
        self.emitting = emitting

    def to_version(self, target_version: str) -> "Emitting":
        kwargs = {"sdf_version": target_version}
        kwargs["emitting"] = self.emitting
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("emitting")
        if self.emitting is not None:
            el.text = str(self.emitting).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Emitting":
        _text = el.text or True
        _emitting = _text.strip().lower() == 'true'
        return cls(sdf_version=version, emitting=_emitting)


class Duration(Model):
    def __init__(self, sdf_version: str, duration: float = 0):
        self.__version__ = sdf_version
        self.duration = duration

    def to_version(self, target_version: str) -> "Duration":
        kwargs = {"sdf_version": target_version}
        kwargs["duration"] = self.duration
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("duration")
        if self.duration is not None:
            el.text = str(self.duration)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Duration":
        _text = el.text or 0
        _duration = _parse_double(_text)
        return cls(sdf_version=version, duration=_duration)


class ParticleSize(Model):
    def __init__(self, sdf_version: str, particle_size: Vector3 = None):
        self.__version__ = sdf_version
        if particle_size is None:
            particle_size = Vector3.from_sdf("1 1 1")
        self.particle_size = particle_size

    def to_version(self, target_version: str) -> "ParticleSize":
        kwargs = {"sdf_version": target_version}
        kwargs["particle_size"] = self.particle_size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("particle_size")
        if self.particle_size is not None:
            el.text = self.particle_size.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ParticleSize":
        _text = el.text or "1 1 1"
        _particle_size = Vector3.from_sdf(_text)
        return cls(sdf_version=version, particle_size=_particle_size)


class Lifetime(Model):
    def __init__(self, sdf_version: str, lifetime: float = 5):
        self.__version__ = sdf_version
        self.lifetime = lifetime

    def to_version(self, target_version: str) -> "Lifetime":
        kwargs = {"sdf_version": target_version}
        kwargs["lifetime"] = self.lifetime
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lifetime")
        if self.lifetime is not None:
            el.text = str(self.lifetime)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Lifetime":
        _text = el.text or 5
        _lifetime = _parse_double(_text)
        return cls(sdf_version=version, lifetime=_lifetime)


class Rate(Model):
    def __init__(self, sdf_version: str, rate: float = 10):
        self.__version__ = sdf_version
        self.rate = rate

    def to_version(self, target_version: str) -> "Rate":
        kwargs = {"sdf_version": target_version}
        kwargs["rate"] = self.rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rate")
        if self.rate is not None:
            el.text = str(self.rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Rate":
        _text = el.text or 10
        _rate = _parse_double(_text)
        return cls(sdf_version=version, rate=_rate)


class MinVelocity(Model):
    def __init__(self, sdf_version: str, min_velocity: float = 1):
        self.__version__ = sdf_version
        self.min_velocity = min_velocity

    def to_version(self, target_version: str) -> "MinVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["min_velocity"] = self.min_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_velocity")
        if self.min_velocity is not None:
            el.text = str(self.min_velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinVelocity":
        _text = el.text or 1
        _min_velocity = _parse_double(_text)
        return cls(sdf_version=version, min_velocity=_min_velocity)


class MaxVelocity(Model):
    def __init__(self, sdf_version: str, max_velocity: float = 1):
        self.__version__ = sdf_version
        self.max_velocity = max_velocity

    def to_version(self, target_version: str) -> "MaxVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["max_velocity"] = self.max_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_velocity")
        if self.max_velocity is not None:
            el.text = str(self.max_velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxVelocity":
        _text = el.text or 1
        _max_velocity = _parse_double(_text)
        return cls(sdf_version=version, max_velocity=_max_velocity)


class ScaleRate(Model):
    def __init__(self, sdf_version: str, scale_rate: float = 0):
        self.__version__ = sdf_version
        self.scale_rate = scale_rate

    def to_version(self, target_version: str) -> "ScaleRate":
        kwargs = {"sdf_version": target_version}
        kwargs["scale_rate"] = self.scale_rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale_rate")
        if self.scale_rate is not None:
            el.text = str(self.scale_rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ScaleRate":
        _text = el.text or 0
        _scale_rate = _parse_double(_text)
        return cls(sdf_version=version, scale_rate=_scale_rate)


class ColorStart(Model):
    def __init__(self, sdf_version: str, color_start: Color = None):
        self.__version__ = sdf_version
        if color_start is None:
            color_start = Color.from_sdf("1 1 1 1")
        self.color_start = color_start

    def to_version(self, target_version: str) -> "ColorStart":
        kwargs = {"sdf_version": target_version}
        kwargs["color_start"] = self.color_start
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("color_start")
        if self.color_start is not None:
            el.text = self.color_start.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ColorStart":
        _text = el.text or "1 1 1 1"
        _color_start = Color.from_sdf(_text)
        return cls(sdf_version=version, color_start=_color_start)


class ColorEnd(Model):
    def __init__(self, sdf_version: str, color_end: Color = None):
        self.__version__ = sdf_version
        if color_end is None:
            color_end = Color.from_sdf("1 1 1 1")
        self.color_end = color_end

    def to_version(self, target_version: str) -> "ColorEnd":
        kwargs = {"sdf_version": target_version}
        kwargs["color_end"] = self.color_end
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("color_end")
        if self.color_end is not None:
            el.text = self.color_end.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ColorEnd":
        _text = el.text or "1 1 1 1"
        _color_end = Color.from_sdf(_text)
        return cls(sdf_version=version, color_end=_color_end)


class ColorRangeImage(Model):
    def __init__(self, sdf_version: str, color_range_image: str = ""):
        self.__version__ = sdf_version
        self.color_range_image = color_range_image

    def to_version(self, target_version: str) -> "ColorRangeImage":
        kwargs = {"sdf_version": target_version}
        kwargs["color_range_image"] = self.color_range_image
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("color_range_image")
        if self.color_range_image is not None:
            el.text = self.color_range_image
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ColorRangeImage":
        _text = el.text or ""
        _color_range_image = _text
        return cls(sdf_version=version, color_range_image=_color_range_image)


class ParticleScatterRatio(Model):
    def __init__(self, sdf_version: str, particle_scatter_ratio: float = 0.65):
        self.__version__ = sdf_version
        self.particle_scatter_ratio = particle_scatter_ratio

    def to_version(self, target_version: str) -> "ParticleScatterRatio":
        kwargs = {"sdf_version": target_version}
        kwargs["particle_scatter_ratio"] = self.particle_scatter_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("particle_scatter_ratio")
        if self.particle_scatter_ratio is not None:
            el.text = str(self.particle_scatter_ratio)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ParticleScatterRatio":
        _text = el.text or 0.65
        _particle_scatter_ratio = _parse_double(_text)
        return cls(sdf_version=version, particle_scatter_ratio=_particle_scatter_ratio)


class ParticleEmitter(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "point",
        pose: "Pose" = None,
        material: "Material" = None,
        emitting: "Emitting" = None,
        duration: "Duration" = None,
        size: "Size" = None,
        particle_size: "ParticleSize" = None,
        lifetime: "Lifetime" = None,
        rate: "Rate" = None,
        min_velocity: "MinVelocity" = None,
        max_velocity: "MaxVelocity" = None,
        scale_rate: "ScaleRate" = None,
        color_start: "ColorStart" = None,
        color_end: "ColorEnd" = None,
        color_range_image: "ColorRangeImage" = None,
        topic: "Topic" = None,
        particle_scatter_ratio: "ParticleScatterRatio" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.pose = pose
        self.material = material
        self.emitting = emitting
        self.duration = duration
        self.size = size
        self.particle_size = particle_size
        self.lifetime = lifetime
        self.rate = rate
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.scale_rate = scale_rate
        self.color_start = color_start
        self.color_end = color_end
        self.color_range_image = color_range_image
        self.topic = topic
        self.particle_scatter_ratio = particle_scatter_ratio

    def to_version(self, target_version: str) -> "ParticleEmitter":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        kwargs["emitting"] = self.emitting.to_version(target_version) if self.emitting is not None else None
        kwargs["duration"] = self.duration.to_version(target_version) if self.duration is not None else None
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        kwargs["particle_size"] = self.particle_size.to_version(target_version) if self.particle_size is not None else None
        kwargs["lifetime"] = self.lifetime.to_version(target_version) if self.lifetime is not None else None
        kwargs["rate"] = self.rate.to_version(target_version) if self.rate is not None else None
        kwargs["min_velocity"] = self.min_velocity.to_version(target_version) if self.min_velocity is not None else None
        kwargs["max_velocity"] = self.max_velocity.to_version(target_version) if self.max_velocity is not None else None
        kwargs["scale_rate"] = self.scale_rate.to_version(target_version) if self.scale_rate is not None else None
        kwargs["color_start"] = self.color_start.to_version(target_version) if self.color_start is not None else None
        kwargs["color_end"] = self.color_end.to_version(target_version) if self.color_end is not None else None
        kwargs["color_range_image"] = self.color_range_image.to_version(target_version) if self.color_range_image is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["particle_scatter_ratio"] = self.particle_scatter_ratio.to_version(target_version) if self.particle_scatter_ratio is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("particle_emitter")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.material is not None:
            el.append(self.material.to_sdf(version))
        if self.emitting is not None:
            el.append(self.emitting.to_sdf(version))
        if self.duration is not None:
            el.append(self.duration.to_sdf(version))
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        if self.particle_size is not None:
            el.append(self.particle_size.to_sdf(version))
        if self.lifetime is not None:
            el.append(self.lifetime.to_sdf(version))
        if self.rate is not None:
            el.append(self.rate.to_sdf(version))
        if self.min_velocity is not None:
            el.append(self.min_velocity.to_sdf(version))
        if self.max_velocity is not None:
            el.append(self.max_velocity.to_sdf(version))
        if self.scale_rate is not None:
            el.append(self.scale_rate.to_sdf(version))
        if self.color_start is not None:
            el.append(self.color_start.to_sdf(version))
        if self.color_end is not None:
            el.append(self.color_end.to_sdf(version))
        if self.color_range_image is not None:
            el.append(self.color_range_image.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.particle_scatter_ratio is not None:
            el.append(self.particle_scatter_ratio.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ParticleEmitter":
        _name = el.get("name", "__default__")
        _type = el.get("type", "point")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        _c_material = el.find("material")
        _material = Material.from_sdf(_c_material, version) if _c_material is not None else None
        _c_emitting = el.find("emitting")
        _emitting = Emitting.from_sdf(_c_emitting, version) if _c_emitting is not None else None
        _c_duration = el.find("duration")
        _duration = Duration.from_sdf(_c_duration, version) if _c_duration is not None else None
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size, version) if _c_size is not None else None
        _c_particle_size = el.find("particle_size")
        _particle_size = ParticleSize.from_sdf(_c_particle_size, version) if _c_particle_size is not None else None
        _c_lifetime = el.find("lifetime")
        _lifetime = Lifetime.from_sdf(_c_lifetime, version) if _c_lifetime is not None else None
        _c_rate = el.find("rate")
        _rate = Rate.from_sdf(_c_rate, version) if _c_rate is not None else None
        _c_min_velocity = el.find("min_velocity")
        _min_velocity = MinVelocity.from_sdf(_c_min_velocity, version) if _c_min_velocity is not None else None
        _c_max_velocity = el.find("max_velocity")
        _max_velocity = MaxVelocity.from_sdf(_c_max_velocity, version) if _c_max_velocity is not None else None
        _c_scale_rate = el.find("scale_rate")
        _scale_rate = ScaleRate.from_sdf(_c_scale_rate, version) if _c_scale_rate is not None else None
        _c_color_start = el.find("color_start")
        _color_start = ColorStart.from_sdf(_c_color_start, version) if _c_color_start is not None else None
        _c_color_end = el.find("color_end")
        _color_end = ColorEnd.from_sdf(_c_color_end, version) if _c_color_end is not None else None
        _c_color_range_image = el.find("color_range_image")
        _color_range_image = ColorRangeImage.from_sdf(_c_color_range_image, version) if _c_color_range_image is not None else None
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic, version) if _c_topic is not None else None
        _c_particle_scatter_ratio = el.find("particle_scatter_ratio")
        _particle_scatter_ratio = ParticleScatterRatio.from_sdf(_c_particle_scatter_ratio, version) if _c_particle_scatter_ratio is not None else None
        return cls(sdf_version=version, name=_name, type=_type, pose=_pose, material=_material, emitting=_emitting, duration=_duration, size=_size, particle_size=_particle_size, lifetime=_lifetime, rate=_rate, min_velocity=_min_velocity, max_velocity=_max_velocity, scale_rate=_scale_rate, color_start=_color_start, color_end=_color_end, color_range_image=_color_range_image, topic=_topic, particle_scatter_ratio=_particle_scatter_ratio)


class EnableWind(Model):
    def __init__(self, sdf_version: str, enable_wind: bool = False):
        self.__version__ = sdf_version
        self.enable_wind = enable_wind

    def to_version(self, target_version: str) -> "EnableWind":
        if self.enable_wind is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_wind"] = self.enable_wind
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_wind")
        if self.enable_wind is not None:
            el.text = str(self.enable_wind).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EnableWind":
        _text = el.text or False
        _enable_wind = _text.strip().lower() == 'true'
        if _enable_wind is not None and cmp_version(version, "1.7") < 0:
            if _enable_wind != False:
                raise ValueError(f"'enable_wind' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, enable_wind=_enable_wind)


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
        velocity_decay: "VelocityDecay" = None,
        audio_sink: List["AudioSink"] = None,
        audio_source: List["AudioSource"] = None,
        must_be_base_link: "MustBeBaseLink" = None,
        frame: List["Frame"] = None,
        velocity: "Velocity" = None,
        acceleration: "Acceleration" = None,
        wrench: "Wrench" = None,
        battery: List["Battery"] = None,
        light: List["Light"] = None,
        particle_emitter: List["ParticleEmitter"] = None,
        enable_wind: "EnableWind" = None
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
        self.audio_sink = audio_sink or []
        self.audio_source = audio_source or []
        self.must_be_base_link = must_be_base_link
        self.frame = frame or []
        self.velocity = velocity
        self.acceleration = acceleration
        self.wrench = wrench
        self.battery = battery or []
        self.light = light or []
        self.particle_emitter = particle_emitter or []
        self.enable_wind = enable_wind

    def to_version(self, target_version: str) -> "Link":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.velocity_decay is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'velocity_decay' is not supported in SDF version {target_version} (added in 1.2)")
        if self.audio_sink is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio_sink' is not supported in SDF version {target_version} (added in 1.4)")
        if self.audio_source is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio_source' is not supported in SDF version {target_version} (added in 1.4)")
        if self.must_be_base_link is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {target_version} (added in 1.4)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.velocity is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (added in 1.5)")
        if self.acceleration is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {target_version} (added in 1.5)")
        if self.wrench is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'wrench' is not supported in SDF version {target_version} (added in 1.5)")
        if self.battery is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'battery' is not supported in SDF version {target_version} (added in 1.7)")
        if self.light is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'light' is not supported in SDF version {target_version} (added in 1.7)")
        if self.particle_emitter is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'particle_emitter' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_wind is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.7)")
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
        kwargs["audio_sink"] = [c.to_version(target_version) for c in (self.audio_sink or [])]
        kwargs["audio_source"] = [c.to_version(target_version) for c in (self.audio_source or [])]
        kwargs["must_be_base_link"] = self.must_be_base_link.to_version(target_version) if self.must_be_base_link is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["wrench"] = self.wrench.to_version(target_version) if self.wrench is not None else None
        kwargs["battery"] = [c.to_version(target_version) for c in (self.battery or [])]
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        kwargs["particle_emitter"] = [c.to_version(target_version) for c in (self.particle_emitter or [])]
        kwargs["enable_wind"] = self.enable_wind.to_version(target_version) if self.enable_wind is not None else None
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
        for item in (self.audio_sink or []):
            el.append(item.to_sdf(version))
        for item in (self.audio_source or []):
            el.append(item.to_sdf(version))
        if self.must_be_base_link is not None:
            el.append(self.must_be_base_link.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        if self.wrench is not None:
            el.append(self.wrench.to_sdf(version))
        for item in (self.battery or []):
            el.append(item.to_sdf(version))
        for item in (self.light or []):
            el.append(item.to_sdf(version))
        for item in (self.particle_emitter or []):
            el.append(item.to_sdf(version))
        if self.enable_wind is not None:
            el.append(self.enable_wind.to_sdf(version))
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
        _audio_sink = [AudioSink.from_sdf(c, version) for c in el.findall("audio_sink")]
        if _audio_sink and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'audio_sink' is not supported in SDF version {version} (added in 1.4)")
        _audio_source = [AudioSource.from_sdf(c, version) for c in el.findall("audio_source")]
        if _audio_source and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'audio_source' is not supported in SDF version {version} (added in 1.4)")
        _c_must_be_base_link = el.find("must_be_base_link")
        _must_be_base_link = MustBeBaseLink.from_sdf(_c_must_be_base_link, version) if _c_must_be_base_link is not None else None
        if _must_be_base_link is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {version} (added in 1.4)")
        _frame = [Frame.from_sdf(c, version) for c in el.findall("frame")]
        if _frame and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity, version) if _c_velocity is not None else None
        if _velocity is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'velocity' is not supported in SDF version {version} (added in 1.5)")
        _c_acceleration = el.find("acceleration")
        _acceleration = Acceleration.from_sdf(_c_acceleration, version) if _c_acceleration is not None else None
        if _acceleration is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'acceleration' is not supported in SDF version {version} (added in 1.5)")
        _c_wrench = el.find("wrench")
        _wrench = Wrench.from_sdf(_c_wrench, version) if _c_wrench is not None else None
        if _wrench is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'wrench' is not supported in SDF version {version} (added in 1.5)")
        _battery = [Battery.from_sdf(c, version) for c in el.findall("battery")]
        if _battery and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'battery' is not supported in SDF version {version} (added in 1.7)")
        _light = [Light.from_sdf(c, version) for c in el.findall("light")]
        if _light and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'light' is not supported in SDF version {version} (added in 1.7)")
        _particle_emitter = [ParticleEmitter.from_sdf(c, version) for c in el.findall("particle_emitter")]
        if _particle_emitter and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'particle_emitter' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_wind = el.find("enable_wind")
        _enable_wind = EnableWind.from_sdf(_c_enable_wind, version) if _c_enable_wind is not None else None
        if _enable_wind is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, name=_name, gravity=_gravity, self_collide=_self_collide, kinematic=_kinematic, inertial=_inertial, collision=_collision, visual=_visual, sensor=_sensor, projector=_projector, origin=_origin, damping=_damping, pose=_pose, velocity_decay=_velocity_decay, audio_sink=_audio_sink, audio_source=_audio_source, must_be_base_link=_must_be_base_link, frame=_frame, velocity=_velocity, acceleration=_acceleration, wrench=_wrench, battery=_battery, light=_light, particle_emitter=_particle_emitter, enable_wind=_enable_wind)


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


class SpringReference(Model):
    def __init__(self, sdf_version: str, spring_reference: float = 0):
        self.__version__ = sdf_version
        self.spring_reference = spring_reference

    def to_version(self, target_version: str) -> "SpringReference":
        if self.spring_reference is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {target_version} (added in 1.7)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "SpringReference":
        _text = el.text or 0
        _spring_reference = _parse_double(_text)
        if _spring_reference is not None and cmp_version(version, "1.7") < 0:
            if _spring_reference != 0:
                raise ValueError(f"'spring_reference' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, spring_reference=_spring_reference)


class SpringStiffness(Model):
    def __init__(self, sdf_version: str, spring_stiffness: float = 0):
        self.__version__ = sdf_version
        self.spring_stiffness = spring_stiffness

    def to_version(self, target_version: str) -> "SpringStiffness":
        if self.spring_stiffness is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {target_version} (added in 1.7)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "SpringStiffness":
        _text = el.text or 0
        _spring_stiffness = _parse_double(_text)
        if _spring_stiffness is not None and cmp_version(version, "1.7") < 0:
            if _spring_stiffness != 0:
                raise ValueError(f"'spring_stiffness' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, spring_stiffness=_spring_stiffness)


class Dynamics(Model):
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
        if self.spring_reference is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {target_version} (added in 1.7)")
        if self.spring_stiffness is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {target_version} (added in 1.7)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Dynamics":
        _damping = _parse_double(el.get("damping", 0))
        _friction = _parse_double(el.get("friction", 0))
        _c_spring_reference = el.find("spring_reference")
        _spring_reference = SpringReference.from_sdf(_c_spring_reference, version) if _c_spring_reference is not None else None
        if _spring_reference is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {version} (added in 1.7)")
        _c_spring_stiffness = el.find("spring_stiffness")
        _spring_stiffness = SpringStiffness.from_sdf(_c_spring_stiffness, version) if _c_spring_stiffness is not None else None
        if _spring_stiffness is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, damping=_damping, friction=_friction, spring_reference=_spring_reference, spring_stiffness=_spring_stiffness)


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


class Dissipation(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Dissipation":
        _text = el.text or 1.0
        _dissipation = _parse_double(_text)
        if _dissipation is not None and cmp_version(version, "1.4") < 0:
            if _dissipation != 1.0:
                raise ValueError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, dissipation=_dissipation)


class Limit(Model):
    def __init__(
        self,
        sdf_version: str,
        lower: float = -1e16,
        upper: float = 1e16,
        effort: float = 0,
        velocity: float = 0,
        stiffness: "Stiffness" = None,
        dissipation: "Dissipation" = None
    ):
        self.__version__ = sdf_version
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity
        self.stiffness = stiffness
        self.dissipation = dissipation

    def to_version(self, target_version: str) -> "Limit":
        if self.stiffness is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'stiffness' is not supported in SDF version {target_version} (added in 1.4)")
        if self.dissipation is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'dissipation' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["lower"] = self.lower
        kwargs["upper"] = self.upper
        kwargs["effort"] = self.effort
        kwargs["velocity"] = self.velocity
        kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
        kwargs["dissipation"] = self.dissipation.to_version(target_version) if self.dissipation is not None else None
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
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Limit":
        _lower = _parse_double(el.get("lower", -1e16))
        _upper = _parse_double(el.get("upper", 1e16))
        _effort = _parse_double(el.get("effort", 0))
        _velocity = _parse_double(el.get("velocity", 0))
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness, version) if _c_stiffness is not None else None
        if _stiffness is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
        _c_dissipation = el.find("dissipation")
        _dissipation = Dissipation.from_sdf(_c_dissipation, version) if _c_dissipation is not None else None
        if _dissipation is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, lower=_lower, upper=_upper, effort=_effort, velocity=_velocity, stiffness=_stiffness, dissipation=_dissipation)


class Xyz(Model):
    def __init__(self, sdf_version: str, xyz: Vector3 = None, expressed_in: str = ""):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.expressed_in = expressed_in

    def to_version(self, target_version: str) -> "Xyz":
        if self.xyz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.2)")
        if self.expressed_in is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'expressed_in' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        kwargs["expressed_in"] = self.expressed_in
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xyz")
        if self.xyz is not None:
            el.text = self.xyz.to_sdf()
        if self.expressed_in is not None:
            el.set("expressed_in", self.expressed_in)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xyz":
        _text = el.text or "0 0 1"
        _xyz = Vector3.from_sdf(_text)
        if _xyz is not None and cmp_version(version, "1.2") < 0:
            if _xyz != "0 0 1":
                raise ValueError(f"'xyz' is not supported in SDF version {version} (added in 1.2)")
        _expressed_in = el.get("expressed_in", "")
        if _expressed_in is not None and cmp_version(version, "1.7") < 0:
            if _expressed_in != "":
                raise ValueError(f"'expressed_in' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, xyz=_xyz, expressed_in=_expressed_in)


class InitialPosition(Model):
    def __init__(self, sdf_version: str, initial_position: float = 0):
        self.__version__ = sdf_version
        self.initial_position = initial_position

    def to_version(self, target_version: str) -> "InitialPosition":
        if self.initial_position is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.7)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "InitialPosition":
        _text = el.text or 0
        _initial_position = _parse_double(_text)
        if _initial_position is not None and cmp_version(version, "1.7") < 0:
            if _initial_position != 0:
                raise ValueError(f"'initial_position' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, initial_position=_initial_position)


class Multiplier(Model):
    def __init__(self, sdf_version: str, multiplier: float = 1.0):
        self.__version__ = sdf_version
        self.multiplier = multiplier

    def to_version(self, target_version: str) -> "Multiplier":
        kwargs = {"sdf_version": target_version}
        kwargs["multiplier"] = self.multiplier
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("multiplier")
        if self.multiplier is not None:
            el.text = str(self.multiplier)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Multiplier":
        _text = el.text or 1.0
        _multiplier = _parse_double(_text)
        return cls(sdf_version=version, multiplier=_multiplier)


class Offset(Model):
    def __init__(self, sdf_version: str, offset: float = 0):
        self.__version__ = sdf_version
        self.offset = offset

    def to_version(self, target_version: str) -> "Offset":
        kwargs = {"sdf_version": target_version}
        kwargs["offset"] = self.offset
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("offset")
        if self.offset is not None:
            el.text = str(self.offset)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Offset":
        _text = el.text or 0
        _offset = _parse_double(_text)
        return cls(sdf_version=version, offset=_offset)


class Reference(Model):
    def __init__(self, sdf_version: str, reference: float = 0):
        self.__version__ = sdf_version
        self.reference = reference

    def to_version(self, target_version: str) -> "Reference":
        kwargs = {"sdf_version": target_version}
        kwargs["reference"] = self.reference
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("reference")
        if self.reference is not None:
            el.text = str(self.reference)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Reference":
        _text = el.text or 0
        _reference = _parse_double(_text)
        return cls(sdf_version=version, reference=_reference)


class Mimic(Model):
    def __init__(
        self,
        sdf_version: str,
        joint: str = "",
        axis: str = "axis",
        multiplier: "Multiplier" = None,
        offset: "Offset" = None,
        reference: "Reference" = None
    ):
        self.__version__ = sdf_version
        self.joint = joint
        self.axis = axis
        self.multiplier = multiplier
        self.offset = offset
        self.reference = reference

    def to_version(self, target_version: str) -> "Mimic":
        kwargs = {"sdf_version": target_version}
        kwargs["joint"] = self.joint
        kwargs["axis"] = self.axis
        kwargs["multiplier"] = self.multiplier.to_version(target_version) if self.multiplier is not None else None
        kwargs["offset"] = self.offset.to_version(target_version) if self.offset is not None else None
        kwargs["reference"] = self.reference.to_version(target_version) if self.reference is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mimic")
        if self.joint is not None:
            el.set("joint", self.joint)
        if self.axis is not None:
            el.set("axis", self.axis)
        if self.multiplier is not None:
            el.append(self.multiplier.to_sdf(version))
        if self.offset is not None:
            el.append(self.offset.to_sdf(version))
        if self.reference is not None:
            el.append(self.reference.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mimic":
        _joint = el.get("joint", "")
        _axis = el.get("axis", "axis")
        _c_multiplier = el.find("multiplier")
        _multiplier = Multiplier.from_sdf(_c_multiplier, version) if _c_multiplier is not None else None
        _c_offset = el.find("offset")
        _offset = Offset.from_sdf(_c_offset, version) if _c_offset is not None else None
        _c_reference = el.find("reference")
        _reference = Reference.from_sdf(_c_reference, version) if _c_reference is not None else None
        return cls(sdf_version=version, joint=_joint, axis=_axis, multiplier=_multiplier, offset=_offset, reference=_reference)


class Axis(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        xyz: Vector3 = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None,
        initial_position: "InitialPosition" = None,
        mimic: "Mimic" = None
    ):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit
        self.initial_position = initial_position
        self.mimic = mimic

    def to_version(self, target_version: str) -> "Axis":
        if self.initial_position is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.7)")
        if self.mimic is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["initial_position"] = self.initial_position.to_version(target_version) if self.initial_position is not None else None
        kwargs["mimic"] = self.mimic.to_version(target_version) if self.mimic is not None else None
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
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf(version))
        if self.mimic is not None:
            el.append(self.mimic.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Axis":
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 1"))
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics, version) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit, version) if _c_limit is not None else None
        _c_initial_position = el.find("initial_position")
        _initial_position = InitialPosition.from_sdf(_c_initial_position, version) if _c_initial_position is not None else None
        if _initial_position is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {version} (added in 1.7)")
        _c_mimic = el.find("mimic")
        _mimic = Mimic.from_sdf(_c_mimic, version) if _c_mimic is not None else None
        if _mimic is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, xyz=_xyz, dynamics=_dynamics, limit=_limit, initial_position=_initial_position, mimic=_mimic)


class Axis2(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        xyz: Vector3 = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None,
        initial_position: "InitialPosition" = None,
        mimic: "Mimic" = None
    ):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit
        self.initial_position = initial_position
        self.mimic = mimic

    def to_version(self, target_version: str) -> "Axis2":
        if self.initial_position is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.7)")
        if self.mimic is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["initial_position"] = self.initial_position.to_version(target_version) if self.initial_position is not None else None
        kwargs["mimic"] = self.mimic.to_version(target_version) if self.mimic is not None else None
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
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf(version))
        if self.mimic is not None:
            el.append(self.mimic.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Axis2":
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 1"))
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics, version) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit, version) if _c_limit is not None else None
        _c_initial_position = el.find("initial_position")
        _initial_position = InitialPosition.from_sdf(_c_initial_position, version) if _c_initial_position is not None else None
        if _initial_position is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {version} (added in 1.7)")
        _c_mimic = el.find("mimic")
        _mimic = Mimic.from_sdf(_c_mimic, version) if _c_mimic is not None else None
        if _mimic is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, xyz=_xyz, dynamics=_dynamics, limit=_limit, initial_position=_initial_position, mimic=_mimic)


class MustBeLoopJoint(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "MustBeLoopJoint":
        _text = el.text or False
        _must_be_loop_joint = _text.strip().lower() == 'true'
        return cls(sdf_version=version, must_be_loop_joint=_must_be_loop_joint)


class Simbody(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Simbody":
        _c_must_be_loop_joint = el.find("must_be_loop_joint")
        _must_be_loop_joint = MustBeLoopJoint.from_sdf(_c_must_be_loop_joint, version) if _c_must_be_loop_joint is not None else None
        return cls(sdf_version=version, must_be_loop_joint=_must_be_loop_joint)


class ProvideFeedback(Model):
    def __init__(self, sdf_version: str, provide_feedback: bool = False):
        self.__version__ = sdf_version
        self.provide_feedback = provide_feedback

    def to_version(self, target_version: str) -> "ProvideFeedback":
        if self.provide_feedback is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.4)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "ProvideFeedback":
        _text = el.text or False
        _provide_feedback = _text.strip().lower() == 'true'
        if _provide_feedback is not None and cmp_version(version, "1.4") < 0:
            if _provide_feedback != False:
                raise ValueError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, provide_feedback=_provide_feedback)


class Physics(Model):
    _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

    def __init__(
        self,
        sdf_version: str,
        ode: "Ode" = None,
        simbody: "Simbody" = None,
        provide_feedback: "ProvideFeedback" = None
    ):
        self.__version__ = sdf_version
        self.ode = ode
        self.simbody = simbody
        self.provide_feedback = provide_feedback

    def to_version(self, target_version: str) -> "Physics":
        if self.simbody is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'simbody' is not supported in SDF version {target_version} (added in 1.4)")
        if self.provide_feedback is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["simbody"] = self.simbody.to_version(target_version) if self.simbody is not None else None
        kwargs["provide_feedback"] = self.provide_feedback.to_version(target_version) if self.provide_feedback is not None else None
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
        if self.simbody is not None:
            el.append(self.simbody.to_sdf(version))
        if self.provide_feedback is not None:
            el.append(self.provide_feedback.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Physics":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        _c_simbody = el.find("simbody")
        _simbody = Simbody.from_sdf(_c_simbody, version) if _c_simbody is not None else None
        if _simbody is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'simbody' is not supported in SDF version {version} (added in 1.4)")
        _c_provide_feedback = el.find("provide_feedback")
        _provide_feedback = ProvideFeedback.from_sdf(_c_provide_feedback, version) if _c_provide_feedback is not None else None
        if _provide_feedback is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, ode=_ode, simbody=_simbody, provide_feedback=_provide_feedback)


class GearboxRatio(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "GearboxRatio":
        _text = el.text or 1.0
        _gearbox_ratio = _parse_double(_text)
        if _gearbox_ratio is not None and cmp_version(version, "1.4") < 0:
            if _gearbox_ratio != 1.0:
                raise ValueError(f"'gearbox_ratio' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, gearbox_ratio=_gearbox_ratio)


class GearboxReferenceBody(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "GearboxReferenceBody":
        _text = el.text or "__default__"
        _gearbox_reference_body = _text
        if _gearbox_reference_body is not None and cmp_version(version, "1.4") < 0:
            if _gearbox_reference_body != "__default__":
                raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, gearbox_reference_body=_gearbox_reference_body)


class Angle(Model):
    def __init__(self, sdf_version: str, angle: float = 0, axis: int = 0):
        self.__version__ = sdf_version
        self.angle = angle
        self.axis = axis

    def to_version(self, target_version: str) -> "Angle":
        if self.angle is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'angle' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["angle"] = self.angle
        kwargs["axis"] = self.axis
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angle")
        if self.angle is not None:
            el.text = str(self.angle)
        if self.axis is not None:
            el.set("axis", str(self.axis))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Angle":
        _text = el.text or 0
        _angle = _parse_double(_text)
        if _angle is not None and cmp_version(version, "1.5") < 0:
            if _angle != 0:
                raise ValueError(f"'angle' is not supported in SDF version {version} (added in 1.5)")
        _axis = _parse_uint32(el.get("axis", 0))
        return cls(sdf_version=version, angle=_angle, axis=_axis)


class ScrewThreadPitch(Model):
    def __init__(self, sdf_version: str, screw_thread_pitch: float = 1.0):
        self.__version__ = sdf_version
        self.screw_thread_pitch = screw_thread_pitch

    def to_version(self, target_version: str) -> "ScrewThreadPitch":
        if self.screw_thread_pitch is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {target_version} (added in 1.12)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "ScrewThreadPitch":
        _text = el.text or 1.0
        _screw_thread_pitch = _parse_double(_text)
        if _screw_thread_pitch is not None and cmp_version(version, "1.12") < 0:
            if _screw_thread_pitch != 1.0:
                raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, screw_thread_pitch=_screw_thread_pitch)


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
        pose: "Pose" = None,
        sensor: List["Sensor"] = None,
        gearbox_ratio: "GearboxRatio" = None,
        gearbox_reference_body: "GearboxReferenceBody" = None,
        angle: List["Angle"] = None,
        screw_thread_pitch: "ScrewThreadPitch" = None
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
        self.sensor = sensor or []
        self.gearbox_ratio = gearbox_ratio
        self.gearbox_reference_body = gearbox_reference_body
        self.angle = angle or []
        self.screw_thread_pitch = screw_thread_pitch

    def to_version(self, target_version: str) -> "Joint":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.sensor is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'sensor' is not supported in SDF version {target_version} (added in 1.4)")
        if self.gearbox_ratio is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_ratio' is not supported in SDF version {target_version} (added in 1.4)")
        if self.gearbox_reference_body is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {target_version} (added in 1.4)")
        if self.angle is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'angle' is not supported in SDF version {target_version} (added in 1.5)")
        if self.screw_thread_pitch is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {target_version} (added in 1.12)")
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
        kwargs["sensor"] = [c.to_version(target_version) for c in (self.sensor or [])]
        kwargs["gearbox_ratio"] = self.gearbox_ratio.to_version(target_version) if self.gearbox_ratio is not None else None
        kwargs["gearbox_reference_body"] = self.gearbox_reference_body.to_version(target_version) if self.gearbox_reference_body is not None else None
        kwargs["angle"] = [c.to_version(target_version) for c in (self.angle or [])]
        kwargs["screw_thread_pitch"] = self.screw_thread_pitch.to_version(target_version) if self.screw_thread_pitch is not None else None
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
        for item in (self.sensor or []):
            el.append(item.to_sdf(version))
        if self.gearbox_ratio is not None:
            el.append(self.gearbox_ratio.to_sdf(version))
        if self.gearbox_reference_body is not None:
            el.append(self.gearbox_reference_body.to_sdf(version))
        for item in (self.angle or []):
            el.append(item.to_sdf(version))
        if self.screw_thread_pitch is not None:
            el.append(self.screw_thread_pitch.to_sdf(version))
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
        _sensor = [Sensor.from_sdf(c, version) for c in el.findall("sensor")]
        if _sensor and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'sensor' is not supported in SDF version {version} (added in 1.4)")
        _c_gearbox_ratio = el.find("gearbox_ratio")
        _gearbox_ratio = GearboxRatio.from_sdf(_c_gearbox_ratio, version) if _c_gearbox_ratio is not None else None
        if _gearbox_ratio is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'gearbox_ratio' is not supported in SDF version {version} (added in 1.4)")
        _c_gearbox_reference_body = el.find("gearbox_reference_body")
        _gearbox_reference_body = GearboxReferenceBody.from_sdf(_c_gearbox_reference_body, version) if _c_gearbox_reference_body is not None else None
        if _gearbox_reference_body is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {version} (added in 1.4)")
        _angle = [Angle.from_sdf(c, version) for c in el.findall("angle")]
        if _angle and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'angle' is not supported in SDF version {version} (added in 1.5)")
        _c_screw_thread_pitch = el.find("screw_thread_pitch")
        _screw_thread_pitch = ScrewThreadPitch.from_sdf(_c_screw_thread_pitch, version) if _c_screw_thread_pitch is not None else None
        if _screw_thread_pitch is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, name=_name, type=_type, parent=_parent, child=_child, origin=_origin, thread_pitch=_thread_pitch, axis=_axis, axis2=_axis2, physics=_physics, pose=_pose, sensor=_sensor, gearbox_ratio=_gearbox_ratio, gearbox_reference_body=_gearbox_reference_body, angle=_angle, screw_thread_pitch=_screw_thread_pitch)


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


class Position(Model):
    def __init__(self, sdf_version: str, position: float = 0, degrees: bool = False):
        self.__version__ = sdf_version
        self.position = position
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Position":
        kwargs = {"sdf_version": target_version}
        kwargs["position"] = self.position
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("position")
        if self.position is not None:
            el.text = str(self.position)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Position":
        _text = el.text or 0
        _position = _parse_double(_text)
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(sdf_version=version, position=_position, degrees=_degrees)


class AxisState(Model):
    def __init__(
        self,
        sdf_version: str,
        position: "Position" = None,
        velocity: "Velocity" = None,
        acceleration: "Acceleration" = None,
        effort: "Effort" = None
    ):
        self.__version__ = sdf_version
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.effort = effort

    def to_version(self, target_version: str) -> "AxisState":
        kwargs = {"sdf_version": target_version}
        kwargs["position"] = self.position.to_version(target_version) if self.position is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["effort"] = self.effort.to_version(target_version) if self.effort is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis_state")
        if self.position is not None:
            el.append(self.position.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        if self.effort is not None:
            el.append(self.effort.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AxisState":
        _c_position = el.find("position")
        _position = Position.from_sdf(_c_position, version) if _c_position is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity, version) if _c_velocity is not None else None
        _c_acceleration = el.find("acceleration")
        _acceleration = Acceleration.from_sdf(_c_acceleration, version) if _c_acceleration is not None else None
        _c_effort = el.find("effort")
        _effort = Effort.from_sdf(_c_effort, version) if _c_effort is not None else None
        return cls(sdf_version=version, position=_position, velocity=_velocity, acceleration=_acceleration, effort=_effort)


class Axis2State(Model):
    def __init__(
        self,
        sdf_version: str,
        position: "Position" = None,
        velocity: "Velocity" = None,
        acceleration: "Acceleration" = None,
        effort: "Effort" = None
    ):
        self.__version__ = sdf_version
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.effort = effort

    def to_version(self, target_version: str) -> "Axis2State":
        kwargs = {"sdf_version": target_version}
        kwargs["position"] = self.position.to_version(target_version) if self.position is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["effort"] = self.effort.to_version(target_version) if self.effort is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis2_state")
        if self.position is not None:
            el.append(self.position.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        if self.effort is not None:
            el.append(self.effort.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Axis2State":
        _c_position = el.find("position")
        _position = Position.from_sdf(_c_position, version) if _c_position is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity, version) if _c_velocity is not None else None
        _c_acceleration = el.find("acceleration")
        _acceleration = Acceleration.from_sdf(_c_acceleration, version) if _c_acceleration is not None else None
        _c_effort = el.find("effort")
        _effort = Effort.from_sdf(_c_effort, version) if _c_effort is not None else None
        return cls(sdf_version=version, position=_position, velocity=_velocity, acceleration=_acceleration, effort=_effort)


class JointState(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        angle: "Angle" = None,
        axis_state: "AxisState" = None,
        axis2_state: "Axis2State" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.angle = angle
        self.axis_state = axis_state
        self.axis2_state = axis2_state

    def to_version(self, target_version: str) -> "JointState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["angle"] = self.angle.to_version(target_version) if self.angle is not None else None
        kwargs["axis_state"] = self.axis_state.to_version(target_version) if self.axis_state is not None else None
        kwargs["axis2_state"] = self.axis2_state.to_version(target_version) if self.axis2_state is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("joint_state")
        if self.name is not None:
            el.set("name", self.name)
        if self.angle is not None:
            el.append(self.angle.to_sdf(version))
        if self.axis_state is not None:
            el.append(self.axis_state.to_sdf(version))
        if self.axis2_state is not None:
            el.append(self.axis2_state.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "JointState":
        _name = el.get("name", "__default__")
        _c_angle = el.find("angle")
        _angle = Angle.from_sdf(_c_angle, version) if _c_angle is not None else None
        _c_axis_state = el.find("axis_state")
        _axis_state = AxisState.from_sdf(_c_axis_state, version) if _c_axis_state is not None else None
        _c_axis2_state = el.find("axis2_state")
        _axis2_state = Axis2State.from_sdf(_c_axis2_state, version) if _c_axis2_state is not None else None
        return cls(sdf_version=version, name=_name, angle=_angle, axis_state=_axis_state, axis2_state=_axis2_state)


class LinearVelocity(Model):
    def __init__(self, sdf_version: str, linear_velocity: Vector3 = None):
        self.__version__ = sdf_version
        if linear_velocity is None:
            linear_velocity = Vector3.from_sdf("0 0 0")
        self.linear_velocity = linear_velocity

    def to_version(self, target_version: str) -> "LinearVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["linear_velocity"] = self.linear_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear_velocity")
        if self.linear_velocity is not None:
            el.text = self.linear_velocity.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LinearVelocity":
        _text = el.text or "0 0 0"
        _linear_velocity = Vector3.from_sdf(_text)
        return cls(sdf_version=version, linear_velocity=_linear_velocity)


class AngularAcceleration(Model):
    def __init__(
        self,
        sdf_version: str,
        angular_acceleration: Vector3 = None,
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if angular_acceleration is None:
            angular_acceleration = Vector3.from_sdf("0 0 0")
        self.angular_acceleration = angular_acceleration
        self.degrees = degrees

    def to_version(self, target_version: str) -> "AngularAcceleration":
        kwargs = {"sdf_version": target_version}
        kwargs["angular_acceleration"] = self.angular_acceleration
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angular_acceleration")
        if self.angular_acceleration is not None:
            el.text = self.angular_acceleration.to_sdf()
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AngularAcceleration":
        _text = el.text or "0 0 0"
        _angular_acceleration = Vector3.from_sdf(_text)
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(sdf_version=version, angular_acceleration=_angular_acceleration, degrees=_degrees)


class CollisionState(Model):
    def __init__(self, sdf_version: str, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "CollisionState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision_state")
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CollisionState":
        _name = el.get("name", "__default__")
        return cls(sdf_version=version, name=_name)


class LinkState(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        pose: "Pose" = None,
        angular_velocity: "AngularVelocity" = None,
        linear_velocity: "LinearVelocity" = None,
        velocity: "Velocity" = None,
        angular_acceleration: "AngularAcceleration" = None,
        linear_acceleration: "LinearAcceleration" = None,
        acceleration: "Acceleration" = None,
        torque: "Torque" = None,
        force: "Force" = None,
        wrench: "Wrench" = None,
        collision_state: List["CollisionState"] = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose
        self.angular_velocity = angular_velocity
        self.linear_velocity = linear_velocity
        self.velocity = velocity
        self.angular_acceleration = angular_acceleration
        self.linear_acceleration = linear_acceleration
        self.acceleration = acceleration
        self.torque = torque
        self.force = force
        self.wrench = wrench
        self.collision_state = collision_state or []

    def to_version(self, target_version: str) -> "LinkState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if self.angular_velocity is not None else None
        kwargs["linear_velocity"] = self.linear_velocity.to_version(target_version) if self.linear_velocity is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["angular_acceleration"] = self.angular_acceleration.to_version(target_version) if self.angular_acceleration is not None else None
        kwargs["linear_acceleration"] = self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None else None
        kwargs["acceleration"] = self.acceleration.to_version(target_version) if self.acceleration is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
        kwargs["wrench"] = self.wrench.to_version(target_version) if self.wrench is not None else None
        kwargs["collision_state"] = [c.to_version(target_version) for c in (self.collision_state or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("link_state")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
        if self.linear_velocity is not None:
            el.append(self.linear_velocity.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.angular_acceleration is not None:
            el.append(self.angular_acceleration.to_sdf(version))
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf(version))
        if self.acceleration is not None:
            el.append(self.acceleration.to_sdf(version))
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        if self.wrench is not None:
            el.append(self.wrench.to_sdf(version))
        for item in (self.collision_state or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LinkState":
        _name = el.get("name", "__default__")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        _c_angular_velocity = el.find("angular_velocity")
        _angular_velocity = AngularVelocity.from_sdf(_c_angular_velocity, version) if _c_angular_velocity is not None else None
        _c_linear_velocity = el.find("linear_velocity")
        _linear_velocity = LinearVelocity.from_sdf(_c_linear_velocity, version) if _c_linear_velocity is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity, version) if _c_velocity is not None else None
        _c_angular_acceleration = el.find("angular_acceleration")
        _angular_acceleration = AngularAcceleration.from_sdf(_c_angular_acceleration, version) if _c_angular_acceleration is not None else None
        _c_linear_acceleration = el.find("linear_acceleration")
        _linear_acceleration = LinearAcceleration.from_sdf(_c_linear_acceleration, version) if _c_linear_acceleration is not None else None
        _c_acceleration = el.find("acceleration")
        _acceleration = Acceleration.from_sdf(_c_acceleration, version) if _c_acceleration is not None else None
        _c_torque = el.find("torque")
        _torque = Torque.from_sdf(_c_torque, version) if _c_torque is not None else None
        _c_force = el.find("force")
        _force = Force.from_sdf(_c_force, version) if _c_force is not None else None
        _c_wrench = el.find("wrench")
        _wrench = Wrench.from_sdf(_c_wrench, version) if _c_wrench is not None else None
        _collision_state = [CollisionState.from_sdf(c, version) for c in el.findall("collision_state")]
        return cls(sdf_version=version, name=_name, pose=_pose, angular_velocity=_angular_velocity, linear_velocity=_linear_velocity, velocity=_velocity, angular_acceleration=_angular_acceleration, linear_acceleration=_linear_acceleration, acceleration=_acceleration, torque=_torque, force=_force, wrench=_wrench, collision_state=_collision_state)


class ModelState(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        joint_state: List["JointState"] = None,
        frame: List["Frame"] = None,
        pose: "Pose" = None,
        link_state: List["LinkState"] = None,
        model_state: List["ModelState"] = None,
        scale: "Scale" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.joint_state = joint_state or []
        self.frame = frame or []
        self.pose = pose
        self.link_state = link_state or []
        self.model_state = model_state or []
        self.scale = scale

    def to_version(self, target_version: str) -> "ModelState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["joint_state"] = [c.to_version(target_version) for c in (self.joint_state or [])]
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["link_state"] = [c.to_version(target_version) for c in (self.link_state or [])]
        kwargs["model_state"] = [c.to_version(target_version) for c in (self.model_state or [])]
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("model_state")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.joint_state or []):
            el.append(item.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        for item in (self.link_state or []):
            el.append(item.to_sdf(version))
        for item in (self.model_state or []):
            el.append(item.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ModelState":
        _name = el.get("name", "__default__")
        _joint_state = [JointState.from_sdf(c, version) for c in el.findall("joint_state")]
        _frame = [Frame.from_sdf(c, version) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        _link_state = [LinkState.from_sdf(c, version) for c in el.findall("link_state")]
        _model_state = [ModelState.from_sdf(c, version) for c in el.findall("model_state")]
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale, version) if _c_scale is not None else None
        return cls(sdf_version=version, name=_name, joint_state=_joint_state, frame=_frame, pose=_pose, link_state=_link_state, model_state=_model_state, scale=_scale)


class PlacementFrame(Model):
    def __init__(self, sdf_version: str, placement_frame: str = ""):
        self.__version__ = sdf_version
        self.placement_frame = placement_frame

    def to_version(self, target_version: str) -> "PlacementFrame":
        if self.placement_frame is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["placement_frame"] = self.placement_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("placement_frame")
        if self.placement_frame is not None:
            el.text = self.placement_frame
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PlacementFrame":
        _text = el.text or ""
        _placement_frame = _text
        if _placement_frame is not None and cmp_version(version, "1.12") < 0:
            if _placement_frame != "":
                raise ValueError(f"'placement_frame' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, placement_frame=_placement_frame)


class Include(Model):
    def __init__(
        self,
        sdf_version: str,
        merge: bool = False,
        pose: "Pose" = None,
        plugin: List["Plugin"] = None,
        uri: "Uri" = None,
        name: "Name" = None,
        static: "Static" = None,
        model_state: "ModelState" = None,
        placement_frame: "PlacementFrame" = None
    ):
        self.__version__ = sdf_version
        self.merge = merge
        self.pose = pose
        self.plugin = plugin or []
        self.uri = uri
        self.name = name
        self.static = static
        self.model_state = model_state
        self.placement_frame = placement_frame

    def to_version(self, target_version: str) -> "Include":
        if self.merge is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'merge' is not supported in SDF version {target_version} (added in 1.12)")
        if self.model_state is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_state' is not supported in SDF version {target_version} (added in 1.12)")
        if self.placement_frame is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["merge"] = self.merge
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["static"] = self.static.to_version(target_version) if self.static is not None else None
        kwargs["model_state"] = self.model_state.to_version(target_version) if self.model_state is not None else None
        kwargs["placement_frame"] = self.placement_frame.to_version(target_version) if self.placement_frame is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("include")
        if self.merge is not None:
            el.set("merge", str(self.merge).lower())
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        if self.static is not None:
            el.append(self.static.to_sdf(version))
        if self.model_state is not None:
            el.append(self.model_state.to_sdf(version))
        if self.placement_frame is not None:
            el.append(self.placement_frame.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Include":
        _merge = el.get("merge", False).strip().lower() == 'true'
        if _merge is not None and cmp_version(version, "1.12") < 0:
            if _merge != False:
                raise ValueError(f"'merge' is not supported in SDF version {version} (added in 1.12)")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name, version) if _c_name is not None else None
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static, version) if _c_static is not None else None
        _c_model_state = el.find("model_state")
        _model_state = ModelState.from_sdf(_c_model_state, version) if _c_model_state is not None else None
        if _model_state is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'model_state' is not supported in SDF version {version} (added in 1.12)")
        _c_placement_frame = el.find("placement_frame")
        _placement_frame = PlacementFrame.from_sdf(_c_placement_frame, version) if _c_placement_frame is not None else None
        if _placement_frame is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, merge=_merge, pose=_pose, plugin=_plugin, uri=_uri, name=_name, static=_static, model_state=_model_state, placement_frame=_placement_frame)


class Model(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        static: bool = False,
        canonical_link: str = "",
        placement_frame: str = "",
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        gripper: List["Gripper"] = None,
        origin: "Origin" = None,
        allow_auto_disable: "AllowAutoDisable" = None,
        pose: "Pose" = None,
        frame: List["Frame"] = None,
        model: List["Model"] = None,
        scale: "Scale" = None,
        self_collide: "SelfCollide" = None,
        include: List["Include"] = None,
        enable_wind: "EnableWind" = None,
        model_state: "ModelState" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.static = static
        self.canonical_link = canonical_link
        self.placement_frame = placement_frame
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.gripper = gripper or []
        self.origin = origin
        self.allow_auto_disable = allow_auto_disable
        self.pose = pose
        self.frame = frame or []
        self.model = model or []
        self.scale = scale
        self.self_collide = self_collide
        self.include = include or []
        self.enable_wind = enable_wind
        self.model_state = model_state

    def to_version(self, target_version: str) -> "Model":
        if self.canonical_link is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'canonical_link' is not supported in SDF version {target_version} (added in 1.7)")
        if self.placement_frame is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.12)")
        if self.allow_auto_disable is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'allow_auto_disable' is not supported in SDF version {target_version} (added in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.model is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'model' is not supported in SDF version {target_version} (added in 1.5)")
        if self.scale is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.6)")
        if self.self_collide is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (added in 1.7)")
        if self.include is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'include' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_wind is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.7)")
        if self.model_state is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_state' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["static"] = self.static
        kwargs["canonical_link"] = self.canonical_link
        kwargs["placement_frame"] = self.placement_frame
        kwargs["link"] = [c.to_version(target_version) for c in (self.link or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["gripper"] = [c.to_version(target_version) for c in (self.gripper or [])]
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["allow_auto_disable"] = self.allow_auto_disable.to_version(target_version) if self.allow_auto_disable is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        kwargs["self_collide"] = self.self_collide.to_version(target_version) if self.self_collide is not None else None
        kwargs["include"] = [c.to_version(target_version) for c in (self.include or [])]
        kwargs["enable_wind"] = self.enable_wind.to_version(target_version) if self.enable_wind is not None else None
        kwargs["model_state"] = self.model_state.to_version(target_version) if self.model_state is not None else None
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
        if self.canonical_link is not None:
            el.set("canonical_link", self.canonical_link)
        if self.placement_frame is not None:
            el.set("placement_frame", self.placement_frame)
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
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf(version))
        for item in (self.include or []):
            el.append(item.to_sdf(version))
        if self.enable_wind is not None:
            el.append(self.enable_wind.to_sdf(version))
        if self.model_state is not None:
            el.append(self.model_state.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Model":
        _name = el.get("name", "__default__")
        _static = el.get("static", False).strip().lower() == 'true'
        _canonical_link = el.get("canonical_link", "")
        if _canonical_link is not None and cmp_version(version, "1.7") < 0:
            if _canonical_link != "":
                raise ValueError(f"'canonical_link' is not supported in SDF version {version} (added in 1.7)")
        _placement_frame = el.get("placement_frame", "")
        if _placement_frame is not None and cmp_version(version, "1.12") < 0:
            if _placement_frame != "":
                raise ValueError(f"'placement_frame' is not supported in SDF version {version} (added in 1.12)")
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
        _frame = [Frame.from_sdf(c, version) for c in el.findall("frame")]
        if _frame and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _model = [Model.from_sdf(c, version) for c in el.findall("model")]
        if _model and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'model' is not supported in SDF version {version} (added in 1.5)")
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale, version) if _c_scale is not None else None
        if _scale is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {version} (added in 1.6)")
        _c_self_collide = el.find("self_collide")
        _self_collide = SelfCollide.from_sdf(_c_self_collide, version) if _c_self_collide is not None else None
        if _self_collide is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {version} (added in 1.7)")
        _include = [Include.from_sdf(c, version) for c in el.findall("include")]
        if _include and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'include' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_wind = el.find("enable_wind")
        _enable_wind = EnableWind.from_sdf(_c_enable_wind, version) if _c_enable_wind is not None else None
        if _enable_wind is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {version} (added in 1.7)")
        _c_model_state = el.find("model_state")
        _model_state = ModelState.from_sdf(_c_model_state, version) if _c_model_state is not None else None
        if _model_state is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'model_state' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, name=_name, static=_static, canonical_link=_canonical_link, placement_frame=_placement_frame, link=_link, joint=_joint, plugin=_plugin, gripper=_gripper, origin=_origin, allow_auto_disable=_allow_auto_disable, pose=_pose, frame=_frame, model=_model, scale=_scale, self_collide=_self_collide, include=_include, enable_wind=_enable_wind, model_state=_model_state)
