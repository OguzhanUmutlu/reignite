### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.geometry import Geometry
    from ..elements.material import Material
    from ..elements.plugin import Plugin
    from ..elements.pose import Pose


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class CastShadows(BaseModel):
    def __init__(self, sdf_version: str, cast_shadows: bool = True):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows

    def to_version(self, target_version: str) -> "CastShadows":
        if self.cast_shadows is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'cast_shadows' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["cast_shadows"] = self.cast_shadows
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cast_shadows")
        if self.cast_shadows is not None:
            el.text = str(self.cast_shadows).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _cast_shadows = str(_text).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows
        if _cast_shadows is not None and cmp_version(version, "1.2") < 0:
            if _cast_shadows != True:
                return SDFError(f"'cast_shadows' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, cast_shadows=_cast_shadows)


class LaserRetro(BaseModel):
    def __init__(self, sdf_version: str, laser_retro: float = 0.0):
        self.__version__ = sdf_version
        self.laser_retro = laser_retro

    def to_version(self, target_version: str) -> "LaserRetro":
        if self.laser_retro is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'laser_retro' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["laser_retro"] = self.laser_retro
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("laser_retro")
        if self.laser_retro is not None:
            el.text = str(self.laser_retro)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _laser_retro = _parse_double(_text)
        if isinstance(_laser_retro, SDFError):
            return _laser_retro
        if _laser_retro is not None and cmp_version(version, "1.2") < 0:
            if _laser_retro != 0.0:
                return SDFError(f"'laser_retro' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, laser_retro=_laser_retro)


class Layer(BaseModel):
    def __init__(self, sdf_version: str, layer: int = 0):
        self.__version__ = sdf_version
        self.layer = layer

    def to_version(self, target_version: str) -> "Layer":
        kwargs = {"sdf_version": target_version}
        kwargs["layer"] = self.layer
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("layer")
        if self.layer is not None:
            el.text = str(self.layer)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _layer = _parse_int32(_text)
        if isinstance(_layer, SDFError):
            return _layer
        return cls(sdf_version=version, layer=_layer)


class Meta(BaseModel):
    def __init__(self, sdf_version: str, layer: "Layer" = None):
        self.__version__ = sdf_version
        self.layer = layer

    def to_version(self, target_version: str) -> "Meta":
        kwargs = {"sdf_version": target_version}
        kwargs["layer"] = self.layer.to_version(target_version) if self.layer is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("meta")
        if self.layer is not None:
            el.append(self.layer.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_layer = el.find("layer")
        if _c_layer is not None:
            _res = Layer._from_sdf(_c_layer, version)
            if isinstance(_res, SDFError):
                return _res.extend("layer")
            _layer = _res
        else:
            _layer = None
        return cls(sdf_version=version, layer=_layer)


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


class Transparency(BaseModel):
    def __init__(self, sdf_version: str, transparency: float = 0.0):
        self.__version__ = sdf_version
        self.transparency = transparency

    def to_version(self, target_version: str) -> "Transparency":
        if self.transparency is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'transparency' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["transparency"] = self.transparency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("transparency")
        if self.transparency is not None:
            el.text = str(self.transparency)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _transparency = _parse_double(_text)
        if isinstance(_transparency, SDFError):
            return _transparency
        if _transparency is not None and cmp_version(version, "1.2") < 0:
            if _transparency != 0.0:
                return SDFError(f"'transparency' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, transparency=_transparency)


class VisibilityFlags(BaseModel):
    def __init__(self, sdf_version: str, visibility_flags: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "VisibilityFlags":
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_flags"] = self.visibility_flags
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visibility_flags")
        if self.visibility_flags is not None:
            el.text = str(self.visibility_flags)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4294967295
        _visibility_flags = _parse_uint32(_text)
        if isinstance(_visibility_flags, SDFError):
            return _visibility_flags
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            if _visibility_flags != 4294967295:
                return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_flags=_visibility_flags)


class Visual(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        cast_shadows: bool = True,
        frame: List["Frame"] = None,
        geometry: "Geometry" = None,
        laser_retro: float = 0.0,
        material: "Material" = None,
        meta: "Meta" = None,
        name: str = "__default__",
        origin: "Origin" = None,
        plugin: List["Plugin"] = None,
        pose: "Pose" = None,
        transparency: float = 0.0,
        visibility_flags: "VisibilityFlags" = None
    ):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows
        self.frame = frame or []
        self.geometry = geometry
        self.laser_retro = laser_retro
        self.material = material
        self.meta = meta
        self.name = name
        self.origin = origin
        self.plugin = plugin or []
        self.pose = pose
        self.transparency = transparency
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "Visual":
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.material import Material
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.cast_shadows is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'cast_shadows' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.laser_retro is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'laser_retro' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.meta is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'meta' is not supported in SDF version {target_version} (added in 1.5)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.plugin is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {target_version} (added in 1.3)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.transparency is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'transparency' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["cast_shadows"] = self.cast_shadows
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["laser_retro"] = self.laser_retro
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        kwargs["meta"] = self.meta.to_version(target_version) if self.meta is not None else None
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["transparency"] = self.transparency
        kwargs["visibility_flags"] = self.visibility_flags.to_version(target_version) if self.visibility_flags is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.material import Material
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visual")
        if self.cast_shadows is not None:
            el.set("cast_shadows", str(self.cast_shadows).lower())
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.geometry is None:
            self.geometry = Geometry(sdf_version=version)
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.laser_retro is not None:
            el.set("laser_retro", str(self.laser_retro))
        if self.material is not None:
            el.append(self.material.to_sdf(version))
        if self.meta is not None:
            el.append(self.meta.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.transparency is not None:
            el.set("transparency", str(self.transparency))
        if self.visibility_flags is not None:
            el.append(self.visibility_flags.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.material import Material
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        _cast_shadows = str(el.get("cast_shadows", True)).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows.extend("@cast_shadows")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_geometry = el.find("geometry")
        if _c_geometry is not None:
            _res = Geometry._from_sdf(_c_geometry, version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        else:
            _res = Geometry._from_sdf(ET.Element("geometry"), version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        _laser_retro = _parse_double(el.get("laser_retro", 0.0))
        if isinstance(_laser_retro, SDFError):
            return _laser_retro.extend("@laser_retro")
        _c_material = el.find("material")
        if _c_material is not None:
            _res = Material._from_sdf(_c_material, version)
            if isinstance(_res, SDFError):
                return _res.extend("material")
            _material = _res
        else:
            _material = None
        _c_meta = el.find("meta")
        if _c_meta is not None:
            _res = Meta._from_sdf(_c_meta, version)
            if isinstance(_res, SDFError):
                return _res.extend("meta")
            _meta = _res
        else:
            _meta = None
        if _meta is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'meta' is not supported in SDF version {version} (added in 1.5)")
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
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        if _plugin and cmp_version(version, "1.3") < 0:
            return SDFError(f"'plugin' is not supported in SDF version {version} (added in 1.3)")
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
        _transparency = _parse_double(el.get("transparency", 0.0))
        if isinstance(_transparency, SDFError):
            return _transparency.extend("@transparency")
        _c_visibility_flags = el.find("visibility_flags")
        if _c_visibility_flags is not None:
            _res = VisibilityFlags._from_sdf(_c_visibility_flags, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_flags")
            _visibility_flags = _res
        else:
            _visibility_flags = None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, cast_shadows=_cast_shadows, frame=_frame, geometry=_geometry, laser_retro=_laser_retro, material=_material, meta=_meta, name=_name, origin=_origin, plugin=_plugin, pose=_pose, transparency=_transparency, visibility_flags=_visibility_flags)
