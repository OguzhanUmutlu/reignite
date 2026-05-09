### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color as _SDFColor
from ..utils.pose import Pose as _SDFPose
from ..utils.vector2d import Vector2d as _SDFVector2d
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



class Mass(BaseModel):
    def __init__(self, sdf_version: str, mass: float = 1.0):
        self.__version__ = sdf_version
        self.mass = mass

    def to_version(self, target_version: str) -> "Mass":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _mass = _parse_double(_text)
        if isinstance(_mass, SDFError):
            return _mass
        return cls(sdf_version=version, mass=_mass)


class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Pose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.8") >= 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (removed in 1.8)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Ixx(BaseModel):
    def __init__(self, sdf_version: str, ixx: float = 1.0):
        self.__version__ = sdf_version
        self.ixx = ixx

    def to_version(self, target_version: str) -> "Ixx":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _ixx = _parse_double(_text)
        if isinstance(_ixx, SDFError):
            return _ixx
        return cls(sdf_version=version, ixx=_ixx)


class Ixy(BaseModel):
    def __init__(self, sdf_version: str, ixy: float = 0.0):
        self.__version__ = sdf_version
        self.ixy = ixy

    def to_version(self, target_version: str) -> "Ixy":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _ixy = _parse_double(_text)
        if isinstance(_ixy, SDFError):
            return _ixy
        return cls(sdf_version=version, ixy=_ixy)


class Ixz(BaseModel):
    def __init__(self, sdf_version: str, ixz: float = 0.0):
        self.__version__ = sdf_version
        self.ixz = ixz

    def to_version(self, target_version: str) -> "Ixz":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _ixz = _parse_double(_text)
        if isinstance(_ixz, SDFError):
            return _ixz
        return cls(sdf_version=version, ixz=_ixz)


class Iyy(BaseModel):
    def __init__(self, sdf_version: str, iyy: float = 1.0):
        self.__version__ = sdf_version
        self.iyy = iyy

    def to_version(self, target_version: str) -> "Iyy":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _iyy = _parse_double(_text)
        if isinstance(_iyy, SDFError):
            return _iyy
        return cls(sdf_version=version, iyy=_iyy)


class Iyz(BaseModel):
    def __init__(self, sdf_version: str, iyz: float = 0.0):
        self.__version__ = sdf_version
        self.iyz = iyz

    def to_version(self, target_version: str) -> "Iyz":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _iyz = _parse_double(_text)
        if isinstance(_iyz, SDFError):
            return _iyz
        return cls(sdf_version=version, iyz=_iyz)


class Izz(BaseModel):
    def __init__(self, sdf_version: str, izz: float = 1.0):
        self.__version__ = sdf_version
        self.izz = izz

    def to_version(self, target_version: str) -> "Izz":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _izz = _parse_double(_text)
        if isinstance(_izz, SDFError):
            return _izz
        return cls(sdf_version=version, izz=_izz)


class Inertia(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        ixx: "Ixx" = None,
        ixy: "Ixy" = None,
        ixz: "Ixz" = None,
        iyy: "Iyy" = None,
        iyz: "Iyz" = None,
        izz: "Izz" = None
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
        kwargs["ixx"] = self.ixx.to_version(target_version) if self.ixx is not None else None
        kwargs["ixy"] = self.ixy.to_version(target_version) if self.ixy is not None else None
        kwargs["ixz"] = self.ixz.to_version(target_version) if self.ixz is not None else None
        kwargs["iyy"] = self.iyy.to_version(target_version) if self.iyy is not None else None
        kwargs["iyz"] = self.iyz.to_version(target_version) if self.iyz is not None else None
        kwargs["izz"] = self.izz.to_version(target_version) if self.izz is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inertia")
        if self.ixx is not None:
            el.append(self.ixx.to_sdf(version))
        if self.ixy is not None:
            el.append(self.ixy.to_sdf(version))
        if self.ixz is not None:
            el.append(self.ixz.to_sdf(version))
        if self.iyy is not None:
            el.append(self.iyy.to_sdf(version))
        if self.iyz is not None:
            el.append(self.iyz.to_sdf(version))
        if self.izz is not None:
            el.append(self.izz.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_ixx = el.find("ixx")
        if _c_ixx is not None:
            _res = Ixx._from_sdf(_c_ixx, version)
            if isinstance(_res, SDFError):
                return _res.extend("ixx")
            _ixx = _res
        else:
            _ixx = None
        _c_ixy = el.find("ixy")
        if _c_ixy is not None:
            _res = Ixy._from_sdf(_c_ixy, version)
            if isinstance(_res, SDFError):
                return _res.extend("ixy")
            _ixy = _res
        else:
            _ixy = None
        _c_ixz = el.find("ixz")
        if _c_ixz is not None:
            _res = Ixz._from_sdf(_c_ixz, version)
            if isinstance(_res, SDFError):
                return _res.extend("ixz")
            _ixz = _res
        else:
            _ixz = None
        _c_iyy = el.find("iyy")
        if _c_iyy is not None:
            _res = Iyy._from_sdf(_c_iyy, version)
            if isinstance(_res, SDFError):
                return _res.extend("iyy")
            _iyy = _res
        else:
            _iyy = None
        _c_iyz = el.find("iyz")
        if _c_iyz is not None:
            _res = Iyz._from_sdf(_c_iyz, version)
            if isinstance(_res, SDFError):
                return _res.extend("iyz")
            _iyz = _res
        else:
            _iyz = None
        _c_izz = el.find("izz")
        if _c_izz is not None:
            _res = Izz._from_sdf(_c_izz, version)
            if isinstance(_res, SDFError):
                return _res.extend("izz")
            _izz = _res
        else:
            _izz = None
        return cls(sdf_version=version, ixx=_ixx, ixy=_ixy, ixz=_ixz, iyy=_iyy, iyz=_iyz, izz=_izz)


class FramePose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(self, sdf_version: str, pose: _SDFPose = None, frame: str = ""):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame

    def to_version(self, target_version: str) -> "FramePose":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        return cls(sdf_version=version, pose=_pose, frame=_frame)


class Frame(BaseModel):
    def __init__(self, sdf_version: str, name: str = "", pose: "FramePose" = None):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "Frame":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = FramePose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, name=_name, pose=_pose)


class Inertial(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        mass: "Mass" = None,
        pose: "Pose" = None,
        inertia: "Inertia" = None,
        frame: List["Frame"] = None
    ):
        self.__version__ = sdf_version
        self.mass = mass
        self.pose = pose
        self.inertia = inertia
        self.frame = frame or []

    def to_version(self, target_version: str) -> "Inertial":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["mass"] = self.mass.to_version(target_version) if self.mass is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["inertia"] = self.inertia.to_version(target_version) if self.inertia is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inertial")
        if self.mass is not None:
            el.append(self.mass.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.inertia is not None:
            el.append(self.inertia.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_mass = el.find("mass")
        if _c_mass is not None:
            _res = Mass._from_sdf(_c_mass, version)
            if isinstance(_res, SDFError):
                return _res.extend("mass")
            _mass = _res
        else:
            _mass = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_inertia = el.find("inertia")
        if _c_inertia is not None:
            _res = Inertia._from_sdf(_c_inertia, version)
            if isinstance(_res, SDFError):
                return _res.extend("inertia")
            _inertia = _res
        else:
            _inertia = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, mass=_mass, pose=_pose, inertia=_inertia, frame=_frame)


class Size(BaseModel):
    def __init__(self, sdf_version: str, size: _SDFVector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = _SDFVector3.from_sdf("1 1 1")
        self.size = size

    def to_version(self, target_version: str) -> "Size":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _size = _SDFVector3._from_sdf(_text, version)
        if isinstance(_size, SDFError):
            return _size
        return cls(sdf_version=version, size=_size)


class Box(BaseModel):
    def __init__(self, sdf_version: str, size: "Size" = None):
        self.__version__ = sdf_version
        self.size = size

    def to_version(self, target_version: str) -> "Box":
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("box")
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_size = el.find("size")
        if _c_size is not None:
            _res = Size._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        return cls(sdf_version=version, size=_size)


class Radius(BaseModel):
    def __init__(self, sdf_version: str, radius: float = 1):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Radius":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _radius = _parse_double(_text)
        if isinstance(_radius, SDFError):
            return _radius
        return cls(sdf_version=version, radius=_radius)


class Sphere(BaseModel):
    def __init__(self, sdf_version: str, radius: "Radius" = None):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Sphere":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sphere")
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_radius = el.find("radius")
        if _c_radius is not None:
            _res = Radius._from_sdf(_c_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("radius")
            _radius = _res
        else:
            _radius = None
        return cls(sdf_version=version, radius=_radius)


class Length(BaseModel):
    def __init__(self, sdf_version: str, length: float = 1):
        self.__version__ = sdf_version
        self.length = length

    def to_version(self, target_version: str) -> "Length":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _length = _parse_double(_text)
        if isinstance(_length, SDFError):
            return _length
        return cls(sdf_version=version, length=_length)


class Cylinder(BaseModel):
    def __init__(self, sdf_version: str, radius: "Radius" = None, length: "Length" = None):
        self.__version__ = sdf_version
        self.radius = radius
        self.length = length

    def to_version(self, target_version: str) -> "Cylinder":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["length"] = self.length.to_version(target_version) if self.length is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cylinder")
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.length is not None:
            el.append(self.length.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_radius = el.find("radius")
        if _c_radius is not None:
            _res = Radius._from_sdf(_c_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("radius")
            _radius = _res
        else:
            _radius = None
        _c_length = el.find("length")
        if _c_length is not None:
            _res = Length._from_sdf(_c_length, version)
            if isinstance(_res, SDFError):
                return _res.extend("length")
            _length = _res
        else:
            _length = None
        return cls(sdf_version=version, radius=_radius, length=_length)


class Filename(BaseModel):
    def __init__(self, sdf_version: str, filename: str = "__default__"):
        self.__version__ = sdf_version
        self.filename = filename

    def to_version(self, target_version: str) -> "Filename":
        if self.filename is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (removed in 1.3)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _filename = _text
        if isinstance(_filename, SDFError):
            return _filename
        return cls(sdf_version=version, filename=_filename)


class Uri(BaseModel):
    def __init__(self, sdf_version: str, uri: str = "__default__"):
        self.__version__ = sdf_version
        self.uri = uri

    def to_version(self, target_version: str) -> "Uri":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _uri = _text
        if isinstance(_uri, SDFError):
            return _uri
        return cls(sdf_version=version, uri=_uri)


class Scale(BaseModel):
    def __init__(self, sdf_version: str, scale: _SDFVector3 = None):
        self.__version__ = sdf_version
        if scale is None:
            scale = _SDFVector3.from_sdf("1 1 1")
        self.scale = scale

    def to_version(self, target_version: str) -> "Scale":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _scale = _SDFVector3._from_sdf(_text, version)
        if isinstance(_scale, SDFError):
            return _scale
        return cls(sdf_version=version, scale=_scale)


class Name(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _name = _text
        if isinstance(_name, SDFError):
            return _name
        return cls(sdf_version=version, name=_name)


class Center(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _center = str(_text).strip().lower() == 'true'
        if isinstance(_center, SDFError):
            return _center
        return cls(sdf_version=version, center=_center)


class Submesh(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_name = el.find("name")
        if _c_name is not None:
            _res = Name._from_sdf(_c_name, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _name = _res
        else:
            _name = None
        _c_center = el.find("center")
        if _c_center is not None:
            _res = Center._from_sdf(_c_center, version)
            if isinstance(_res, SDFError):
                return _res.extend("center")
            _center = _res
        else:
            _center = None
        return cls(sdf_version=version, name=_name, center=_center)


class Mesh(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        filename: "Filename" = None,
        uri: "Uri" = None,
        scale: "Scale" = None,
        submesh: "Submesh" = None
    ):
        self.__version__ = sdf_version
        self.filename = filename
        self.uri = uri
        self.scale = scale
        self.submesh = submesh

    def to_version(self, target_version: str) -> "Mesh":
        if self.filename is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (removed in 1.3)")
        if self.submesh is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'submesh' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename.to_version(target_version) if self.filename is not None else None
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        kwargs["submesh"] = self.submesh.to_version(target_version) if self.submesh is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mesh")
        if self.filename is not None:
            el.append(self.filename.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        if self.submesh is not None:
            el.append(self.submesh.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_filename = el.find("filename")
        if _c_filename is not None:
            _res = Filename._from_sdf(_c_filename, version)
            if isinstance(_res, SDFError):
                return _res.extend("filename")
            _filename = _res
        else:
            _filename = None
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        _c_scale = el.find("scale")
        if _c_scale is not None:
            _res = Scale._from_sdf(_c_scale, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale")
            _scale = _res
        else:
            _scale = None
        _c_submesh = el.find("submesh")
        if _c_submesh is not None:
            _res = Submesh._from_sdf(_c_submesh, version)
            if isinstance(_res, SDFError):
                return _res.extend("submesh")
            _submesh = _res
        else:
            _submesh = None
        if _submesh is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'submesh' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, filename=_filename, uri=_uri, scale=_scale, submesh=_submesh)


class Normal(BaseModel):
    def __init__(self, sdf_version: str, normal: _SDFVector3 = None):
        self.__version__ = sdf_version
        if normal is None:
            normal = _SDFVector3.from_sdf("0 0 1")
        self.normal = normal

    def to_version(self, target_version: str) -> "Normal":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 1"
        _normal = _SDFVector3._from_sdf(_text, version)
        if isinstance(_normal, SDFError):
            return _normal
        return cls(sdf_version=version, normal=_normal)


class PlaneSize(BaseModel):
    def __init__(self, sdf_version: str, size: _SDFVector2d = None):
        self.__version__ = sdf_version
        if size is None:
            size = _SDFVector2d.from_sdf("1 1")
        self.size = size

    def to_version(self, target_version: str) -> "PlaneSize":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1"
        _size = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_size, SDFError):
            return _size
        return cls(sdf_version=version, size=_size)


class Plane(BaseModel):
    def __init__(self, sdf_version: str, normal: "Normal" = None, size: "PlaneSize" = None):
        self.__version__ = sdf_version
        self.normal = normal
        self.size = size

    def to_version(self, target_version: str) -> "Plane":
        kwargs = {"sdf_version": target_version}
        kwargs["normal"] = self.normal.to_version(target_version) if self.normal is not None else None
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plane")
        if self.normal is not None:
            el.append(self.normal.to_sdf(version))
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_normal = el.find("normal")
        if _c_normal is not None:
            _res = Normal._from_sdf(_c_normal, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal")
            _normal = _res
        else:
            _normal = None
        _c_size = el.find("size")
        if _c_size is not None:
            _res = PlaneSize._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        return cls(sdf_version=version, normal=_normal, size=_size)


class ImageScale(BaseModel):
    def __init__(self, sdf_version: str, scale: float = 1):
        self.__version__ = sdf_version
        self.scale = scale

    def to_version(self, target_version: str) -> "ImageScale":
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
            el.text = str(self.scale)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _scale = _parse_double(_text)
        if isinstance(_scale, SDFError):
            return _scale
        return cls(sdf_version=version, scale=_scale)


class Threshold(BaseModel):
    def __init__(self, sdf_version: str, threshold: int = 200):
        self.__version__ = sdf_version
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Threshold":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 200
        _threshold = _parse_int32(_text)
        if isinstance(_threshold, SDFError):
            return _threshold
        return cls(sdf_version=version, threshold=_threshold)


class Height(BaseModel):
    def __init__(self, sdf_version: str, height: float = 1):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _height = _parse_double(_text)
        if isinstance(_height, SDFError):
            return _height
        return cls(sdf_version=version, height=_height)


class Granularity(BaseModel):
    def __init__(self, sdf_version: str, granularity: int = 1):
        self.__version__ = sdf_version
        self.granularity = granularity

    def to_version(self, target_version: str) -> "Granularity":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _granularity = _parse_int32(_text)
        if isinstance(_granularity, SDFError):
            return _granularity
        return cls(sdf_version=version, granularity=_granularity)


class Image(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        uri: "Uri" = None,
        scale: "ImageScale" = None,
        threshold: "Threshold" = None,
        height: "Height" = None,
        granularity: "Granularity" = None
    ):
        self.__version__ = sdf_version
        self.uri = uri
        self.scale = scale
        self.threshold = threshold
        self.height = height
        self.granularity = granularity

    def to_version(self, target_version: str) -> "Image":
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        kwargs["threshold"] = self.threshold.to_version(target_version) if self.threshold is not None else None
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        kwargs["granularity"] = self.granularity.to_version(target_version) if self.granularity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("image")
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        if self.threshold is not None:
            el.append(self.threshold.to_sdf(version))
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        if self.granularity is not None:
            el.append(self.granularity.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        _c_scale = el.find("scale")
        if _c_scale is not None:
            _res = ImageScale._from_sdf(_c_scale, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale")
            _scale = _res
        else:
            _scale = None
        _c_threshold = el.find("threshold")
        if _c_threshold is not None:
            _res = Threshold._from_sdf(_c_threshold, version)
            if isinstance(_res, SDFError):
                return _res.extend("threshold")
            _threshold = _res
        else:
            _threshold = None
        _c_height = el.find("height")
        if _c_height is not None:
            _res = Height._from_sdf(_c_height, version)
            if isinstance(_res, SDFError):
                return _res.extend("height")
            _height = _res
        else:
            _height = None
        _c_granularity = el.find("granularity")
        if _c_granularity is not None:
            _res = Granularity._from_sdf(_c_granularity, version)
            if isinstance(_res, SDFError):
                return _res.extend("granularity")
            _granularity = _res
        else:
            _granularity = None
        return cls(sdf_version=version, uri=_uri, scale=_scale, threshold=_threshold, height=_height, granularity=_granularity)


class Pos(BaseModel):
    def __init__(self, sdf_version: str, pos: _SDFVector3 = None):
        self.__version__ = sdf_version
        if pos is None:
            pos = _SDFVector3.from_sdf("0 0 0")
        self.pos = pos

    def to_version(self, target_version: str) -> "Pos":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _pos = _SDFVector3._from_sdf(_text, version)
        if isinstance(_pos, SDFError):
            return _pos
        return cls(sdf_version=version, pos=_pos)


class TextureSize(BaseModel):
    def __init__(self, sdf_version: str, size: float = 10):
        self.__version__ = sdf_version
        self.size = size

    def to_version(self, target_version: str) -> "TextureSize":
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
            el.text = str(self.size)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _size = _parse_double(_text)
        if isinstance(_size, SDFError):
            return _size
        return cls(sdf_version=version, size=_size)


class Diffuse(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _diffuse = _text
        if isinstance(_diffuse, SDFError):
            return _diffuse
        return cls(sdf_version=version, diffuse=_diffuse)


class TextureNormal(BaseModel):
    def __init__(self, sdf_version: str, normal: str = "__default__"):
        self.__version__ = sdf_version
        self.normal = normal

    def to_version(self, target_version: str) -> "TextureNormal":
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
            el.text = self.normal
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _normal = _text
        if isinstance(_normal, SDFError):
            return _normal
        return cls(sdf_version=version, normal=_normal)


class Texture(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        size: "TextureSize" = None,
        diffuse: "Diffuse" = None,
        normal: "TextureNormal" = None
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_size = el.find("size")
        if _c_size is not None:
            _res = TextureSize._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        _c_diffuse = el.find("diffuse")
        if _c_diffuse is not None:
            _res = Diffuse._from_sdf(_c_diffuse, version)
            if isinstance(_res, SDFError):
                return _res.extend("diffuse")
            _diffuse = _res
        else:
            _diffuse = None
        _c_normal = el.find("normal")
        if _c_normal is not None:
            _res = TextureNormal._from_sdf(_c_normal, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal")
            _normal = _res
        else:
            _normal = None
        return cls(sdf_version=version, size=_size, diffuse=_diffuse, normal=_normal)


class MinHeight(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min_height = _parse_double(_text)
        if isinstance(_min_height, SDFError):
            return _min_height
        return cls(sdf_version=version, min_height=_min_height)


class FadeDist(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _fade_dist = _parse_double(_text)
        if isinstance(_fade_dist, SDFError):
            return _fade_dist
        return cls(sdf_version=version, fade_dist=_fade_dist)


class Blend(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_min_height = el.find("min_height")
        if _c_min_height is not None:
            _res = MinHeight._from_sdf(_c_min_height, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_height")
            _min_height = _res
        else:
            _min_height = None
        _c_fade_dist = el.find("fade_dist")
        if _c_fade_dist is not None:
            _res = FadeDist._from_sdf(_c_fade_dist, version)
            if isinstance(_res, SDFError):
                return _res.extend("fade_dist")
            _fade_dist = _res
        else:
            _fade_dist = None
        return cls(sdf_version=version, min_height=_min_height, fade_dist=_fade_dist)


class UseTerrainPaging(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _use_terrain_paging = str(_text).strip().lower() == 'true'
        if isinstance(_use_terrain_paging, SDFError):
            return _use_terrain_paging
        if _use_terrain_paging is not None and cmp_version(version, "1.4") < 0:
            if _use_terrain_paging != False:
                return SDFError(f"'use_terrain_paging' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, use_terrain_paging=_use_terrain_paging)


class Sampling(BaseModel):
    def __init__(self, sdf_version: str, sampling: int = 2):
        self.__version__ = sdf_version
        self.sampling = sampling

    def to_version(self, target_version: str) -> "Sampling":
        if self.sampling is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {target_version} (added in 1.6)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2
        _sampling = _parse_uint32(_text)
        if isinstance(_sampling, SDFError):
            return _sampling
        if _sampling is not None and cmp_version(version, "1.6") < 0:
            if _sampling != 2:
                return SDFError(f"'sampling' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, sampling=_sampling)


class Heightmap(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        uri: "Uri" = None,
        size: "Size" = None,
        pos: "Pos" = None,
        texture: List["Texture"] = None,
        blend: List["Blend"] = None,
        use_terrain_paging: "UseTerrainPaging" = None,
        sampling: "Sampling" = None
    ):
        self.__version__ = sdf_version
        self.uri = uri
        self.size = size
        self.pos = pos
        self.texture = texture or []
        self.blend = blend or []
        self.use_terrain_paging = use_terrain_paging
        self.sampling = sampling

    def to_version(self, target_version: str) -> "Heightmap":
        if self.use_terrain_paging is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'use_terrain_paging' is not supported in SDF version {target_version} (added in 1.4)")
        if self.sampling is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        kwargs["pos"] = self.pos.to_version(target_version) if self.pos is not None else None
        kwargs["texture"] = [c.to_version(target_version) for c in (self.texture or [])]
        kwargs["blend"] = [c.to_version(target_version) for c in (self.blend or [])]
        kwargs["use_terrain_paging"] = self.use_terrain_paging.to_version(target_version) if self.use_terrain_paging is not None else None
        kwargs["sampling"] = self.sampling.to_version(target_version) if self.sampling is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("heightmap")
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        if self.pos is not None:
            el.append(self.pos.to_sdf(version))
        for item in (self.texture or []):
            el.append(item.to_sdf(version))
        for item in (self.blend or []):
            el.append(item.to_sdf(version))
        if self.use_terrain_paging is not None:
            el.append(self.use_terrain_paging.to_sdf(version))
        if self.sampling is not None:
            el.append(self.sampling.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        _c_size = el.find("size")
        if _c_size is not None:
            _res = Size._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        _c_pos = el.find("pos")
        if _c_pos is not None:
            _res = Pos._from_sdf(_c_pos, version)
            if isinstance(_res, SDFError):
                return _res.extend("pos")
            _pos = _res
        else:
            _pos = None
        _texture = []
        for c in el.findall("texture"):
            _res = Texture._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("texture")
            _texture.append(_res)
        _blend = []
        for c in el.findall("blend"):
            _res = Blend._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("blend")
            _blend.append(_res)
        _c_use_terrain_paging = el.find("use_terrain_paging")
        if _c_use_terrain_paging is not None:
            _res = UseTerrainPaging._from_sdf(_c_use_terrain_paging, version)
            if isinstance(_res, SDFError):
                return _res.extend("use_terrain_paging")
            _use_terrain_paging = _res
        else:
            _use_terrain_paging = None
        if _use_terrain_paging is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'use_terrain_paging' is not supported in SDF version {version} (added in 1.4)")
        _c_sampling = el.find("sampling")
        if _c_sampling is not None:
            _res = Sampling._from_sdf(_c_sampling, version)
            if isinstance(_res, SDFError):
                return _res.extend("sampling")
            _sampling = _res
        else:
            _sampling = None
        if _sampling is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'sampling' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, uri=_uri, size=_size, pos=_pos, texture=_texture, blend=_blend, use_terrain_paging=_use_terrain_paging, sampling=_sampling)


class Empty(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Point(BaseModel):
    def __init__(self, sdf_version: str, point: _SDFVector2d = None):
        self.__version__ = sdf_version
        if point is None:
            point = _SDFVector2d.from_sdf("0 0")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _point = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_point, SDFError):
            return _point
        return cls(sdf_version=version, point=_point)


class PolylineHeight(BaseModel):
    def __init__(self, sdf_version: str, height: float = 1.0):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "PolylineHeight":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _height = _parse_double(_text)
        if isinstance(_height, SDFError):
            return _height
        return cls(sdf_version=version, height=_height)


class Polyline(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        point: List["Point"] = None,
        height: "PolylineHeight" = None
    ):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _point = []
        for c in el.findall("point"):
            _res = Point._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("point")
            _point.append(_res)
        _c_height = el.find("height")
        if _c_height is not None:
            _res = PolylineHeight._from_sdf(_c_height, version)
            if isinstance(_res, SDFError):
                return _res.extend("height")
            _height = _res
        else:
            _height = None
        return cls(sdf_version=version, point=_point, height=_height)


class Radii(BaseModel):
    def __init__(self, sdf_version: str, radii: _SDFVector3 = None):
        self.__version__ = sdf_version
        if radii is None:
            radii = _SDFVector3.from_sdf("1 1 1")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _radii = _SDFVector3._from_sdf(_text, version)
        if isinstance(_radii, SDFError):
            return _radii
        return cls(sdf_version=version, radii=_radii)


class Ellipsoid(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_radii = el.find("radii")
        if _c_radii is not None:
            _res = Radii._from_sdf(_c_radii, version)
            if isinstance(_res, SDFError):
                return _res.extend("radii")
            _radii = _res
        else:
            _radii = None
        return cls(sdf_version=version, radii=_radii)


class CapsuleRadius(BaseModel):
    def __init__(self, sdf_version: str, radius: float = 0.5):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "CapsuleRadius":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.5
        _radius = _parse_double(_text)
        if isinstance(_radius, SDFError):
            return _radius
        return cls(sdf_version=version, radius=_radius)


class Capsule(BaseModel):
    def __init__(self, sdf_version: str, radius: "CapsuleRadius" = None, length: "Length" = None):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_radius = el.find("radius")
        if _c_radius is not None:
            _res = CapsuleRadius._from_sdf(_c_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("radius")
            _radius = _res
        else:
            _radius = None
        _c_length = el.find("length")
        if _c_length is not None:
            _res = Length._from_sdf(_c_length, version)
            if isinstance(_res, SDFError):
                return _res.extend("length")
            _length = _res
        else:
            _length = None
        return cls(sdf_version=version, radius=_radius, length=_length)


class Geometry(BaseModel):
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
        ellipsoid: "Ellipsoid" = None,
        capsule: "Capsule" = None
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
        self.ellipsoid = ellipsoid
        self.capsule = capsule

    def to_version(self, target_version: str) -> "Geometry":
        if self.empty is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'empty' is not supported in SDF version {target_version} (added in 1.3)")
        if self.polyline is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'polyline' is not supported in SDF version {target_version} (added in 1.5)")
        if self.ellipsoid is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'ellipsoid' is not supported in SDF version {target_version} (added in 1.8)")
        if self.capsule is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'capsule' is not supported in SDF version {target_version} (added in 1.8)")
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
        kwargs["ellipsoid"] = self.ellipsoid.to_version(target_version) if self.ellipsoid is not None else None
        kwargs["capsule"] = self.capsule.to_version(target_version) if self.capsule is not None else None
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
        if self.ellipsoid is not None:
            el.append(self.ellipsoid.to_sdf(version))
        if self.capsule is not None:
            el.append(self.capsule.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_box = el.find("box")
        if _c_box is not None:
            _res = Box._from_sdf(_c_box, version)
            if isinstance(_res, SDFError):
                return _res.extend("box")
            _box = _res
        else:
            _box = None
        _c_sphere = el.find("sphere")
        if _c_sphere is not None:
            _res = Sphere._from_sdf(_c_sphere, version)
            if isinstance(_res, SDFError):
                return _res.extend("sphere")
            _sphere = _res
        else:
            _sphere = None
        _c_cylinder = el.find("cylinder")
        if _c_cylinder is not None:
            _res = Cylinder._from_sdf(_c_cylinder, version)
            if isinstance(_res, SDFError):
                return _res.extend("cylinder")
            _cylinder = _res
        else:
            _cylinder = None
        _c_mesh = el.find("mesh")
        if _c_mesh is not None:
            _res = Mesh._from_sdf(_c_mesh, version)
            if isinstance(_res, SDFError):
                return _res.extend("mesh")
            _mesh = _res
        else:
            _mesh = None
        _c_plane = el.find("plane")
        if _c_plane is not None:
            _res = Plane._from_sdf(_c_plane, version)
            if isinstance(_res, SDFError):
                return _res.extend("plane")
            _plane = _res
        else:
            _plane = None
        _c_image = el.find("image")
        if _c_image is not None:
            _res = Image._from_sdf(_c_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        else:
            _image = None
        _c_heightmap = el.find("heightmap")
        if _c_heightmap is not None:
            _res = Heightmap._from_sdf(_c_heightmap, version)
            if isinstance(_res, SDFError):
                return _res.extend("heightmap")
            _heightmap = _res
        else:
            _heightmap = None
        _c_empty = el.find("empty")
        if _c_empty is not None:
            _res = Empty._from_sdf(_c_empty, version)
            if isinstance(_res, SDFError):
                return _res.extend("empty")
            _empty = _res
        else:
            _empty = None
        if _empty is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'empty' is not supported in SDF version {version} (added in 1.3)")
        _c_polyline = el.find("polyline")
        if _c_polyline is not None:
            _res = Polyline._from_sdf(_c_polyline, version)
            if isinstance(_res, SDFError):
                return _res.extend("polyline")
            _polyline = _res
        else:
            _polyline = None
        if _polyline is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'polyline' is not supported in SDF version {version} (added in 1.5)")
        _c_ellipsoid = el.find("ellipsoid")
        if _c_ellipsoid is not None:
            _res = Ellipsoid._from_sdf(_c_ellipsoid, version)
            if isinstance(_res, SDFError):
                return _res.extend("ellipsoid")
            _ellipsoid = _res
        else:
            _ellipsoid = None
        if _ellipsoid is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'ellipsoid' is not supported in SDF version {version} (added in 1.8)")
        _c_capsule = el.find("capsule")
        if _c_capsule is not None:
            _res = Capsule._from_sdf(_c_capsule, version)
            if isinstance(_res, SDFError):
                return _res.extend("capsule")
            _capsule = _res
        else:
            _capsule = None
        if _capsule is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'capsule' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, box=_box, sphere=_sphere, cylinder=_cylinder, mesh=_mesh, plane=_plane, image=_image, heightmap=_heightmap, empty=_empty, polyline=_polyline, ellipsoid=_ellipsoid, capsule=_capsule)


class RestitutionCoefficient(BaseModel):
    def __init__(self, sdf_version: str, restitution_coefficient: float = 0):
        self.__version__ = sdf_version
        self.restitution_coefficient = restitution_coefficient

    def to_version(self, target_version: str) -> "RestitutionCoefficient":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _restitution_coefficient = _parse_double(_text)
        if isinstance(_restitution_coefficient, SDFError):
            return _restitution_coefficient
        return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient)


class BounceThreshold(BaseModel):
    def __init__(self, sdf_version: str, threshold: float = 100000):
        self.__version__ = sdf_version
        self.threshold = threshold

    def to_version(self, target_version: str) -> "BounceThreshold":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100000
        _threshold = _parse_double(_text)
        if isinstance(_threshold, SDFError):
            return _threshold
        return cls(sdf_version=version, threshold=_threshold)


class Bounce(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        restitution_coefficient: "RestitutionCoefficient" = None,
        threshold: "BounceThreshold" = None
    ):
        self.__version__ = sdf_version
        self.restitution_coefficient = restitution_coefficient
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Bounce":
        kwargs = {"sdf_version": target_version}
        kwargs["restitution_coefficient"] = self.restitution_coefficient.to_version(target_version) if self.restitution_coefficient is not None else None
        kwargs["threshold"] = self.threshold.to_version(target_version) if self.threshold is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bounce")
        if self.restitution_coefficient is not None:
            el.append(self.restitution_coefficient.to_sdf(version))
        if self.threshold is not None:
            el.append(self.threshold.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_restitution_coefficient = el.find("restitution_coefficient")
        if _c_restitution_coefficient is not None:
            _res = RestitutionCoefficient._from_sdf(_c_restitution_coefficient, version)
            if isinstance(_res, SDFError):
                return _res.extend("restitution_coefficient")
            _restitution_coefficient = _res
        else:
            _restitution_coefficient = None
        _c_threshold = el.find("threshold")
        if _c_threshold is not None:
            _res = BounceThreshold._from_sdf(_c_threshold, version)
            if isinstance(_res, SDFError):
                return _res.extend("threshold")
            _threshold = _res
        else:
            _threshold = None
        return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient, threshold=_threshold)


class Mu(BaseModel):
    def __init__(self, sdf_version: str, mu: float = -1):
        self.__version__ = sdf_version
        self.mu = mu

    def to_version(self, target_version: str) -> "Mu":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -1
        _mu = _parse_double(_text)
        if isinstance(_mu, SDFError):
            return _mu
        return cls(sdf_version=version, mu=_mu)


class Mu2(BaseModel):
    def __init__(self, sdf_version: str, mu2: float = -1):
        self.__version__ = sdf_version
        self.mu2 = mu2

    def to_version(self, target_version: str) -> "Mu2":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -1
        _mu2 = _parse_double(_text)
        if isinstance(_mu2, SDFError):
            return _mu2
        return cls(sdf_version=version, mu2=_mu2)


class Fdir1(BaseModel):
    def __init__(self, sdf_version: str, fdir1: _SDFVector3 = None):
        self.__version__ = sdf_version
        if fdir1 is None:
            fdir1 = _SDFVector3.from_sdf("0 0 0")
        self.fdir1 = fdir1

    def to_version(self, target_version: str) -> "Fdir1":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _fdir1 = _SDFVector3._from_sdf(_text, version)
        if isinstance(_fdir1, SDFError):
            return _fdir1
        return cls(sdf_version=version, fdir1=_fdir1)


class Slip1(BaseModel):
    def __init__(self, sdf_version: str, slip1: float = 0.0):
        self.__version__ = sdf_version
        self.slip1 = slip1

    def to_version(self, target_version: str) -> "Slip1":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _slip1 = _parse_double(_text)
        if isinstance(_slip1, SDFError):
            return _slip1
        return cls(sdf_version=version, slip1=_slip1)


class Slip2(BaseModel):
    def __init__(self, sdf_version: str, slip2: float = 0.0):
        self.__version__ = sdf_version
        self.slip2 = slip2

    def to_version(self, target_version: str) -> "Slip2":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _slip2 = _parse_double(_text)
        if isinstance(_slip2, SDFError):
            return _slip2
        return cls(sdf_version=version, slip2=_slip2)


class Ode(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        mu: "Mu" = None,
        mu2: "Mu2" = None,
        fdir1: "Fdir1" = None,
        slip1: "Slip1" = None,
        slip2: "Slip2" = None
    ):
        self.__version__ = sdf_version
        self.mu = mu
        self.mu2 = mu2
        self.fdir1 = fdir1
        self.slip1 = slip1
        self.slip2 = slip2

    def to_version(self, target_version: str) -> "Ode":
        kwargs = {"sdf_version": target_version}
        kwargs["mu"] = self.mu.to_version(target_version) if self.mu is not None else None
        kwargs["mu2"] = self.mu2.to_version(target_version) if self.mu2 is not None else None
        kwargs["fdir1"] = self.fdir1.to_version(target_version) if self.fdir1 is not None else None
        kwargs["slip1"] = self.slip1.to_version(target_version) if self.slip1 is not None else None
        kwargs["slip2"] = self.slip2.to_version(target_version) if self.slip2 is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.mu is not None:
            el.append(self.mu.to_sdf(version))
        if self.mu2 is not None:
            el.append(self.mu2.to_sdf(version))
        if self.fdir1 is not None:
            el.append(self.fdir1.to_sdf(version))
        if self.slip1 is not None:
            el.append(self.slip1.to_sdf(version))
        if self.slip2 is not None:
            el.append(self.slip2.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_mu = el.find("mu")
        if _c_mu is not None:
            _res = Mu._from_sdf(_c_mu, version)
            if isinstance(_res, SDFError):
                return _res.extend("mu")
            _mu = _res
        else:
            _mu = None
        _c_mu2 = el.find("mu2")
        if _c_mu2 is not None:
            _res = Mu2._from_sdf(_c_mu2, version)
            if isinstance(_res, SDFError):
                return _res.extend("mu2")
            _mu2 = _res
        else:
            _mu2 = None
        _c_fdir1 = el.find("fdir1")
        if _c_fdir1 is not None:
            _res = Fdir1._from_sdf(_c_fdir1, version)
            if isinstance(_res, SDFError):
                return _res.extend("fdir1")
            _fdir1 = _res
        else:
            _fdir1 = None
        _c_slip1 = el.find("slip1")
        if _c_slip1 is not None:
            _res = Slip1._from_sdf(_c_slip1, version)
            if isinstance(_res, SDFError):
                return _res.extend("slip1")
            _slip1 = _res
        else:
            _slip1 = None
        _c_slip2 = el.find("slip2")
        if _c_slip2 is not None:
            _res = Slip2._from_sdf(_c_slip2, version)
            if isinstance(_res, SDFError):
                return _res.extend("slip2")
            _slip2 = _res
        else:
            _slip2 = None
        return cls(sdf_version=version, mu=_mu, mu2=_mu2, fdir1=_fdir1, slip1=_slip1, slip2=_slip2)


class BulletFriction(BaseModel):
    def __init__(self, sdf_version: str, friction: float = 1):
        self.__version__ = sdf_version
        self.friction = friction

    def to_version(self, target_version: str) -> "BulletFriction":
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
        _text = el.text or 1
        _friction = _parse_double(_text)
        if isinstance(_friction, SDFError):
            return _friction
        return cls(sdf_version=version, friction=_friction)


class Friction2(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _friction2 = _parse_double(_text)
        if isinstance(_friction2, SDFError):
            return _friction2
        return cls(sdf_version=version, friction2=_friction2)


class RollingFriction(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _rolling_friction = _parse_double(_text)
        if isinstance(_rolling_friction, SDFError):
            return _rolling_friction
        return cls(sdf_version=version, rolling_friction=_rolling_friction)


class Bullet(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        friction: "BulletFriction" = None,
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_friction = el.find("friction")
        if _c_friction is not None:
            _res = BulletFriction._from_sdf(_c_friction, version)
            if isinstance(_res, SDFError):
                return _res.extend("friction")
            _friction = _res
        else:
            _friction = None
        _c_friction2 = el.find("friction2")
        if _c_friction2 is not None:
            _res = Friction2._from_sdf(_c_friction2, version)
            if isinstance(_res, SDFError):
                return _res.extend("friction2")
            _friction2 = _res
        else:
            _friction2 = None
        _c_fdir1 = el.find("fdir1")
        if _c_fdir1 is not None:
            _res = Fdir1._from_sdf(_c_fdir1, version)
            if isinstance(_res, SDFError):
                return _res.extend("fdir1")
            _fdir1 = _res
        else:
            _fdir1 = None
        _c_rolling_friction = el.find("rolling_friction")
        if _c_rolling_friction is not None:
            _res = RollingFriction._from_sdf(_c_rolling_friction, version)
            if isinstance(_res, SDFError):
                return _res.extend("rolling_friction")
            _rolling_friction = _res
        else:
            _rolling_friction = None
        return cls(sdf_version=version, friction=_friction, friction2=_friction2, fdir1=_fdir1, rolling_friction=_rolling_friction)


class Coefficient(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _coefficient = _parse_double(_text)
        if isinstance(_coefficient, SDFError):
            return _coefficient
        return cls(sdf_version=version, coefficient=_coefficient)


class UsePatchRadius(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _use_patch_radius = str(_text).strip().lower() == 'true'
        if isinstance(_use_patch_radius, SDFError):
            return _use_patch_radius
        return cls(sdf_version=version, use_patch_radius=_use_patch_radius)


class PatchRadius(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _patch_radius = _parse_double(_text)
        if isinstance(_patch_radius, SDFError):
            return _patch_radius
        return cls(sdf_version=version, patch_radius=_patch_radius)


class SurfaceRadius(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _surface_radius = _parse_double(_text)
        if isinstance(_surface_radius, SDFError):
            return _surface_radius
        return cls(sdf_version=version, surface_radius=_surface_radius)


class Slip(BaseModel):
    def __init__(self, sdf_version: str, slip: float = 0.0):
        self.__version__ = sdf_version
        self.slip = slip

    def to_version(self, target_version: str) -> "Slip":
        kwargs = {"sdf_version": target_version}
        kwargs["slip"] = self.slip
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("slip")
        if self.slip is not None:
            el.text = str(self.slip)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _slip = _parse_double(_text)
        if isinstance(_slip, SDFError):
            return _slip
        return cls(sdf_version=version, slip=_slip)


class TorsionalOde(BaseModel):
    def __init__(self, sdf_version: str, slip: "Slip" = None):
        self.__version__ = sdf_version
        self.slip = slip

    def to_version(self, target_version: str) -> "TorsionalOde":
        kwargs = {"sdf_version": target_version}
        kwargs["slip"] = self.slip.to_version(target_version) if self.slip is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.slip is not None:
            el.append(self.slip.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_slip = el.find("slip")
        if _c_slip is not None:
            _res = Slip._from_sdf(_c_slip, version)
            if isinstance(_res, SDFError):
                return _res.extend("slip")
            _slip = _res
        else:
            _slip = None
        return cls(sdf_version=version, slip=_slip)


class Torsional(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        coefficient: "Coefficient" = None,
        use_patch_radius: "UsePatchRadius" = None,
        patch_radius: "PatchRadius" = None,
        surface_radius: "SurfaceRadius" = None,
        ode: "TorsionalOde" = None
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_coefficient = el.find("coefficient")
        if _c_coefficient is not None:
            _res = Coefficient._from_sdf(_c_coefficient, version)
            if isinstance(_res, SDFError):
                return _res.extend("coefficient")
            _coefficient = _res
        else:
            _coefficient = None
        _c_use_patch_radius = el.find("use_patch_radius")
        if _c_use_patch_radius is not None:
            _res = UsePatchRadius._from_sdf(_c_use_patch_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("use_patch_radius")
            _use_patch_radius = _res
        else:
            _use_patch_radius = None
        _c_patch_radius = el.find("patch_radius")
        if _c_patch_radius is not None:
            _res = PatchRadius._from_sdf(_c_patch_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("patch_radius")
            _patch_radius = _res
        else:
            _patch_radius = None
        _c_surface_radius = el.find("surface_radius")
        if _c_surface_radius is not None:
            _res = SurfaceRadius._from_sdf(_c_surface_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("surface_radius")
            _surface_radius = _res
        else:
            _surface_radius = None
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = TorsionalOde._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        return cls(sdf_version=version, coefficient=_coefficient, use_patch_radius=_use_patch_radius, patch_radius=_patch_radius, surface_radius=_surface_radius, ode=_ode)


class Friction(BaseModel):
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
        if self.torsional is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'torsional' is not supported in SDF version {target_version} (added in 1.5)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = Ode._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        _c_bullet = el.find("bullet")
        if _c_bullet is not None:
            _res = Bullet._from_sdf(_c_bullet, version)
            if isinstance(_res, SDFError):
                return _res.extend("bullet")
            _bullet = _res
        else:
            _bullet = None
        if _bullet is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
        _c_torsional = el.find("torsional")
        if _c_torsional is not None:
            _res = Torsional._from_sdf(_c_torsional, version)
            if isinstance(_res, SDFError):
                return _res.extend("torsional")
            _torsional = _res
        else:
            _torsional = None
        if _torsional is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'torsional' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, ode=_ode, bullet=_bullet, torsional=_torsional)


class SoftCfm(BaseModel):
    def __init__(self, sdf_version: str, soft_cfm: float = 0):
        self.__version__ = sdf_version
        self.soft_cfm = soft_cfm

    def to_version(self, target_version: str) -> "SoftCfm":
        kwargs = {"sdf_version": target_version}
        kwargs["soft_cfm"] = self.soft_cfm
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("soft_cfm")
        if self.soft_cfm is not None:
            el.text = str(self.soft_cfm)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _soft_cfm = _parse_double(_text)
        if isinstance(_soft_cfm, SDFError):
            return _soft_cfm
        return cls(sdf_version=version, soft_cfm=_soft_cfm)


class SoftErp(BaseModel):
    def __init__(self, sdf_version: str, soft_erp: float = 0.2):
        self.__version__ = sdf_version
        self.soft_erp = soft_erp

    def to_version(self, target_version: str) -> "SoftErp":
        kwargs = {"sdf_version": target_version}
        kwargs["soft_erp"] = self.soft_erp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("soft_erp")
        if self.soft_erp is not None:
            el.text = str(self.soft_erp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.2
        _soft_erp = _parse_double(_text)
        if isinstance(_soft_erp, SDFError):
            return _soft_erp
        return cls(sdf_version=version, soft_erp=_soft_erp)


class Kp(BaseModel):
    def __init__(self, sdf_version: str, kp: float = 1000000000000.0):
        self.__version__ = sdf_version
        self.kp = kp

    def to_version(self, target_version: str) -> "Kp":
        kwargs = {"sdf_version": target_version}
        kwargs["kp"] = self.kp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("kp")
        if self.kp is not None:
            el.text = str(self.kp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1000000000000.0
        _kp = _parse_double(_text)
        if isinstance(_kp, SDFError):
            return _kp
        return cls(sdf_version=version, kp=_kp)


class Kd(BaseModel):
    def __init__(self, sdf_version: str, kd: float = 1.0):
        self.__version__ = sdf_version
        self.kd = kd

    def to_version(self, target_version: str) -> "Kd":
        kwargs = {"sdf_version": target_version}
        kwargs["kd"] = self.kd
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("kd")
        if self.kd is not None:
            el.text = str(self.kd)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _kd = _parse_double(_text)
        if isinstance(_kd, SDFError):
            return _kd
        return cls(sdf_version=version, kd=_kd)


class MaxVel(BaseModel):
    def __init__(self, sdf_version: str, max_vel: float = 0.01):
        self.__version__ = sdf_version
        self.max_vel = max_vel

    def to_version(self, target_version: str) -> "MaxVel":
        kwargs = {"sdf_version": target_version}
        kwargs["max_vel"] = self.max_vel
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_vel")
        if self.max_vel is not None:
            el.text = str(self.max_vel)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.01
        _max_vel = _parse_double(_text)
        if isinstance(_max_vel, SDFError):
            return _max_vel
        return cls(sdf_version=version, max_vel=_max_vel)


class MinDepth(BaseModel):
    def __init__(self, sdf_version: str, min_depth: float = 0):
        self.__version__ = sdf_version
        self.min_depth = min_depth

    def to_version(self, target_version: str) -> "MinDepth":
        kwargs = {"sdf_version": target_version}
        kwargs["min_depth"] = self.min_depth
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_depth")
        if self.min_depth is not None:
            el.text = str(self.min_depth)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min_depth = _parse_double(_text)
        if isinstance(_min_depth, SDFError):
            return _min_depth
        return cls(sdf_version=version, min_depth=_min_depth)


class ContactOde(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        soft_cfm: "SoftCfm" = None,
        soft_erp: "SoftErp" = None,
        kp: "Kp" = None,
        kd: "Kd" = None,
        max_vel: "MaxVel" = None,
        min_depth: "MinDepth" = None
    ):
        self.__version__ = sdf_version
        self.soft_cfm = soft_cfm
        self.soft_erp = soft_erp
        self.kp = kp
        self.kd = kd
        self.max_vel = max_vel
        self.min_depth = min_depth

    def to_version(self, target_version: str) -> "ContactOde":
        kwargs = {"sdf_version": target_version}
        kwargs["soft_cfm"] = self.soft_cfm.to_version(target_version) if self.soft_cfm is not None else None
        kwargs["soft_erp"] = self.soft_erp.to_version(target_version) if self.soft_erp is not None else None
        kwargs["kp"] = self.kp.to_version(target_version) if self.kp is not None else None
        kwargs["kd"] = self.kd.to_version(target_version) if self.kd is not None else None
        kwargs["max_vel"] = self.max_vel.to_version(target_version) if self.max_vel is not None else None
        kwargs["min_depth"] = self.min_depth.to_version(target_version) if self.min_depth is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.soft_cfm is not None:
            el.append(self.soft_cfm.to_sdf(version))
        if self.soft_erp is not None:
            el.append(self.soft_erp.to_sdf(version))
        if self.kp is not None:
            el.append(self.kp.to_sdf(version))
        if self.kd is not None:
            el.append(self.kd.to_sdf(version))
        if self.max_vel is not None:
            el.append(self.max_vel.to_sdf(version))
        if self.min_depth is not None:
            el.append(self.min_depth.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_soft_cfm = el.find("soft_cfm")
        if _c_soft_cfm is not None:
            _res = SoftCfm._from_sdf(_c_soft_cfm, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_cfm")
            _soft_cfm = _res
        else:
            _soft_cfm = None
        _c_soft_erp = el.find("soft_erp")
        if _c_soft_erp is not None:
            _res = SoftErp._from_sdf(_c_soft_erp, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_erp")
            _soft_erp = _res
        else:
            _soft_erp = None
        _c_kp = el.find("kp")
        if _c_kp is not None:
            _res = Kp._from_sdf(_c_kp, version)
            if isinstance(_res, SDFError):
                return _res.extend("kp")
            _kp = _res
        else:
            _kp = None
        _c_kd = el.find("kd")
        if _c_kd is not None:
            _res = Kd._from_sdf(_c_kd, version)
            if isinstance(_res, SDFError):
                return _res.extend("kd")
            _kd = _res
        else:
            _kd = None
        _c_max_vel = el.find("max_vel")
        if _c_max_vel is not None:
            _res = MaxVel._from_sdf(_c_max_vel, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_vel")
            _max_vel = _res
        else:
            _max_vel = None
        _c_min_depth = el.find("min_depth")
        if _c_min_depth is not None:
            _res = MinDepth._from_sdf(_c_min_depth, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_depth")
            _min_depth = _res
        else:
            _min_depth = None
        return cls(sdf_version=version, soft_cfm=_soft_cfm, soft_erp=_soft_erp, kp=_kp, kd=_kd, max_vel=_max_vel, min_depth=_min_depth)


class CollideBitmask(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _collide_bitmask = _parse_uint32(_text)
        if isinstance(_collide_bitmask, SDFError):
            return _collide_bitmask
        if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
            if _collide_bitmask != 1:
                return SDFError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_bitmask=_collide_bitmask)


class SplitImpulse(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _split_impulse = str(_text).strip().lower() == 'true'
        if isinstance(_split_impulse, SDFError):
            return _split_impulse
        return cls(sdf_version=version, split_impulse=_split_impulse)


class SplitImpulsePenetrationThreshold(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -0.01
        _split_impulse_penetration_threshold = _parse_double(_text)
        if isinstance(_split_impulse_penetration_threshold, SDFError):
            return _split_impulse_penetration_threshold
        return cls(sdf_version=version, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)


class ContactBullet(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        soft_cfm: "SoftCfm" = None,
        soft_erp: "SoftErp" = None,
        kp: "Kp" = None,
        kd: "Kd" = None,
        split_impulse: "SplitImpulse" = None,
        split_impulse_penetration_threshold: "SplitImpulsePenetrationThreshold" = None
    ):
        self.__version__ = sdf_version
        self.soft_cfm = soft_cfm
        self.soft_erp = soft_erp
        self.kp = kp
        self.kd = kd
        self.split_impulse = split_impulse
        self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

    def to_version(self, target_version: str) -> "ContactBullet":
        kwargs = {"sdf_version": target_version}
        kwargs["soft_cfm"] = self.soft_cfm.to_version(target_version) if self.soft_cfm is not None else None
        kwargs["soft_erp"] = self.soft_erp.to_version(target_version) if self.soft_erp is not None else None
        kwargs["kp"] = self.kp.to_version(target_version) if self.kp is not None else None
        kwargs["kd"] = self.kd.to_version(target_version) if self.kd is not None else None
        kwargs["split_impulse"] = self.split_impulse.to_version(target_version) if self.split_impulse is not None else None
        kwargs["split_impulse_penetration_threshold"] = self.split_impulse_penetration_threshold.to_version(target_version) if self.split_impulse_penetration_threshold is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bullet")
        if self.soft_cfm is not None:
            el.append(self.soft_cfm.to_sdf(version))
        if self.soft_erp is not None:
            el.append(self.soft_erp.to_sdf(version))
        if self.kp is not None:
            el.append(self.kp.to_sdf(version))
        if self.kd is not None:
            el.append(self.kd.to_sdf(version))
        if self.split_impulse is not None:
            el.append(self.split_impulse.to_sdf(version))
        if self.split_impulse_penetration_threshold is not None:
            el.append(self.split_impulse_penetration_threshold.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_soft_cfm = el.find("soft_cfm")
        if _c_soft_cfm is not None:
            _res = SoftCfm._from_sdf(_c_soft_cfm, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_cfm")
            _soft_cfm = _res
        else:
            _soft_cfm = None
        _c_soft_erp = el.find("soft_erp")
        if _c_soft_erp is not None:
            _res = SoftErp._from_sdf(_c_soft_erp, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_erp")
            _soft_erp = _res
        else:
            _soft_erp = None
        _c_kp = el.find("kp")
        if _c_kp is not None:
            _res = Kp._from_sdf(_c_kp, version)
            if isinstance(_res, SDFError):
                return _res.extend("kp")
            _kp = _res
        else:
            _kp = None
        _c_kd = el.find("kd")
        if _c_kd is not None:
            _res = Kd._from_sdf(_c_kd, version)
            if isinstance(_res, SDFError):
                return _res.extend("kd")
            _kd = _res
        else:
            _kd = None
        _c_split_impulse = el.find("split_impulse")
        if _c_split_impulse is not None:
            _res = SplitImpulse._from_sdf(_c_split_impulse, version)
            if isinstance(_res, SDFError):
                return _res.extend("split_impulse")
            _split_impulse = _res
        else:
            _split_impulse = None
        _c_split_impulse_penetration_threshold = el.find("split_impulse_penetration_threshold")
        if _c_split_impulse_penetration_threshold is not None:
            _res = SplitImpulsePenetrationThreshold._from_sdf(_c_split_impulse_penetration_threshold, version)
            if isinstance(_res, SDFError):
                return _res.extend("split_impulse_penetration_threshold")
            _split_impulse_penetration_threshold = _res
        else:
            _split_impulse_penetration_threshold = None
        return cls(sdf_version=version, soft_cfm=_soft_cfm, soft_erp=_soft_erp, kp=_kp, kd=_kd, split_impulse=_split_impulse, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)


class CollideWithoutContactBitmask(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _collide_without_contact_bitmask = _parse_uint32(_text)
        if isinstance(_collide_without_contact_bitmask, SDFError):
            return _collide_without_contact_bitmask
        if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
            if _collide_without_contact_bitmask != 1:
                return SDFError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_without_contact_bitmask=_collide_without_contact_bitmask)


class CollideWithoutContact(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _collide_without_contact = str(_text).strip().lower() == 'true'
        if isinstance(_collide_without_contact, SDFError):
            return _collide_without_contact
        if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
            if _collide_without_contact != False:
                return SDFError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_without_contact=_collide_without_contact)


class ElasticModulus(BaseModel):
    def __init__(self, sdf_version: str, elastic_modulus: float = -1):
        self.__version__ = sdf_version
        self.elastic_modulus = elastic_modulus

    def to_version(self, target_version: str) -> "ElasticModulus":
        if self.elastic_modulus is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.5)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -1
        _elastic_modulus = _parse_double(_text)
        if isinstance(_elastic_modulus, SDFError):
            return _elastic_modulus
        if _elastic_modulus is not None and cmp_version(version, "1.5") < 0:
            if _elastic_modulus != -1:
                return SDFError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, elastic_modulus=_elastic_modulus)


class PoissonsRatio(BaseModel):
    def __init__(self, sdf_version: str, poissons_ratio: float = 0.3):
        self.__version__ = sdf_version
        self.poissons_ratio = poissons_ratio

    def to_version(self, target_version: str) -> "PoissonsRatio":
        if self.poissons_ratio is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.5)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.3
        _poissons_ratio = _parse_double(_text)
        if isinstance(_poissons_ratio, SDFError):
            return _poissons_ratio
        if _poissons_ratio is not None and cmp_version(version, "1.5") < 0:
            if _poissons_ratio != 0.3:
                return SDFError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, poissons_ratio=_poissons_ratio)


class CategoryBitmask(BaseModel):
    def __init__(self, sdf_version: str, category_bitmask: int = 65535):
        self.__version__ = sdf_version
        self.category_bitmask = category_bitmask

    def to_version(self, target_version: str) -> "CategoryBitmask":
        if self.category_bitmask is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.6)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 65535
        _category_bitmask = _parse_uint32(_text)
        if isinstance(_category_bitmask, SDFError):
            return _category_bitmask
        if _category_bitmask is not None and cmp_version(version, "1.6") < 0:
            if _category_bitmask != 65535:
                return SDFError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, category_bitmask=_category_bitmask)


class Contact(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        ode: "ContactOde" = None,
        collide_bitmask: "CollideBitmask" = None,
        bullet: "ContactBullet" = None,
        collide_without_contact_bitmask: "CollideWithoutContactBitmask" = None,
        collide_without_contact: "CollideWithoutContact" = None,
        elastic_modulus: "ElasticModulus" = None,
        poissons_ratio: "PoissonsRatio" = None,
        category_bitmask: "CategoryBitmask" = None
    ):
        self.__version__ = sdf_version
        self.ode = ode
        self.collide_bitmask = collide_bitmask
        self.bullet = bullet
        self.collide_without_contact_bitmask = collide_without_contact_bitmask
        self.collide_without_contact = collide_without_contact
        self.elastic_modulus = elastic_modulus
        self.poissons_ratio = poissons_ratio
        self.category_bitmask = category_bitmask

    def to_version(self, target_version: str) -> "Contact":
        if self.collide_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
        if self.collide_without_contact_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        if self.collide_without_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {target_version} (added in 1.4)")
        if self.elastic_modulus is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.5)")
        if self.poissons_ratio is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.5)")
        if self.category_bitmask is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["collide_bitmask"] = self.collide_bitmask.to_version(target_version) if self.collide_bitmask is not None else None
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["collide_without_contact_bitmask"] = self.collide_without_contact_bitmask.to_version(target_version) if self.collide_without_contact_bitmask is not None else None
        kwargs["collide_without_contact"] = self.collide_without_contact.to_version(target_version) if self.collide_without_contact is not None else None
        kwargs["elastic_modulus"] = self.elastic_modulus.to_version(target_version) if self.elastic_modulus is not None else None
        kwargs["poissons_ratio"] = self.poissons_ratio.to_version(target_version) if self.poissons_ratio is not None else None
        kwargs["category_bitmask"] = self.category_bitmask.to_version(target_version) if self.category_bitmask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.collide_bitmask is not None:
            el.append(self.collide_bitmask.to_sdf(version))
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.collide_without_contact_bitmask is not None:
            el.append(self.collide_without_contact_bitmask.to_sdf(version))
        if self.collide_without_contact is not None:
            el.append(self.collide_without_contact.to_sdf(version))
        if self.elastic_modulus is not None:
            el.append(self.elastic_modulus.to_sdf(version))
        if self.poissons_ratio is not None:
            el.append(self.poissons_ratio.to_sdf(version))
        if self.category_bitmask is not None:
            el.append(self.category_bitmask.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = ContactOde._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        _c_collide_bitmask = el.find("collide_bitmask")
        if _c_collide_bitmask is not None:
            _res = CollideBitmask._from_sdf(_c_collide_bitmask, version)
            if isinstance(_res, SDFError):
                return _res.extend("collide_bitmask")
            _collide_bitmask = _res
        else:
            _collide_bitmask = None
        if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
        _c_bullet = el.find("bullet")
        if _c_bullet is not None:
            _res = ContactBullet._from_sdf(_c_bullet, version)
            if isinstance(_res, SDFError):
                return _res.extend("bullet")
            _bullet = _res
        else:
            _bullet = None
        if _bullet is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
        _c_collide_without_contact_bitmask = el.find("collide_without_contact_bitmask")
        if _c_collide_without_contact_bitmask is not None:
            _res = CollideWithoutContactBitmask._from_sdf(_c_collide_without_contact_bitmask, version)
            if isinstance(_res, SDFError):
                return _res.extend("collide_without_contact_bitmask")
            _collide_without_contact_bitmask = _res
        else:
            _collide_without_contact_bitmask = None
        if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
        _c_collide_without_contact = el.find("collide_without_contact")
        if _c_collide_without_contact is not None:
            _res = CollideWithoutContact._from_sdf(_c_collide_without_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("collide_without_contact")
            _collide_without_contact = _res
        else:
            _collide_without_contact = None
        if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
        _c_elastic_modulus = el.find("elastic_modulus")
        if _c_elastic_modulus is not None:
            _res = ElasticModulus._from_sdf(_c_elastic_modulus, version)
            if isinstance(_res, SDFError):
                return _res.extend("elastic_modulus")
            _elastic_modulus = _res
        else:
            _elastic_modulus = None
        if _elastic_modulus is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.5)")
        _c_poissons_ratio = el.find("poissons_ratio")
        if _c_poissons_ratio is not None:
            _res = PoissonsRatio._from_sdf(_c_poissons_ratio, version)
            if isinstance(_res, SDFError):
                return _res.extend("poissons_ratio")
            _poissons_ratio = _res
        else:
            _poissons_ratio = None
        if _poissons_ratio is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.5)")
        _c_category_bitmask = el.find("category_bitmask")
        if _c_category_bitmask is not None:
            _res = CategoryBitmask._from_sdf(_c_category_bitmask, version)
            if isinstance(_res, SDFError):
                return _res.extend("category_bitmask")
            _category_bitmask = _res
        else:
            _category_bitmask = None
        if _category_bitmask is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, ode=_ode, collide_bitmask=_collide_bitmask, bullet=_bullet, collide_without_contact_bitmask=_collide_without_contact_bitmask, collide_without_contact=_collide_without_contact, elastic_modulus=_elastic_modulus, poissons_ratio=_poissons_ratio, category_bitmask=_category_bitmask)


class BoneAttachment(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100.0
        _bone_attachment = _parse_double(_text)
        if isinstance(_bone_attachment, SDFError):
            return _bone_attachment
        return cls(sdf_version=version, bone_attachment=_bone_attachment)


class Stiffness(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100.0
        _stiffness = _parse_double(_text)
        if isinstance(_stiffness, SDFError):
            return _stiffness
        return cls(sdf_version=version, stiffness=_stiffness)


class Damping(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10.0
        _damping = _parse_double(_text)
        if isinstance(_damping, SDFError):
            return _damping
        return cls(sdf_version=version, damping=_damping)


class FleshMassFraction(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.05
        _flesh_mass_fraction = _parse_double(_text)
        if isinstance(_flesh_mass_fraction, SDFError):
            return _flesh_mass_fraction
        return cls(sdf_version=version, flesh_mass_fraction=_flesh_mass_fraction)


class Dart(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_bone_attachment = el.find("bone_attachment")
        if _c_bone_attachment is not None:
            _res = BoneAttachment._from_sdf(_c_bone_attachment, version)
            if isinstance(_res, SDFError):
                return _res.extend("bone_attachment")
            _bone_attachment = _res
        else:
            _bone_attachment = None
        _c_stiffness = el.find("stiffness")
        if _c_stiffness is not None:
            _res = Stiffness._from_sdf(_c_stiffness, version)
            if isinstance(_res, SDFError):
                return _res.extend("stiffness")
            _stiffness = _res
        else:
            _stiffness = None
        _c_damping = el.find("damping")
        if _c_damping is not None:
            _res = Damping._from_sdf(_c_damping, version)
            if isinstance(_res, SDFError):
                return _res.extend("damping")
            _damping = _res
        else:
            _damping = None
        _c_flesh_mass_fraction = el.find("flesh_mass_fraction")
        if _c_flesh_mass_fraction is not None:
            _res = FleshMassFraction._from_sdf(_c_flesh_mass_fraction, version)
            if isinstance(_res, SDFError):
                return _res.extend("flesh_mass_fraction")
            _flesh_mass_fraction = _res
        else:
            _flesh_mass_fraction = None
        return cls(sdf_version=version, bone_attachment=_bone_attachment, stiffness=_stiffness, damping=_damping, flesh_mass_fraction=_flesh_mass_fraction)


class SoftContact(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_dart = el.find("dart")
        if _c_dart is not None:
            _res = Dart._from_sdf(_c_dart, version)
            if isinstance(_res, SDFError):
                return _res.extend("dart")
            _dart = _res
        else:
            _dart = None
        return cls(sdf_version=version, dart=_dart)


class Surface(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_bounce = el.find("bounce")
        if _c_bounce is not None:
            _res = Bounce._from_sdf(_c_bounce, version)
            if isinstance(_res, SDFError):
                return _res.extend("bounce")
            _bounce = _res
        else:
            _bounce = None
        _c_friction = el.find("friction")
        if _c_friction is not None:
            _res = Friction._from_sdf(_c_friction, version)
            if isinstance(_res, SDFError):
                return _res.extend("friction")
            _friction = _res
        else:
            _friction = None
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = Contact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _c_soft_contact = el.find("soft_contact")
        if _c_soft_contact is not None:
            _res = SoftContact._from_sdf(_c_soft_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_contact")
            _soft_contact = _res
        else:
            _soft_contact = None
        if _soft_contact is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'soft_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, bounce=_bounce, friction=_friction, contact=_contact, soft_contact=_soft_contact)


class LaserRetro(BaseModel):
    def __init__(self, sdf_version: str, laser_retro: float = 0):
        self.__version__ = sdf_version
        self.laser_retro = laser_retro

    def to_version(self, target_version: str) -> "LaserRetro":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _laser_retro = _parse_double(_text)
        if isinstance(_laser_retro, SDFError):
            return _laser_retro
        return cls(sdf_version=version, laser_retro=_laser_retro)


class MaxContacts(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _max_contacts = _parse_int32(_text)
        if isinstance(_max_contacts, SDFError):
            return _max_contacts
        return cls(sdf_version=version, max_contacts=_max_contacts)


class CollisionPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "CollisionPose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Collision(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        geometry: "Geometry" = None,
        surface: "Surface" = None,
        laser_retro: "LaserRetro" = None,
        max_contacts: "MaxContacts" = None,
        pose: "CollisionPose" = None,
        frame: List["Frame"] = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.geometry = geometry
        self.surface = surface
        self.laser_retro = laser_retro
        self.max_contacts = max_contacts
        self.pose = pose
        self.frame = frame or []

    def to_version(self, target_version: str) -> "Collision":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["surface"] = self.surface.to_version(target_version) if self.surface is not None else None
        kwargs["laser_retro"] = self.laser_retro.to_version(target_version) if self.laser_retro is not None else None
        kwargs["max_contacts"] = self.max_contacts.to_version(target_version) if self.max_contacts is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision")
        if self.name is not None:
            el.set("name", self.name)
        if self.geometry is None:
            self.geometry = Geometry(sdf_version=version)
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.surface is not None:
            el.append(self.surface.to_sdf(version))
        if self.laser_retro is not None:
            el.append(self.laser_retro.to_sdf(version))
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
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
        _c_surface = el.find("surface")
        if _c_surface is not None:
            _res = Surface._from_sdf(_c_surface, version)
            if isinstance(_res, SDFError):
                return _res.extend("surface")
            _surface = _res
        else:
            _surface = None
        _c_laser_retro = el.find("laser_retro")
        if _c_laser_retro is not None:
            _res = LaserRetro._from_sdf(_c_laser_retro, version)
            if isinstance(_res, SDFError):
                return _res.extend("laser_retro")
            _laser_retro = _res
        else:
            _laser_retro = None
        _c_max_contacts = el.find("max_contacts")
        if _c_max_contacts is not None:
            _res = MaxContacts._from_sdf(_c_max_contacts, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_contacts")
            _max_contacts = _res
        else:
            _max_contacts = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = CollisionPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, name=_name, geometry=_geometry, surface=_surface, laser_retro=_laser_retro, max_contacts=_max_contacts, pose=_pose, frame=_frame)


class CastShadows(BaseModel):
    def __init__(self, sdf_version: str, cast_shadows: bool = True):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows

    def to_version(self, target_version: str) -> "CastShadows":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _cast_shadows = str(_text).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows
        return cls(sdf_version=version, cast_shadows=_cast_shadows)


class VisualLaserRetro(BaseModel):
    def __init__(self, sdf_version: str, laser_retro: float = 0.0):
        self.__version__ = sdf_version
        self.laser_retro = laser_retro

    def to_version(self, target_version: str) -> "VisualLaserRetro":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _laser_retro = _parse_double(_text)
        if isinstance(_laser_retro, SDFError):
            return _laser_retro
        return cls(sdf_version=version, laser_retro=_laser_retro)


class Transparency(BaseModel):
    def __init__(self, sdf_version: str, transparency: float = 0.0):
        self.__version__ = sdf_version
        self.transparency = transparency

    def to_version(self, target_version: str) -> "Transparency":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _transparency = _parse_double(_text)
        if isinstance(_transparency, SDFError):
            return _transparency
        return cls(sdf_version=version, transparency=_transparency)


class VisualPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "VisualPose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Script(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        _c_name = el.find("name")
        if _c_name is not None:
            _res = Name._from_sdf(_c_name, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _name = _res
        else:
            _name = None
        return cls(sdf_version=version, uri=_uri, name=_name)


class NormalMap(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _normal_map = _text
        if isinstance(_normal_map, SDFError):
            return _normal_map
        return cls(sdf_version=version, normal_map=_normal_map)


class Shader(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "pixel")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_normal_map = el.find("normal_map")
        if _c_normal_map is not None:
            _res = NormalMap._from_sdf(_c_normal_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal_map")
            _normal_map = _res
        else:
            _normal_map = None
        return cls(sdf_version=version, type=_type, normal_map=_normal_map)


class Ambient(BaseModel):
    def __init__(self, sdf_version: str, ambient: _SDFColor = None):
        self.__version__ = sdf_version
        if ambient is None:
            ambient = _SDFColor.from_sdf("0 0 0 1")
        self.ambient = ambient

    def to_version(self, target_version: str) -> "Ambient":
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _ambient = _SDFColor._from_sdf(_text, version)
        if isinstance(_ambient, SDFError):
            return _ambient
        return cls(sdf_version=version, ambient=_ambient)


class MaterialDiffuse(BaseModel):
    def __init__(self, sdf_version: str, diffuse: _SDFColor = None):
        self.__version__ = sdf_version
        if diffuse is None:
            diffuse = _SDFColor.from_sdf("0 0 0 1")
        self.diffuse = diffuse

    def to_version(self, target_version: str) -> "MaterialDiffuse":
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
            el.text = self.diffuse.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _diffuse = _SDFColor._from_sdf(_text, version)
        if isinstance(_diffuse, SDFError):
            return _diffuse
        return cls(sdf_version=version, diffuse=_diffuse)


class Specular(BaseModel):
    def __init__(self, sdf_version: str, specular: _SDFColor = None):
        self.__version__ = sdf_version
        if specular is None:
            specular = _SDFColor.from_sdf("0 0 0 1")
        self.specular = specular

    def to_version(self, target_version: str) -> "Specular":
        kwargs = {"sdf_version": target_version}
        kwargs["specular"] = self.specular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular")
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _specular = _SDFColor._from_sdf(_text, version)
        if isinstance(_specular, SDFError):
            return _specular
        return cls(sdf_version=version, specular=_specular)


class Emissive(BaseModel):
    def __init__(self, sdf_version: str, emissive: _SDFColor = None):
        self.__version__ = sdf_version
        if emissive is None:
            emissive = _SDFColor.from_sdf("0 0 0 1")
        self.emissive = emissive

    def to_version(self, target_version: str) -> "Emissive":
        kwargs = {"sdf_version": target_version}
        kwargs["emissive"] = self.emissive
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("emissive")
        if self.emissive is not None:
            el.text = self.emissive.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _emissive = _SDFColor._from_sdf(_text, version)
        if isinstance(_emissive, SDFError):
            return _emissive
        return cls(sdf_version=version, emissive=_emissive)


class Lighting(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _lighting = str(_text).strip().lower() == 'true'
        if isinstance(_lighting, SDFError):
            return _lighting
        if _lighting is not None and cmp_version(version, "1.4") < 0:
            if _lighting != True:
                return SDFError(f"'lighting' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, lighting=_lighting)


class AlbedoMap(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _albedo_map = _text
        if isinstance(_albedo_map, SDFError):
            return _albedo_map
        return cls(sdf_version=version, albedo_map=_albedo_map)


class RoughnessMap(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _roughness_map = _text
        if isinstance(_roughness_map, SDFError):
            return _roughness_map
        return cls(sdf_version=version, roughness_map=_roughness_map)


class Roughness(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.5"
        _roughness = _text
        if isinstance(_roughness, SDFError):
            return _roughness
        return cls(sdf_version=version, roughness=_roughness)


class MetalnessMap(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _metalness_map = _text
        if isinstance(_metalness_map, SDFError):
            return _metalness_map
        return cls(sdf_version=version, metalness_map=_metalness_map)


class Metalness(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.5"
        _metalness = _text
        if isinstance(_metalness, SDFError):
            return _metalness
        return cls(sdf_version=version, metalness=_metalness)


class EnvironmentMap(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _environment_map = _text
        if isinstance(_environment_map, SDFError):
            return _environment_map
        return cls(sdf_version=version, environment_map=_environment_map)


class AmbientOcclusionMap(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _ambient_occlusion_map = _text
        if isinstance(_ambient_occlusion_map, SDFError):
            return _ambient_occlusion_map
        return cls(sdf_version=version, ambient_occlusion_map=_ambient_occlusion_map)


class MetalNormalMap(BaseModel):
    def __init__(self, sdf_version: str, normal_map: str = "", type: str = "tangent"):
        self.__version__ = sdf_version
        self.normal_map = normal_map
        self.type = type

    def to_version(self, target_version: str) -> "MetalNormalMap":
        kwargs = {"sdf_version": target_version}
        kwargs["normal_map"] = self.normal_map
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal_map")
        if self.normal_map is not None:
            el.text = self.normal_map
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _normal_map = _text
        if isinstance(_normal_map, SDFError):
            return _normal_map
        _type = el.get("type", "tangent")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, normal_map=_normal_map, type=_type)


class EmissiveMap(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _emissive_map = _text
        if isinstance(_emissive_map, SDFError):
            return _emissive_map
        return cls(sdf_version=version, emissive_map=_emissive_map)


class LightMap(BaseModel):
    def __init__(self, sdf_version: str, light_map: str = "", uv_set: int = 0):
        self.__version__ = sdf_version
        self.light_map = light_map
        self.uv_set = uv_set

    def to_version(self, target_version: str) -> "LightMap":
        if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _light_map = _text
        if isinstance(_light_map, SDFError):
            return _light_map
        if _light_map is not None and cmp_version(version, "1.7") < 0:
            if _light_map != "":
                return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
        _uv_set = _parse_uint32(el.get("uv_set", 0))
        if isinstance(_uv_set, SDFError):
            return _uv_set.extend("@uv_set")
        return cls(sdf_version=version, light_map=_light_map, uv_set=_uv_set)


class Metal(BaseModel):
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
        normal_map: "MetalNormalMap" = None,
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
        if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_albedo_map = el.find("albedo_map")
        if _c_albedo_map is not None:
            _res = AlbedoMap._from_sdf(_c_albedo_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("albedo_map")
            _albedo_map = _res
        else:
            _albedo_map = None
        _c_roughness_map = el.find("roughness_map")
        if _c_roughness_map is not None:
            _res = RoughnessMap._from_sdf(_c_roughness_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("roughness_map")
            _roughness_map = _res
        else:
            _roughness_map = None
        _c_roughness = el.find("roughness")
        if _c_roughness is not None:
            _res = Roughness._from_sdf(_c_roughness, version)
            if isinstance(_res, SDFError):
                return _res.extend("roughness")
            _roughness = _res
        else:
            _roughness = None
        _c_metalness_map = el.find("metalness_map")
        if _c_metalness_map is not None:
            _res = MetalnessMap._from_sdf(_c_metalness_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("metalness_map")
            _metalness_map = _res
        else:
            _metalness_map = None
        _c_metalness = el.find("metalness")
        if _c_metalness is not None:
            _res = Metalness._from_sdf(_c_metalness, version)
            if isinstance(_res, SDFError):
                return _res.extend("metalness")
            _metalness = _res
        else:
            _metalness = None
        _c_environment_map = el.find("environment_map")
        if _c_environment_map is not None:
            _res = EnvironmentMap._from_sdf(_c_environment_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("environment_map")
            _environment_map = _res
        else:
            _environment_map = None
        _c_ambient_occlusion_map = el.find("ambient_occlusion_map")
        if _c_ambient_occlusion_map is not None:
            _res = AmbientOcclusionMap._from_sdf(_c_ambient_occlusion_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient_occlusion_map")
            _ambient_occlusion_map = _res
        else:
            _ambient_occlusion_map = None
        _c_normal_map = el.find("normal_map")
        if _c_normal_map is not None:
            _res = MetalNormalMap._from_sdf(_c_normal_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal_map")
            _normal_map = _res
        else:
            _normal_map = None
        _c_emissive_map = el.find("emissive_map")
        if _c_emissive_map is not None:
            _res = EmissiveMap._from_sdf(_c_emissive_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("emissive_map")
            _emissive_map = _res
        else:
            _emissive_map = None
        _c_light_map = el.find("light_map")
        if _c_light_map is not None:
            _res = LightMap._from_sdf(_c_light_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_map")
            _light_map = _res
        else:
            _light_map = None
        if _light_map is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, albedo_map=_albedo_map, roughness_map=_roughness_map, roughness=_roughness, metalness_map=_metalness_map, metalness=_metalness, environment_map=_environment_map, ambient_occlusion_map=_ambient_occlusion_map, normal_map=_normal_map, emissive_map=_emissive_map, light_map=_light_map)


class SpecularMap(BaseModel):
    def __init__(self, sdf_version: str, specular_map: str = ""):
        self.__version__ = sdf_version
        self.specular_map = specular_map

    def to_version(self, target_version: str) -> "SpecularMap":
        kwargs = {"sdf_version": target_version}
        kwargs["specular_map"] = self.specular_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular_map")
        if self.specular_map is not None:
            el.text = self.specular_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _specular_map = _text
        if isinstance(_specular_map, SDFError):
            return _specular_map
        return cls(sdf_version=version, specular_map=_specular_map)


class GlossinessMap(BaseModel):
    def __init__(self, sdf_version: str, glossiness_map: str = ""):
        self.__version__ = sdf_version
        self.glossiness_map = glossiness_map

    def to_version(self, target_version: str) -> "GlossinessMap":
        kwargs = {"sdf_version": target_version}
        kwargs["glossiness_map"] = self.glossiness_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("glossiness_map")
        if self.glossiness_map is not None:
            el.text = self.glossiness_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _glossiness_map = _text
        if isinstance(_glossiness_map, SDFError):
            return _glossiness_map
        return cls(sdf_version=version, glossiness_map=_glossiness_map)


class Glossiness(BaseModel):
    def __init__(self, sdf_version: str, glossiness: str = "0"):
        self.__version__ = sdf_version
        self.glossiness = glossiness

    def to_version(self, target_version: str) -> "Glossiness":
        kwargs = {"sdf_version": target_version}
        kwargs["glossiness"] = self.glossiness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("glossiness")
        if self.glossiness is not None:
            el.text = self.glossiness
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0"
        _glossiness = _text
        if isinstance(_glossiness, SDFError):
            return _glossiness
        return cls(sdf_version=version, glossiness=_glossiness)


class SpecularNormalMap(BaseModel):
    def __init__(self, sdf_version: str, normal_map: str = "", type: str = "tangent"):
        self.__version__ = sdf_version
        self.normal_map = normal_map
        self.type = type

    def to_version(self, target_version: str) -> "SpecularNormalMap":
        kwargs = {"sdf_version": target_version}
        kwargs["normal_map"] = self.normal_map
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal_map")
        if self.normal_map is not None:
            el.text = self.normal_map
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _normal_map = _text
        if isinstance(_normal_map, SDFError):
            return _normal_map
        _type = el.get("type", "tangent")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, normal_map=_normal_map, type=_type)


class PbrSpecular(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        albedo_map: "AlbedoMap" = None,
        specular_map: "SpecularMap" = None,
        glossiness_map: "GlossinessMap" = None,
        glossiness: "Glossiness" = None,
        environment_map: "EnvironmentMap" = None,
        ambient_occlusion_map: "AmbientOcclusionMap" = None,
        normal_map: "SpecularNormalMap" = None,
        emissive_map: "EmissiveMap" = None,
        light_map: "LightMap" = None
    ):
        self.__version__ = sdf_version
        self.albedo_map = albedo_map
        self.specular_map = specular_map
        self.glossiness_map = glossiness_map
        self.glossiness = glossiness
        self.environment_map = environment_map
        self.ambient_occlusion_map = ambient_occlusion_map
        self.normal_map = normal_map
        self.emissive_map = emissive_map
        self.light_map = light_map

    def to_version(self, target_version: str) -> "PbrSpecular":
        if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["albedo_map"] = self.albedo_map.to_version(target_version) if self.albedo_map is not None else None
        kwargs["specular_map"] = self.specular_map.to_version(target_version) if self.specular_map is not None else None
        kwargs["glossiness_map"] = self.glossiness_map.to_version(target_version) if self.glossiness_map is not None else None
        kwargs["glossiness"] = self.glossiness.to_version(target_version) if self.glossiness is not None else None
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
        el = ET.Element("specular")
        if self.albedo_map is not None:
            el.append(self.albedo_map.to_sdf(version))
        if self.specular_map is not None:
            el.append(self.specular_map.to_sdf(version))
        if self.glossiness_map is not None:
            el.append(self.glossiness_map.to_sdf(version))
        if self.glossiness is not None:
            el.append(self.glossiness.to_sdf(version))
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_albedo_map = el.find("albedo_map")
        if _c_albedo_map is not None:
            _res = AlbedoMap._from_sdf(_c_albedo_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("albedo_map")
            _albedo_map = _res
        else:
            _albedo_map = None
        _c_specular_map = el.find("specular_map")
        if _c_specular_map is not None:
            _res = SpecularMap._from_sdf(_c_specular_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular_map")
            _specular_map = _res
        else:
            _specular_map = None
        _c_glossiness_map = el.find("glossiness_map")
        if _c_glossiness_map is not None:
            _res = GlossinessMap._from_sdf(_c_glossiness_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("glossiness_map")
            _glossiness_map = _res
        else:
            _glossiness_map = None
        _c_glossiness = el.find("glossiness")
        if _c_glossiness is not None:
            _res = Glossiness._from_sdf(_c_glossiness, version)
            if isinstance(_res, SDFError):
                return _res.extend("glossiness")
            _glossiness = _res
        else:
            _glossiness = None
        _c_environment_map = el.find("environment_map")
        if _c_environment_map is not None:
            _res = EnvironmentMap._from_sdf(_c_environment_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("environment_map")
            _environment_map = _res
        else:
            _environment_map = None
        _c_ambient_occlusion_map = el.find("ambient_occlusion_map")
        if _c_ambient_occlusion_map is not None:
            _res = AmbientOcclusionMap._from_sdf(_c_ambient_occlusion_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient_occlusion_map")
            _ambient_occlusion_map = _res
        else:
            _ambient_occlusion_map = None
        _c_normal_map = el.find("normal_map")
        if _c_normal_map is not None:
            _res = SpecularNormalMap._from_sdf(_c_normal_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal_map")
            _normal_map = _res
        else:
            _normal_map = None
        _c_emissive_map = el.find("emissive_map")
        if _c_emissive_map is not None:
            _res = EmissiveMap._from_sdf(_c_emissive_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("emissive_map")
            _emissive_map = _res
        else:
            _emissive_map = None
        _c_light_map = el.find("light_map")
        if _c_light_map is not None:
            _res = LightMap._from_sdf(_c_light_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_map")
            _light_map = _res
        else:
            _light_map = None
        if _light_map is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, albedo_map=_albedo_map, specular_map=_specular_map, glossiness_map=_glossiness_map, glossiness=_glossiness, environment_map=_environment_map, ambient_occlusion_map=_ambient_occlusion_map, normal_map=_normal_map, emissive_map=_emissive_map, light_map=_light_map)


class Pbr(BaseModel):
    def __init__(self, sdf_version: str, metal: "Metal" = None, specular: "PbrSpecular" = None):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_metal = el.find("metal")
        if _c_metal is not None:
            _res = Metal._from_sdf(_c_metal, version)
            if isinstance(_res, SDFError):
                return _res.extend("metal")
            _metal = _res
        else:
            _metal = None
        _c_specular = el.find("specular")
        if _c_specular is not None:
            _res = PbrSpecular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        return cls(sdf_version=version, metal=_metal, specular=_specular)


class Shininess(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _shininess = _parse_double(_text)
        if isinstance(_shininess, SDFError):
            return _shininess
        if _shininess is not None and cmp_version(version, "1.7") < 0:
            if _shininess != 0:
                return SDFError(f"'shininess' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, shininess=_shininess)


class DoubleSided(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _double_sided = str(_text).strip().lower() == 'true'
        if isinstance(_double_sided, SDFError):
            return _double_sided
        if _double_sided is not None and cmp_version(version, "1.7") < 0:
            if _double_sided != False:
                return SDFError(f"'double_sided' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, double_sided=_double_sided)


class RenderOrder(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _render_order = _parse_double(_text)
        if isinstance(_render_order, SDFError):
            return _render_order
        if _render_order is not None and cmp_version(version, "1.7") < 0:
            if _render_order != 0.0:
                return SDFError(f"'render_order' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, render_order=_render_order)


class Material(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        script: "Script" = None,
        shader: "Shader" = None,
        ambient: "Ambient" = None,
        diffuse: "MaterialDiffuse" = None,
        specular: "Specular" = None,
        emissive: "Emissive" = None,
        lighting: "Lighting" = None,
        pbr: "Pbr" = None,
        shininess: "Shininess" = None,
        double_sided: "DoubleSided" = None,
        render_order: "RenderOrder" = None
    ):
        self.__version__ = sdf_version
        self.script = script
        self.shader = shader
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.emissive = emissive
        self.lighting = lighting
        self.pbr = pbr
        self.shininess = shininess
        self.double_sided = double_sided
        self.render_order = render_order

    def to_version(self, target_version: str) -> "Material":
        if self.lighting is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'lighting' is not supported in SDF version {target_version} (added in 1.4)")
        if self.pbr is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'pbr' is not supported in SDF version {target_version} (added in 1.6)")
        if self.shininess is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {target_version} (added in 1.7)")
        if self.double_sided is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {target_version} (added in 1.7)")
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["script"] = self.script.to_version(target_version) if self.script is not None else None
        kwargs["shader"] = self.shader.to_version(target_version) if self.shader is not None else None
        kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["emissive"] = self.emissive.to_version(target_version) if self.emissive is not None else None
        kwargs["lighting"] = self.lighting.to_version(target_version) if self.lighting is not None else None
        kwargs["pbr"] = self.pbr.to_version(target_version) if self.pbr is not None else None
        kwargs["shininess"] = self.shininess.to_version(target_version) if self.shininess is not None else None
        kwargs["double_sided"] = self.double_sided.to_version(target_version) if self.double_sided is not None else None
        kwargs["render_order"] = self.render_order.to_version(target_version) if self.render_order is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("material")
        if self.script is not None:
            el.append(self.script.to_sdf(version))
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
        if self.pbr is not None:
            el.append(self.pbr.to_sdf(version))
        if self.shininess is not None:
            el.append(self.shininess.to_sdf(version))
        if self.double_sided is not None:
            el.append(self.double_sided.to_sdf(version))
        if self.render_order is not None:
            el.append(self.render_order.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_script = el.find("script")
        if _c_script is not None:
            _res = Script._from_sdf(_c_script, version)
            if isinstance(_res, SDFError):
                return _res.extend("script")
            _script = _res
        else:
            _script = None
        _c_shader = el.find("shader")
        if _c_shader is not None:
            _res = Shader._from_sdf(_c_shader, version)
            if isinstance(_res, SDFError):
                return _res.extend("shader")
            _shader = _res
        else:
            _shader = None
        _c_ambient = el.find("ambient")
        if _c_ambient is not None:
            _res = Ambient._from_sdf(_c_ambient, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient")
            _ambient = _res
        else:
            _ambient = None
        _c_diffuse = el.find("diffuse")
        if _c_diffuse is not None:
            _res = MaterialDiffuse._from_sdf(_c_diffuse, version)
            if isinstance(_res, SDFError):
                return _res.extend("diffuse")
            _diffuse = _res
        else:
            _diffuse = None
        _c_specular = el.find("specular")
        if _c_specular is not None:
            _res = Specular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        _c_emissive = el.find("emissive")
        if _c_emissive is not None:
            _res = Emissive._from_sdf(_c_emissive, version)
            if isinstance(_res, SDFError):
                return _res.extend("emissive")
            _emissive = _res
        else:
            _emissive = None
        _c_lighting = el.find("lighting")
        if _c_lighting is not None:
            _res = Lighting._from_sdf(_c_lighting, version)
            if isinstance(_res, SDFError):
                return _res.extend("lighting")
            _lighting = _res
        else:
            _lighting = None
        if _lighting is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'lighting' is not supported in SDF version {version} (added in 1.4)")
        _c_pbr = el.find("pbr")
        if _c_pbr is not None:
            _res = Pbr._from_sdf(_c_pbr, version)
            if isinstance(_res, SDFError):
                return _res.extend("pbr")
            _pbr = _res
        else:
            _pbr = None
        if _pbr is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'pbr' is not supported in SDF version {version} (added in 1.6)")
        _c_shininess = el.find("shininess")
        if _c_shininess is not None:
            _res = Shininess._from_sdf(_c_shininess, version)
            if isinstance(_res, SDFError):
                return _res.extend("shininess")
            _shininess = _res
        else:
            _shininess = None
        if _shininess is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'shininess' is not supported in SDF version {version} (added in 1.7)")
        _c_double_sided = el.find("double_sided")
        if _c_double_sided is not None:
            _res = DoubleSided._from_sdf(_c_double_sided, version)
            if isinstance(_res, SDFError):
                return _res.extend("double_sided")
            _double_sided = _res
        else:
            _double_sided = None
        if _double_sided is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'double_sided' is not supported in SDF version {version} (added in 1.7)")
        _c_render_order = el.find("render_order")
        if _c_render_order is not None:
            _res = RenderOrder._from_sdf(_c_render_order, version)
            if isinstance(_res, SDFError):
                return _res.extend("render_order")
            _render_order = _res
        else:
            _render_order = None
        if _render_order is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'render_order' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, script=_script, shader=_shader, ambient=_ambient, diffuse=_diffuse, specular=_specular, emissive=_emissive, lighting=_lighting, pbr=_pbr, shininess=_shininess, double_sided=_double_sided, render_order=_render_order)


class Plugin(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        return cls(sdf_version=version, name=_name, filename=_filename)


class Layer(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _layer = _parse_int32(_text)
        if isinstance(_layer, SDFError):
            return _layer
        return cls(sdf_version=version, layer=_layer)


class Meta(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_layer = el.find("layer")
        if _c_layer is not None:
            _res = Layer._from_sdf(_c_layer, version)
            if isinstance(_res, SDFError):
                return _res.extend("layer")
            _layer = _res
        else:
            _layer = None
        return cls(sdf_version=version, layer=_layer)


class VisibilityFlags(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4294967295
        _visibility_flags = _parse_uint32(_text)
        if isinstance(_visibility_flags, SDFError):
            return _visibility_flags
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            if _visibility_flags != 4294967295:
                return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_flags=_visibility_flags)


class Visual(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        geometry: "Geometry" = None,
        cast_shadows: "CastShadows" = None,
        laser_retro: "VisualLaserRetro" = None,
        transparency: "Transparency" = None,
        pose: "VisualPose" = None,
        material: "Material" = None,
        plugin: List["Plugin"] = None,
        frame: List["Frame"] = None,
        meta: "Meta" = None,
        visibility_flags: "VisibilityFlags" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.geometry = geometry
        self.cast_shadows = cast_shadows
        self.laser_retro = laser_retro
        self.transparency = transparency
        self.pose = pose
        self.material = material
        self.plugin = plugin or []
        self.frame = frame or []
        self.meta = meta
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "Visual":
        if self.plugin is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {target_version} (added in 1.3)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.meta is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'meta' is not supported in SDF version {target_version} (added in 1.5)")
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["cast_shadows"] = self.cast_shadows.to_version(target_version) if self.cast_shadows is not None else None
        kwargs["laser_retro"] = self.laser_retro.to_version(target_version) if self.laser_retro is not None else None
        kwargs["transparency"] = self.transparency.to_version(target_version) if self.transparency is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["meta"] = self.meta.to_version(target_version) if self.meta is not None else None
        kwargs["visibility_flags"] = self.visibility_flags.to_version(target_version) if self.visibility_flags is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visual")
        if self.name is not None:
            el.set("name", self.name)
        if self.geometry is None:
            self.geometry = Geometry(sdf_version=version)
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.cast_shadows is not None:
            el.append(self.cast_shadows.to_sdf(version))
        if self.laser_retro is not None:
            el.append(self.laser_retro.to_sdf(version))
        if self.transparency is not None:
            el.append(self.transparency.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.material is not None:
            el.append(self.material.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.meta is not None:
            el.append(self.meta.to_sdf(version))
        if self.visibility_flags is not None:
            el.append(self.visibility_flags.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
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
        _c_cast_shadows = el.find("cast_shadows")
        if _c_cast_shadows is not None:
            _res = CastShadows._from_sdf(_c_cast_shadows, version)
            if isinstance(_res, SDFError):
                return _res.extend("cast_shadows")
            _cast_shadows = _res
        else:
            _cast_shadows = None
        _c_laser_retro = el.find("laser_retro")
        if _c_laser_retro is not None:
            _res = VisualLaserRetro._from_sdf(_c_laser_retro, version)
            if isinstance(_res, SDFError):
                return _res.extend("laser_retro")
            _laser_retro = _res
        else:
            _laser_retro = None
        _c_transparency = el.find("transparency")
        if _c_transparency is not None:
            _res = Transparency._from_sdf(_c_transparency, version)
            if isinstance(_res, SDFError):
                return _res.extend("transparency")
            _transparency = _res
        else:
            _transparency = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = VisualPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_material = el.find("material")
        if _c_material is not None:
            _res = Material._from_sdf(_c_material, version)
            if isinstance(_res, SDFError):
                return _res.extend("material")
            _material = _res
        else:
            _material = None
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        if _plugin and cmp_version(version, "1.3") < 0:
            return SDFError(f"'plugin' is not supported in SDF version {version} (added in 1.3)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_meta = el.find("meta")
        if _c_meta is not None:
            _res = Meta._from_sdf(_c_meta, version)
            if isinstance(_res, SDFError):
                return _res.extend("meta")
            _meta = _res
        else:
            _meta = None
        if _meta is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'meta' is not supported in SDF version {version} (added in 1.5)")
        _c_visibility_flags = el.find("visibility_flags")
        if _c_visibility_flags is not None:
            _res = VisibilityFlags._from_sdf(_c_visibility_flags, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_flags")
            _visibility_flags = _res
        else:
            _visibility_flags = None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, name=_name, geometry=_geometry, cast_shadows=_cast_shadows, laser_retro=_laser_retro, transparency=_transparency, pose=_pose, material=_material, plugin=_plugin, frame=_frame, meta=_meta, visibility_flags=_visibility_flags)


class HorizontalFov(BaseModel):
    def __init__(self, sdf_version: str, horizontal_fov: float = 1.047):
        self.__version__ = sdf_version
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "HorizontalFov":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal_fov"] = self.horizontal_fov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal_fov")
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.047
        _horizontal_fov = _parse_double(_text)
        if isinstance(_horizontal_fov, SDFError):
            return _horizontal_fov
        return cls(sdf_version=version, horizontal_fov=_horizontal_fov)


class Width(BaseModel):
    def __init__(self, sdf_version: str, width: int = 320):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 320
        _width = _parse_int32(_text)
        if isinstance(_width, SDFError):
            return _width
        return cls(sdf_version=version, width=_width)


class ImageHeight(BaseModel):
    def __init__(self, sdf_version: str, height: int = 240):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "ImageHeight":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 240
        _height = _parse_int32(_text)
        if isinstance(_height, SDFError):
            return _height
        return cls(sdf_version=version, height=_height)


class Format(BaseModel):
    def __init__(self, sdf_version: str, format: str = "R8G8B8"):
        self.__version__ = sdf_version
        self.format = format

    def to_version(self, target_version: str) -> "Format":
        kwargs = {"sdf_version": target_version}
        kwargs["format"] = self.format
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("format")
        if self.format is not None:
            el.text = self.format
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "R8G8B8"
        _format = _text
        if isinstance(_format, SDFError):
            return _format
        return cls(sdf_version=version, format=_format)


class AntiAliasing(BaseModel):
    def __init__(self, sdf_version: str, anti_aliasing: int = 4):
        self.__version__ = sdf_version
        self.anti_aliasing = anti_aliasing

    def to_version(self, target_version: str) -> "AntiAliasing":
        if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["anti_aliasing"] = self.anti_aliasing
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("anti_aliasing")
        if self.anti_aliasing is not None:
            el.text = str(self.anti_aliasing)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4
        _anti_aliasing = _parse_int32(_text)
        if isinstance(_anti_aliasing, SDFError):
            return _anti_aliasing
        if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
            if _anti_aliasing != 4:
                return SDFError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, anti_aliasing=_anti_aliasing)


class CameraImage(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        width: "Width" = None,
        height: "ImageHeight" = None,
        format: "Format" = None,
        anti_aliasing: "AntiAliasing" = None
    ):
        self.__version__ = sdf_version
        self.width = width
        self.height = height
        self.format = format
        self.anti_aliasing = anti_aliasing

    def to_version(self, target_version: str) -> "CameraImage":
        if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["width"] = self.width.to_version(target_version) if self.width is not None else None
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        kwargs["format"] = self.format.to_version(target_version) if self.format is not None else None
        kwargs["anti_aliasing"] = self.anti_aliasing.to_version(target_version) if self.anti_aliasing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("image")
        if self.width is not None:
            el.append(self.width.to_sdf(version))
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        if self.format is not None:
            el.append(self.format.to_sdf(version))
        if self.anti_aliasing is not None:
            el.append(self.anti_aliasing.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_width = el.find("width")
        if _c_width is not None:
            _res = Width._from_sdf(_c_width, version)
            if isinstance(_res, SDFError):
                return _res.extend("width")
            _width = _res
        else:
            _width = None
        _c_height = el.find("height")
        if _c_height is not None:
            _res = ImageHeight._from_sdf(_c_height, version)
            if isinstance(_res, SDFError):
                return _res.extend("height")
            _height = _res
        else:
            _height = None
        _c_format = el.find("format")
        if _c_format is not None:
            _res = Format._from_sdf(_c_format, version)
            if isinstance(_res, SDFError):
                return _res.extend("format")
            _format = _res
        else:
            _format = None
        _c_anti_aliasing = el.find("anti_aliasing")
        if _c_anti_aliasing is not None:
            _res = AntiAliasing._from_sdf(_c_anti_aliasing, version)
            if isinstance(_res, SDFError):
                return _res.extend("anti_aliasing")
            _anti_aliasing = _res
        else:
            _anti_aliasing = None
        if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, width=_width, height=_height, format=_format, anti_aliasing=_anti_aliasing)


class Near(BaseModel):
    def __init__(self, sdf_version: str, near: float = .1):
        self.__version__ = sdf_version
        self.near = near

    def to_version(self, target_version: str) -> "Near":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or .1
        _near = _parse_double(_text)
        if isinstance(_near, SDFError):
            return _near
        return cls(sdf_version=version, near=_near)


class Far(BaseModel):
    def __init__(self, sdf_version: str, far: float = 100):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "Far":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100
        _far = _parse_double(_text)
        if isinstance(_far, SDFError):
            return _far
        return cls(sdf_version=version, far=_far)


class Clip(BaseModel):
    def __init__(self, sdf_version: str, near: "Near" = None, far: "Far" = None):
        self.__version__ = sdf_version
        self.near = near
        self.far = far

    def to_version(self, target_version: str) -> "Clip":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near.to_version(target_version) if self.near is not None else None
        kwargs["far"] = self.far.to_version(target_version) if self.far is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("clip")
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        if self.far is not None:
            el.append(self.far.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_near = el.find("near")
        if _c_near is not None:
            _res = Near._from_sdf(_c_near, version)
            if isinstance(_res, SDFError):
                return _res.extend("near")
            _near = _res
        else:
            _near = None
        _c_far = el.find("far")
        if _c_far is not None:
            _res = Far._from_sdf(_c_far, version)
            if isinstance(_res, SDFError):
                return _res.extend("far")
            _far = _res
        else:
            _far = None
        return cls(sdf_version=version, near=_near, far=_far)


class Path(BaseModel):
    def __init__(self, sdf_version: str, path: str = "__default__"):
        self.__version__ = sdf_version
        self.path = path

    def to_version(self, target_version: str) -> "Path":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _path = _text
        if isinstance(_path, SDFError):
            return _path
        return cls(sdf_version=version, path=_path)


class Save(BaseModel):
    def __init__(self, sdf_version: str, enabled: bool = False, path: "Path" = None):
        self.__version__ = sdf_version
        self.enabled = enabled
        self.path = path

    def to_version(self, target_version: str) -> "Save":
        kwargs = {"sdf_version": target_version}
        kwargs["enabled"] = self.enabled
        kwargs["path"] = self.path.to_version(target_version) if self.path is not None else None
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
            el.append(self.path.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _enabled = str(el.get("enabled", False)).strip().lower() == 'true'
        if isinstance(_enabled, SDFError):
            return _enabled.extend("@enabled")
        _c_path = el.find("path")
        if _c_path is not None:
            _res = Path._from_sdf(_c_path, version)
            if isinstance(_res, SDFError):
                return _res.extend("path")
            _path = _res
        else:
            _path = None
        return cls(sdf_version=version, enabled=_enabled, path=_path)


class Output(BaseModel):
    def __init__(self, sdf_version: str, output: str = "depths"):
        self.__version__ = sdf_version
        self.output = output

    def to_version(self, target_version: str) -> "Output":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "depths"
        _output = _text
        if isinstance(_output, SDFError):
            return _output
        return cls(sdf_version=version, output=_output)


class ClipFar(BaseModel):
    def __init__(self, sdf_version: str, far: float = 10.0):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "ClipFar":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10.0
        _far = _parse_double(_text)
        if isinstance(_far, SDFError):
            return _far
        return cls(sdf_version=version, far=_far)


class DepthCameraClip(BaseModel):
    def __init__(self, sdf_version: str, near: "Near" = None, far: "ClipFar" = None):
        self.__version__ = sdf_version
        self.near = near
        self.far = far

    def to_version(self, target_version: str) -> "DepthCameraClip":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near.to_version(target_version) if self.near is not None else None
        kwargs["far"] = self.far.to_version(target_version) if self.far is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("clip")
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        if self.far is not None:
            el.append(self.far.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_near = el.find("near")
        if _c_near is not None:
            _res = Near._from_sdf(_c_near, version)
            if isinstance(_res, SDFError):
                return _res.extend("near")
            _near = _res
        else:
            _near = None
        _c_far = el.find("far")
        if _c_far is not None:
            _res = ClipFar._from_sdf(_c_far, version)
            if isinstance(_res, SDFError):
                return _res.extend("far")
            _far = _res
        else:
            _far = None
        return cls(sdf_version=version, near=_near, far=_far)


class DepthCamera(BaseModel):
    def __init__(self, sdf_version: str, output: "Output" = None, clip: "DepthCameraClip" = None):
        self.__version__ = sdf_version
        self.output = output
        self.clip = clip

    def to_version(self, target_version: str) -> "DepthCamera":
        if self.clip is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'clip' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["output"] = self.output.to_version(target_version) if self.output is not None else None
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("depth_camera")
        if self.output is not None:
            el.append(self.output.to_sdf(version))
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_output = el.find("output")
        if _c_output is not None:
            _res = Output._from_sdf(_c_output, version)
            if isinstance(_res, SDFError):
                return _res.extend("output")
            _output = _res
        else:
            _output = None
        _c_clip = el.find("clip")
        if _c_clip is not None:
            _res = DepthCameraClip._from_sdf(_c_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        else:
            _clip = None
        if _clip is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'clip' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, output=_output, clip=_clip)


class CameraPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "CameraPose":
        if self.pose is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.3)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        if _pose is not None and cmp_version(version, "1.3") < 0:
            if _pose != "0 0 0 0 0 0":
                return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.3)")
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Type(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "gaussian"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        return cls(sdf_version=version, type=_type)


class Mean(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _mean = _parse_double(_text)
        if isinstance(_mean, SDFError):
            return _mean
        return cls(sdf_version=version, mean=_mean)


class Stddev(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _stddev = _parse_double(_text)
        if isinstance(_stddev, SDFError):
            return _stddev
        return cls(sdf_version=version, stddev=_stddev)


class Noise(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev)


class LensType(BaseModel):
    def __init__(self, sdf_version: str, type: str = "stereographic"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "LensType":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "stereographic"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        return cls(sdf_version=version, type=_type)


class ScaleToHfov(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _scale_to_hfov = str(_text).strip().lower() == 'true'
        if isinstance(_scale_to_hfov, SDFError):
            return _scale_to_hfov
        return cls(sdf_version=version, scale_to_hfov=_scale_to_hfov)


class C1(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _c1 = _parse_double(_text)
        if isinstance(_c1, SDFError):
            return _c1
        return cls(sdf_version=version, c1=_c1)


class C2(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _c2 = _parse_double(_text)
        if isinstance(_c2, SDFError):
            return _c2
        return cls(sdf_version=version, c2=_c2)


class C3(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _c3 = _parse_double(_text)
        if isinstance(_c3, SDFError):
            return _c3
        return cls(sdf_version=version, c3=_c3)


class F(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _f = _parse_double(_text)
        if isinstance(_f, SDFError):
            return _f
        return cls(sdf_version=version, f=_f)


class Fun(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "tan"
        _fun = _text
        if isinstance(_fun, SDFError):
            return _fun
        return cls(sdf_version=version, fun=_fun)


class CustomFunction(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_c1 = el.find("c1")
        if _c_c1 is not None:
            _res = C1._from_sdf(_c_c1, version)
            if isinstance(_res, SDFError):
                return _res.extend("c1")
            _c1 = _res
        else:
            _c1 = None
        _c_c2 = el.find("c2")
        if _c_c2 is not None:
            _res = C2._from_sdf(_c_c2, version)
            if isinstance(_res, SDFError):
                return _res.extend("c2")
            _c2 = _res
        else:
            _c2 = None
        _c_c3 = el.find("c3")
        if _c_c3 is not None:
            _res = C3._from_sdf(_c_c3, version)
            if isinstance(_res, SDFError):
                return _res.extend("c3")
            _c3 = _res
        else:
            _c3 = None
        _c_f = el.find("f")
        if _c_f is not None:
            _res = F._from_sdf(_c_f, version)
            if isinstance(_res, SDFError):
                return _res.extend("f")
            _f = _res
        else:
            _f = None
        _c_fun = el.find("fun")
        if _c_fun is not None:
            _res = Fun._from_sdf(_c_fun, version)
            if isinstance(_res, SDFError):
                return _res.extend("fun")
            _fun = _res
        else:
            _fun = None
        return cls(sdf_version=version, c1=_c1, c2=_c2, c3=_c3, f=_f, fun=_fun)


class CutoffAngle(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.5707
        _cutoff_angle = _parse_double(_text)
        if isinstance(_cutoff_angle, SDFError):
            return _cutoff_angle
        return cls(sdf_version=version, cutoff_angle=_cutoff_angle)


class EnvTextureSize(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 256
        _env_texture_size = _parse_int32(_text)
        if isinstance(_env_texture_size, SDFError):
            return _env_texture_size
        return cls(sdf_version=version, env_texture_size=_env_texture_size)


class Fx(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _fx = _parse_double(_text)
        if isinstance(_fx, SDFError):
            return _fx
        return cls(sdf_version=version, fx=_fx)


class Fy(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _fy = _parse_double(_text)
        if isinstance(_fy, SDFError):
            return _fy
        return cls(sdf_version=version, fy=_fy)


class Cx(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 160
        _cx = _parse_double(_text)
        if isinstance(_cx, SDFError):
            return _cx
        return cls(sdf_version=version, cx=_cx)


class Cy(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 120
        _cy = _parse_double(_text)
        if isinstance(_cy, SDFError):
            return _cy
        return cls(sdf_version=version, cy=_cy)


class S(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _s = _parse_double(_text)
        if isinstance(_s, SDFError):
            return _s
        return cls(sdf_version=version, s=_s)


class Intrinsics(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_fx = el.find("fx")
        if _c_fx is not None:
            _res = Fx._from_sdf(_c_fx, version)
            if isinstance(_res, SDFError):
                return _res.extend("fx")
            _fx = _res
        else:
            _fx = None
        _c_fy = el.find("fy")
        if _c_fy is not None:
            _res = Fy._from_sdf(_c_fy, version)
            if isinstance(_res, SDFError):
                return _res.extend("fy")
            _fy = _res
        else:
            _fy = None
        _c_cx = el.find("cx")
        if _c_cx is not None:
            _res = Cx._from_sdf(_c_cx, version)
            if isinstance(_res, SDFError):
                return _res.extend("cx")
            _cx = _res
        else:
            _cx = None
        _c_cy = el.find("cy")
        if _c_cy is not None:
            _res = Cy._from_sdf(_c_cy, version)
            if isinstance(_res, SDFError):
                return _res.extend("cy")
            _cy = _res
        else:
            _cy = None
        _c_s = el.find("s")
        if _c_s is not None:
            _res = S._from_sdf(_c_s, version)
            if isinstance(_res, SDFError):
                return _res.extend("s")
            _s = _res
        else:
            _s = None
        return cls(sdf_version=version, fx=_fx, fy=_fy, cx=_cx, cy=_cy, s=_s)


class PFx(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _p_fx = _parse_double(_text)
        if isinstance(_p_fx, SDFError):
            return _p_fx
        return cls(sdf_version=version, p_fx=_p_fx)


class PFy(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _p_fy = _parse_double(_text)
        if isinstance(_p_fy, SDFError):
            return _p_fy
        return cls(sdf_version=version, p_fy=_p_fy)


class PCx(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 160
        _p_cx = _parse_double(_text)
        if isinstance(_p_cx, SDFError):
            return _p_cx
        return cls(sdf_version=version, p_cx=_p_cx)


class PCy(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 120
        _p_cy = _parse_double(_text)
        if isinstance(_p_cy, SDFError):
            return _p_cy
        return cls(sdf_version=version, p_cy=_p_cy)


class Tx(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _tx = _parse_double(_text)
        if isinstance(_tx, SDFError):
            return _tx
        return cls(sdf_version=version, tx=_tx)


class Ty(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _ty = _parse_double(_text)
        if isinstance(_ty, SDFError):
            return _ty
        return cls(sdf_version=version, ty=_ty)


class Projection(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_p_fx = el.find("p_fx")
        if _c_p_fx is not None:
            _res = PFx._from_sdf(_c_p_fx, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_fx")
            _p_fx = _res
        else:
            _p_fx = None
        _c_p_fy = el.find("p_fy")
        if _c_p_fy is not None:
            _res = PFy._from_sdf(_c_p_fy, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_fy")
            _p_fy = _res
        else:
            _p_fy = None
        _c_p_cx = el.find("p_cx")
        if _c_p_cx is not None:
            _res = PCx._from_sdf(_c_p_cx, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_cx")
            _p_cx = _res
        else:
            _p_cx = None
        _c_p_cy = el.find("p_cy")
        if _c_p_cy is not None:
            _res = PCy._from_sdf(_c_p_cy, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_cy")
            _p_cy = _res
        else:
            _p_cy = None
        _c_tx = el.find("tx")
        if _c_tx is not None:
            _res = Tx._from_sdf(_c_tx, version)
            if isinstance(_res, SDFError):
                return _res.extend("tx")
            _tx = _res
        else:
            _tx = None
        _c_ty = el.find("ty")
        if _c_ty is not None:
            _res = Ty._from_sdf(_c_ty, version)
            if isinstance(_res, SDFError):
                return _res.extend("ty")
            _ty = _res
        else:
            _ty = None
        return cls(sdf_version=version, p_fx=_p_fx, p_fy=_p_fy, p_cx=_p_cx, p_cy=_p_cy, tx=_tx, ty=_ty)


class Lens(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: "LensType" = None,
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
        if self.intrinsics is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'intrinsics' is not supported in SDF version {target_version} (added in 1.6)")
        if self.projection is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'projection' is not supported in SDF version {target_version} (added in 1.7)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_type = el.find("type")
        if _c_type is not None:
            _res = LensType._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        _c_scale_to_hfov = el.find("scale_to_hfov")
        if _c_scale_to_hfov is not None:
            _res = ScaleToHfov._from_sdf(_c_scale_to_hfov, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale_to_hfov")
            _scale_to_hfov = _res
        else:
            _scale_to_hfov = None
        _c_custom_function = el.find("custom_function")
        if _c_custom_function is not None:
            _res = CustomFunction._from_sdf(_c_custom_function, version)
            if isinstance(_res, SDFError):
                return _res.extend("custom_function")
            _custom_function = _res
        else:
            _custom_function = None
        _c_cutoff_angle = el.find("cutoff_angle")
        if _c_cutoff_angle is not None:
            _res = CutoffAngle._from_sdf(_c_cutoff_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("cutoff_angle")
            _cutoff_angle = _res
        else:
            _cutoff_angle = None
        _c_env_texture_size = el.find("env_texture_size")
        if _c_env_texture_size is not None:
            _res = EnvTextureSize._from_sdf(_c_env_texture_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("env_texture_size")
            _env_texture_size = _res
        else:
            _env_texture_size = None
        _c_intrinsics = el.find("intrinsics")
        if _c_intrinsics is not None:
            _res = Intrinsics._from_sdf(_c_intrinsics, version)
            if isinstance(_res, SDFError):
                return _res.extend("intrinsics")
            _intrinsics = _res
        else:
            _intrinsics = None
        if _intrinsics is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'intrinsics' is not supported in SDF version {version} (added in 1.6)")
        _c_projection = el.find("projection")
        if _c_projection is not None:
            _res = Projection._from_sdf(_c_projection, version)
            if isinstance(_res, SDFError):
                return _res.extend("projection")
            _projection = _res
        else:
            _projection = None
        if _projection is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'projection' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, type=_type, scale_to_hfov=_scale_to_hfov, custom_function=_custom_function, cutoff_angle=_cutoff_angle, env_texture_size=_env_texture_size, intrinsics=_intrinsics, projection=_projection)


class K1(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k1 = _parse_double(_text)
        if isinstance(_k1, SDFError):
            return _k1
        return cls(sdf_version=version, k1=_k1)


class K2(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k2 = _parse_double(_text)
        if isinstance(_k2, SDFError):
            return _k2
        return cls(sdf_version=version, k2=_k2)


class K3(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k3 = _parse_double(_text)
        if isinstance(_k3, SDFError):
            return _k3
        return cls(sdf_version=version, k3=_k3)


class P1(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _p1 = _parse_double(_text)
        if isinstance(_p1, SDFError):
            return _p1
        return cls(sdf_version=version, p1=_p1)


class P2(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _p2 = _parse_double(_text)
        if isinstance(_p2, SDFError):
            return _p2
        return cls(sdf_version=version, p2=_p2)


class DistortionCenter(BaseModel):
    def __init__(self, sdf_version: str, center: _SDFVector2d = None):
        self.__version__ = sdf_version
        if center is None:
            center = _SDFVector2d.from_sdf("0.5 0.5")
        self.center = center

    def to_version(self, target_version: str) -> "DistortionCenter":
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
            el.text = self.center.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.5 0.5"
        _center = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_center, SDFError):
            return _center
        return cls(sdf_version=version, center=_center)


class Distortion(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        k1: "K1" = None,
        k2: "K2" = None,
        k3: "K3" = None,
        p1: "P1" = None,
        p2: "P2" = None,
        center: "DistortionCenter" = None
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_k1 = el.find("k1")
        if _c_k1 is not None:
            _res = K1._from_sdf(_c_k1, version)
            if isinstance(_res, SDFError):
                return _res.extend("k1")
            _k1 = _res
        else:
            _k1 = None
        _c_k2 = el.find("k2")
        if _c_k2 is not None:
            _res = K2._from_sdf(_c_k2, version)
            if isinstance(_res, SDFError):
                return _res.extend("k2")
            _k2 = _res
        else:
            _k2 = None
        _c_k3 = el.find("k3")
        if _c_k3 is not None:
            _res = K3._from_sdf(_c_k3, version)
            if isinstance(_res, SDFError):
                return _res.extend("k3")
            _k3 = _res
        else:
            _k3 = None
        _c_p1 = el.find("p1")
        if _c_p1 is not None:
            _res = P1._from_sdf(_c_p1, version)
            if isinstance(_res, SDFError):
                return _res.extend("p1")
            _p1 = _res
        else:
            _p1 = None
        _c_p2 = el.find("p2")
        if _c_p2 is not None:
            _res = P2._from_sdf(_c_p2, version)
            if isinstance(_res, SDFError):
                return _res.extend("p2")
            _p2 = _res
        else:
            _p2 = None
        _c_center = el.find("center")
        if _c_center is not None:
            _res = DistortionCenter._from_sdf(_c_center, version)
            if isinstance(_res, SDFError):
                return _res.extend("center")
            _center = _res
        else:
            _center = None
        return cls(sdf_version=version, k1=_k1, k2=_k2, k3=_k3, p1=_p1, p2=_p2, center=_center)


class OpticalFrameId(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _optical_frame_id = _text
        if isinstance(_optical_frame_id, SDFError):
            return _optical_frame_id
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            if _optical_frame_id != "":
                return SDFError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, optical_frame_id=_optical_frame_id)


class CameraInfoTopic(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _camera_info_topic = _text
        if isinstance(_camera_info_topic, SDFError):
            return _camera_info_topic
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            if _camera_info_topic != "__default__":
                return SDFError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, camera_info_topic=_camera_info_topic)


class VisibilityMask(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4294967295
        _visibility_mask = _parse_uint32(_text)
        if isinstance(_visibility_mask, SDFError):
            return _visibility_mask
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            if _visibility_mask != 4294967295:
                return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_mask=_visibility_mask)


class SegmentationType(BaseModel):
    def __init__(self, sdf_version: str, segmentation_type: str = "semantic"):
        self.__version__ = sdf_version
        self.segmentation_type = segmentation_type

    def to_version(self, target_version: str) -> "SegmentationType":
        if self.segmentation_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.9)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "semantic"
        _segmentation_type = _text
        if isinstance(_segmentation_type, SDFError):
            return _segmentation_type
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            if _segmentation_type != "semantic":
                return SDFError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, segmentation_type=_segmentation_type)


class BoxType(BaseModel):
    def __init__(self, sdf_version: str, box_type: str = "2d"):
        self.__version__ = sdf_version
        self.box_type = box_type

    def to_version(self, target_version: str) -> "BoxType":
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "2d"
        _box_type = _text
        if isinstance(_box_type, SDFError):
            return _box_type
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            if _box_type != "2d":
                return SDFError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, box_type=_box_type)


class Triggered(BaseModel):
    def __init__(self, sdf_version: str, triggered: bool = False):
        self.__version__ = sdf_version
        self.triggered = triggered

    def to_version(self, target_version: str) -> "Triggered":
        if self.triggered is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.9)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _triggered = str(_text).strip().lower() == 'true'
        if isinstance(_triggered, SDFError):
            return _triggered
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            if _triggered != False:
                return SDFError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, triggered=_triggered)


class TriggerTopic(BaseModel):
    def __init__(self, sdf_version: str, trigger_topic: str = ""):
        self.__version__ = sdf_version
        self.trigger_topic = trigger_topic

    def to_version(self, target_version: str) -> "TriggerTopic":
        if self.trigger_topic is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.9)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _trigger_topic = _text
        if isinstance(_trigger_topic, SDFError):
            return _trigger_topic
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            if _trigger_topic != "":
                return SDFError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, trigger_topic=_trigger_topic)


class Camera(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        horizontal_fov: "HorizontalFov" = None,
        image: "CameraImage" = None,
        clip: "Clip" = None,
        save: "Save" = None,
        depth_camera: "DepthCamera" = None,
        pose: "CameraPose" = None,
        noise: "Noise" = None,
        lens: "Lens" = None,
        distortion: "Distortion" = None,
        frame: List["Frame"] = None,
        optical_frame_id: "OpticalFrameId" = None,
        camera_info_topic: "CameraInfoTopic" = None,
        visibility_mask: "VisibilityMask" = None,
        segmentation_type: "SegmentationType" = None,
        box_type: "BoxType" = None,
        triggered: "Triggered" = None,
        trigger_topic: "TriggerTopic" = None
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
        self.lens = lens
        self.distortion = distortion
        self.frame = frame or []
        self.optical_frame_id = optical_frame_id
        self.camera_info_topic = camera_info_topic
        self.visibility_mask = visibility_mask
        self.segmentation_type = segmentation_type
        self.box_type = box_type
        self.triggered = triggered
        self.trigger_topic = trigger_topic

    def to_version(self, target_version: str) -> "Camera":
        if self.name is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.3)")
        if self.pose is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.3)")
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.lens is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'lens' is not supported in SDF version {target_version} (added in 1.5)")
        if self.distortion is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'distortion' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        if self.segmentation_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.9)")
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
        if self.triggered is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.9)")
        if self.trigger_topic is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["horizontal_fov"] = self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        kwargs["save"] = self.save.to_version(target_version) if self.save is not None else None
        kwargs["depth_camera"] = self.depth_camera.to_version(target_version) if self.depth_camera is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["lens"] = self.lens.to_version(target_version) if self.lens is not None else None
        kwargs["distortion"] = self.distortion.to_version(target_version) if self.distortion is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["optical_frame_id"] = self.optical_frame_id.to_version(target_version) if self.optical_frame_id is not None else None
        kwargs["camera_info_topic"] = self.camera_info_topic.to_version(target_version) if self.camera_info_topic is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        kwargs["segmentation_type"] = self.segmentation_type.to_version(target_version) if self.segmentation_type is not None else None
        kwargs["box_type"] = self.box_type.to_version(target_version) if self.box_type is not None else None
        kwargs["triggered"] = self.triggered.to_version(target_version) if self.triggered is not None else None
        kwargs["trigger_topic"] = self.trigger_topic.to_version(target_version) if self.trigger_topic is not None else None
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
        if self.image is None:
            self.image = CameraImage(sdf_version=version)
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.clip is None:
            self.clip = Clip(sdf_version=version)
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
        if self.lens is not None:
            el.append(self.lens.to_sdf(version))
        if self.distortion is not None:
            el.append(self.distortion.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.optical_frame_id is not None:
            el.append(self.optical_frame_id.to_sdf(version))
        if self.camera_info_topic is not None:
            el.append(self.camera_info_topic.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        if self.segmentation_type is not None:
            el.append(self.segmentation_type.to_sdf(version))
        if self.box_type is not None:
            el.append(self.box_type.to_sdf(version))
        if self.triggered is not None:
            el.append(self.triggered.to_sdf(version))
        if self.trigger_topic is not None:
            el.append(self.trigger_topic.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        if _name is not None and cmp_version(version, "1.3") < 0:
            if _name != "__default__":
                return SDFError(f"'name' is not supported in SDF version {version} (added in 1.3)")
        _c_horizontal_fov = el.find("horizontal_fov")
        if _c_horizontal_fov is not None:
            _res = HorizontalFov._from_sdf(_c_horizontal_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal_fov")
            _horizontal_fov = _res
        else:
            _horizontal_fov = None
        _c_image = el.find("image")
        if _c_image is not None:
            _res = CameraImage._from_sdf(_c_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        else:
            _res = CameraImage._from_sdf(ET.Element("image"), version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        _c_clip = el.find("clip")
        if _c_clip is not None:
            _res = Clip._from_sdf(_c_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        else:
            _res = Clip._from_sdf(ET.Element("clip"), version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        _c_save = el.find("save")
        if _c_save is not None:
            _res = Save._from_sdf(_c_save, version)
            if isinstance(_res, SDFError):
                return _res.extend("save")
            _save = _res
        else:
            _save = None
        _c_depth_camera = el.find("depth_camera")
        if _c_depth_camera is not None:
            _res = DepthCamera._from_sdf(_c_depth_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("depth_camera")
            _depth_camera = _res
        else:
            _depth_camera = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = CameraPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.3)")
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_lens = el.find("lens")
        if _c_lens is not None:
            _res = Lens._from_sdf(_c_lens, version)
            if isinstance(_res, SDFError):
                return _res.extend("lens")
            _lens = _res
        else:
            _lens = None
        if _lens is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'lens' is not supported in SDF version {version} (added in 1.5)")
        _c_distortion = el.find("distortion")
        if _c_distortion is not None:
            _res = Distortion._from_sdf(_c_distortion, version)
            if isinstance(_res, SDFError):
                return _res.extend("distortion")
            _distortion = _res
        else:
            _distortion = None
        if _distortion is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'distortion' is not supported in SDF version {version} (added in 1.5)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_optical_frame_id = el.find("optical_frame_id")
        if _c_optical_frame_id is not None:
            _res = OpticalFrameId._from_sdf(_c_optical_frame_id, version)
            if isinstance(_res, SDFError):
                return _res.extend("optical_frame_id")
            _optical_frame_id = _res
        else:
            _optical_frame_id = None
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        _c_camera_info_topic = el.find("camera_info_topic")
        if _c_camera_info_topic is not None:
            _res = CameraInfoTopic._from_sdf(_c_camera_info_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera_info_topic")
            _camera_info_topic = _res
        else:
            _camera_info_topic = None
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        _c_visibility_mask = el.find("visibility_mask")
        if _c_visibility_mask is not None:
            _res = VisibilityMask._from_sdf(_c_visibility_mask, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_mask")
            _visibility_mask = _res
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        _c_segmentation_type = el.find("segmentation_type")
        if _c_segmentation_type is not None:
            _res = SegmentationType._from_sdf(_c_segmentation_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("segmentation_type")
            _segmentation_type = _res
        else:
            _segmentation_type = None
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        _c_box_type = el.find("box_type")
        if _c_box_type is not None:
            _res = BoxType._from_sdf(_c_box_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("box_type")
            _box_type = _res
        else:
            _box_type = None
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        _c_triggered = el.find("triggered")
        if _c_triggered is not None:
            _res = Triggered._from_sdf(_c_triggered, version)
            if isinstance(_res, SDFError):
                return _res.extend("triggered")
            _triggered = _res
        else:
            _triggered = None
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        _c_trigger_topic = el.find("trigger_topic")
        if _c_trigger_topic is not None:
            _res = TriggerTopic._from_sdf(_c_trigger_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("trigger_topic")
            _trigger_topic = _res
        else:
            _trigger_topic = None
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, name=_name, horizontal_fov=_horizontal_fov, image=_image, clip=_clip, save=_save, depth_camera=_depth_camera, pose=_pose, noise=_noise, lens=_lens, distortion=_distortion, frame=_frame, optical_frame_id=_optical_frame_id, camera_info_topic=_camera_info_topic, visibility_mask=_visibility_mask, segmentation_type=_segmentation_type, box_type=_box_type, triggered=_triggered, trigger_topic=_trigger_topic)


class Samples(BaseModel):
    def __init__(self, sdf_version: str, samples: int = 640):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "Samples":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 640
        _samples = _parse_uint32(_text)
        if isinstance(_samples, SDFError):
            return _samples
        return cls(sdf_version=version, samples=_samples)


class Resolution(BaseModel):
    def __init__(self, sdf_version: str, resolution: float = 1):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Resolution":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _resolution = _parse_double(_text)
        if isinstance(_resolution, SDFError):
            return _resolution
        return cls(sdf_version=version, resolution=_resolution)


class MinAngle(BaseModel):
    def __init__(self, sdf_version: str, min_angle: float = 0):
        self.__version__ = sdf_version
        self.min_angle = min_angle

    def to_version(self, target_version: str) -> "MinAngle":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min_angle = _parse_double(_text)
        if isinstance(_min_angle, SDFError):
            return _min_angle
        return cls(sdf_version=version, min_angle=_min_angle)


class MaxAngle(BaseModel):
    def __init__(self, sdf_version: str, max_angle: float = 0):
        self.__version__ = sdf_version
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "MaxAngle":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max_angle = _parse_double(_text)
        if isinstance(_max_angle, SDFError):
            return _max_angle
        return cls(sdf_version=version, max_angle=_max_angle)


class Horizontal(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        samples: "Samples" = None,
        resolution: "Resolution" = None,
        min_angle: "MinAngle" = None,
        max_angle: "MaxAngle" = None
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "Horizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples.to_version(target_version) if self.samples is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        kwargs["min_angle"] = self.min_angle.to_version(target_version) if self.min_angle is not None else None
        kwargs["max_angle"] = self.max_angle.to_version(target_version) if self.max_angle is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.samples is not None:
            el.append(self.samples.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        if self.min_angle is not None:
            el.append(self.min_angle.to_sdf(version))
        if self.max_angle is not None:
            el.append(self.max_angle.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_samples = el.find("samples")
        if _c_samples is not None:
            _res = Samples._from_sdf(_c_samples, version)
            if isinstance(_res, SDFError):
                return _res.extend("samples")
            _samples = _res
        else:
            _samples = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = Resolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        _c_min_angle = el.find("min_angle")
        if _c_min_angle is not None:
            _res = MinAngle._from_sdf(_c_min_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_angle")
            _min_angle = _res
        else:
            _min_angle = None
        _c_max_angle = el.find("max_angle")
        if _c_max_angle is not None:
            _res = MaxAngle._from_sdf(_c_max_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_angle")
            _max_angle = _res
        else:
            _max_angle = None
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class VerticalSamples(BaseModel):
    def __init__(self, sdf_version: str, samples: int = 1):
        self.__version__ = sdf_version
        self.samples = samples

    def to_version(self, target_version: str) -> "VerticalSamples":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _samples = _parse_uint32(_text)
        if isinstance(_samples, SDFError):
            return _samples
        return cls(sdf_version=version, samples=_samples)


class Vertical(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        samples: "VerticalSamples" = None,
        resolution: "Resolution" = None,
        min_angle: "MinAngle" = None,
        max_angle: "MaxAngle" = None
    ):
        self.__version__ = sdf_version
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_version(self, target_version: str) -> "Vertical":
        kwargs = {"sdf_version": target_version}
        kwargs["samples"] = self.samples.to_version(target_version) if self.samples is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        kwargs["min_angle"] = self.min_angle.to_version(target_version) if self.min_angle is not None else None
        kwargs["max_angle"] = self.max_angle.to_version(target_version) if self.max_angle is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.samples is not None:
            el.append(self.samples.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        if self.min_angle is not None:
            el.append(self.min_angle.to_sdf(version))
        if self.max_angle is not None:
            el.append(self.max_angle.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_samples = el.find("samples")
        if _c_samples is not None:
            _res = VerticalSamples._from_sdf(_c_samples, version)
            if isinstance(_res, SDFError):
                return _res.extend("samples")
            _samples = _res
        else:
            _samples = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = Resolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        _c_min_angle = el.find("min_angle")
        if _c_min_angle is not None:
            _res = MinAngle._from_sdf(_c_min_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_angle")
            _min_angle = _res
        else:
            _min_angle = None
        _c_max_angle = el.find("max_angle")
        if _c_max_angle is not None:
            _res = MaxAngle._from_sdf(_c_max_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_angle")
            _max_angle = _res
        else:
            _max_angle = None
        return cls(sdf_version=version, samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class Scan(BaseModel):
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
        if self.horizontal is None:
            self.horizontal = Horizontal(sdf_version=version)
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_horizontal = el.find("horizontal")
        if _c_horizontal is not None:
            _res = Horizontal._from_sdf(_c_horizontal, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        else:
            _res = Horizontal._from_sdf(ET.Element("horizontal"), version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        _c_vertical = el.find("vertical")
        if _c_vertical is not None:
            _res = Vertical._from_sdf(_c_vertical, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical")
            _vertical = _res
        else:
            _vertical = None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Min(BaseModel):
    def __init__(self, sdf_version: str, min: float = 0):
        self.__version__ = sdf_version
        self.min = min

    def to_version(self, target_version: str) -> "Min":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min = _parse_double(_text)
        if isinstance(_min, SDFError):
            return _min
        return cls(sdf_version=version, min=_min)


class Max(BaseModel):
    def __init__(self, sdf_version: str, max: float = 0):
        self.__version__ = sdf_version
        self.max = max

    def to_version(self, target_version: str) -> "Max":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _max = _parse_double(_text)
        if isinstance(_max, SDFError):
            return _max
        return cls(sdf_version=version, max=_max)


class RangeResolution(BaseModel):
    def __init__(self, sdf_version: str, resolution: float = 0):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "RangeResolution":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _resolution = _parse_double(_text)
        if isinstance(_resolution, SDFError):
            return _resolution
        return cls(sdf_version=version, resolution=_resolution)


class Range(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        min: "Min" = None,
        max: "Max" = None,
        resolution: "RangeResolution" = None
    ):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Range":
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min.to_version(target_version) if self.min is not None else None
        kwargs["max"] = self.max.to_version(target_version) if self.max is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.min is not None:
            el.append(self.min.to_sdf(version))
        if self.max is not None:
            el.append(self.max.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_min = el.find("min")
        if _c_min is not None:
            _res = Min._from_sdf(_c_min, version)
            if isinstance(_res, SDFError):
                return _res.extend("min")
            _min = _res
        else:
            _min = None
        _c_max = el.find("max")
        if _c_max is not None:
            _res = Max._from_sdf(_c_max, version)
            if isinstance(_res, SDFError):
                return _res.extend("max")
            _max = _res
        else:
            _max = None
        _c_resolution = el.find("resolution")
        if _c_resolution is not None:
            _res = RangeResolution._from_sdf(_c_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("resolution")
            _resolution = _res
        else:
            _resolution = None
        return cls(sdf_version=version, min=_min, max=_max, resolution=_resolution)


class Ray(BaseModel):
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
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
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
        if self.scan is None:
            self.scan = Scan(sdf_version=version)
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is None:
            self.range = Range(sdf_version=version)
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_scan = el.find("scan")
        if _c_scan is not None:
            _res = Scan._from_sdf(_c_scan, version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        else:
            _res = Scan._from_sdf(ET.Element("scan"), version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        _c_range = el.find("range")
        if _c_range is not None:
            _res = Range._from_sdf(_c_range, version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        else:
            _res = Range._from_sdf(ET.Element("range"), version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_visibility_mask = el.find("visibility_mask")
        if _c_visibility_mask is not None:
            _res = VisibilityMask._from_sdf(_c_visibility_mask, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_mask")
            _visibility_mask = _res
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)


class ContactCollision(BaseModel):
    def __init__(self, sdf_version: str, collision: str = "__default__"):
        self.__version__ = sdf_version
        self.collision = collision

    def to_version(self, target_version: str) -> "ContactCollision":
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = self.collision
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision")
        if self.collision is not None:
            el.text = self.collision
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _collision = _text
        if isinstance(_collision, SDFError):
            return _collision
        return cls(sdf_version=version, collision=_collision)


class Topic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = "__default_topic__"):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default_topic__"
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


class SensorContact(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        collision: "ContactCollision" = None,
        topic: "Topic" = None
    ):
        self.__version__ = sdf_version
        self.collision = collision
        self.topic = topic

    def to_version(self, target_version: str) -> "SensorContact":
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = self.collision.to_version(target_version) if self.collision is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.collision is not None:
            el.append(self.collision.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_collision = el.find("collision")
        if _c_collision is not None:
            _res = ContactCollision._from_sdf(_c_collision, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collision = _res
        else:
            _collision = None
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = Topic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        return cls(sdf_version=version, collision=_collision, topic=_topic)


class Rfidtag(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Rfid(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class AlwaysOn(BaseModel):
    def __init__(self, sdf_version: str, always_on: bool = False):
        self.__version__ = sdf_version
        self.always_on = always_on

    def to_version(self, target_version: str) -> "AlwaysOn":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _always_on = str(_text).strip().lower() == 'true'
        if isinstance(_always_on, SDFError):
            return _always_on
        return cls(sdf_version=version, always_on=_always_on)


class UpdateRate(BaseModel):
    def __init__(self, sdf_version: str, update_rate: float = 0):
        self.__version__ = sdf_version
        self.update_rate = update_rate

    def to_version(self, target_version: str) -> "UpdateRate":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _update_rate = _parse_double(_text)
        if isinstance(_update_rate, SDFError):
            return _update_rate
        return cls(sdf_version=version, update_rate=_update_rate)


class Visualize(BaseModel):
    def __init__(self, sdf_version: str, visualize: bool = False):
        self.__version__ = sdf_version
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Visualize":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _visualize = str(_text).strip().lower() == 'true'
        if isinstance(_visualize, SDFError):
            return _visualize
        return cls(sdf_version=version, visualize=_visualize)


class SensorPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "SensorPose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class SensorTopic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = "__default"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "SensorTopic":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default"
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


class BiasMean(BaseModel):
    def __init__(self, sdf_version: str, bias_mean: float = 0.0):
        self.__version__ = sdf_version
        self.bias_mean = bias_mean

    def to_version(self, target_version: str) -> "BiasMean":
        kwargs = {"sdf_version": target_version}
        kwargs["bias_mean"] = self.bias_mean
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bias_mean")
        if self.bias_mean is not None:
            el.text = str(self.bias_mean)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _bias_mean = _parse_double(_text)
        if isinstance(_bias_mean, SDFError):
            return _bias_mean
        return cls(sdf_version=version, bias_mean=_bias_mean)


class BiasStddev(BaseModel):
    def __init__(self, sdf_version: str, bias_stddev: float = 0.0):
        self.__version__ = sdf_version
        self.bias_stddev = bias_stddev

    def to_version(self, target_version: str) -> "BiasStddev":
        kwargs = {"sdf_version": target_version}
        kwargs["bias_stddev"] = self.bias_stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bias_stddev")
        if self.bias_stddev is not None:
            el.text = str(self.bias_stddev)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _bias_stddev = _parse_double(_text)
        if isinstance(_bias_stddev, SDFError):
            return _bias_stddev
        return cls(sdf_version=version, bias_stddev=_bias_stddev)


class Rate(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev

    def to_version(self, target_version: str) -> "Rate":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rate")
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        return cls(sdf_version=version, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev)


class Accel(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev

    def to_version(self, target_version: str) -> "Accel":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("accel")
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        return cls(sdf_version=version, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev)


class ImuNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        rate: "Rate" = None,
        accel: "Accel" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.rate = rate
        self.accel = accel

    def to_version(self, target_version: str) -> "ImuNoise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["rate"] = self.rate.to_version(target_version) if self.rate is not None else None
        kwargs["accel"] = self.accel.to_version(target_version) if self.accel is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.rate is None:
            self.rate = Rate(sdf_version=version)
        if self.rate is not None:
            el.append(self.rate.to_sdf(version))
        if self.accel is None:
            self.accel = Accel(sdf_version=version)
        if self.accel is not None:
            el.append(self.accel.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        _c_rate = el.find("rate")
        if _c_rate is not None:
            _res = Rate._from_sdf(_c_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("rate")
            _rate = _res
        else:
            _res = Rate._from_sdf(ET.Element("rate"), version)
            if isinstance(_res, SDFError):
                return _res.extend("rate")
            _rate = _res
        _c_accel = el.find("accel")
        if _c_accel is not None:
            _res = Accel._from_sdf(_c_accel, version)
            if isinstance(_res, SDFError):
                return _res.extend("accel")
            _accel = _res
        else:
            _res = Accel._from_sdf(ET.Element("accel"), version)
            if isinstance(_res, SDFError):
                return _res.extend("accel")
            _accel = _res
        return cls(sdf_version=version, type=_type, rate=_rate, accel=_accel)


class Precision(BaseModel):
    def __init__(self, sdf_version: str, precision: float = 0.0):
        self.__version__ = sdf_version
        self.precision = precision

    def to_version(self, target_version: str) -> "Precision":
        kwargs = {"sdf_version": target_version}
        kwargs["precision"] = self.precision
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("precision")
        if self.precision is not None:
            el.text = str(self.precision)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _precision = _parse_double(_text)
        if isinstance(_precision, SDFError):
            return _precision
        return cls(sdf_version=version, precision=_precision)


class DynamicBiasCorrelationTime(BaseModel):
    def __init__(self, sdf_version: str, dynamic_bias_correlation_time: float = 0.0):
        self.__version__ = sdf_version
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time

    def to_version(self, target_version: str) -> "DynamicBiasCorrelationTime":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamic_bias_correlation_time")
        if self.dynamic_bias_correlation_time is not None:
            el.text = str(self.dynamic_bias_correlation_time)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _dynamic_bias_correlation_time = _parse_double(_text)
        if isinstance(_dynamic_bias_correlation_time, SDFError):
            return _dynamic_bias_correlation_time
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            if _dynamic_bias_correlation_time != 0.0:
                return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, dynamic_bias_correlation_time=_dynamic_bias_correlation_time)


class DynamicBiasStddev(BaseModel):
    def __init__(self, sdf_version: str, dynamic_bias_stddev: float = 0.0):
        self.__version__ = sdf_version
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "DynamicBiasStddev":
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamic_bias_stddev")
        if self.dynamic_bias_stddev is not None:
            el.text = str(self.dynamic_bias_stddev)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _dynamic_bias_stddev = _parse_double(_text)
        if isinstance(_dynamic_bias_stddev, SDFError):
            return _dynamic_bias_stddev
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            if _dynamic_bias_stddev != 0.0:
                return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, dynamic_bias_stddev=_dynamic_bias_stddev)


class XNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "XNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class X(BaseModel):
    def __init__(self, sdf_version: str, noise: "XNoise" = None):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = XNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class YNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "YNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class Y(BaseModel):
    def __init__(self, sdf_version: str, noise: "YNoise" = None):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = YNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class ZNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "ZNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class Z(BaseModel):
    def __init__(self, sdf_version: str, noise: "ZNoise" = None):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = ZNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class LinearAcceleration(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class AngularVelocity(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class EnableOrientation(BaseModel):
    def __init__(self, sdf_version: str, enable_orientation: bool = True):
        self.__version__ = sdf_version
        self.enable_orientation = enable_orientation

    def to_version(self, target_version: str) -> "EnableOrientation":
        if self.enable_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.6)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _enable_orientation = str(_text).strip().lower() == 'true'
        if isinstance(_enable_orientation, SDFError):
            return _enable_orientation
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            if _enable_orientation != True:
                return SDFError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, enable_orientation=_enable_orientation)


class Localization(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "CUSTOM"
        _localization = _text
        if isinstance(_localization, SDFError):
            return _localization
        return cls(sdf_version=version, localization=_localization)


class CustomRpy(BaseModel):
    def __init__(self, sdf_version: str, custom_rpy: _SDFVector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if custom_rpy is None:
            custom_rpy = _SDFVector3.from_sdf("0 0 0")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _custom_rpy = _SDFVector3._from_sdf(_text, version)
        if isinstance(_custom_rpy, SDFError):
            return _custom_rpy
        _parent_frame = el.get("parent_frame", "")
        if isinstance(_parent_frame, SDFError):
            return _parent_frame.extend("@parent_frame")
        return cls(sdf_version=version, custom_rpy=_custom_rpy, parent_frame=_parent_frame)


class GravDirX(BaseModel):
    def __init__(self, sdf_version: str, grav_dir_x: _SDFVector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if grav_dir_x is None:
            grav_dir_x = _SDFVector3.from_sdf("1 0 0")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 0 0"
        _grav_dir_x = _SDFVector3._from_sdf(_text, version)
        if isinstance(_grav_dir_x, SDFError):
            return _grav_dir_x
        _parent_frame = el.get("parent_frame", "")
        if isinstance(_parent_frame, SDFError):
            return _parent_frame.extend("@parent_frame")
        return cls(sdf_version=version, grav_dir_x=_grav_dir_x, parent_frame=_parent_frame)


class OrientationReferenceFrame(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_localization = el.find("localization")
        if _c_localization is not None:
            _res = Localization._from_sdf(_c_localization, version)
            if isinstance(_res, SDFError):
                return _res.extend("localization")
            _localization = _res
        else:
            _localization = None
        _c_custom_rpy = el.find("custom_rpy")
        if _c_custom_rpy is not None:
            _res = CustomRpy._from_sdf(_c_custom_rpy, version)
            if isinstance(_res, SDFError):
                return _res.extend("custom_rpy")
            _custom_rpy = _res
        else:
            _custom_rpy = None
        _c_grav_dir_x = el.find("grav_dir_x")
        if _c_grav_dir_x is not None:
            _res = GravDirX._from_sdf(_c_grav_dir_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("grav_dir_x")
            _grav_dir_x = _res
        else:
            _grav_dir_x = None
        return cls(sdf_version=version, localization=_localization, custom_rpy=_custom_rpy, grav_dir_x=_grav_dir_x)


class Imu(BaseModel):
    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}, {"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}]}]

    def __init__(
        self,
        sdf_version: str,
        topic: "Topic" = None,
        noise: "ImuNoise" = None,
        linear_acceleration: "LinearAcceleration" = None,
        angular_velocity: "AngularVelocity" = None,
        enable_orientation: "EnableOrientation" = None,
        orientation_reference_frame: "OrientationReferenceFrame" = None
    ):
        self.__version__ = sdf_version
        self.topic = topic
        self.noise = noise
        self.linear_acceleration = linear_acceleration
        self.angular_velocity = angular_velocity
        self.enable_orientation = enable_orientation
        self.orientation_reference_frame = orientation_reference_frame

    def to_version(self, target_version: str) -> "Imu":
        if self.topic is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'topic' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.noise is not None and cmp_version(target_version, "1.6") >= 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (removed in 1.6)")
        if self.linear_acceleration is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'linear_acceleration' is not supported in SDF version {target_version} (added in 1.5)")
        if self.angular_velocity is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'angular_velocity' is not supported in SDF version {target_version} (added in 1.5)")
        if self.enable_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        if self.orientation_reference_frame is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'orientation_reference_frame' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["linear_acceleration"] = self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None else None
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if self.angular_velocity is not None else None
        kwargs["enable_orientation"] = self.enable_orientation.to_version(target_version) if self.enable_orientation is not None else None
        kwargs["orientation_reference_frame"] = self.orientation_reference_frame.to_version(target_version) if self.orientation_reference_frame is not None else None
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
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf(version))
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
        if self.enable_orientation is not None:
            el.append(self.enable_orientation.to_sdf(version))
        if self.orientation_reference_frame is not None:
            el.append(self.orientation_reference_frame.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = Topic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = ImuNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_linear_acceleration = el.find("linear_acceleration")
        if _c_linear_acceleration is not None:
            _res = LinearAcceleration._from_sdf(_c_linear_acceleration, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_acceleration")
            _linear_acceleration = _res
        else:
            _linear_acceleration = None
        if _linear_acceleration is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'linear_acceleration' is not supported in SDF version {version} (added in 1.5)")
        _c_angular_velocity = el.find("angular_velocity")
        if _c_angular_velocity is not None:
            _res = AngularVelocity._from_sdf(_c_angular_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular_velocity")
            _angular_velocity = _res
        else:
            _angular_velocity = None
        if _angular_velocity is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'angular_velocity' is not supported in SDF version {version} (added in 1.5)")
        _c_enable_orientation = el.find("enable_orientation")
        if _c_enable_orientation is not None:
            _res = EnableOrientation._from_sdf(_c_enable_orientation, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_orientation")
            _enable_orientation = _res
        else:
            _enable_orientation = None
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        _c_orientation_reference_frame = el.find("orientation_reference_frame")
        if _c_orientation_reference_frame is not None:
            _res = OrientationReferenceFrame._from_sdf(_c_orientation_reference_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("orientation_reference_frame")
            _orientation_reference_frame = _res
        else:
            _orientation_reference_frame = None
        if _orientation_reference_frame is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'orientation_reference_frame' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, topic=_topic, noise=_noise, linear_acceleration=_linear_acceleration, angular_velocity=_angular_velocity, enable_orientation=_enable_orientation, orientation_reference_frame=_orientation_reference_frame)


class HorizontalNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "HorizontalNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class PositionSensingHorizontal(BaseModel):
    def __init__(self, sdf_version: str, noise: "HorizontalNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "PositionSensingHorizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = HorizontalNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class VerticalNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "VerticalNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class PositionSensingVertical(BaseModel):
    def __init__(self, sdf_version: str, noise: "VerticalNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "PositionSensingVertical":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = VerticalNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class PositionSensing(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "PositionSensingHorizontal" = None,
        vertical: "PositionSensingVertical" = None
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_horizontal = el.find("horizontal")
        if _c_horizontal is not None:
            _res = PositionSensingHorizontal._from_sdf(_c_horizontal, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        else:
            _horizontal = None
        _c_vertical = el.find("vertical")
        if _c_vertical is not None:
            _res = PositionSensingVertical._from_sdf(_c_vertical, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical")
            _vertical = _res
        else:
            _vertical = None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class VelocitySensingHorizontal(BaseModel):
    def __init__(self, sdf_version: str, noise: "HorizontalNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VelocitySensingHorizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = HorizontalNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class VelocitySensingVertical(BaseModel):
    def __init__(self, sdf_version: str, noise: "VerticalNoise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VelocitySensingVertical":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = VerticalNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class VelocitySensing(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "VelocitySensingHorizontal" = None,
        vertical: "VelocitySensingVertical" = None
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_horizontal = el.find("horizontal")
        if _c_horizontal is not None:
            _res = VelocitySensingHorizontal._from_sdf(_c_horizontal, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal")
            _horizontal = _res
        else:
            _horizontal = None
        _c_vertical = el.find("vertical")
        if _c_vertical is not None:
            _res = VelocitySensingVertical._from_sdf(_c_vertical, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical")
            _vertical = _res
        else:
            _vertical = None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Gps(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_position_sensing = el.find("position_sensing")
        if _c_position_sensing is not None:
            _res = PositionSensing._from_sdf(_c_position_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("position_sensing")
            _position_sensing = _res
        else:
            _position_sensing = None
        _c_velocity_sensing = el.find("velocity_sensing")
        if _c_velocity_sensing is not None:
            _res = VelocitySensing._from_sdf(_c_velocity_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity_sensing")
            _velocity_sensing = _res
        else:
            _velocity_sensing = None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class SonarMax(BaseModel):
    def __init__(self, sdf_version: str, max: float = 1.0):
        self.__version__ = sdf_version
        self.max = max

    def to_version(self, target_version: str) -> "SonarMax":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _max = _parse_double(_text)
        if isinstance(_max, SDFError):
            return _max
        return cls(sdf_version=version, max=_max)


class SonarRadius(BaseModel):
    def __init__(self, sdf_version: str, radius: float = 0.5):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "SonarRadius":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.5
        _radius = _parse_double(_text)
        if isinstance(_radius, SDFError):
            return _radius
        return cls(sdf_version=version, radius=_radius)


class SonarGeometry(BaseModel):
    def __init__(self, sdf_version: str, geometry: str = "cone"):
        self.__version__ = sdf_version
        self.geometry = geometry

    def to_version(self, target_version: str) -> "SonarGeometry":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["geometry"] = self.geometry
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("geometry")
        if self.geometry is not None:
            el.text = self.geometry
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "cone"
        _geometry = _text
        if isinstance(_geometry, SDFError):
            return _geometry
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            if _geometry != "cone":
                return SDFError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, geometry=_geometry)


class Sonar(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        min: "Min" = None,
        max: "SonarMax" = None,
        radius: "SonarRadius" = None,
        geometry: "SonarGeometry" = None
    ):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.radius = radius
        self.geometry = geometry

    def to_version(self, target_version: str) -> "Sonar":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_min = el.find("min")
        if _c_min is not None:
            _res = Min._from_sdf(_c_min, version)
            if isinstance(_res, SDFError):
                return _res.extend("min")
            _min = _res
        else:
            _min = None
        _c_max = el.find("max")
        if _c_max is not None:
            _res = SonarMax._from_sdf(_c_max, version)
            if isinstance(_res, SDFError):
                return _res.extend("max")
            _max = _res
        else:
            _max = None
        _c_radius = el.find("radius")
        if _c_radius is not None:
            _res = SonarRadius._from_sdf(_c_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("radius")
            _radius = _res
        else:
            _radius = None
        _c_geometry = el.find("geometry")
        if _c_geometry is not None:
            _res = SonarGeometry._from_sdf(_c_geometry, version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        else:
            _geometry = None
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, min=_min, max=_max, radius=_radius, geometry=_geometry)


class Essid(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "wireless"
        _essid = _text
        if isinstance(_essid, SDFError):
            return _essid
        return cls(sdf_version=version, essid=_essid)


class Frequency(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2442
        _frequency = _parse_double(_text)
        if isinstance(_frequency, SDFError):
            return _frequency
        return cls(sdf_version=version, frequency=_frequency)


class MinFrequency(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2412
        _min_frequency = _parse_double(_text)
        if isinstance(_min_frequency, SDFError):
            return _min_frequency
        return cls(sdf_version=version, min_frequency=_min_frequency)


class MaxFrequency(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2484
        _max_frequency = _parse_double(_text)
        if isinstance(_max_frequency, SDFError):
            return _max_frequency
        return cls(sdf_version=version, max_frequency=_max_frequency)


class Gain(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2.5
        _gain = _parse_double(_text)
        if isinstance(_gain, SDFError):
            return _gain
        return cls(sdf_version=version, gain=_gain)


class Power(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 14.50
        _power = _parse_double(_text)
        if isinstance(_power, SDFError):
            return _power
        return cls(sdf_version=version, power=_power)


class Sensitivity(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -90
        _sensitivity = _parse_double(_text)
        if isinstance(_sensitivity, SDFError):
            return _sensitivity
        return cls(sdf_version=version, sensitivity=_sensitivity)


class Transceiver(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_essid = el.find("essid")
        if _c_essid is not None:
            _res = Essid._from_sdf(_c_essid, version)
            if isinstance(_res, SDFError):
                return _res.extend("essid")
            _essid = _res
        else:
            _essid = None
        _c_frequency = el.find("frequency")
        if _c_frequency is not None:
            _res = Frequency._from_sdf(_c_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("frequency")
            _frequency = _res
        else:
            _frequency = None
        _c_min_frequency = el.find("min_frequency")
        if _c_min_frequency is not None:
            _res = MinFrequency._from_sdf(_c_min_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_frequency")
            _min_frequency = _res
        else:
            _min_frequency = None
        _c_max_frequency = el.find("max_frequency")
        if _c_max_frequency is not None:
            _res = MaxFrequency._from_sdf(_c_max_frequency, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_frequency")
            _max_frequency = _res
        else:
            _max_frequency = None
        _c_gain = el.find("gain")
        if _c_gain is not None:
            _res = Gain._from_sdf(_c_gain, version)
            if isinstance(_res, SDFError):
                return _res.extend("gain")
            _gain = _res
        else:
            _gain = None
        _c_power = el.find("power")
        if _c_power is not None:
            _res = Power._from_sdf(_c_power, version)
            if isinstance(_res, SDFError):
                return _res.extend("power")
            _power = _res
        else:
            _power = None
        _c_sensitivity = el.find("sensitivity")
        if _c_sensitivity is not None:
            _res = Sensitivity._from_sdf(_c_sensitivity, version)
            if isinstance(_res, SDFError):
                return _res.extend("sensitivity")
            _sensitivity = _res
        else:
            _sensitivity = None
        return cls(sdf_version=version, essid=_essid, frequency=_frequency, min_frequency=_min_frequency, max_frequency=_max_frequency, gain=_gain, power=_power, sensitivity=_sensitivity)


class ForceTorqueFrame(BaseModel):
    def __init__(self, sdf_version: str, frame: str = "parent"):
        self.__version__ = sdf_version
        self.frame = frame

    def to_version(self, target_version: str) -> "ForceTorqueFrame":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "parent"
        _frame = _text
        if isinstance(_frame, SDFError):
            return _frame
        return cls(sdf_version=version, frame=_frame)


class MeasureDirection(BaseModel):
    def __init__(self, sdf_version: str, measure_direction: str = "child_to_parent"):
        self.__version__ = sdf_version
        self.measure_direction = measure_direction

    def to_version(self, target_version: str) -> "MeasureDirection":
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "child_to_parent"
        _measure_direction = _text
        if isinstance(_measure_direction, SDFError):
            return _measure_direction
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            if _measure_direction != "child_to_parent":
                return SDFError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, measure_direction=_measure_direction)


class Torque(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class Force(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class ForceTorque(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        frame: "ForceTorqueFrame" = None,
        measure_direction: "MeasureDirection" = None,
        torque: "Torque" = None,
        force: "Force" = None
    ):
        self.__version__ = sdf_version
        self.frame = frame
        self.measure_direction = measure_direction
        self.torque = torque
        self.force = force

    def to_version(self, target_version: str) -> "ForceTorque":
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        if self.torque is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {target_version} (added in 1.7)")
        if self.force is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame.to_version(target_version) if self.frame is not None else None
        kwargs["measure_direction"] = self.measure_direction.to_version(target_version) if self.measure_direction is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
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
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_frame = el.find("frame")
        if _c_frame is not None:
            _res = ForceTorqueFrame._from_sdf(_c_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame = _res
        else:
            _frame = None
        _c_measure_direction = el.find("measure_direction")
        if _c_measure_direction is not None:
            _res = MeasureDirection._from_sdf(_c_measure_direction, version)
            if isinstance(_res, SDFError):
                return _res.extend("measure_direction")
            _measure_direction = _res
        else:
            _measure_direction = None
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        _c_torque = el.find("torque")
        if _c_torque is not None:
            _res = Torque._from_sdf(_c_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("torque")
            _torque = _res
        else:
            _torque = None
        if _torque is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'torque' is not supported in SDF version {version} (added in 1.7)")
        _c_force = el.find("force")
        if _c_force is not None:
            _res = Force._from_sdf(_c_force, version)
            if isinstance(_res, SDFError):
                return _res.extend("force")
            _force = _res
        else:
            _force = None
        if _force is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'force' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, frame=_frame, measure_direction=_measure_direction, torque=_torque, force=_force)


class VerticalPositionNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "VerticalPositionNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class VerticalPosition(BaseModel):
    def __init__(self, sdf_version: str, noise: "VerticalPositionNoise" = None):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = VerticalPositionNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class VerticalVelocityNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        precision: "Precision" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.dynamic_bias_stddev = dynamic_bias_stddev

    def to_version(self, target_version: str) -> "VerticalVelocityNoise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, precision=_precision, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev)


class VerticalVelocity(BaseModel):
    def __init__(self, sdf_version: str, noise: "VerticalVelocityNoise" = None):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = VerticalVelocityNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class Altimeter(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_vertical_position = el.find("vertical_position")
        if _c_vertical_position is not None:
            _res = VerticalPosition._from_sdf(_c_vertical_position, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical_position")
            _vertical_position = _res
        else:
            _vertical_position = None
        _c_vertical_velocity = el.find("vertical_velocity")
        if _c_vertical_velocity is not None:
            _res = VerticalVelocity._from_sdf(_c_vertical_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical_velocity")
            _vertical_velocity = _res
        else:
            _vertical_velocity = None
        return cls(sdf_version=version, vertical_position=_vertical_position, vertical_velocity=_vertical_velocity)


class Magnetometer(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class LogicalCameraNear(BaseModel):
    def __init__(self, sdf_version: str, near: float = 0):
        self.__version__ = sdf_version
        self.near = near

    def to_version(self, target_version: str) -> "LogicalCameraNear":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _near = _parse_double(_text)
        if isinstance(_near, SDFError):
            return _near
        return cls(sdf_version=version, near=_near)


class LogicalCameraFar(BaseModel):
    def __init__(self, sdf_version: str, far: float = 1):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "LogicalCameraFar":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _far = _parse_double(_text)
        if isinstance(_far, SDFError):
            return _far
        return cls(sdf_version=version, far=_far)


class AspectRatio(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _aspect_ratio = _parse_double(_text)
        if isinstance(_aspect_ratio, SDFError):
            return _aspect_ratio
        return cls(sdf_version=version, aspect_ratio=_aspect_ratio)


class LogicalCameraHorizontalFov(BaseModel):
    def __init__(self, sdf_version: str, horizontal_fov: float = 1):
        self.__version__ = sdf_version
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "LogicalCameraHorizontalFov":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal_fov"] = self.horizontal_fov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal_fov")
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _horizontal_fov = _parse_double(_text)
        if isinstance(_horizontal_fov, SDFError):
            return _horizontal_fov
        return cls(sdf_version=version, horizontal_fov=_horizontal_fov)


class LogicalCamera(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        near: "LogicalCameraNear" = None,
        far: "LogicalCameraFar" = None,
        aspect_ratio: "AspectRatio" = None,
        horizontal_fov: "LogicalCameraHorizontalFov" = None
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_near = el.find("near")
        if _c_near is not None:
            _res = LogicalCameraNear._from_sdf(_c_near, version)
            if isinstance(_res, SDFError):
                return _res.extend("near")
            _near = _res
        else:
            _near = None
        _c_far = el.find("far")
        if _c_far is not None:
            _res = LogicalCameraFar._from_sdf(_c_far, version)
            if isinstance(_res, SDFError):
                return _res.extend("far")
            _far = _res
        else:
            _far = None
        _c_aspect_ratio = el.find("aspect_ratio")
        if _c_aspect_ratio is not None:
            _res = AspectRatio._from_sdf(_c_aspect_ratio, version)
            if isinstance(_res, SDFError):
                return _res.extend("aspect_ratio")
            _aspect_ratio = _res
        else:
            _aspect_ratio = None
        _c_horizontal_fov = el.find("horizontal_fov")
        if _c_horizontal_fov is not None:
            _res = LogicalCameraHorizontalFov._from_sdf(_c_horizontal_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal_fov")
            _horizontal_fov = _res
        else:
            _horizontal_fov = None
        return cls(sdf_version=version, near=_near, far=_far, aspect_ratio=_aspect_ratio, horizontal_fov=_horizontal_fov)


class ReferenceAltitude(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _reference_altitude = _parse_double(_text)
        if isinstance(_reference_altitude, SDFError):
            return _reference_altitude
        return cls(sdf_version=version, reference_altitude=_reference_altitude)


class PressureNoise(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        type: str = "none",
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        bias_mean: "BiasMean" = None,
        bias_stddev: "BiasStddev" = None,
        dynamic_bias_stddev: "DynamicBiasStddev" = None,
        dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
        precision: "Precision" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.dynamic_bias_stddev = dynamic_bias_stddev
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.precision = precision

    def to_version(self, target_version: str) -> "PressureNoise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["bias_mean"] = self.bias_mean.to_version(target_version) if self.bias_mean is not None else None
        kwargs["bias_stddev"] = self.bias_stddev.to_version(target_version) if self.bias_stddev is not None else None
        kwargs["dynamic_bias_stddev"] = self.dynamic_bias_stddev.to_version(target_version) if self.dynamic_bias_stddev is not None else None
        kwargs["dynamic_bias_correlation_time"] = self.dynamic_bias_correlation_time.to_version(target_version) if self.dynamic_bias_correlation_time is not None else None
        kwargs["precision"] = self.precision.to_version(target_version) if self.precision is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf(version))
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf(version))
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf(version))
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf(version))
        if self.precision is not None:
            el.append(self.precision.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_bias_mean = el.find("bias_mean")
        if _c_bias_mean is not None:
            _res = BiasMean._from_sdf(_c_bias_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_mean")
            _bias_mean = _res
        else:
            _bias_mean = None
        _c_bias_stddev = el.find("bias_stddev")
        if _c_bias_stddev is not None:
            _res = BiasStddev._from_sdf(_c_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("bias_stddev")
            _bias_stddev = _res
        else:
            _bias_stddev = None
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        if _c_dynamic_bias_stddev is not None:
            _res = DynamicBiasStddev._from_sdf(_c_dynamic_bias_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _res
        else:
            _dynamic_bias_stddev = None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        if _c_dynamic_bias_correlation_time is not None:
            _res = DynamicBiasCorrelationTime._from_sdf(_c_dynamic_bias_correlation_time, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _res
        else:
            _dynamic_bias_correlation_time = None
        _c_precision = el.find("precision")
        if _c_precision is not None:
            _res = Precision._from_sdf(_c_precision, version)
            if isinstance(_res, SDFError):
                return _res.extend("precision")
            _precision = _res
        else:
            _precision = None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev, dynamic_bias_stddev=_dynamic_bias_stddev, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, precision=_precision)


class Pressure(BaseModel):
    def __init__(self, sdf_version: str, noise: "PressureNoise" = None):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = PressureNoise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        return cls(sdf_version=version, noise=_noise)


class AirPressure(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_reference_altitude = el.find("reference_altitude")
        if _c_reference_altitude is not None:
            _res = ReferenceAltitude._from_sdf(_c_reference_altitude, version)
            if isinstance(_res, SDFError):
                return _res.extend("reference_altitude")
            _reference_altitude = _res
        else:
            _reference_altitude = None
        _c_pressure = el.find("pressure")
        if _c_pressure is not None:
            _res = Pressure._from_sdf(_c_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("pressure")
            _pressure = _res
        else:
            _pressure = None
        return cls(sdf_version=version, reference_altitude=_reference_altitude, pressure=_pressure)


class Lidar(BaseModel):
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
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
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
        if self.scan is None:
            self.scan = Scan(sdf_version=version)
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is None:
            self.range = Range(sdf_version=version)
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_scan = el.find("scan")
        if _c_scan is not None:
            _res = Scan._from_sdf(_c_scan, version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        else:
            _res = Scan._from_sdf(ET.Element("scan"), version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        _c_range = el.find("range")
        if _c_range is not None:
            _res = Range._from_sdf(_c_range, version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        else:
            _res = Range._from_sdf(ET.Element("range"), version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        _c_visibility_mask = el.find("visibility_mask")
        if _c_visibility_mask is not None:
            _res = VisibilityMask._from_sdf(_c_visibility_mask, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_mask")
            _visibility_mask = _res
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)


class Navsat(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_position_sensing = el.find("position_sensing")
        if _c_position_sensing is not None:
            _res = PositionSensing._from_sdf(_c_position_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("position_sensing")
            _position_sensing = _res
        else:
            _position_sensing = None
        _c_velocity_sensing = el.find("velocity_sensing")
        if _c_velocity_sensing is not None:
            _res = VelocitySensing._from_sdf(_c_velocity_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity_sensing")
            _velocity_sensing = _res
        else:
            _velocity_sensing = None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class EnableMetrics(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _enable_metrics = str(_text).strip().lower() == 'true'
        if isinstance(_enable_metrics, SDFError):
            return _enable_metrics
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            if _enable_metrics != False:
                return SDFError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, enable_metrics=_enable_metrics)


class Sensor(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "__default__",
        plugin: List["Plugin"] = None,
        camera: "Camera" = None,
        ray: "Ray" = None,
        contact: "SensorContact" = None,
        rfidtag: "Rfidtag" = None,
        rfid: "Rfid" = None,
        always_on: "AlwaysOn" = None,
        update_rate: "UpdateRate" = None,
        visualize: "Visualize" = None,
        pose: "SensorPose" = None,
        topic: "SensorTopic" = None,
        imu: "Imu" = None,
        gps: "Gps" = None,
        sonar: "Sonar" = None,
        transceiver: "Transceiver" = None,
        force_torque: "ForceTorque" = None,
        frame: List["Frame"] = None,
        altimeter: "Altimeter" = None,
        magnetometer: "Magnetometer" = None,
        logical_camera: "LogicalCamera" = None,
        air_pressure: "AirPressure" = None,
        lidar: "Lidar" = None,
        navsat: "Navsat" = None,
        enable_metrics: "EnableMetrics" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.plugin = plugin or []
        self.camera = camera
        self.ray = ray
        self.contact = contact
        self.rfidtag = rfidtag
        self.rfid = rfid
        self.always_on = always_on
        self.update_rate = update_rate
        self.visualize = visualize
        self.pose = pose
        self.topic = topic
        self.imu = imu
        self.gps = gps
        self.sonar = sonar
        self.transceiver = transceiver
        self.force_torque = force_torque
        self.frame = frame or []
        self.altimeter = altimeter
        self.magnetometer = magnetometer
        self.logical_camera = logical_camera
        self.air_pressure = air_pressure
        self.lidar = lidar
        self.navsat = navsat
        self.enable_metrics = enable_metrics

    def to_version(self, target_version: str) -> "Sensor":
        if self.imu is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'imu' is not supported in SDF version {target_version} (added in 1.3)")
        if self.gps is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gps' is not supported in SDF version {target_version} (added in 1.4)")
        if self.sonar is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'sonar' is not supported in SDF version {target_version} (added in 1.4)")
        if self.transceiver is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'transceiver' is not supported in SDF version {target_version} (added in 1.4)")
        if self.force_torque is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'force_torque' is not supported in SDF version {target_version} (added in 1.4)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.altimeter is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'altimeter' is not supported in SDF version {target_version} (added in 1.5)")
        if self.magnetometer is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'magnetometer' is not supported in SDF version {target_version} (added in 1.5)")
        if self.logical_camera is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'logical_camera' is not supported in SDF version {target_version} (added in 1.5)")
        if self.air_pressure is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'air_pressure' is not supported in SDF version {target_version} (added in 1.6)")
        if self.lidar is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'lidar' is not supported in SDF version {target_version} (added in 1.6)")
        if self.navsat is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'navsat' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        kwargs["ray"] = self.ray.to_version(target_version) if self.ray is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["rfidtag"] = self.rfidtag.to_version(target_version) if self.rfidtag is not None else None
        kwargs["rfid"] = self.rfid.to_version(target_version) if self.rfid is not None else None
        kwargs["always_on"] = self.always_on.to_version(target_version) if self.always_on is not None else None
        kwargs["update_rate"] = self.update_rate.to_version(target_version) if self.update_rate is not None else None
        kwargs["visualize"] = self.visualize.to_version(target_version) if self.visualize is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["imu"] = self.imu.to_version(target_version) if self.imu is not None else None
        kwargs["gps"] = self.gps.to_version(target_version) if self.gps is not None else None
        kwargs["sonar"] = self.sonar.to_version(target_version) if self.sonar is not None else None
        kwargs["transceiver"] = self.transceiver.to_version(target_version) if self.transceiver is not None else None
        kwargs["force_torque"] = self.force_torque.to_version(target_version) if self.force_torque is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["altimeter"] = self.altimeter.to_version(target_version) if self.altimeter is not None else None
        kwargs["magnetometer"] = self.magnetometer.to_version(target_version) if self.magnetometer is not None else None
        kwargs["logical_camera"] = self.logical_camera.to_version(target_version) if self.logical_camera is not None else None
        kwargs["air_pressure"] = self.air_pressure.to_version(target_version) if self.air_pressure is not None else None
        kwargs["lidar"] = self.lidar.to_version(target_version) if self.lidar is not None else None
        kwargs["navsat"] = self.navsat.to_version(target_version) if self.navsat is not None else None
        kwargs["enable_metrics"] = self.enable_metrics.to_version(target_version) if self.enable_metrics is not None else None
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
        if self.always_on is not None:
            el.append(self.always_on.to_sdf(version))
        if self.update_rate is not None:
            el.append(self.update_rate.to_sdf(version))
        if self.visualize is not None:
            el.append(self.visualize.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.imu is not None:
            el.append(self.imu.to_sdf(version))
        if self.gps is not None:
            el.append(self.gps.to_sdf(version))
        if self.sonar is not None:
            el.append(self.sonar.to_sdf(version))
        if self.transceiver is not None:
            el.append(self.transceiver.to_sdf(version))
        if self.force_torque is not None:
            el.append(self.force_torque.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.altimeter is not None:
            el.append(self.altimeter.to_sdf(version))
        if self.magnetometer is not None:
            el.append(self.magnetometer.to_sdf(version))
        if self.logical_camera is not None:
            el.append(self.logical_camera.to_sdf(version))
        if self.air_pressure is not None:
            el.append(self.air_pressure.to_sdf(version))
        if self.lidar is not None:
            el.append(self.lidar.to_sdf(version))
        if self.navsat is not None:
            el.append(self.navsat.to_sdf(version))
        if self.enable_metrics is not None:
            el.append(self.enable_metrics.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _type = el.get("type", "__default__")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _c_camera = el.find("camera")
        if _c_camera is not None:
            _res = Camera._from_sdf(_c_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera")
            _camera = _res
        else:
            _camera = None
        _c_ray = el.find("ray")
        if _c_ray is not None:
            _res = Ray._from_sdf(_c_ray, version)
            if isinstance(_res, SDFError):
                return _res.extend("ray")
            _ray = _res
        else:
            _ray = None
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = SensorContact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _c_rfidtag = el.find("rfidtag")
        if _c_rfidtag is not None:
            _res = Rfidtag._from_sdf(_c_rfidtag, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfidtag")
            _rfidtag = _res
        else:
            _rfidtag = None
        _c_rfid = el.find("rfid")
        if _c_rfid is not None:
            _res = Rfid._from_sdf(_c_rfid, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfid")
            _rfid = _res
        else:
            _rfid = None
        _c_always_on = el.find("always_on")
        if _c_always_on is not None:
            _res = AlwaysOn._from_sdf(_c_always_on, version)
            if isinstance(_res, SDFError):
                return _res.extend("always_on")
            _always_on = _res
        else:
            _always_on = None
        _c_update_rate = el.find("update_rate")
        if _c_update_rate is not None:
            _res = UpdateRate._from_sdf(_c_update_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("update_rate")
            _update_rate = _res
        else:
            _update_rate = None
        _c_visualize = el.find("visualize")
        if _c_visualize is not None:
            _res = Visualize._from_sdf(_c_visualize, version)
            if isinstance(_res, SDFError):
                return _res.extend("visualize")
            _visualize = _res
        else:
            _visualize = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = SensorPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = SensorTopic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        _c_imu = el.find("imu")
        if _c_imu is not None:
            _res = Imu._from_sdf(_c_imu, version)
            if isinstance(_res, SDFError):
                return _res.extend("imu")
            _imu = _res
        else:
            _imu = None
        if _imu is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'imu' is not supported in SDF version {version} (added in 1.3)")
        _c_gps = el.find("gps")
        if _c_gps is not None:
            _res = Gps._from_sdf(_c_gps, version)
            if isinstance(_res, SDFError):
                return _res.extend("gps")
            _gps = _res
        else:
            _gps = None
        if _gps is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'gps' is not supported in SDF version {version} (added in 1.4)")
        _c_sonar = el.find("sonar")
        if _c_sonar is not None:
            _res = Sonar._from_sdf(_c_sonar, version)
            if isinstance(_res, SDFError):
                return _res.extend("sonar")
            _sonar = _res
        else:
            _sonar = None
        if _sonar is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'sonar' is not supported in SDF version {version} (added in 1.4)")
        _c_transceiver = el.find("transceiver")
        if _c_transceiver is not None:
            _res = Transceiver._from_sdf(_c_transceiver, version)
            if isinstance(_res, SDFError):
                return _res.extend("transceiver")
            _transceiver = _res
        else:
            _transceiver = None
        if _transceiver is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'transceiver' is not supported in SDF version {version} (added in 1.4)")
        _c_force_torque = el.find("force_torque")
        if _c_force_torque is not None:
            _res = ForceTorque._from_sdf(_c_force_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("force_torque")
            _force_torque = _res
        else:
            _force_torque = None
        if _force_torque is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'force_torque' is not supported in SDF version {version} (added in 1.4)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_altimeter = el.find("altimeter")
        if _c_altimeter is not None:
            _res = Altimeter._from_sdf(_c_altimeter, version)
            if isinstance(_res, SDFError):
                return _res.extend("altimeter")
            _altimeter = _res
        else:
            _altimeter = None
        if _altimeter is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'altimeter' is not supported in SDF version {version} (added in 1.5)")
        _c_magnetometer = el.find("magnetometer")
        if _c_magnetometer is not None:
            _res = Magnetometer._from_sdf(_c_magnetometer, version)
            if isinstance(_res, SDFError):
                return _res.extend("magnetometer")
            _magnetometer = _res
        else:
            _magnetometer = None
        if _magnetometer is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'magnetometer' is not supported in SDF version {version} (added in 1.5)")
        _c_logical_camera = el.find("logical_camera")
        if _c_logical_camera is not None:
            _res = LogicalCamera._from_sdf(_c_logical_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("logical_camera")
            _logical_camera = _res
        else:
            _logical_camera = None
        if _logical_camera is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'logical_camera' is not supported in SDF version {version} (added in 1.5)")
        _c_air_pressure = el.find("air_pressure")
        if _c_air_pressure is not None:
            _res = AirPressure._from_sdf(_c_air_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("air_pressure")
            _air_pressure = _res
        else:
            _air_pressure = None
        if _air_pressure is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'air_pressure' is not supported in SDF version {version} (added in 1.6)")
        _c_lidar = el.find("lidar")
        if _c_lidar is not None:
            _res = Lidar._from_sdf(_c_lidar, version)
            if isinstance(_res, SDFError):
                return _res.extend("lidar")
            _lidar = _res
        else:
            _lidar = None
        if _lidar is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'lidar' is not supported in SDF version {version} (added in 1.6)")
        _c_navsat = el.find("navsat")
        if _c_navsat is not None:
            _res = Navsat._from_sdf(_c_navsat, version)
            if isinstance(_res, SDFError):
                return _res.extend("navsat")
            _navsat = _res
        else:
            _navsat = None
        if _navsat is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'navsat' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_metrics = el.find("enable_metrics")
        if _c_enable_metrics is not None:
            _res = EnableMetrics._from_sdf(_c_enable_metrics, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_metrics")
            _enable_metrics = _res
        else:
            _enable_metrics = None
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, name=_name, type=_type, plugin=_plugin, camera=_camera, ray=_ray, contact=_contact, rfidtag=_rfidtag, rfid=_rfid, always_on=_always_on, update_rate=_update_rate, visualize=_visualize, pose=_pose, topic=_topic, imu=_imu, gps=_gps, sonar=_sonar, transceiver=_transceiver, force_torque=_force_torque, frame=_frame, altimeter=_altimeter, magnetometer=_magnetometer, logical_camera=_logical_camera, air_pressure=_air_pressure, lidar=_lidar, navsat=_navsat, enable_metrics=_enable_metrics)


class ProjectorTexture(BaseModel):
    def __init__(self, sdf_version: str, texture: str = "__default__"):
        self.__version__ = sdf_version
        self.texture = texture

    def to_version(self, target_version: str) -> "ProjectorTexture":
        kwargs = {"sdf_version": target_version}
        kwargs["texture"] = self.texture
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("texture")
        if self.texture is not None:
            el.text = self.texture
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _texture = _text
        if isinstance(_texture, SDFError):
            return _texture
        return cls(sdf_version=version, texture=_texture)


class ProjectorPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "ProjectorPose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Fov(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.785
        _fov = _parse_double(_text)
        if isinstance(_fov, SDFError):
            return _fov
        return cls(sdf_version=version, fov=_fov)


class NearClip(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.1
        _near_clip = _parse_double(_text)
        if isinstance(_near_clip, SDFError):
            return _near_clip
        return cls(sdf_version=version, near_clip=_near_clip)


class FarClip(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10.0
        _far_clip = _parse_double(_text)
        if isinstance(_far_clip, SDFError):
            return _far_clip
        return cls(sdf_version=version, far_clip=_far_clip)


class Projector(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        plugin: List["Plugin"] = None,
        texture: "ProjectorTexture" = None,
        pose: "ProjectorPose" = None,
        fov: "Fov" = None,
        near_clip: "NearClip" = None,
        far_clip: "FarClip" = None,
        frame: List["Frame"] = None,
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
        self.frame = frame or []
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "Projector":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
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
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
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
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.visibility_flags is not None:
            el.append(self.visibility_flags.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _c_texture = el.find("texture")
        if _c_texture is not None:
            _res = ProjectorTexture._from_sdf(_c_texture, version)
            if isinstance(_res, SDFError):
                return _res.extend("texture")
            _texture = _res
        else:
            _texture = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = ProjectorPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_fov = el.find("fov")
        if _c_fov is not None:
            _res = Fov._from_sdf(_c_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("fov")
            _fov = _res
        else:
            _fov = None
        _c_near_clip = el.find("near_clip")
        if _c_near_clip is not None:
            _res = NearClip._from_sdf(_c_near_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("near_clip")
            _near_clip = _res
        else:
            _near_clip = None
        _c_far_clip = el.find("far_clip")
        if _c_far_clip is not None:
            _res = FarClip._from_sdf(_c_far_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("far_clip")
            _far_clip = _res
        else:
            _far_clip = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_visibility_flags = el.find("visibility_flags")
        if _c_visibility_flags is not None:
            _res = VisibilityFlags._from_sdf(_c_visibility_flags, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_flags")
            _visibility_flags = _res
        else:
            _visibility_flags = None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, name=_name, plugin=_plugin, texture=_texture, pose=_pose, fov=_fov, near_clip=_near_clip, far_clip=_far_clip, frame=_frame, visibility_flags=_visibility_flags)


class Gravity(BaseModel):
    def __init__(self, sdf_version: str, gravity: bool = True):
        self.__version__ = sdf_version
        self.gravity = gravity

    def to_version(self, target_version: str) -> "Gravity":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _gravity = str(_text).strip().lower() == 'true'
        if isinstance(_gravity, SDFError):
            return _gravity
        return cls(sdf_version=version, gravity=_gravity)


class SelfCollide(BaseModel):
    def __init__(self, sdf_version: str, self_collide: bool = False):
        self.__version__ = sdf_version
        self.self_collide = self_collide

    def to_version(self, target_version: str) -> "SelfCollide":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _self_collide = str(_text).strip().lower() == 'true'
        if isinstance(_self_collide, SDFError):
            return _self_collide
        return cls(sdf_version=version, self_collide=_self_collide)


class Kinematic(BaseModel):
    def __init__(self, sdf_version: str, kinematic: bool = False):
        self.__version__ = sdf_version
        self.kinematic = kinematic

    def to_version(self, target_version: str) -> "Kinematic":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _kinematic = str(_text).strip().lower() == 'true'
        if isinstance(_kinematic, SDFError):
            return _kinematic
        return cls(sdf_version=version, kinematic=_kinematic)


class LinkPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "LinkPose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Linear(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _linear = _parse_double(_text)
        if isinstance(_linear, SDFError):
            return _linear
        return cls(sdf_version=version, linear=_linear)


class Angular(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _angular = _parse_double(_text)
        if isinstance(_angular, SDFError):
            return _angular
        return cls(sdf_version=version, angular=_angular)


class VelocityDecay(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_linear = el.find("linear")
        if _c_linear is not None:
            _res = Linear._from_sdf(_c_linear, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear")
            _linear = _res
        else:
            _linear = None
        _c_angular = el.find("angular")
        if _c_angular is not None:
            _res = Angular._from_sdf(_c_angular, version)
            if isinstance(_res, SDFError):
                return _res.extend("angular")
            _angular = _res
        else:
            _angular = None
        return cls(sdf_version=version, linear=_linear, angular=_angular)


class Pitch(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _pitch = _parse_double(_text)
        if isinstance(_pitch, SDFError):
            return _pitch
        return cls(sdf_version=version, pitch=_pitch)


class AudioSourceGain(BaseModel):
    def __init__(self, sdf_version: str, gain: float = 1.0):
        self.__version__ = sdf_version
        self.gain = gain

    def to_version(self, target_version: str) -> "AudioSourceGain":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _gain = _parse_double(_text)
        if isinstance(_gain, SDFError):
            return _gain
        return cls(sdf_version=version, gain=_gain)


class AudioSourceContact(BaseModel):
    def __init__(self, sdf_version: str, collision: List["ContactCollision"] = None):
        self.__version__ = sdf_version
        self.collision = collision or []

    def to_version(self, target_version: str) -> "AudioSourceContact":
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = [c.to_version(target_version) for c in (self.collision or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        for item in (self.collision or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _collision = []
        for c in el.findall("collision"):
            _res = ContactCollision._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collision.append(_res)
        return cls(sdf_version=version, collision=_collision)


class Loop(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _loop = str(_text).strip().lower() == 'true'
        if isinstance(_loop, SDFError):
            return _loop
        return cls(sdf_version=version, loop=_loop)


class AudioSourcePose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "AudioSourcePose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class AudioSource(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        uri: "Uri" = None,
        pitch: "Pitch" = None,
        gain: "AudioSourceGain" = None,
        contact: "AudioSourceContact" = None,
        loop: "Loop" = None,
        pose: "AudioSourcePose" = None,
        frame: List["Frame"] = None
    ):
        self.__version__ = sdf_version
        self.uri = uri
        self.pitch = pitch
        self.gain = gain
        self.contact = contact
        self.loop = loop
        self.pose = pose
        self.frame = frame or []

    def to_version(self, target_version: str) -> "AudioSource":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["pitch"] = self.pitch.to_version(target_version) if self.pitch is not None else None
        kwargs["gain"] = self.gain.to_version(target_version) if self.gain is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["loop"] = self.loop.to_version(target_version) if self.loop is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
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
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        _c_pitch = el.find("pitch")
        if _c_pitch is not None:
            _res = Pitch._from_sdf(_c_pitch, version)
            if isinstance(_res, SDFError):
                return _res.extend("pitch")
            _pitch = _res
        else:
            _pitch = None
        _c_gain = el.find("gain")
        if _c_gain is not None:
            _res = AudioSourceGain._from_sdf(_c_gain, version)
            if isinstance(_res, SDFError):
                return _res.extend("gain")
            _gain = _res
        else:
            _gain = None
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = AudioSourceContact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _c_loop = el.find("loop")
        if _c_loop is not None:
            _res = Loop._from_sdf(_c_loop, version)
            if isinstance(_res, SDFError):
                return _res.extend("loop")
            _loop = _res
        else:
            _loop = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = AudioSourcePose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, uri=_uri, pitch=_pitch, gain=_gain, contact=_contact, loop=_loop, pose=_pose, frame=_frame)


class MustBeBaseLink(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _must_be_base_link = str(_text).strip().lower() == 'true'
        if isinstance(_must_be_base_link, SDFError):
            return _must_be_base_link
        if _must_be_base_link is not None and cmp_version(version, "1.4") < 0:
            if _must_be_base_link != False:
                return SDFError(f"'must_be_base_link' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, must_be_base_link=_must_be_base_link)


class AudioSink(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Voltage(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _voltage = _parse_double(_text)
        if isinstance(_voltage, SDFError):
            return _voltage
        return cls(sdf_version=version, voltage=_voltage)


class Battery(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_voltage = el.find("voltage")
        if _c_voltage is not None:
            _res = Voltage._from_sdf(_c_voltage, version)
            if isinstance(_res, SDFError):
                return _res.extend("voltage")
            _voltage = _res
        else:
            _voltage = None
        return cls(sdf_version=version, name=_name, voltage=_voltage)


class EnableWind(BaseModel):
    def __init__(self, sdf_version: str, enable_wind: bool = False):
        self.__version__ = sdf_version
        self.enable_wind = enable_wind

    def to_version(self, target_version: str) -> "EnableWind":
        if self.enable_wind is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.6)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _enable_wind = str(_text).strip().lower() == 'true'
        if isinstance(_enable_wind, SDFError):
            return _enable_wind
        if _enable_wind is not None and cmp_version(version, "1.6") < 0:
            if _enable_wind != False:
                return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, enable_wind=_enable_wind)


class ParticleEmitterPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "ParticleEmitterPose":
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Emitting(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _emitting = str(_text).strip().lower() == 'true'
        if isinstance(_emitting, SDFError):
            return _emitting
        return cls(sdf_version=version, emitting=_emitting)


class Duration(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _duration = _parse_double(_text)
        if isinstance(_duration, SDFError):
            return _duration
        return cls(sdf_version=version, duration=_duration)


class ParticleSize(BaseModel):
    def __init__(self, sdf_version: str, particle_size: _SDFVector3 = None):
        self.__version__ = sdf_version
        if particle_size is None:
            particle_size = _SDFVector3.from_sdf("1 1 1")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _particle_size = _SDFVector3._from_sdf(_text, version)
        if isinstance(_particle_size, SDFError):
            return _particle_size
        return cls(sdf_version=version, particle_size=_particle_size)


class Lifetime(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 5
        _lifetime = _parse_double(_text)
        if isinstance(_lifetime, SDFError):
            return _lifetime
        return cls(sdf_version=version, lifetime=_lifetime)


class ParticleEmitterRate(BaseModel):
    def __init__(self, sdf_version: str, rate: float = 10):
        self.__version__ = sdf_version
        self.rate = rate

    def to_version(self, target_version: str) -> "ParticleEmitterRate":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _rate = _parse_double(_text)
        if isinstance(_rate, SDFError):
            return _rate
        return cls(sdf_version=version, rate=_rate)


class MinVelocity(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _min_velocity = _parse_double(_text)
        if isinstance(_min_velocity, SDFError):
            return _min_velocity
        return cls(sdf_version=version, min_velocity=_min_velocity)


class MaxVelocity(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _max_velocity = _parse_double(_text)
        if isinstance(_max_velocity, SDFError):
            return _max_velocity
        return cls(sdf_version=version, max_velocity=_max_velocity)


class ScaleRate(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _scale_rate = _parse_double(_text)
        if isinstance(_scale_rate, SDFError):
            return _scale_rate
        return cls(sdf_version=version, scale_rate=_scale_rate)


class ColorStart(BaseModel):
    def __init__(self, sdf_version: str, color_start: _SDFColor = None):
        self.__version__ = sdf_version
        if color_start is None:
            color_start = _SDFColor.from_sdf("1 1 1 1")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1 1"
        _color_start = _SDFColor._from_sdf(_text, version)
        if isinstance(_color_start, SDFError):
            return _color_start
        return cls(sdf_version=version, color_start=_color_start)


class ColorEnd(BaseModel):
    def __init__(self, sdf_version: str, color_end: _SDFColor = None):
        self.__version__ = sdf_version
        if color_end is None:
            color_end = _SDFColor.from_sdf("1 1 1 1")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1 1"
        _color_end = _SDFColor._from_sdf(_text, version)
        if isinstance(_color_end, SDFError):
            return _color_end
        return cls(sdf_version=version, color_end=_color_end)


class ColorRangeImage(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _color_range_image = _text
        if isinstance(_color_range_image, SDFError):
            return _color_range_image
        return cls(sdf_version=version, color_range_image=_color_range_image)


class ParticleEmitterTopic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = ""):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "ParticleEmitterTopic":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


class ParticleScatterRatio(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.65
        _particle_scatter_ratio = _parse_double(_text)
        if isinstance(_particle_scatter_ratio, SDFError):
            return _particle_scatter_ratio
        return cls(sdf_version=version, particle_scatter_ratio=_particle_scatter_ratio)


class ParticleEmitter(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "point",
        pose: "ParticleEmitterPose" = None,
        material: "Material" = None,
        emitting: "Emitting" = None,
        duration: "Duration" = None,
        size: "Size" = None,
        particle_size: "ParticleSize" = None,
        lifetime: "Lifetime" = None,
        rate: "ParticleEmitterRate" = None,
        min_velocity: "MinVelocity" = None,
        max_velocity: "MaxVelocity" = None,
        scale_rate: "ScaleRate" = None,
        color_start: "ColorStart" = None,
        color_end: "ColorEnd" = None,
        color_range_image: "ColorRangeImage" = None,
        topic: "ParticleEmitterTopic" = None,
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _type = el.get("type", "point")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = ParticleEmitterPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_material = el.find("material")
        if _c_material is not None:
            _res = Material._from_sdf(_c_material, version)
            if isinstance(_res, SDFError):
                return _res.extend("material")
            _material = _res
        else:
            _material = None
        _c_emitting = el.find("emitting")
        if _c_emitting is not None:
            _res = Emitting._from_sdf(_c_emitting, version)
            if isinstance(_res, SDFError):
                return _res.extend("emitting")
            _emitting = _res
        else:
            _emitting = None
        _c_duration = el.find("duration")
        if _c_duration is not None:
            _res = Duration._from_sdf(_c_duration, version)
            if isinstance(_res, SDFError):
                return _res.extend("duration")
            _duration = _res
        else:
            _duration = None
        _c_size = el.find("size")
        if _c_size is not None:
            _res = Size._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        _c_particle_size = el.find("particle_size")
        if _c_particle_size is not None:
            _res = ParticleSize._from_sdf(_c_particle_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("particle_size")
            _particle_size = _res
        else:
            _particle_size = None
        _c_lifetime = el.find("lifetime")
        if _c_lifetime is not None:
            _res = Lifetime._from_sdf(_c_lifetime, version)
            if isinstance(_res, SDFError):
                return _res.extend("lifetime")
            _lifetime = _res
        else:
            _lifetime = None
        _c_rate = el.find("rate")
        if _c_rate is not None:
            _res = ParticleEmitterRate._from_sdf(_c_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("rate")
            _rate = _res
        else:
            _rate = None
        _c_min_velocity = el.find("min_velocity")
        if _c_min_velocity is not None:
            _res = MinVelocity._from_sdf(_c_min_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_velocity")
            _min_velocity = _res
        else:
            _min_velocity = None
        _c_max_velocity = el.find("max_velocity")
        if _c_max_velocity is not None:
            _res = MaxVelocity._from_sdf(_c_max_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_velocity")
            _max_velocity = _res
        else:
            _max_velocity = None
        _c_scale_rate = el.find("scale_rate")
        if _c_scale_rate is not None:
            _res = ScaleRate._from_sdf(_c_scale_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale_rate")
            _scale_rate = _res
        else:
            _scale_rate = None
        _c_color_start = el.find("color_start")
        if _c_color_start is not None:
            _res = ColorStart._from_sdf(_c_color_start, version)
            if isinstance(_res, SDFError):
                return _res.extend("color_start")
            _color_start = _res
        else:
            _color_start = None
        _c_color_end = el.find("color_end")
        if _c_color_end is not None:
            _res = ColorEnd._from_sdf(_c_color_end, version)
            if isinstance(_res, SDFError):
                return _res.extend("color_end")
            _color_end = _res
        else:
            _color_end = None
        _c_color_range_image = el.find("color_range_image")
        if _c_color_range_image is not None:
            _res = ColorRangeImage._from_sdf(_c_color_range_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("color_range_image")
            _color_range_image = _res
        else:
            _color_range_image = None
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = ParticleEmitterTopic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        _c_particle_scatter_ratio = el.find("particle_scatter_ratio")
        if _c_particle_scatter_ratio is not None:
            _res = ParticleScatterRatio._from_sdf(_c_particle_scatter_ratio, version)
            if isinstance(_res, SDFError):
                return _res.extend("particle_scatter_ratio")
            _particle_scatter_ratio = _res
        else:
            _particle_scatter_ratio = None
        return cls(sdf_version=version, name=_name, type=_type, pose=_pose, material=_material, emitting=_emitting, duration=_duration, size=_size, particle_size=_particle_size, lifetime=_lifetime, rate=_rate, min_velocity=_min_velocity, max_velocity=_max_velocity, scale_rate=_scale_rate, color_start=_color_start, color_end=_color_end, color_range_image=_color_range_image, topic=_topic, particle_scatter_ratio=_particle_scatter_ratio)


class LightPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "LightPose":
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class LightCastShadows(BaseModel):
    def __init__(self, sdf_version: str, cast_shadows: bool = False):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows

    def to_version(self, target_version: str) -> "LightCastShadows":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _cast_shadows = str(_text).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows
        return cls(sdf_version=version, cast_shadows=_cast_shadows)


class LightDiffuse(BaseModel):
    def __init__(self, sdf_version: str, diffuse: _SDFColor = None):
        self.__version__ = sdf_version
        if diffuse is None:
            diffuse = _SDFColor.from_sdf("1 1 1 1")
        self.diffuse = diffuse

    def to_version(self, target_version: str) -> "LightDiffuse":
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
            el.text = self.diffuse.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1 1"
        _diffuse = _SDFColor._from_sdf(_text, version)
        if isinstance(_diffuse, SDFError):
            return _diffuse
        return cls(sdf_version=version, diffuse=_diffuse)


class LightSpecular(BaseModel):
    def __init__(self, sdf_version: str, specular: _SDFColor = None):
        self.__version__ = sdf_version
        if specular is None:
            specular = _SDFColor.from_sdf(".1 .1 .1 1")
        self.specular = specular

    def to_version(self, target_version: str) -> "LightSpecular":
        kwargs = {"sdf_version": target_version}
        kwargs["specular"] = self.specular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular")
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ".1 .1 .1 1"
        _specular = _SDFColor._from_sdf(_text, version)
        if isinstance(_specular, SDFError):
            return _specular
        return cls(sdf_version=version, specular=_specular)


class AttenuationRange(BaseModel):
    def __init__(self, sdf_version: str, range: float = 10):
        self.__version__ = sdf_version
        self.range = range

    def to_version(self, target_version: str) -> "AttenuationRange":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _range = _parse_double(_text)
        if isinstance(_range, SDFError):
            return _range
        return cls(sdf_version=version, range=_range)


class AttenuationLinear(BaseModel):
    def __init__(self, sdf_version: str, linear: float = 1):
        self.__version__ = sdf_version
        self.linear = linear

    def to_version(self, target_version: str) -> "AttenuationLinear":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _linear = _parse_double(_text)
        if isinstance(_linear, SDFError):
            return _linear
        return cls(sdf_version=version, linear=_linear)


class Constant(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _constant = _parse_double(_text)
        if isinstance(_constant, SDFError):
            return _constant
        return cls(sdf_version=version, constant=_constant)


class Quadratic(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _quadratic = _parse_double(_text)
        if isinstance(_quadratic, SDFError):
            return _quadratic
        return cls(sdf_version=version, quadratic=_quadratic)


class Attenuation(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        range: "AttenuationRange" = None,
        linear: "AttenuationLinear" = None,
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_range = el.find("range")
        if _c_range is not None:
            _res = AttenuationRange._from_sdf(_c_range, version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        else:
            _range = None
        _c_linear = el.find("linear")
        if _c_linear is not None:
            _res = AttenuationLinear._from_sdf(_c_linear, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear")
            _linear = _res
        else:
            _linear = None
        _c_constant = el.find("constant")
        if _c_constant is not None:
            _res = Constant._from_sdf(_c_constant, version)
            if isinstance(_res, SDFError):
                return _res.extend("constant")
            _constant = _res
        else:
            _constant = None
        _c_quadratic = el.find("quadratic")
        if _c_quadratic is not None:
            _res = Quadratic._from_sdf(_c_quadratic, version)
            if isinstance(_res, SDFError):
                return _res.extend("quadratic")
            _quadratic = _res
        else:
            _quadratic = None
        return cls(sdf_version=version, range=_range, linear=_linear, constant=_constant, quadratic=_quadratic)


class Direction(BaseModel):
    def __init__(self, sdf_version: str, direction: _SDFVector3 = None):
        self.__version__ = sdf_version
        if direction is None:
            direction = _SDFVector3.from_sdf("0 0 -1")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 -1"
        _direction = _SDFVector3._from_sdf(_text, version)
        if isinstance(_direction, SDFError):
            return _direction
        return cls(sdf_version=version, direction=_direction)


class InnerAngle(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _inner_angle = _parse_double(_text)
        if isinstance(_inner_angle, SDFError):
            return _inner_angle
        return cls(sdf_version=version, inner_angle=_inner_angle)


class OuterAngle(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _outer_angle = _parse_double(_text)
        if isinstance(_outer_angle, SDFError):
            return _outer_angle
        return cls(sdf_version=version, outer_angle=_outer_angle)


class Falloff(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _falloff = _parse_double(_text)
        if isinstance(_falloff, SDFError):
            return _falloff
        return cls(sdf_version=version, falloff=_falloff)


class Spot(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_inner_angle = el.find("inner_angle")
        if _c_inner_angle is not None:
            _res = InnerAngle._from_sdf(_c_inner_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("inner_angle")
            _inner_angle = _res
        else:
            _inner_angle = None
        _c_outer_angle = el.find("outer_angle")
        if _c_outer_angle is not None:
            _res = OuterAngle._from_sdf(_c_outer_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("outer_angle")
            _outer_angle = _res
        else:
            _outer_angle = None
        _c_falloff = el.find("falloff")
        if _c_falloff is not None:
            _res = Falloff._from_sdf(_c_falloff, version)
            if isinstance(_res, SDFError):
                return _res.extend("falloff")
            _falloff = _res
        else:
            _falloff = None
        return cls(sdf_version=version, inner_angle=_inner_angle, outer_angle=_outer_angle, falloff=_falloff)


class Intensity(BaseModel):
    def __init__(self, sdf_version: str, intensity: float = 1):
        self.__version__ = sdf_version
        self.intensity = intensity

    def to_version(self, target_version: str) -> "Intensity":
        if self.intensity is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.8)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _intensity = _parse_double(_text)
        if isinstance(_intensity, SDFError):
            return _intensity
        if _intensity is not None and cmp_version(version, "1.8") < 0:
            if _intensity != 1:
                return SDFError(f"'intensity' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, intensity=_intensity)


class LightOn(BaseModel):
    def __init__(self, sdf_version: str, light_on: bool = True):
        self.__version__ = sdf_version
        self.light_on = light_on

    def to_version(self, target_version: str) -> "LightOn":
        if self.light_on is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.8)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _light_on = str(_text).strip().lower() == 'true'
        if isinstance(_light_on, SDFError):
            return _light_on
        if _light_on is not None and cmp_version(version, "1.8") < 0:
            if _light_on != True:
                return SDFError(f"'light_on' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, light_on=_light_on)


class LightVisualize(BaseModel):
    def __init__(self, sdf_version: str, visualize: bool = True):
        self.__version__ = sdf_version
        self.visualize = visualize

    def to_version(self, target_version: str) -> "LightVisualize":
        if self.visualize is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.8)")
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _visualize = str(_text).strip().lower() == 'true'
        if isinstance(_visualize, SDFError):
            return _visualize
        if _visualize is not None and cmp_version(version, "1.8") < 0:
            if _visualize != True:
                return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, visualize=_visualize)


class Light(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "point",
        frame: List["Frame"] = None,
        pose: "LightPose" = None,
        cast_shadows: "LightCastShadows" = None,
        diffuse: "LightDiffuse" = None,
        specular: "LightSpecular" = None,
        attenuation: "Attenuation" = None,
        direction: "Direction" = None,
        spot: "Spot" = None,
        intensity: "Intensity" = None,
        light_on: "LightOn" = None,
        visualize: "LightVisualize" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.frame = frame or []
        self.pose = pose
        self.cast_shadows = cast_shadows
        self.diffuse = diffuse
        self.specular = specular
        self.attenuation = attenuation
        self.direction = direction
        self.spot = spot
        self.intensity = intensity
        self.light_on = light_on
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Light":
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.intensity is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.8)")
        if self.light_on is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.8)")
        if self.visualize is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.8)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["cast_shadows"] = self.cast_shadows.to_version(target_version) if self.cast_shadows is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["attenuation"] = self.attenuation.to_version(target_version) if self.attenuation is not None else None
        kwargs["direction"] = self.direction.to_version(target_version) if self.direction is not None else None
        kwargs["spot"] = self.spot.to_version(target_version) if self.spot is not None else None
        kwargs["intensity"] = self.intensity.to_version(target_version) if self.intensity is not None else None
        kwargs["light_on"] = self.light_on.to_version(target_version) if self.light_on is not None else None
        kwargs["visualize"] = self.visualize.to_version(target_version) if self.visualize is not None else None
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
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
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
        if self.intensity is not None:
            el.append(self.intensity.to_sdf(version))
        if self.light_on is not None:
            el.append(self.light_on.to_sdf(version))
        if self.visualize is not None:
            el.append(self.visualize.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _type = el.get("type", "point")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = LightPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_cast_shadows = el.find("cast_shadows")
        if _c_cast_shadows is not None:
            _res = LightCastShadows._from_sdf(_c_cast_shadows, version)
            if isinstance(_res, SDFError):
                return _res.extend("cast_shadows")
            _cast_shadows = _res
        else:
            _cast_shadows = None
        _c_diffuse = el.find("diffuse")
        if _c_diffuse is not None:
            _res = LightDiffuse._from_sdf(_c_diffuse, version)
            if isinstance(_res, SDFError):
                return _res.extend("diffuse")
            _diffuse = _res
        else:
            _diffuse = None
        _c_specular = el.find("specular")
        if _c_specular is not None:
            _res = LightSpecular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        _c_attenuation = el.find("attenuation")
        if _c_attenuation is not None:
            _res = Attenuation._from_sdf(_c_attenuation, version)
            if isinstance(_res, SDFError):
                return _res.extend("attenuation")
            _attenuation = _res
        else:
            _attenuation = None
        _c_direction = el.find("direction")
        if _c_direction is not None:
            _res = Direction._from_sdf(_c_direction, version)
            if isinstance(_res, SDFError):
                return _res.extend("direction")
            _direction = _res
        else:
            _direction = None
        _c_spot = el.find("spot")
        if _c_spot is not None:
            _res = Spot._from_sdf(_c_spot, version)
            if isinstance(_res, SDFError):
                return _res.extend("spot")
            _spot = _res
        else:
            _spot = None
        _c_intensity = el.find("intensity")
        if _c_intensity is not None:
            _res = Intensity._from_sdf(_c_intensity, version)
            if isinstance(_res, SDFError):
                return _res.extend("intensity")
            _intensity = _res
        else:
            _intensity = None
        if _intensity is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'intensity' is not supported in SDF version {version} (added in 1.8)")
        _c_light_on = el.find("light_on")
        if _c_light_on is not None:
            _res = LightOn._from_sdf(_c_light_on, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_on")
            _light_on = _res
        else:
            _light_on = None
        if _light_on is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'light_on' is not supported in SDF version {version} (added in 1.8)")
        _c_visualize = el.find("visualize")
        if _c_visualize is not None:
            _res = LightVisualize._from_sdf(_c_visualize, version)
            if isinstance(_res, SDFError):
                return _res.extend("visualize")
            _visualize = _res
        else:
            _visualize = None
        if _visualize is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, name=_name, type=_type, frame=_frame, pose=_pose, cast_shadows=_cast_shadows, diffuse=_diffuse, specular=_specular, attenuation=_attenuation, direction=_direction, spot=_spot, intensity=_intensity, light_on=_light_on, visualize=_visualize)


class Link(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        inertial: "Inertial" = None,
        collision: List["Collision"] = None,
        visual: List["Visual"] = None,
        sensor: List["Sensor"] = None,
        projector: List["Projector"] = None,
        gravity: "Gravity" = None,
        self_collide: "SelfCollide" = None,
        kinematic: "Kinematic" = None,
        pose: "LinkPose" = None,
        velocity_decay: "VelocityDecay" = None,
        audio_source: List["AudioSource"] = None,
        must_be_base_link: "MustBeBaseLink" = None,
        audio_sink: List["AudioSink"] = None,
        battery: List["Battery"] = None,
        frame: List["Frame"] = None,
        enable_wind: "EnableWind" = None,
        particle_emitter: List["ParticleEmitter"] = None,
        light: List["Light"] = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.inertial = inertial
        self.collision = collision or []
        self.visual = visual or []
        self.sensor = sensor or []
        self.projector = projector or []
        self.gravity = gravity
        self.self_collide = self_collide
        self.kinematic = kinematic
        self.pose = pose
        self.velocity_decay = velocity_decay
        self.audio_source = audio_source or []
        self.must_be_base_link = must_be_base_link
        self.audio_sink = audio_sink or []
        self.battery = battery or []
        self.frame = frame or []
        self.enable_wind = enable_wind
        self.particle_emitter = particle_emitter or []
        self.light = light or []

    def to_version(self, target_version: str) -> "Link":
        if self.audio_source is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio_source' is not supported in SDF version {target_version} (added in 1.4)")
        if self.must_be_base_link is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'must_be_base_link' is not supported in SDF version {target_version} (added in 1.4)")
        if self.audio_sink is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio_sink' is not supported in SDF version {target_version} (added in 1.4)")
        if self.battery is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'battery' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.enable_wind is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.6)")
        if self.particle_emitter is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'particle_emitter' is not supported in SDF version {target_version} (added in 1.6)")
        if self.light is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'light' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["inertial"] = self.inertial.to_version(target_version) if self.inertial is not None else None
        kwargs["collision"] = [c.to_version(target_version) for c in (self.collision or [])]
        kwargs["visual"] = [c.to_version(target_version) for c in (self.visual or [])]
        kwargs["sensor"] = [c.to_version(target_version) for c in (self.sensor or [])]
        kwargs["projector"] = [c.to_version(target_version) for c in (self.projector or [])]
        kwargs["gravity"] = self.gravity.to_version(target_version) if self.gravity is not None else None
        kwargs["self_collide"] = self.self_collide.to_version(target_version) if self.self_collide is not None else None
        kwargs["kinematic"] = self.kinematic.to_version(target_version) if self.kinematic is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["velocity_decay"] = self.velocity_decay.to_version(target_version) if self.velocity_decay is not None else None
        kwargs["audio_source"] = [c.to_version(target_version) for c in (self.audio_source or [])]
        kwargs["must_be_base_link"] = self.must_be_base_link.to_version(target_version) if self.must_be_base_link is not None else None
        kwargs["audio_sink"] = [c.to_version(target_version) for c in (self.audio_sink or [])]
        kwargs["battery"] = [c.to_version(target_version) for c in (self.battery or [])]
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["enable_wind"] = self.enable_wind.to_version(target_version) if self.enable_wind is not None else None
        kwargs["particle_emitter"] = [c.to_version(target_version) for c in (self.particle_emitter or [])]
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("link")
        if self.name is not None:
            el.set("name", self.name)
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
        if self.gravity is not None:
            el.append(self.gravity.to_sdf(version))
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf(version))
        if self.kinematic is not None:
            el.append(self.kinematic.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.velocity_decay is not None:
            el.append(self.velocity_decay.to_sdf(version))
        for item in (self.audio_source or []):
            el.append(item.to_sdf(version))
        if self.must_be_base_link is not None:
            el.append(self.must_be_base_link.to_sdf(version))
        for item in (self.audio_sink or []):
            el.append(item.to_sdf(version))
        for item in (self.battery or []):
            el.append(item.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.enable_wind is not None:
            el.append(self.enable_wind.to_sdf(version))
        for item in (self.particle_emitter or []):
            el.append(item.to_sdf(version))
        for item in (self.light or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_inertial = el.find("inertial")
        if _c_inertial is not None:
            _res = Inertial._from_sdf(_c_inertial, version)
            if isinstance(_res, SDFError):
                return _res.extend("inertial")
            _inertial = _res
        else:
            _inertial = None
        _collision = []
        for c in el.findall("collision"):
            _res = Collision._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collision.append(_res)
        _visual = []
        for c in el.findall("visual"):
            _res = Visual._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("visual")
            _visual.append(_res)
        _sensor = []
        for c in el.findall("sensor"):
            _res = Sensor._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("sensor")
            _sensor.append(_res)
        _projector = []
        for c in el.findall("projector"):
            _res = Projector._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("projector")
            _projector.append(_res)
        _c_gravity = el.find("gravity")
        if _c_gravity is not None:
            _res = Gravity._from_sdf(_c_gravity, version)
            if isinstance(_res, SDFError):
                return _res.extend("gravity")
            _gravity = _res
        else:
            _gravity = None
        _c_self_collide = el.find("self_collide")
        if _c_self_collide is not None:
            _res = SelfCollide._from_sdf(_c_self_collide, version)
            if isinstance(_res, SDFError):
                return _res.extend("self_collide")
            _self_collide = _res
        else:
            _self_collide = None
        _c_kinematic = el.find("kinematic")
        if _c_kinematic is not None:
            _res = Kinematic._from_sdf(_c_kinematic, version)
            if isinstance(_res, SDFError):
                return _res.extend("kinematic")
            _kinematic = _res
        else:
            _kinematic = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = LinkPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_velocity_decay = el.find("velocity_decay")
        if _c_velocity_decay is not None:
            _res = VelocityDecay._from_sdf(_c_velocity_decay, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity_decay")
            _velocity_decay = _res
        else:
            _velocity_decay = None
        _audio_source = []
        for c in el.findall("audio_source"):
            _res = AudioSource._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("audio_source")
            _audio_source.append(_res)
        if _audio_source and cmp_version(version, "1.4") < 0:
            return SDFError(f"'audio_source' is not supported in SDF version {version} (added in 1.4)")
        _c_must_be_base_link = el.find("must_be_base_link")
        if _c_must_be_base_link is not None:
            _res = MustBeBaseLink._from_sdf(_c_must_be_base_link, version)
            if isinstance(_res, SDFError):
                return _res.extend("must_be_base_link")
            _must_be_base_link = _res
        else:
            _must_be_base_link = None
        if _must_be_base_link is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'must_be_base_link' is not supported in SDF version {version} (added in 1.4)")
        _audio_sink = []
        for c in el.findall("audio_sink"):
            _res = AudioSink._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("audio_sink")
            _audio_sink.append(_res)
        if _audio_sink and cmp_version(version, "1.4") < 0:
            return SDFError(f"'audio_sink' is not supported in SDF version {version} (added in 1.4)")
        _battery = []
        for c in el.findall("battery"):
            _res = Battery._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("battery")
            _battery.append(_res)
        if _battery and cmp_version(version, "1.5") < 0:
            return SDFError(f"'battery' is not supported in SDF version {version} (added in 1.5)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_enable_wind = el.find("enable_wind")
        if _c_enable_wind is not None:
            _res = EnableWind._from_sdf(_c_enable_wind, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_wind")
            _enable_wind = _res
        else:
            _enable_wind = None
        if _enable_wind is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.6)")
        _particle_emitter = []
        for c in el.findall("particle_emitter"):
            _res = ParticleEmitter._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("particle_emitter")
            _particle_emitter.append(_res)
        if _particle_emitter and cmp_version(version, "1.6") < 0:
            return SDFError(f"'particle_emitter' is not supported in SDF version {version} (added in 1.6)")
        _light = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _light.append(_res)
        if _light and cmp_version(version, "1.6") < 0:
            return SDFError(f"'light' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, name=_name, inertial=_inertial, collision=_collision, visual=_visual, sensor=_sensor, projector=_projector, gravity=_gravity, self_collide=_self_collide, kinematic=_kinematic, pose=_pose, velocity_decay=_velocity_decay, audio_source=_audio_source, must_be_base_link=_must_be_base_link, audio_sink=_audio_sink, battery=_battery, frame=_frame, enable_wind=_enable_wind, particle_emitter=_particle_emitter, light=_light)


class Parent(BaseModel):
    def __init__(self, sdf_version: str, parent: str = "__default__"):
        self.__version__ = sdf_version
        self.parent = parent

    def to_version(self, target_version: str) -> "Parent":
        kwargs = {"sdf_version": target_version}
        kwargs["parent"] = self.parent
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("parent")
        if self.parent is not None:
            el.text = self.parent
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _parent = _text
        if isinstance(_parent, SDFError):
            return _parent
        return cls(sdf_version=version, parent=_parent)


class Child(BaseModel):
    def __init__(self, sdf_version: str, child: str = "__default__"):
        self.__version__ = sdf_version
        self.child = child

    def to_version(self, target_version: str) -> "Child":
        kwargs = {"sdf_version": target_version}
        kwargs["child"] = self.child
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("child")
        if self.child is not None:
            el.text = self.child
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _child = _text
        if isinstance(_child, SDFError):
            return _child
        return cls(sdf_version=version, child=_child)


class JointPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: _SDFPose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "JointPose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
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
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


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


class Xyz(BaseModel):
    def __init__(self, sdf_version: str, xyz: _SDFVector3 = None, expressed_in: str = ""):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = _SDFVector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.expressed_in = expressed_in

    def to_version(self, target_version: str) -> "Xyz":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 1"
        _xyz = _SDFVector3._from_sdf(_text, version)
        if isinstance(_xyz, SDFError):
            return _xyz
        _expressed_in = el.get("expressed_in", "")
        if isinstance(_expressed_in, SDFError):
            return _expressed_in.extend("@expressed_in")
        if _expressed_in is not None and cmp_version(version, "1.7") < 0:
            if _expressed_in != "":
                return SDFError(f"'expressed_in' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, xyz=_xyz, expressed_in=_expressed_in)


class DynamicsDamping(BaseModel):
    def __init__(self, sdf_version: str, damping: float = 0):
        self.__version__ = sdf_version
        self.damping = damping

    def to_version(self, target_version: str) -> "DynamicsDamping":
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
        return cls(sdf_version=version, damping=_damping)


class DynamicsFriction(BaseModel):
    def __init__(self, sdf_version: str, friction: float = 0):
        self.__version__ = sdf_version
        self.friction = friction

    def to_version(self, target_version: str) -> "DynamicsFriction":
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
        return cls(sdf_version=version, friction=_friction)


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


class Dynamics(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        damping: "DynamicsDamping" = None,
        friction: "DynamicsFriction" = None,
        spring_stiffness: "SpringStiffness" = None,
        spring_reference: "SpringReference" = None
    ):
        self.__version__ = sdf_version
        self.damping = damping
        self.friction = friction
        self.spring_stiffness = spring_stiffness
        self.spring_reference = spring_reference

    def to_version(self, target_version: str) -> "Dynamics":
        if self.spring_stiffness is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {target_version} (added in 1.5)")
        if self.spring_reference is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["damping"] = self.damping.to_version(target_version) if self.damping is not None else None
        kwargs["friction"] = self.friction.to_version(target_version) if self.friction is not None else None
        kwargs["spring_stiffness"] = self.spring_stiffness.to_version(target_version) if self.spring_stiffness is not None else None
        kwargs["spring_reference"] = self.spring_reference.to_version(target_version) if self.spring_reference is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamics")
        if self.damping is not None:
            el.append(self.damping.to_sdf(version))
        if self.friction is not None:
            el.append(self.friction.to_sdf(version))
        if self.spring_stiffness is not None:
            el.append(self.spring_stiffness.to_sdf(version))
        if self.spring_reference is not None:
            el.append(self.spring_reference.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_damping = el.find("damping")
        if _c_damping is not None:
            _res = DynamicsDamping._from_sdf(_c_damping, version)
            if isinstance(_res, SDFError):
                return _res.extend("damping")
            _damping = _res
        else:
            _damping = None
        _c_friction = el.find("friction")
        if _c_friction is not None:
            _res = DynamicsFriction._from_sdf(_c_friction, version)
            if isinstance(_res, SDFError):
                return _res.extend("friction")
            _friction = _res
        else:
            _friction = None
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
        return cls(sdf_version=version, damping=_damping, friction=_friction, spring_stiffness=_spring_stiffness, spring_reference=_spring_reference)


class Lower(BaseModel):
    def __init__(self, sdf_version: str, lower: float = -1e16):
        self.__version__ = sdf_version
        self.lower = lower

    def to_version(self, target_version: str) -> "Lower":
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
        return cls(sdf_version=version, lower=_lower)


class Upper(BaseModel):
    def __init__(self, sdf_version: str, upper: float = 1e16):
        self.__version__ = sdf_version
        self.upper = upper

    def to_version(self, target_version: str) -> "Upper":
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
        return cls(sdf_version=version, upper=_upper)


class Effort(BaseModel):
    def __init__(self, sdf_version: str, effort: float = 0):
        self.__version__ = sdf_version
        self.effort = effort

    def to_version(self, target_version: str) -> "Effort":
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
        return cls(sdf_version=version, effort=_effort)


class Velocity(BaseModel):
    def __init__(self, sdf_version: str, velocity: float = 0):
        self.__version__ = sdf_version
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Velocity":
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
        return cls(sdf_version=version, velocity=_velocity)


class LimitStiffness(BaseModel):
    def __init__(self, sdf_version: str, stiffness: float = 1e8):
        self.__version__ = sdf_version
        self.stiffness = stiffness

    def to_version(self, target_version: str) -> "LimitStiffness":
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


class Limit(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        lower: "Lower" = None,
        upper: "Upper" = None,
        effort: "Effort" = None,
        velocity: "Velocity" = None,
        stiffness: "LimitStiffness" = None,
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
        kwargs["lower"] = self.lower.to_version(target_version) if self.lower is not None else None
        kwargs["upper"] = self.upper.to_version(target_version) if self.upper is not None else None
        kwargs["effort"] = self.effort.to_version(target_version) if self.effort is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
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
            el.append(self.lower.to_sdf(version))
        if self.upper is not None:
            el.append(self.upper.to_sdf(version))
        if self.effort is not None:
            el.append(self.effort.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_lower = el.find("lower")
        if _c_lower is not None:
            _res = Lower._from_sdf(_c_lower, version)
            if isinstance(_res, SDFError):
                return _res.extend("lower")
            _lower = _res
        else:
            _lower = None
        _c_upper = el.find("upper")
        if _c_upper is not None:
            _res = Upper._from_sdf(_c_upper, version)
            if isinstance(_res, SDFError):
                return _res.extend("upper")
            _upper = _res
        else:
            _upper = None
        _c_effort = el.find("effort")
        if _c_effort is not None:
            _res = Effort._from_sdf(_c_effort, version)
            if isinstance(_res, SDFError):
                return _res.extend("effort")
            _effort = _res
        else:
            _effort = None
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        _c_stiffness = el.find("stiffness")
        if _c_stiffness is not None:
            _res = LimitStiffness._from_sdf(_c_stiffness, version)
            if isinstance(_res, SDFError):
                return _res.extend("stiffness")
            _stiffness = _res
        else:
            _stiffness = None
        if _stiffness is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
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
        return cls(sdf_version=version, lower=_lower, upper=_upper, effort=_effort, velocity=_velocity, stiffness=_stiffness, dissipation=_dissipation)


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


class Axis(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        xyz: "Xyz" = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None,
        use_parent_model_frame: "UseParentModelFrame" = None,
        initial_position: "InitialPosition" = None
    ):
        self.__version__ = sdf_version
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit
        self.use_parent_model_frame = use_parent_model_frame
        self.initial_position = initial_position

    def to_version(self, target_version: str) -> "Axis":
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.initial_position is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.6)")
        if self.initial_position is not None and cmp_version(target_version, "1.9") >= 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (removed in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz.to_version(target_version) if self.xyz is not None else None
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["use_parent_model_frame"] = self.use_parent_model_frame.to_version(target_version) if self.use_parent_model_frame is not None else None
        kwargs["initial_position"] = self.initial_position.to_version(target_version) if self.initial_position is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis")
        if self.xyz is not None:
            el.append(self.xyz.to_sdf(version))
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf(version))
        if self.limit is None:
            self.limit = Limit(sdf_version=version)
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf(version))
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_xyz = el.find("xyz")
        if _c_xyz is not None:
            _res = Xyz._from_sdf(_c_xyz, version)
            if isinstance(_res, SDFError):
                return _res.extend("xyz")
            _xyz = _res
        else:
            _xyz = None
        _c_dynamics = el.find("dynamics")
        if _c_dynamics is not None:
            _res = Dynamics._from_sdf(_c_dynamics, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamics")
            _dynamics = _res
        else:
            _dynamics = None
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
        return cls(sdf_version=version, xyz=_xyz, dynamics=_dynamics, limit=_limit, use_parent_model_frame=_use_parent_model_frame, initial_position=_initial_position)


class Axis2(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        xyz: "Xyz" = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None,
        use_parent_model_frame: "UseParentModelFrame" = None,
        initial_position: "InitialPosition" = None
    ):
        self.__version__ = sdf_version
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit
        self.use_parent_model_frame = use_parent_model_frame
        self.initial_position = initial_position

    def to_version(self, target_version: str) -> "Axis2":
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.initial_position is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.6)")
        if self.initial_position is not None and cmp_version(target_version, "1.9") >= 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (removed in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz.to_version(target_version) if self.xyz is not None else None
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["use_parent_model_frame"] = self.use_parent_model_frame.to_version(target_version) if self.use_parent_model_frame is not None else None
        kwargs["initial_position"] = self.initial_position.to_version(target_version) if self.initial_position is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis2")
        if self.xyz is not None:
            el.append(self.xyz.to_sdf(version))
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf(version))
        if cmp_version(version, "1.6") >= 0:
            if self.limit is None:
                self.limit = Limit(sdf_version=version)
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf(version))
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_xyz = el.find("xyz")
        if _c_xyz is not None:
            _res = Xyz._from_sdf(_c_xyz, version)
            if isinstance(_res, SDFError):
                return _res.extend("xyz")
            _xyz = _res
        else:
            _xyz = None
        _c_dynamics = el.find("dynamics")
        if _c_dynamics is not None:
            _res = Dynamics._from_sdf(_c_dynamics, version)
            if isinstance(_res, SDFError):
                return _res.extend("dynamics")
            _dynamics = _res
        else:
            _dynamics = None
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
        return cls(sdf_version=version, xyz=_xyz, dynamics=_dynamics, limit=_limit, use_parent_model_frame=_use_parent_model_frame, initial_position=_initial_position)


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


class OdeBounce(BaseModel):
    def __init__(self, sdf_version: str, bounce: float = 0):
        self.__version__ = sdf_version
        self.bounce = bounce

    def to_version(self, target_version: str) -> "OdeBounce":
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


class LimitCfm(BaseModel):
    def __init__(self, sdf_version: str, cfm: float = 0.0):
        self.__version__ = sdf_version
        self.cfm = cfm

    def to_version(self, target_version: str) -> "LimitCfm":
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
        return cls(sdf_version=version, cfm=_cfm)


class Erp(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.2
        _erp = _parse_double(_text)
        if isinstance(_erp, SDFError):
            return _erp
        return cls(sdf_version=version, erp=_erp)


class OdeLimit(BaseModel):
    def __init__(self, sdf_version: str, cfm: "LimitCfm" = None, erp: "Erp" = None):
        self.__version__ = sdf_version
        self.cfm = cfm
        self.erp = erp

    def to_version(self, target_version: str) -> "OdeLimit":
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm.to_version(target_version) if self.cfm is not None else None
        kwargs["erp"] = self.erp.to_version(target_version) if self.erp is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("limit")
        if self.cfm is not None:
            el.append(self.cfm.to_sdf(version))
        if self.erp is not None:
            el.append(self.erp.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_cfm = el.find("cfm")
        if _c_cfm is not None:
            _res = LimitCfm._from_sdf(_c_cfm, version)
            if isinstance(_res, SDFError):
                return _res.extend("cfm")
            _cfm = _res
        else:
            _cfm = None
        _c_erp = el.find("erp")
        if _c_erp is not None:
            _res = Erp._from_sdf(_c_erp, version)
            if isinstance(_res, SDFError):
                return _res.extend("erp")
            _erp = _res
        else:
            _erp = None
        return cls(sdf_version=version, cfm=_cfm, erp=_erp)


class SuspensionCfm(BaseModel):
    def __init__(self, sdf_version: str, cfm: float = 0.0):
        self.__version__ = sdf_version
        self.cfm = cfm

    def to_version(self, target_version: str) -> "SuspensionCfm":
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
        return cls(sdf_version=version, cfm=_cfm)


class Suspension(BaseModel):
    def __init__(self, sdf_version: str, cfm: "SuspensionCfm" = None, erp: "Erp" = None):
        self.__version__ = sdf_version
        self.cfm = cfm
        self.erp = erp

    def to_version(self, target_version: str) -> "Suspension":
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm.to_version(target_version) if self.cfm is not None else None
        kwargs["erp"] = self.erp.to_version(target_version) if self.erp is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("suspension")
        if self.cfm is not None:
            el.append(self.cfm.to_sdf(version))
        if self.erp is not None:
            el.append(self.erp.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_cfm = el.find("cfm")
        if _c_cfm is not None:
            _res = SuspensionCfm._from_sdf(_c_cfm, version)
            if isinstance(_res, SDFError):
                return _res.extend("cfm")
            _cfm = _res
        else:
            _cfm = None
        _c_erp = el.find("erp")
        if _c_erp is not None:
            _res = Erp._from_sdf(_c_erp, version)
            if isinstance(_res, SDFError):
                return _res.extend("erp")
            _erp = _res
        else:
            _erp = None
        return cls(sdf_version=version, cfm=_cfm, erp=_erp)


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


class PhysicsOde(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        fudge_factor: "FudgeFactor" = None,
        cfm: "Cfm" = None,
        bounce: "OdeBounce" = None,
        max_force: "MaxForce" = None,
        velocity: "Velocity" = None,
        limit: "OdeLimit" = None,
        suspension: "Suspension" = None,
        provide_feedback: "ProvideFeedback" = None,
        cfm_damping: "CfmDamping" = None,
        implicit_spring_damper: "ImplicitSpringDamper" = None,
        erp: "Erp" = None
    ):
        self.__version__ = sdf_version
        self.fudge_factor = fudge_factor
        self.cfm = cfm
        self.bounce = bounce
        self.max_force = max_force
        self.velocity = velocity
        self.limit = limit
        self.suspension = suspension
        self.provide_feedback = provide_feedback
        self.cfm_damping = cfm_damping
        self.implicit_spring_damper = implicit_spring_damper
        self.erp = erp

    def to_version(self, target_version: str) -> "PhysicsOde":
        if self.provide_feedback is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.3)")
        if self.provide_feedback is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.cfm_damping is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'cfm_damping' is not supported in SDF version {target_version} (added in 1.3)")
        if self.implicit_spring_damper is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'implicit_spring_damper' is not supported in SDF version {target_version} (added in 1.4)")
        if self.erp is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'erp' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["fudge_factor"] = self.fudge_factor.to_version(target_version) if self.fudge_factor is not None else None
        kwargs["cfm"] = self.cfm.to_version(target_version) if self.cfm is not None else None
        kwargs["bounce"] = self.bounce.to_version(target_version) if self.bounce is not None else None
        kwargs["max_force"] = self.max_force.to_version(target_version) if self.max_force is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["suspension"] = self.suspension.to_version(target_version) if self.suspension is not None else None
        kwargs["provide_feedback"] = self.provide_feedback.to_version(target_version) if self.provide_feedback is not None else None
        kwargs["cfm_damping"] = self.cfm_damping.to_version(target_version) if self.cfm_damping is not None else None
        kwargs["implicit_spring_damper"] = self.implicit_spring_damper.to_version(target_version) if self.implicit_spring_damper is not None else None
        kwargs["erp"] = self.erp.to_version(target_version) if self.erp is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.fudge_factor is not None:
            el.append(self.fudge_factor.to_sdf(version))
        if self.cfm is not None:
            el.append(self.cfm.to_sdf(version))
        if self.bounce is not None:
            el.append(self.bounce.to_sdf(version))
        if self.max_force is not None:
            el.append(self.max_force.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.suspension is not None:
            el.append(self.suspension.to_sdf(version))
        if self.provide_feedback is not None:
            el.append(self.provide_feedback.to_sdf(version))
        if self.cfm_damping is not None:
            el.append(self.cfm_damping.to_sdf(version))
        if self.implicit_spring_damper is not None:
            el.append(self.implicit_spring_damper.to_sdf(version))
        if self.erp is not None:
            el.append(self.erp.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_fudge_factor = el.find("fudge_factor")
        if _c_fudge_factor is not None:
            _res = FudgeFactor._from_sdf(_c_fudge_factor, version)
            if isinstance(_res, SDFError):
                return _res.extend("fudge_factor")
            _fudge_factor = _res
        else:
            _fudge_factor = None
        _c_cfm = el.find("cfm")
        if _c_cfm is not None:
            _res = Cfm._from_sdf(_c_cfm, version)
            if isinstance(_res, SDFError):
                return _res.extend("cfm")
            _cfm = _res
        else:
            _cfm = None
        _c_bounce = el.find("bounce")
        if _c_bounce is not None:
            _res = OdeBounce._from_sdf(_c_bounce, version)
            if isinstance(_res, SDFError):
                return _res.extend("bounce")
            _bounce = _res
        else:
            _bounce = None
        _c_max_force = el.find("max_force")
        if _c_max_force is not None:
            _res = MaxForce._from_sdf(_c_max_force, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_force")
            _max_force = _res
        else:
            _max_force = None
        _c_velocity = el.find("velocity")
        if _c_velocity is not None:
            _res = Velocity._from_sdf(_c_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity")
            _velocity = _res
        else:
            _velocity = None
        _c_limit = el.find("limit")
        if _c_limit is not None:
            _res = OdeLimit._from_sdf(_c_limit, version)
            if isinstance(_res, SDFError):
                return _res.extend("limit")
            _limit = _res
        else:
            _limit = None
        _c_suspension = el.find("suspension")
        if _c_suspension is not None:
            _res = Suspension._from_sdf(_c_suspension, version)
            if isinstance(_res, SDFError):
                return _res.extend("suspension")
            _suspension = _res
        else:
            _suspension = None
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
        return cls(sdf_version=version, fudge_factor=_fudge_factor, cfm=_cfm, bounce=_bounce, max_force=_max_force, velocity=_velocity, limit=_limit, suspension=_suspension, provide_feedback=_provide_feedback, cfm_damping=_cfm_damping, implicit_spring_damper=_implicit_spring_damper, erp=_erp)


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


class Physics(BaseModel):
    _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

    def __init__(
        self,
        sdf_version: str,
        ode: "PhysicsOde" = None,
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = PhysicsOde._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
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
        return cls(sdf_version=version, ode=_ode, simbody=_simbody, provide_feedback=_provide_feedback)


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


class SensorTopic2(BaseModel):
    def __init__(self, sdf_version: str, topic: str = "__default__"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "SensorTopic2":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


class JointSensor(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "__default__",
        plugin: List["Plugin"] = None,
        camera: "Camera" = None,
        contact: "SensorContact" = None,
        force_torque: "ForceTorque" = None,
        gps: "Gps" = None,
        imu: "Imu" = None,
        ray: "Ray" = None,
        rfidtag: "Rfidtag" = None,
        rfid: "Rfid" = None,
        sonar: "Sonar" = None,
        transceiver: "Transceiver" = None,
        always_on: "AlwaysOn" = None,
        update_rate: "UpdateRate" = None,
        visualize: "Visualize" = None,
        pose: "SensorPose" = None,
        topic: "SensorTopic2" = None,
        frame: List["Frame"] = None,
        altimeter: "Altimeter" = None,
        magnetometer: "Magnetometer" = None,
        logical_camera: "LogicalCamera" = None,
        air_pressure: "AirPressure" = None,
        lidar: "Lidar" = None,
        navsat: "Navsat" = None,
        enable_metrics: "EnableMetrics" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.plugin = plugin or []
        self.camera = camera
        self.contact = contact
        self.force_torque = force_torque
        self.gps = gps
        self.imu = imu
        self.ray = ray
        self.rfidtag = rfidtag
        self.rfid = rfid
        self.sonar = sonar
        self.transceiver = transceiver
        self.always_on = always_on
        self.update_rate = update_rate
        self.visualize = visualize
        self.pose = pose
        self.topic = topic
        self.frame = frame or []
        self.altimeter = altimeter
        self.magnetometer = magnetometer
        self.logical_camera = logical_camera
        self.air_pressure = air_pressure
        self.lidar = lidar
        self.navsat = navsat
        self.enable_metrics = enable_metrics

    def to_version(self, target_version: str) -> "JointSensor":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.altimeter is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'altimeter' is not supported in SDF version {target_version} (added in 1.5)")
        if self.magnetometer is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'magnetometer' is not supported in SDF version {target_version} (added in 1.5)")
        if self.logical_camera is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'logical_camera' is not supported in SDF version {target_version} (added in 1.5)")
        if self.air_pressure is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'air_pressure' is not supported in SDF version {target_version} (added in 1.6)")
        if self.lidar is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'lidar' is not supported in SDF version {target_version} (added in 1.6)")
        if self.navsat is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'navsat' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["force_torque"] = self.force_torque.to_version(target_version) if self.force_torque is not None else None
        kwargs["gps"] = self.gps.to_version(target_version) if self.gps is not None else None
        kwargs["imu"] = self.imu.to_version(target_version) if self.imu is not None else None
        kwargs["ray"] = self.ray.to_version(target_version) if self.ray is not None else None
        kwargs["rfidtag"] = self.rfidtag.to_version(target_version) if self.rfidtag is not None else None
        kwargs["rfid"] = self.rfid.to_version(target_version) if self.rfid is not None else None
        kwargs["sonar"] = self.sonar.to_version(target_version) if self.sonar is not None else None
        kwargs["transceiver"] = self.transceiver.to_version(target_version) if self.transceiver is not None else None
        kwargs["always_on"] = self.always_on.to_version(target_version) if self.always_on is not None else None
        kwargs["update_rate"] = self.update_rate.to_version(target_version) if self.update_rate is not None else None
        kwargs["visualize"] = self.visualize.to_version(target_version) if self.visualize is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["altimeter"] = self.altimeter.to_version(target_version) if self.altimeter is not None else None
        kwargs["magnetometer"] = self.magnetometer.to_version(target_version) if self.magnetometer is not None else None
        kwargs["logical_camera"] = self.logical_camera.to_version(target_version) if self.logical_camera is not None else None
        kwargs["air_pressure"] = self.air_pressure.to_version(target_version) if self.air_pressure is not None else None
        kwargs["lidar"] = self.lidar.to_version(target_version) if self.lidar is not None else None
        kwargs["navsat"] = self.navsat.to_version(target_version) if self.navsat is not None else None
        kwargs["enable_metrics"] = self.enable_metrics.to_version(target_version) if self.enable_metrics is not None else None
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
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.camera is not None:
            el.append(self.camera.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        if self.force_torque is not None:
            el.append(self.force_torque.to_sdf(version))
        if self.gps is not None:
            el.append(self.gps.to_sdf(version))
        if self.imu is not None:
            el.append(self.imu.to_sdf(version))
        if self.ray is not None:
            el.append(self.ray.to_sdf(version))
        if self.rfidtag is not None:
            el.append(self.rfidtag.to_sdf(version))
        if self.rfid is not None:
            el.append(self.rfid.to_sdf(version))
        if self.sonar is not None:
            el.append(self.sonar.to_sdf(version))
        if self.transceiver is not None:
            el.append(self.transceiver.to_sdf(version))
        if self.always_on is not None:
            el.append(self.always_on.to_sdf(version))
        if self.update_rate is not None:
            el.append(self.update_rate.to_sdf(version))
        if self.visualize is not None:
            el.append(self.visualize.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.altimeter is not None:
            el.append(self.altimeter.to_sdf(version))
        if self.magnetometer is not None:
            el.append(self.magnetometer.to_sdf(version))
        if self.logical_camera is not None:
            el.append(self.logical_camera.to_sdf(version))
        if self.air_pressure is not None:
            el.append(self.air_pressure.to_sdf(version))
        if self.lidar is not None:
            el.append(self.lidar.to_sdf(version))
        if self.navsat is not None:
            el.append(self.navsat.to_sdf(version))
        if self.enable_metrics is not None:
            el.append(self.enable_metrics.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _type = el.get("type", "__default__")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _c_camera = el.find("camera")
        if _c_camera is not None:
            _res = Camera._from_sdf(_c_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera")
            _camera = _res
        else:
            _camera = None
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = SensorContact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _c_force_torque = el.find("force_torque")
        if _c_force_torque is not None:
            _res = ForceTorque._from_sdf(_c_force_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("force_torque")
            _force_torque = _res
        else:
            _force_torque = None
        _c_gps = el.find("gps")
        if _c_gps is not None:
            _res = Gps._from_sdf(_c_gps, version)
            if isinstance(_res, SDFError):
                return _res.extend("gps")
            _gps = _res
        else:
            _gps = None
        _c_imu = el.find("imu")
        if _c_imu is not None:
            _res = Imu._from_sdf(_c_imu, version)
            if isinstance(_res, SDFError):
                return _res.extend("imu")
            _imu = _res
        else:
            _imu = None
        _c_ray = el.find("ray")
        if _c_ray is not None:
            _res = Ray._from_sdf(_c_ray, version)
            if isinstance(_res, SDFError):
                return _res.extend("ray")
            _ray = _res
        else:
            _ray = None
        _c_rfidtag = el.find("rfidtag")
        if _c_rfidtag is not None:
            _res = Rfidtag._from_sdf(_c_rfidtag, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfidtag")
            _rfidtag = _res
        else:
            _rfidtag = None
        _c_rfid = el.find("rfid")
        if _c_rfid is not None:
            _res = Rfid._from_sdf(_c_rfid, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfid")
            _rfid = _res
        else:
            _rfid = None
        _c_sonar = el.find("sonar")
        if _c_sonar is not None:
            _res = Sonar._from_sdf(_c_sonar, version)
            if isinstance(_res, SDFError):
                return _res.extend("sonar")
            _sonar = _res
        else:
            _sonar = None
        _c_transceiver = el.find("transceiver")
        if _c_transceiver is not None:
            _res = Transceiver._from_sdf(_c_transceiver, version)
            if isinstance(_res, SDFError):
                return _res.extend("transceiver")
            _transceiver = _res
        else:
            _transceiver = None
        _c_always_on = el.find("always_on")
        if _c_always_on is not None:
            _res = AlwaysOn._from_sdf(_c_always_on, version)
            if isinstance(_res, SDFError):
                return _res.extend("always_on")
            _always_on = _res
        else:
            _always_on = None
        _c_update_rate = el.find("update_rate")
        if _c_update_rate is not None:
            _res = UpdateRate._from_sdf(_c_update_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("update_rate")
            _update_rate = _res
        else:
            _update_rate = None
        _c_visualize = el.find("visualize")
        if _c_visualize is not None:
            _res = Visualize._from_sdf(_c_visualize, version)
            if isinstance(_res, SDFError):
                return _res.extend("visualize")
            _visualize = _res
        else:
            _visualize = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = SensorPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = SensorTopic2._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_altimeter = el.find("altimeter")
        if _c_altimeter is not None:
            _res = Altimeter._from_sdf(_c_altimeter, version)
            if isinstance(_res, SDFError):
                return _res.extend("altimeter")
            _altimeter = _res
        else:
            _altimeter = None
        if _altimeter is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'altimeter' is not supported in SDF version {version} (added in 1.5)")
        _c_magnetometer = el.find("magnetometer")
        if _c_magnetometer is not None:
            _res = Magnetometer._from_sdf(_c_magnetometer, version)
            if isinstance(_res, SDFError):
                return _res.extend("magnetometer")
            _magnetometer = _res
        else:
            _magnetometer = None
        if _magnetometer is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'magnetometer' is not supported in SDF version {version} (added in 1.5)")
        _c_logical_camera = el.find("logical_camera")
        if _c_logical_camera is not None:
            _res = LogicalCamera._from_sdf(_c_logical_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("logical_camera")
            _logical_camera = _res
        else:
            _logical_camera = None
        if _logical_camera is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'logical_camera' is not supported in SDF version {version} (added in 1.5)")
        _c_air_pressure = el.find("air_pressure")
        if _c_air_pressure is not None:
            _res = AirPressure._from_sdf(_c_air_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("air_pressure")
            _air_pressure = _res
        else:
            _air_pressure = None
        if _air_pressure is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'air_pressure' is not supported in SDF version {version} (added in 1.6)")
        _c_lidar = el.find("lidar")
        if _c_lidar is not None:
            _res = Lidar._from_sdf(_c_lidar, version)
            if isinstance(_res, SDFError):
                return _res.extend("lidar")
            _lidar = _res
        else:
            _lidar = None
        if _lidar is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'lidar' is not supported in SDF version {version} (added in 1.6)")
        _c_navsat = el.find("navsat")
        if _c_navsat is not None:
            _res = Navsat._from_sdf(_c_navsat, version)
            if isinstance(_res, SDFError):
                return _res.extend("navsat")
            _navsat = _res
        else:
            _navsat = None
        if _navsat is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'navsat' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_metrics = el.find("enable_metrics")
        if _c_enable_metrics is not None:
            _res = EnableMetrics._from_sdf(_c_enable_metrics, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_metrics")
            _enable_metrics = _res
        else:
            _enable_metrics = None
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, name=_name, type=_type, plugin=_plugin, camera=_camera, contact=_contact, force_torque=_force_torque, gps=_gps, imu=_imu, ray=_ray, rfidtag=_rfidtag, rfid=_rfid, sonar=_sonar, transceiver=_transceiver, always_on=_always_on, update_rate=_update_rate, visualize=_visualize, pose=_pose, topic=_topic, frame=_frame, altimeter=_altimeter, magnetometer=_magnetometer, logical_camera=_logical_camera, air_pressure=_air_pressure, lidar=_lidar, navsat=_navsat, enable_metrics=_enable_metrics)


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


class Joint(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "__default__",
        parent: "Parent" = None,
        child: "Child" = None,
        pose: "JointPose" = None,
        thread_pitch: "ThreadPitch" = None,
        axis: "Axis" = None,
        axis2: "Axis2" = None,
        physics: "Physics" = None,
        gearbox_reference_body: "GearboxReferenceBody" = None,
        sensor: List["JointSensor"] = None,
        gearbox_ratio: "GearboxRatio" = None,
        frame: List["Frame"] = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.parent = parent
        self.child = child
        self.pose = pose
        self.thread_pitch = thread_pitch
        self.axis = axis
        self.axis2 = axis2
        self.physics = physics
        self.gearbox_reference_body = gearbox_reference_body
        self.sensor = sensor or []
        self.gearbox_ratio = gearbox_ratio
        self.frame = frame or []

    def to_version(self, target_version: str) -> "Joint":
        if self.gearbox_reference_body is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {target_version} (added in 1.4)")
        if self.sensor is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'sensor' is not supported in SDF version {target_version} (added in 1.4)")
        if self.gearbox_ratio is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_ratio' is not supported in SDF version {target_version} (added in 1.4)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["parent"] = self.parent.to_version(target_version) if self.parent is not None else None
        kwargs["child"] = self.child.to_version(target_version) if self.child is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["thread_pitch"] = self.thread_pitch.to_version(target_version) if self.thread_pitch is not None else None
        kwargs["axis"] = self.axis.to_version(target_version) if self.axis is not None else None
        kwargs["axis2"] = self.axis2.to_version(target_version) if self.axis2 is not None else None
        kwargs["physics"] = self.physics.to_version(target_version) if self.physics is not None else None
        kwargs["gearbox_reference_body"] = self.gearbox_reference_body.to_version(target_version) if self.gearbox_reference_body is not None else None
        kwargs["sensor"] = [c.to_version(target_version) for c in (self.sensor or [])]
        kwargs["gearbox_ratio"] = self.gearbox_ratio.to_version(target_version) if self.gearbox_ratio is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
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
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.thread_pitch is not None:
            el.append(self.thread_pitch.to_sdf(version))
        if self.axis is not None:
            el.append(self.axis.to_sdf(version))
        if self.axis2 is not None:
            el.append(self.axis2.to_sdf(version))
        if self.physics is not None:
            el.append(self.physics.to_sdf(version))
        if self.gearbox_reference_body is not None:
            el.append(self.gearbox_reference_body.to_sdf(version))
        for item in (self.sensor or []):
            el.append(item.to_sdf(version))
        if self.gearbox_ratio is not None:
            el.append(self.gearbox_ratio.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _type = el.get("type", "__default__")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_parent = el.find("parent")
        if _c_parent is not None:
            _res = Parent._from_sdf(_c_parent, version)
            if isinstance(_res, SDFError):
                return _res.extend("parent")
            _parent = _res
        else:
            _parent = None
        _c_child = el.find("child")
        if _c_child is not None:
            _res = Child._from_sdf(_c_child, version)
            if isinstance(_res, SDFError):
                return _res.extend("child")
            _child = _res
        else:
            _child = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = JointPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_thread_pitch = el.find("thread_pitch")
        if _c_thread_pitch is not None:
            _res = ThreadPitch._from_sdf(_c_thread_pitch, version)
            if isinstance(_res, SDFError):
                return _res.extend("thread_pitch")
            _thread_pitch = _res
        else:
            _thread_pitch = None
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
        _c_physics = el.find("physics")
        if _c_physics is not None:
            _res = Physics._from_sdf(_c_physics, version)
            if isinstance(_res, SDFError):
                return _res.extend("physics")
            _physics = _res
        else:
            _physics = None
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
        _sensor = []
        for c in el.findall("sensor"):
            _res = JointSensor._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("sensor")
            _sensor.append(_res)
        if _sensor and cmp_version(version, "1.4") < 0:
            return SDFError(f"'sensor' is not supported in SDF version {version} (added in 1.4)")
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
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, name=_name, type=_type, parent=_parent, child=_child, pose=_pose, thread_pitch=_thread_pitch, axis=_axis, axis2=_axis2, physics=_physics, gearbox_reference_body=_gearbox_reference_body, sensor=_sensor, gearbox_ratio=_gearbox_ratio, frame=_frame)


class DetachSteps(BaseModel):
    def __init__(self, sdf_version: str, detach_steps: int = 40):
        self.__version__ = sdf_version
        self.detach_steps = detach_steps

    def to_version(self, target_version: str) -> "DetachSteps":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 40
        _detach_steps = _parse_int32(_text)
        if isinstance(_detach_steps, SDFError):
            return _detach_steps
        return cls(sdf_version=version, detach_steps=_detach_steps)


class AttachSteps(BaseModel):
    def __init__(self, sdf_version: str, attach_steps: int = 20):
        self.__version__ = sdf_version
        self.attach_steps = attach_steps

    def to_version(self, target_version: str) -> "AttachSteps":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 20
        _attach_steps = _parse_int32(_text)
        if isinstance(_attach_steps, SDFError):
            return _attach_steps
        return cls(sdf_version=version, attach_steps=_attach_steps)


class MinContactCount(BaseModel):
    def __init__(self, sdf_version: str, min_contact_count: int = 2):
        self.__version__ = sdf_version
        self.min_contact_count = min_contact_count

    def to_version(self, target_version: str) -> "MinContactCount":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2
        _min_contact_count = _parse_uint32(_text)
        if isinstance(_min_contact_count, SDFError):
            return _min_contact_count
        return cls(sdf_version=version, min_contact_count=_min_contact_count)


class GraspCheck(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        detach_steps: "DetachSteps" = None,
        attach_steps: "AttachSteps" = None,
        min_contact_count: "MinContactCount" = None
    ):
        self.__version__ = sdf_version
        self.detach_steps = detach_steps
        self.attach_steps = attach_steps
        self.min_contact_count = min_contact_count

    def to_version(self, target_version: str) -> "GraspCheck":
        kwargs = {"sdf_version": target_version}
        kwargs["detach_steps"] = self.detach_steps.to_version(target_version) if self.detach_steps is not None else None
        kwargs["attach_steps"] = self.attach_steps.to_version(target_version) if self.attach_steps is not None else None
        kwargs["min_contact_count"] = self.min_contact_count.to_version(target_version) if self.min_contact_count is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grasp_check")
        if self.detach_steps is not None:
            el.append(self.detach_steps.to_sdf(version))
        if self.attach_steps is not None:
            el.append(self.attach_steps.to_sdf(version))
        if self.min_contact_count is not None:
            el.append(self.min_contact_count.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_detach_steps = el.find("detach_steps")
        if _c_detach_steps is not None:
            _res = DetachSteps._from_sdf(_c_detach_steps, version)
            if isinstance(_res, SDFError):
                return _res.extend("detach_steps")
            _detach_steps = _res
        else:
            _detach_steps = None
        _c_attach_steps = el.find("attach_steps")
        if _c_attach_steps is not None:
            _res = AttachSteps._from_sdf(_c_attach_steps, version)
            if isinstance(_res, SDFError):
                return _res.extend("attach_steps")
            _attach_steps = _res
        else:
            _attach_steps = None
        _c_min_contact_count = el.find("min_contact_count")
        if _c_min_contact_count is not None:
            _res = MinContactCount._from_sdf(_c_min_contact_count, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_contact_count")
            _min_contact_count = _res
        else:
            _min_contact_count = None
        return cls(sdf_version=version, detach_steps=_detach_steps, attach_steps=_attach_steps, min_contact_count=_min_contact_count)


class GripperLink(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _gripper_link = _text
        if isinstance(_gripper_link, SDFError):
            return _gripper_link
        return cls(sdf_version=version, gripper_link=_gripper_link)


class PalmLink(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _palm_link = _text
        if isinstance(_palm_link, SDFError):
            return _palm_link
        return cls(sdf_version=version, palm_link=_palm_link)


class Gripper(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_grasp_check = el.find("grasp_check")
        if _c_grasp_check is not None:
            _res = GraspCheck._from_sdf(_c_grasp_check, version)
            if isinstance(_res, SDFError):
                return _res.extend("grasp_check")
            _grasp_check = _res
        else:
            _grasp_check = None
        _gripper_link = []
        for c in el.findall("gripper_link"):
            _res = GripperLink._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("gripper_link")
            _gripper_link.append(_res)
        _c_palm_link = el.find("palm_link")
        if _c_palm_link is not None:
            _res = PalmLink._from_sdf(_c_palm_link, version)
            if isinstance(_res, SDFError):
                return _res.extend("palm_link")
            _palm_link = _res
        else:
            _palm_link = None
        return cls(sdf_version=version, name=_name, grasp_check=_grasp_check, gripper_link=_gripper_link, palm_link=_palm_link)


class RobotPose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(self, sdf_version: str, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "RobotPose":
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        return cls(sdf_version=version, pose=_pose)


class Robot(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        gripper: List["Gripper"] = None,
        pose: "RobotPose" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.gripper = gripper or []
        self.pose = pose

    def to_version(self, target_version: str) -> "Robot":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["link"] = [c.to_version(target_version) for c in (self.link or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["gripper"] = [c.to_version(target_version) for c in (self.gripper or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("robot")
        if self.name is not None:
            el.set("name", self.name)
        if not self.link:
            raise ValueError(f"'link' is required in SDF version {version}")
        for item in (self.link or []):
            el.append(item.to_sdf(version))
        for item in (self.joint or []):
            el.append(item.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        for item in (self.gripper or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _link = []
        for c in el.findall("link"):
            _res = Link._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link")
            _link.append(_res)
        if not _link:
            return SDFError(f"'link' is required in SDF version {version}")
        _joint = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joint.append(_res)
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _gripper = []
        for c in el.findall("gripper"):
            _res = Gripper._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("gripper")
            _gripper.append(_res)
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = RobotPose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, name=_name, link=_link, joint=_joint, plugin=_plugin, gripper=_gripper, pose=_pose)
