### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_uint32
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.joint_state import JointState
    from ..elements.link_state import LinkState

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class ModelState(BaseModel):
    class Joint(BaseModel):
        class Angle(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                angle: float | None = None,
                axis: int | None = None
            ):
                super().__init__(sdf_version)
                self.angle = angle
                self.axis = axis

            def to_version(self, target_version: str) -> "ModelState.Joint.Angle":
                kwargs: dict = {"sdf_version": target_version, "angle": self.angle, "axis": self.axis}
                return ModelState.Joint.Angle(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("angle")
                if self.angle is not None:
                    el.text = str(self.angle)
                if self.axis is not None:
                    el.set("axis", str(self.axis))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "ModelState.Joint.Angle | SDFError":
                _raw_angle = el.text
                if _raw_angle is not None:
                    _angle = _parse_double(_raw_angle)
                    if isinstance(_angle, SDFError):
                        return _angle
                else:
                    _angle = None
                _raw_axis = el.get("axis")
                if _raw_axis is not None:
                    _axis = _parse_uint32(_raw_axis)
                    if isinstance(_axis, SDFError):
                        return _axis.extend("@axis")
                else:
                    _axis = None
                return cls(sdf_version=version, angle=_angle, axis=_axis)

        def __init__(
            self,
            sdf_version: str | None = None,
            angles: List["ModelState.Joint.Angle"] = None,
            name: str | None = None
        ):
            super().__init__(sdf_version)
            self.angles = angles or []
            self.name = name
            for _i, _c in enumerate(self.angles):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, 'sdfversion', None) is None:
                    _c.sdfversion = self.sdfversion
                elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.angles[_i] = _c.to_version(self.sdfversion)

        def add_angle(self, *items: "ModelState.Joint.Angle"):
            if self.angles is None:
                self.angles = []
            self.angles.extend(items)

        def to_version(self, target_version: str) -> "ModelState.Joint":
            kwargs: dict = {"sdf_version": target_version, "angles": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.angles or [])], "name": self.name}
            return ModelState.Joint(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("joint")
            for item in (self.angles or []):
                _child_res = item.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('angle')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.name is not None:
                el.set("name", self.name)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "ModelState.Joint | SDFError":
            _angles = []
            for c in el.findall("angle"):
                _res = cls.Angle._from_sdf(c, version)
                if isinstance(_res, SDFError):
                    return _res.extend("angle")
                _angles.append(_res)
            _raw_name = el.get("name")
            if _raw_name is not None:
                _name = _raw_name
                if isinstance(_name, SDFError):
                    return _name.extend("@name")
            else:
                _name = None
            return cls(sdf_version=version, angles=_angles, name=_name)

    def __init__(
        self,
        sdf_version: str | None = None,
        frames: List["Frame"] = None,
        joint_states: List["JointState"] = None,
        joints: List["ModelState.Joint"] = None,
        link_states: List["LinkState"] = None,
        links: List["LinkState"] = None,
        model_states: List["ModelState"] = None,
        models: List["ModelState"] = None,
        name: str | None = None,
        pose: _PoseT | None = None,
        scale: _Vector3T | None = None
    ):
        super().__init__(sdf_version)
        self.frames = frames or []
        self.joint_states = joint_states or []
        self.joints = joints or []
        self.link_states = link_states or []
        self.links = links or []
        self.model_states = model_states or []
        self.models = models or []
        self.name = name
        self.pose = _pose(pose) if pose is not None else None
        self.scale = _vector3(scale) if scale is not None else None
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.joint_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.joint_states[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.joints):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.joints[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.link_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.link_states[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.links):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.links[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.model_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.model_states[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.models):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.models[_i] = _c.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_joint_state(self, *items: "JointState"):
        if self.joint_states is None:
            self.joint_states = []
        self.joint_states.extend(items)

    def add_joint(self, *items: "ModelState.Joint"):
        if self.joints is None:
            self.joints = []
        self.joints.extend(items)

    def add_link_state(self, *items: "LinkState"):
        if self.link_states is None:
            self.link_states = []
        self.link_states.extend(items)

    def add_link(self, *items: "LinkState"):
        if self.links is None:
            self.links = []
        self.links.extend(items)

    def add_model_state(self, *items: "ModelState"):
        if self.model_states is None:
            self.model_states = []
        self.model_states.extend(items)

    def add_model(self, *items: "ModelState"):
        if self.models is None:
            self.models = []
        self.models.extend(items)

    def to_version(self, target_version: str) -> "ModelState":
        from ..elements.frame import Frame
        from ..elements.joint_state import JointState
        from ..elements.link_state import LinkState
        if self.joint_states and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'joint_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.joints and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'joints' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.link_states and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'link_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.links and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'links' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.model_states and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.models and cmp_version(target_version, "1.12") >= 0:
            raise ValueError(f"'models' is not supported in SDF version {target_version} (removed in 1.12)")
        if self.scale is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs: dict = {"sdf_version": target_version, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "joint_states": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joint_states or [])], "joints": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joints or [])], "link_states": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.link_states or [])], "links": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.links or [])], "model_states": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.model_states or [])], "models": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])], "name": self.name, "pose": self.pose, "scale": self.scale}
        return ModelState(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.joint_state import JointState
        from ..elements.link_state import LinkState
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("model_state")
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.joint_states or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('joint_state')
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
        for item in (self.link_states or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('link_state')
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
        for item in (self.model_states or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('model_state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.models or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('model')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            _c_tmp = ET.Element("pose")
            _c_tmp.text = str(self.pose)
            el.append(_c_tmp)
        if self.scale is not None:
            _c_tmp = ET.Element("scale")
            _c_tmp.text = str(self.scale)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "ModelState | SDFError":
        from ..elements.frame import Frame
        from ..elements.joint_state import JointState
        from ..elements.link_state import LinkState
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
        if _joint_states and cmp_version(version, "1.12") < 0:
            return SDFError(f"'joint_states' is not supported in SDF version {version} (added in 1.12)")
        _joints = []
        for c in el.findall("joint"):
            _res = cls.Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joints.append(_res)
        _link_states = []
        for c in el.findall("link_state"):
            _res = LinkState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link_state")
            _link_states.append(_res)
        if _link_states and cmp_version(version, "1.12") < 0:
            return SDFError(f"'link_states' is not supported in SDF version {version} (added in 1.12)")
        _links = []
        for c in el.findall("link"):
            _res = LinkState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link")
            _links.append(_res)
        _model_states = []
        for c in el.findall("model_state"):
            _res = ModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_state")
            _model_states.append(_res)
        if _model_states and cmp_version(version, "1.12") < 0:
            return SDFError(f"'model_states' is not supported in SDF version {version} (added in 1.12)")
        _models = []
        for c in el.findall("model"):
            _res = ModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _models.append(_res)
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        _c_tmp = el.find("pose")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 0 0 0"
            _val = _parse_pose(_text)
            if isinstance(_val, SDFError):
                return _val.extend("pose")
            _pose = _val
        else:
            _pose = None
        _c_tmp = el.find("scale")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("scale")
            _scale = _val
        else:
            _scale = None
        if _scale is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'scale' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, frames=_frames, joint_states=_joint_states, joints=_joints, link_states=_link_states, links=_links, model_states=_model_states, models=_models, name=_name, pose=_pose, scale=_scale)
