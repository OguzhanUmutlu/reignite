### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose

if typing.TYPE_CHECKING:
    from ..elements.gripper import Gripper
    from ..elements.joint import Joint
    from ..elements.link import Link
    from ..elements.plugin import Plugin

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Robot(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        grippers: List["Gripper"] = None,
        joints: List["Joint"] = None,
        links: List["Link"] = None,
        name: str | None = "__default__",
        plugins: List["Plugin"] = None,
        pose: _PoseT | None = None
    ):
        super().__init__(sdf_version)
        self.grippers = grippers or []
        self.joints = joints or []
        self.links = links or []
        self.name = name if name is not None else "__default__"
        self.plugins = plugins or []
        self.pose = _pose("0 0 0 0 0 0") if pose is None else _pose(pose)
        for _i, _c in enumerate(self.grippers):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.grippers[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.joints):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.joints[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.links):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.links[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.plugins[_i] = _c.to_version(self.sdfversion)

    def add_gripper(self, *items: "Gripper"):
        if self.grippers is None:
            self.grippers = []
        self.grippers.extend(items)

    def add_joint(self, *items: "Joint"):
        if self.joints is None:
            self.joints = []
        self.joints.extend(items)

    def add_link(self, *items: "Link"):
        if self.links is None:
            self.links = []
        self.links.extend(items)

    def add_plugin(self, *items: "Plugin"):
        if self.plugins is None:
            self.plugins = []
        self.plugins.extend(items)

    def to_version(self, target_version: str) -> "Robot":
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.plugin import Plugin
        kwargs: dict = {"sdf_version": target_version, "grippers": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.grippers or [])], "joints": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joints or [])], "links": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.links or [])], "name": self.name, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])], "pose": self.pose}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.plugin import Plugin
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("robot")
        for item in (self.grippers or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('gripper')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.joints or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('joint')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.links or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('link')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.plugins or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = str(self.pose)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Robot | SDFError":
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.plugin import Plugin
        _grippers = []
        for c in el.findall("gripper"):
            _res = Gripper._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("gripper")
            _grippers.append(_res)
        _joints = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joints.append(_res)
        _links = []
        for c in el.findall("link"):
            _res = Link._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link")
            _links.append(_res)
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _plugins = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugins.append(_res)
        _c_tmp = el.find("pose")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text)
            if isinstance(_val, SDFError):
                return _val.extend("pose")
            _pose = _val
        else:
            _pose = None
        return cls(sdf_version=version, grippers=_grippers, joints=_joints, links=_links, name=_name, plugins=_plugins, pose=_pose)
