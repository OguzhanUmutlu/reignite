### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


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



class AttachSteps(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 20
        _attach_steps = _parse_int32(_text)
        if isinstance(_attach_steps, SDFError):
            return _attach_steps
        if _attach_steps is not None and cmp_version(version, "1.2") < 0:
            if _attach_steps != 20:
                return SDFError(f"'attach_steps' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, attach_steps=_attach_steps)


class DetachSteps(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 40
        _detach_steps = _parse_int32(_text)
        if isinstance(_detach_steps, SDFError):
            return _detach_steps
        if _detach_steps is not None and cmp_version(version, "1.2") < 0:
            if _detach_steps != 40:
                return SDFError(f"'detach_steps' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, detach_steps=_detach_steps)


class GraspCheck(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        attach_steps: int = 20,
        detach_steps: int = 40,
        min_contact_count: int = 2
    ):
        self.__version__ = sdf_version
        self.attach_steps = attach_steps
        self.detach_steps = detach_steps
        self.min_contact_count = min_contact_count

    def to_version(self, target_version: str) -> "GraspCheck":
        if self.attach_steps is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'attach_steps' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.detach_steps is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'detach_steps' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.min_contact_count is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'min_contact_count' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["attach_steps"] = self.attach_steps
        kwargs["detach_steps"] = self.detach_steps
        kwargs["min_contact_count"] = self.min_contact_count
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grasp_check")
        if self.attach_steps is not None:
            el.set("attach_steps", str(self.attach_steps))
        if self.detach_steps is not None:
            el.set("detach_steps", str(self.detach_steps))
        if self.min_contact_count is not None:
            el.set("min_contact_count", str(self.min_contact_count))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _attach_steps = _parse_int32(el.get("attach_steps", 20))
        if isinstance(_attach_steps, SDFError):
            return _attach_steps.extend("@attach_steps")
        _detach_steps = _parse_int32(el.get("detach_steps", 40))
        if isinstance(_detach_steps, SDFError):
            return _detach_steps.extend("@detach_steps")
        _min_contact_count = _parse_uint32(el.get("min_contact_count", 2))
        if isinstance(_min_contact_count, SDFError):
            return _min_contact_count.extend("@min_contact_count")
        return cls(sdf_version=version, attach_steps=_attach_steps, detach_steps=_detach_steps, min_contact_count=_min_contact_count)


class Gripper(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        grasp_check: "GraspCheck" = None,
        gripper_link: List["GripperLink"] = None,
        name: str = "__default__",
        palm_link: "PalmLink" = None
    ):
        self.__version__ = sdf_version
        self.grasp_check = grasp_check
        self.gripper_link = gripper_link or []
        self.name = name
        self.palm_link = palm_link

    def to_version(self, target_version: str) -> "Gripper":
        kwargs = {"sdf_version": target_version}
        kwargs["grasp_check"] = self.grasp_check.to_version(target_version) if self.grasp_check is not None else None
        kwargs["gripper_link"] = [c.to_version(target_version) for c in (self.gripper_link or [])]
        kwargs["name"] = self.name
        kwargs["palm_link"] = self.palm_link.to_version(target_version) if self.palm_link is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gripper")
        if self.grasp_check is not None:
            el.append(self.grasp_check.to_sdf(version))
        for item in (self.gripper_link or []):
            el.append(item.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.palm_link is not None:
            el.append(self.palm_link.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_palm_link = el.find("palm_link")
        if _c_palm_link is not None:
            _res = PalmLink._from_sdf(_c_palm_link, version)
            if isinstance(_res, SDFError):
                return _res.extend("palm_link")
            _palm_link = _res
        else:
            _palm_link = None
        return cls(sdf_version=version, grasp_check=_grasp_check, gripper_link=_gripper_link, name=_name, palm_link=_palm_link)


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


class MinContactCount(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2
        _min_contact_count = _parse_uint32(_text)
        if isinstance(_min_contact_count, SDFError):
            return _min_contact_count
        if _min_contact_count is not None and cmp_version(version, "1.2") < 0:
            if _min_contact_count != 2:
                return SDFError(f"'min_contact_count' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min_contact_count=_min_contact_count)


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
