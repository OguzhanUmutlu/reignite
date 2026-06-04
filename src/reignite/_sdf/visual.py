### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_int32, _parse_uint32
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.geometry import Geometry
    from ..elements.material import Material
    from ..elements.plugin import Plugin
    from ..elements.pose import Pose

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Visual(BaseModel):
    class Meta(BaseModel):
        def __init__(self, sdf_version: str | None = None, layer: int | None = None):
            super().__init__(sdf_version)
            self.layer = layer

        def to_version(self, target_version: str) -> "Visual.Meta":
            kwargs: dict = {"sdf_version": target_version, "layer": self.layer}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("meta")
            if self.layer is not None:
                _c_tmp = ET.Element("layer")
                _c_tmp.text = str(self.layer)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Visual.Meta | SDFError":
            _c_tmp = el.find("layer")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_int32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("layer")
                _layer = _val
            else:
                _layer = None
            return cls(sdf_version=version, layer=_layer)

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Visual.Origin":
            kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Visual.Origin | SDFError":
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
        cast_shadows: bool | None = None,
        frames: List["Frame"] = None,
        geometry: "Geometry" = None,
        laser_retro: float | None = None,
        material: "Material" = None,
        meta: "Visual.Meta" = None,
        name: str | None = None,
        origin: "Visual.Origin" = None,
        plugins: List["Plugin"] = None,
        pose: "Pose" = None,
        transparency: float | None = None,
        visibility_flags: int | None = None
    ):
        super().__init__(sdf_version)
        self.cast_shadows = cast_shadows
        self.frames = frames or []
        self.geometry = geometry
        self.laser_retro = laser_retro
        self.material = material
        self.meta = meta
        self.name = name
        self.origin = origin
        self.plugins = plugins or []
        self.pose = pose
        self.transparency = transparency
        self.visibility_flags = visibility_flags
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.geometry is not None and hasattr(self.geometry, 'to_version'):
            if getattr(self.geometry, 'sdfversion', None) is None:
                self.geometry.sdfversion = self.sdfversion
            elif getattr(self.geometry, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.geometry = self.geometry.to_version(self.sdfversion)
        if self.material is not None and hasattr(self.material, 'to_version'):
            if getattr(self.material, 'sdfversion', None) is None:
                self.material.sdfversion = self.sdfversion
            elif getattr(self.material, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.material = self.material.to_version(self.sdfversion)
        if self.meta is not None and hasattr(self.meta, 'to_version'):
            if getattr(self.meta, 'sdfversion', None) is None:
                self.meta.sdfversion = self.sdfversion
            elif getattr(self.meta, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.meta = self.meta.to_version(self.sdfversion)
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

    def add_plugin(self, *items: "Plugin"):
        if self.plugins is None:
            self.plugins = []
        self.plugins.extend(items)

    def to_version(self, target_version: str) -> "Visual":
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.material import Material
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.meta is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'meta' is not supported in SDF version {target_version} (added in 1.5)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.plugins and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'plugins' is not supported in SDF version {target_version} (added in 1.3)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "cast_shadows": self.cast_shadows, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "geometry": self.geometry.to_version(target_version) if self.geometry is not None and hasattr(self.geometry, "to_version") else self.geometry, "laser_retro": self.laser_retro, "material": self.material.to_version(target_version) if self.material is not None and hasattr(self.material, "to_version") else self.material, "meta": self.meta.to_version(target_version) if self.meta is not None and hasattr(self.meta, "to_version") else self.meta, "name": self.name, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])], "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "transparency": self.transparency, "visibility_flags": self.visibility_flags}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.material import Material
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("visual")
        if self.cast_shadows is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("cast_shadows")
                _c_tmp.text = str(self.cast_shadows).lower()
                el.append(_c_tmp)
            else:
                el.set("cast_shadows", str(self.cast_shadows).lower())
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.geometry is not None:
            _child_res = self.geometry.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('geometry')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.laser_retro is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("laser_retro")
                _c_tmp.text = str(self.laser_retro)
                el.append(_c_tmp)
            else:
                el.set("laser_retro", str(self.laser_retro))
        if self.material is not None:
            _child_res = self.material.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('material')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.meta is not None:
            _child_res = self.meta.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('meta')
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
        if self.transparency is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("transparency")
                _c_tmp.text = str(self.transparency)
                el.append(_c_tmp)
            else:
                el.set("transparency", str(self.transparency))
        if self.visibility_flags is not None:
            _c_tmp = ET.Element("visibility_flags")
            _c_tmp.text = str(self.visibility_flags)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Visual | SDFError":
        from ..elements.frame import Frame
        from ..elements.geometry import Geometry
        from ..elements.material import Material
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        _raw_cast_shadows = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("cast_shadows")
            if _c_tmp is not None: _raw_cast_shadows = _c_tmp.text
        else:
            _raw_cast_shadows = el.get("cast_shadows")
        if _raw_cast_shadows is not None:
            _cast_shadows = str(_raw_cast_shadows).strip().lower() == 'true'
            if isinstance(_cast_shadows, SDFError):
                return _cast_shadows.extend("@cast_shadows")
        else:
            _cast_shadows = None
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _c_geometry = el.find("geometry")
        if _c_geometry is not None:
            _res = Geometry._from_sdf(_c_geometry, version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        else:
            _geometry = None
        _raw_laser_retro = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("laser_retro")
            if _c_tmp is not None: _raw_laser_retro = _c_tmp.text
        else:
            _raw_laser_retro = el.get("laser_retro")
        if _raw_laser_retro is not None:
            _laser_retro = _parse_double(_raw_laser_retro)
            if isinstance(_laser_retro, SDFError):
                return _laser_retro.extend("@laser_retro")
        else:
            _laser_retro = None
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
            _res = cls.Meta._from_sdf(_c_meta, version)
            if isinstance(_res, SDFError):
                return _res.extend("meta")
            _meta = _res
        else:
            _meta = None
        if _meta is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'meta' is not supported in SDF version {version} (added in 1.5)")
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
        _plugins = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugins.append(_res)
        if _plugins and cmp_version(version, "1.3") < 0:
            return SDFError(f"'plugins' is not supported in SDF version {version} (added in 1.3)")
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
        _raw_transparency = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("transparency")
            if _c_tmp is not None: _raw_transparency = _c_tmp.text
        else:
            _raw_transparency = el.get("transparency")
        if _raw_transparency is not None:
            _transparency = _parse_double(_raw_transparency)
            if isinstance(_transparency, SDFError):
                return _transparency.extend("@transparency")
        else:
            _transparency = None
        _c_tmp = el.find("visibility_flags")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 4294967295
            _val = _parse_uint32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("visibility_flags")
            _visibility_flags = _val
        else:
            _visibility_flags = None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, cast_shadows=_cast_shadows, frames=_frames, geometry=_geometry, laser_retro=_laser_retro, material=_material, meta=_meta, name=_name, origin=_origin, plugins=_plugins, pose=_pose, transparency=_transparency, visibility_flags=_visibility_flags)
