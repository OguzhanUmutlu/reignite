from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ._base import Model
from ..utils.pose import Pose
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



class Uri(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Uri":
        _text = el.text or "__default__"
        _uri = _text
        return cls(sdf_version=version, uri=_uri)


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


class Gain(Model):
    def __init__(self, sdf_version: str, gain: float = 1.0):
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
        _text = el.text or 1.0
        _gain = _parse_double(_text)
        return cls(sdf_version=version, gain=_gain)


class Collision(Model):
    def __init__(self, sdf_version: str, collision: str = "__default__"):
        self.__version__ = sdf_version
        self.collision = collision

    def to_version(self, target_version: str) -> "Collision":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Collision":
        _text = el.text or "__default__"
        _collision = _text
        return cls(sdf_version=version, collision=_collision)


class Contact(Model):
    def __init__(self, sdf_version: str, collision: List["Collision"] = None):
        self.__version__ = sdf_version
        self.collision = collision or []

    def to_version(self, target_version: str) -> "Contact":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Contact":
        _collision = [Collision.from_sdf(c, version) for c in el.findall("collision")]
        return cls(sdf_version=version, collision=_collision)


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


class Pose(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: Pose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Pose":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        _frame = el.get("frame", "")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                raise ValueError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                raise ValueError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                raise ValueError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Frame(Model):
    def __init__(self, sdf_version: str, name: str = "", pose: "Pose" = None):
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
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Frame":
        _name = el.get("name", "")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        return cls(sdf_version=version, name=_name, pose=_pose)


class AudioSource(Model):
    def __init__(
        self,
        sdf_version: str,
        uri: "Uri" = None,
        pitch: "Pitch" = None,
        gain: "Gain" = None,
        contact: "Contact" = None,
        loop: "Loop" = None,
        pose: "Pose" = None,
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
        _frame = [Frame.from_sdf(c, version) for c in el.findall("frame")]
        if _frame and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, uri=_uri, pitch=_pitch, gain=_gain, contact=_contact, loop=_loop, pose=_pose, frame=_frame)
