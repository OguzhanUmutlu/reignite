### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.gripper import Gripper
    from ..elements.joint import Joint
    from ..elements.link import Link
    from ..elements.model_state import ModelState
    from ..elements.plugin import Plugin
    from ..elements.pose import Pose

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Model(BaseModel):
    class Include(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            merge: bool | None = None,
            model_states: List["ModelState"] = None,
            name: str | None = None,
            placement_frame: str | None = None,
            plugins: List["Plugin"] = None,
            pose: "Pose" = None,
            static: bool | None = None,
            uri: str | None = None
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
                if getattr(_c, 'sdfversion', None) is None:
                    _c.sdfversion = self.sdfversion
                elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.model_states[_i] = _c.to_version(self.sdfversion)
            for _i, _c in enumerate(self.plugins):
                if not hasattr(_c, 'to_version'): continue
                if getattr(_c, 'sdfversion', None) is None:
                    _c.sdfversion = self.sdfversion
                elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.plugins[_i] = _c.to_version(self.sdfversion)
            if self.pose is not None and hasattr(self.pose, 'to_version'):
                if getattr(self.pose, 'sdfversion', None) is None:
                    self.pose.sdfversion = self.sdfversion
                elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.pose = self.pose.to_version(self.sdfversion)

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
            if self.merge is not None and cmp_version(target_version, "1.9") < 0:
                raise ValueError(f"'merge' is not supported in SDF version {target_version} (added in 1.9)")
            if self.model_states and cmp_version(target_version, "1.12") < 0:
                raise ValueError(f"'model_states' is not supported in SDF version {target_version} (added in 1.12)")
            if self.placement_frame is not None and cmp_version(target_version, "1.8") < 0:
                raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.8)")
            kwargs: dict = {"sdf_version": target_version, "merge": self.merge, "model_states": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.model_states or [])], "name": self.name, "placement_frame": self.placement_frame, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])], "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "static": self.static, "uri": self.uri}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.model_state import ModelState
            from ..elements.plugin import Plugin
            from ..elements.pose import Pose
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("include")
            if self.merge is not None:
                el.set("merge", str(self.merge).lower())
            for item in (self.model_states or []):
                _child_res = item.to_sdf(version)
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
                _child_res = item.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('plugin')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.pose is not None:
                _child_res = self.pose.to_sdf(version)
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
            _raw_merge = el.get("merge")
            if _raw_merge is not None:
                _merge = str(_raw_merge).strip().lower() == 'true'
                if isinstance(_merge, SDFError):
                    return _merge.extend("@merge")
            else:
                _merge = None
            if _merge is not None and cmp_version(version, "1.9") < 0:
                if _merge != False:
                    return SDFError(f"'merge' is not supported in SDF version {version} (added in 1.9)")
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
                _text = _c_tmp.text if _c_tmp.text is not None else None
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("name")
                _name = _val
            else:
                _name = None
            _c_tmp = el.find("placement_frame")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else None
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("placement_frame")
                _placement_frame = _val
            else:
                _placement_frame = None
            if _placement_frame is not None and cmp_version(version, "1.8") < 0:
                return SDFError(f"'placement_frame' is not supported in SDF version {version} (added in 1.8)")
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

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Model.Origin":
            kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("origin")
            if self.pose is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("pose")
                    _c_tmp.text = str(self.pose)
                    el.append(_c_tmp)
                else:
                    el.set("pose", str(self.pose))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Model.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is not None:
                _pose = _parse_pose(_raw_pose)
                if isinstance(_pose, SDFError):
                    return _pose.extend("@pose")
            else:
                _pose = None
            return cls(sdf_version=version, pose=_pose)

    def __init__(
        self,
        sdf_version: str | None = None,
        allow_auto_disable: bool | None = None,
        canonical_link: str | None = None,
        enable_wind: bool | None = None,
        frames: List["Frame"] = None,
        grippers: List["Gripper"] = None,
        includes: List["Model.Include"] = None,
        joints: List["Joint"] = None,
        links: List["Link"] = None,
        model_states: List["ModelState"] = None,
        models: List["Model"] = None,
        name: str | None = None,
        origin: "Model.Origin" = None,
        placement_frame: str | None = None,
        plugins: List["Plugin"] = None,
        pose: "Pose" = None,
        self_collide: bool | None = None,
        static: bool | None = None
    ):
        super().__init__(sdf_version)
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
        self.self_collide = self_collide
        self.static = static
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.grippers):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.grippers[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.includes):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.includes[_i] = _c.to_version(self.sdfversion)
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
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, 'sdfversion', None) is None:
                self.origin.sdfversion = self.sdfversion
            elif getattr(self.origin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.origin = self.origin.to_version(self.sdfversion)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.plugins[_i] = _c.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)

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

    def add_model(self, *items: "Model"):
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
        if self.canonical_link is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'canonical_link' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_wind is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_wind' is not supported in SDF version {target_version} (added in 1.6)")
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.includes and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'includes' is not supported in SDF version {target_version} (added in 1.5)")
        if self.model_states and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_states' is not supported in SDF version {target_version} (added in 1.12)")
        if self.models and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'models' is not supported in SDF version {target_version} (added in 1.5)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.placement_frame is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.8)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.self_collide is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'self_collide' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs: dict = {"sdf_version": target_version, "allow_auto_disable": self.allow_auto_disable, "canonical_link": self.canonical_link, "enable_wind": self.enable_wind, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "grippers": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.grippers or [])], "includes": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.includes or [])], "joints": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joints or [])], "links": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.links or [])], "model_states": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.model_states or [])], "models": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])], "name": self.name, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "placement_frame": self.placement_frame, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])], "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "self_collide": self.self_collide, "static": self.static}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.gripper import Gripper
        from ..elements.joint import Joint
        from ..elements.link import Link
        from ..elements.model_state import ModelState
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
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
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.grippers or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('gripper')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.includes or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('include')
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
        if self.origin is not None:
            _child_res = self.origin.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('origin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.placement_frame is not None:
            el.set("placement_frame", self.placement_frame)
        for item in (self.plugins or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _child_res = self.pose.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.self_collide is not None:
            _c_tmp = ET.Element("self_collide")
            _c_tmp.text = str(self.self_collide).lower()
            el.append(_c_tmp)
        if self.static is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("static")
                _c_tmp.text = str(self.static).lower()
                el.append(_c_tmp)
            else:
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
        _raw_canonical_link = el.get("canonical_link")
        if _raw_canonical_link is not None:
            _canonical_link = _raw_canonical_link
            if isinstance(_canonical_link, SDFError):
                return _canonical_link.extend("@canonical_link")
        else:
            _canonical_link = None
        if _canonical_link is not None and cmp_version(version, "1.7") < 0:
            if _canonical_link != None:
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
        if _enable_wind is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'enable_wind' is not supported in SDF version {version} (added in 1.6)")
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
        if _includes and cmp_version(version, "1.5") < 0:
            return SDFError(f"'includes' is not supported in SDF version {version} (added in 1.5)")
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
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _models.append(_res)
        if _models and cmp_version(version, "1.5") < 0:
            return SDFError(f"'models' is not supported in SDF version {version} (added in 1.5)")
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = cls.Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
        _raw_placement_frame = el.get("placement_frame")
        if _raw_placement_frame is not None:
            _placement_frame = _raw_placement_frame
            if isinstance(_placement_frame, SDFError):
                return _placement_frame.extend("@placement_frame")
        else:
            _placement_frame = None
        if _placement_frame is not None and cmp_version(version, "1.8") < 0:
            if _placement_frame != None:
                return SDFError(f"'placement_frame' is not supported in SDF version {version} (added in 1.8)")
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
        _c_tmp = el.find("self_collide")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("self_collide")
            _self_collide = _val
        else:
            _self_collide = None
        if _self_collide is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'self_collide' is not supported in SDF version {version} (added in 1.5)")
        _raw_static = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("static")
            if _c_tmp is not None: _raw_static = _c_tmp.text
        else:
            _raw_static = el.get("static")
        if _raw_static is not None:
            _static = str(_raw_static).strip().lower() == 'true'
            if isinstance(_static, SDFError):
                return _static.extend("@static")
        else:
            _static = None
        return cls(sdf_version=version, allow_auto_disable=_allow_auto_disable, canonical_link=_canonical_link, enable_wind=_enable_wind, frames=_frames, grippers=_grippers, includes=_includes, joints=_joints, links=_links, model_states=_model_states, models=_models, name=_name, origin=_origin, placement_frame=_placement_frame, plugins=_plugins, pose=_pose, self_collide=_self_collide, static=_static)
