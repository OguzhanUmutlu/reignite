### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color as _SDFColor
from ..utils.pose import Pose as _SDFPose
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations


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


class Diffuse(BaseModel):
    def __init__(self, sdf_version: str, diffuse: _SDFColor = None, rgba: _SDFColor = None):
        self.__version__ = sdf_version
        if diffuse is None:
            diffuse = _SDFColor.from_sdf("1 1 1 1")
        if rgba is None:
            rgba = _SDFColor.from_sdf("1 1 1 1")
        self.diffuse = diffuse
        self.rgba = rgba

    def to_version(self, target_version: str) -> "Diffuse":
        if self.diffuse is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'diffuse' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["diffuse"] = self.diffuse
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse.to_sdf()
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1 1"
        _diffuse = _SDFColor._from_sdf(_text, version)
        if isinstance(_diffuse, SDFError):
            return _diffuse
        _rgba = _SDFColor._from_sdf(el.get("rgba", "1 1 1 1"), version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        return cls(sdf_version=version, diffuse=_diffuse, rgba=_rgba)


class Specular(BaseModel):
    def __init__(self, sdf_version: str, rgba: _SDFColor = None, specular: _SDFColor = None):
        self.__version__ = sdf_version
        if rgba is None:
            rgba = _SDFColor.from_sdf(".1 .1 .1 1")
        if specular is None:
            specular = _SDFColor.from_sdf(".1 .1 .1 1")
        self.rgba = rgba
        self.specular = specular

    def to_version(self, target_version: str) -> "Specular":
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.specular is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'specular' is not supported in SDF version {target_version} (removed in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["rgba"] = self.rgba
        kwargs["specular"] = self.specular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _rgba = _SDFColor._from_sdf(el.get("rgba", ".1 .1 .1 1"), version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        _text = el.text or ".1 .1 .1 1"
        _specular = _SDFColor._from_sdf(_text, version)
        if isinstance(_specular, SDFError):
            return _specular
        return cls(sdf_version=version, rgba=_rgba, specular=_specular)


class Quadratic(BaseModel):
    def __init__(self, sdf_version: str, quadratic: float = 0):
        self.__version__ = sdf_version
        self.quadratic = quadratic

    def to_version(self, target_version: str) -> "Quadratic":
        if self.quadratic is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'quadratic' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["quadratic"] = self.quadratic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("quadratic")
        if self.quadratic is not None:
            el.text = str(self.quadratic)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _quadratic = _parse_double(_text)
        if isinstance(_quadratic, SDFError):
            return _quadratic
        if _quadratic is not None and cmp_version(version, "1.2") < 0:
            if _quadratic != 0:
                return SDFError(f"'quadratic' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, quadratic=_quadratic)


class Constant(BaseModel):
    def __init__(self, sdf_version: str, constant: float = 1):
        self.__version__ = sdf_version
        self.constant = constant

    def to_version(self, target_version: str) -> "Constant":
        if self.constant is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'constant' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["constant"] = self.constant
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("constant")
        if self.constant is not None:
            el.text = str(self.constant)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _constant = _parse_double(_text)
        if isinstance(_constant, SDFError):
            return _constant
        if _constant is not None and cmp_version(version, "1.2") < 0:
            if _constant != 1:
                return SDFError(f"'constant' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, constant=_constant)


class Range(BaseModel):
    def __init__(self, sdf_version: str, range: float = 10):
        self.__version__ = sdf_version
        self.range = range

    def to_version(self, target_version: str) -> "Range":
        if self.range is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'range' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["range"] = self.range
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.range is not None:
            el.text = str(self.range)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _range = _parse_double(_text)
        if isinstance(_range, SDFError):
            return _range
        if _range is not None and cmp_version(version, "1.2") < 0:
            if _range != 10:
                return SDFError(f"'range' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, range=_range)


class Linear(BaseModel):
    def __init__(self, sdf_version: str, linear: float = 1):
        self.__version__ = sdf_version
        self.linear = linear

    def to_version(self, target_version: str) -> "Linear":
        if self.linear is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'linear' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["linear"] = self.linear
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear")
        if self.linear is not None:
            el.text = str(self.linear)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _linear = _parse_double(_text)
        if isinstance(_linear, SDFError):
            return _linear
        if _linear is not None and cmp_version(version, "1.2") < 0:
            if _linear != 1:
                return SDFError(f"'linear' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, linear=_linear)


class Attenuation(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        constant: float = 1,
        linear: float = 1,
        quadratic: float = 0,
        range: float = 10
    ):
        self.__version__ = sdf_version
        self.constant = constant
        self.linear = linear
        self.quadratic = quadratic
        self.range = range

    def to_version(self, target_version: str) -> "Attenuation":
        if self.constant is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'constant' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.linear is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'linear' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.quadratic is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'quadratic' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.range is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'range' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["constant"] = self.constant
        kwargs["linear"] = self.linear
        kwargs["quadratic"] = self.quadratic
        kwargs["range"] = self.range
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("attenuation")
        if self.constant is not None:
            el.set("constant", str(self.constant))
        if self.linear is not None:
            el.set("linear", str(self.linear))
        if self.quadratic is not None:
            el.set("quadratic", str(self.quadratic))
        if self.range is not None:
            el.set("range", str(self.range))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _constant = _parse_double(el.get("constant", 1))
        if isinstance(_constant, SDFError):
            return _constant.extend("@constant")
        _linear = _parse_double(el.get("linear", 1))
        if isinstance(_linear, SDFError):
            return _linear.extend("@linear")
        _quadratic = _parse_double(el.get("quadratic", 0))
        if isinstance(_quadratic, SDFError):
            return _quadratic.extend("@quadratic")
        _range = _parse_double(el.get("range", 10))
        if isinstance(_range, SDFError):
            return _range.extend("@range")
        return cls(sdf_version=version, constant=_constant, linear=_linear, quadratic=_quadratic, range=_range)


class Direction(BaseModel):
    def __init__(self, sdf_version: str, direction: _SDFVector3 = None, xyz: _SDFVector3 = None):
        self.__version__ = sdf_version
        if direction is None:
            direction = _SDFVector3.from_sdf("0 0 -1")
        if xyz is None:
            xyz = _SDFVector3.from_sdf("0 0 -1")
        self.direction = direction
        self.xyz = xyz

    def to_version(self, target_version: str) -> "Direction":
        if self.direction is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'direction' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.xyz is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["direction"] = self.direction
        kwargs["xyz"] = self.xyz
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("direction")
        if self.direction is not None:
            el.text = self.direction.to_sdf()
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 -1"
        _direction = _SDFVector3._from_sdf(_text, version)
        if isinstance(_direction, SDFError):
            return _direction
        _xyz = _SDFVector3._from_sdf(el.get("xyz", "0 0 -1"), version)
        if isinstance(_xyz, SDFError):
            return _xyz.extend("@xyz")
        return cls(sdf_version=version, direction=_direction, xyz=_xyz)


class Falloff(BaseModel):
    def __init__(self, sdf_version: str, falloff: float = 0):
        self.__version__ = sdf_version
        self.falloff = falloff

    def to_version(self, target_version: str) -> "Falloff":
        if self.falloff is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'falloff' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["falloff"] = self.falloff
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("falloff")
        if self.falloff is not None:
            el.text = str(self.falloff)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _falloff = _parse_double(_text)
        if isinstance(_falloff, SDFError):
            return _falloff
        if _falloff is not None and cmp_version(version, "1.2") < 0:
            if _falloff != 0:
                return SDFError(f"'falloff' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, falloff=_falloff)


class InnerAngle(BaseModel):
    def __init__(self, sdf_version: str, inner_angle: float = 0):
        self.__version__ = sdf_version
        self.inner_angle = inner_angle

    def to_version(self, target_version: str) -> "InnerAngle":
        if self.inner_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'inner_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["inner_angle"] = self.inner_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("inner_angle")
        if self.inner_angle is not None:
            el.text = str(self.inner_angle)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _inner_angle = _parse_double(_text)
        if isinstance(_inner_angle, SDFError):
            return _inner_angle
        if _inner_angle is not None and cmp_version(version, "1.2") < 0:
            if _inner_angle != 0:
                return SDFError(f"'inner_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, inner_angle=_inner_angle)


class OuterAngle(BaseModel):
    def __init__(self, sdf_version: str, outer_angle: float = 0):
        self.__version__ = sdf_version
        self.outer_angle = outer_angle

    def to_version(self, target_version: str) -> "OuterAngle":
        if self.outer_angle is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'outer_angle' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["outer_angle"] = self.outer_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("outer_angle")
        if self.outer_angle is not None:
            el.text = str(self.outer_angle)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _outer_angle = _parse_double(_text)
        if isinstance(_outer_angle, SDFError):
            return _outer_angle
        if _outer_angle is not None and cmp_version(version, "1.2") < 0:
            if _outer_angle != 0:
                return SDFError(f"'outer_angle' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, outer_angle=_outer_angle)


class Spot(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        falloff: float = 0,
        inner_angle: float = 0,
        outer_angle: float = 0
    ):
        self.__version__ = sdf_version
        self.falloff = falloff
        self.inner_angle = inner_angle
        self.outer_angle = outer_angle

    def to_version(self, target_version: str) -> "Spot":
        if self.falloff is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'falloff' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.inner_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'inner_angle' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.outer_angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'outer_angle' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["falloff"] = self.falloff
        kwargs["inner_angle"] = self.inner_angle
        kwargs["outer_angle"] = self.outer_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spot")
        if self.falloff is not None:
            el.set("falloff", str(self.falloff))
        if self.inner_angle is not None:
            el.set("inner_angle", str(self.inner_angle))
        if self.outer_angle is not None:
            el.set("outer_angle", str(self.outer_angle))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _falloff = _parse_double(el.get("falloff", 0))
        if isinstance(_falloff, SDFError):
            return _falloff.extend("@falloff")
        _inner_angle = _parse_double(el.get("inner_angle", 0))
        if isinstance(_inner_angle, SDFError):
            return _inner_angle.extend("@inner_angle")
        _outer_angle = _parse_double(el.get("outer_angle", 0))
        if isinstance(_outer_angle, SDFError):
            return _outer_angle.extend("@outer_angle")
        return cls(sdf_version=version, falloff=_falloff, inner_angle=_inner_angle, outer_angle=_outer_angle)


class CastShadows(BaseModel):
    def __init__(self, sdf_version: str, cast_shadows: bool = False):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows

    def to_version(self, target_version: str) -> "CastShadows":
        if self.cast_shadows is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'cast_shadows' is not supported in SDF version {target_version} (added in 1.2)")
        if self.cast_shadows is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'cast_shadows' is not supported in SDF version {target_version} (removed in 1.5)")
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
        _text = el.text or False
        _cast_shadows = str(_text).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows
        if _cast_shadows is not None and cmp_version(version, "1.2") < 0:
            if _cast_shadows != False:
                return SDFError(f"'cast_shadows' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, cast_shadows=_cast_shadows)


class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        degrees: bool = False,
        frame: str = "",
        pose: _SDFPose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy"
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.degrees = degrees
        self.frame = frame
        self.pose = pose
        self.relative_to = relative_to
        self.rotation_format = rotation_format

    def to_version(self, target_version: str) -> "Pose":
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["degrees"] = self.degrees
        kwargs["frame"] = self.frame
        kwargs["pose"] = self.pose
        kwargs["relative_to"] = self.relative_to
        kwargs["rotation_format"] = self.rotation_format
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        if _pose is not None and cmp_version(version, "1.2") < 0:
            if _pose != "0 0 0 0 0 0":
                return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, degrees=_degrees, frame=_frame, pose=_pose, relative_to=_relative_to, rotation_format=_rotation_format)


class FramePose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(self, sdf_version: str, frame: str = "", pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.frame = frame
        self.pose = pose

    def to_version(self, target_version: str) -> "FramePose":
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        return cls(sdf_version=version, frame=_frame, pose=_pose)


class Frame(BaseModel):
    def __init__(self, sdf_version: str, name: str = "", pose: "FramePose" = None):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "Frame":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = FramePose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, name=_name, pose=_pose)


class LightOn(BaseModel):
    def __init__(self, sdf_version: str, light_on: bool = True):
        self.__version__ = sdf_version
        self.light_on = light_on

    def to_version(self, target_version: str) -> "LightOn":
        if self.light_on is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["light_on"] = self.light_on
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light_on")
        if self.light_on is not None:
            el.text = str(self.light_on).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _light_on = str(_text).strip().lower() == 'true'
        if isinstance(_light_on, SDFError):
            return _light_on
        if _light_on is not None and cmp_version(version, "1.12") < 0:
            if _light_on != True:
                return SDFError(f"'light_on' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, light_on=_light_on)


class Visualize(BaseModel):
    def __init__(self, sdf_version: str, visualize: bool = True):
        self.__version__ = sdf_version
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Visualize":
        if self.visualize is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["visualize"] = self.visualize
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visualize")
        if self.visualize is not None:
            el.text = str(self.visualize).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _visualize = str(_text).strip().lower() == 'true'
        if isinstance(_visualize, SDFError):
            return _visualize
        if _visualize is not None and cmp_version(version, "1.12") < 0:
            if _visualize != True:
                return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, visualize=_visualize)


class Intensity(BaseModel):
    def __init__(self, sdf_version: str, intensity: float = 1):
        self.__version__ = sdf_version
        self.intensity = intensity

    def to_version(self, target_version: str) -> "Intensity":
        if self.intensity is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["intensity"] = self.intensity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("intensity")
        if self.intensity is not None:
            el.text = str(self.intensity)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _intensity = _parse_double(_text)
        if isinstance(_intensity, SDFError):
            return _intensity
        if _intensity is not None and cmp_version(version, "1.12") < 0:
            if _intensity != 1:
                return SDFError(f"'intensity' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, intensity=_intensity)


class Light(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        attenuation: "Attenuation" = None,
        cast_shadows: bool = False,
        diffuse: "Diffuse" = None,
        direction: "Direction" = None,
        frame: List["Frame"] = None,
        intensity: "Intensity" = None,
        light_on: "LightOn" = None,
        name: str = "__default__",
        origin: "Origin" = None,
        pose: "Pose" = None,
        specular: "Specular" = None,
        spot: "Spot" = None,
        type: str = "point",
        visualize: "Visualize" = None
    ):
        self.__version__ = sdf_version
        self.attenuation = attenuation
        self.cast_shadows = cast_shadows
        self.diffuse = diffuse
        self.direction = direction
        self.frame = frame or []
        self.intensity = intensity
        self.light_on = light_on
        self.name = name
        self.origin = origin
        self.pose = pose
        self.specular = specular
        self.spot = spot
        self.type = type
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Light":
        if self.attenuation is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'attenuation' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.cast_shadows is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'cast_shadows' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.diffuse is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'diffuse' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.direction is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'direction' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.intensity is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'intensity' is not supported in SDF version {target_version} (added in 1.12)")
        if self.light_on is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'light_on' is not supported in SDF version {target_version} (added in 1.12)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.specular is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'specular' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.spot is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'spot' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.type is not None and cmp_version(target_version, "1.5") >= 0:
            raise ValueError(f"'type' is not supported in SDF version {target_version} (removed in 1.5)")
        if self.visualize is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["attenuation"] = self.attenuation.to_version(target_version) if self.attenuation is not None else None
        kwargs["cast_shadows"] = self.cast_shadows
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["direction"] = self.direction.to_version(target_version) if self.direction is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["intensity"] = self.intensity.to_version(target_version) if self.intensity is not None else None
        kwargs["light_on"] = self.light_on.to_version(target_version) if self.light_on is not None else None
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["spot"] = self.spot.to_version(target_version) if self.spot is not None else None
        kwargs["type"] = self.type
        kwargs["visualize"] = self.visualize.to_version(target_version) if self.visualize is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light")
        if self.attenuation is not None:
            el.append(self.attenuation.to_sdf(version))
        if self.cast_shadows is not None:
            el.set("cast_shadows", str(self.cast_shadows).lower())
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.direction is not None:
            el.append(self.direction.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.intensity is not None:
            el.append(self.intensity.to_sdf(version))
        if self.light_on is not None:
            el.append(self.light_on.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.specular is not None:
            el.append(self.specular.to_sdf(version))
        if self.spot is not None:
            el.append(self.spot.to_sdf(version))
        if self.type is not None:
            el.set("type", self.type)
        if self.visualize is not None:
            el.append(self.visualize.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_attenuation = el.find("attenuation")
        if _c_attenuation is not None:
            _res = Attenuation._from_sdf(_c_attenuation, version)
            if isinstance(_res, SDFError):
                return _res.extend("attenuation")
            _attenuation = _res
        else:
            _attenuation = None
        _cast_shadows = str(el.get("cast_shadows", False)).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows.extend("@cast_shadows")
        _c_diffuse = el.find("diffuse")
        if _c_diffuse is not None:
            _res = Diffuse._from_sdf(_c_diffuse, version)
            if isinstance(_res, SDFError):
                return _res.extend("diffuse")
            _diffuse = _res
        else:
            _diffuse = None
        _c_direction = el.find("direction")
        if _c_direction is not None:
            _res = Direction._from_sdf(_c_direction, version)
            if isinstance(_res, SDFError):
                return _res.extend("direction")
            _direction = _res
        else:
            _direction = None
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_intensity = el.find("intensity")
        if _c_intensity is not None:
            _res = Intensity._from_sdf(_c_intensity, version)
            if isinstance(_res, SDFError):
                return _res.extend("intensity")
            _intensity = _res
        else:
            _intensity = None
        if _intensity is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'intensity' is not supported in SDF version {version} (added in 1.12)")
        _c_light_on = el.find("light_on")
        if _c_light_on is not None:
            _res = LightOn._from_sdf(_c_light_on, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_on")
            _light_on = _res
        else:
            _light_on = None
        if _light_on is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'light_on' is not supported in SDF version {version} (added in 1.12)")
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
            _res = Specular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        _c_spot = el.find("spot")
        if _c_spot is not None:
            _res = Spot._from_sdf(_c_spot, version)
            if isinstance(_res, SDFError):
                return _res.extend("spot")
            _spot = _res
        else:
            _spot = None
        _type = el.get("type", "point")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_visualize = el.find("visualize")
        if _c_visualize is not None:
            _res = Visualize._from_sdf(_c_visualize, version)
            if isinstance(_res, SDFError):
                return _res.extend("visualize")
            _visualize = _res
        else:
            _visualize = None
        if _visualize is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, attenuation=_attenuation, cast_shadows=_cast_shadows, diffuse=_diffuse, direction=_direction, frame=_frame, intensity=_intensity, light_on=_light_on, name=_name, origin=_origin, pose=_pose, specular=_specular, spot=_spot, type=_type, visualize=_visualize)
