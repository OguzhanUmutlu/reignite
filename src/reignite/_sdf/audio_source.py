### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose, Pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame

def _parse_pose(raw: str, el: ET.Element | None = None) -> _PoseT | SDFError:
    try:
        is_degrees = el is not None and str(el.get('degrees')).lower() == 'true'
        return _pose(raw, degrees=is_degrees)
    except ValueError as e:
        return SDFError(str(e))

def _pose_to_sdf(val: _PoseT, el: ET.Element | None = None) -> str:
    if el is not None:
        el.attrib.pop('degrees', None)
    if isinstance(val, Pose):
        return val.to_sdf()
    p = _pose(val)
    return p.to_sdf()


# noinspection PyUnusedImports
class AudioSource(BaseModel):
    class Contact(BaseModel):
        def __init__(self, sdf_version: str | None = None, collisions: List[str] | None = None):
            super().__init__(sdf_version)
            self.collisions = collisions or []

        def add_collision(self, *items: str):
            if self.collisions is None:
                self.collisions = []
            self.collisions.extend(items)

        def to_version(self, target_version: str) -> "AudioSource.Contact":
            kwargs: dict = {"sdf_version": target_version, "collisions": self.collisions}
            return AudioSource.Contact(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("contact")
            for _v in (self.collisions or []):
                _c_tmp = ET.Element("collision")
                _c_tmp.text = _v
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "AudioSource.Contact | SDFError":
            _collisions = []
            for c in el.findall("collision"):
                _text = c.text if c.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("collision")
                _collisions.append(_val)
            return cls(sdf_version=version, collisions=_collisions)

    def __init__(
        self,
        sdf_version: str | None = None,
        contact: "AudioSource.Contact" = None,
        frames: List["Frame"] = None,
        gain: float | None = None,
        loop: bool | None = None,
        pitch: float | None = None,
        pose: _PoseT | None = None,
        uri: str | None = None
    ):
        super().__init__(sdf_version)
        self.contact = contact
        self.frames = frames or []
        self.gain = gain
        self.loop = loop
        self.pitch = pitch
        self.pose = _pose(pose) if pose is not None else None
        self.uri = uri
        if self.contact is not None and hasattr(self.contact, 'to_version'):
            if getattr(self.contact, 'sdfversion', None) is None:
                self.contact.sdfversion = self.sdfversion
            elif getattr(self.contact, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.contact = self.contact.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def to_version(self, target_version: str) -> "AudioSource":
        from ..elements.frame import Frame
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "contact": self.contact.to_version(target_version) if self.contact is not None and hasattr(self.contact, "to_version") else self.contact, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "gain": self.gain, "loop": self.loop, "pitch": self.pitch, "pose": self.pose, "uri": self.uri}
        return AudioSource(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("audio_source")
        if self.contact is not None:
            _child_res = self.contact.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('contact')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.gain is not None:
            _c_tmp = ET.Element("gain")
            _c_tmp.text = str(self.gain)
            el.append(_c_tmp)
        if self.loop is not None:
            _c_tmp = ET.Element("loop")
            _c_tmp.text = str(self.loop).lower()
            el.append(_c_tmp)
        if self.pitch is not None:
            _c_tmp = ET.Element("pitch")
            _c_tmp.text = str(self.pitch)
            el.append(_c_tmp)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = _pose_to_sdf(self.pose, _c_tmp)
            el.append(_c_tmp)
        if self.uri is not None:
            _c_tmp = ET.Element("uri")
            _c_tmp.text = self.uri
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "AudioSource | SDFError":
        from ..elements.frame import Frame
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = cls.Contact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _c_tmp = el.find("gain")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("gain")
            _gain = _val
        else:
            _gain = None
        _c_tmp = el.find("loop")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("loop")
            _loop = _val
        else:
            _loop = None
        _c_tmp = el.find("pitch")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("pitch")
            _pitch = _val
        else:
            _pitch = None
        _c_tmp = el.find("pose")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text, _c_tmp)
            if isinstance(_val, SDFError):
                return _val.extend("pose")
            _pose = _val
        else:
            _pose = None
        _c_tmp = el.find("uri")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("uri")
            _uri = _val
        else:
            _uri = None
        return cls(sdf_version=version, contact=_contact, frames=_frames, gain=_gain, loop=_loop, pitch=_pitch, pose=_pose, uri=_uri)
