### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.gripper import Gripper
    from ..elements.joint import Joint
    from ..elements.link import Link
    from ..elements.model_state import ModelState
    from ..elements.plugin import Plugin
    from ..elements.pose import Pose


class Model(BaseModel):
    class Include(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            merge: bool = False,
            model_states: List["ModelState"] = None,
            name: str = "",
            placement_frame: str = "",
            plugins: List["Plugin"] = None,
            pose: "Pose" = None,
            static: bool = False,
            uri: str = "__default__"
        ):
            super().__init__(sdf_version)
            self.merge = merge
            self.model_states = model_states or []
            self.name = name
            self.placement_frame = placement_frame
            self.plugins = plugins or []
            self.pose = pose
            self.static = static
            self.uri = uri
            for _i, _c in enumerate(self.model_states):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, '__version__', None) is None:
                    _c.__version__ = self.__version__
                elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.model_states[_i] = _c.to_version(self.__version__)
            for _i, _c in enumerate(self.plugins):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, '__version__', None) is None:
                    _c.__version__ = self.__version__
                elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.plugins[_i] = _c.to_version(self.__version__)
            if self.pose is not None and hasattr(self.pose, 'to_version'):
                if getattr(self.pose, '__version__', None) is None:
                    self.pose.__version__ = self.__version__
                elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.pose = self.pose.to_version(self.__version__)

        def add_model_state(self, *items: "ModelState"):
            if self.model_states is None:
                self.model_states = []
            self.model_states.extend(items)

        def add_plugin(self, *items: "Plugin"):
            if self.plugins is None:
                self.plugins = []
            self.plugins.extend(items)

        def to_version(self, target_version: str) -> "Model.Include":
            from ..elements.model_state import ModelState
            from ..elements.plugin import Plugin
            from ..elements.pose import Pose
            if self.merge is not None and cmp_version(target_version, "1.12") < 0:
                raise ValueError(f"'merge' is not supported in SDF version {target_version} (added in 1.12)")
            if self.model_states is not None and cmp_version(target_version, "1.12") < 0:
                raise ValueError(f"'model_states' is not supported in SDF version {target_version} (added in 1.12)")
            if self.placement_frame is not None and cmp_version(target_version, "1.12") < 0:
                raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.12)")
            kwargs = {"sdf_version": target_version}
            kwargs["merge"] = self.merge
            kwargs["model_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.model_states or [])]
            kwargs["name"] = self.name
            kwargs["placement_frame"] = self.placement_frame
            kwargs["plugins"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])]
            kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
            kwargs["static"] = self.static
            kwargs["uri"] = self.uri
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.model_state import ModelState
            from ..elements.plugin import Plugin
            from ..elements.pose import Pose
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("include")
            if self.merge is not None:
                el.set("merge", str(self.merge).lower())
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
                _c_tmp = ET.Element("name")
                _c_tmp.text = self.name
                el.append(_c_tmp)
            if self.placement_frame is not None:
                _c_tmp = ET.Element("placement_frame")
                _c_tmp.text = self.placement_frame
                el.append(_c_tmp)
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
            if self.static is not None:
                _c_tmp = ET.Element("static")
                _c_tmp.text = str(self.static).lower()
                el.append(_c_tmp)
            if self.uri is not None:
                _c_tmp = ET.Element("uri")
                _c_tmp.text = self.uri
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Model.Include | SDFError":
            from ..elements.model_state import ModelState
            from ..elements.plugin import Plugin
            from ..elements.pose import Pose
            _merge = str(el.get("merge", False)).strip().lower() == 'true'
            if isinstance(_merge, SDFError):
                return _merge.extend("@merge")
            if _merge is not None and cmp_version(version, "1.12") < 0:
                if _merge != False:
                    return SDFError(f"'merge' is not supported in SDF version {version} (added in 1.12)")
            _model_states = []
            for c in el.findall("model_state"):
                _res = ModelState._from_sdf(c, version)
                if isinstance(_res, SDFError):
                    return _res.extend("model_state")
                _model_states.append(_res)
            if _model_states and cmp_version(version, "1.12") < 0:
                return SDFError(f"'model_states' is not supported in SDF version {version} (added in 1.12)")
            _c_tmp = el.find("name")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else ""
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("name")
                _name = _val
            else:
                _name = None
            _c_tmp = el.find("placement_frame")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else ""
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("placement_frame")
                _placement_frame = _val
            else:
                _placement_frame = None
            if _placement_frame is not None and cmp_version(version, "1.12") < 0:
                return SDFError(f"'placement_frame' is not supported in SDF version {version} (added in 1.12)")
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
            _c_tmp = el.find("static")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else False
                _val = str(_text).strip().lower() == 'true'
                if isinstance(_val, SDFError):
                    return _val.extend("static")
                _static = _val
            else:
                _static = None
            _c_tmp = el.find("uri")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("uri")
                _uri = _val
            else:
                _uri = None
            return cls(sdf_version=version, merge=_merge, model_states=_model_states, name=_name, placement_frame=_placement_frame, plugins=_plugins, pose=_pose, static=_static, uri=_uri)

    class ModelModel(BaseModel):
        def __init__(self, sdf_version: str | None = None, name: str = "__default__"):
            super().__init__(sdf_version)
            self.name = name

        def to_version(self, target_version: str) -> "Model.ModelModel":
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
            el = ET.Element("model")
            if self.name is not None:
                el.set("name", self.name)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Model.ModelModel | SDFError":
            _name = el.get("name", "__default__")
            if isinstance(_name, SDFError):
                return _name.extend("@name")
            return cls(sdf_version=version, name=_name)

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _SDFPose = None):
            super().__init__(sdf_version)
            if pose is None:
                pose = _SDFPose.from_sdf("0 0 0 0 0 0", version=sdf_version)
            self.pose = pose

        def to_version(self, target_version: str) -> "Model.Origin":
            kwargs = {"sdf_version": target_version}
            kwargs["pose"] = self.pose
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("origin")
            if self.pose is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("pose")
                    _c_tmp.text = self.pose.to_sdf(version)
                    el.append(_c_tmp)
                else:
                    el.set("pose", self.pose.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Model.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is None: _raw_pose = "0 0 0 0 0 0"
            _pose = _SDFPose._from_sdf(_raw_pose, version)
            if isinstance(_pose, SDFError):
                return _pose.extend("@pose")
            return cls(sdf_version=version, pose=_pose)

    def __init__(
        self,
        sdf_version: str | None = None,
        allow_auto_disable: bool = True,
        canonical_link: str = "",
        enable_wind: bool = False,
        frames: List["Frame"] = None,
        grippers: List["Gripper"] = None,
        includes: List["Model.Include"] = None,
        joints: List["Joint"] = None,
        links: List["Link"] = None,
        model_states: List["ModelState"] = None,
        models: List["Model.ModelModel"] = None,
        name: str = "__default__",
        origin: "Model.Origin" = None,
        placement_frame: str = "",
        plugins: List["Plugin"] = None,
        pose: "Pose" = None,
        scale: _SDFVector3 = None,
        self_collide: bool = False,
        static: bool = False
    ):
        super().__init__(sdf_version)
        if scale is None:
            scale = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
        self.allow_auto_disable = allow_auto_disable
        self.canonical_link = canonical_link
        self.enable_wind = enable_wind
        self.frames = frames or []
        self.grippers = grippers or []
        self.includes = includes or []
        self.joints = joints or []
        self.links = links or []
        self.model_states = model_states or []
        self.models = models or []
        self.name = name
        self.origin = origin
        self.placement_frame = placement_frame
        self.plugins = plugins or []
        self.pose = pose
        self.scale = scale
        self.self_collide = self_collide
        self.static = static
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.grippers):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.grippers[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.includes):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.includes[_i] = _c.to_version(self.__version__)
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
        for _i, _c in enumerate(self.model_states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.model_states[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.models):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.models[_i] = _c.to_version(self.__version__)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, '__version__', None) is None:
                self.origin.__version__ = self.__version__
            elif getattr(self.origin, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.origin = self.origin.to_version(self.__version__)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.plugins[_i] = _c.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_gripper(self, *items: "Gripper"):
        if self.grippers is None:
            self.grippers = []
        self.grippers.extend(items)

    def add_include(self, *items: "Model.Include"):
        if self.includes is None:
            self.includes = []
        self.includes.extend(items)

    def add_joint(self, *items: "Joint"):
        if self.joints is None:
            self.joints = []
        self.joints.extend(items)

    def add_link(self, *items: "Link"):
        if self.links is None:
            self.links = []
        self.links.extend(items)

    def add_model_state(self, *items: "ModelState"):
        if self.model_states is None:
            self.model_states = []
        self.model_states.extend(items)

    def add_model(self, *items: "Model.ModelModel"):
        if self.models is None:
            self.models = []
        self.models.extend(items)

    def add_plugin(self, *items: "Plugin"):
        if self.plugins is None:
            self.plugins = []
        self.plugins.extend(items)

    def to_version(self, target_version: str) -> "Model":
        from ..elements.frame import Frame
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.model_state import ModelState
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
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
        if self.frames is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.grippers is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'grippers' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.includes is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'includes' is not supported in SDF version {target_version} (added in 1.7)")
        if self.includes is not None and cmp_version(target_version, "1.8") >= 0:
            raise ValueError(f"'includes' is not supported in SDF version {target_version} (removed in 1.8)")
        if self.model_states is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.models is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'models' is not supported in SDF version {target_version} (added in 1.5)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.placement_frame is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.12)")
        if self.plugins is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'plugins' is not supported in SDF version {target_version} (removed in 1.5)")
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
        kwargs["allow_auto_disable"] = self.allow_auto_disable
        kwargs["canonical_link"] = self.canonical_link
        kwargs["enable_wind"] = self.enable_wind
        kwargs["frames"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])]
        kwargs["grippers"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.grippers or [])]
        kwargs["includes"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.includes or [])]
        kwargs["joints"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joints or [])]
        kwargs["links"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.links or [])]
        kwargs["model_states"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.model_states or [])]
        kwargs["models"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])]
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if hasattr(self.origin, "to_version") else self.origin
        kwargs["placement_frame"] = self.placement_frame
        kwargs["plugins"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
        kwargs["scale"] = self.scale
        kwargs["self_collide"] = self.self_collide
        kwargs["static"] = self.static
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.model_state import ModelState
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("model")
        if self.allow_auto_disable is not None:
            _c_tmp = ET.Element("allow_auto_disable")
            _c_tmp.text = str(self.allow_auto_disable).lower()
            el.append(_c_tmp)
        if self.canonical_link is not None:
            el.set("canonical_link", self.canonical_link)
        if self.enable_wind is not None:
            _c_tmp = ET.Element("enable_wind")
            _c_tmp.text = str(self.enable_wind).lower()
            el.append(_c_tmp)
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
        for item in (self.includes or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('include')
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
        for item in (self.models or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('model')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            if hasattr(self.origin, 'to_sdf'):
                _child_res = self.origin.to_sdf(version)
            else:
                _child_res = str(self.origin)
            if isinstance(_child_res, str):
                _item_el = ET.Element('origin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.placement_frame is not None:
            el.set("placement_frame", self.placement_frame)
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
        if self.self_collide is not None:
            _c_tmp = ET.Element("self_collide")
            _c_tmp.text = str(self.self_collide).lower()
            el.append(_c_tmp)
        if self.static is not None:
            el.set("static", str(self.static).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Model | SDFError":
        from ..elements.frame import Frame
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.model_state import ModelState
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        _c_tmp = el.find("allow_auto_disable")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else True
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("allow_auto_disable")
            _allow_auto_disable = _val
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
        _c_tmp = el.find("enable_wind")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("enable_wind")
            _enable_wind = _val
        else:
            _enable_wind = None
        if _enable_wind is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.7)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _grippers = []
        for c in el.findall("gripper"):
            _res = Gripper._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("gripper")
            _grippers.append(_res)
        _includes = []
        for c in el.findall("include"):
            _res = cls.Include._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("include")
            _includes.append(_res)
        if _includes and cmp_version(version, "1.7") < 0:
            return SDFError(f"'includes' is not supported in SDF version {version} (added in 1.7)")
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
            _res = cls.ModelModel._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _models.append(_res)
        if _models and cmp_version(version, "1.5") < 0:
            return SDFError(f"'models' is not supported in SDF version {version} (added in 1.5)")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = cls.Origin._from_sdf(_c_origin, version)
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
        if _pose is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _c_tmp = el.find("scale")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _SDFVector3._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("scale")
            _scale = _val
        else:
            _scale = None
        if _scale is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'scale' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("self_collide")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("self_collide")
            _self_collide = _val
        else:
            _self_collide = None
        if _self_collide is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'self_collide' is not supported in SDF version {version} (added in 1.7)")
        _static = str(el.get("static", False)).strip().lower() == 'true'
        if isinstance(_static, SDFError):
            return _static.extend("@static")
        return cls(sdf_version=version, allow_auto_disable=_allow_auto_disable, canonical_link=_canonical_link, enable_wind=_enable_wind, frames=_frames, grippers=_grippers, includes=_includes, joints=_joints, links=_links, model_states=_model_states, models=_models, name=_name, origin=_origin, placement_frame=_placement_frame, plugins=_plugins, pose=_pose, scale=_scale, self_collide=_self_collide, static=_static)
