### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations

if typing.TYPE_CHECKING:
    from ..elements.actor import Actor
    from ..elements.atmosphere import Atmosphere
    from ..elements.frame import Frame
    from ..elements.gui import Gui
    from ..elements.joint import Joint
    from ..elements.light import Light
    from ..elements.model import Model
    from ..elements.model_state import ModelState
    from ..elements.physics import Physics
    from ..elements.plugin import Plugin
    from ..elements.population import Population
    from ..elements.pose import Pose
    from ..elements.road import Road
    from ..elements.scene import Scene
    from ..elements.spherical_coordinates import SphericalCoordinates
    from ..elements.state import State

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class World(BaseModel):
    class Audio(BaseModel):
        def __init__(self, sdf_version: str | None = None, device: str | None = "default"):
            super().__init__(sdf_version)
            self.device = device if device is not None else "default"

        def to_version(self, target_version: str) -> "World.Audio":
            kwargs: dict = {"sdf_version": target_version, "device": self.device}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("audio")
            if self.device is not None:
                _c_tmp = ET.Element("device")
                _c_tmp.text = self.device
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "World.Audio | SDFError":
            _c_tmp = el.find("device")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "default"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("device")
                _device = _val
            else:
                _device = None
            return cls(sdf_version=version, device=_device)

    class Include(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            merge: bool | None = False,
            model_states: List["ModelState"] = None,
            name: str | None = "",
            placement_frame: str | None = "",
            plugins: List["Plugin"] = None,
            pose: "Pose" = None,
            static: bool | None = False,
            uri: str | None = "__default__"
        ):
            super().__init__(sdf_version)
            self.merge = merge if merge is not None else False
            self.model_states = model_states or []
            self.name = name if name is not None else ""
            self.placement_frame = placement_frame if placement_frame is not None else ""
            self.plugins = plugins or []
            self.pose = pose
            self.static = static if static is not None else False
            self.uri = uri if uri is not None else "__default__"
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

        def to_version(self, target_version: str) -> "World.Include":
            from ..elements.model_state import ModelState
            from ..elements.plugin import Plugin
            from ..elements.pose import Pose
            if self.merge is not None and cmp_version(target_version, "1.10") < 0:
                raise ValueError(f"'merge' is not supported in SDF version {target_version} (added in 1.10)")
            if self.model_states is not None and cmp_version(target_version, "1.12") < 0:
                raise ValueError(f"'model_states' is not supported in SDF version {target_version} (added in 1.12)")
            if self.name is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.5)")
            if self.placement_frame is not None and cmp_version(target_version, "1.8") < 0:
                raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.8)")
            if self.plugins is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'plugins' is not supported in SDF version {target_version} (added in 1.5)")
            if self.pose is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.5)")
            if self.static is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.5)")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "World.Include | SDFError":
            from ..elements.model_state import ModelState
            from ..elements.plugin import Plugin
            from ..elements.pose import Pose
            _merge = str(el.get("merge", False)).strip().lower() == 'true'
            if isinstance(_merge, SDFError):
                return _merge.extend("@merge")
            if _merge is not None and cmp_version(version, "1.10") < 0:
                if _merge != False:
                    return SDFError(f"'merge' is not supported in SDF version {version} (added in 1.10)")
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
            if _name is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'name' is not supported in SDF version {version} (added in 1.5)")
            _c_tmp = el.find("placement_frame")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else ""
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
            if _plugins and cmp_version(version, "1.5") < 0:
                return SDFError(f"'plugins' is not supported in SDF version {version} (added in 1.5)")
            _c_pose = el.find("pose")
            if _c_pose is not None:
                _res = Pose._from_sdf(_c_pose, version)
                if isinstance(_res, SDFError):
                    return _res.extend("pose")
                _pose = _res
            else:
                _pose = None
            if _pose is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.5)")
            _c_tmp = el.find("static")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else False
                _val = str(_text).strip().lower() == 'true'
                if isinstance(_val, SDFError):
                    return _val.extend("static")
                _static = _val
            else:
                _static = None
            if _static is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'static' is not supported in SDF version {version} (added in 1.5)")
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

    class Wind(BaseModel):
        def __init__(self, sdf_version: str | None = None, linear_velocity: _Vector3T | None = None):
            super().__init__(sdf_version)
            self.linear_velocity = _vector3("0 0 0") if linear_velocity is None else _vector3(linear_velocity)

        def to_version(self, target_version: str) -> "World.Wind":
            kwargs: dict = {"sdf_version": target_version, "linear_velocity": self.linear_velocity}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("wind")
            if self.linear_velocity is not None:
                _c_tmp = ET.Element("linear_velocity")
                _c_tmp.text = str(self.linear_velocity)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "World.Wind | SDFError":
            _c_tmp = el.find("linear_velocity")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
                _val = _parse_vector3(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("linear_velocity")
                _linear_velocity = _val
            else:
                _linear_velocity = None
            return cls(sdf_version=version, linear_velocity=_linear_velocity)

    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "physics::gravity", "to": "gravity"}, {"type": "move", "from": "physics::magnetic_field", "to": "magnetic_field"}]}]

    def __init__(
        self,
        sdf_version: str | None = None,
        actors: List["Actor"] = None,
        atmosphere: "Atmosphere" = None,
        audio: "World.Audio" = None,
        frames: List["Frame"] = None,
        gravity: _Vector3T | None = None,
        gui: "Gui" = None,
        includes: List["World.Include"] = None,
        joints: List["Joint"] = None,
        lights: List["Light"] = None,
        magnetic_field: _Vector3T | None = None,
        models: List["Model"] = None,
        name: str | None = "__default__",
        physics: "Physics" = None,
        plugins: List["Plugin"] = None,
        populations: List["Population"] = None,
        roads: List["Road"] = None,
        scene: "Scene" = None,
        spherical_coordinates: "SphericalCoordinates" = None,
        states: List["State"] = None,
        wind: "World.Wind" = None
    ):
        super().__init__(sdf_version)
        self.actors = actors or []
        self.atmosphere = atmosphere
        self.audio = audio
        self.frames = frames or []
        self.gravity = _vector3("0 0 -9.8") if gravity is None else _vector3(gravity)
        self.gui = gui
        self.includes = includes or []
        self.joints = joints or []
        self.lights = lights or []
        self.magnetic_field = _vector3("5.5645e-6 22.8758e-6 -42.3884e-6") if magnetic_field is None else _vector3(magnetic_field)
        self.models = models or []
        self.name = name if name is not None else "__default__"
        self.physics = physics
        self.plugins = plugins or []
        self.populations = populations or []
        self.roads = roads or []
        self.scene = scene
        self.spherical_coordinates = spherical_coordinates
        self.states = states or []
        self.wind = wind
        for _i, _c in enumerate(self.actors):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.actors[_i] = _c.to_version(self.sdfversion)
        if self.atmosphere is not None and hasattr(self.atmosphere, 'to_version'):
            if getattr(self.atmosphere, 'sdfversion', None) is None:
                self.atmosphere.sdfversion = self.sdfversion
            elif getattr(self.atmosphere, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.atmosphere = self.atmosphere.to_version(self.sdfversion)
        if self.audio is not None and hasattr(self.audio, 'to_version'):
            if getattr(self.audio, 'sdfversion', None) is None:
                self.audio.sdfversion = self.sdfversion
            elif getattr(self.audio, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.audio = self.audio.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.gui is not None and hasattr(self.gui, 'to_version'):
            if getattr(self.gui, 'sdfversion', None) is None:
                self.gui.sdfversion = self.sdfversion
            elif getattr(self.gui, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.gui = self.gui.to_version(self.sdfversion)
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
        for _i, _c in enumerate(self.lights):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.lights[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.models):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.models[_i] = _c.to_version(self.sdfversion)
        if self.physics is not None and hasattr(self.physics, 'to_version'):
            if getattr(self.physics, 'sdfversion', None) is None:
                self.physics.sdfversion = self.sdfversion
            elif getattr(self.physics, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.physics = self.physics.to_version(self.sdfversion)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.plugins[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.populations):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.populations[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.roads):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.roads[_i] = _c.to_version(self.sdfversion)
        if self.scene is not None and hasattr(self.scene, 'to_version'):
            if getattr(self.scene, 'sdfversion', None) is None:
                self.scene.sdfversion = self.sdfversion
            elif getattr(self.scene, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.scene = self.scene.to_version(self.sdfversion)
        if self.spherical_coordinates is not None and hasattr(self.spherical_coordinates, 'to_version'):
            if getattr(self.spherical_coordinates, 'sdfversion', None) is None:
                self.spherical_coordinates.sdfversion = self.sdfversion
            elif getattr(self.spherical_coordinates, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.spherical_coordinates = self.spherical_coordinates.to_version(self.sdfversion)
        for _i, _c in enumerate(self.states):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.states[_i] = _c.to_version(self.sdfversion)
        if self.wind is not None and hasattr(self.wind, 'to_version'):
            if getattr(self.wind, 'sdfversion', None) is None:
                self.wind.sdfversion = self.sdfversion
            elif getattr(self.wind, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.wind = self.wind.to_version(self.sdfversion)

    def add_actor(self, *items: "Actor"):
        if self.actors is None:
            self.actors = []
        self.actors.extend(items)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_include(self, *items: "World.Include"):
        if self.includes is None:
            self.includes = []
        self.includes.extend(items)

    def add_joint(self, *items: "Joint"):
        if self.joints is None:
            self.joints = []
        self.joints.extend(items)

    def add_light(self, *items: "Light"):
        if self.lights is None:
            self.lights = []
        self.lights.extend(items)

    def add_model(self, *items: "Model"):
        if self.models is None:
            self.models = []
        self.models.extend(items)

    def add_plugin(self, *items: "Plugin"):
        if self.plugins is None:
            self.plugins = []
        self.plugins.extend(items)

    def add_population(self, *items: "Population"):
        if self.populations is None:
            self.populations = []
        self.populations.extend(items)

    def add_road(self, *items: "Road"):
        if self.roads is None:
            self.roads = []
        self.roads.extend(items)

    def add_state(self, *items: "State"):
        if self.states is None:
            self.states = []
        self.states.extend(items)

    def to_version(self, target_version: str) -> "World":
        from ..elements.actor import Actor
        from ..elements.atmosphere import Atmosphere
        from ..elements.frame import Frame
        from ..elements.gui import Gui
        from ..elements.joint import Joint
        from ..elements.light import Light
        from ..elements.model import Model
        from ..elements.physics import Physics
        from ..elements.plugin import Plugin
        from ..elements.population import Population
        from ..elements.road import Road
        from ..elements.scene import Scene
        from ..elements.spherical_coordinates import SphericalCoordinates
        from ..elements.state import State
        if self.atmosphere is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'atmosphere' is not supported in SDF version {target_version} (added in 1.6)")
        if self.audio is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'audio' is not supported in SDF version {target_version} (added in 1.4)")
        if self.frames is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.7)")
        if self.gravity is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'gravity' is not supported in SDF version {target_version} (added in 1.6)")
        if self.includes is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'includes' is not supported in SDF version {target_version} (added in 1.4)")
        if self.joints is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'joints' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.magnetic_field is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (added in 1.6)")
        if self.populations is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'populations' is not supported in SDF version {target_version} (added in 1.5)")
        if self.spherical_coordinates is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'spherical_coordinates' is not supported in SDF version {target_version} (added in 1.4)")
        if self.wind is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'wind' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs: dict = {"sdf_version": target_version, "actors": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.actors or [])], "atmosphere": self.atmosphere.to_version(target_version) if self.atmosphere is not None and hasattr(self.atmosphere, "to_version") else self.atmosphere, "audio": self.audio.to_version(target_version) if self.audio is not None and hasattr(self.audio, "to_version") else self.audio, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "gravity": self.gravity, "gui": self.gui.to_version(target_version) if self.gui is not None and hasattr(self.gui, "to_version") else self.gui, "includes": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.includes or [])], "joints": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.joints or [])], "lights": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.lights or [])], "magnetic_field": self.magnetic_field, "models": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])], "name": self.name, "physics": self.physics.to_version(target_version) if self.physics is not None and hasattr(self.physics, "to_version") else self.physics, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])], "populations": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.populations or [])], "roads": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.roads or [])], "scene": self.scene.to_version(target_version) if self.scene is not None and hasattr(self.scene, "to_version") else self.scene, "spherical_coordinates": self.spherical_coordinates.to_version(target_version) if self.spherical_coordinates is not None and hasattr(self.spherical_coordinates, "to_version") else self.spherical_coordinates, "states": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.states or [])], "wind": self.wind.to_version(target_version) if self.wind is not None and hasattr(self.wind, "to_version") else self.wind}
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.actor import Actor
        from ..elements.atmosphere import Atmosphere
        from ..elements.frame import Frame
        from ..elements.gui import Gui
        from ..elements.joint import Joint
        from ..elements.light import Light
        from ..elements.model import Model
        from ..elements.physics import Physics
        from ..elements.plugin import Plugin
        from ..elements.population import Population
        from ..elements.road import Road
        from ..elements.scene import Scene
        from ..elements.spherical_coordinates import SphericalCoordinates
        from ..elements.state import State
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("world")
        for item in (self.actors or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('actor')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.atmosphere is not None:
            _child_res = self.atmosphere.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('atmosphere')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.audio is not None:
            _child_res = self.audio.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('audio')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.gravity is not None:
            _c_tmp = ET.Element("gravity")
            _c_tmp.text = str(self.gravity)
            el.append(_c_tmp)
        if self.gui is not None:
            _child_res = self.gui.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('gui')
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
        for item in (self.lights or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('light')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.magnetic_field is not None:
            _c_tmp = ET.Element("magnetic_field")
            _c_tmp.text = str(self.magnetic_field)
            el.append(_c_tmp)
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
        if self.physics is not None:
            _child_res = self.physics.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('physics')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.plugins or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.populations or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('population')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.roads or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('road')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.scene is not None:
            _child_res = self.scene.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('scene')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.spherical_coordinates is not None:
            _child_res = self.spherical_coordinates.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('spherical_coordinates')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.states or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('state')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.wind is not None:
            _child_res = self.wind.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('wind')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "World | SDFError":
        from ..elements.actor import Actor
        from ..elements.atmosphere import Atmosphere
        from ..elements.frame import Frame
        from ..elements.gui import Gui
        from ..elements.joint import Joint
        from ..elements.light import Light
        from ..elements.model import Model
        from ..elements.physics import Physics
        from ..elements.plugin import Plugin
        from ..elements.population import Population
        from ..elements.road import Road
        from ..elements.scene import Scene
        from ..elements.spherical_coordinates import SphericalCoordinates
        from ..elements.state import State
        _actors = []
        for c in el.findall("actor"):
            _res = Actor._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("actor")
            _actors.append(_res)
        _c_atmosphere = el.find("atmosphere")
        if _c_atmosphere is not None:
            _res = Atmosphere._from_sdf(_c_atmosphere, version)
            if isinstance(_res, SDFError):
                return _res.extend("atmosphere")
            _atmosphere = _res
        else:
            _atmosphere = None
        if _atmosphere is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'atmosphere' is not supported in SDF version {version} (added in 1.6)")
        _c_audio = el.find("audio")
        if _c_audio is not None:
            _res = cls.Audio._from_sdf(_c_audio, version)
            if isinstance(_res, SDFError):
                return _res.extend("audio")
            _audio = _res
        else:
            _audio = None
        if _audio is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'audio' is not supported in SDF version {version} (added in 1.4)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.7") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.7)")
        _c_tmp = el.find("gravity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 -9.8"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("gravity")
            _gravity = _val
        else:
            _gravity = None
        if _gravity is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'gravity' is not supported in SDF version {version} (added in 1.6)")
        _c_gui = el.find("gui")
        if _c_gui is not None:
            _res = Gui._from_sdf(_c_gui, version)
            if isinstance(_res, SDFError):
                return _res.extend("gui")
            _gui = _res
        else:
            _gui = None
        _includes = []
        for c in el.findall("include"):
            _res = cls.Include._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("include")
            _includes.append(_res)
        if _includes and cmp_version(version, "1.4") < 0:
            return SDFError(f"'includes' is not supported in SDF version {version} (added in 1.4)")
        _joints = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joints.append(_res)
        _lights = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _lights.append(_res)
        _c_tmp = el.find("magnetic_field")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "5.5645e-6 22.8758e-6 -42.3884e-6"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("magnetic_field")
            _magnetic_field = _val
        else:
            _magnetic_field = None
        if _magnetic_field is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'magnetic_field' is not supported in SDF version {version} (added in 1.6)")
        _models = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _models.append(_res)
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_physics = el.find("physics")
        if _c_physics is not None:
            _res = Physics._from_sdf(_c_physics, version)
            if isinstance(_res, SDFError):
                return _res.extend("physics")
            _physics = _res
        else:
            _physics = None
        _plugins = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugins.append(_res)
        _populations = []
        for c in el.findall("population"):
            _res = Population._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("population")
            _populations.append(_res)
        if _populations and cmp_version(version, "1.5") < 0:
            return SDFError(f"'populations' is not supported in SDF version {version} (added in 1.5)")
        _roads = []
        for c in el.findall("road"):
            _res = Road._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("road")
            _roads.append(_res)
        _c_scene = el.find("scene")
        if _c_scene is not None:
            _res = Scene._from_sdf(_c_scene, version)
            if isinstance(_res, SDFError):
                return _res.extend("scene")
            _scene = _res
        else:
            _scene = None
        _c_spherical_coordinates = el.find("spherical_coordinates")
        if _c_spherical_coordinates is not None:
            _res = SphericalCoordinates._from_sdf(_c_spherical_coordinates, version)
            if isinstance(_res, SDFError):
                return _res.extend("spherical_coordinates")
            _spherical_coordinates = _res
        else:
            _spherical_coordinates = None
        if _spherical_coordinates is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'spherical_coordinates' is not supported in SDF version {version} (added in 1.4)")
        _states = []
        for c in el.findall("state"):
            _res = State._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("state")
            _states.append(_res)
        _c_wind = el.find("wind")
        if _c_wind is not None:
            _res = cls.Wind._from_sdf(_c_wind, version)
            if isinstance(_res, SDFError):
                return _res.extend("wind")
            _wind = _res
        else:
            _wind = None
        if _wind is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'wind' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, actors=_actors, atmosphere=_atmosphere, audio=_audio, frames=_frames, gravity=_gravity, gui=_gui, includes=_includes, joints=_joints, lights=_lights, magnetic_field=_magnetic_field, models=_models, name=_name, physics=_physics, plugins=_plugins, populations=_populations, roads=_roads, scene=_scene, spherical_coordinates=_spherical_coordinates, states=_states, wind=_wind)
