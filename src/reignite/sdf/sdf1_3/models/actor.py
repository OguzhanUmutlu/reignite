from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from ..model import Model
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


class Pose(Model):
    def __init__(self, pose: Pose = None):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        return cls(pose=_pose)


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
    def __init__(self, mass: "Mass" = None, pose: "Pose" = None, inertia: "Inertia" = None):
        self.mass = mass
        self.pose = pose
        self.inertia = inertia

    def to_sdf(self) -> ET.Element:
        el = ET.Element("inertial")
        if self.mass is not None:
            el.append(self.mass.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.inertia is not None:
            el.append(self.inertia.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Inertial":
        _c_mass = el.find("mass")
        _mass = Mass.from_sdf(_c_mass) if _c_mass is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_inertia = el.find("inertia")
        _inertia = Inertia.from_sdf(_c_inertia) if _c_inertia is not None else None
        return cls(mass=_mass, pose=_pose, inertia=_inertia)


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


class Scale(Model):
    def __init__(self, scale: Vector3 = None):
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        self.scale = scale

    def to_sdf(self) -> ET.Element:
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = self.scale.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scale":
        _text = el.text or "1 1 1"
        _scale = Vector3.from_sdf(_text)
        return cls(scale=_scale)


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


class Normal(Model):
    def __init__(self, normal: Vector3 = None):
        if normal is None:
            normal = Vector3.from_sdf("0 0 1")
        self.normal = normal

    def to_sdf(self) -> ET.Element:
        el = ET.Element("normal")
        if self.normal is not None:
            el.text = self.normal.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Normal":
        _text = el.text or "0 0 1"
        _normal = Vector3.from_sdf(_text)
        return cls(normal=_normal)


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
    def __init__(self, diffuse: Color = None):
        if diffuse is None:
            diffuse = Color.from_sdf("1 1 1 1")
        self.diffuse = diffuse

    def to_sdf(self) -> ET.Element:
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _text = el.text or "1 1 1 1"
        _diffuse = Color.from_sdf(_text)
        return cls(diffuse=_diffuse)


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


class Heightmap(Model):
    def __init__(
            self,
            uri: "Uri" = None,
            size: "Size" = None,
            pos: "Pos" = None,
            texture: List["Texture"] = None,
            blend: List["Blend"] = None
    ):
        self.uri = uri
        self.size = size
        self.pos = pos
        self.texture = texture or []
        self.blend = blend or []

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
        return cls(uri=_uri, size=_size, pos=_pos, texture=_texture, blend=_blend)


class Geometry(Model):
    def __init__(
            self,
            box: "Box" = None,
            sphere: "Sphere" = None,
            cylinder: "Cylinder" = None,
            mesh: "Mesh" = None,
            plane: "Plane" = None,
            image: "Image" = None,
            heightmap: "Heightmap" = None,
            empty: "Empty" = None
    ):
        self.box = box
        self.sphere = sphere
        self.cylinder = cylinder
        self.mesh = mesh
        self.plane = plane
        self.image = image
        self.heightmap = heightmap
        self.empty = empty

    def to_sdf(self) -> ET.Element:
        el = ET.Element("geometry")
        if self.box is not None:
            el.append(self.box.to_sdf())
        if self.sphere is not None:
            el.append(self.sphere.to_sdf())
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf())
        if self.mesh is not None:
            el.append(self.mesh.to_sdf())
        if self.plane is not None:
            el.append(self.plane.to_sdf())
        if self.image is not None:
            el.append(self.image.to_sdf())
        if self.heightmap is not None:
            el.append(self.heightmap.to_sdf())
        if self.empty is not None:
            el.append(self.empty.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Geometry":
        _c_box = el.find("box")
        _box = Box.from_sdf(_c_box) if _c_box is not None else None
        _c_sphere = el.find("sphere")
        _sphere = Sphere.from_sdf(_c_sphere) if _c_sphere is not None else None
        _c_cylinder = el.find("cylinder")
        _cylinder = Cylinder.from_sdf(_c_cylinder) if _c_cylinder is not None else None
        _c_mesh = el.find("mesh")
        _mesh = Mesh.from_sdf(_c_mesh) if _c_mesh is not None else None
        _c_plane = el.find("plane")
        _plane = Plane.from_sdf(_c_plane) if _c_plane is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image) if _c_image is not None else None
        _c_heightmap = el.find("heightmap")
        _heightmap = Heightmap.from_sdf(_c_heightmap) if _c_heightmap is not None else None
        _c_empty = el.find("empty")
        _empty = Empty.from_sdf(_c_empty) if _c_empty is not None else None
        return cls(box=_box, sphere=_sphere, cylinder=_cylinder, mesh=_mesh, plane=_plane, image=_image,
                   heightmap=_heightmap, empty=_empty)


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


class Type(Model):
    def __init__(self, type: str = "quick"):
        self.type = type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _text = el.text or "quick"
        _type = _text
        return cls(type=_type)


class Dt(Model):
    def __init__(self, dt: float = 0.001):
        self.dt = dt

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dt")
        if self.dt is not None:
            el.text = str(self.dt)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dt":
        _text = el.text or 0.001
        _dt = _parse_double(_text)
        return cls(dt=_dt)


class Iters(Model):
    def __init__(self, iters: int = 50):
        self.iters = iters

    def to_sdf(self) -> ET.Element:
        el = ET.Element("iters")
        if self.iters is not None:
            el.text = str(self.iters)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Iters":
        _text = el.text or 50
        _iters = _parse_int32(_text)
        return cls(iters=_iters)


class PreconIters(Model):
    def __init__(self, precon_iters: int = 0):
        self.precon_iters = precon_iters

    def to_sdf(self) -> ET.Element:
        el = ET.Element("precon_iters")
        if self.precon_iters is not None:
            el.text = str(self.precon_iters)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PreconIters":
        _text = el.text or 0
        _precon_iters = _parse_int32(_text)
        return cls(precon_iters=_precon_iters)


class Sor(Model):
    def __init__(self, sor: float = 1.3):
        self.sor = sor

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sor")
        if self.sor is not None:
            el.text = str(self.sor)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sor":
        _text = el.text or 1.3
        _sor = _parse_double(_text)
        return cls(sor=_sor)


class Solver(Model):
    def __init__(
            self,
            type: "Type" = None,
            dt: "Dt" = None,
            iters: "Iters" = None,
            precon_iters: "PreconIters" = None,
            sor: "Sor" = None
    ):
        self.type = type
        self.dt = dt
        self.iters = iters
        self.precon_iters = precon_iters
        self.sor = sor

    def to_sdf(self) -> ET.Element:
        el = ET.Element("solver")
        if self.type is not None:
            el.append(self.type.to_sdf())
        if self.dt is not None:
            el.append(self.dt.to_sdf())
        if self.iters is not None:
            el.append(self.iters.to_sdf())
        if self.precon_iters is not None:
            el.append(self.precon_iters.to_sdf())
        if self.sor is not None:
            el.append(self.sor.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Solver":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type) if _c_type is not None else None
        _c_dt = el.find("dt")
        _dt = Dt.from_sdf(_c_dt) if _c_dt is not None else None
        _c_iters = el.find("iters")
        _iters = Iters.from_sdf(_c_iters) if _c_iters is not None else None
        _c_precon_iters = el.find("precon_iters")
        _precon_iters = PreconIters.from_sdf(_c_precon_iters) if _c_precon_iters is not None else None
        _c_sor = el.find("sor")
        _sor = Sor.from_sdf(_c_sor) if _c_sor is not None else None
        return cls(type=_type, dt=_dt, iters=_iters, precon_iters=_precon_iters, sor=_sor)


class Cfm(Model):
    def __init__(self, cfm: float = 0):
        self.cfm = cfm

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cfm")
        if self.cfm is not None:
            el.text = str(self.cfm)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Cfm":
        _text = el.text or 0
        _cfm = _parse_double(_text)
        return cls(cfm=_cfm)


class Erp(Model):
    def __init__(self, erp: float = 0.2):
        self.erp = erp

    def to_sdf(self) -> ET.Element:
        el = ET.Element("erp")
        if self.erp is not None:
            el.text = str(self.erp)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Erp":
        _text = el.text or 0.2
        _erp = _parse_double(_text)
        return cls(erp=_erp)


class ContactMaxCorrectingVel(Model):
    def __init__(self, contact_max_correcting_vel: float = 100.0):
        self.contact_max_correcting_vel = contact_max_correcting_vel

    def to_sdf(self) -> ET.Element:
        el = ET.Element("contact_max_correcting_vel")
        if self.contact_max_correcting_vel is not None:
            el.text = str(self.contact_max_correcting_vel)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ContactMaxCorrectingVel":
        _text = el.text or 100.0
        _contact_max_correcting_vel = _parse_double(_text)
        return cls(contact_max_correcting_vel=_contact_max_correcting_vel)


class ContactSurfaceLayer(Model):
    def __init__(self, contact_surface_layer: float = 0.001):
        self.contact_surface_layer = contact_surface_layer

    def to_sdf(self) -> ET.Element:
        el = ET.Element("contact_surface_layer")
        if self.contact_surface_layer is not None:
            el.text = str(self.contact_surface_layer)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ContactSurfaceLayer":
        _text = el.text or 0.001
        _contact_surface_layer = _parse_double(_text)
        return cls(contact_surface_layer=_contact_surface_layer)


class Constraints(Model):
    def __init__(
            self,
            cfm: "Cfm" = None,
            erp: "Erp" = None,
            contact_max_correcting_vel: "ContactMaxCorrectingVel" = None,
            contact_surface_layer: "ContactSurfaceLayer" = None
    ):
        self.cfm = cfm
        self.erp = erp
        self.contact_max_correcting_vel = contact_max_correcting_vel
        self.contact_surface_layer = contact_surface_layer

    def to_sdf(self) -> ET.Element:
        el = ET.Element("constraints")
        if self.cfm is not None:
            el.append(self.cfm.to_sdf())
        if self.erp is not None:
            el.append(self.erp.to_sdf())
        if self.contact_max_correcting_vel is not None:
            el.append(self.contact_max_correcting_vel.to_sdf())
        if self.contact_surface_layer is not None:
            el.append(self.contact_surface_layer.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Constraints":
        _c_cfm = el.find("cfm")
        _cfm = Cfm.from_sdf(_c_cfm) if _c_cfm is not None else None
        _c_erp = el.find("erp")
        _erp = Erp.from_sdf(_c_erp) if _c_erp is not None else None
        _c_contact_max_correcting_vel = el.find("contact_max_correcting_vel")
        _contact_max_correcting_vel = ContactMaxCorrectingVel.from_sdf(
            _c_contact_max_correcting_vel) if _c_contact_max_correcting_vel is not None else None
        _c_contact_surface_layer = el.find("contact_surface_layer")
        _contact_surface_layer = ContactSurfaceLayer.from_sdf(
            _c_contact_surface_layer) if _c_contact_surface_layer is not None else None
        return cls(cfm=_cfm, erp=_erp, contact_max_correcting_vel=_contact_max_correcting_vel,
                   contact_surface_layer=_contact_surface_layer)


class Ode(Model):
    def __init__(self, solver: "Solver" = None, constraints: "Constraints" = None):
        self.solver = solver
        self.constraints = constraints

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ode")
        if self.solver is not None:
            el.append(self.solver.to_sdf())
        if self.constraints is not None:
            el.append(self.constraints.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver) if _c_solver is not None else None
        _c_constraints = el.find("constraints")
        _constraints = Constraints.from_sdf(_c_constraints) if _c_constraints is not None else None
        return cls(solver=_solver, constraints=_constraints)


class Friction(Model):
    def __init__(self, ode: "Ode" = None):
        self.ode = ode

    def to_sdf(self) -> ET.Element:
        el = ET.Element("friction")
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Friction":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(ode=_ode)


class Contact(Model):
    def __init__(self, ode: "Ode" = None):
        self.ode = ode

    def to_sdf(self) -> ET.Element:
        el = ET.Element("contact")
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Contact":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(ode=_ode)


class Surface(Model):
    def __init__(
            self,
            bounce: "Bounce" = None,
            friction: "Friction" = None,
            contact: "Contact" = None
    ):
        self.bounce = bounce
        self.friction = friction
        self.contact = contact

    def to_sdf(self) -> ET.Element:
        el = ET.Element("surface")
        if self.bounce is not None:
            el.append(self.bounce.to_sdf())
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Surface":
        _c_bounce = el.find("bounce")
        _bounce = Bounce.from_sdf(_c_bounce) if _c_bounce is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        return cls(bounce=_bounce, friction=_friction, contact=_contact)


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
    def __init__(self, max_contacts: int = 20):
        self.max_contacts = max_contacts

    def to_sdf(self) -> ET.Element:
        el = ET.Element("max_contacts")
        if self.max_contacts is not None:
            el.text = str(self.max_contacts)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxContacts":
        _text = el.text or 20
        _max_contacts = _parse_int32(_text)
        return cls(max_contacts=_max_contacts)


class Collision(Model):
    def __init__(
            self,
            name: str = "__default__",
            geometry: "Geometry" = None,
            surface: "Surface" = None,
            laser_retro: "LaserRetro" = None,
            max_contacts: "MaxContacts" = None,
            pose: "Pose" = None
    ):
        self.name = name
        self.geometry = geometry
        self.surface = surface
        self.laser_retro = laser_retro
        self.max_contacts = max_contacts
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collision")
        if self.name is not None:
            el.set("name", self.name)
        if self.geometry is not None:
            el.append(self.geometry.to_sdf())
        if self.surface is not None:
            el.append(self.surface.to_sdf())
        if self.laser_retro is not None:
            el.append(self.laser_retro.to_sdf())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Collision":
        _name = el.get("name", "__default__")
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry) if _c_geometry is not None else None
        _c_surface = el.find("surface")
        _surface = Surface.from_sdf(_c_surface) if _c_surface is not None else None
        _c_laser_retro = el.find("laser_retro")
        _laser_retro = LaserRetro.from_sdf(_c_laser_retro) if _c_laser_retro is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_name, geometry=_geometry, surface=_surface, laser_retro=_laser_retro,
                   max_contacts=_max_contacts, pose=_pose)


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
    def __init__(self, cast_shadows: bool = False):
        self.cast_shadows = cast_shadows

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cast_shadows")
        if self.cast_shadows is not None:
            el.text = str(self.cast_shadows).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CastShadows":
        _text = el.text or False
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


class Ambient(Model):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0.2 0.2 0.2 1.0")
        self.ambient = ambient

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _text = el.text or "0.2 0.2 0.2 1.0"
        _ambient = Color.from_sdf(_text)
        return cls(ambient=_ambient)


class Specular(Model):
    def __init__(self, specular: Color = None):
        if specular is None:
            specular = Color.from_sdf(".1 .1 .1 1")
        self.specular = specular

    def to_sdf(self) -> ET.Element:
        el = ET.Element("specular")
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _text = el.text or ".1 .1 .1 1"
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
            ambient: "Ambient" = None,
            diffuse: "Diffuse" = None,
            specular: "Specular" = None,
            emissive: "Emissive" = None
    ):
        self.script = script
        self.shader = shader
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
        _c_ambient = el.find("ambient")
        _ambient = Ambient.from_sdf(_c_ambient) if _c_ambient is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse) if _c_diffuse is not None else None
        _c_specular = el.find("specular")
        _specular = Specular.from_sdf(_c_specular) if _c_specular is not None else None
        _c_emissive = el.find("emissive")
        _emissive = Emissive.from_sdf(_c_emissive) if _c_emissive is not None else None
        return cls(script=_script, shader=_shader, ambient=_ambient, diffuse=_diffuse, specular=_specular,
                   emissive=_emissive)


class Visual(Model):
    def __init__(
            self,
            name: str = "__default__",
            geometry: "Geometry" = None,
            plugin: List["Plugin"] = None,
            cast_shadows: "CastShadows" = None,
            laser_retro: "LaserRetro" = None,
            transparency: "Transparency" = None,
            pose: "Pose" = None,
            material: "Material" = None
    ):
        self.name = name
        self.geometry = geometry
        self.plugin = plugin or []
        self.cast_shadows = cast_shadows
        self.laser_retro = laser_retro
        self.transparency = transparency
        self.pose = pose
        self.material = material

    def to_sdf(self) -> ET.Element:
        el = ET.Element("visual")
        if self.name is not None:
            el.set("name", self.name)
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
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.material is not None:
            el.append(self.material.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visual":
        _name = el.get("name", "__default__")
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry) if _c_geometry is not None else None
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_cast_shadows = el.find("cast_shadows")
        _cast_shadows = CastShadows.from_sdf(_c_cast_shadows) if _c_cast_shadows is not None else None
        _c_laser_retro = el.find("laser_retro")
        _laser_retro = LaserRetro.from_sdf(_c_laser_retro) if _c_laser_retro is not None else None
        _c_transparency = el.find("transparency")
        _transparency = Transparency.from_sdf(_c_transparency) if _c_transparency is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_material = el.find("material")
        _material = Material.from_sdf(_c_material) if _c_material is not None else None
        return cls(name=_name, geometry=_geometry, plugin=_plugin, cast_shadows=_cast_shadows, laser_retro=_laser_retro,
                   transparency=_transparency, pose=_pose, material=_material)


class Camera(Model):
    def __init__(
            self,
            name: str = "user_camera",
            view_controller: "ViewController" = None,
            pose: "Pose" = None,
            track_visual: "TrackVisual" = None
    ):
        self.name = name
        self.view_controller = view_controller
        self.pose = pose
        self.track_visual = track_visual

    def to_sdf(self) -> ET.Element:
        el = ET.Element("camera")
        if self.name is not None:
            el.set("name", self.name)
        if self.view_controller is not None:
            el.append(self.view_controller.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.track_visual is not None:
            el.append(self.track_visual.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _name = el.get("name", "user_camera")
        _c_view_controller = el.find("view_controller")
        _view_controller = ViewController.from_sdf(_c_view_controller) if _c_view_controller is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_track_visual = el.find("track_visual")
        _track_visual = TrackVisual.from_sdf(_c_track_visual) if _c_track_visual is not None else None
        return cls(name=_name, view_controller=_view_controller, pose=_pose, track_visual=_track_visual)


class Samples(Model):
    def __init__(self, samples: int = 640):
        self.samples = samples

    def to_sdf(self) -> ET.Element:
        el = ET.Element("samples")
        if self.samples is not None:
            el.text = str(self.samples)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Samples":
        _text = el.text or 640
        _samples = _parse_uint32(_text)
        return cls(samples=_samples)


class Resolution(Model):
    def __init__(self, resolution: float = 1):
        self.resolution = resolution

    def to_sdf(self) -> ET.Element:
        el = ET.Element("resolution")
        if self.resolution is not None:
            el.text = str(self.resolution)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Resolution":
        _text = el.text or 1
        _resolution = _parse_double(_text)
        return cls(resolution=_resolution)


class MinAngle(Model):
    def __init__(self, min_angle: float = 0):
        self.min_angle = min_angle

    def to_sdf(self) -> ET.Element:
        el = ET.Element("min_angle")
        if self.min_angle is not None:
            el.text = str(self.min_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MinAngle":
        _text = el.text or 0
        _min_angle = _parse_double(_text)
        return cls(min_angle=_min_angle)


class MaxAngle(Model):
    def __init__(self, max_angle: float = 0):
        self.max_angle = max_angle

    def to_sdf(self) -> ET.Element:
        el = ET.Element("max_angle")
        if self.max_angle is not None:
            el.text = str(self.max_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxAngle":
        _text = el.text or 0
        _max_angle = _parse_double(_text)
        return cls(max_angle=_max_angle)


class Horizontal(Model):
    def __init__(
            self,
            samples: "Samples" = None,
            resolution: "Resolution" = None,
            min_angle: "MinAngle" = None,
            max_angle: "MaxAngle" = None
    ):
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_sdf(self) -> ET.Element:
        el = ET.Element("horizontal")
        if self.samples is not None:
            el.append(self.samples.to_sdf())
        if self.resolution is not None:
            el.append(self.resolution.to_sdf())
        if self.min_angle is not None:
            el.append(self.min_angle.to_sdf())
        if self.max_angle is not None:
            el.append(self.max_angle.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Horizontal":
        _c_samples = el.find("samples")
        _samples = Samples.from_sdf(_c_samples) if _c_samples is not None else None
        _c_resolution = el.find("resolution")
        _resolution = Resolution.from_sdf(_c_resolution) if _c_resolution is not None else None
        _c_min_angle = el.find("min_angle")
        _min_angle = MinAngle.from_sdf(_c_min_angle) if _c_min_angle is not None else None
        _c_max_angle = el.find("max_angle")
        _max_angle = MaxAngle.from_sdf(_c_max_angle) if _c_max_angle is not None else None
        return cls(samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


class Vertical(Model):
    def __init__(
            self,
            samples: "Samples" = None,
            resolution: "Resolution" = None,
            min_angle: "MinAngle" = None,
            max_angle: "MaxAngle" = None
    ):
        self.samples = samples
        self.resolution = resolution
        self.min_angle = min_angle
        self.max_angle = max_angle

    def to_sdf(self) -> ET.Element:
        el = ET.Element("vertical")
        if self.samples is not None:
            el.append(self.samples.to_sdf())
        if self.resolution is not None:
            el.append(self.resolution.to_sdf())
        if self.min_angle is not None:
            el.append(self.min_angle.to_sdf())
        if self.max_angle is not None:
            el.append(self.max_angle.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Vertical":
        _c_samples = el.find("samples")
        _samples = Samples.from_sdf(_c_samples) if _c_samples is not None else None
        _c_resolution = el.find("resolution")
        _resolution = Resolution.from_sdf(_c_resolution) if _c_resolution is not None else None
        _c_min_angle = el.find("min_angle")
        _min_angle = MinAngle.from_sdf(_c_min_angle) if _c_min_angle is not None else None
        _c_max_angle = el.find("max_angle")
        _max_angle = MaxAngle.from_sdf(_c_max_angle) if _c_max_angle is not None else None
        return cls(samples=_samples, resolution=_resolution, min_angle=_min_angle, max_angle=_max_angle)


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


class Range(Model):
    def __init__(self, range: float = 10):
        self.range = range

    def to_sdf(self) -> ET.Element:
        el = ET.Element("range")
        if self.range is not None:
            el.text = str(self.range)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Range":
        _text = el.text or 10
        _range = _parse_double(_text)
        return cls(range=_range)


class Ray(Model):
    def __init__(self, scan: "Scan" = None, range: "Range" = None):
        self.scan = scan
        self.range = range

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ray")
        if self.scan is not None:
            el.append(self.scan.to_sdf())
        if self.range is not None:
            el.append(self.range.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ray":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range) if _c_range is not None else None
        return cls(scan=_scan, range=_range)


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
    def __init__(self, update_rate: float = 1000):
        self.update_rate = update_rate

    def to_sdf(self) -> ET.Element:
        el = ET.Element("update_rate")
        if self.update_rate is not None:
            el.text = str(self.update_rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UpdateRate":
        _text = el.text or 1000
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


class Sensor(Model):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "__default__",
            plugin: List["Plugin"] = None,
            camera: "Camera" = None,
            ray: "Ray" = None,
            contact: "Contact" = None,
            rfidtag: "Rfidtag" = None,
            rfid: "Rfid" = None,
            imu: "Imu" = None,
            always_on: "AlwaysOn" = None,
            update_rate: "UpdateRate" = None,
            visualize: "Visualize" = None,
            pose: "Pose" = None,
            topic: "Topic" = None
    ):
        self.name = name
        self.type = type
        self.plugin = plugin or []
        self.camera = camera
        self.ray = ray
        self.contact = contact
        self.rfidtag = rfidtag
        self.rfid = rfid
        self.imu = imu
        self.always_on = always_on
        self.update_rate = update_rate
        self.visualize = visualize
        self.pose = pose
        self.topic = topic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sensor")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.camera is not None:
            el.append(self.camera.to_sdf())
        if self.ray is not None:
            el.append(self.ray.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        if self.rfidtag is not None:
            el.append(self.rfidtag.to_sdf())
        if self.rfid is not None:
            el.append(self.rfid.to_sdf())
        if self.imu is not None:
            el.append(self.imu.to_sdf())
        if self.always_on is not None:
            el.append(self.always_on.to_sdf())
        if self.update_rate is not None:
            el.append(self.update_rate.to_sdf())
        if self.visualize is not None:
            el.append(self.visualize.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.topic is not None:
            el.append(self.topic.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sensor":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_camera = el.find("camera")
        _camera = Camera.from_sdf(_c_camera) if _c_camera is not None else None
        _c_ray = el.find("ray")
        _ray = Ray.from_sdf(_c_ray) if _c_ray is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        _c_rfidtag = el.find("rfidtag")
        _rfidtag = Rfidtag.from_sdf(_c_rfidtag) if _c_rfidtag is not None else None
        _c_rfid = el.find("rfid")
        _rfid = Rfid.from_sdf(_c_rfid) if _c_rfid is not None else None
        _c_imu = el.find("imu")
        _imu = Imu.from_sdf(_c_imu) if _c_imu is not None else None
        _c_always_on = el.find("always_on")
        _always_on = AlwaysOn.from_sdf(_c_always_on) if _c_always_on is not None else None
        _c_update_rate = el.find("update_rate")
        _update_rate = UpdateRate.from_sdf(_c_update_rate) if _c_update_rate is not None else None
        _c_visualize = el.find("visualize")
        _visualize = Visualize.from_sdf(_c_visualize) if _c_visualize is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic) if _c_topic is not None else None
        return cls(name=_name, type=_type, plugin=_plugin, camera=_camera, ray=_ray, contact=_contact, rfidtag=_rfidtag,
                   rfid=_rfid, imu=_imu, always_on=_always_on, update_rate=_update_rate, visualize=_visualize,
                   pose=_pose, topic=_topic)


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
            plugin: List["Plugin"] = None,
            texture: "Texture" = None,
            pose: "Pose" = None,
            fov: "Fov" = None,
            near_clip: "NearClip" = None,
            far_clip: "FarClip" = None
    ):
        self.name = name
        self.plugin = plugin or []
        self.texture = texture
        self.pose = pose
        self.fov = fov
        self.near_clip = near_clip
        self.far_clip = far_clip

    def to_sdf(self) -> ET.Element:
        el = ET.Element("projector")
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.texture is not None:
            el.append(self.texture.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
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
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_texture = el.find("texture")
        _texture = Texture.from_sdf(_c_texture) if _c_texture is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_fov = el.find("fov")
        _fov = Fov.from_sdf(_c_fov) if _c_fov is not None else None
        _c_near_clip = el.find("near_clip")
        _near_clip = NearClip.from_sdf(_c_near_clip) if _c_near_clip is not None else None
        _c_far_clip = el.find("far_clip")
        _far_clip = FarClip.from_sdf(_c_far_clip) if _c_far_clip is not None else None
        return cls(name=_name, plugin=_plugin, texture=_texture, pose=_pose, fov=_fov, near_clip=_near_clip,
                   far_clip=_far_clip)


class Gravity(Model):
    def __init__(self, gravity: Vector3 = None):
        if gravity is None:
            gravity = Vector3.from_sdf("0 0 -9.8")
        self.gravity = gravity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gravity")
        if self.gravity is not None:
            el.text = self.gravity.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gravity":
        _text = el.text or "0 0 -9.8"
        _gravity = Vector3.from_sdf(_text)
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


class Linear(Model):
    def __init__(self, linear: float = 1):
        self.linear = linear

    def to_sdf(self) -> ET.Element:
        el = ET.Element("linear")
        if self.linear is not None:
            el.text = str(self.linear)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Linear":
        _text = el.text or 1
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
            inertial: "Inertial" = None,
            collision: List["Collision"] = None,
            visual: List["Visual"] = None,
            sensor: List["Sensor"] = None,
            projector: List["Projector"] = None,
            gravity: "Gravity" = None,
            self_collide: "SelfCollide" = None,
            kinematic: "Kinematic" = None,
            pose: "Pose" = None,
            velocity_decay: "VelocityDecay" = None
    ):
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

    def to_sdf(self) -> ET.Element:
        el = ET.Element("link")
        if self.name is not None:
            el.set("name", self.name)
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
        if self.gravity is not None:
            el.append(self.gravity.to_sdf())
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf())
        if self.kinematic is not None:
            el.append(self.kinematic.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.velocity_decay is not None:
            el.append(self.velocity_decay.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Link":
        _name = el.get("name", "__default__")
        _c_inertial = el.find("inertial")
        _inertial = Inertial.from_sdf(_c_inertial) if _c_inertial is not None else None
        _collision = [Collision.from_sdf(c) for c in el.findall("collision")]
        _visual = [Visual.from_sdf(c) for c in el.findall("visual")]
        _sensor = [Sensor.from_sdf(c) for c in el.findall("sensor")]
        _projector = [Projector.from_sdf(c) for c in el.findall("projector")]
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_self_collide = el.find("self_collide")
        _self_collide = SelfCollide.from_sdf(_c_self_collide) if _c_self_collide is not None else None
        _c_kinematic = el.find("kinematic")
        _kinematic = Kinematic.from_sdf(_c_kinematic) if _c_kinematic is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_velocity_decay = el.find("velocity_decay")
        _velocity_decay = VelocityDecay.from_sdf(_c_velocity_decay) if _c_velocity_decay is not None else None
        return cls(name=_name, inertial=_inertial, collision=_collision, visual=_visual, sensor=_sensor,
                   projector=_projector, gravity=_gravity, self_collide=_self_collide, kinematic=_kinematic, pose=_pose,
                   velocity_decay=_velocity_decay)


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


class Damping(Model):
    def __init__(self, damping: float = 0):
        self.damping = damping

    def to_sdf(self) -> ET.Element:
        el = ET.Element("damping")
        if self.damping is not None:
            el.text = str(self.damping)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Damping":
        _text = el.text or 0
        _damping = _parse_double(_text)
        return cls(damping=_damping)


class Dynamics(Model):
    def __init__(self, damping: "Damping" = None, friction: "Friction" = None):
        self.damping = damping
        self.friction = friction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dynamics")
        if self.damping is not None:
            el.append(self.damping.to_sdf())
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dynamics":
        _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping) if _c_damping is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        return cls(damping=_damping, friction=_friction)


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


class Limit(Model):
    def __init__(
            self,
            lower: "Lower" = None,
            upper: "Upper" = None,
            effort: "Effort" = None,
            velocity: "Velocity" = None
    ):
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity

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
        return cls(lower=_lower, upper=_upper, effort=_effort, velocity=_velocity)


class Axis(Model):
    def __init__(self, xyz: "Xyz" = None, dynamics: "Dynamics" = None, limit: "Limit" = None):
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit

    def to_sdf(self) -> ET.Element:
        el = ET.Element("axis")
        if self.xyz is not None:
            el.append(self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf())
        if self.limit is not None:
            el.append(self.limit.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis":
        _c_xyz = el.find("xyz")
        _xyz = Xyz.from_sdf(_c_xyz) if _c_xyz is not None else None
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit) if _c_limit is not None else None
        return cls(xyz=_xyz, dynamics=_dynamics, limit=_limit)


class Axis2(Model):
    def __init__(self, xyz: "Xyz" = None, dynamics: "Dynamics" = None, limit: "Limit" = None):
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit

    def to_sdf(self) -> ET.Element:
        el = ET.Element("axis2")
        if self.xyz is not None:
            el.append(self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf())
        if self.limit is not None:
            el.append(self.limit.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis2":
        _c_xyz = el.find("xyz")
        _xyz = Xyz.from_sdf(_c_xyz) if _c_xyz is not None else None
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit) if _c_limit is not None else None
        return cls(xyz=_xyz, dynamics=_dynamics, limit=_limit)


class Bullet(Model):
    def __init__(self, dt: "Dt" = None):
        self.dt = dt

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bullet")
        if self.dt is not None:
            el.append(self.dt.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _c_dt = el.find("dt")
        _dt = Dt.from_sdf(_c_dt) if _c_dt is not None else None
        return cls(dt=_dt)


class Physics(Model):
    def __init__(
            self,
            type: str = "ode",
            update_rate: "UpdateRate" = None,
            max_contacts: "MaxContacts" = None,
            gravity: "Gravity" = None,
            bullet: "Bullet" = None,
            ode: "Ode" = None
    ):
        self.type = type
        self.update_rate = update_rate
        self.max_contacts = max_contacts
        self.gravity = gravity
        self.bullet = bullet
        self.ode = ode

    def to_sdf(self) -> ET.Element:
        el = ET.Element("physics")
        if self.type is not None:
            el.set("type", self.type)
        if self.update_rate is not None:
            el.append(self.update_rate.to_sdf())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        if self.gravity is not None:
            el.append(self.gravity.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Physics":
        _type = el.get("type", "ode")
        _c_update_rate = el.find("update_rate")
        _update_rate = UpdateRate.from_sdf(_c_update_rate) if _c_update_rate is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        return cls(type=_type, update_rate=_update_rate, max_contacts=_max_contacts, gravity=_gravity, bullet=_bullet,
                   ode=_ode)


class Joint(Model):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "__default__",
            parent: "Parent" = None,
            child: "Child" = None,
            pose: "Pose" = None,
            thread_pitch: "ThreadPitch" = None,
            axis: "Axis" = None,
            axis2: "Axis2" = None,
            physics: "Physics" = None
    ):
        self.name = name
        self.type = type
        self.parent = parent
        self.child = child
        self.pose = pose
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
        if self.parent is not None:
            el.append(self.parent.to_sdf())
        if self.child is not None:
            el.append(self.child.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
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
        _c_parent = el.find("parent")
        _parent = Parent.from_sdf(_c_parent) if _c_parent is not None else None
        _c_child = el.find("child")
        _child = Child.from_sdf(_c_child) if _c_child is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_thread_pitch = el.find("thread_pitch")
        _thread_pitch = ThreadPitch.from_sdf(_c_thread_pitch) if _c_thread_pitch is not None else None
        _c_axis = el.find("axis")
        _axis = Axis.from_sdf(_c_axis) if _c_axis is not None else None
        _c_axis2 = el.find("axis2")
        _axis2 = Axis2.from_sdf(_c_axis2) if _c_axis2 is not None else None
        _c_physics = el.find("physics")
        _physics = Physics.from_sdf(_c_physics) if _c_physics is not None else None
        return cls(name=_name, type=_type, parent=_parent, child=_child, pose=_pose, thread_pitch=_thread_pitch,
                   axis=_axis, axis2=_axis2, physics=_physics)


class Filename(Model):
    def __init__(self, filename: str = "__default__"):
        self.filename = filename

    def to_sdf(self) -> ET.Element:
        el = ET.Element("filename")
        if self.filename is not None:
            el.text = self.filename
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Filename":
        _text = el.text or "__default__"
        _filename = _text
        return cls(filename=_filename)


class Skin(Model):
    def __init__(self, filename: "Filename" = None, scale: "Scale" = None):
        self.filename = filename
        self.scale = scale

    def to_sdf(self) -> ET.Element:
        el = ET.Element("skin")
        if self.filename is not None:
            el.append(self.filename.to_sdf())
        if self.scale is not None:
            el.append(self.scale.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Skin":
        _c_filename = el.find("filename")
        _filename = Filename.from_sdf(_c_filename) if _c_filename is not None else None
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale) if _c_scale is not None else None
        return cls(filename=_filename, scale=_scale)


class InterpolateX(Model):
    def __init__(self, interpolate_x: bool = False):
        self.interpolate_x = interpolate_x

    def to_sdf(self) -> ET.Element:
        el = ET.Element("interpolate_x")
        if self.interpolate_x is not None:
            el.text = str(self.interpolate_x).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "InterpolateX":
        _text = el.text or False
        _interpolate_x = _text.strip().lower() == 'true'
        return cls(interpolate_x=_interpolate_x)


class Animation(Model):
    def __init__(
            self,
            name: str = "__default__",
            filename: "Filename" = None,
            scale: "Scale" = None,
            interpolate_x: "InterpolateX" = None
    ):
        self.name = name
        self.filename = filename
        self.scale = scale
        self.interpolate_x = interpolate_x

    def to_sdf(self) -> ET.Element:
        el = ET.Element("animation")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.append(self.filename.to_sdf())
        if self.scale is not None:
            el.append(self.scale.to_sdf())
        if self.interpolate_x is not None:
            el.append(self.interpolate_x.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Animation":
        _name = el.get("name", "__default__")
        _c_filename = el.find("filename")
        _filename = Filename.from_sdf(_c_filename) if _c_filename is not None else None
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale) if _c_scale is not None else None
        _c_interpolate_x = el.find("interpolate_x")
        _interpolate_x = InterpolateX.from_sdf(_c_interpolate_x) if _c_interpolate_x is not None else None
        return cls(name=_name, filename=_filename, scale=_scale, interpolate_x=_interpolate_x)


class Actor(Model):
    def __init__(
            self,
            name: str = "__default__",
            static: bool = False,
            link: List["Link"] = None,
            joint: List["Joint"] = None,
            plugin: List["Plugin"] = None,
            pose: "Pose" = None,
            skin: "Skin" = None,
            animation: List["Animation"] = None,
            script: "Script" = None
    ):
        self.name = name
        self.static = static
        self.link = link or []
        self.joint = joint or []
        self.plugin = plugin or []
        self.pose = pose
        self.skin = skin
        self.animation = animation or []
        self.script = script

    def to_sdf(self) -> ET.Element:
        el = ET.Element("actor")
        if self.name is not None:
            el.set("name", self.name)
        if self.static is not None:
            el.set("static", str(self.static).lower())
        for item in (self.link or []):
            el.append(item.to_sdf())
        for item in (self.joint or []):
            el.append(item.to_sdf())
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.skin is not None:
            el.append(self.skin.to_sdf())
        for item in (self.animation or []):
            el.append(item.to_sdf())
        if self.script is not None:
            el.append(self.script.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Actor":
        _name = el.get("name", "__default__")
        _static = el.get("static", False).strip().lower() == 'true'
        _link = [Link.from_sdf(c) for c in el.findall("link")]
        _joint = [Joint.from_sdf(c) for c in el.findall("joint")]
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_skin = el.find("skin")
        _skin = Skin.from_sdf(_c_skin) if _c_skin is not None else None
        _animation = [Animation.from_sdf(c) for c in el.findall("animation")]
        _c_script = el.find("script")
        _script = Script.from_sdf(_c_script) if _c_script is not None else None
        return cls(name=_name, static=_static, link=_link, joint=_joint, plugin=_plugin, pose=_pose, skin=_skin,
                   animation=_animation, script=_script)
