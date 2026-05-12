### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3
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


class Audio(BaseModel):
    def __init__(self, sdf_version: str, device: "Device" = None):
        self.__version__ = sdf_version
        self.device = device

    def to_version(self, target_version: str) -> "Audio":
        kwargs = {"sdf_version": target_version}
        kwargs["device"] = self.device.to_version(target_version) if self.device is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("audio")
        if self.device is not None:
            el.append(self.device.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_device = el.find("device")
        if _c_device is not None:
            _res = Device._from_sdf(_c_device, version)
            if isinstance(_res, SDFError):
                return _res.extend("device")
            _device = _res
        else:
            _device = None
        return cls(sdf_version=version, device=_device)


class Device(BaseModel):
    def __init__(self, sdf_version: str, device: str = "default"):
        self.__version__ = sdf_version
        self.device = device

    def to_version(self, target_version: str) -> "Device":
        kwargs = {"sdf_version": target_version}
        kwargs["device"] = self.device
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("device")
        if self.device is not None:
            el.text = self.device
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "default"
        _device = _text
        if isinstance(_device, SDFError):
            return _device
        return cls(sdf_version=version, device=_device)


class Gravity(BaseModel):
    def __init__(self, sdf_version: str, gravity: _SDFVector3 = None):
        self.__version__ = sdf_version
        if gravity is None:
            gravity = _SDFVector3.from_sdf("0 0 -9.8")
        self.gravity = gravity

    def to_version(self, target_version: str) -> "Gravity":
        if self.gravity is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'gravity' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["gravity"] = self.gravity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gravity")
        if self.gravity is not None:
            el.text = self.gravity.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 -9.8"
        _gravity = _SDFVector3._from_sdf(_text, version)
        if isinstance(_gravity, SDFError):
            return _gravity
        if _gravity is not None and cmp_version(version, "1.6") < 0:
            if _gravity != "0 0 -9.8":
                return SDFError(f"'gravity' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, gravity=_gravity)


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
        from ..elements.model_state import ModelState
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.merge is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'merge' is not supported in SDF version {target_version} (added in 1.10)")
        if self.model_state is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'model_state' is not supported in SDF version {target_version} (added in 1.12)")
        if self.name is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.5)")
        if self.placement_frame is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.8)")
        if self.plugin is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {target_version} (added in 1.5)")
        if self.pose is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.5)")
        if self.static is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.5)")
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
        from ..elements.model_state import ModelState
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
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
        from ..elements.model_state import ModelState
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        _merge = str(el.get("merge", False)).strip().lower() == 'true'
        if isinstance(_merge, SDFError):
            return _merge.extend("@merge")
        if _merge is not None and cmp_version(version, "1.10") < 0:
            if _merge != False:
                return SDFError(f"'merge' is not supported in SDF version {version} (added in 1.10)")
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
        if _name is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'name' is not supported in SDF version {version} (added in 1.5)")
        _c_placement_frame = el.find("placement_frame")
        if _c_placement_frame is not None:
            _res = PlacementFrame._from_sdf(_c_placement_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("placement_frame")
            _placement_frame = _res
        else:
            _placement_frame = None
        if _placement_frame is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'placement_frame' is not supported in SDF version {version} (added in 1.8)")
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        if _plugin and cmp_version(version, "1.5") < 0:
            return SDFError(f"'plugin' is not supported in SDF version {version} (added in 1.5)")
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
        _c_static = el.find("static")
        if _c_static is not None:
            _res = Static._from_sdf(_c_static, version)
            if isinstance(_res, SDFError):
                return _res.extend("static")
            _static = _res
        else:
            _static = None
        if _static is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'static' is not supported in SDF version {version} (added in 1.5)")
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        return cls(sdf_version=version, merge=_merge, model_state=_model_state, name=_name, placement_frame=_placement_frame, plugin=_plugin, pose=_pose, static=_static, uri=_uri)


class LinearVelocity(BaseModel):
    def __init__(self, sdf_version: str, linear_velocity: _SDFVector3 = None):
        self.__version__ = sdf_version
        if linear_velocity is None:
            linear_velocity = _SDFVector3.from_sdf("0 0 0")
        self.linear_velocity = linear_velocity

    def to_version(self, target_version: str) -> "LinearVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["linear_velocity"] = self.linear_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear_velocity")
        if self.linear_velocity is not None:
            el.text = self.linear_velocity.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _linear_velocity = _SDFVector3._from_sdf(_text, version)
        if isinstance(_linear_velocity, SDFError):
            return _linear_velocity
        return cls(sdf_version=version, linear_velocity=_linear_velocity)


class MagneticField(BaseModel):
    def __init__(self, sdf_version: str, magnetic_field: _SDFVector3 = None):
        self.__version__ = sdf_version
        if magnetic_field is None:
            magnetic_field = _SDFVector3.from_sdf("5.5645e-6 22.8758e-6 -42.3884e-6")
        self.magnetic_field = magnetic_field

    def to_version(self, target_version: str) -> "MagneticField":
        if self.magnetic_field is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["magnetic_field"] = self.magnetic_field
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("magnetic_field")
        if self.magnetic_field is not None:
            el.text = self.magnetic_field.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "5.5645e-6 22.8758e-6 -42.3884e-6"
        _magnetic_field = _SDFVector3._from_sdf(_text, version)
        if isinstance(_magnetic_field, SDFError):
            return _magnetic_field
        if _magnetic_field is not None and cmp_version(version, "1.6") < 0:
            if _magnetic_field != "5.5645e-6 22.8758e-6 -42.3884e-6":
                return SDFError(f"'magnetic_field' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, magnetic_field=_magnetic_field)


class Name(BaseModel):
    def __init__(self, sdf_version: str, name: str = ""):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "Name":
        if self.name is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.5)")
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
        if _name is not None and cmp_version(version, "1.5") < 0:
            if _name != "":
                return SDFError(f"'name' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, name=_name)


class PlacementFrame(BaseModel):
    def __init__(self, sdf_version: str, placement_frame: str = ""):
        self.__version__ = sdf_version
        self.placement_frame = placement_frame

    def to_version(self, target_version: str) -> "PlacementFrame":
        if self.placement_frame is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'placement_frame' is not supported in SDF version {target_version} (added in 1.8)")
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
        if _placement_frame is not None and cmp_version(version, "1.8") < 0:
            if _placement_frame != "":
                return SDFError(f"'placement_frame' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, placement_frame=_placement_frame)


class Static(BaseModel):
    def __init__(self, sdf_version: str, static: bool = False):
        self.__version__ = sdf_version
        self.static = static

    def to_version(self, target_version: str) -> "Static":
        if self.static is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'static' is not supported in SDF version {target_version} (added in 1.5)")
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
        if _static is not None and cmp_version(version, "1.5") < 0:
            if _static != False:
                return SDFError(f"'static' is not supported in SDF version {version} (added in 1.5)")
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


class Wind(BaseModel):
    def __init__(self, sdf_version: str, linear_velocity: "LinearVelocity" = None):
        self.__version__ = sdf_version
        self.linear_velocity = linear_velocity

    def to_version(self, target_version: str) -> "Wind":
        kwargs = {"sdf_version": target_version}
        kwargs["linear_velocity"] = self.linear_velocity.to_version(target_version) if self.linear_velocity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("wind")
        if self.linear_velocity is not None:
            el.append(self.linear_velocity.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_linear_velocity = el.find("linear_velocity")
        if _c_linear_velocity is not None:
            _res = LinearVelocity._from_sdf(_c_linear_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("linear_velocity")
            _linear_velocity = _res
        else:
            _linear_velocity = None
        return cls(sdf_version=version, linear_velocity=_linear_velocity)


class World(BaseModel):
    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "physics::gravity", "to": "gravity"}, {"type": "move", "from": "physics::magnetic_field", "to": "magnetic_field"}]}]

    def __init__(
        self,
        sdf_version: str,
        actor: List["Actor"] = None,
        atmosphere: "Atmosphere" = None,
        audio: "Audio" = None,
        frame: List["Frame"] = None,
        gravity: "Gravity" = None,
        gui: "Gui" = None,
        include: List["Include"] = None,
        joint: List["Joint"] = None,
        light: List["Light"] = None,
        magnetic_field: "MagneticField" = None,
        model: List["Model"] = None,
        name: str = "__default__",
        physics: "Physics" = None,
        plugin: List["Plugin"] = None,
        population: List["Population"] = None,
        road: List["Road"] = None,
        scene: "Scene" = None,
        spherical_coordinates: "SphericalCoordinates" = None,
        state: List["State"] = None,
        wind: "Wind" = None
    ):
        self.__version__ = sdf_version
        self.actor = actor or []
        self.atmosphere = atmosphere
        self.audio = audio
        self.frame = frame or []
        self.gravity = gravity
        self.gui = gui
        self.include = include or []
        self.joint = joint or []
        self.light = light or []
        self.magnetic_field = magnetic_field
        self.model = model or []
        self.name = name
        self.physics = physics
        self.plugin = plugin or []
        self.population = population or []
        self.road = road or []
        self.scene = scene
        self.spherical_coordinates = spherical_coordinates
        self.state = state or []
        self.wind = wind

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
        if self.frame is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.7)")
        if self.gravity is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'gravity' is not supported in SDF version {target_version} (added in 1.6)")
        if self.include is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'include' is not supported in SDF version {target_version} (added in 1.4)")
        if self.joint is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'joint' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.magnetic_field is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'magnetic_field' is not supported in SDF version {target_version} (added in 1.6)")
        if self.population is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'population' is not supported in SDF version {target_version} (added in 1.5)")
        if self.spherical_coordinates is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'spherical_coordinates' is not supported in SDF version {target_version} (added in 1.4)")
        if self.wind is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'wind' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["actor"] = [c.to_version(target_version) for c in (self.actor or [])]
        kwargs["atmosphere"] = self.atmosphere.to_version(target_version) if self.atmosphere is not None else None
        kwargs["audio"] = self.audio.to_version(target_version) if self.audio is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["gravity"] = self.gravity.to_version(target_version) if self.gravity is not None else None
        kwargs["gui"] = self.gui.to_version(target_version) if self.gui is not None else None
        kwargs["include"] = [c.to_version(target_version) for c in (self.include or [])]
        kwargs["joint"] = [c.to_version(target_version) for c in (self.joint or [])]
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        kwargs["magnetic_field"] = self.magnetic_field.to_version(target_version) if self.magnetic_field is not None else None
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["name"] = self.name
        kwargs["physics"] = self.physics.to_version(target_version) if self.physics is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["population"] = [c.to_version(target_version) for c in (self.population or [])]
        kwargs["road"] = [c.to_version(target_version) for c in (self.road or [])]
        kwargs["scene"] = self.scene.to_version(target_version) if self.scene is not None else None
        kwargs["spherical_coordinates"] = self.spherical_coordinates.to_version(target_version) if self.spherical_coordinates is not None else None
        kwargs["state"] = [c.to_version(target_version) for c in (self.state or [])]
        kwargs["wind"] = self.wind.to_version(target_version) if self.wind is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
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
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("world")
        for item in (self.actor or []):
            el.append(item.to_sdf(version))
        if cmp_version(version, "1.6") >= 0:
            if self.atmosphere is None:
                self.atmosphere = Atmosphere(sdf_version=version)
        if self.atmosphere is not None:
            el.append(self.atmosphere.to_sdf(version))
        if self.audio is not None:
            el.append(self.audio.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.gravity is not None:
            el.append(self.gravity.to_sdf(version))
        if self.gui is not None:
            el.append(self.gui.to_sdf(version))
        for item in (self.include or []):
            el.append(item.to_sdf(version))
        for item in (self.joint or []):
            el.append(item.to_sdf(version))
        for item in (self.light or []):
            el.append(item.to_sdf(version))
        if self.magnetic_field is not None:
            el.append(self.magnetic_field.to_sdf(version))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.physics is None:
            self.physics = Physics(sdf_version=version)
        if self.physics is not None:
            el.append(self.physics.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        for item in (self.population or []):
            el.append(item.to_sdf(version))
        for item in (self.road or []):
            el.append(item.to_sdf(version))
        if self.scene is None:
            self.scene = Scene(sdf_version=version)
        if self.scene is not None:
            el.append(self.scene.to_sdf(version))
        if self.spherical_coordinates is not None:
            el.append(self.spherical_coordinates.to_sdf(version))
        for item in (self.state or []):
            el.append(item.to_sdf(version))
        if self.wind is not None:
            el.append(self.wind.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        _actor = []
        for c in el.findall("actor"):
            _res = Actor._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("actor")
            _actor.append(_res)
        _c_atmosphere = el.find("atmosphere")
        if _c_atmosphere is not None:
            _res = Atmosphere._from_sdf(_c_atmosphere, version)
            if isinstance(_res, SDFError):
                return _res.extend("atmosphere")
            _atmosphere = _res
        else:
            _res = Atmosphere._from_sdf(ET.Element("atmosphere"), version)
            if isinstance(_res, SDFError):
                return _res.extend("atmosphere")
            _atmosphere = _res
        if _atmosphere is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'atmosphere' is not supported in SDF version {version} (added in 1.6)")
        _c_audio = el.find("audio")
        if _c_audio is not None:
            _res = Audio._from_sdf(_c_audio, version)
            if isinstance(_res, SDFError):
                return _res.extend("audio")
            _audio = _res
        else:
            _audio = None
        if _audio is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'audio' is not supported in SDF version {version} (added in 1.4)")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.7") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.7)")
        _c_gravity = el.find("gravity")
        if _c_gravity is not None:
            _res = Gravity._from_sdf(_c_gravity, version)
            if isinstance(_res, SDFError):
                return _res.extend("gravity")
            _gravity = _res
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
        _include = []
        for c in el.findall("include"):
            _res = Include._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("include")
            _include.append(_res)
        if _include and cmp_version(version, "1.4") < 0:
            return SDFError(f"'include' is not supported in SDF version {version} (added in 1.4)")
        _joint = []
        for c in el.findall("joint"):
            _res = Joint._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("joint")
            _joint.append(_res)
        _light = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _light.append(_res)
        _c_magnetic_field = el.find("magnetic_field")
        if _c_magnetic_field is not None:
            _res = MagneticField._from_sdf(_c_magnetic_field, version)
            if isinstance(_res, SDFError):
                return _res.extend("magnetic_field")
            _magnetic_field = _res
        else:
            _magnetic_field = None
        if _magnetic_field is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'magnetic_field' is not supported in SDF version {version} (added in 1.6)")
        _model = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _model.append(_res)
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
            _res = Physics._from_sdf(ET.Element("physics"), version)
            if isinstance(_res, SDFError):
                return _res.extend("physics")
            _physics = _res
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        _population = []
        for c in el.findall("population"):
            _res = Population._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("population")
            _population.append(_res)
        if _population and cmp_version(version, "1.5") < 0:
            return SDFError(f"'population' is not supported in SDF version {version} (added in 1.5)")
        _road = []
        for c in el.findall("road"):
            _res = Road._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("road")
            _road.append(_res)
        _c_scene = el.find("scene")
        if _c_scene is not None:
            _res = Scene._from_sdf(_c_scene, version)
            if isinstance(_res, SDFError):
                return _res.extend("scene")
            _scene = _res
        else:
            _res = Scene._from_sdf(ET.Element("scene"), version)
            if isinstance(_res, SDFError):
                return _res.extend("scene")
            _scene = _res
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
        _state = []
        for c in el.findall("state"):
            _res = State._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("state")
            _state.append(_res)
        _c_wind = el.find("wind")
        if _c_wind is not None:
            _res = Wind._from_sdf(_c_wind, version)
            if isinstance(_res, SDFError):
                return _res.extend("wind")
            _wind = _res
        else:
            _wind = None
        if _wind is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'wind' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, actor=_actor, atmosphere=_atmosphere, audio=_audio, frame=_frame, gravity=_gravity, gui=_gui, include=_include, joint=_joint, light=_light, magnetic_field=_magnetic_field, model=_model, name=_name, physics=_physics, plugin=_plugin, population=_population, road=_road, scene=_scene, spherical_coordinates=_spherical_coordinates, state=_state, wind=_wind)
