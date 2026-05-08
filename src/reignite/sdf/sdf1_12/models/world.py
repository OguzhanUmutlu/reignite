from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_11.models.dart import Dart as _PrevDart
from ...sdf1_11.models.contact import Contact as _PrevContact
from ...sdf1_11.models.simbody import Simbody as _PrevSimbody
from ...sdf1_11.models.bullet import Bullet as _PrevBullet
from ...sdf1_11.models.ode import Ode as _PrevOde
from ...sdf1_11.models.physics import Physics as _PrevPhysics
from ...sdf1_11.models.pose import Pose as _PrevPose
from ...sdf1_11.models.frame import Frame as _PrevFrame
from ...sdf1_11.models.world import World as _PrevWorld
from ....utils.pose import Pose
from .atmosphere import Atmosphere
from .gui import Gui
from .scene import Scene
from .light import Light
from .joint import Joint
from .model import Model
from .actor import Actor
from .plugin import Plugin
from .road import Road
from .spherical_coordinates import SphericalCoordinates
from .state import State
from .population import Population
from .audio import Audio
from .wind import Wind
from .include import Include
from .gravity import Gravity
from .magnetic_field import MagneticField


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
        _collision_detector = CollisionDetector.from_sdf(_c_collision_detector) if _c_collision_detector is not None else None
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
        _plastic_coef_restitution = PlasticCoefRestitution.from_sdf(_c_plastic_coef_restitution) if _c_plastic_coef_restitution is not None else None
        _c_plastic_impact_velocity = el.find("plastic_impact_velocity")
        _plastic_impact_velocity = PlasticImpactVelocity.from_sdf(_c_plastic_impact_velocity) if _c_plastic_impact_velocity is not None else None
        _c_static_friction = el.find("static_friction")
        _static_friction = StaticFriction.from_sdf(_c_static_friction) if _c_static_friction is not None else None
        _c_dynamic_friction = el.find("dynamic_friction")
        _dynamic_friction = DynamicFriction.from_sdf(_c_dynamic_friction) if _c_dynamic_friction is not None else None
        _c_viscous_friction = el.find("viscous_friction")
        _viscous_friction = ViscousFriction.from_sdf(_c_viscous_friction) if _c_viscous_friction is not None else None
        _c_override_impact_capture_velocity = el.find("override_impact_capture_velocity")
        _override_impact_capture_velocity = OverrideImpactCaptureVelocity.from_sdf(_c_override_impact_capture_velocity) if _c_override_impact_capture_velocity is not None else None
        _c_override_stiction_transition_velocity = el.find("override_stiction_transition_velocity")
        _override_stiction_transition_velocity = OverrideStictionTransitionVelocity.from_sdf(_c_override_stiction_transition_velocity) if _c_override_stiction_transition_velocity is not None else None
        return cls(stiffness=_stiffness, dissipation=_dissipation, plastic_coef_restitution=_plastic_coef_restitution, plastic_impact_velocity=_plastic_impact_velocity, static_friction=_static_friction, dynamic_friction=_dynamic_friction, viscous_friction=_viscous_friction, override_impact_capture_velocity=_override_impact_capture_velocity, override_stiction_transition_velocity=_override_stiction_transition_velocity)


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
        _max_transient_velocity = MaxTransientVelocity.from_sdf(_c_max_transient_velocity) if _c_max_transient_velocity is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        return cls(min_step_size=_min_step_size, accuracy=_accuracy, max_transient_velocity=_max_transient_velocity, contact=_contact)


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
        _real_time_update_rate = RealTimeUpdateRate.from_sdf(_c_real_time_update_rate) if _c_real_time_update_rate is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_dart = el.find("dart")
        _dart = Dart.from_sdf(_c_dart) if _c_dart is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(name=_name, default=_default, type=_type, max_step_size=_max_step_size, real_time_factor=_real_time_factor, real_time_update_rate=_real_time_update_rate, max_contacts=_max_contacts, dart=_dart, simbody=_base.simbody, bullet=_bullet, ode=_base.ode)


class Pose(_PrevPose):
    def __init__(
        self,
        pose: Pose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose, relative_to=relative_to, rotation_format=rotation_format, degrees=degrees)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        return cls(pose=_base.pose, relative_to=_base.relative_to, rotation_format=_base.rotation_format, degrees=_base.degrees)


class Frame(_PrevFrame):
    def __init__(self, name: str = "", attached_to: str = "", pose: "Pose" = None):
        super().__init__()
        self.name = name
        self.attached_to = attached_to
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.name is not None:
            el.set("name", self.name)
        if self.attached_to is not None:
            el.set("attached_to", self.attached_to)
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frame":
        _name = el.get("name", "")
        _attached_to = el.get("attached_to", "")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_name, attached_to=_attached_to, pose=_pose)


class World(_PrevWorld):
    def __init__(
        self,
        name: str = "__default__",
        atmosphere: "Atmosphere" = None,
        gui: "Gui" = None,
        physics: List["Physics"] = None,
        scene: "Scene" = None,
        light: List["Light"] = None,
        frame: List["Frame"] = None,
        joint: List["Joint"] = None,
        model: List["Model"] = None,
        actor: List["Actor"] = None,
        plugin: List["Plugin"] = None,
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
        super().__init__(name=name, atmosphere=atmosphere, gui=gui, physics=physics, scene=scene, light=light, frame=frame, joint=joint, model=model, actor=actor, plugin=plugin, road=road, spherical_coordinates=spherical_coordinates, state=state, population=population, audio=audio, wind=wind, include=include, gravity=gravity, magnetic_field=magnetic_field)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "World":
        _base = _PrevWorld.from_sdf(el)
        return cls(name=_base.name, atmosphere=_base.atmosphere, gui=_base.gui, physics=_base.physics, scene=_base.scene, light=_base.light, frame=_base.frame, joint=_base.joint, model=_base.model, actor=_base.actor, plugin=_base.plugin, road=_base.road, spherical_coordinates=_base.spherical_coordinates, state=_base.state, population=_base.population, audio=_base.audio, wind=_base.wind, include=_base.include, gravity=_base.gravity, magnetic_field=_base.magnetic_field)
