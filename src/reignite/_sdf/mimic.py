### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class Mimic(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        axis: str | None = None,
        joint: str | None = None,
        multiplier: float | None = None,
        offset: float | None = None,
        reference: float | None = None
    ):
        super().__init__(sdf_version)
        self.axis = axis
        self.joint = joint
        self.multiplier = multiplier
        self.offset = offset
        self.reference = reference

    def to_version(self, target_version: str) -> "Mimic":
        kwargs: dict = {"sdf_version": target_version, "axis": self.axis, "joint": self.joint, "multiplier": self.multiplier, "offset": self.offset, "reference": self.reference}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("mimic")
        if self.axis is not None:
            el.set("axis", self.axis)
        if self.joint is None:
            raise ValueError(f"'joint' is required in SDF version {version}")
        if self.joint is not None:
            el.set("joint", self.joint)
        if self.multiplier is not None:
            _c_tmp = ET.Element("multiplier")
            _c_tmp.text = str(self.multiplier)
            el.append(_c_tmp)
        if self.offset is not None:
            _c_tmp = ET.Element("offset")
            _c_tmp.text = str(self.offset)
            el.append(_c_tmp)
        if self.reference is not None:
            _c_tmp = ET.Element("reference")
            _c_tmp.text = str(self.reference)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Mimic | SDFError":
        _axis = el.get("axis", "axis")
        if isinstance(_axis, SDFError):
            return _axis.extend("@axis")
        if el.get("joint") is None:
            return SDFError(f"'joint' is required in SDF version {version}")
        _joint = el.get("joint", None)
        if isinstance(_joint, SDFError):
            return _joint.extend("@joint")
        _c_tmp = el.find("multiplier")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("multiplier")
            _multiplier = _val
        else:
            _multiplier = None
        _c_tmp = el.find("offset")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("offset")
            _offset = _val
        else:
            _offset = None
        _c_tmp = el.find("reference")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("reference")
            _reference = _val
        else:
            _reference = None
        return cls(sdf_version=version, axis=_axis, joint=_joint, multiplier=_multiplier, offset=_offset, reference=_reference)
