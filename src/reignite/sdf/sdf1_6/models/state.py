from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .deletions import Deletions
from .insertions import Insertions
from .iterations import Iterations
from .model import Model
from .real_time import RealTime
from .sim_time import SimTime
from .wall_time import WallTime
from ..model import Model
from ...sdf1_5.models.attenuation import Attenuation as _PrevAttenuation
from ...sdf1_5.models.cast_shadows import CastShadows as _PrevCastShadows
from ...sdf1_5.models.constant import Constant as _PrevConstant
from ...sdf1_5.models.diffuse import Diffuse as _PrevDiffuse
from ...sdf1_5.models.direction import Direction as _PrevDirection
from ...sdf1_5.models.falloff import Falloff as _PrevFalloff
from ...sdf1_5.models.frame import Frame as _PrevFrame
from ...sdf1_5.models.inner_angle import InnerAngle as _PrevInnerAngle
from ...sdf1_5.models.light import Light as _PrevLight
from ...sdf1_5.models.outer_angle import OuterAngle as _PrevOuterAngle
from ...sdf1_5.models.pose import Pose as _PrevPose
from ...sdf1_5.models.quadratic import Quadratic as _PrevQuadratic
from ...sdf1_5.models.range import Range as _PrevRange
from ...sdf1_5.models.specular import Specular as _PrevSpecular
from ...sdf1_5.models.spot import Spot as _PrevSpot
from ...sdf1_5.models.state import State as _PrevState
from ....utils.color import Color
from ....utils.pose import Pose


def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class Pose(_PrevPose):
    def __init__(self, pose: Pose = None, frame: str = ""):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose, frame=frame)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        return cls(pose=_base.pose, frame=_base.frame)


class Frame(_PrevFrame):
    def __init__(self, name: str = "", pose: "Pose" = None):
        super().__init__(name=name, pose=pose)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frame":
        _base = _PrevFrame.from_sdf(el)
        return cls(name=_base.name, pose=_base.pose)


class CastShadows(_PrevCastShadows):
    def __init__(self, cast_shadows: bool = False):
        super().__init__(cast_shadows=cast_shadows)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CastShadows":
        _base = _PrevCastShadows.from_sdf(el)
        return cls(cast_shadows=_base.cast_shadows)


class Diffuse(_PrevDiffuse):
    def __init__(self, diffuse: Color = None):
        if diffuse is None:
            diffuse = Color.from_sdf("1 1 1 1")
        super().__init__(diffuse=diffuse)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _base = _PrevDiffuse.from_sdf(el)
        return cls(diffuse=_base.diffuse)


class Specular(_PrevSpecular):
    def __init__(self, specular: Color = None):
        if specular is None:
            specular = Color.from_sdf(".1 .1 .1 1")
        super().__init__(specular=specular)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _base = _PrevSpecular.from_sdf(el)
        return cls(specular=_base.specular)


class Range(_PrevRange):
    def __init__(self, range: float = 10):
        super().__init__(range=range)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Range":
        _base = _PrevRange.from_sdf(el)
        return cls(range=_base.range)


class Constant(_PrevConstant):
    def __init__(self, constant: float = 1):
        super().__init__(constant=constant)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Constant":
        _base = _PrevConstant.from_sdf(el)
        return cls(constant=_base.constant)


class Quadratic(_PrevQuadratic):
    def __init__(self, quadratic: float = 0):
        super().__init__(quadratic=quadratic)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Quadratic":
        _base = _PrevQuadratic.from_sdf(el)
        return cls(quadratic=_base.quadratic)


class Attenuation(_PrevAttenuation):
    def __init__(
            self,
            range: "Range" = None,
            linear: "Linear" = None,
            constant: "Constant" = None,
            quadratic: "Quadratic" = None
    ):
        super().__init__(range=range, linear=linear, constant=constant, quadratic=quadratic)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Attenuation":
        _base = _PrevAttenuation.from_sdf(el)
        return cls(range=_base.range, linear=_base.linear, constant=_base.constant, quadratic=_base.quadratic)


class Direction(_PrevDirection):
    def __init__(self, direction: float = 0.0):
        super().__init__(direction=direction)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Direction":
        _base = _PrevDirection.from_sdf(el)
        return cls(direction=_base.direction)


class InnerAngle(_PrevInnerAngle):
    def __init__(self, inner_angle: float = 0):
        super().__init__(inner_angle=inner_angle)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "InnerAngle":
        _base = _PrevInnerAngle.from_sdf(el)
        return cls(inner_angle=_base.inner_angle)


class OuterAngle(_PrevOuterAngle):
    def __init__(self, outer_angle: float = 0):
        super().__init__(outer_angle=outer_angle)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "OuterAngle":
        _base = _PrevOuterAngle.from_sdf(el)
        return cls(outer_angle=_base.outer_angle)


class Falloff(_PrevFalloff):
    def __init__(self, falloff: float = 0):
        super().__init__(falloff=falloff)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Falloff":
        _base = _PrevFalloff.from_sdf(el)
        return cls(falloff=_base.falloff)


class Spot(_PrevSpot):
    def __init__(
            self,
            inner_angle: "InnerAngle" = None,
            outer_angle: "OuterAngle" = None,
            falloff: "Falloff" = None
    ):
        super().__init__(inner_angle=inner_angle, outer_angle=outer_angle, falloff=falloff)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Spot":
        _base = _PrevSpot.from_sdf(el)
        return cls(inner_angle=_base.inner_angle, outer_angle=_base.outer_angle, falloff=_base.falloff)


class Light(_PrevLight):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "point",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            cast_shadows: "CastShadows" = None,
            diffuse: "Diffuse" = None,
            specular: "Specular" = None,
            attenuation: "Attenuation" = None,
            direction: "Direction" = None,
            spot: "Spot" = None
    ):
        super().__init__(name=name, type=type, frame=frame, pose=pose, cast_shadows=cast_shadows, diffuse=diffuse,
                         specular=specular, attenuation=attenuation, direction=direction, spot=spot)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Light":
        _base = _PrevLight.from_sdf(el)
        return cls(name=_base.name, type=_base.type, frame=_base.frame, pose=_base.pose,
                   cast_shadows=_base.cast_shadows, diffuse=_base.diffuse, specular=_base.specular,
                   attenuation=_base.attenuation, direction=_base.direction, spot=_base.spot)


class State(_PrevState):
    def __init__(
            self,
            world_name: str = "__default__",
            model: List["Model"] = None,
            light: List["Light"] = None,
            sim_time: "SimTime" = None,
            wall_time: "WallTime" = None,
            real_time: "RealTime" = None,
            iterations: "Iterations" = None,
            insertions: "Insertions" = None,
            deletions: "Deletions" = None
    ):
        super().__init__(world_name=world_name, model=model, light=light, sim_time=sim_time, wall_time=wall_time,
                         real_time=real_time, iterations=iterations, insertions=insertions, deletions=deletions)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "State":
        _base = _PrevState.from_sdf(el)
        return cls(world_name=_base.world_name, model=_base.model, light=_base.light, sim_time=_base.sim_time,
                   wall_time=_base.wall_time, real_time=_base.real_time, iterations=_base.iterations,
                   insertions=_base.insertions, deletions=_base.deletions)
