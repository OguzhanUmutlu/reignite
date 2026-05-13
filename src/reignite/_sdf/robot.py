### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose

if typing.TYPE_CHECKING:
    from ..elements.gripper import Gripper
    from ..elements.joint import Joint
    from ..elements.link import Link
    from ..elements.plugin import Plugin


class Robot(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        grippers: List["Gripper"] = None,
        joints: List["Joint"] = None,
        links: List["Link"] = None,
        name: str = "__default__",
        plugins: List["Plugin"] = None,
        pose: _SDFPose = None
    ):
        super().__init__(sdf_version)
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        self.grippers = grippers or []
        self.joints = joints or []
        self.links = links or []
        self.name = name
        self.plugins = plugins or []
        self.pose = pose
        for _i, _c in enumerate(self.grippers):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.grippers[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.joints):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.joints[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.links):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.links[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.plugins[_i] = _c.to_version(self.__version__)

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
        kwargs = {"sdf_version": target_version}
        kwargs["grippers"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.grippers or [])]
        kwargs["joints"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joints or [])]
        kwargs["links"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.links or [])]
        kwargs["name"] = self.name
        kwargs["plugins"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])]
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.plugin import Plugin
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("robot")
        for item in (self.grippers or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('gripper')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.joints or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('joint')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.links or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('link')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.plugins or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = self.pose.to_sdf(version)
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
            _val = _SDFPose._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("pose")
            _pose = _val
        else:
            _pose = None
        return cls(sdf_version=version, grippers=_grippers, joints=_joints, links=_links, name=_name, plugins=_plugins, pose=_pose)
