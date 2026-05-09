from __future__ import annotations

from xml.etree import ElementTree as ET

from .albedo_map import AlbedoMap
from .ambient_occlusion_map import AmbientOcclusionMap
from .emissive_map import EmissiveMap
from .environment_map import EnvironmentMap
from .metalness import Metalness
from .metalness_map import MetalnessMap
from .normal_map import NormalMap
from .roughness import Roughness
from .roughness_map import RoughnessMap
from ..model import Model


class Metal(Model):
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
            emissive_map: "EmissiveMap" = None
    ):
        self.albedo_map = albedo_map
        self.roughness_map = roughness_map
        self.roughness = roughness
        self.metalness_map = metalness_map
        self.metalness = metalness
        self.environment_map = environment_map
        self.ambient_occlusion_map = ambient_occlusion_map
        self.normal_map = normal_map
        self.emissive_map = emissive_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("metal")
        if self.albedo_map is not None:
            el.append(self.albedo_map.to_sdf())
        if self.roughness_map is not None:
            el.append(self.roughness_map.to_sdf())
        if self.roughness is not None:
            el.append(self.roughness.to_sdf())
        if self.metalness_map is not None:
            el.append(self.metalness_map.to_sdf())
        if self.metalness is not None:
            el.append(self.metalness.to_sdf())
        if self.environment_map is not None:
            el.append(self.environment_map.to_sdf())
        if self.ambient_occlusion_map is not None:
            el.append(self.ambient_occlusion_map.to_sdf())
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf())
        if self.emissive_map is not None:
            el.append(self.emissive_map.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Metal":
        _c_albedo_map = el.find("albedo_map")
        _albedo_map = AlbedoMap.from_sdf(_c_albedo_map) if _c_albedo_map is not None else None
        _c_roughness_map = el.find("roughness_map")
        _roughness_map = RoughnessMap.from_sdf(_c_roughness_map) if _c_roughness_map is not None else None
        _c_roughness = el.find("roughness")
        _roughness = Roughness.from_sdf(_c_roughness) if _c_roughness is not None else None
        _c_metalness_map = el.find("metalness_map")
        _metalness_map = MetalnessMap.from_sdf(_c_metalness_map) if _c_metalness_map is not None else None
        _c_metalness = el.find("metalness")
        _metalness = Metalness.from_sdf(_c_metalness) if _c_metalness is not None else None
        _c_environment_map = el.find("environment_map")
        _environment_map = EnvironmentMap.from_sdf(_c_environment_map) if _c_environment_map is not None else None
        _c_ambient_occlusion_map = el.find("ambient_occlusion_map")
        _ambient_occlusion_map = AmbientOcclusionMap.from_sdf(
            _c_ambient_occlusion_map) if _c_ambient_occlusion_map is not None else None
        _c_normal_map = el.find("normal_map")
        _normal_map = NormalMap.from_sdf(_c_normal_map) if _c_normal_map is not None else None
        _c_emissive_map = el.find("emissive_map")
        _emissive_map = EmissiveMap.from_sdf(_c_emissive_map) if _c_emissive_map is not None else None
        return cls(albedo_map=_albedo_map, roughness_map=_roughness_map, roughness=_roughness,
                   metalness_map=_metalness_map, metalness=_metalness, environment_map=_environment_map,
                   ambient_occlusion_map=_ambient_occlusion_map, normal_map=_normal_map, emissive_map=_emissive_map)
