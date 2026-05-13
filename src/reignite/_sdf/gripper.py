### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError


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



class Gripper(BaseModel):
    class GraspCheck(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            attach_steps: int = 20,
            detach_steps: int = 40,
            min_contact_count: int = 2
        ):
            super().__init__(sdf_version)
            self.attach_steps = attach_steps
            self.detach_steps = detach_steps
            self.min_contact_count = min_contact_count

        def to_version(self, target_version: str) -> "Gripper.GraspCheck":
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

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("grasp_check")
            if self.attach_steps is not None:
                el.set("attach_steps", str(self.attach_steps))
            if self.detach_steps is not None:
                el.set("detach_steps", str(self.detach_steps))
            if self.min_contact_count is not None:
                el.set("min_contact_count", str(self.min_contact_count))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Gripper.GraspCheck | SDFError":
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

    def __init__(
        self,
        sdf_version: str | None = None,
        grasp_check: "Gripper.GraspCheck" = None,
        gripper_links: List[str] = None,
        name: str = "__default__",
        palm_link: str = "__default__"
    ):
        super().__init__(sdf_version)
        self.grasp_check = grasp_check
        self.gripper_links = gripper_links or []
        self.name = name
        self.palm_link = palm_link
        if self.grasp_check is not None and hasattr(self.grasp_check, 'to_version'):
            if getattr(self.grasp_check, '__version__', None) is None:
                self.grasp_check.__version__ = self.__version__
            elif getattr(self.grasp_check, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.grasp_check = self.grasp_check.to_version(self.__version__)

    def add_gripper_link(self, *items: str):
        if self.gripper_links is None:
            self.gripper_links = []
        self.gripper_links.extend(items)

    def to_version(self, target_version: str) -> "Gripper":
        kwargs = {"sdf_version": target_version}
        kwargs["grasp_check"] = self.grasp_check.to_version(target_version) if hasattr(self.grasp_check, "to_version") else self.grasp_check
        kwargs["gripper_links"] = self.gripper_links
        kwargs["name"] = self.name
        kwargs["palm_link"] = self.palm_link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("gripper")
        if self.grasp_check is not None:
            if hasattr(self.grasp_check, 'to_sdf'):
                _child_res = self.grasp_check.to_sdf(version)
            else:
                _child_res = str(self.grasp_check)
            if isinstance(_child_res, str):
                _item_el = ET.Element('grasp_check')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for _v in (self.gripper_links or []):
            _c_tmp = ET.Element("gripper_link")
            _c_tmp.text = _v
            el.append(_c_tmp)
        if self.name is not None:
            el.set("name", self.name)
        if self.palm_link is not None:
            _c_tmp = ET.Element("palm_link")
            _c_tmp.text = self.palm_link
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Gripper | SDFError":
        _c_grasp_check = el.find("grasp_check")
        if _c_grasp_check is not None:
            _res = cls.GraspCheck._from_sdf(_c_grasp_check, version)
            if isinstance(_res, SDFError):
                return _res.extend("grasp_check")
            _grasp_check = _res
        else:
            _grasp_check = None
        _gripper_links = []
        for c in el.findall("gripper_link"):
            _text = c.text if c.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("gripper_link")
            _gripper_links.append(_val)
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_tmp = el.find("palm_link")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("palm_link")
            _palm_link = _val
        else:
            _palm_link = None
        return cls(sdf_version=version, grasp_check=_grasp_check, gripper_links=_gripper_links, name=_name, palm_link=_palm_link)
