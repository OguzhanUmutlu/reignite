### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.migration import apply_migrations

if typing.TYPE_CHECKING:
    from ..elements.gripper import Gripper
    from ..elements.joint import Joint
    from ..elements.link import Link
    from ..elements.plugin import Plugin


class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(self, sdf_version: str | None = None, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
        self.pose = pose

    def to_version(self, target_version: str) -> "Pose":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf(version)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        return cls(sdf_version=version, pose=_pose)


class Robot(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        grippers: List["Gripper"] = None,
        joints: List["Joint"] = None,
        links: List["Link"] = None,
        name: str = "__default__",
        plugins: List["Plugin"] = None,
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.grippers = grippers or []
        self.joints = joints or []
        self.links = links or []
        self.name = name
        self.plugins = plugins or []
        self.pose = pose
        for _i, _c in enumerate(self.grippers):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.grippers[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.joints):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.joints[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.links):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.links[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.plugins):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.plugins[_i] = _c.to_version(self.__version__)
        if self.pose is not None:
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Robot":
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.plugin import Plugin
        kwargs = {"sdf_version": target_version}
        kwargs["grippers"] = [c.to_version(target_version) for c in (self.grippers or [])]
        kwargs["joints"] = [c.to_version(target_version) for c in (self.joints or [])]
        kwargs["links"] = [c.to_version(target_version) for c in (self.links or [])]
        kwargs["name"] = self.name
        kwargs["plugins"] = [c.to_version(target_version) for c in (self.plugins or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
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
            el.append(item.to_sdf(version))
        for item in (self.joints or []):
            el.append(item.to_sdf(version))
        for item in (self.links or []):
            el.append(item.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.plugins or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, grippers=_grippers, joints=_joints, links=_links, name=_name, plugins=_plugins, pose=_pose)
