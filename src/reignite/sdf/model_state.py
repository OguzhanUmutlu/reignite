### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3

from .frame import Frame
from .joint_state import JointState
from .link_state import LinkState
from .pose import Pose


class ModelState(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        frame: List["Frame"] = None,
        joint_state: List["JointState"] = None,
        link_state: List["LinkState"] = None,
        model_state: List["ModelStateModelState"] = None,
        name: str = "__default__",
        pose: "Pose" = None,
        scale: "Scale" = None
    ):
        self.__version__ = sdf_version
        self.frame = frame or []
        self.joint_state = joint_state or []
        self.link_state = link_state or []
        self.model_state = model_state or []
        self.name = name
        self.pose = pose
        self.scale = scale

    def to_version(self, target_version: str) -> "ModelState":
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["joint_state"] = [c.to_version(target_version) for c in (self.joint_state or [])]
        kwargs["link_state"] = [c.to_version(target_version) for c in (self.link_state or [])]
        kwargs["model_state"] = [c.to_version(target_version) for c in (self.model_state or [])]
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("model_state")
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        for item in (self.joint_state or []):
            el.append(item.to_sdf(version))
        for item in (self.link_state or []):
            el.append(item.to_sdf(version))
        for item in (self.model_state or []):
            el.append(item.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        _joint_state = []
        for c in el.findall("joint_state"):
            _res = JointState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint_state")
            _joint_state.append(_res)
        _link_state = []
        for c in el.findall("link_state"):
            _res = LinkState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link_state")
            _link_state.append(_res)
        _model_state = []
        for c in el.findall("model_state"):
            _res = ModelStateModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_state")
            _model_state.append(_res)
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_scale = el.find("scale")
        if _c_scale is not None:
            _res = Scale._from_sdf(_c_scale, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale")
            _scale = _res
        else:
            _scale = None
        return cls(sdf_version=version, frame=_frame, joint_state=_joint_state, link_state=_link_state, model_state=_model_state, name=_name, pose=_pose, scale=_scale)


class ModelStateModelState(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "ModelStateModelState":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("model_state")
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, name=_name)


class Scale(BaseModel):
    def __init__(self, sdf_version: str, scale: _SDFVector3 = None):
        self.__version__ = sdf_version
        if scale is None:
            scale = _SDFVector3.from_sdf("1 1 1")
        self.scale = scale

    def to_version(self, target_version: str) -> "Scale":
        kwargs = {"sdf_version": target_version}
        kwargs["scale"] = self.scale
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = self.scale.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _scale = _SDFVector3._from_sdf(_text, version)
        if isinstance(_scale, SDFError):
            return _scale
        return cls(sdf_version=version, scale=_scale)
