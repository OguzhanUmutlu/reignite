from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .include import Include
from .model import Model
from ....utils.color import Color
from ....utils.pose import Pose
from ....utils.vector3 import Vector3


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
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class Pose(Model):
    def __init__(self, pose: Pose = None, frame: str = ""):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.frame is not None:
            el.set("frame", self.frame)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        _frame = el.get("frame", "")
        return cls(pose=_pose, frame=_frame)


class Frame(Model):
    def __init__(self, name: str = "", pose: "Pose" = None):
        self.name = name
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("frame")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frame":
        _name = el.get("name", "")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_name, pose=_pose)


class Mass(Model):
    def __init__(self, mass: float = 1.0):
        self.mass = mass

    def to_sdf(self) -> ET.Element:
        el = ET.Element("mass")
        if self.mass is not None:
            el.text = str(self.mass)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mass":
        _text = el.text or 1.0
        _mass = _parse_double(_text)
        return cls(mass=_mass)


class Ixx(Model):
    def __init__(self, ixx: float = 1.0):
        self.ixx = ixx

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ixx")
        if self.ixx is not None:
            el.text = str(self.ixx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ixx":
        _text = el.text or 1.0
        _ixx = _parse_double(_text)
        return cls(ixx=_ixx)


class Ixy(Model):
    def __init__(self, ixy: float = 0.0):
        self.ixy = ixy

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ixy")
        if self.ixy is not None:
            el.text = str(self.ixy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ixy":
        _text = el.text or 0.0
        _ixy = _parse_double(_text)
        return cls(ixy=_ixy)


class Ixz(Model):
    def __init__(self, ixz: float = 0.0):
        self.ixz = ixz

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ixz")
        if self.ixz is not None:
            el.text = str(self.ixz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ixz":
        _text = el.text or 0.0
        _ixz = _parse_double(_text)
        return cls(ixz=_ixz)


class Iyy(Model):
    def __init__(self, iyy: float = 1.0):
        self.iyy = iyy

    def to_sdf(self) -> ET.Element:
        el = ET.Element("iyy")
        if self.iyy is not None:
            el.text = str(self.iyy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Iyy":
        _text = el.text or 1.0
        _iyy = _parse_double(_text)
        return cls(iyy=_iyy)


class Iyz(Model):
    def __init__(self, iyz: float = 0.0):
        self.iyz = iyz

    def to_sdf(self) -> ET.Element:
        el = ET.Element("iyz")
        if self.iyz is not None:
            el.text = str(self.iyz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Iyz":
        _text = el.text or 0.0
        _iyz = _parse_double(_text)
        return cls(iyz=_iyz)


class Izz(Model):
    def __init__(self, izz: float = 1.0):
        self.izz = izz

    def to_sdf(self) -> ET.Element:
        el = ET.Element("izz")
        if self.izz is not None:
            el.text = str(self.izz)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Izz":
        _text = el.text or 1.0
        _izz = _parse_double(_text)
        return cls(izz=_izz)


class Inertia(Model):
    def __init__(
            self,
            ixx: "Ixx" = None,
            ixy: "Ixy" = None,
            ixz: "Ixz" = None,
            iyy: "Iyy" = None,
            iyz: "Iyz" = None,
            izz: "Izz" = None
    ):
        self.ixx = ixx
        self.ixy = ixy
        self.ixz = ixz
        self.iyy = iyy
        self.iyz = iyz
        self.izz = izz

    def to_sdf(self) -> ET.Element:
        el = ET.Element("inertia")
        if self.ixx is not None:
            el.append(self.ixx.to_sdf())
        if self.ixy is not None:
            el.append(self.ixy.to_sdf())
        if self.ixz is not None:
            el.append(self.ixz.to_sdf())
        if self.iyy is not None:
            el.append(self.iyy.to_sdf())
        if self.iyz is not None:
            el.append(self.iyz.to_sdf())
        if self.izz is not None:
            el.append(self.izz.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertia":
        _c_ixx = el.find("ixx")
        _ixx = Ixx.from_sdf(_c_ixx) if _c_ixx is not None else None
        _c_ixy = el.find("ixy")
        _ixy = Ixy.from_sdf(_c_ixy) if _c_ixy is not None else None
        _c_ixz = el.find("ixz")
        _ixz = Ixz.from_sdf(_c_ixz) if _c_ixz is not None else None
        _c_iyy = el.find("iyy")
        _iyy = Iyy.from_sdf(_c_iyy) if _c_iyy is not None else None
        _c_iyz = el.find("iyz")
        _iyz = Iyz.from_sdf(_c_iyz) if _c_iyz is not None else None
        _c_izz = el.find("izz")
        _izz = Izz.from_sdf(_c_izz) if _c_izz is not None else None
        return cls(ixx=_ixx, ixy=_ixy, ixz=_ixz, iyy=_iyy, iyz=_iyz, izz=_izz)


class Inertial(Model):
    def __init__(
            self,
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            mass: "Mass" = None,
            inertia: "Inertia" = None
    ):
        self.frame = frame or []
        self.pose = pose
        self.mass = mass
        self.inertia = inertia

    def to_sdf(self) -> ET.Element:
        el = ET.Element("inertial")
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.mass is not None:
            el.append(self.mass.to_sdf())
        if self.inertia is not None:
            el.append(self.inertia.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_mass = el.find("mass")
        _mass = Mass.from_sdf(_c_mass) if _c_mass is not None else None
        _c_inertia = el.find("inertia")
        _inertia = Inertia.from_sdf(_c_inertia) if _c_inertia is not None else None
        return cls(frame=_frame, pose=_pose, mass=_mass, inertia=_inertia)


class Size(Model):
    def __init__(self, size: Vector3 = None):
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        self.size = size

    def to_sdf(self) -> ET.Element:
        el = ET.Element("size")
        if self.size is not None:
            el.text = self.size.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Size":
        _text = el.text or "1 1 1"
        _size = Vector3.from_sdf(_text)
        return cls(size=_size)


class Box(Model):
    def __init__(self, size: "Size" = None):
        self.size = size

    def to_sdf(self) -> ET.Element:
        el = ET.Element("box")
        if self.size is not None:
            el.append(self.size.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Box":
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size) if _c_size is not None else None
        return cls(size=_size)


class Radius(Model):
    def __init__(self, radius: float = 1):
        self.radius = radius

    def to_sdf(self) -> ET.Element:
        el = ET.Element("radius")
        if self.radius is not None:
            el.text = str(self.radius)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Radius":
        _text = el.text or 1
        _radius = _parse_double(_text)
        return cls(radius=_radius)


class Length(Model):
    def __init__(self, length: float = 1):
        self.length = length

    def to_sdf(self) -> ET.Element:
        el = ET.Element("length")
        if self.length is not None:
            el.text = str(self.length)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Length":
        _text = el.text or 1
        _length = _parse_double(_text)
        return cls(length=_length)


class Cylinder(Model):
    def __init__(self, radius: "Radius" = None, length: "Length" = None):
        self.radius = radius
        self.length = length

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cylinder")
        if self.radius is not None:
            el.append(self.radius.to_sdf())
        if self.length is not None:
            el.append(self.length.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Cylinder":
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius) if _c_radius is not None else None
        _c_length = el.find("length")
        _length = Length.from_sdf(_c_length) if _c_length is not None else None
        return cls(radius=_radius, length=_length)


class Uri(Model):
    def __init__(self, uri: str = "__default__"):
        self.uri = uri

    def to_sdf(self) -> ET.Element:
        el = ET.Element("uri")
        if self.uri is not None:
            el.text = self.uri
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Uri":
        _text = el.text or "__default__"
        _uri = _text
        return cls(uri=_uri)


class Pos(Model):
    def __init__(self, pos: Vector3 = None):
        if pos is None:
            pos = Vector3.from_sdf("0 0 0")
        self.pos = pos

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pos")
        if self.pos is not None:
            el.text = self.pos.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pos":
        _text = el.text or "0 0 0"
        _pos = Vector3.from_sdf(_text)
        return cls(pos=_pos)


class Diffuse(Model):
    def __init__(self, diffuse: str = "__default__"):
        self.diffuse = diffuse

    def to_sdf(self) -> ET.Element:
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _text = el.text or "__default__"
        _diffuse = _text
        return cls(diffuse=_diffuse)


class Normal(Model):
    def __init__(self, normal: str = "__default__"):
        self.normal = normal

    def to_sdf(self) -> ET.Element:
        el = ET.Element("normal")
        if self.normal is not None:
            el.text = self.normal
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Normal":
        _text = el.text or "__default__"
        _normal = _text
        return cls(normal=_normal)


class Texture(Model):
    def __init__(self, size: "Size" = None, diffuse: "Diffuse" = None, normal: "Normal" = None):
        self.size = size
        self.diffuse = diffuse
        self.normal = normal

    def to_sdf(self) -> ET.Element:
        el = ET.Element("texture")
        if self.size is not None:
            el.append(self.size.to_sdf())
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf())
        if self.normal is not None:
            el.append(self.normal.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Texture":
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size) if _c_size is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse) if _c_diffuse is not None else None
        _c_normal = el.find("normal")
        _normal = Normal.from_sdf(_c_normal) if _c_normal is not None else None
        return cls(size=_size, diffuse=_diffuse, normal=_normal)


class MinHeight(Model):
    def __init__(self, min_height: float = 0):
        self.min_height = min_height

    def to_sdf(self) -> ET.Element:
        el = ET.Element("min_height")
        if self.min_height is not None:
            el.text = str(self.min_height)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MinHeight":
        _text = el.text or 0
        _min_height = _parse_double(_text)
        return cls(min_height=_min_height)


class FadeDist(Model):
    def __init__(self, fade_dist: float = 0):
        self.fade_dist = fade_dist

    def to_sdf(self) -> ET.Element:
        el = ET.Element("fade_dist")
        if self.fade_dist is not None:
            el.text = str(self.fade_dist)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "FadeDist":
        _text = el.text or 0
        _fade_dist = _parse_double(_text)
        return cls(fade_dist=_fade_dist)


class Blend(Model):
    def __init__(self, min_height: "MinHeight" = None, fade_dist: "FadeDist" = None):
        self.min_height = min_height
        self.fade_dist = fade_dist

    def to_sdf(self) -> ET.Element:
        el = ET.Element("blend")
        if self.min_height is not None:
            el.append(self.min_height.to_sdf())
        if self.fade_dist is not None:
            el.append(self.fade_dist.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Blend":
        _c_min_height = el.find("min_height")
        _min_height = MinHeight.from_sdf(_c_min_height) if _c_min_height is not None else None
        _c_fade_dist = el.find("fade_dist")
        _fade_dist = FadeDist.from_sdf(_c_fade_dist) if _c_fade_dist is not None else None
        return cls(min_height=_min_height, fade_dist=_fade_dist)


class UseTerrainPaging(Model):
    def __init__(self, use_terrain_paging: bool = False):
        self.use_terrain_paging = use_terrain_paging

    def to_sdf(self) -> ET.Element:
        el = ET.Element("use_terrain_paging")
        if self.use_terrain_paging is not None:
            el.text = str(self.use_terrain_paging).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UseTerrainPaging":
        _text = el.text or False
        _use_terrain_paging = _text.strip().lower() == 'true'
        return cls(use_terrain_paging=_use_terrain_paging)


class Heightmap(Model):
    def __init__(
            self,
            uri: "Uri" = None,
            size: "Size" = None,
            pos: "Pos" = None,
            texture: List["Texture"] = None,
            blend: List["Blend"] = None,
            use_terrain_paging: "UseTerrainPaging" = None
    ):
        self.uri = uri
        self.size = size
        self.pos = pos
        self.texture = texture or []
        self.blend = blend or []
        self.use_terrain_paging = use_terrain_paging

    def to_sdf(self) -> ET.Element:
        el = ET.Element("heightmap")
        if self.uri is not None:
            el.append(self.uri.to_sdf())
        if self.size is not None:
            el.append(self.size.to_sdf())
        if self.pos is not None:
            el.append(self.pos.to_sdf())
        for item in (self.texture or []):
            el.append(item.to_sdf())
        for item in (self.blend or []):
            el.append(item.to_sdf())
        if self.use_terrain_paging is not None:
            el.append(self.use_terrain_paging.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Heightmap":
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri) if _c_uri is not None else None
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size) if _c_size is not None else None
        _c_pos = el.find("pos")
        _pos = Pos.from_sdf(_c_pos) if _c_pos is not None else None
        _texture = [Texture.from_sdf(c) for c in el.findall("texture")]
        _blend = [Blend.from_sdf(c) for c in el.findall("blend")]
        _c_use_terrain_paging = el.find("use_terrain_paging")
        _use_terrain_paging = UseTerrainPaging.from_sdf(
            _c_use_terrain_paging) if _c_use_terrain_paging is not None else None
        return cls(uri=_uri, size=_size, pos=_pos, texture=_texture, blend=_blend,
                   use_terrain_paging=_use_terrain_paging)


class Scale(Model):
    def __init__(self, scale: float = 1):
        self.scale = scale

    def to_sdf(self) -> ET.Element:
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = str(self.scale)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scale":
        _text = el.text or 1
        _scale = _parse_double(_text)
        return cls(scale=_scale)


class Threshold(Model):
    def __init__(self, threshold: int = 200):
        self.threshold = threshold

    def to_sdf(self) -> ET.Element:
        el = ET.Element("threshold")
        if self.threshold is not None:
            el.text = str(self.threshold)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Threshold":
        _text = el.text or 200
        _threshold = _parse_int32(_text)
        return cls(threshold=_threshold)


class Height(Model):
    def __init__(self, height: float = 1):
        self.height = height

    def to_sdf(self) -> ET.Element:
        el = ET.Element("height")
        if self.height is not None:
            el.text = str(self.height)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Height":
        _text = el.text or 1
        _height = _parse_double(_text)
        return cls(height=_height)


class Granularity(Model):
    def __init__(self, granularity: int = 1):
        self.granularity = granularity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("granularity")
        if self.granularity is not None:
            el.text = str(self.granularity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Granularity":
        _text = el.text or 1
        _granularity = _parse_int32(_text)
        return cls(granularity=_granularity)


class Image(Model):
    def __init__(
            self,
            uri: "Uri" = None,
            scale: "Scale" = None,
            threshold: "Threshold" = None,
            height: "Height" = None,
            granularity: "Granularity" = None
    ):
        self.uri = uri
        self.scale = scale
        self.threshold = threshold
        self.height = height
        self.granularity = granularity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("image")
        if self.uri is not None:
            el.append(self.uri.to_sdf())
        if self.scale is not None:
            el.append(self.scale.to_sdf())
        if self.threshold is not None:
            el.append(self.threshold.to_sdf())
        if self.height is not None:
            el.append(self.height.to_sdf())
        if self.granularity is not None:
            el.append(self.granularity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Image":
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri) if _c_uri is not None else None
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale) if _c_scale is not None else None
        _c_threshold = el.find("threshold")
        _threshold = Threshold.from_sdf(_c_threshold) if _c_threshold is not None else None
        _c_height = el.find("height")
        _height = Height.from_sdf(_c_height) if _c_height is not None else None
        _c_granularity = el.find("granularity")
        _granularity = Granularity.from_sdf(_c_granularity) if _c_granularity is not None else None
        return cls(uri=_uri, scale=_scale, threshold=_threshold, height=_height, granularity=_granularity)


class Name(Model):
    def __init__(self, name: str = "__default__"):
        self.name = name

    def to_sdf(self) -> ET.Element:
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Name":
        _text = el.text or "__default__"
        _name = _text
        return cls(name=_name)


class Center(Model):
    def __init__(self, center: bool = False):
        self.center = center

    def to_sdf(self) -> ET.Element:
        el = ET.Element("center")
        if self.center is not None:
            el.text = str(self.center).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Center":
        _text = el.text or False
        _center = _text.strip().lower() == 'true'
        return cls(center=_center)


class Submesh(Model):
    def __init__(self, name: "Name" = None, center: "Center" = None):
        self.name = name
        self.center = center

    def to_sdf(self) -> ET.Element:
        el = ET.Element("submesh")
        if self.name is not None:
            el.append(self.name.to_sdf())
        if self.center is not None:
            el.append(self.center.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Submesh":
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name) if _c_name is not None else None
        _c_center = el.find("center")
        _center = Center.from_sdf(_c_center) if _c_center is not None else None
        return cls(name=_name, center=_center)


class Mesh(Model):
    def __init__(self, uri: "Uri" = None, submesh: "Submesh" = None, scale: "Scale" = None):
        self.uri = uri
        self.submesh = submesh
        self.scale = scale

    def to_sdf(self) -> ET.Element:
        el = ET.Element("mesh")
        if self.uri is not None:
            el.append(self.uri.to_sdf())
        if self.submesh is not None:
            el.append(self.submesh.to_sdf())
        if self.scale is not None:
            el.append(self.scale.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mesh":
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri) if _c_uri is not None else None
        _c_submesh = el.find("submesh")
        _submesh = Submesh.from_sdf(_c_submesh) if _c_submesh is not None else None
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale) if _c_scale is not None else None
        return cls(uri=_uri, submesh=_submesh, scale=_scale)


class Plane(Model):
    def __init__(self, normal: "Normal" = None, size: "Size" = None):
        self.normal = normal
        self.size = size

    def to_sdf(self) -> ET.Element:
        el = ET.Element("plane")
        if self.normal is not None:
            el.append(self.normal.to_sdf())
        if self.size is not None:
            el.append(self.size.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Plane":
        _c_normal = el.find("normal")
        _normal = Normal.from_sdf(_c_normal) if _c_normal is not None else None
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size) if _c_size is not None else None
        return cls(normal=_normal, size=_size)


class Sphere(Model):
    def __init__(self, radius: "Radius" = None):
        self.radius = radius

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sphere")
        if self.radius is not None:
            el.append(self.radius.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sphere":
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius) if _c_radius is not None else None
        return cls(radius=_radius)


class Geometry(Model):
    def __init__(
            self,
            box: "Box" = None,
            cylinder: "Cylinder" = None,
            heightmap: "Heightmap" = None,
            image: "Image" = None,
            mesh: "Mesh" = None,
            plane: "Plane" = None,
            polyline: "Polyline" = None,
            sphere: "Sphere" = None,
            empty: "Empty" = None
    ):
        self.box = box
        self.cylinder = cylinder
        self.heightmap = heightmap
        self.image = image
        self.mesh = mesh
        self.plane = plane
        self.polyline = polyline
        self.sphere = sphere
        self.empty = empty

    def to_sdf(self) -> ET.Element:
        el = ET.Element("geometry")
        if self.box is not None:
            el.append(self.box.to_sdf())
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf())
        if self.heightmap is not None:
            el.append(self.heightmap.to_sdf())
        if self.image is not None:
            el.append(self.image.to_sdf())
        if self.mesh is not None:
            el.append(self.mesh.to_sdf())
        if self.plane is not None:
            el.append(self.plane.to_sdf())
        if self.polyline is not None:
            el.append(self.polyline.to_sdf())
        if self.sphere is not None:
            el.append(self.sphere.to_sdf())
        if self.empty is not None:
            el.append(self.empty.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Geometry":
        _c_box = el.find("box")
        _box = Box.from_sdf(_c_box) if _c_box is not None else None
        _c_cylinder = el.find("cylinder")
        _cylinder = Cylinder.from_sdf(_c_cylinder) if _c_cylinder is not None else None
        _c_heightmap = el.find("heightmap")
        _heightmap = Heightmap.from_sdf(_c_heightmap) if _c_heightmap is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image) if _c_image is not None else None
        _c_mesh = el.find("mesh")
        _mesh = Mesh.from_sdf(_c_mesh) if _c_mesh is not None else None
        _c_plane = el.find("plane")
        _plane = Plane.from_sdf(_c_plane) if _c_plane is not None else None
        _c_polyline = el.find("polyline")
        _polyline = Polyline.from_sdf(_c_polyline) if _c_polyline is not None else None
        _c_sphere = el.find("sphere")
        _sphere = Sphere.from_sdf(_c_sphere) if _c_sphere is not None else None
        _c_empty = el.find("empty")
        _empty = Empty.from_sdf(_c_empty) if _c_empty is not None else None
        return cls(box=_box, cylinder=_cylinder, heightmap=_heightmap, image=_image, mesh=_mesh, plane=_plane,
                   polyline=_polyline, sphere=_sphere, empty=_empty)


class RestitutionCoefficient(Model):
    def __init__(self, restitution_coefficient: float = 0):
        self.restitution_coefficient = restitution_coefficient

    def to_sdf(self) -> ET.Element:
        el = ET.Element("restitution_coefficient")
        if self.restitution_coefficient is not None:
            el.text = str(self.restitution_coefficient)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "RestitutionCoefficient":
        _text = el.text or 0
        _restitution_coefficient = _parse_double(_text)
        return cls(restitution_coefficient=_restitution_coefficient)


class Bounce(Model):
    def __init__(
            self,
            restitution_coefficient: "RestitutionCoefficient" = None,
            threshold: "Threshold" = None
    ):
        self.restitution_coefficient = restitution_coefficient
        self.threshold = threshold

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bounce")
        if self.restitution_coefficient is not None:
            el.append(self.restitution_coefficient.to_sdf())
        if self.threshold is not None:
            el.append(self.threshold.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bounce":
        _c_restitution_coefficient = el.find("restitution_coefficient")
        _restitution_coefficient = RestitutionCoefficient.from_sdf(
            _c_restitution_coefficient) if _c_restitution_coefficient is not None else None
        _c_threshold = el.find("threshold")
        _threshold = Threshold.from_sdf(_c_threshold) if _c_threshold is not None else None
        return cls(restitution_coefficient=_restitution_coefficient, threshold=_threshold)


class Ode(Model):
    def __init__(self, slip: "Slip" = None):
        self.slip = slip

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ode")
        if self.slip is not None:
            el.append(self.slip.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_slip = el.find("slip")
        _slip = Slip.from_sdf(_c_slip) if _c_slip is not None else None
        return cls(slip=_slip)


class Friction2(Model):
    def __init__(self, friction2: float = 1):
        self.friction2 = friction2

    def to_sdf(self) -> ET.Element:
        el = ET.Element("friction2")
        if self.friction2 is not None:
            el.text = str(self.friction2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Friction2":
        _text = el.text or 1
        _friction2 = _parse_double(_text)
        return cls(friction2=_friction2)


class Fdir1(Model):
    def __init__(self, fdir1: Vector3 = None):
        if fdir1 is None:
            fdir1 = Vector3.from_sdf("0 0 0")
        self.fdir1 = fdir1

    def to_sdf(self) -> ET.Element:
        el = ET.Element("fdir1")
        if self.fdir1 is not None:
            el.text = self.fdir1.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fdir1":
        _text = el.text or "0 0 0"
        _fdir1 = Vector3.from_sdf(_text)
        return cls(fdir1=_fdir1)


class RollingFriction(Model):
    def __init__(self, rolling_friction: float = 1):
        self.rolling_friction = rolling_friction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("rolling_friction")
        if self.rolling_friction is not None:
            el.text = str(self.rolling_friction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "RollingFriction":
        _text = el.text or 1
        _rolling_friction = _parse_double(_text)
        return cls(rolling_friction=_rolling_friction)


class Bullet(Model):
    def __init__(
            self,
            friction: "Friction" = None,
            friction2: "Friction2" = None,
            fdir1: "Fdir1" = None,
            rolling_friction: "RollingFriction" = None
    ):
        self.friction = friction
        self.friction2 = friction2
        self.fdir1 = fdir1
        self.rolling_friction = rolling_friction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bullet")
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        if self.friction2 is not None:
            el.append(self.friction2.to_sdf())
        if self.fdir1 is not None:
            el.append(self.fdir1.to_sdf())
        if self.rolling_friction is not None:
            el.append(self.rolling_friction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        _c_friction2 = el.find("friction2")
        _friction2 = Friction2.from_sdf(_c_friction2) if _c_friction2 is not None else None
        _c_fdir1 = el.find("fdir1")
        _fdir1 = Fdir1.from_sdf(_c_fdir1) if _c_fdir1 is not None else None
        _c_rolling_friction = el.find("rolling_friction")
        _rolling_friction = RollingFriction.from_sdf(_c_rolling_friction) if _c_rolling_friction is not None else None
        return cls(friction=_friction, friction2=_friction2, fdir1=_fdir1, rolling_friction=_rolling_friction)


class Friction(Model):
    def __init__(self, torsional: "Torsional" = None, ode: "Ode" = None, bullet: "Bullet" = None):
        self.torsional = torsional
        self.ode = ode
        self.bullet = bullet

    def to_sdf(self) -> ET.Element:
        el = ET.Element("friction")
        if self.torsional is not None:
            el.append(self.torsional.to_sdf())
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Friction":
        _c_torsional = el.find("torsional")
        _torsional = Torsional.from_sdf(_c_torsional) if _c_torsional is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(torsional=_torsional, ode=_ode, bullet=_bullet)


class CollideWithoutContact(Model):
    def __init__(self, collide_without_contact: bool = False):
        self.collide_without_contact = collide_without_contact

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collide_without_contact")
        if self.collide_without_contact is not None:
            el.text = str(self.collide_without_contact).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollideWithoutContact":
        _text = el.text or False
        _collide_without_contact = _text.strip().lower() == 'true'
        return cls(collide_without_contact=_collide_without_contact)


class CollideWithoutContactBitmask(Model):
    def __init__(self, collide_without_contact_bitmask: int = 1):
        self.collide_without_contact_bitmask = collide_without_contact_bitmask

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collide_without_contact_bitmask")
        if self.collide_without_contact_bitmask is not None:
            el.text = str(self.collide_without_contact_bitmask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollideWithoutContactBitmask":
        _text = el.text or 1
        _collide_without_contact_bitmask = _parse_uint32(_text)
        return cls(collide_without_contact_bitmask=_collide_without_contact_bitmask)


class CollideBitmask(Model):
    def __init__(self, collide_bitmask: int = 65535):
        self.collide_bitmask = collide_bitmask

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collide_bitmask")
        if self.collide_bitmask is not None:
            el.text = str(self.collide_bitmask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollideBitmask":
        _text = el.text or 65535
        _collide_bitmask = _parse_uint32(_text)
        return cls(collide_bitmask=_collide_bitmask)


class Contact(Model):
    def __init__(
            self,
            collide_without_contact: "CollideWithoutContact" = None,
            collide_without_contact_bitmask: "CollideWithoutContactBitmask" = None,
            collide_bitmask: "CollideBitmask" = None,
            poissons_ratio: "PoissonsRatio" = None,
            elastic_modulus: "ElasticModulus" = None,
            ode: "Ode" = None,
            bullet: "Bullet" = None
    ):
        self.collide_without_contact = collide_without_contact
        self.collide_without_contact_bitmask = collide_without_contact_bitmask
        self.collide_bitmask = collide_bitmask
        self.poissons_ratio = poissons_ratio
        self.elastic_modulus = elastic_modulus
        self.ode = ode
        self.bullet = bullet

    def to_sdf(self) -> ET.Element:
        el = ET.Element("contact")
        if self.collide_without_contact is not None:
            el.append(self.collide_without_contact.to_sdf())
        if self.collide_without_contact_bitmask is not None:
            el.append(self.collide_without_contact_bitmask.to_sdf())
        if self.collide_bitmask is not None:
            el.append(self.collide_bitmask.to_sdf())
        if self.poissons_ratio is not None:
            el.append(self.poissons_ratio.to_sdf())
        if self.elastic_modulus is not None:
            el.append(self.elastic_modulus.to_sdf())
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Contact":
        _c_collide_without_contact = el.find("collide_without_contact")
        _collide_without_contact = CollideWithoutContact.from_sdf(
            _c_collide_without_contact) if _c_collide_without_contact is not None else None
        _c_collide_without_contact_bitmask = el.find("collide_without_contact_bitmask")
        _collide_without_contact_bitmask = CollideWithoutContactBitmask.from_sdf(
            _c_collide_without_contact_bitmask) if _c_collide_without_contact_bitmask is not None else None
        _c_collide_bitmask = el.find("collide_bitmask")
        _collide_bitmask = CollideBitmask.from_sdf(_c_collide_bitmask) if _c_collide_bitmask is not None else None
        _c_poissons_ratio = el.find("poissons_ratio")
        _poissons_ratio = PoissonsRatio.from_sdf(_c_poissons_ratio) if _c_poissons_ratio is not None else None
        _c_elastic_modulus = el.find("elastic_modulus")
        _elastic_modulus = ElasticModulus.from_sdf(_c_elastic_modulus) if _c_elastic_modulus is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(collide_without_contact=_collide_without_contact,
                   collide_without_contact_bitmask=_collide_without_contact_bitmask, collide_bitmask=_collide_bitmask,
                   poissons_ratio=_poissons_ratio, elastic_modulus=_elastic_modulus, ode=_ode, bullet=_bullet)


class BoneAttachment(Model):
    def __init__(self, bone_attachment: float = 100.0):
        self.bone_attachment = bone_attachment

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bone_attachment")
        if self.bone_attachment is not None:
            el.text = str(self.bone_attachment)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "BoneAttachment":
        _text = el.text or 100.0
        _bone_attachment = _parse_double(_text)
        return cls(bone_attachment=_bone_attachment)


class Stiffness(Model):
    def __init__(self, stiffness: float = 100.0):
        self.stiffness = stiffness

    def to_sdf(self) -> ET.Element:
        el = ET.Element("stiffness")
        if self.stiffness is not None:
            el.text = str(self.stiffness)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Stiffness":
        _text = el.text or 100.0
        _stiffness = _parse_double(_text)
        return cls(stiffness=_stiffness)


class Damping(Model):
    def __init__(self, damping: float = 10.0):
        self.damping = damping

    def to_sdf(self) -> ET.Element:
        el = ET.Element("damping")
        if self.damping is not None:
            el.text = str(self.damping)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Damping":
        _text = el.text or 10.0
        _damping = _parse_double(_text)
        return cls(damping=_damping)


class FleshMassFraction(Model):
    def __init__(self, flesh_mass_fraction: float = 0.05):
        self.flesh_mass_fraction = flesh_mass_fraction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("flesh_mass_fraction")
        if self.flesh_mass_fraction is not None:
            el.text = str(self.flesh_mass_fraction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "FleshMassFraction":
        _text = el.text or 0.05
        _flesh_mass_fraction = _parse_double(_text)
        return cls(flesh_mass_fraction=_flesh_mass_fraction)


class Dart(Model):
    def __init__(
            self,
            bone_attachment: "BoneAttachment" = None,
            stiffness: "Stiffness" = None,
            damping: "Damping" = None,
            flesh_mass_fraction: "FleshMassFraction" = None
    ):
        self.bone_attachment = bone_attachment
        self.stiffness = stiffness
        self.damping = damping
        self.flesh_mass_fraction = flesh_mass_fraction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dart")
        if self.bone_attachment is not None:
            el.append(self.bone_attachment.to_sdf())
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf())
        if self.damping is not None:
            el.append(self.damping.to_sdf())
        if self.flesh_mass_fraction is not None:
            el.append(self.flesh_mass_fraction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dart":
        _c_bone_attachment = el.find("bone_attachment")
        _bone_attachment = BoneAttachment.from_sdf(_c_bone_attachment) if _c_bone_attachment is not None else None
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness) if _c_stiffness is not None else None
        _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping) if _c_damping is not None else None
        _c_flesh_mass_fraction = el.find("flesh_mass_fraction")
        _flesh_mass_fraction = FleshMassFraction.from_sdf(
            _c_flesh_mass_fraction) if _c_flesh_mass_fraction is not None else None
        return cls(bone_attachment=_bone_attachment, stiffness=_stiffness, damping=_damping,
                   flesh_mass_fraction=_flesh_mass_fraction)


class SoftContact(Model):
    def __init__(self, dart: "Dart" = None):
        self.dart = dart

    def to_sdf(self) -> ET.Element:
        el = ET.Element("soft_contact")
        if self.dart is not None:
            el.append(self.dart.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SoftContact":
        _c_dart = el.find("dart")
        _dart = Dart.from_sdf(_c_dart) if _c_dart is not None else None
        return cls(dart=_dart)


class Surface(Model):
    def __init__(
            self,
            bounce: "Bounce" = None,
            friction: "Friction" = None,
            contact: "Contact" = None,
            soft_contact: "SoftContact" = None
    ):
        self.bounce = bounce
        self.friction = friction
        self.contact = contact
        self.soft_contact = soft_contact

    def to_sdf(self) -> ET.Element:
        el = ET.Element("surface")
        if self.bounce is not None:
            el.append(self.bounce.to_sdf())
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        if self.soft_contact is not None:
            el.append(self.soft_contact.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Surface":
        _c_bounce = el.find("bounce")
        _bounce = Bounce.from_sdf(_c_bounce) if _c_bounce is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        _c_soft_contact = el.find("soft_contact")
        _soft_contact = SoftContact.from_sdf(_c_soft_contact) if _c_soft_contact is not None else None
        return cls(bounce=_bounce, friction=_friction, contact=_contact, soft_contact=_soft_contact)


class LaserRetro(Model):
    def __init__(self, laser_retro: float = 0):
        self.laser_retro = laser_retro

    def to_sdf(self) -> ET.Element:
        el = ET.Element("laser_retro")
        if self.laser_retro is not None:
            el.text = str(self.laser_retro)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LaserRetro":
        _text = el.text or 0
        _laser_retro = _parse_double(_text)
        return cls(laser_retro=_laser_retro)


class MaxContacts(Model):
    def __init__(self, max_contacts: int = 10):
        self.max_contacts = max_contacts

    def to_sdf(self) -> ET.Element:
        el = ET.Element("max_contacts")
        if self.max_contacts is not None:
            el.text = str(self.max_contacts)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxContacts":
        _text = el.text or 10
        _max_contacts = _parse_int32(_text)
        return cls(max_contacts=_max_contacts)


class Collision(Model):
    def __init__(
            self,
            name: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            geometry: "Geometry" = None,
            surface: "Surface" = None,
            laser_retro: "LaserRetro" = None,
            max_contacts: "MaxContacts" = None
    ):
        self.name = name
        self.frame = frame or []
        self.pose = pose
        self.geometry = geometry
        self.surface = surface
        self.laser_retro = laser_retro
        self.max_contacts = max_contacts

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collision")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.geometry is not None:
            el.append(self.geometry.to_sdf())
        if self.surface is not None:
            el.append(self.surface.to_sdf())
        if self.laser_retro is not None:
            el.append(self.laser_retro.to_sdf())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Collision":
        _name = el.get("name", "__default__")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry) if _c_geometry is not None else None
        _c_surface = el.find("surface")
        _surface = Surface.from_sdf(_c_surface) if _c_surface is not None else None
        _c_laser_retro = el.find("laser_retro")
        _laser_retro = LaserRetro.from_sdf(_c_laser_retro) if _c_laser_retro is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        return cls(name=_name, frame=_frame, pose=_pose, geometry=_geometry, surface=_surface, laser_retro=_laser_retro,
                   max_contacts=_max_contacts)


class Script(Model):
    def __init__(self, uri: List["Uri"] = None, name: "Name" = None):
        self.uri = uri or []
        self.name = name

    def to_sdf(self) -> ET.Element:
        el = ET.Element("script")
        for item in (self.uri or []):
            el.append(item.to_sdf())
        if self.name is not None:
            el.append(self.name.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Script":
        _uri = [Uri.from_sdf(c) for c in el.findall("uri")]
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name) if _c_name is not None else None
        return cls(uri=_uri, name=_name)


class NormalMap(Model):
    def __init__(self, normal_map: str = "__default__"):
        self.normal_map = normal_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("normal_map")
        if self.normal_map is not None:
            el.text = self.normal_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "NormalMap":
        _text = el.text or "__default__"
        _normal_map = _text
        return cls(normal_map=_normal_map)


class Shader(Model):
    def __init__(self, type: str = "pixel", normal_map: "NormalMap" = None):
        self.type = type
        self.normal_map = normal_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("shader")
        if self.type is not None:
            el.set("type", self.type)
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Shader":
        _type = el.get("type", "pixel")
        _c_normal_map = el.find("normal_map")
        _normal_map = NormalMap.from_sdf(_c_normal_map) if _c_normal_map is not None else None
        return cls(type=_type, normal_map=_normal_map)


class Lighting(Model):
    def __init__(self, lighting: bool = True):
        self.lighting = lighting

    def to_sdf(self) -> ET.Element:
        el = ET.Element("lighting")
        if self.lighting is not None:
            el.text = str(self.lighting).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Lighting":
        _text = el.text or True
        _lighting = _text.strip().lower() == 'true'
        return cls(lighting=_lighting)


class Ambient(Model):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0 0 0 1")
        self.ambient = ambient

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _text = el.text or "0 0 0 1"
        _ambient = Color.from_sdf(_text)
        return cls(ambient=_ambient)


class Specular(Model):
    def __init__(self, specular: Color = None):
        if specular is None:
            specular = Color.from_sdf("0 0 0 1")
        self.specular = specular

    def to_sdf(self) -> ET.Element:
        el = ET.Element("specular")
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _text = el.text or "0 0 0 1"
        _specular = Color.from_sdf(_text)
        return cls(specular=_specular)


class Emissive(Model):
    def __init__(self, emissive: Color = None):
        if emissive is None:
            emissive = Color.from_sdf("0 0 0 1")
        self.emissive = emissive

    def to_sdf(self) -> ET.Element:
        el = ET.Element("emissive")
        if self.emissive is not None:
            el.text = self.emissive.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Emissive":
        _text = el.text or "0 0 0 1"
        _emissive = Color.from_sdf(_text)
        return cls(emissive=_emissive)


class Material(Model):
    def __init__(
            self,
            script: "Script" = None,
            shader: "Shader" = None,
            lighting: "Lighting" = None,
            ambient: "Ambient" = None,
            diffuse: "Diffuse" = None,
            specular: "Specular" = None,
            emissive: "Emissive" = None
    ):
        self.script = script
        self.shader = shader
        self.lighting = lighting
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.emissive = emissive

    def to_sdf(self) -> ET.Element:
        el = ET.Element("material")
        if self.script is not None:
            el.append(self.script.to_sdf())
        if self.shader is not None:
            el.append(self.shader.to_sdf())
        if self.lighting is not None:
            el.append(self.lighting.to_sdf())
        if self.ambient is not None:
            el.append(self.ambient.to_sdf())
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf())
        if self.specular is not None:
            el.append(self.specular.to_sdf())
        if self.emissive is not None:
            el.append(self.emissive.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Material":
        _c_script = el.find("script")
        _script = Script.from_sdf(_c_script) if _c_script is not None else None
        _c_shader = el.find("shader")
        _shader = Shader.from_sdf(_c_shader) if _c_shader is not None else None
        _c_lighting = el.find("lighting")
        _lighting = Lighting.from_sdf(_c_lighting) if _c_lighting is not None else None
        _c_ambient = el.find("ambient")
        _ambient = Ambient.from_sdf(_c_ambient) if _c_ambient is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse) if _c_diffuse is not None else None
        _c_specular = el.find("specular")
        _specular = Specular.from_sdf(_c_specular) if _c_specular is not None else None
        _c_emissive = el.find("emissive")
        _emissive = Emissive.from_sdf(_c_emissive) if _c_emissive is not None else None
        return cls(script=_script, shader=_shader, lighting=_lighting, ambient=_ambient, diffuse=_diffuse,
                   specular=_specular, emissive=_emissive)


class Plugin(Model):
    def __init__(self, name: str = "__default__", filename: str = "__default__"):
        self.name = name
        self.filename = filename

    def to_sdf(self) -> ET.Element:
        el = ET.Element("plugin")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.set("filename", self.filename)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Plugin":
        _name = el.get("name", "__default__")
        _filename = el.get("filename", "__default__")
        return cls(name=_name, filename=_filename)


class CastShadows(Model):
    def __init__(self, cast_shadows: bool = True):
        self.cast_shadows = cast_shadows

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cast_shadows")
        if self.cast_shadows is not None:
            el.text = str(self.cast_shadows).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CastShadows":
        _text = el.text or True
        _cast_shadows = _text.strip().lower() == 'true'
        return cls(cast_shadows=_cast_shadows)


class Transparency(Model):
    def __init__(self, transparency: float = 0.0):
        self.transparency = transparency

    def to_sdf(self) -> ET.Element:
        el = ET.Element("transparency")
        if self.transparency is not None:
            el.text = str(self.transparency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Transparency":
        _text = el.text or 0.0
        _transparency = _parse_double(_text)
        return cls(transparency=_transparency)


class Visual(Model):
    def __init__(
            self,
            name: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            material: "Material" = None,
            geometry: "Geometry" = None,
            plugin: List["Plugin"] = None,
            cast_shadows: "CastShadows" = None,
            laser_retro: "LaserRetro" = None,
            transparency: "Transparency" = None,
            meta: "Meta" = None
    ):
        self.name = name
        self.frame = frame or []
        self.pose = pose
        self.material = material
        self.geometry = geometry
        self.plugin = plugin or []
        self.cast_shadows = cast_shadows
        self.laser_retro = laser_retro
        self.transparency = transparency
        self.meta = meta

    def to_sdf(self) -> ET.Element:
        el = ET.Element("visual")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.material is not None:
            el.append(self.material.to_sdf())
        if self.geometry is not None:
            el.append(self.geometry.to_sdf())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.cast_shadows is not None:
            el.append(self.cast_shadows.to_sdf())
        if self.laser_retro is not None:
            el.append(self.laser_retro.to_sdf())
        if self.transparency is not None:
            el.append(self.transparency.to_sdf())
        if self.meta is not None:
            el.append(self.meta.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visual":
        _name = el.get("name", "__default__")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_material = el.find("material")
        _material = Material.from_sdf(_c_material) if _c_material is not None else None
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry) if _c_geometry is not None else None
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_cast_shadows = el.find("cast_shadows")
        _cast_shadows = CastShadows.from_sdf(_c_cast_shadows) if _c_cast_shadows is not None else None
        _c_laser_retro = el.find("laser_retro")
        _laser_retro = LaserRetro.from_sdf(_c_laser_retro) if _c_laser_retro is not None else None
        _c_transparency = el.find("transparency")
        _transparency = Transparency.from_sdf(_c_transparency) if _c_transparency is not None else None
        _c_meta = el.find("meta")
        _meta = Meta.from_sdf(_c_meta) if _c_meta is not None else None
        return cls(name=_name, frame=_frame, pose=_pose, material=_material, geometry=_geometry, plugin=_plugin,
                   cast_shadows=_cast_shadows, laser_retro=_laser_retro, transparency=_transparency, meta=_meta)


class HorizontalFov(Model):
    def __init__(self, horizontal_fov: float = 1.047):
        self.horizontal_fov = horizontal_fov

    def to_sdf(self) -> ET.Element:
        el = ET.Element("horizontal_fov")
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "HorizontalFov":
        _text = el.text or 1.047
        _horizontal_fov = _parse_double(_text)
        return cls(horizontal_fov=_horizontal_fov)


class Near(Model):
    def __init__(self, near: float = .1):
        self.near = near

    def to_sdf(self) -> ET.Element:
        el = ET.Element("near")
        if self.near is not None:
            el.text = str(self.near)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Near":
        _text = el.text or .1
        _near = _parse_double(_text)
        return cls(near=_near)


class Far(Model):
    def __init__(self, far: float = 100):
        self.far = far

    def to_sdf(self) -> ET.Element:
        el = ET.Element("far")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Far":
        _text = el.text or 100
        _far = _parse_double(_text)
        return cls(far=_far)


class Clip(Model):
    def __init__(self, near: "Near" = None, far: "Far" = None):
        self.near = near
        self.far = far

    def to_sdf(self) -> ET.Element:
        el = ET.Element("clip")
        if self.near is not None:
            el.append(self.near.to_sdf())
        if self.far is not None:
            el.append(self.far.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Clip":
        _c_near = el.find("near")
        _near = Near.from_sdf(_c_near) if _c_near is not None else None
        _c_far = el.find("far")
        _far = Far.from_sdf(_c_far) if _c_far is not None else None
        return cls(near=_near, far=_far)


class Path(Model):
    def __init__(self, path: str = "__default__"):
        self.path = path

    def to_sdf(self) -> ET.Element:
        el = ET.Element("path")
        if self.path is not None:
            el.text = self.path
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Path":
        _text = el.text or "__default__"
        _path = _text
        return cls(path=_path)


class Save(Model):
    def __init__(self, enabled: bool = False, path: "Path" = None):
        self.enabled = enabled
        self.path = path

    def to_sdf(self) -> ET.Element:
        el = ET.Element("save")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        if self.path is not None:
            el.append(self.path.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Save":
        _enabled = el.get("enabled", False).strip().lower() == 'true'
        _c_path = el.find("path")
        _path = Path.from_sdf(_c_path) if _c_path is not None else None
        return cls(enabled=_enabled, path=_path)


class Output(Model):
    def __init__(self, output: str = "depths"):
        self.output = output

    def to_sdf(self) -> ET.Element:
        el = ET.Element("output")
        if self.output is not None:
            el.text = self.output
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Output":
        _text = el.text or "depths"
        _output = _text
        return cls(output=_output)


class DepthCamera(Model):
    def __init__(self, output: "Output" = None):
        self.output = output

    def to_sdf(self) -> ET.Element:
        el = ET.Element("depth_camera")
        if self.output is not None:
            el.append(self.output.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DepthCamera":
        _c_output = el.find("output")
        _output = Output.from_sdf(_c_output) if _c_output is not None else None
        return cls(output=_output)


class Mean(Model):
    def __init__(self, mean: float = 0.0):
        self.mean = mean

    def to_sdf(self) -> ET.Element:
        el = ET.Element("mean")
        if self.mean is not None:
            el.text = str(self.mean)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mean":
        _text = el.text or 0.0
        _mean = _parse_double(_text)
        return cls(mean=_mean)


class Stddev(Model):
    def __init__(self, stddev: float = 0.0):
        self.stddev = stddev

    def to_sdf(self) -> ET.Element:
        el = ET.Element("stddev")
        if self.stddev is not None:
            el.text = str(self.stddev)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Stddev":
        _text = el.text or 0.0
        _stddev = _parse_double(_text)
        return cls(stddev=_stddev)


class BiasMean(Model):
    def __init__(self, bias_mean: float = 0.0):
        self.bias_mean = bias_mean

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bias_mean")
        if self.bias_mean is not None:
            el.text = str(self.bias_mean)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "BiasMean":
        _text = el.text or 0.0
        _bias_mean = _parse_double(_text)
        return cls(bias_mean=_bias_mean)


class BiasStddev(Model):
    def __init__(self, bias_stddev: float = 0.0):
        self.bias_stddev = bias_stddev

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bias_stddev")
        if self.bias_stddev is not None:
            el.text = str(self.bias_stddev)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "BiasStddev":
        _text = el.text or 0.0
        _bias_stddev = _parse_double(_text)
        return cls(bias_stddev=_bias_stddev)


class Precision(Model):
    def __init__(self, precision: float = 0.0):
        self.precision = precision

    def to_sdf(self) -> ET.Element:
        el = ET.Element("precision")
        if self.precision is not None:
            el.text = str(self.precision)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Precision":
        _text = el.text or 0.0
        _precision = _parse_double(_text)
        return cls(precision=_precision)


class Noise(Model):
    def __init__(
            self,
            type: str = "none",
            mean: "Mean" = None,
            stddev: "Stddev" = None,
            bias_mean: "BiasMean" = None,
            bias_stddev: "BiasStddev" = None,
            precision: "Precision" = None
    ):
        self.type = type
        self.mean = mean
        self.stddev = stddev
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.precision = precision

    def to_sdf(self) -> ET.Element:
        el = ET.Element("noise")
        if self.type is not None:
            el.set("type", self.type)
        if self.mean is not None:
            el.append(self.mean.to_sdf())
        if self.stddev is not None:
            el.append(self.stddev.to_sdf())
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf())
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf())
        if self.precision is not None:
            el.append(self.precision.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Noise":
        _type = el.get("type", "none")
        _c_mean = el.find("mean")
        _mean = Mean.from_sdf(_c_mean) if _c_mean is not None else None
        _c_stddev = el.find("stddev")
        _stddev = Stddev.from_sdf(_c_stddev) if _c_stddev is not None else None
        _c_bias_mean = el.find("bias_mean")
        _bias_mean = BiasMean.from_sdf(_c_bias_mean) if _c_bias_mean is not None else None
        _c_bias_stddev = el.find("bias_stddev")
        _bias_stddev = BiasStddev.from_sdf(_c_bias_stddev) if _c_bias_stddev is not None else None
        _c_precision = el.find("precision")
        _precision = Precision.from_sdf(_c_precision) if _c_precision is not None else None
        return cls(type=_type, mean=_mean, stddev=_stddev, bias_mean=_bias_mean, bias_stddev=_bias_stddev,
                   precision=_precision)


class Camera(Model):
    def __init__(
            self,
            name: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            horizontal_fov: "HorizontalFov" = None,
            image: "Image" = None,
            clip: "Clip" = None,
            save: "Save" = None,
            depth_camera: "DepthCamera" = None,
            noise: "Noise" = None,
            distortion: "Distortion" = None,
            lens: "Lens" = None
    ):
        self.name = name
        self.frame = frame or []
        self.pose = pose
        self.horizontal_fov = horizontal_fov
        self.image = image
        self.clip = clip
        self.save = save
        self.depth_camera = depth_camera
        self.noise = noise
        self.distortion = distortion
        self.lens = lens

    def to_sdf(self) -> ET.Element:
        el = ET.Element("camera")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf())
        if self.image is not None:
            el.append(self.image.to_sdf())
        if self.clip is not None:
            el.append(self.clip.to_sdf())
        if self.save is not None:
            el.append(self.save.to_sdf())
        if self.depth_camera is not None:
            el.append(self.depth_camera.to_sdf())
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        if self.distortion is not None:
            el.append(self.distortion.to_sdf())
        if self.lens is not None:
            el.append(self.lens.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _name = el.get("name", "__default__")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_horizontal_fov = el.find("horizontal_fov")
        _horizontal_fov = HorizontalFov.from_sdf(_c_horizontal_fov) if _c_horizontal_fov is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image) if _c_image is not None else None
        _c_clip = el.find("clip")
        _clip = Clip.from_sdf(_c_clip) if _c_clip is not None else None
        _c_save = el.find("save")
        _save = Save.from_sdf(_c_save) if _c_save is not None else None
        _c_depth_camera = el.find("depth_camera")
        _depth_camera = DepthCamera.from_sdf(_c_depth_camera) if _c_depth_camera is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        _c_distortion = el.find("distortion")
        _distortion = Distortion.from_sdf(_c_distortion) if _c_distortion is not None else None
        _c_lens = el.find("lens")
        _lens = Lens.from_sdf(_c_lens) if _c_lens is not None else None
        return cls(name=_name, frame=_frame, pose=_pose, horizontal_fov=_horizontal_fov, image=_image, clip=_clip,
                   save=_save, depth_camera=_depth_camera, noise=_noise, distortion=_distortion, lens=_lens)


class ForceTorque(Model):
    def __init__(self, frame: "Frame" = None, measure_direction: "MeasureDirection" = None):
        self.frame = frame
        self.measure_direction = measure_direction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("force_torque")
        if self.frame is not None:
            el.append(self.frame.to_sdf())
        if self.measure_direction is not None:
            el.append(self.measure_direction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ForceTorque":
        _c_frame = el.find("frame")
        _frame = Frame.from_sdf(_c_frame) if _c_frame is not None else None
        _c_measure_direction = el.find("measure_direction")
        _measure_direction = MeasureDirection.from_sdf(
            _c_measure_direction) if _c_measure_direction is not None else None
        return cls(frame=_frame, measure_direction=_measure_direction)


class Horizontal(Model):
    def __init__(self, noise: "Noise" = None):
        self.noise = noise

    def to_sdf(self) -> ET.Element:
        el = ET.Element("horizontal")
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Horizontal":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        return cls(noise=_noise)


class Vertical(Model):
    def __init__(self, noise: "Noise" = None):
        self.noise = noise

    def to_sdf(self) -> ET.Element:
        el = ET.Element("vertical")
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Vertical":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        return cls(noise=_noise)


class PositionSensing(Model):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        self.horizontal = horizontal
        self.vertical = vertical

    def to_sdf(self) -> ET.Element:
        el = ET.Element("position_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf())
        if self.vertical is not None:
            el.append(self.vertical.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PositionSensing":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical) if _c_vertical is not None else None
        return cls(horizontal=_horizontal, vertical=_vertical)


class VelocitySensing(Model):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        self.horizontal = horizontal
        self.vertical = vertical

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf())
        if self.vertical is not None:
            el.append(self.vertical.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VelocitySensing":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical) if _c_vertical is not None else None
        return cls(horizontal=_horizontal, vertical=_vertical)


class Gps(Model):
    def __init__(
            self,
            position_sensing: "PositionSensing" = None,
            velocity_sensing: "VelocitySensing" = None
    ):
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gps")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf())
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gps":
        _c_position_sensing = el.find("position_sensing")
        _position_sensing = PositionSensing.from_sdf(_c_position_sensing) if _c_position_sensing is not None else None
        _c_velocity_sensing = el.find("velocity_sensing")
        _velocity_sensing = VelocitySensing.from_sdf(_c_velocity_sensing) if _c_velocity_sensing is not None else None
        return cls(position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class Topic(Model):
    def __init__(self, topic: str = "__default_topic__"):
        self.topic = topic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Topic":
        _text = el.text or "__default_topic__"
        _topic = _text
        return cls(topic=_topic)


class Imu(Model):
    def __init__(
            self,
            topic: "Topic" = None,
            angular_velocity: "AngularVelocity" = None,
            linear_acceleration: "LinearAcceleration" = None,
            noise: "Noise" = None
    ):
        self.topic = topic
        self.angular_velocity = angular_velocity
        self.linear_acceleration = linear_acceleration
        self.noise = noise

    def to_sdf(self) -> ET.Element:
        el = ET.Element("imu")
        if self.topic is not None:
            el.append(self.topic.to_sdf())
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf())
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf())
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Imu":
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic) if _c_topic is not None else None
        _c_angular_velocity = el.find("angular_velocity")
        _angular_velocity = AngularVelocity.from_sdf(_c_angular_velocity) if _c_angular_velocity is not None else None
        _c_linear_acceleration = el.find("linear_acceleration")
        _linear_acceleration = LinearAcceleration.from_sdf(
            _c_linear_acceleration) if _c_linear_acceleration is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        return cls(topic=_topic, angular_velocity=_angular_velocity, linear_acceleration=_linear_acceleration,
                   noise=_noise)


class Scan(Model):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        self.horizontal = horizontal
        self.vertical = vertical

    def to_sdf(self) -> ET.Element:
        el = ET.Element("scan")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf())
        if self.vertical is not None:
            el.append(self.vertical.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scan":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical) if _c_vertical is not None else None
        return cls(horizontal=_horizontal, vertical=_vertical)


class Min(Model):
    def __init__(self, min: float = 0):
        self.min = min

    def to_sdf(self) -> ET.Element:
        el = ET.Element("min")
        if self.min is not None:
            el.text = str(self.min)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Min":
        _text = el.text or 0
        _min = _parse_double(_text)
        return cls(min=_min)


class Max(Model):
    def __init__(self, max: float = 0):
        self.max = max

    def to_sdf(self) -> ET.Element:
        el = ET.Element("max")
        if self.max is not None:
            el.text = str(self.max)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Max":
        _text = el.text or 0
        _max = _parse_double(_text)
        return cls(max=_max)


class Resolution(Model):
    def __init__(self, resolution: float = 0):
        self.resolution = resolution

    def to_sdf(self) -> ET.Element:
        el = ET.Element("resolution")
        if self.resolution is not None:
            el.text = str(self.resolution)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Resolution":
        _text = el.text or 0
        _resolution = _parse_double(_text)
        return cls(resolution=_resolution)


class Range(Model):
    def __init__(self, min: "Min" = None, max: "Max" = None, resolution: "Resolution" = None):
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_sdf(self) -> ET.Element:
        el = ET.Element("range")
        if self.min is not None:
            el.append(self.min.to_sdf())
        if self.max is not None:
            el.append(self.max.to_sdf())
        if self.resolution is not None:
            el.append(self.resolution.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Range":
        _c_min = el.find("min")
        _min = Min.from_sdf(_c_min) if _c_min is not None else None
        _c_max = el.find("max")
        _max = Max.from_sdf(_c_max) if _c_max is not None else None
        _c_resolution = el.find("resolution")
        _resolution = Resolution.from_sdf(_c_resolution) if _c_resolution is not None else None
        return cls(min=_min, max=_max, resolution=_resolution)


class Ray(Model):
    def __init__(self, scan: "Scan" = None, range: "Range" = None, noise: "Noise" = None):
        self.scan = scan
        self.range = range
        self.noise = noise

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ray")
        if self.scan is not None:
            el.append(self.scan.to_sdf())
        if self.range is not None:
            el.append(self.range.to_sdf())
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ray":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range) if _c_range is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        return cls(scan=_scan, range=_range, noise=_noise)


class Sonar(Model):
    def __init__(self, min: "Min" = None, max: "Max" = None, radius: "Radius" = None):
        self.min = min
        self.max = max
        self.radius = radius

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sonar")
        if self.min is not None:
            el.append(self.min.to_sdf())
        if self.max is not None:
            el.append(self.max.to_sdf())
        if self.radius is not None:
            el.append(self.radius.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sonar":
        _c_min = el.find("min")
        _min = Min.from_sdf(_c_min) if _c_min is not None else None
        _c_max = el.find("max")
        _max = Max.from_sdf(_c_max) if _c_max is not None else None
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius) if _c_radius is not None else None
        return cls(min=_min, max=_max, radius=_radius)


class Essid(Model):
    def __init__(self, essid: str = "wireless"):
        self.essid = essid

    def to_sdf(self) -> ET.Element:
        el = ET.Element("essid")
        if self.essid is not None:
            el.text = self.essid
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Essid":
        _text = el.text or "wireless"
        _essid = _text
        return cls(essid=_essid)


class Frequency(Model):
    def __init__(self, frequency: float = 2442):
        self.frequency = frequency

    def to_sdf(self) -> ET.Element:
        el = ET.Element("frequency")
        if self.frequency is not None:
            el.text = str(self.frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frequency":
        _text = el.text or 2442
        _frequency = _parse_double(_text)
        return cls(frequency=_frequency)


class MinFrequency(Model):
    def __init__(self, min_frequency: float = 2412):
        self.min_frequency = min_frequency

    def to_sdf(self) -> ET.Element:
        el = ET.Element("min_frequency")
        if self.min_frequency is not None:
            el.text = str(self.min_frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MinFrequency":
        _text = el.text or 2412
        _min_frequency = _parse_double(_text)
        return cls(min_frequency=_min_frequency)


class MaxFrequency(Model):
    def __init__(self, max_frequency: float = 2484):
        self.max_frequency = max_frequency

    def to_sdf(self) -> ET.Element:
        el = ET.Element("max_frequency")
        if self.max_frequency is not None:
            el.text = str(self.max_frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxFrequency":
        _text = el.text or 2484
        _max_frequency = _parse_double(_text)
        return cls(max_frequency=_max_frequency)


class Gain(Model):
    def __init__(self, gain: float = 2.5):
        self.gain = gain

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gain")
        if self.gain is not None:
            el.text = str(self.gain)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gain":
        _text = el.text or 2.5
        _gain = _parse_double(_text)
        return cls(gain=_gain)


class Power(Model):
    def __init__(self, power: float = 14.50):
        self.power = power

    def to_sdf(self) -> ET.Element:
        el = ET.Element("power")
        if self.power is not None:
            el.text = str(self.power)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Power":
        _text = el.text or 14.50
        _power = _parse_double(_text)
        return cls(power=_power)


class Sensitivity(Model):
    def __init__(self, sensitivity: float = -90):
        self.sensitivity = sensitivity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sensitivity")
        if self.sensitivity is not None:
            el.text = str(self.sensitivity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sensitivity":
        _text = el.text or -90
        _sensitivity = _parse_double(_text)
        return cls(sensitivity=_sensitivity)


class Transceiver(Model):
    def __init__(
            self,
            essid: "Essid" = None,
            frequency: "Frequency" = None,
            min_frequency: "MinFrequency" = None,
            max_frequency: "MaxFrequency" = None,
            gain: "Gain" = None,
            power: "Power" = None,
            sensitivity: "Sensitivity" = None
    ):
        self.essid = essid
        self.frequency = frequency
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.gain = gain
        self.power = power
        self.sensitivity = sensitivity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("transceiver")
        if self.essid is not None:
            el.append(self.essid.to_sdf())
        if self.frequency is not None:
            el.append(self.frequency.to_sdf())
        if self.min_frequency is not None:
            el.append(self.min_frequency.to_sdf())
        if self.max_frequency is not None:
            el.append(self.max_frequency.to_sdf())
        if self.gain is not None:
            el.append(self.gain.to_sdf())
        if self.power is not None:
            el.append(self.power.to_sdf())
        if self.sensitivity is not None:
            el.append(self.sensitivity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Transceiver":
        _c_essid = el.find("essid")
        _essid = Essid.from_sdf(_c_essid) if _c_essid is not None else None
        _c_frequency = el.find("frequency")
        _frequency = Frequency.from_sdf(_c_frequency) if _c_frequency is not None else None
        _c_min_frequency = el.find("min_frequency")
        _min_frequency = MinFrequency.from_sdf(_c_min_frequency) if _c_min_frequency is not None else None
        _c_max_frequency = el.find("max_frequency")
        _max_frequency = MaxFrequency.from_sdf(_c_max_frequency) if _c_max_frequency is not None else None
        _c_gain = el.find("gain")
        _gain = Gain.from_sdf(_c_gain) if _c_gain is not None else None
        _c_power = el.find("power")
        _power = Power.from_sdf(_c_power) if _c_power is not None else None
        _c_sensitivity = el.find("sensitivity")
        _sensitivity = Sensitivity.from_sdf(_c_sensitivity) if _c_sensitivity is not None else None
        return cls(essid=_essid, frequency=_frequency, min_frequency=_min_frequency, max_frequency=_max_frequency,
                   gain=_gain, power=_power, sensitivity=_sensitivity)


class AlwaysOn(Model):
    def __init__(self, always_on: bool = False):
        self.always_on = always_on

    def to_sdf(self) -> ET.Element:
        el = ET.Element("always_on")
        if self.always_on is not None:
            el.text = str(self.always_on).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AlwaysOn":
        _text = el.text or False
        _always_on = _text.strip().lower() == 'true'
        return cls(always_on=_always_on)


class UpdateRate(Model):
    def __init__(self, update_rate: float = 0):
        self.update_rate = update_rate

    def to_sdf(self) -> ET.Element:
        el = ET.Element("update_rate")
        if self.update_rate is not None:
            el.text = str(self.update_rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UpdateRate":
        _text = el.text or 0
        _update_rate = _parse_double(_text)
        return cls(update_rate=_update_rate)


class Visualize(Model):
    def __init__(self, visualize: bool = False):
        self.visualize = visualize

    def to_sdf(self) -> ET.Element:
        el = ET.Element("visualize")
        if self.visualize is not None:
            el.text = str(self.visualize).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visualize":
        _text = el.text or False
        _visualize = _text.strip().lower() == 'true'
        return cls(visualize=_visualize)


class Sensor(Model):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            plugin: List["Plugin"] = None,
            altimeter: "Altimeter" = None,
            camera: "Camera" = None,
            contact: "Contact" = None,
            force_torque: "ForceTorque" = None,
            gps: "Gps" = None,
            imu: "Imu" = None,
            logical_camera: "LogicalCamera" = None,
            magnetometer: "Magnetometer" = None,
            ray: "Ray" = None,
            rfidtag: "Rfidtag" = None,
            rfid: "Rfid" = None,
            sonar: "Sonar" = None,
            transceiver: "Transceiver" = None,
            always_on: "AlwaysOn" = None,
            update_rate: "UpdateRate" = None,
            visualize: "Visualize" = None,
            topic: "Topic" = None
    ):
        self.name = name
        self.type = type
        self.frame = frame or []
        self.pose = pose
        self.plugin = plugin or []
        self.altimeter = altimeter
        self.camera = camera
        self.contact = contact
        self.force_torque = force_torque
        self.gps = gps
        self.imu = imu
        self.logical_camera = logical_camera
        self.magnetometer = magnetometer
        self.ray = ray
        self.rfidtag = rfidtag
        self.rfid = rfid
        self.sonar = sonar
        self.transceiver = transceiver
        self.always_on = always_on
        self.update_rate = update_rate
        self.visualize = visualize
        self.topic = topic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sensor")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.altimeter is not None:
            el.append(self.altimeter.to_sdf())
        if self.camera is not None:
            el.append(self.camera.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        if self.force_torque is not None:
            el.append(self.force_torque.to_sdf())
        if self.gps is not None:
            el.append(self.gps.to_sdf())
        if self.imu is not None:
            el.append(self.imu.to_sdf())
        if self.logical_camera is not None:
            el.append(self.logical_camera.to_sdf())
        if self.magnetometer is not None:
            el.append(self.magnetometer.to_sdf())
        if self.ray is not None:
            el.append(self.ray.to_sdf())
        if self.rfidtag is not None:
            el.append(self.rfidtag.to_sdf())
        if self.rfid is not None:
            el.append(self.rfid.to_sdf())
        if self.sonar is not None:
            el.append(self.sonar.to_sdf())
        if self.transceiver is not None:
            el.append(self.transceiver.to_sdf())
        if self.always_on is not None:
            el.append(self.always_on.to_sdf())
        if self.update_rate is not None:
            el.append(self.update_rate.to_sdf())
        if self.visualize is not None:
            el.append(self.visualize.to_sdf())
        if self.topic is not None:
            el.append(self.topic.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sensor":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_altimeter = el.find("altimeter")
        _altimeter = Altimeter.from_sdf(_c_altimeter) if _c_altimeter is not None else None
        _c_camera = el.find("camera")
        _camera = Camera.from_sdf(_c_camera) if _c_camera is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        _c_force_torque = el.find("force_torque")
        _force_torque = ForceTorque.from_sdf(_c_force_torque) if _c_force_torque is not None else None
        _c_gps = el.find("gps")
        _gps = Gps.from_sdf(_c_gps) if _c_gps is not None else None
        _c_imu = el.find("imu")
        _imu = Imu.from_sdf(_c_imu) if _c_imu is not None else None
        _c_logical_camera = el.find("logical_camera")
        _logical_camera = LogicalCamera.from_sdf(_c_logical_camera) if _c_logical_camera is not None else None
        _c_magnetometer = el.find("magnetometer")
        _magnetometer = Magnetometer.from_sdf(_c_magnetometer) if _c_magnetometer is not None else None
        _c_ray = el.find("ray")
        _ray = Ray.from_sdf(_c_ray) if _c_ray is not None else None
        _c_rfidtag = el.find("rfidtag")
        _rfidtag = Rfidtag.from_sdf(_c_rfidtag) if _c_rfidtag is not None else None
        _c_rfid = el.find("rfid")
        _rfid = Rfid.from_sdf(_c_rfid) if _c_rfid is not None else None
        _c_sonar = el.find("sonar")
        _sonar = Sonar.from_sdf(_c_sonar) if _c_sonar is not None else None
        _c_transceiver = el.find("transceiver")
        _transceiver = Transceiver.from_sdf(_c_transceiver) if _c_transceiver is not None else None
        _c_always_on = el.find("always_on")
        _always_on = AlwaysOn.from_sdf(_c_always_on) if _c_always_on is not None else None
        _c_update_rate = el.find("update_rate")
        _update_rate = UpdateRate.from_sdf(_c_update_rate) if _c_update_rate is not None else None
        _c_visualize = el.find("visualize")
        _visualize = Visualize.from_sdf(_c_visualize) if _c_visualize is not None else None
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic) if _c_topic is not None else None
        return cls(name=_name, type=_type, frame=_frame, pose=_pose, plugin=_plugin, altimeter=_altimeter,
                   camera=_camera, contact=_contact, force_torque=_force_torque, gps=_gps, imu=_imu,
                   logical_camera=_logical_camera, magnetometer=_magnetometer, ray=_ray, rfidtag=_rfidtag, rfid=_rfid,
                   sonar=_sonar, transceiver=_transceiver, always_on=_always_on, update_rate=_update_rate,
                   visualize=_visualize, topic=_topic)


class Fov(Model):
    def __init__(self, fov: float = 0.785):
        self.fov = fov

    def to_sdf(self) -> ET.Element:
        el = ET.Element("fov")
        if self.fov is not None:
            el.text = str(self.fov)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fov":
        _text = el.text or 0.785
        _fov = _parse_double(_text)
        return cls(fov=_fov)


class NearClip(Model):
    def __init__(self, near_clip: float = 0.1):
        self.near_clip = near_clip

    def to_sdf(self) -> ET.Element:
        el = ET.Element("near_clip")
        if self.near_clip is not None:
            el.text = str(self.near_clip)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "NearClip":
        _text = el.text or 0.1
        _near_clip = _parse_double(_text)
        return cls(near_clip=_near_clip)


class FarClip(Model):
    def __init__(self, far_clip: float = 10.0):
        self.far_clip = far_clip

    def to_sdf(self) -> ET.Element:
        el = ET.Element("far_clip")
        if self.far_clip is not None:
            el.text = str(self.far_clip)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "FarClip":
        _text = el.text or 10.0
        _far_clip = _parse_double(_text)
        return cls(far_clip=_far_clip)


class Projector(Model):
    def __init__(
            self,
            name: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            plugin: List["Plugin"] = None,
            texture: "Texture" = None,
            fov: "Fov" = None,
            near_clip: "NearClip" = None,
            far_clip: "FarClip" = None
    ):
        self.name = name
        self.frame = frame or []
        self.pose = pose
        self.plugin = plugin or []
        self.texture = texture
        self.fov = fov
        self.near_clip = near_clip
        self.far_clip = far_clip

    def to_sdf(self) -> ET.Element:
        el = ET.Element("projector")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.texture is not None:
            el.append(self.texture.to_sdf())
        if self.fov is not None:
            el.append(self.fov.to_sdf())
        if self.near_clip is not None:
            el.append(self.near_clip.to_sdf())
        if self.far_clip is not None:
            el.append(self.far_clip.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Projector":
        _name = el.get("name", "__default__")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_texture = el.find("texture")
        _texture = Texture.from_sdf(_c_texture) if _c_texture is not None else None
        _c_fov = el.find("fov")
        _fov = Fov.from_sdf(_c_fov) if _c_fov is not None else None
        _c_near_clip = el.find("near_clip")
        _near_clip = NearClip.from_sdf(_c_near_clip) if _c_near_clip is not None else None
        _c_far_clip = el.find("far_clip")
        _far_clip = FarClip.from_sdf(_c_far_clip) if _c_far_clip is not None else None
        return cls(name=_name, frame=_frame, pose=_pose, plugin=_plugin, texture=_texture, fov=_fov,
                   near_clip=_near_clip, far_clip=_far_clip)


class Pitch(Model):
    def __init__(self, pitch: float = 1.0):
        self.pitch = pitch

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pitch")
        if self.pitch is not None:
            el.text = str(self.pitch)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pitch":
        _text = el.text or 1.0
        _pitch = _parse_double(_text)
        return cls(pitch=_pitch)


class Loop(Model):
    def __init__(self, loop: bool = False):
        self.loop = loop

    def to_sdf(self) -> ET.Element:
        el = ET.Element("loop")
        if self.loop is not None:
            el.text = str(self.loop).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Loop":
        _text = el.text or False
        _loop = _text.strip().lower() == 'true'
        return cls(loop=_loop)


class AudioSource(Model):
    def __init__(
            self,
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            uri: "Uri" = None,
            pitch: "Pitch" = None,
            gain: "Gain" = None,
            contact: "Contact" = None,
            loop: "Loop" = None
    ):
        self.frame = frame or []
        self.pose = pose
        self.uri = uri
        self.pitch = pitch
        self.gain = gain
        self.contact = contact
        self.loop = loop

    def to_sdf(self) -> ET.Element:
        el = ET.Element("audio_source")
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.uri is not None:
            el.append(self.uri.to_sdf())
        if self.pitch is not None:
            el.append(self.pitch.to_sdf())
        if self.gain is not None:
            el.append(self.gain.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        if self.loop is not None:
            el.append(self.loop.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AudioSource":
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri) if _c_uri is not None else None
        _c_pitch = el.find("pitch")
        _pitch = Pitch.from_sdf(_c_pitch) if _c_pitch is not None else None
        _c_gain = el.find("gain")
        _gain = Gain.from_sdf(_c_gain) if _c_gain is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        _c_loop = el.find("loop")
        _loop = Loop.from_sdf(_c_loop) if _c_loop is not None else None
        return cls(frame=_frame, pose=_pose, uri=_uri, pitch=_pitch, gain=_gain, contact=_contact, loop=_loop)


class Gravity(Model):
    def __init__(self, gravity: bool = True):
        self.gravity = gravity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gravity")
        if self.gravity is not None:
            el.text = str(self.gravity).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gravity":
        _text = el.text or True
        _gravity = _text.strip().lower() == 'true'
        return cls(gravity=_gravity)


class SelfCollide(Model):
    def __init__(self, self_collide: bool = False):
        self.self_collide = self_collide

    def to_sdf(self) -> ET.Element:
        el = ET.Element("self_collide")
        if self.self_collide is not None:
            el.text = str(self.self_collide).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SelfCollide":
        _text = el.text or False
        _self_collide = _text.strip().lower() == 'true'
        return cls(self_collide=_self_collide)


class Kinematic(Model):
    def __init__(self, kinematic: bool = False):
        self.kinematic = kinematic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("kinematic")
        if self.kinematic is not None:
            el.text = str(self.kinematic).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Kinematic":
        _text = el.text or False
        _kinematic = _text.strip().lower() == 'true'
        return cls(kinematic=_kinematic)


class MustBeBaseLink(Model):
    def __init__(self, must_be_base_link: bool = False):
        self.must_be_base_link = must_be_base_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("must_be_base_link")
        if self.must_be_base_link is not None:
            el.text = str(self.must_be_base_link).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MustBeBaseLink":
        _text = el.text or False
        _must_be_base_link = _text.strip().lower() == 'true'
        return cls(must_be_base_link=_must_be_base_link)


class Linear(Model):
    def __init__(self, linear: float = 0.0):
        self.linear = linear

    def to_sdf(self) -> ET.Element:
        el = ET.Element("linear")
        if self.linear is not None:
            el.text = str(self.linear)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Linear":
        _text = el.text or 0.0
        _linear = _parse_double(_text)
        return cls(linear=_linear)


class Angular(Model):
    def __init__(self, angular: float = 0.0):
        self.angular = angular

    def to_sdf(self) -> ET.Element:
        el = ET.Element("angular")
        if self.angular is not None:
            el.text = str(self.angular)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Angular":
        _text = el.text or 0.0
        _angular = _parse_double(_text)
        return cls(angular=_angular)


class VelocityDecay(Model):
    def __init__(self, linear: "Linear" = None, angular: "Angular" = None):
        self.linear = linear
        self.angular = angular

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity_decay")
        if self.linear is not None:
            el.append(self.linear.to_sdf())
        if self.angular is not None:
            el.append(self.angular.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VelocityDecay":
        _c_linear = el.find("linear")
        _linear = Linear.from_sdf(_c_linear) if _c_linear is not None else None
        _c_angular = el.find("angular")
        _angular = Angular.from_sdf(_c_angular) if _c_angular is not None else None
        return cls(linear=_linear, angular=_angular)


class Link(Model):
    def __init__(
            self,
            name: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            inertial: "Inertial" = None,
            collision: List["Collision"] = None,
            visual: List["Visual"] = None,
            sensor: List["Sensor"] = None,
            projector: List["Projector"] = None,
            audio_sink: List["AudioSink"] = None,
            audio_source: List["AudioSource"] = None,
            battery: List["Battery"] = None,
            gravity: "Gravity" = None,
            self_collide: "SelfCollide" = None,
            kinematic: "Kinematic" = None,
            must_be_base_link: "MustBeBaseLink" = None,
            velocity_decay: "VelocityDecay" = None
    ):
        self.name = name
        self.frame = frame or []
        self.pose = pose
        self.inertial = inertial
        self.collision = collision or []
        self.visual = visual or []
        self.sensor = sensor or []
        self.projector = projector or []
        self.audio_sink = audio_sink or []
        self.audio_source = audio_source or []
        self.battery = battery or []
        self.gravity = gravity
        self.self_collide = self_collide
        self.kinematic = kinematic
        self.must_be_base_link = must_be_base_link
        self.velocity_decay = velocity_decay

    def to_sdf(self) -> ET.Element:
        el = ET.Element("link")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.inertial is not None:
            el.append(self.inertial.to_sdf())
        for item in (self.collision or []):
            el.append(item.to_sdf())
        for item in (self.visual or []):
            el.append(item.to_sdf())
        for item in (self.sensor or []):
            el.append(item.to_sdf())
        for item in (self.projector or []):
            el.append(item.to_sdf())
        for item in (self.audio_sink or []):
            el.append(item.to_sdf())
        for item in (self.audio_source or []):
            el.append(item.to_sdf())
        for item in (self.battery or []):
            el.append(item.to_sdf())
        if self.gravity is not None:
            el.append(self.gravity.to_sdf())
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf())
        if self.kinematic is not None:
            el.append(self.kinematic.to_sdf())
        if self.must_be_base_link is not None:
            el.append(self.must_be_base_link.to_sdf())
        if self.velocity_decay is not None:
            el.append(self.velocity_decay.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Link":
        _name = el.get("name", "__default__")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_inertial = el.find("inertial")
        _inertial = Inertial.from_sdf(_c_inertial) if _c_inertial is not None else None
        _collision = [Collision.from_sdf(c) for c in el.findall("collision")]
        _visual = [Visual.from_sdf(c) for c in el.findall("visual")]
        _sensor = [Sensor.from_sdf(c) for c in el.findall("sensor")]
        _projector = [Projector.from_sdf(c) for c in el.findall("projector")]
        _audio_sink = [AudioSink.from_sdf(c) for c in el.findall("audio_sink")]
        _audio_source = [AudioSource.from_sdf(c) for c in el.findall("audio_source")]
        _battery = [Battery.from_sdf(c) for c in el.findall("battery")]
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_self_collide = el.find("self_collide")
        _self_collide = SelfCollide.from_sdf(_c_self_collide) if _c_self_collide is not None else None
        _c_kinematic = el.find("kinematic")
        _kinematic = Kinematic.from_sdf(_c_kinematic) if _c_kinematic is not None else None
        _c_must_be_base_link = el.find("must_be_base_link")
        _must_be_base_link = MustBeBaseLink.from_sdf(_c_must_be_base_link) if _c_must_be_base_link is not None else None
        _c_velocity_decay = el.find("velocity_decay")
        _velocity_decay = VelocityDecay.from_sdf(_c_velocity_decay) if _c_velocity_decay is not None else None
        return cls(name=_name, frame=_frame, pose=_pose, inertial=_inertial, collision=_collision, visual=_visual,
                   sensor=_sensor, projector=_projector, audio_sink=_audio_sink, audio_source=_audio_source,
                   battery=_battery, gravity=_gravity, self_collide=_self_collide, kinematic=_kinematic,
                   must_be_base_link=_must_be_base_link, velocity_decay=_velocity_decay)


class Parent(Model):
    def __init__(self, parent: str = "__default__"):
        self.parent = parent

    def to_sdf(self) -> ET.Element:
        el = ET.Element("parent")
        if self.parent is not None:
            el.text = self.parent
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Parent":
        _text = el.text or "__default__"
        _parent = _text
        return cls(parent=_parent)


class Child(Model):
    def __init__(self, child: str = "__default__"):
        self.child = child

    def to_sdf(self) -> ET.Element:
        el = ET.Element("child")
        if self.child is not None:
            el.text = self.child
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Child":
        _text = el.text or "__default__"
        _child = _text
        return cls(child=_child)


class GearboxRatio(Model):
    def __init__(self, gearbox_ratio: float = 1.0):
        self.gearbox_ratio = gearbox_ratio

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gearbox_ratio")
        if self.gearbox_ratio is not None:
            el.text = str(self.gearbox_ratio)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GearboxRatio":
        _text = el.text or 1.0
        _gearbox_ratio = _parse_double(_text)
        return cls(gearbox_ratio=_gearbox_ratio)


class GearboxReferenceBody(Model):
    def __init__(self, gearbox_reference_body: str = "__default__"):
        self.gearbox_reference_body = gearbox_reference_body

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gearbox_reference_body")
        if self.gearbox_reference_body is not None:
            el.text = self.gearbox_reference_body
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GearboxReferenceBody":
        _text = el.text or "__default__"
        _gearbox_reference_body = _text
        return cls(gearbox_reference_body=_gearbox_reference_body)


class ThreadPitch(Model):
    def __init__(self, thread_pitch: float = 1.0):
        self.thread_pitch = thread_pitch

    def to_sdf(self) -> ET.Element:
        el = ET.Element("thread_pitch")
        if self.thread_pitch is not None:
            el.text = str(self.thread_pitch)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ThreadPitch":
        _text = el.text or 1.0
        _thread_pitch = _parse_double(_text)
        return cls(thread_pitch=_thread_pitch)


class Xyz(Model):
    def __init__(self, xyz: Vector3 = None):
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz

    def to_sdf(self) -> ET.Element:
        el = ET.Element("xyz")
        if self.xyz is not None:
            el.text = self.xyz.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Xyz":
        _text = el.text or "0 0 1"
        _xyz = Vector3.from_sdf(_text)
        return cls(xyz=_xyz)


class Dynamics(Model):
    def __init__(
            self,
            damping: "Damping" = None,
            friction: "Friction" = None,
            spring_reference: "SpringReference" = None,
            spring_stiffness: "SpringStiffness" = None
    ):
        self.damping = damping
        self.friction = friction
        self.spring_reference = spring_reference
        self.spring_stiffness = spring_stiffness

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dynamics")
        if self.damping is not None:
            el.append(self.damping.to_sdf())
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        if self.spring_reference is not None:
            el.append(self.spring_reference.to_sdf())
        if self.spring_stiffness is not None:
            el.append(self.spring_stiffness.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dynamics":
        _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping) if _c_damping is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        _c_spring_reference = el.find("spring_reference")
        _spring_reference = SpringReference.from_sdf(_c_spring_reference) if _c_spring_reference is not None else None
        _c_spring_stiffness = el.find("spring_stiffness")
        _spring_stiffness = SpringStiffness.from_sdf(_c_spring_stiffness) if _c_spring_stiffness is not None else None
        return cls(damping=_damping, friction=_friction, spring_reference=_spring_reference,
                   spring_stiffness=_spring_stiffness)


class Lower(Model):
    def __init__(self, lower: float = -1e16):
        self.lower = lower

    def to_sdf(self) -> ET.Element:
        el = ET.Element("lower")
        if self.lower is not None:
            el.text = str(self.lower)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Lower":
        _text = el.text or -1e16
        _lower = _parse_double(_text)
        return cls(lower=_lower)


class Upper(Model):
    def __init__(self, upper: float = 1e16):
        self.upper = upper

    def to_sdf(self) -> ET.Element:
        el = ET.Element("upper")
        if self.upper is not None:
            el.text = str(self.upper)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Upper":
        _text = el.text or 1e16
        _upper = _parse_double(_text)
        return cls(upper=_upper)


class Effort(Model):
    def __init__(self, effort: float = -1):
        self.effort = effort

    def to_sdf(self) -> ET.Element:
        el = ET.Element("effort")
        if self.effort is not None:
            el.text = str(self.effort)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Effort":
        _text = el.text or -1
        _effort = _parse_double(_text)
        return cls(effort=_effort)


class Velocity(Model):
    def __init__(self, velocity: float = -1):
        self.velocity = velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = str(self.velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Velocity":
        _text = el.text or -1
        _velocity = _parse_double(_text)
        return cls(velocity=_velocity)


class Dissipation(Model):
    def __init__(self, dissipation: float = 1.0):
        self.dissipation = dissipation

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dissipation")
        if self.dissipation is not None:
            el.text = str(self.dissipation)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dissipation":
        _text = el.text or 1.0
        _dissipation = _parse_double(_text)
        return cls(dissipation=_dissipation)


class Limit(Model):
    def __init__(
            self,
            lower: "Lower" = None,
            upper: "Upper" = None,
            effort: "Effort" = None,
            velocity: "Velocity" = None,
            stiffness: "Stiffness" = None,
            dissipation: "Dissipation" = None
    ):
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity
        self.stiffness = stiffness
        self.dissipation = dissipation

    def to_sdf(self) -> ET.Element:
        el = ET.Element("limit")
        if self.lower is not None:
            el.append(self.lower.to_sdf())
        if self.upper is not None:
            el.append(self.upper.to_sdf())
        if self.effort is not None:
            el.append(self.effort.to_sdf())
        if self.velocity is not None:
            el.append(self.velocity.to_sdf())
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf())
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Limit":
        _c_lower = el.find("lower")
        _lower = Lower.from_sdf(_c_lower) if _c_lower is not None else None
        _c_upper = el.find("upper")
        _upper = Upper.from_sdf(_c_upper) if _c_upper is not None else None
        _c_effort = el.find("effort")
        _effort = Effort.from_sdf(_c_effort) if _c_effort is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity) if _c_velocity is not None else None
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness) if _c_stiffness is not None else None
        _c_dissipation = el.find("dissipation")
        _dissipation = Dissipation.from_sdf(_c_dissipation) if _c_dissipation is not None else None
        return cls(lower=_lower, upper=_upper, effort=_effort, velocity=_velocity, stiffness=_stiffness,
                   dissipation=_dissipation)


class Axis(Model):
    def __init__(
            self,
            xyz: "Xyz" = None,
            use_parent_model_frame: "UseParentModelFrame" = None,
            dynamics: "Dynamics" = None,
            limit: "Limit" = None
    ):
        self.xyz = xyz
        self.use_parent_model_frame = use_parent_model_frame
        self.dynamics = dynamics
        self.limit = limit

    def to_sdf(self) -> ET.Element:
        el = ET.Element("axis")
        if self.xyz is not None:
            el.append(self.xyz.to_sdf())
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf())
        if self.limit is not None:
            el.append(self.limit.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis":
        _c_xyz = el.find("xyz")
        _xyz = Xyz.from_sdf(_c_xyz) if _c_xyz is not None else None
        _c_use_parent_model_frame = el.find("use_parent_model_frame")
        _use_parent_model_frame = UseParentModelFrame.from_sdf(
            _c_use_parent_model_frame) if _c_use_parent_model_frame is not None else None
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit) if _c_limit is not None else None
        return cls(xyz=_xyz, use_parent_model_frame=_use_parent_model_frame, dynamics=_dynamics, limit=_limit)


class Axis2(Model):
    def __init__(
            self,
            xyz: "Xyz" = None,
            use_parent_model_frame: "UseParentModelFrame" = None,
            dynamics: "Dynamics" = None,
            limit: "Limit" = None
    ):
        self.xyz = xyz
        self.use_parent_model_frame = use_parent_model_frame
        self.dynamics = dynamics
        self.limit = limit

    def to_sdf(self) -> ET.Element:
        el = ET.Element("axis2")
        if self.xyz is not None:
            el.append(self.xyz.to_sdf())
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf())
        if self.limit is not None:
            el.append(self.limit.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis2":
        _c_xyz = el.find("xyz")
        _xyz = Xyz.from_sdf(_c_xyz) if _c_xyz is not None else None
        _c_use_parent_model_frame = el.find("use_parent_model_frame")
        _use_parent_model_frame = UseParentModelFrame.from_sdf(
            _c_use_parent_model_frame) if _c_use_parent_model_frame is not None else None
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit) if _c_limit is not None else None
        return cls(xyz=_xyz, use_parent_model_frame=_use_parent_model_frame, dynamics=_dynamics, limit=_limit)


class MustBeLoopJoint(Model):
    def __init__(self, must_be_loop_joint: bool = False):
        self.must_be_loop_joint = must_be_loop_joint

    def to_sdf(self) -> ET.Element:
        el = ET.Element("must_be_loop_joint")
        if self.must_be_loop_joint is not None:
            el.text = str(self.must_be_loop_joint).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MustBeLoopJoint":
        _text = el.text or False
        _must_be_loop_joint = _text.strip().lower() == 'true'
        return cls(must_be_loop_joint=_must_be_loop_joint)


class Simbody(Model):
    def __init__(self, must_be_loop_joint: "MustBeLoopJoint" = None):
        self.must_be_loop_joint = must_be_loop_joint

    def to_sdf(self) -> ET.Element:
        el = ET.Element("simbody")
        if self.must_be_loop_joint is not None:
            el.append(self.must_be_loop_joint.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Simbody":
        _c_must_be_loop_joint = el.find("must_be_loop_joint")
        _must_be_loop_joint = MustBeLoopJoint.from_sdf(
            _c_must_be_loop_joint) if _c_must_be_loop_joint is not None else None
        return cls(must_be_loop_joint=_must_be_loop_joint)


class ProvideFeedback(Model):
    def __init__(self, provide_feedback: bool = False):
        self.provide_feedback = provide_feedback

    def to_sdf(self) -> ET.Element:
        el = ET.Element("provide_feedback")
        if self.provide_feedback is not None:
            el.text = str(self.provide_feedback).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ProvideFeedback":
        _text = el.text or False
        _provide_feedback = _text.strip().lower() == 'true'
        return cls(provide_feedback=_provide_feedback)


class Physics(Model):
    def __init__(
            self,
            simbody: "Simbody" = None,
            ode: "Ode" = None,
            provide_feedback: "ProvideFeedback" = None
    ):
        self.simbody = simbody
        self.ode = ode
        self.provide_feedback = provide_feedback

    def to_sdf(self) -> ET.Element:
        el = ET.Element("physics")
        if self.simbody is not None:
            el.append(self.simbody.to_sdf())
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        if self.provide_feedback is not None:
            el.append(self.provide_feedback.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Physics":
        _c_simbody = el.find("simbody")
        _simbody = Simbody.from_sdf(_c_simbody) if _c_simbody is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        _c_provide_feedback = el.find("provide_feedback")
        _provide_feedback = ProvideFeedback.from_sdf(_c_provide_feedback) if _c_provide_feedback is not None else None
        return cls(simbody=_simbody, ode=_ode, provide_feedback=_provide_feedback)


class Joint(Model):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            sensor: List["Sensor"] = None,
            parent: "Parent" = None,
            child: "Child" = None,
            gearbox_ratio: "GearboxRatio" = None,
            gearbox_reference_body: "GearboxReferenceBody" = None,
            thread_pitch: "ThreadPitch" = None,
            axis: "Axis" = None,
            axis2: "Axis2" = None,
            physics: "Physics" = None
    ):
        self.name = name
        self.type = type
        self.frame = frame or []
        self.pose = pose
        self.sensor = sensor or []
        self.parent = parent
        self.child = child
        self.gearbox_ratio = gearbox_ratio
        self.gearbox_reference_body = gearbox_reference_body
        self.thread_pitch = thread_pitch
        self.axis = axis
        self.axis2 = axis2
        self.physics = physics

    def to_sdf(self) -> ET.Element:
        el = ET.Element("joint")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        for item in (self.sensor or []):
            el.append(item.to_sdf())
        if self.parent is not None:
            el.append(self.parent.to_sdf())
        if self.child is not None:
            el.append(self.child.to_sdf())
        if self.gearbox_ratio is not None:
            el.append(self.gearbox_ratio.to_sdf())
        if self.gearbox_reference_body is not None:
            el.append(self.gearbox_reference_body.to_sdf())
        if self.thread_pitch is not None:
            el.append(self.thread_pitch.to_sdf())
        if self.axis is not None:
            el.append(self.axis.to_sdf())
        if self.axis2 is not None:
            el.append(self.axis2.to_sdf())
        if self.physics is not None:
            el.append(self.physics.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Joint":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _sensor = [Sensor.from_sdf(c) for c in el.findall("sensor")]
        _c_parent = el.find("parent")
        _parent = Parent.from_sdf(_c_parent) if _c_parent is not None else None
        _c_child = el.find("child")
        _child = Child.from_sdf(_c_child) if _c_child is not None else None
        _c_gearbox_ratio = el.find("gearbox_ratio")
        _gearbox_ratio = GearboxRatio.from_sdf(_c_gearbox_ratio) if _c_gearbox_ratio is not None else None
        _c_gearbox_reference_body = el.find("gearbox_reference_body")
        _gearbox_reference_body = GearboxReferenceBody.from_sdf(
            _c_gearbox_reference_body) if _c_gearbox_reference_body is not None else None
        _c_thread_pitch = el.find("thread_pitch")
        _thread_pitch = ThreadPitch.from_sdf(_c_thread_pitch) if _c_thread_pitch is not None else None
        _c_axis = el.find("axis")
        _axis = Axis.from_sdf(_c_axis) if _c_axis is not None else None
        _c_axis2 = el.find("axis2")
        _axis2 = Axis2.from_sdf(_c_axis2) if _c_axis2 is not None else None
        _c_physics = el.find("physics")
        _physics = Physics.from_sdf(_c_physics) if _c_physics is not None else None
        return cls(name=_name, type=_type, frame=_frame, pose=_pose, sensor=_sensor, parent=_parent, child=_child,
                   gearbox_ratio=_gearbox_ratio, gearbox_reference_body=_gearbox_reference_body,
                   thread_pitch=_thread_pitch, axis=_axis, axis2=_axis2, physics=_physics)


class DetachSteps(Model):
    def __init__(self, detach_steps: int = 40):
        self.detach_steps = detach_steps

    def to_sdf(self) -> ET.Element:
        el = ET.Element("detach_steps")
        if self.detach_steps is not None:
            el.text = str(self.detach_steps)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DetachSteps":
        _text = el.text or 40
        _detach_steps = _parse_int32(_text)
        return cls(detach_steps=_detach_steps)


class AttachSteps(Model):
    def __init__(self, attach_steps: int = 20):
        self.attach_steps = attach_steps

    def to_sdf(self) -> ET.Element:
        el = ET.Element("attach_steps")
        if self.attach_steps is not None:
            el.text = str(self.attach_steps)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AttachSteps":
        _text = el.text or 20
        _attach_steps = _parse_int32(_text)
        return cls(attach_steps=_attach_steps)


class MinContactCount(Model):
    def __init__(self, min_contact_count: int = 2):
        self.min_contact_count = min_contact_count

    def to_sdf(self) -> ET.Element:
        el = ET.Element("min_contact_count")
        if self.min_contact_count is not None:
            el.text = str(self.min_contact_count)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MinContactCount":
        _text = el.text or 2
        _min_contact_count = _parse_uint32(_text)
        return cls(min_contact_count=_min_contact_count)


class GraspCheck(Model):
    def __init__(
            self,
            detach_steps: "DetachSteps" = None,
            attach_steps: "AttachSteps" = None,
            min_contact_count: "MinContactCount" = None
    ):
        self.detach_steps = detach_steps
        self.attach_steps = attach_steps
        self.min_contact_count = min_contact_count

    def to_sdf(self) -> ET.Element:
        el = ET.Element("grasp_check")
        if self.detach_steps is not None:
            el.append(self.detach_steps.to_sdf())
        if self.attach_steps is not None:
            el.append(self.attach_steps.to_sdf())
        if self.min_contact_count is not None:
            el.append(self.min_contact_count.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GraspCheck":
        _c_detach_steps = el.find("detach_steps")
        _detach_steps = DetachSteps.from_sdf(_c_detach_steps) if _c_detach_steps is not None else None
        _c_attach_steps = el.find("attach_steps")
        _attach_steps = AttachSteps.from_sdf(_c_attach_steps) if _c_attach_steps is not None else None
        _c_min_contact_count = el.find("min_contact_count")
        _min_contact_count = MinContactCount.from_sdf(
            _c_min_contact_count) if _c_min_contact_count is not None else None
        return cls(detach_steps=_detach_steps, attach_steps=_attach_steps, min_contact_count=_min_contact_count)


class GripperLink(Model):
    def __init__(self, gripper_link: str = "__default__"):
        self.gripper_link = gripper_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gripper_link")
        if self.gripper_link is not None:
            el.text = self.gripper_link
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "GripperLink":
        _text = el.text or "__default__"
        _gripper_link = _text
        return cls(gripper_link=_gripper_link)


class PalmLink(Model):
    def __init__(self, palm_link: str = "__default__"):
        self.palm_link = palm_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("palm_link")
        if self.palm_link is not None:
            el.text = self.palm_link
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PalmLink":
        _text = el.text or "__default__"
        _palm_link = _text
        return cls(palm_link=_palm_link)


class Gripper(Model):
    def __init__(
            self,
            name: str = "__default__",
            grasp_check: "GraspCheck" = None,
            gripper_link: List["GripperLink"] = None,
            palm_link: "PalmLink" = None
    ):
        self.name = name
        self.grasp_check = grasp_check
        self.gripper_link = gripper_link or []
        self.palm_link = palm_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gripper")
        if self.name is not None:
            el.set("name", self.name)
        if self.grasp_check is not None:
            el.append(self.grasp_check.to_sdf())
        for item in (self.gripper_link or []):
            el.append(item.to_sdf())
        if self.palm_link is not None:
            el.append(self.palm_link.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gripper":
        _name = el.get("name", "__default__")
        _c_grasp_check = el.find("grasp_check")
        _grasp_check = GraspCheck.from_sdf(_c_grasp_check) if _c_grasp_check is not None else None
        _gripper_link = [GripperLink.from_sdf(c) for c in el.findall("gripper_link")]
        _c_palm_link = el.find("palm_link")
        _palm_link = PalmLink.from_sdf(_c_palm_link) if _c_palm_link is not None else None
        return cls(name=_name, grasp_check=_grasp_check, gripper_link=_gripper_link, palm_link=_palm_link)


class Static(Model):
    def __init__(self, static: bool = False):
        self.static = static

    def to_sdf(self) -> ET.Element:
        el = ET.Element("static")
        if self.static is not None:
            el.text = str(self.static).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Static":
        _text = el.text or False
        _static = _text.strip().lower() == 'true'
        return cls(static=_static)


class AllowAutoDisable(Model):
    def __init__(self, allow_auto_disable: bool = True):
        self.allow_auto_disable = allow_auto_disable

    def to_sdf(self) -> ET.Element:
        el = ET.Element("allow_auto_disable")
        if self.allow_auto_disable is not None:
            el.text = str(self.allow_auto_disable).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AllowAutoDisable":
        _text = el.text or True
        _allow_auto_disable = _text.strip().lower() == 'true'
        return cls(allow_auto_disable=_allow_auto_disable)


class Model(Model):
    def __init__(
            self,
            name: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            link: List["Link"] = None,
            joint: List["Joint"] = None,
            plugin: List["Plugin"] = None,
            gripper: List["Gripper"] = None,
            static: "Static" = None,
            self_collide: "SelfCollide" = None,
            allow_auto_disable: "AllowAutoDisable" = None,
            include: List["Include"] = None,
            model: List["Model"] = None
    ):
        self.name = name
        self.frame = frame or []
        self.pose = pose
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.gripper = gripper or []
        self.static = static
        self.self_collide = self_collide
        self.allow_auto_disable = allow_auto_disable
        self.include = include or []
        self.model = model or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("model")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        for item in (self.link or []):
            el.append(item.to_sdf())
        for item in (self.joint or []):
            el.append(item.to_sdf())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        for item in (self.gripper or []):
            el.append(item.to_sdf())
        if self.static is not None:
            el.append(self.static.to_sdf())
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf())
        if self.allow_auto_disable is not None:
            el.append(self.allow_auto_disable.to_sdf())
        for item in (self.include or []):
            el.append(item.to_sdf())
        for item in (self.model or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        _name = el.get("name", "__default__")
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _link = [Link.from_sdf(c) for c in el.findall("link")]
        _joint = [Joint.from_sdf(c) for c in el.findall("joint")]
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _gripper = [Gripper.from_sdf(c) for c in el.findall("gripper")]
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static) if _c_static is not None else None
        _c_self_collide = el.find("self_collide")
        _self_collide = SelfCollide.from_sdf(_c_self_collide) if _c_self_collide is not None else None
        _c_allow_auto_disable = el.find("allow_auto_disable")
        _allow_auto_disable = AllowAutoDisable.from_sdf(
            _c_allow_auto_disable) if _c_allow_auto_disable is not None else None
        _include = [Include.from_sdf(c) for c in el.findall("include")]
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        return cls(name=_name, frame=_frame, pose=_pose, link=_link, joint=_joint, plugin=_plugin, gripper=_gripper,
                   static=_static, self_collide=_self_collide, allow_auto_disable=_allow_auto_disable, include=_include,
                   model=_model)
