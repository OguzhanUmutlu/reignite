from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_4.models.contact import Contact as _PrevContact
from ...sdf1_4.models.simbody import Simbody as _PrevSimbody
from ...sdf1_4.models.bullet import Bullet as _PrevBullet
from ...sdf1_4.models.ode import Ode as _PrevOde
from ...sdf1_4.models.physics import Physics as _PrevPhysics
from ...sdf1_4.models.static import Static as _PrevStatic
from ...sdf1_4.models.include import Include as _PrevInclude
from ...sdf1_4.models.model import Model as _PrevModel
from ...sdf1_4.models.world import World as _PrevWorld
from .gui import Gui
from .scene import Scene
from .light import Light
from .actor import Actor
from .plugin import Plugin
from .joint import Joint
from .road import Road
from .spherical_coordinates import SphericalCoordinates
from .state import State
from .population import Population
from .audio import Audio


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
        gravity: "Gravity" = None,
        magnetic_field: "MagneticField" = None,
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
        self.gravity = gravity
        self.magnetic_field = magnetic_field
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
        if self.gravity is not None:
            el.append(self.gravity.to_sdf())
        if self.magnetic_field is not None:
            el.append(self.magnetic_field.to_sdf())
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
        _c_gravity = el.find("gravity")
        _gravity = Gravity.from_sdf(_c_gravity) if _c_gravity is not None else None
        _c_magnetic_field = el.find("magnetic_field")
        _magnetic_field = MagneticField.from_sdf(_c_magnetic_field) if _c_magnetic_field is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(name=_name, default=_default, type=_type, max_step_size=_max_step_size, real_time_factor=_real_time_factor, real_time_update_rate=_real_time_update_rate, max_contacts=_max_contacts, gravity=_gravity, magnetic_field=_magnetic_field, simbody=_base.simbody, bullet=_bullet, ode=_base.ode)


class Static(_PrevStatic):
    def __init__(self, static: bool = False):
        super().__init__(static=static)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Static":
        _base = _PrevStatic.from_sdf(el)
        return cls(static=_base.static)


class Include(_PrevInclude):
    def __init__(
        self,
        plugin: List["Plugin"] = None,
        uri: "Uri" = None,
        pose: "Pose" = None,
        name: "Name" = None,
        static: "Static" = None
    ):
        super().__init__(uri=uri)
        self.plugin = plugin or []
        self.pose = pose
        self.name = name
        self.static = static

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.plugin or []):
            el.append(item.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.name is not None:
            el.append(self.name.to_sdf())
        if self.static is not None:
            el.append(self.static.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Include":
        _base = _PrevInclude.from_sdf(el)
        _plugin = [Plugin.from_sdf(c) for c in el.findall("plugin")]
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name) if _c_name is not None else None
        _c_static = el.find("static")
        _static = Static.from_sdf(_c_static) if _c_static is not None else None
        return cls(plugin=_plugin, uri=_base.uri, pose=_pose, name=_name, static=_static)


class Model(_PrevModel):
    def __init__(
        self,
        name: str = "__default__",
        frame: List["Frame"] = None,
        pose: "Pose" = None,
        link: List["Link"] = None,
        joint: List["Joint"] = None,
        plugin: List["Plugin"] = None,
        gripper: List["Gripper"] = None,
        static: "Static" = None,
        self_collide: "SelfCollide" = None,
        allow_auto_disable: "AllowAutoDisable" = None,
        include: List["Include"] = None,
        model: List["Model"] = None
    ):
        super().__init__(name=name, pose=pose, link=link, joint=joint, plugin=plugin, gripper=gripper, static=static, allow_auto_disable=allow_auto_disable)
        self.frame = frame or []
        self.self_collide = self_collide
        self.include = include or []
        self.model = model or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.self_collide is not None:
            el.append(self.self_collide.to_sdf())
        for item in (self.include or []):
            el.append(item.to_sdf())
        for item in (self.model or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Model":
        _base = _PrevModel.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_self_collide = el.find("self_collide")
        _self_collide = SelfCollide.from_sdf(_c_self_collide) if _c_self_collide is not None else None
        _include = [Include.from_sdf(c) for c in el.findall("include")]
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        return cls(name=_base.name, frame=_frame, pose=_base.pose, link=_base.link, joint=_base.joint, plugin=_base.plugin, gripper=_base.gripper, static=_base.static, self_collide=_self_collide, allow_auto_disable=_base.allow_auto_disable, include=_include, model=_model)


class World(_PrevWorld):
    def __init__(
        self,
        name: str = "__default__",
        gui: "Gui" = None,
        physics: "Physics" = None,
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
        include: List["Include"] = None
    ):
        super().__init__(name=name, gui=gui, physics=physics, scene=scene, light=light, model=model, actor=actor, plugin=plugin, joint=joint, road=road, spherical_coordinates=spherical_coordinates, state=state, audio=audio, include=include)
        self.population = population or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.population or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "World":
        _base = _PrevWorld.from_sdf(el)
        _population = [Population.from_sdf(c) for c in el.findall("population")]
        return cls(name=_base.name, gui=_base.gui, physics=_base.physics, scene=_base.scene, light=_base.light, model=_base.model, actor=_base.actor, plugin=_base.plugin, joint=_base.joint, road=_base.road, spherical_coordinates=_base.spherical_coordinates, state=_base.state, population=_population, audio=_base.audio, include=_base.include)
