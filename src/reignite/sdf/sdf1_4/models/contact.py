from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .stiffness import Stiffness
from .dissipation import Dissipation
from .plastic_coef_restitution import PlasticCoefRestitution
from .plastic_impact_velocity import PlasticImpactVelocity
from .static_friction import StaticFriction
from .dynamic_friction import DynamicFriction
from .viscous_friction import ViscousFriction
from .override_impact_capture_velocity import OverrideImpactCaptureVelocity
from .override_stiction_transition_velocity import OverrideStictionTransitionVelocity


class Contact(Model):
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
        el = ET.Element("contact")
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
