### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.joint_state import JointState
    from ..elements.link_state import LinkState
    from ..elements.pose import Pose


class ModelState(BaseModel):
    class ModelStateModelState(BaseModel):
        def __init__(self, sdf_version: str | None = None, name: str = "__default__"):
            super().__init__(sdf_version)
            self.name = name

        def to_version(self, target_version: str) -> "ModelState.ModelStateModelState":
            kwargs = {"sdf_version": target_version}
            kwargs["name"] = self.name
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("model_state")
            if self.name is not None:
                el.set("name", self.name)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "ModelState.ModelStateModelState | SDFError":
            _name = el.get("name", "__default__")
            if isinstance(_name, SDFError):
                return _name.extend("@name")
            return cls(sdf_version=version, name=_name)

    def __init__(
        self,
        sdf_version: str | None = None,
        frames: List["Frame"] = None,
        joint_states: List["JointState"] = None,
        link_states: List["LinkState"] = None,
        model_states: List["ModelState.ModelStateModelState"] = None,
        name: str = "__default__",
        pose: "Pose" = None,
        scale: _SDFVector3 = None
    ):
        super().__init__(sdf_version)
        if scale is None:
            scale = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
        self.frames = frames or []
        self.joint_states = joint_states or []
        self.link_states = link_states or []
        self.model_states = model_states or []
        self.name = name
        self.pose = pose
        self.scale = scale
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.joint_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.joint_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.link_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.link_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.model_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.model_states[_i] = _c.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_joint_state(self, *items: "JointState"):
        if self.joint_states is None:
            self.joint_states = []
        self.joint_states.extend(items)

    def add_link_state(self, *items: "LinkState"):
        if self.link_states is None:
            self.link_states = []
        self.link_states.extend(items)

    def add_model_state(self, *items: "ModelState.ModelStateModelState"):
        if self.model_states is None:
            self.model_states = []
        self.model_states.extend(items)

    def to_version(self, target_version: str) -> "ModelState":
        from ..elements.frame import Frame
        from ..elements.joint_state import JointState
        from ..elements.link_state import LinkState
        from ..elements.pose import Pose
        kwargs = {"sdf_version": target_version}
        kwargs["frames"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])]
        kwargs["joint_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joint_states or [])]
        kwargs["link_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.link_states or [])]
        kwargs["model_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.model_states or [])]
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
        kwargs["scale"] = self.scale
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.joint_state import JointState
        from ..elements.link_state import LinkState
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("model_state")
        for item in (self.frames or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.joint_states or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('joint_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.link_states or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('link_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.model_states or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('model_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            if hasattr(self.pose, 'to_sdf'):
                _child_res = self.pose.to_sdf(version)
            else:
                _child_res = str(self.pose)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.scale is not None:
            _c_tmp = ET.Element("scale")
            _c_tmp.text = self.scale.to_sdf(version)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "ModelState | SDFError":
        from ..elements.frame import Frame
        from ..elements.joint_state import JointState
        from ..elements.link_state import LinkState
        from ..elements.pose import Pose
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        _joint_states = []
        for c in el.findall("joint_state"):
            _res = JointState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint_state")
            _joint_states.append(_res)
        _link_states = []
        for c in el.findall("link_state"):
            _res = LinkState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link_state")
            _link_states.append(_res)
        _model_states = []
        for c in el.findall("model_state"):
            _res = cls.ModelStateModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_state")
            _model_states.append(_res)
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
        _c_tmp = el.find("scale")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _SDFVector3._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("scale")
            _scale = _val
        else:
            _scale = None
        return cls(sdf_version=version, frames=_frames, joint_states=_joint_states, link_states=_link_states, model_states=_model_states, name=_name, pose=_pose, scale=_scale)
