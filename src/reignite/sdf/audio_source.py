### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

from .frame import Frame
from .pose import Pose


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



class AudioSource(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        contact: "Contact" = None,
        frame: List["Frame"] = None,
        gain: "Gain" = None,
        loop: "Loop" = None,
        pitch: "Pitch" = None,
        pose: "Pose" = None,
        uri: "Uri" = None
    ):
        self.__version__ = sdf_version
        self.contact = contact
        self.frame = frame or []
        self.gain = gain
        self.loop = loop
        self.pitch = pitch
        self.pose = pose
        self.uri = uri

    def to_version(self, target_version: str) -> "AudioSource":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["gain"] = self.gain.to_version(target_version) if self.gain is not None else None
        kwargs["loop"] = self.loop.to_version(target_version) if self.loop is not None else None
        kwargs["pitch"] = self.pitch.to_version(target_version) if self.pitch is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("audio_source")
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.gain is not None:
            el.append(self.gain.to_sdf(version))
        if self.loop is not None:
            el.append(self.loop.to_sdf(version))
        if self.pitch is not None:
            el.append(self.pitch.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = Contact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_gain = el.find("gain")
        if _c_gain is not None:
            _res = Gain._from_sdf(_c_gain, version)
            if isinstance(_res, SDFError):
                return _res.extend("gain")
            _gain = _res
        else:
            _gain = None
        _c_loop = el.find("loop")
        if _c_loop is not None:
            _res = Loop._from_sdf(_c_loop, version)
            if isinstance(_res, SDFError):
                return _res.extend("loop")
            _loop = _res
        else:
            _loop = None
        _c_pitch = el.find("pitch")
        if _c_pitch is not None:
            _res = Pitch._from_sdf(_c_pitch, version)
            if isinstance(_res, SDFError):
                return _res.extend("pitch")
            _pitch = _res
        else:
            _pitch = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        return cls(sdf_version=version, contact=_contact, frame=_frame, gain=_gain, loop=_loop, pitch=_pitch, pose=_pose, uri=_uri)


class Collision(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _collision = _text
        if isinstance(_collision, SDFError):
            return _collision
        return cls(sdf_version=version, collision=_collision)


class Contact(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _collision = []
        for c in el.findall("collision"):
            _res = Collision._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collision.append(_res)
        return cls(sdf_version=version, collision=_collision)


class Gain(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _gain = _parse_double(_text)
        if isinstance(_gain, SDFError):
            return _gain
        return cls(sdf_version=version, gain=_gain)


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
