from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from .actor import Actor
from .atmosphere import Atmosphere
from .audio import Audio
from .gravity import Gravity
from .gui import Gui
from .include import Include
from .joint import Joint
from .magnetic_field import MagneticField
from .model import Model
from .plugin import Plugin
from .population import Population
from .road import Road
from .scene import Scene
from .spherical_coordinates import SphericalCoordinates
from .state import State
from .wind import Wind
from ..model import Model
from ...sdf1_5.models.attenuation import Attenuation as _PrevAttenuation
from ...sdf1_5.models.bullet import Bullet as _PrevBullet
from ...sdf1_5.models.cast_shadows import CastShadows as _PrevCastShadows
from ...sdf1_5.models.constant import Constant as _PrevConstant
from ...sdf1_5.models.contact import Contact as _PrevContact
from ...sdf1_5.models.dart import Dart as _PrevDart
from ...sdf1_5.models.diffuse import Diffuse as _PrevDiffuse
from ...sdf1_5.models.direction import Direction as _PrevDirection
from ...sdf1_5.models.falloff import Falloff as _PrevFalloff
from ...sdf1_5.models.frame import Frame as _PrevFrame
from ...sdf1_5.models.inner_angle import InnerAngle as _PrevInnerAngle
from ...sdf1_5.models.light import Light as _PrevLight
from ...sdf1_5.models.ode import Ode as _PrevOde
from ...sdf1_5.models.outer_angle import OuterAngle as _PrevOuterAngle
from ...sdf1_5.models.physics import Physics as _PrevPhysics
from ...sdf1_5.models.pose import Pose as _PrevPose
from ...sdf1_5.models.quadratic import Quadratic as _PrevQuadratic
from ...sdf1_5.models.range import Range as _PrevRange
from ...sdf1_5.models.simbody import Simbody as _PrevSimbody
from ...sdf1_5.models.specular import Specular as _PrevSpecular
from ...sdf1_5.models.spot import Spot as _PrevSpot
from ...sdf1_5.models.world import World as _PrevWorld
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


class Dart(_PrevDart):
    def __init__(self, solver: "Solver" = None, collision_detector: "CollisionDetector" = None):
        super().__init__()
        self.solver = solver
        self.collision_detector = collision_detector

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.solver is not None:
            el.append(self.solver.to_sdf())
        if self.collision_detector is not None:
            el.append(self.collision_detector.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dart":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver) if _c_solver is not None else None
        _c_collision_detector = el.find("collision_detector")
        _collision_detector = CollisionDetector.from_sdf(
            _c_collision_detector) if _c_collision_detector is not None else None
        return cls(solver=_solver, collision_detector=_collision_detector)


class Contact(_PrevContact):
    def __init__(
            self,
            stiffness: "Stiffness" = None,
            dissipation: "Dissipation" = None,
            plastic_coef_restitution: "PlasticCoefRestitution" = None,
            plastic_impact_velocity: "PlasticImpactVelocity" = None,
            static_friction: "StaticFriction" = None,
            dynamic_friction: "DynamicFriction" = None,
            viscous_friction: "ViscousFriction" = None,
            override_impact_capture_velocity: "OverrideImpactCaptureVelocity" = None,
            override_stiction_transition_velocity: "OverrideStictionTransitionVelocity" = None
    ):
        super().__init__()
        self.stiffness = stiffness
        self.dissipation = dissipation
        self.plastic_coef_restitution = plastic_coef_restitution
        self.plastic_impact_velocity = plastic_impact_velocity
        self.static_friction = static_friction
        self.dynamic_friction = dynamic_friction
        self.viscous_friction = viscous_friction
        self.override_impact_capture_velocity = override_impact_capture_velocity
        self.override_stiction_transition_velocity = override_stiction_transition_velocity

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf())
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf())
        if self.plastic_coef_restitution is not None:
            el.append(self.plastic_coef_restitution.to_sdf())
        if self.plastic_impact_velocity is not None:
            el.append(self.plastic_impact_velocity.to_sdf())
        if self.static_friction is not None:
            el.append(self.static_friction.to_sdf())
        if self.dynamic_friction is not None:
            el.append(self.dynamic_friction.to_sdf())
        if self.viscous_friction is not None:
            el.append(self.viscous_friction.to_sdf())
        if self.override_impact_capture_velocity is not None:
            el.append(self.override_impact_capture_velocity.to_sdf())
        if self.override_stiction_transition_velocity is not None:
            el.append(self.override_stiction_transition_velocity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Contact":
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness) if _c_stiffness is not None else None
        _c_dissipation = el.find("dissipation")
        _dissipation = Dissipation.from_sdf(_c_dissipation) if _c_dissipation is not None else None
        _c_plastic_coef_restitution = el.find("plastic_coef_restitution")
        _plastic_coef_restitution = PlasticCoefRestitution.from_sdf(
            _c_plastic_coef_restitution) if _c_plastic_coef_restitution is not None else None
        _c_plastic_impact_velocity = el.find("plastic_impact_velocity")
        _plastic_impact_velocity = PlasticImpactVelocity.from_sdf(
            _c_plastic_impact_velocity) if _c_plastic_impact_velocity is not None else None
        _c_static_friction = el.find("static_friction")
        _static_friction = StaticFriction.from_sdf(_c_static_friction) if _c_static_friction is not None else None
        _c_dynamic_friction = el.find("dynamic_friction")
        _dynamic_friction = DynamicFriction.from_sdf(_c_dynamic_friction) if _c_dynamic_friction is not None else None
        _c_viscous_friction = el.find("viscous_friction")
        _viscous_friction = ViscousFriction.from_sdf(_c_viscous_friction) if _c_viscous_friction is not None else None
        _c_override_impact_capture_velocity = el.find("override_impact_capture_velocity")
        _override_impact_capture_velocity = OverrideImpactCaptureVelocity.from_sdf(
            _c_override_impact_capture_velocity) if _c_override_impact_capture_velocity is not None else None
        _c_override_stiction_transition_velocity = el.find("override_stiction_transition_velocity")
        _override_stiction_transition_velocity = OverrideStictionTransitionVelocity.from_sdf(
            _c_override_stiction_transition_velocity) if _c_override_stiction_transition_velocity is not None else None
        return cls(stiffness=_stiffness, dissipation=_dissipation, plastic_coef_restitution=_plastic_coef_restitution,
                   plastic_impact_velocity=_plastic_impact_velocity, static_friction=_static_friction,
                   dynamic_friction=_dynamic_friction, viscous_friction=_viscous_friction,
                   override_impact_capture_velocity=_override_impact_capture_velocity,
                   override_stiction_transition_velocity=_override_stiction_transition_velocity)


class Simbody(_PrevSimbody):
    def __init__(
            self,
            min_step_size: "MinStepSize" = None,
            accuracy: "Accuracy" = None,
            max_transient_velocity: "MaxTransientVelocity" = None,
            contact: "Contact" = None
    ):
        super().__init__()
        self.min_step_size = min_step_size
        self.accuracy = accuracy
        self.max_transient_velocity = max_transient_velocity
        self.contact = contact

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.min_step_size is not None:
            el.append(self.min_step_size.to_sdf())
        if self.accuracy is not None:
            el.append(self.accuracy.to_sdf())
        if self.max_transient_velocity is not None:
            el.append(self.max_transient_velocity.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Simbody":
        _c_min_step_size = el.find("min_step_size")
        _min_step_size = MinStepSize.from_sdf(_c_min_step_size) if _c_min_step_size is not None else None
        _c_accuracy = el.find("accuracy")
        _accuracy = Accuracy.from_sdf(_c_accuracy) if _c_accuracy is not None else None
        _c_max_transient_velocity = el.find("max_transient_velocity")
        _max_transient_velocity = MaxTransientVelocity.from_sdf(
            _c_max_transient_velocity) if _c_max_transient_velocity is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        return cls(min_step_size=_min_step_size, accuracy=_accuracy, max_transient_velocity=_max_transient_velocity,
                   contact=_contact)


class Bullet(_PrevBullet):
    def __init__(self, solver: "Solver" = None, constraints: "Constraints" = None):
        super().__init__()
        self.solver = solver
        self.constraints = constraints

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.solver is not None:
            el.append(self.solver.to_sdf())
        if self.constraints is not None:
            el.append(self.constraints.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver) if _c_solver is not None else None
        _c_constraints = el.find("constraints")
        _constraints = Constraints.from_sdf(_c_constraints) if _c_constraints is not None else None
        return cls(solver=_solver, constraints=_constraints)


class Ode(_PrevOde):
    def __init__(self, solver: "Solver" = None, constraints: "Constraints" = None):
        super().__init__()
        self.solver = solver
        self.constraints = constraints

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.solver is not None:
            el.append(self.solver.to_sdf())
        if self.constraints is not None:
            el.append(self.constraints.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver) if _c_solver is not None else None
        _c_constraints = el.find("constraints")
        _constraints = Constraints.from_sdf(_c_constraints) if _c_constraints is not None else None
        return cls(solver=_solver, constraints=_constraints)


class Physics(_PrevPhysics):
    def __init__(
            self,
            name: str = "default_physics",
            default: bool = False,
            type: str = "ode",
            max_step_size: "MaxStepSize" = None,
            real_time_factor: "RealTimeFactor" = None,
            real_time_update_rate: "RealTimeUpdateRate" = None,
            max_contacts: "MaxContacts" = None,
            dart: "Dart" = None,
            simbody: "Simbody" = None,
            bullet: "Bullet" = None,
            ode: "Ode" = None
    ):
        super().__init__(simbody=simbody, ode=ode)
        self.name = name
        self.default = default
        self.type = type
        self.max_step_size = max_step_size
        self.real_time_factor = real_time_factor
        self.real_time_update_rate = real_time_update_rate
        self.max_contacts = max_contacts
        self.dart = dart
        self.bullet = bullet

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.name is not None:
            el.set("name", self.name)
        if self.default is not None:
            el.set("default", str(self.default).lower())
        if self.type is not None:
            el.set("type", self.type)
        if self.max_step_size is not None:
            el.append(self.max_step_size.to_sdf())
        if self.real_time_factor is not None:
            el.append(self.real_time_factor.to_sdf())
        if self.real_time_update_rate is not None:
            el.append(self.real_time_update_rate.to_sdf())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        if self.dart is not None:
            el.append(self.dart.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Physics":
        _base = _PrevPhysics.from_sdf(el)
        _name = el.get("name", "default_physics")
        _default = el.get("default", False).strip().lower() == 'true'
        _type = el.get("type", "ode")
        _c_max_step_size = el.find("max_step_size")
        _max_step_size = MaxStepSize.from_sdf(_c_max_step_size) if _c_max_step_size is not None else None
        _c_real_time_factor = el.find("real_time_factor")
        _real_time_factor = RealTimeFactor.from_sdf(_c_real_time_factor) if _c_real_time_factor is not None else None
        _c_real_time_update_rate = el.find("real_time_update_rate")
        _real_time_update_rate = RealTimeUpdateRate.from_sdf(
            _c_real_time_update_rate) if _c_real_time_update_rate is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_dart = el.find("dart")
        _dart = Dart.from_sdf(_c_dart) if _c_dart is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(name=_name, default=_default, type=_type, max_step_size=_max_step_size,
                   real_time_factor=_real_time_factor, real_time_update_rate=_real_time_update_rate,
                   max_contacts=_max_contacts, dart=_dart, simbody=_base.simbody, bullet=_bullet, ode=_base.ode)


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


class World(_PrevWorld):
    def __init__(
            self,
            name: str = "__default__",
            atmosphere: "Atmosphere" = None,
            gui: "Gui" = None,
            physics: List["Physics"] = None,
            scene: "Scene" = None,
            light: List["Light"] = None,
            model: List["Model"] = None,
            actor: List["Actor"] = None,
            plugin: List["Plugin"] = None,
            joint: List["Joint"] = None,
            road: List["Road"] = None,
            spherical_coordinates: "SphericalCoordinates" = None,
            state: List["State"] = None,
            population: List["Population"] = None,
            audio: "Audio" = None,
            wind: "Wind" = None,
            include: List["Include"] = None,
            gravity: "Gravity" = None,
            magnetic_field: "MagneticField" = None
    ):
        super().__init__(name=name, gui=gui, physics=physics, scene=scene, light=light, model=model, actor=actor,
                         plugin=plugin, joint=joint, road=road, spherical_coordinates=spherical_coordinates,
                         state=state, population=population, audio=audio, include=include)
        self.atmosphere = atmosphere
        self.wind = wind
        self.gravity = gravity
        self.magnetic_field = magnetic_field

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.atmosphere is not None:
            el.append(self.atmosphere.to_sdf())
        if self.wind is not None:
            el.append(self.wind.to_sdf())
        if self.gravity is not None:
            el.append(self.gravity.to_sdf())
        if self.magnetic_field is not None:
            el.append(self.magnetic_field.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "World":
        _base = _PrevWorld.from_sdf(el)
        _c_atmosphere = el.find("atmosphere")
        _atmosphere = Atmosphere.from_sdf(_c_atmosphere) if _c_atmosphere is not None else None
        _c_wind = el.find("wind")
        _wind = Wind.from_sdf(_c_wind) if _c_wind is not None else None
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_magnetic_field = el.find("magnetic_field")
        _magnetic_field = MagneticField.from_sdf(_c_magnetic_field) if _c_magnetic_field is not None else None
        return cls(name=_base.name, atmosphere=_atmosphere, gui=_base.gui, physics=_base.physics, scene=_base.scene,
                   light=_base.light, model=_base.model, actor=_base.actor, plugin=_base.plugin, joint=_base.joint,
                   road=_base.road, spherical_coordinates=_base.spherical_coordinates, state=_base.state,
                   population=_base.population, audio=_base.audio, wind=_wind, include=_base.include, gravity=_gravity,
                   magnetic_field=_magnetic_field)
