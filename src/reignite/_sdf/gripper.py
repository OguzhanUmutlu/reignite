### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_int32, _parse_uint32
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


# noinspection PyUnusedImports
class Gripper(BaseModel):
    class GraspCheck(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            attach_steps: int | None = None,
            detach_steps: int | None = None,
            min_contact_count: int | None = None
        ):
            super().__init__(sdf_version)
            self.attach_steps = attach_steps
            self.detach_steps = detach_steps
            self.min_contact_count = min_contact_count

        def to_version(self, target_version: str) -> "Gripper.GraspCheck":
            kwargs: dict = {"sdf_version": target_version, "attach_steps": self.attach_steps, "detach_steps": self.detach_steps, "min_contact_count": self.min_contact_count}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("grasp_check")
            if self.attach_steps is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("attach_steps")
                    _c_tmp.text = str(self.attach_steps)
                    el.append(_c_tmp)
                else:
                    el.set("attach_steps", str(self.attach_steps))
            if self.detach_steps is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("detach_steps")
                    _c_tmp.text = str(self.detach_steps)
                    el.append(_c_tmp)
                else:
                    el.set("detach_steps", str(self.detach_steps))
            if self.min_contact_count is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("min_contact_count")
                    _c_tmp.text = str(self.min_contact_count)
                    el.append(_c_tmp)
                else:
                    el.set("min_contact_count", str(self.min_contact_count))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Gripper.GraspCheck | SDFError":
            _raw_attach_steps = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("attach_steps")
                if _c_tmp is not None: _raw_attach_steps = _c_tmp.text
            else:
                _raw_attach_steps = el.get("attach_steps")
            if _raw_attach_steps is not None:
                _attach_steps = _parse_int32(_raw_attach_steps)
                if isinstance(_attach_steps, SDFError):
                    return _attach_steps.extend("@attach_steps")
            else:
                _attach_steps = None
            _raw_detach_steps = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("detach_steps")
                if _c_tmp is not None: _raw_detach_steps = _c_tmp.text
            else:
                _raw_detach_steps = el.get("detach_steps")
            if _raw_detach_steps is not None:
                _detach_steps = _parse_int32(_raw_detach_steps)
                if isinstance(_detach_steps, SDFError):
                    return _detach_steps.extend("@detach_steps")
            else:
                _detach_steps = None
            _raw_min_contact_count = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("min_contact_count")
                if _c_tmp is not None: _raw_min_contact_count = _c_tmp.text
            else:
                _raw_min_contact_count = el.get("min_contact_count")
            if _raw_min_contact_count is not None:
                _min_contact_count = _parse_uint32(_raw_min_contact_count)
                if isinstance(_min_contact_count, SDFError):
                    return _min_contact_count.extend("@min_contact_count")
            else:
                _min_contact_count = None
            return cls(sdf_version=version, attach_steps=_attach_steps, detach_steps=_detach_steps, min_contact_count=_min_contact_count)

    def __init__(
        self,
        sdf_version: str | None = None,
        grasp_check: "Gripper.GraspCheck" = None,
        gripper_links: List[str] | None = None,
        name: str | None = None,
        palm_link: str | None = None
    ):
        super().__init__(sdf_version)
        self.grasp_check = grasp_check
        self.gripper_links = gripper_links or []
        self.name = name
        self.palm_link = palm_link
        if self.grasp_check is not None and hasattr(self.grasp_check, 'to_version'):
            if getattr(self.grasp_check, 'sdfversion', None) is None:
                self.grasp_check.sdfversion = self.sdfversion
            elif getattr(self.grasp_check, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.grasp_check = self.grasp_check.to_version(self.sdfversion)

    def add_gripper_link(self, *items: str):
        if self.gripper_links is None:
            self.gripper_links = []
        self.gripper_links.extend(items)

    def to_version(self, target_version: str) -> "Gripper":
        kwargs: dict = {"sdf_version": target_version, "grasp_check": self.grasp_check.to_version(target_version) if self.grasp_check is not None and hasattr(self.grasp_check, "to_version") else self.grasp_check, "gripper_links": self.gripper_links, "name": self.name, "palm_link": self.palm_link}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("gripper")
        if self.grasp_check is not None:
            _child_res = self.grasp_check.to_sdf(version)
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
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
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
