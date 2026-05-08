from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.metal import Metal as _PrevMetal
from .albedo_map import AlbedoMap
from .roughness_map import RoughnessMap
from .roughness import Roughness
from .metalness_map import MetalnessMap
from .metalness import Metalness
from .environment_map import EnvironmentMap
from .ambient_occlusion_map import AmbientOcclusionMap
from .normal_map import NormalMap
from .emissive_map import EmissiveMap
from .light_map import LightMap


class Metal(_PrevMetal):
    def __init__(
        self,
        albedo_map: "AlbedoMap" = None,
        roughness_map: "RoughnessMap" = None,
        roughness: "Roughness" = None,
        metalness_map: "MetalnessMap" = None,
        metalness: "Metalness" = None,
        environment_map: "EnvironmentMap" = None,
        ambient_occlusion_map: "AmbientOcclusionMap" = None,
        normal_map: "NormalMap" = None,
        emissive_map: "EmissiveMap" = None,
        light_map: "LightMap" = None
    ):
        super().__init__(albedo_map=albedo_map, roughness_map=roughness_map, roughness=roughness, metalness_map=metalness_map, metalness=metalness, environment_map=environment_map, ambient_occlusion_map=ambient_occlusion_map, normal_map=normal_map, emissive_map=emissive_map, light_map=light_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Metal":
        _base = _PrevMetal.from_sdf(el)
        return cls(albedo_map=_base.albedo_map, roughness_map=_base.roughness_map, roughness=_base.roughness, metalness_map=_base.metalness_map, metalness=_base.metalness, environment_map=_base.environment_map, ambient_occlusion_map=_base.ambient_occlusion_map, normal_map=_base.normal_map, emissive_map=_base.emissive_map, light_map=_base.light_map)
