from __future__ import annotations

from xml.etree import ElementTree as ET

from .dissipation import Dissipation
from .dynamic_friction import DynamicFriction
from .override_impact_capture_velocity import OverrideImpactCaptureVelocity
from .override_stiction_transition_velocity import OverrideStictionTransitionVelocity
from .plastic_coef_restitution import PlasticCoefRestitution
from .plastic_impact_velocity import PlasticImpactVelocity
from .static_friction import StaticFriction
from .stiffness import Stiffness
from .viscous_friction import ViscousFriction
from ...sdf1_4.models.contact import Contact as _PrevContact


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
        super().__init__(stiffness=stiffness, dissipation=dissipation,
                         plastic_coef_restitution=plastic_coef_restitution,
                         plastic_impact_velocity=plastic_impact_velocity, static_friction=static_friction,
                         dynamic_friction=dynamic_friction, viscous_friction=viscous_friction,
                         override_impact_capture_velocity=override_impact_capture_velocity,
                         override_stiction_transition_velocity=override_stiction_transition_velocity)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Contact":
        _base = _PrevContact.from_sdf(el)
        return cls(stiffness=_base.stiffness, dissipation=_base.dissipation,
                   plastic_coef_restitution=_base.plastic_coef_restitution,
                   plastic_impact_velocity=_base.plastic_impact_velocity, static_friction=_base.static_friction,
                   dynamic_friction=_base.dynamic_friction, viscous_friction=_base.viscous_friction,
                   override_impact_capture_velocity=_base.override_impact_capture_velocity,
                   override_stiction_transition_velocity=_base.override_stiction_transition_velocity)
