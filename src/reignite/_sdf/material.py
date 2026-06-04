### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_uint32
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import _ColorT, _color
from ..utils.version import cmp_version

def _parse_color(raw: str) -> _ColorT | SDFError:
    try:
        return _color(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Material(BaseModel):
    class Pbr(BaseModel):
        class Metal(BaseModel):
            class LightMap(BaseModel):
                def __init__(
                    self,
                    sdf_version: str | None = None,
                    light_map: str | None = None,
                    uv_set: int | None = None
                ):
                    super().__init__(sdf_version)
                    self.light_map = light_map
                    self.uv_set = uv_set

                def to_version(self, target_version: str) -> "Material.Pbr.Metal.LightMap":
                    if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
                        raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
                    kwargs: dict = {"sdf_version": target_version, "light_map": self.light_map, "uv_set": self.uv_set}
                    return self.__class__(**kwargs)

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.sdfversion is None and version is not None:
                        self.sdfversion = version
                    elif version is not None and version != self.sdfversion:
                        return self.to_version(str(version)).to_sdf(version)
                    if version is None:
                        version = self.sdfversion or "1.12"
                    el = ET.Element("light_map")
                    if self.light_map is not None:
                        el.text = self.light_map
                    if self.uv_set is not None:
                        el.set("uv_set", str(self.uv_set))
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Pbr.Metal.LightMap | SDFError":
                    _raw_light_map = el.text
                    if _raw_light_map is not None:
                        _light_map = _raw_light_map
                        if isinstance(_light_map, SDFError):
                            return _light_map
                    else:
                        _light_map = None
                    if _light_map is not None and cmp_version(version, "1.7") < 0:
                        if _light_map != None:
                            return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
                    _raw_uv_set = el.get("uv_set")
                    if _raw_uv_set is not None:
                        _uv_set = _parse_uint32(_raw_uv_set)
                        if isinstance(_uv_set, SDFError):
                            return _uv_set.extend("@uv_set")
                    else:
                        _uv_set = None
                    return cls(sdf_version=version, light_map=_light_map, uv_set=_uv_set)

            class NormalMap(BaseModel):
                def __init__(
                    self,
                    sdf_version: str | None = None,
                    normal_map: str | None = None,
                    type: str | None = None
                ):
                    super().__init__(sdf_version)
                    self.normal_map = normal_map
                    self.type = type

                def to_version(self, target_version: str) -> "Material.Pbr.Metal.NormalMap":
                    kwargs: dict = {"sdf_version": target_version, "normal_map": self.normal_map, "type": self.type}
                    return self.__class__(**kwargs)

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.sdfversion is None and version is not None:
                        self.sdfversion = version
                    elif version is not None and version != self.sdfversion:
                        return self.to_version(str(version)).to_sdf(version)
                    if version is None:
                        version = self.sdfversion or "1.12"
                    el = ET.Element("normal_map")
                    if self.normal_map is not None:
                        el.text = self.normal_map
                    if self.type is not None:
                        el.set("type", self.type)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Pbr.Metal.NormalMap | SDFError":
                    _raw_normal_map = el.text
                    if _raw_normal_map is not None:
                        _normal_map = _raw_normal_map
                        if isinstance(_normal_map, SDFError):
                            return _normal_map
                    else:
                        _normal_map = None
                    _raw_type = el.get("type")
                    if _raw_type is not None:
                        _type = _raw_type
                        if isinstance(_type, SDFError):
                            return _type.extend("@type")
                    else:
                        _type = None
                    return cls(sdf_version=version, normal_map=_normal_map, type=_type)

            def __init__(
                self,
                sdf_version: str | None = None,
                albedo_map: str | None = None,
                ambient_occlusion_map: str | None = None,
                emissive_map: str | None = None,
                environment_map: str | None = None,
                light_map: "Material.Pbr.Metal.LightMap" = None,
                metalness: str | None = None,
                metalness_map: str | None = None,
                normal_map: "Material.Pbr.Metal.NormalMap" = None,
                roughness: str | None = None,
                roughness_map: str | None = None
            ):
                super().__init__(sdf_version)
                self.albedo_map = albedo_map
                self.ambient_occlusion_map = ambient_occlusion_map
                self.emissive_map = emissive_map
                self.environment_map = environment_map
                self.light_map = light_map
                self.metalness = metalness
                self.metalness_map = metalness_map
                self.normal_map = normal_map
                self.roughness = roughness
                self.roughness_map = roughness_map
                if self.light_map is not None and hasattr(self.light_map, 'to_version'):
                    if getattr(self.light_map, 'sdfversion', None) is None:
                        self.light_map.sdfversion = self.sdfversion
                    elif getattr(self.light_map, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.light_map = self.light_map.to_version(self.sdfversion)
                if self.normal_map is not None and hasattr(self.normal_map, 'to_version'):
                    if getattr(self.normal_map, 'sdfversion', None) is None:
                        self.normal_map.sdfversion = self.sdfversion
                    elif getattr(self.normal_map, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.normal_map = self.normal_map.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "Material.Pbr.Metal":
                if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
                    raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
                kwargs: dict = {"sdf_version": target_version, "albedo_map": self.albedo_map, "ambient_occlusion_map": self.ambient_occlusion_map, "emissive_map": self.emissive_map, "environment_map": self.environment_map, "light_map": self.light_map.to_version(target_version) if self.light_map is not None and hasattr(self.light_map, "to_version") else self.light_map, "metalness": self.metalness, "metalness_map": self.metalness_map, "normal_map": self.normal_map.to_version(target_version) if self.normal_map is not None and hasattr(self.normal_map, "to_version") else self.normal_map, "roughness": self.roughness, "roughness_map": self.roughness_map}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("metal")
                if self.albedo_map is not None:
                    _c_tmp = ET.Element("albedo_map")
                    _c_tmp.text = self.albedo_map
                    el.append(_c_tmp)
                if self.ambient_occlusion_map is not None:
                    _c_tmp = ET.Element("ambient_occlusion_map")
                    _c_tmp.text = self.ambient_occlusion_map
                    el.append(_c_tmp)
                if self.emissive_map is not None:
                    _c_tmp = ET.Element("emissive_map")
                    _c_tmp.text = self.emissive_map
                    el.append(_c_tmp)
                if self.environment_map is not None:
                    _c_tmp = ET.Element("environment_map")
                    _c_tmp.text = self.environment_map
                    el.append(_c_tmp)
                if self.light_map is not None:
                    _child_res = self.light_map.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('light_map')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                if self.metalness is not None:
                    _c_tmp = ET.Element("metalness")
                    _c_tmp.text = self.metalness
                    el.append(_c_tmp)
                if self.metalness_map is not None:
                    _c_tmp = ET.Element("metalness_map")
                    _c_tmp.text = self.metalness_map
                    el.append(_c_tmp)
                if self.normal_map is not None:
                    _child_res = self.normal_map.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('normal_map')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                if self.roughness is not None:
                    _c_tmp = ET.Element("roughness")
                    _c_tmp.text = self.roughness
                    el.append(_c_tmp)
                if self.roughness_map is not None:
                    _c_tmp = ET.Element("roughness_map")
                    _c_tmp.text = self.roughness_map
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Pbr.Metal | SDFError":
                _c_tmp = el.find("albedo_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("albedo_map")
                    _albedo_map = _val
                else:
                    _albedo_map = None
                _c_tmp = el.find("ambient_occlusion_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("ambient_occlusion_map")
                    _ambient_occlusion_map = _val
                else:
                    _ambient_occlusion_map = None
                _c_tmp = el.find("emissive_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("emissive_map")
                    _emissive_map = _val
                else:
                    _emissive_map = None
                _c_tmp = el.find("environment_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("environment_map")
                    _environment_map = _val
                else:
                    _environment_map = None
                _c_light_map = el.find("light_map")
                if _c_light_map is not None:
                    _res = cls.LightMap._from_sdf(_c_light_map, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("light_map")
                    _light_map = _res
                else:
                    _light_map = None
                if _light_map is not None and cmp_version(version, "1.7") < 0:
                    return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
                _c_tmp = el.find("metalness")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "0.5"
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("metalness")
                    _metalness = _val
                else:
                    _metalness = None
                _c_tmp = el.find("metalness_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("metalness_map")
                    _metalness_map = _val
                else:
                    _metalness_map = None
                _c_normal_map = el.find("normal_map")
                if _c_normal_map is not None:
                    _res = cls.NormalMap._from_sdf(_c_normal_map, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("normal_map")
                    _normal_map = _res
                else:
                    _normal_map = None
                _c_tmp = el.find("roughness")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "0.5"
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("roughness")
                    _roughness = _val
                else:
                    _roughness = None
                _c_tmp = el.find("roughness_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("roughness_map")
                    _roughness_map = _val
                else:
                    _roughness_map = None
                return cls(sdf_version=version, albedo_map=_albedo_map, ambient_occlusion_map=_ambient_occlusion_map, emissive_map=_emissive_map, environment_map=_environment_map, light_map=_light_map, metalness=_metalness, metalness_map=_metalness_map, normal_map=_normal_map, roughness=_roughness, roughness_map=_roughness_map)

        class Specular(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                albedo_map: str | None = None,
                ambient_occlusion_map: str | None = None,
                emissive_map: str | None = None,
                environment_map: str | None = None,
                glossiness: str | None = None,
                glossiness_map: str | None = None,
                light_map: "LightMap" = None,
                normal_map: "NormalMap" = None,
                specular_map: str | None = None
            ):
                super().__init__(sdf_version)
                self.albedo_map = albedo_map
                self.ambient_occlusion_map = ambient_occlusion_map
                self.emissive_map = emissive_map
                self.environment_map = environment_map
                self.glossiness = glossiness
                self.glossiness_map = glossiness_map
                self.light_map = light_map
                self.normal_map = normal_map
                self.specular_map = specular_map
                if self.light_map is not None and hasattr(self.light_map, 'to_version'):
                    if getattr(self.light_map, 'sdfversion', None) is None:
                        self.light_map.sdfversion = self.sdfversion
                    elif getattr(self.light_map, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.light_map = self.light_map.to_version(self.sdfversion)
                if self.normal_map is not None and hasattr(self.normal_map, 'to_version'):
                    if getattr(self.normal_map, 'sdfversion', None) is None:
                        self.normal_map.sdfversion = self.sdfversion
                    elif getattr(self.normal_map, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.normal_map = self.normal_map.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "Material.Pbr.Specular":
                if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
                    raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
                kwargs: dict = {"sdf_version": target_version, "albedo_map": self.albedo_map, "ambient_occlusion_map": self.ambient_occlusion_map, "emissive_map": self.emissive_map, "environment_map": self.environment_map, "glossiness": self.glossiness, "glossiness_map": self.glossiness_map, "light_map": self.light_map.to_version(target_version) if self.light_map is not None and hasattr(self.light_map, "to_version") else self.light_map, "normal_map": self.normal_map.to_version(target_version) if self.normal_map is not None and hasattr(self.normal_map, "to_version") else self.normal_map, "specular_map": self.specular_map}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("specular")
                if self.albedo_map is not None:
                    _c_tmp = ET.Element("albedo_map")
                    _c_tmp.text = self.albedo_map
                    el.append(_c_tmp)
                if self.ambient_occlusion_map is not None:
                    _c_tmp = ET.Element("ambient_occlusion_map")
                    _c_tmp.text = self.ambient_occlusion_map
                    el.append(_c_tmp)
                if self.emissive_map is not None:
                    _c_tmp = ET.Element("emissive_map")
                    _c_tmp.text = self.emissive_map
                    el.append(_c_tmp)
                if self.environment_map is not None:
                    _c_tmp = ET.Element("environment_map")
                    _c_tmp.text = self.environment_map
                    el.append(_c_tmp)
                if self.glossiness is not None:
                    _c_tmp = ET.Element("glossiness")
                    _c_tmp.text = self.glossiness
                    el.append(_c_tmp)
                if self.glossiness_map is not None:
                    _c_tmp = ET.Element("glossiness_map")
                    _c_tmp.text = self.glossiness_map
                    el.append(_c_tmp)
                if self.light_map is not None:
                    _child_res = self.light_map.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('light_map')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                if self.normal_map is not None:
                    _child_res = self.normal_map.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('normal_map')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                if self.specular_map is not None:
                    _c_tmp = ET.Element("specular_map")
                    _c_tmp.text = self.specular_map
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Pbr.Specular | SDFError":
                _c_tmp = el.find("albedo_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("albedo_map")
                    _albedo_map = _val
                else:
                    _albedo_map = None
                _c_tmp = el.find("ambient_occlusion_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("ambient_occlusion_map")
                    _ambient_occlusion_map = _val
                else:
                    _ambient_occlusion_map = None
                _c_tmp = el.find("emissive_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("emissive_map")
                    _emissive_map = _val
                else:
                    _emissive_map = None
                _c_tmp = el.find("environment_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("environment_map")
                    _environment_map = _val
                else:
                    _environment_map = None
                _c_tmp = el.find("glossiness")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "0"
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("glossiness")
                    _glossiness = _val
                else:
                    _glossiness = None
                _c_tmp = el.find("glossiness_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("glossiness_map")
                    _glossiness_map = _val
                else:
                    _glossiness_map = None
                _c_light_map = el.find("light_map")
                if _c_light_map is not None:
                    _res = LightMap._from_sdf(_c_light_map, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("light_map")
                    _light_map = _res
                else:
                    _light_map = None
                if _light_map is not None and cmp_version(version, "1.7") < 0:
                    return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
                _c_normal_map = el.find("normal_map")
                if _c_normal_map is not None:
                    _res = NormalMap._from_sdf(_c_normal_map, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("normal_map")
                    _normal_map = _res
                else:
                    _normal_map = None
                _c_tmp = el.find("specular_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else None
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("specular_map")
                    _specular_map = _val
                else:
                    _specular_map = None
                return cls(sdf_version=version, albedo_map=_albedo_map, ambient_occlusion_map=_ambient_occlusion_map, emissive_map=_emissive_map, environment_map=_environment_map, glossiness=_glossiness, glossiness_map=_glossiness_map, light_map=_light_map, normal_map=_normal_map, specular_map=_specular_map)

        def __init__(
            self,
            sdf_version: str | None = None,
            metal: "Material.Pbr.Metal" = None,
            specular: "Material.Pbr.Specular" = None
        ):
            super().__init__(sdf_version)
            self.metal = metal
            self.specular = specular
            if self.metal is not None and hasattr(self.metal, 'to_version'):
                if getattr(self.metal, 'sdfversion', None) is None:
                    self.metal.sdfversion = self.sdfversion
                elif getattr(self.metal, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.metal = self.metal.to_version(self.sdfversion)
            if self.specular is not None and hasattr(self.specular, 'to_version'):
                if getattr(self.specular, 'sdfversion', None) is None:
                    self.specular.sdfversion = self.sdfversion
                elif getattr(self.specular, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.specular = self.specular.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Material.Pbr":
            kwargs: dict = {"sdf_version": target_version, "metal": self.metal.to_version(target_version) if self.metal is not None and hasattr(self.metal, "to_version") else self.metal, "specular": self.specular.to_version(target_version) if self.specular is not None and hasattr(self.specular, "to_version") else self.specular}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("pbr")
            if self.metal is not None:
                _child_res = self.metal.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('metal')
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
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Pbr | SDFError":
            _c_metal = el.find("metal")
            if _c_metal is not None:
                _res = cls.Metal._from_sdf(_c_metal, version)
                if isinstance(_res, SDFError):
                    return _res.extend("metal")
                _metal = _res
            else:
                _metal = None
            _c_specular = el.find("specular")
            if _c_specular is not None:
                _res = cls.Specular._from_sdf(_c_specular, version)
                if isinstance(_res, SDFError):
                    return _res.extend("specular")
                _specular = _res
            else:
                _specular = None
            return cls(sdf_version=version, metal=_metal, specular=_specular)

    class Script(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            name: str | None = None,
            uris: List[str] | None = None
        ):
            super().__init__(sdf_version)
            self.name = name
            self.uris = uris or []

        def add_uri(self, *items: str):
            if self.uris is None:
                self.uris = []
            self.uris.extend(items)

        def to_version(self, target_version: str) -> "Material.Script":
            kwargs: dict = {"sdf_version": target_version, "name": self.name, "uris": self.uris}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("script")
            if self.name is not None:
                _c_tmp = ET.Element("name")
                _c_tmp.text = self.name
                el.append(_c_tmp)
            for _v in (self.uris or []):
                _c_tmp = ET.Element("uri")
                _c_tmp.text = _v
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Script | SDFError":
            _c_tmp = el.find("name")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("name")
                _name = _val
            else:
                _name = None
            _uris = []
            for c in el.findall("uri"):
                _text = c.text if c.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("uri")
                _uris.append(_val)
            return cls(sdf_version=version, name=_name, uris=_uris)

    class Shader(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            normal_map: str | None = None,
            type: str | None = None
        ):
            super().__init__(sdf_version)
            self.normal_map = normal_map
            self.type = type

        def to_version(self, target_version: str) -> "Material.Shader":
            kwargs: dict = {"sdf_version": target_version, "normal_map": self.normal_map, "type": self.type}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("shader")
            if self.normal_map is not None:
                _c_tmp = ET.Element("normal_map")
                _c_tmp.text = self.normal_map
                el.append(_c_tmp)
            if self.type is not None:
                el.set("type", self.type)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Shader | SDFError":
            _c_tmp = el.find("normal_map")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("normal_map")
                _normal_map = _val
            else:
                _normal_map = None
            _raw_type = el.get("type")
            if _raw_type is not None:
                _type = _raw_type
                if isinstance(_type, SDFError):
                    return _type.extend("@type")
            else:
                _type = None
            return cls(sdf_version=version, normal_map=_normal_map, type=_type)

    def __init__(
        self,
        sdf_version: str | None = None,
        ambient: _ColorT | None = None,
        diffuse: _ColorT | None = None,
        double_sided: bool | None = None,
        emissive: _ColorT | None = None,
        lighting: bool | None = None,
        pbr: "Material.Pbr" = None,
        render_order: float | None = None,
        script: "Material.Script" = None,
        shader: "Material.Shader" = None,
        shininess: float | None = None,
        specular: _ColorT | None = None
    ):
        super().__init__(sdf_version)
        self.ambient = _color(ambient) if ambient is not None else None
        self.diffuse = _color(diffuse) if diffuse is not None else None
        self.double_sided = double_sided
        self.emissive = _color(emissive) if emissive is not None else None
        self.lighting = lighting
        self.pbr = pbr
        self.render_order = render_order
        self.script = script
        self.shader = shader
        self.shininess = shininess
        self.specular = _color(specular) if specular is not None else None
        if self.pbr is not None and hasattr(self.pbr, 'to_version'):
            if getattr(self.pbr, 'sdfversion', None) is None:
                self.pbr.sdfversion = self.sdfversion
            elif getattr(self.pbr, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pbr = self.pbr.to_version(self.sdfversion)
        if self.script is not None and hasattr(self.script, 'to_version'):
            if getattr(self.script, 'sdfversion', None) is None:
                self.script.sdfversion = self.sdfversion
            elif getattr(self.script, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.script = self.script.to_version(self.sdfversion)
        if self.shader is not None and hasattr(self.shader, 'to_version'):
            if getattr(self.shader, 'sdfversion', None) is None:
                self.shader.sdfversion = self.sdfversion
            elif getattr(self.shader, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.shader = self.shader.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Material":
        if self.double_sided is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {target_version} (added in 1.7)")
        if self.pbr is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'pbr' is not supported in SDF version {target_version} (added in 1.6)")
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        if self.shininess is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "ambient": self.ambient, "diffuse": self.diffuse, "double_sided": self.double_sided, "emissive": self.emissive, "lighting": self.lighting, "pbr": self.pbr.to_version(target_version) if self.pbr is not None and hasattr(self.pbr, "to_version") else self.pbr, "render_order": self.render_order, "script": self.script.to_version(target_version) if self.script is not None and hasattr(self.script, "to_version") else self.script, "shader": self.shader.to_version(target_version) if self.shader is not None and hasattr(self.shader, "to_version") else self.shader, "shininess": self.shininess, "specular": self.specular}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("material")
        if self.ambient is not None:
            _c_tmp = ET.Element("ambient")
            _c_tmp.text = str(self.ambient)
            el.append(_c_tmp)
        if self.diffuse is not None:
            _c_tmp = ET.Element("diffuse")
            _c_tmp.text = str(self.diffuse)
            el.append(_c_tmp)
        if self.double_sided is not None:
            _c_tmp = ET.Element("double_sided")
            _c_tmp.text = str(self.double_sided).lower()
            el.append(_c_tmp)
        if self.emissive is not None:
            _c_tmp = ET.Element("emissive")
            _c_tmp.text = str(self.emissive)
            el.append(_c_tmp)
        if self.lighting is not None:
            _c_tmp = ET.Element("lighting")
            _c_tmp.text = str(self.lighting).lower()
            el.append(_c_tmp)
        if self.pbr is not None:
            _child_res = self.pbr.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pbr')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.render_order is not None:
            _c_tmp = ET.Element("render_order")
            _c_tmp.text = str(self.render_order)
            el.append(_c_tmp)
        if self.script is not None:
            _child_res = self.script.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('script')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.shader is not None:
            _child_res = self.shader.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('shader')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.shininess is not None:
            _c_tmp = ET.Element("shininess")
            _c_tmp.text = str(self.shininess)
            el.append(_c_tmp)
        if self.specular is not None:
            _c_tmp = ET.Element("specular")
            _c_tmp.text = str(self.specular)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Material | SDFError":
        _c_tmp = el.find("ambient")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 1"
            _val = _parse_color(_text)
            if isinstance(_val, SDFError):
                return _val.extend("ambient")
            _ambient = _val
        else:
            _ambient = None
        _c_tmp = el.find("diffuse")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 1"
            _val = _parse_color(_text)
            if isinstance(_val, SDFError):
                return _val.extend("diffuse")
            _diffuse = _val
        else:
            _diffuse = None
        _c_tmp = el.find("double_sided")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("double_sided")
            _double_sided = _val
        else:
            _double_sided = None
        if _double_sided is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'double_sided' is not supported in SDF version {version} (added in 1.7)")
        _c_tmp = el.find("emissive")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 1"
            _val = _parse_color(_text)
            if isinstance(_val, SDFError):
                return _val.extend("emissive")
            _emissive = _val
        else:
            _emissive = None
        _c_tmp = el.find("lighting")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else True
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("lighting")
            _lighting = _val
        else:
            _lighting = None
        _c_pbr = el.find("pbr")
        if _c_pbr is not None:
            _res = cls.Pbr._from_sdf(_c_pbr, version)
            if isinstance(_res, SDFError):
                return _res.extend("pbr")
            _pbr = _res
        else:
            _pbr = None
        if _pbr is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'pbr' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("render_order")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("render_order")
            _render_order = _val
        else:
            _render_order = None
        if _render_order is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'render_order' is not supported in SDF version {version} (added in 1.7)")
        _c_script = el.find("script")
        if _c_script is not None:
            _res = cls.Script._from_sdf(_c_script, version)
            if isinstance(_res, SDFError):
                return _res.extend("script")
            _script = _res
        else:
            _script = None
        _c_shader = el.find("shader")
        if _c_shader is not None:
            _res = cls.Shader._from_sdf(_c_shader, version)
            if isinstance(_res, SDFError):
                return _res.extend("shader")
            _shader = _res
        else:
            _shader = None
        _c_tmp = el.find("shininess")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("shininess")
            _shininess = _val
        else:
            _shininess = None
        if _shininess is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'shininess' is not supported in SDF version {version} (added in 1.7)")
        _c_tmp = el.find("specular")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0 1"
            _val = _parse_color(_text)
            if isinstance(_val, SDFError):
                return _val.extend("specular")
            _specular = _val
        else:
            _specular = None
        return cls(sdf_version=version, ambient=_ambient, diffuse=_diffuse, double_sided=_double_sided, emissive=_emissive, lighting=_lighting, pbr=_pbr, render_order=_render_order, script=_script, shader=_shader, shininess=_shininess, specular=_specular)
