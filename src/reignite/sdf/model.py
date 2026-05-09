### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version

from .frame import Frame
from .gripper import Gripper
from .joint import Joint
from .link import Link
from .model_state import ModelState
from .plugin import Plugin
from .pose import Pose


class AllowAutoDisable(BaseModel):
    def __init__(self, sdf_version: str, allow_auto_disable: bool = True):
        self.__version__ = sdf_version
        self.allow_auto_disable = allow_auto_disable

    def to_version(self, target_version: str) -> "AllowAutoDisable":
        if self.allow_auto_disable is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'allow_auto_disable' is not supported in SDF version {target_version} (added in 1.2)")
        if self.allow_auto_disable is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'allow_auto_disable' is not supported in SDF version {target_version} (removed in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["allow_auto_disable"] = self.allow_auto_disable
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("allow_auto_disable")
        if self.allow_auto_disable is not None:
            el.text = str(self.allow_auto_disable).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _allow_auto_disable = str(_text).strip().lower() == 'true'
        if isinstance(_allow_auto_disable, SDFError):
            return _allow_auto_disable
        if _allow_auto_disable is not None and cmp_version(version, "1.2") < 0:
            if _allow_auto_disable != True:
                return SDFError(f"'allow_auto_disable' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, allow_auto_disable=_allow_auto_disable)


class EnableWind(BaseModel):
    def __init__(self, sdf_version: str, enable_wind: bool = False):
        self.__version__ = sdf_version
        self.enable_wind = enable_wind

    def to_version(self, target_version: str) -> "EnableWind":
        if self.enable_wind is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_wind is not None and cmp_version(target_version, "1.8") >= 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (removed in 1.8)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_wind"] = self.enable_wind
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_wind")
        if self.enable_wind is not None:
            el.text = str(self.enable_wind).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _enable_wind = str(_text).strip().lower() == 'true'
        if isinstance(_enable_wind, SDFError):
            return _enable_wind
        if _enable_wind is not None and cmp_version(version, "1.7") < 0:
            if _enable_wind != False:
                return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, enable_wind=_enable_wind)


class Include(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        merge: bool = False,
        model_state: List["ModelState"] = None,
        name: "Name" = None,
        placement_frame: "PlacementFrame" = None,
        plugin: List["Plugin"] = None,
        pose: "Pose" = None,
        static: "Static" = None,
        uri: "Uri" = None
    ):
        self.__version__ = sdf_version
        self.merge = merge
        self.model_state = model_state or []
        self.name = name
        self.placement_frame = placement_frame
        self.plugin = plugin or []
        self.pose = pose
        self.static = static
        self.uri = uri

    def to_version(self, target_version: str) -> "Include":
        if self.merge is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'merge' is not supported in SDF version {target_version} (added in 1.12)")
        if self.model_state is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_state' is not supported in SDF version {target_version} (added in 1.12)")
        if self.placement_frame is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["merge"] = self.merge
        kwargs["model_state"] = [c.to_version(target_version) for c in (self.model_state or [])]
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["placement_frame"] = self.placement_frame.to_version(target_version) if self.placement_frame is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["static"] = self.static.to_version(target_version) if self.static is not None else None
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("include")
        if self.merge is not None:
            el.set("merge", str(self.merge).lower())
        for item in (self.model_state or []):
            el.append(item.to_sdf(version))
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        if self.placement_frame is not None:
            el.append(self.placement_frame.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.static is not None:
            el.append(self.static.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _merge = str(el.get("merge", False)).strip().lower() == 'true'
        if isinstance(_merge, SDFError):
            return _merge.extend("@merge")
        if _merge is not None and cmp_version(version, "1.12") < 0:
            if _merge != False:
                return SDFError(f"'merge' is not supported in SDF version {version} (added in 1.12)")
        _model_state = []
        for c in el.findall("model_state"):
            _res = ModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_state")
            _model_state.append(_res)
        if _model_state and cmp_version(version, "1.12") < 0:
            return SDFError(f"'model_state' is not supported in SDF version {version} (added in 1.12)")
        _c_name = el.find("name")
        if _c_name is not None:
            _res = Name._from_sdf(_c_name, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _name = _res
        else:
            _name = None
        _c_placement_frame = el.find("placement_frame")
        if _c_placement_frame is not None:
            _res = PlacementFrame._from_sdf(_c_placement_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("placement_frame")
            _placement_frame = _res
        else:
            _placement_frame = None
        if _placement_frame is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'placement_frame' is not supported in SDF version {version} (added in 1.12)")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_static = el.find("static")
        if _c_static is not None:
            _res = Static._from_sdf(_c_static, version)
            if isinstance(_res, SDFError):
                return _res.extend("static")
            _static = _res
        else:
            _static = None
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        return cls(sdf_version=version, merge=_merge, model_state=_model_state, name=_name, placement_frame=_placement_frame, plugin=_plugin, pose=_pose, static=_static, uri=_uri)


class Model(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        allow_auto_disable: "AllowAutoDisable" = None,
        canonical_link: str = "",
        enable_wind: "EnableWind" = None,
        frame: List["Frame"] = None,
        gripper: List["Gripper"] = None,
        include: List["Include"] = None,
        joint: List["Joint"] = None,
        link: List["Link"] = None,
        model: List["ModelModel"] = None,
        model_state: List["ModelState"] = None,
        name: str = "__default__",
        origin: "Origin" = None,
        placement_frame: str = "",
        plugin: List["Plugin"] = None,
        pose: "Pose" = None,
        scale: "Scale" = None,
        self_collide: "SelfCollide" = None,
        static: bool = False
    ):
        self.__version__ = sdf_version
        self.allow_auto_disable = allow_auto_disable
        self.canonical_link = canonical_link
        self.enable_wind = enable_wind
        self.frame = frame or []
        self.gripper = gripper or []
        self.include = include or []
        self.joint = joint or []
        self.link = link or []
        self.model = model or []
        self.model_state = model_state or []
        self.name = name
        self.origin = origin
        self.placement_frame = placement_frame
        self.plugin = plugin or []
        self.pose = pose
        self.scale = scale
        self.self_collide = self_collide
        self.static = static

    def to_version(self, target_version: str) -> "Model":
        if self.allow_auto_disable is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'allow_auto_disable' is not supported in SDF version {target_version} (added in 1.2)")
        if self.allow_auto_disable is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'allow_auto_disable' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.canonical_link is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'canonical_link' is not supported in SDF version {target_version} (added in 1.7)")
        if self.canonical_link is not None and cmp_version(target_version, "1.8") >= 0:
            raise ValueError(f"'canonical_link' is not supported in SDF version {target_version} (removed in 1.8)")
        if self.enable_wind is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_wind is not None and cmp_version(target_version, "1.8") >= 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (removed in 1.8)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.gripper is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'gripper' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.include is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'include' is not supported in SDF version {target_version} (added in 1.7)")
        if self.include is not None and cmp_version(target_version, "1.8") >= 0:
            raise ValueError(f"'include' is not supported in SDF version {target_version} (removed in 1.8)")
        if self.model is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'model' is not supported in SDF version {target_version} (added in 1.5)")
        if self.model_state is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_state' is not supported in SDF version {target_version} (added in 1.12)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.placement_frame is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.12)")
        if self.plugin is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'plugin' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.scale is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.6)")
        if self.scale is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.self_collide is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (added in 1.7)")
        if self.self_collide is not None and cmp_version(target_version, "1.8") >= 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (removed in 1.8)")
        if self.static is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["allow_auto_disable"] = self.allow_auto_disable.to_version(target_version) if self.allow_auto_disable is not None else None
        kwargs["canonical_link"] = self.canonical_link
        kwargs["enable_wind"] = self.enable_wind.to_version(target_version) if self.enable_wind is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["gripper"] = [c.to_version(target_version) for c in (self.gripper or [])]
        kwargs["include"] = [c.to_version(target_version) for c in (self.include or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        kwargs["link"] = [c.to_version(target_version) for c in (self.link or [])]
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["model_state"] = [c.to_version(target_version) for c in (self.model_state or [])]
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["placement_frame"] = self.placement_frame
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        kwargs["self_collide"] = self.self_collide.to_version(target_version) if self.self_collide is not None else None
        kwargs["static"] = self.static
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("model")
        if self.allow_auto_disable is not None:
            el.append(self.allow_auto_disable.to_sdf(version))
        if self.canonical_link is not None:
            el.set("canonical_link", self.canonical_link)
        if self.enable_wind is not None:
            el.append(self.enable_wind.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        for item in (self.gripper or []):
            el.append(item.to_sdf(version))
        for item in (self.include or []):
            el.append(item.to_sdf(version))
        for item in (self.joint or []):
            el.append(item.to_sdf(version))
        for item in (self.link or []):
            el.append(item.to_sdf(version))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        for item in (self.model_state or []):
            el.append(item.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.placement_frame is not None:
            el.set("placement_frame", self.placement_frame)
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf(version))
        if self.static is not None:
            el.set("static", str(self.static).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_allow_auto_disable = el.find("allow_auto_disable")
        if _c_allow_auto_disable is not None:
            _res = AllowAutoDisable._from_sdf(_c_allow_auto_disable, version)
            if isinstance(_res, SDFError):
                return _res.extend("allow_auto_disable")
            _allow_auto_disable = _res
        else:
            _allow_auto_disable = None
        if _allow_auto_disable is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'allow_auto_disable' is not supported in SDF version {version} (added in 1.2)")
        _canonical_link = el.get("canonical_link", "")
        if isinstance(_canonical_link, SDFError):
            return _canonical_link.extend("@canonical_link")
        if _canonical_link is not None and cmp_version(version, "1.7") < 0:
            if _canonical_link != "":
                return SDFError(f"'canonical_link' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_wind = el.find("enable_wind")
        if _c_enable_wind is not None:
            _res = EnableWind._from_sdf(_c_enable_wind, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_wind")
            _enable_wind = _res
        else:
            _enable_wind = None
        if _enable_wind is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.7)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _gripper = []
        for c in el.findall("gripper"):
            _res = Gripper._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("gripper")
            _gripper.append(_res)
        _include = []
        for c in el.findall("include"):
            _res = Include._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("include")
            _include.append(_res)
        if _include and cmp_version(version, "1.7") < 0:
            return SDFError(f"'include' is not supported in SDF version {version} (added in 1.7)")
        _joint = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joint.append(_res)
        _link = []
        for c in el.findall("link"):
            _res = Link._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("link")
            _link.append(_res)
        _model = []
        for c in el.findall("model"):
            _res = ModelModel._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _model.append(_res)
        if _model and cmp_version(version, "1.5") < 0:
            return SDFError(f"'model' is not supported in SDF version {version} (added in 1.5)")
        _model_state = []
        for c in el.findall("model_state"):
            _res = ModelState._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_state")
            _model_state.append(_res)
        if _model_state and cmp_version(version, "1.12") < 0:
            return SDFError(f"'model_state' is not supported in SDF version {version} (added in 1.12)")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
        _placement_frame = el.get("placement_frame", "")
        if isinstance(_placement_frame, SDFError):
            return _placement_frame.extend("@placement_frame")
        if _placement_frame is not None and cmp_version(version, "1.12") < 0:
            if _placement_frame != "":
                return SDFError(f"'placement_frame' is not supported in SDF version {version} (added in 1.12)")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _c_scale = el.find("scale")
        if _c_scale is not None:
            _res = Scale._from_sdf(_c_scale, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale")
            _scale = _res
        else:
            _scale = None
        if _scale is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'scale' is not supported in SDF version {version} (added in 1.6)")
        _c_self_collide = el.find("self_collide")
        if _c_self_collide is not None:
            _res = SelfCollide._from_sdf(_c_self_collide, version)
            if isinstance(_res, SDFError):
                return _res.extend("self_collide")
            _self_collide = _res
        else:
            _self_collide = None
        if _self_collide is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'self_collide' is not supported in SDF version {version} (added in 1.7)")
        _static = str(el.get("static", False)).strip().lower() == 'true'
        if isinstance(_static, SDFError):
            return _static.extend("@static")
        return cls(sdf_version=version, allow_auto_disable=_allow_auto_disable, canonical_link=_canonical_link, enable_wind=_enable_wind, frame=_frame, gripper=_gripper, include=_include, joint=_joint, link=_link, model=_model, model_state=_model_state, name=_name, origin=_origin, placement_frame=_placement_frame, plugin=_plugin, pose=_pose, scale=_scale, self_collide=_self_collide, static=_static)


class ModelModel(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "ModelModel":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("model")
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, name=_name)


class Name(BaseModel):
    def __init__(self, sdf_version: str, name: str = ""):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "Name":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _name = _text
        if isinstance(_name, SDFError):
            return _name
        return cls(sdf_version=version, name=_name)


class Origin(BaseModel):
    def __init__(self, sdf_version: str, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "Origin":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("origin")
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _pose = _SDFPose._from_sdf(el.get("pose", "0 0 0 0 0 0"), version)
        if isinstance(_pose, SDFError):
            return _pose.extend("@pose")
        return cls(sdf_version=version, pose=_pose)


class PlacementFrame(BaseModel):
    def __init__(self, sdf_version: str, placement_frame: str = ""):
        self.__version__ = sdf_version
        self.placement_frame = placement_frame

    def to_version(self, target_version: str) -> "PlacementFrame":
        if self.placement_frame is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["placement_frame"] = self.placement_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("placement_frame")
        if self.placement_frame is not None:
            el.text = self.placement_frame
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _placement_frame = _text
        if isinstance(_placement_frame, SDFError):
            return _placement_frame
        if _placement_frame is not None and cmp_version(version, "1.12") < 0:
            if _placement_frame != "":
                return SDFError(f"'placement_frame' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, placement_frame=_placement_frame)


class Scale(BaseModel):
    def __init__(self, sdf_version: str, scale: _SDFVector3 = None):
        self.__version__ = sdf_version
        if scale is None:
            scale = _SDFVector3.from_sdf("1 1 1")
        self.scale = scale

    def to_version(self, target_version: str) -> "Scale":
        if self.scale is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.6)")
        if self.scale is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (removed in 1.7)")
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
        if _scale is not None and cmp_version(version, "1.6") < 0:
            if _scale != "1 1 1":
                return SDFError(f"'scale' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, scale=_scale)


class SelfCollide(BaseModel):
    def __init__(self, sdf_version: str, self_collide: bool = False):
        self.__version__ = sdf_version
        self.self_collide = self_collide

    def to_version(self, target_version: str) -> "SelfCollide":
        if self.self_collide is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (added in 1.7)")
        if self.self_collide is not None and cmp_version(target_version, "1.8") >= 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (removed in 1.8)")
        kwargs = {"sdf_version": target_version}
        kwargs["self_collide"] = self.self_collide
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("self_collide")
        if self.self_collide is not None:
            el.text = str(self.self_collide).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _self_collide = str(_text).strip().lower() == 'true'
        if isinstance(_self_collide, SDFError):
            return _self_collide
        if _self_collide is not None and cmp_version(version, "1.7") < 0:
            if _self_collide != False:
                return SDFError(f"'self_collide' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, self_collide=_self_collide)


class Static(BaseModel):
    def __init__(self, sdf_version: str, static: bool = False):
        self.__version__ = sdf_version
        self.static = static

    def to_version(self, target_version: str) -> "Static":
        if self.static is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.2)")
        if self.static is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (removed in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["static"] = self.static
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("static")
        if self.static is not None:
            el.text = str(self.static).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _static = str(_text).strip().lower() == 'true'
        if isinstance(_static, SDFError):
            return _static
        if _static is not None and cmp_version(version, "1.2") < 0:
            if _static != False:
                return SDFError(f"'static' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, static=_static)


class Uri(BaseModel):
    def __init__(self, sdf_version: str, uri: str = "__default__"):
        self.__version__ = sdf_version
        self.uri = uri

    def to_version(self, target_version: str) -> "Uri":
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("uri")
        if self.uri is not None:
            el.text = self.uri
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _uri = _text
        if isinstance(_uri, SDFError):
            return _uri
        return cls(sdf_version=version, uri=_uri)
