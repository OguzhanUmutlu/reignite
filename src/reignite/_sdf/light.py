### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import _ColorT, _color
from ..utils.pose import _PoseT, _pose
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.pose import Pose

def _parse_color(raw: str) -> _ColorT | SDFError:
    try:
        return _color(raw)
    except ValueError as e:
        return SDFError(str(e))

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
class Light(BaseModel):
    class Attenuation(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            constant: float | None = None,
            linear: float | None = None,
            quadratic: float | None = None,
            range: float | None = None
        ):
            super().__init__(sdf_version)
            self.constant = constant
            self.linear = linear
            self.quadratic = quadratic
            self.range = range

        def to_version(self, target_version: str) -> "Light.Attenuation":
            kwargs: dict = {"sdf_version": target_version, "constant": self.constant, "linear": self.linear, "quadratic": self.quadratic, "range": self.range}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("attenuation")
            if self.constant is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("constant")
                    _c_tmp.text = str(self.constant)
                    el.append(_c_tmp)
                else:
                    el.set("constant", str(self.constant))
            if self.linear is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("linear")
                    _c_tmp.text = str(self.linear)
                    el.append(_c_tmp)
                else:
                    el.set("linear", str(self.linear))
            if self.quadratic is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("quadratic")
                    _c_tmp.text = str(self.quadratic)
                    el.append(_c_tmp)
                else:
                    el.set("quadratic", str(self.quadratic))
            if self.range is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("range")
                    _c_tmp.text = str(self.range)
                    el.append(_c_tmp)
                else:
                    el.set("range", str(self.range))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Light.Attenuation | SDFError":
            _raw_constant = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("constant")
                if _c_tmp is not None: _raw_constant = _c_tmp.text
            else:
                _raw_constant = el.get("constant")
            if _raw_constant is not None:
                _constant = _parse_double(_raw_constant)
                if isinstance(_constant, SDFError):
                    return _constant.extend("@constant")
            else:
                _constant = None
            _raw_linear = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("linear")
                if _c_tmp is not None: _raw_linear = _c_tmp.text
            else:
                _raw_linear = el.get("linear")
            if _raw_linear is not None:
                _linear = _parse_double(_raw_linear)
                if isinstance(_linear, SDFError):
                    return _linear.extend("@linear")
            else:
                _linear = None
            _raw_quadratic = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("quadratic")
                if _c_tmp is not None: _raw_quadratic = _c_tmp.text
            else:
                _raw_quadratic = el.get("quadratic")
            if _raw_quadratic is not None:
                _quadratic = _parse_double(_raw_quadratic)
                if isinstance(_quadratic, SDFError):
                    return _quadratic.extend("@quadratic")
            else:
                _quadratic = None
            _raw_range = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("range")
                if _c_tmp is not None: _raw_range = _c_tmp.text
            else:
                _raw_range = el.get("range")
            if _raw_range is not None:
                _range = _parse_double(_raw_range)
                if isinstance(_range, SDFError):
                    return _range.extend("@range")
            else:
                _range = None
            return cls(sdf_version=version, constant=_constant, linear=_linear, quadratic=_quadratic, range=_range)

    class Diffuse(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            diffuse: _ColorT | None = None,
            rgba: _ColorT | None = None
        ):
            super().__init__(sdf_version)
            self.diffuse = _color(diffuse) if diffuse is not None else None
            self.rgba = _color(rgba) if rgba is not None else None

        def to_version(self, target_version: str) -> "Light.Diffuse":
            kwargs: dict = {"sdf_version": target_version, "diffuse": self.diffuse, "rgba": self.rgba}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("diffuse")
            if self.diffuse is not None:
                el.text = str(self.diffuse)
            if self.rgba is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.rgba)
                else:
                    el.set("rgba", str(self.rgba))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Light.Diffuse | SDFError":
            _raw_diffuse = el.text
            if _raw_diffuse is not None:
                _diffuse = _parse_color(_raw_diffuse)
                if isinstance(_diffuse, SDFError):
                    return _diffuse
            else:
                _diffuse = None
            _raw_rgba = None
            if cmp_version(version, "1.2") >= 0:
                _raw_rgba = el.text
            else:
                _raw_rgba = el.get("rgba")
            if _raw_rgba is not None:
                _rgba = _parse_color(_raw_rgba)
                if isinstance(_rgba, SDFError):
                    return _rgba.extend("@rgba")
            else:
                _rgba = None
            return cls(sdf_version=version, diffuse=_diffuse, rgba=_rgba)

    class Direction(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            direction: _Vector3T | None = None,
            xyz: _Vector3T | None = None
        ):
            super().__init__(sdf_version)
            self.direction = _vector3(direction) if direction is not None else None
            self.xyz = _vector3(xyz) if xyz is not None else None

        def to_version(self, target_version: str) -> "Light.Direction":
            kwargs: dict = {"sdf_version": target_version, "direction": self.direction, "xyz": self.xyz}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("direction")
            if self.direction is not None:
                el.text = str(self.direction)
            if self.xyz is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.xyz)
                else:
                    el.set("xyz", str(self.xyz))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Light.Direction | SDFError":
            _raw_direction = el.text
            if _raw_direction is not None:
                _direction = _parse_vector3(_raw_direction)
                if isinstance(_direction, SDFError):
                    return _direction
            else:
                _direction = None
            _raw_xyz = None
            if cmp_version(version, "1.2") >= 0:
                _raw_xyz = el.text
            else:
                _raw_xyz = el.get("xyz")
            if _raw_xyz is not None:
                _xyz = _parse_vector3(_raw_xyz)
                if isinstance(_xyz, SDFError):
                    return _xyz.extend("@xyz")
            else:
                _xyz = None
            return cls(sdf_version=version, direction=_direction, xyz=_xyz)

    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Light.Origin":
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Light.Origin | SDFError":
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

    class Specular(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            rgba: _ColorT | None = None,
            specular: _ColorT | None = None
        ):
            super().__init__(sdf_version)
            self.rgba = _color(rgba) if rgba is not None else None
            self.specular = _color(specular) if specular is not None else None

        def to_version(self, target_version: str) -> "Light.Specular":
            kwargs: dict = {"sdf_version": target_version, "rgba": self.rgba, "specular": self.specular}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("specular")
            if self.rgba is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.rgba)
                else:
                    el.set("rgba", str(self.rgba))
            if self.specular is not None:
                el.text = str(self.specular)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Light.Specular | SDFError":
            _raw_rgba = None
            if cmp_version(version, "1.2") >= 0:
                _raw_rgba = el.text
            else:
                _raw_rgba = el.get("rgba")
            if _raw_rgba is not None:
                _rgba = _parse_color(_raw_rgba)
                if isinstance(_rgba, SDFError):
                    return _rgba.extend("@rgba")
            else:
                _rgba = None
            _raw_specular = el.text
            if _raw_specular is not None:
                _specular = _parse_color(_raw_specular)
                if isinstance(_specular, SDFError):
                    return _specular
            else:
                _specular = None
            return cls(sdf_version=version, rgba=_rgba, specular=_specular)

    class Spot(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            falloff: float | None = None,
            inner_angle: float | None = None,
            outer_angle: float | None = None
        ):
            super().__init__(sdf_version)
            self.falloff = falloff
            self.inner_angle = inner_angle
            self.outer_angle = outer_angle

        def to_version(self, target_version: str) -> "Light.Spot":
            kwargs: dict = {"sdf_version": target_version, "falloff": self.falloff, "inner_angle": self.inner_angle, "outer_angle": self.outer_angle}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("spot")
            if self.falloff is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("falloff")
                    _c_tmp.text = str(self.falloff)
                    el.append(_c_tmp)
                else:
                    el.set("falloff", str(self.falloff))
            if self.inner_angle is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("inner_angle")
                    _c_tmp.text = str(self.inner_angle)
                    el.append(_c_tmp)
                else:
                    el.set("inner_angle", str(self.inner_angle))
            if self.outer_angle is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("outer_angle")
                    _c_tmp.text = str(self.outer_angle)
                    el.append(_c_tmp)
                else:
                    el.set("outer_angle", str(self.outer_angle))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Light.Spot | SDFError":
            _raw_falloff = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("falloff")
                if _c_tmp is not None: _raw_falloff = _c_tmp.text
            else:
                _raw_falloff = el.get("falloff")
            if _raw_falloff is not None:
                _falloff = _parse_double(_raw_falloff)
                if isinstance(_falloff, SDFError):
                    return _falloff.extend("@falloff")
            else:
                _falloff = None
            _raw_inner_angle = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("inner_angle")
                if _c_tmp is not None: _raw_inner_angle = _c_tmp.text
            else:
                _raw_inner_angle = el.get("inner_angle")
            if _raw_inner_angle is not None:
                _inner_angle = _parse_double(_raw_inner_angle)
                if isinstance(_inner_angle, SDFError):
                    return _inner_angle.extend("@inner_angle")
            else:
                _inner_angle = None
            _raw_outer_angle = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("outer_angle")
                if _c_tmp is not None: _raw_outer_angle = _c_tmp.text
            else:
                _raw_outer_angle = el.get("outer_angle")
            if _raw_outer_angle is not None:
                _outer_angle = _parse_double(_raw_outer_angle)
                if isinstance(_outer_angle, SDFError):
                    return _outer_angle.extend("@outer_angle")
            else:
                _outer_angle = None
            return cls(sdf_version=version, falloff=_falloff, inner_angle=_inner_angle, outer_angle=_outer_angle)

    def __init__(
        self,
        sdf_version: str | None = None,
        attenuation: "Light.Attenuation" = None,
        cast_shadows: bool | None = None,
        diffuse: "Light.Diffuse" = None,
        direction: "Light.Direction" = None,
        frames: List["Frame"] = None,
        intensity: float | None = None,
        light_on: bool | None = None,
        name: str | None = None,
        origin: "Light.Origin" = None,
        pose: "Pose" = None,
        specular: "Light.Specular" = None,
        spot: "Light.Spot" = None,
        type: str | None = None,
        visualize: bool | None = None
    ):
        super().__init__(sdf_version)
        self.attenuation = attenuation
        self.cast_shadows = cast_shadows
        self.diffuse = diffuse
        self.direction = direction
        self.frames = frames or []
        self.intensity = intensity
        self.light_on = light_on
        self.name = name
        self.origin = origin
        self.pose = pose
        self.specular = specular
        self.spot = spot
        self.type = type
        self.visualize = visualize
        if self.attenuation is not None and hasattr(self.attenuation, 'to_version'):
            if getattr(self.attenuation, 'sdfversion', None) is None:
                self.attenuation.sdfversion = self.sdfversion
            elif getattr(self.attenuation, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.attenuation = self.attenuation.to_version(self.sdfversion)
        if self.diffuse is not None and hasattr(self.diffuse, 'to_version'):
            if getattr(self.diffuse, 'sdfversion', None) is None:
                self.diffuse.sdfversion = self.sdfversion
            elif getattr(self.diffuse, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.diffuse = self.diffuse.to_version(self.sdfversion)
        if self.direction is not None and hasattr(self.direction, 'to_version'):
            if getattr(self.direction, 'sdfversion', None) is None:
                self.direction.sdfversion = self.sdfversion
            elif getattr(self.direction, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.direction = self.direction.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, 'sdfversion', None) is None:
                self.origin.sdfversion = self.sdfversion
            elif getattr(self.origin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.origin = self.origin.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)
        if self.specular is not None and hasattr(self.specular, 'to_version'):
            if getattr(self.specular, 'sdfversion', None) is None:
                self.specular.sdfversion = self.sdfversion
            elif getattr(self.specular, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.specular = self.specular.to_version(self.sdfversion)
        if self.spot is not None and hasattr(self.spot, 'to_version'):
            if getattr(self.spot, 'sdfversion', None) is None:
                self.spot.sdfversion = self.sdfversion
            elif getattr(self.spot, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.spot = self.spot.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def to_version(self, target_version: str) -> "Light":
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.intensity is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.8)")
        if self.light_on is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.8)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.visualize is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.8)")
        kwargs: dict = {"sdf_version": target_version, "attenuation": self.attenuation.to_version(target_version) if self.attenuation is not None and hasattr(self.attenuation, "to_version") else self.attenuation, "cast_shadows": self.cast_shadows, "diffuse": self.diffuse.to_version(target_version) if self.diffuse is not None and hasattr(self.diffuse, "to_version") else self.diffuse, "direction": self.direction.to_version(target_version) if self.direction is not None and hasattr(self.direction, "to_version") else self.direction, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "intensity": self.intensity, "light_on": self.light_on, "name": self.name, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "specular": self.specular.to_version(target_version) if self.specular is not None and hasattr(self.specular, "to_version") else self.specular, "spot": self.spot.to_version(target_version) if self.spot is not None and hasattr(self.spot, "to_version") else self.spot, "type": self.type, "visualize": self.visualize}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("light")
        if self.attenuation is not None:
            _child_res = self.attenuation.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('attenuation')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.cast_shadows is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("cast_shadows")
                _c_tmp.text = str(self.cast_shadows).lower()
                el.append(_c_tmp)
            else:
                el.set("cast_shadows", str(self.cast_shadows).lower())
        if self.diffuse is not None:
            _child_res = self.diffuse.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('diffuse')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.direction is not None:
            _child_res = self.direction.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('direction')
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
        if self.intensity is not None:
            _c_tmp = ET.Element("intensity")
            _c_tmp.text = str(self.intensity)
            el.append(_c_tmp)
        if self.light_on is not None:
            _c_tmp = ET.Element("light_on")
            _c_tmp.text = str(self.light_on).lower()
            el.append(_c_tmp)
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
        if self.pose is not None:
            _child_res = self.pose.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.specular is not None:
            _child_res = self.specular.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('specular')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.spot is not None:
            _child_res = self.spot.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('spot')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.type is not None:
            el.set("type", self.type)
        if self.visualize is not None:
            _c_tmp = ET.Element("visualize")
            _c_tmp.text = str(self.visualize).lower()
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Light | SDFError":
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        _c_attenuation = el.find("attenuation")
        if _c_attenuation is not None:
            _res = cls.Attenuation._from_sdf(_c_attenuation, version)
            if isinstance(_res, SDFError):
                return _res.extend("attenuation")
            _attenuation = _res
        else:
            _attenuation = None
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
        _c_diffuse = el.find("diffuse")
        if _c_diffuse is not None:
            _res = cls.Diffuse._from_sdf(_c_diffuse, version)
            if isinstance(_res, SDFError):
                return _res.extend("diffuse")
            _diffuse = _res
        else:
            _diffuse = None
        _c_direction = el.find("direction")
        if _c_direction is not None:
            _res = cls.Direction._from_sdf(_c_direction, version)
            if isinstance(_res, SDFError):
                return _res.extend("direction")
            _direction = _res
        else:
            _direction = None
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _c_tmp = el.find("intensity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("intensity")
            _intensity = _val
        else:
            _intensity = None
        if _intensity is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'intensity' is not supported in SDF version {version} (added in 1.8)")
        _c_tmp = el.find("light_on")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else True
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("light_on")
            _light_on = _val
        else:
            _light_on = None
        if _light_on is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'light_on' is not supported in SDF version {version} (added in 1.8)")
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
        _c_specular = el.find("specular")
        if _c_specular is not None:
            _res = cls.Specular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        _c_spot = el.find("spot")
        if _c_spot is not None:
            _res = cls.Spot._from_sdf(_c_spot, version)
            if isinstance(_res, SDFError):
                return _res.extend("spot")
            _spot = _res
        else:
            _spot = None
        _raw_type = el.get("type")
        if _raw_type is not None:
            _type = _raw_type
            if isinstance(_type, SDFError):
                return _type.extend("@type")
        else:
            _type = None
        _c_tmp = el.find("visualize")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else True
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("visualize")
            _visualize = _val
        else:
            _visualize = None
        if _visualize is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.8)")
        return cls(sdf_version=version, attenuation=_attenuation, cast_shadows=_cast_shadows, diffuse=_diffuse, direction=_direction, frames=_frames, intensity=_intensity, light_on=_light_on, name=_name, origin=_origin, pose=_pose, specular=_specular, spot=_spot, type=_type, visualize=_visualize)
