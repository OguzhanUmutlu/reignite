### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color as _SDFColor, _ColorT, _color
from ..utils.version import cmp_version


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


def _parse_color(raw: str) -> _ColorT | SDFError:
    try:
        return _color(raw)
    except ValueError as e:
        return SDFError(str(e))


class Material(BaseModel):
    class Pbr(BaseModel):
        class Metal(BaseModel):
            class LightMap(BaseModel):
                def __init__(self, sdf_version: str | None = None, light_map: str = "", uv_set: int = 0):
                    super().__init__(sdf_version)
                    self.light_map = light_map
                    self.uv_set = uv_set

                def to_version(self, target_version: str) -> "Material.Pbr.Metal.LightMap":
                    if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
                        raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
                    kwargs = {"sdf_version": target_version}
                    kwargs["light_map"] = self.light_map
                    kwargs["uv_set"] = self.uv_set
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("light_map")
                    if self.light_map is not None:
                        el.text = self.light_map
                    if self.uv_set is not None:
                        el.set("uv_set", str(self.uv_set))
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Pbr.Metal.LightMap | SDFError":
                    _text = el.text or ""
                    _light_map = _text
                    if isinstance(_light_map, SDFError):
                        return _light_map
                    if _light_map is not None and cmp_version(version, "1.7") < 0:
                        if _light_map != "":
                            return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
                    _uv_set = _parse_uint32(el.get("uv_set", 0))
                    if isinstance(_uv_set, SDFError):
                        return _uv_set.extend("@uv_set")
                    return cls(sdf_version=version, light_map=_light_map, uv_set=_uv_set)

            class NormalMap(BaseModel):
                def __init__(self, sdf_version: str | None = None, normal_map: str = "", type: str = "tangent"):
                    super().__init__(sdf_version)
                    self.normal_map = normal_map
                    self.type = type

                def to_version(self, target_version: str) -> "Material.Pbr.Metal.NormalMap":
                    kwargs = {"sdf_version": target_version}
                    kwargs["normal_map"] = self.normal_map
                    kwargs["type"] = self.type
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("normal_map")
                    if self.normal_map is not None:
                        el.text = self.normal_map
                    if self.type is not None:
                        el.set("type", self.type)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Material.Pbr.Metal.NormalMap | SDFError":
                    _text = el.text or ""
                    _normal_map = _text
                    if isinstance(_normal_map, SDFError):
                        return _normal_map
                    _type = el.get("type", "tangent")
                    if isinstance(_type, SDFError):
                        return _type.extend("@type")
                    return cls(sdf_version=version, normal_map=_normal_map, type=_type)

            def __init__(
                self,
                sdf_version: str | None = None,
                albedo_map: str = "",
                ambient_occlusion_map: str = "",
                emissive_map: str = "",
                environment_map: str = "",
                light_map: "Material.Pbr.Metal.LightMap" = None,
                metalness: str = "0.5",
                metalness_map: str = "",
                normal_map: "Material.Pbr.Metal.NormalMap" = None,
                roughness: str = "0.5",
                roughness_map: str = ""
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
                    if getattr(self.light_map, '__version__', None) is None:
                        self.light_map.__version__ = self.__version__
                    elif getattr(self.light_map, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.light_map = self.light_map.to_version(self.__version__)
                if self.normal_map is not None and hasattr(self.normal_map, 'to_version'):
                    if getattr(self.normal_map, '__version__', None) is None:
                        self.normal_map.__version__ = self.__version__
                    elif getattr(self.normal_map, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.normal_map = self.normal_map.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Material.Pbr.Metal":
                if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
                    raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
                kwargs = {"sdf_version": target_version}
                kwargs["albedo_map"] = self.albedo_map
                kwargs["ambient_occlusion_map"] = self.ambient_occlusion_map
                kwargs["emissive_map"] = self.emissive_map
                kwargs["environment_map"] = self.environment_map
                kwargs["light_map"] = self.light_map.to_version(target_version) if hasattr(self.light_map, "to_version") else self.light_map
                kwargs["metalness"] = self.metalness
                kwargs["metalness_map"] = self.metalness_map
                kwargs["normal_map"] = self.normal_map.to_version(target_version) if hasattr(self.normal_map, "to_version") else self.normal_map
                kwargs["roughness"] = self.roughness
                kwargs["roughness_map"] = self.roughness_map
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
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
                    if hasattr(self.light_map, 'to_sdf'):
                        _child_res = self.light_map.to_sdf(version)
                    else:
                        _child_res = str(self.light_map)
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
                    if hasattr(self.normal_map, 'to_sdf'):
                        _child_res = self.normal_map.to_sdf(version)
                    else:
                        _child_res = str(self.normal_map)
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
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("albedo_map")
                    _albedo_map = _val
                else:
                    _albedo_map = None
                _c_tmp = el.find("ambient_occlusion_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("ambient_occlusion_map")
                    _ambient_occlusion_map = _val
                else:
                    _ambient_occlusion_map = None
                _c_tmp = el.find("emissive_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("emissive_map")
                    _emissive_map = _val
                else:
                    _emissive_map = None
                _c_tmp = el.find("environment_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
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
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
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
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
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
                albedo_map: str = "",
                ambient_occlusion_map: str = "",
                emissive_map: str = "",
                environment_map: str = "",
                glossiness: str = "0",
                glossiness_map: str = "",
                light_map: "LightMap" = None,
                normal_map: "NormalMap" = None,
                specular_map: str = ""
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
                    if getattr(self.light_map, '__version__', None) is None:
                        self.light_map.__version__ = self.__version__
                    elif getattr(self.light_map, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.light_map = self.light_map.to_version(self.__version__)
                if self.normal_map is not None and hasattr(self.normal_map, 'to_version'):
                    if getattr(self.normal_map, '__version__', None) is None:
                        self.normal_map.__version__ = self.__version__
                    elif getattr(self.normal_map, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.normal_map = self.normal_map.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Material.Pbr.Specular":
                if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
                    raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
                kwargs = {"sdf_version": target_version}
                kwargs["albedo_map"] = self.albedo_map
                kwargs["ambient_occlusion_map"] = self.ambient_occlusion_map
                kwargs["emissive_map"] = self.emissive_map
                kwargs["environment_map"] = self.environment_map
                kwargs["glossiness"] = self.glossiness
                kwargs["glossiness_map"] = self.glossiness_map
                kwargs["light_map"] = self.light_map.to_version(target_version) if hasattr(self.light_map, "to_version") else self.light_map
                kwargs["normal_map"] = self.normal_map.to_version(target_version) if hasattr(self.normal_map, "to_version") else self.normal_map
                kwargs["specular_map"] = self.specular_map
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
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
                    if hasattr(self.light_map, 'to_sdf'):
                        _child_res = self.light_map.to_sdf(version)
                    else:
                        _child_res = str(self.light_map)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('light_map')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                if self.normal_map is not None:
                    if hasattr(self.normal_map, 'to_sdf'):
                        _child_res = self.normal_map.to_sdf(version)
                    else:
                        _child_res = str(self.normal_map)
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
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("albedo_map")
                    _albedo_map = _val
                else:
                    _albedo_map = None
                _c_tmp = el.find("ambient_occlusion_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("ambient_occlusion_map")
                    _ambient_occlusion_map = _val
                else:
                    _ambient_occlusion_map = None
                _c_tmp = el.find("emissive_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("emissive_map")
                    _emissive_map = _val
                else:
                    _emissive_map = None
                _c_tmp = el.find("environment_map")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
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
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
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
                    _text = _c_tmp.text if _c_tmp.text is not None else ""
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
                if getattr(self.metal, '__version__', None) is None:
                    self.metal.__version__ = self.__version__
                elif getattr(self.metal, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.metal = self.metal.to_version(self.__version__)
            if self.specular is not None and hasattr(self.specular, 'to_version'):
                if getattr(self.specular, '__version__', None) is None:
                    self.specular.__version__ = self.__version__
                elif getattr(self.specular, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.specular = self.specular.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Material.Pbr":
            kwargs = {"sdf_version": target_version}
            kwargs["metal"] = self.metal.to_version(target_version) if hasattr(self.metal, "to_version") else self.metal
            kwargs["specular"] = self.specular.to_version(target_version) if hasattr(self.specular, "to_version") else self.specular
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("pbr")
            if self.metal is not None:
                if hasattr(self.metal, 'to_sdf'):
                    _child_res = self.metal.to_sdf(version)
                else:
                    _child_res = str(self.metal)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('metal')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.specular is not None:
                if hasattr(self.specular, 'to_sdf'):
                    _child_res = self.specular.to_sdf(version)
                else:
                    _child_res = str(self.specular)
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
            name: str = "__default__",
            uris: List[str] = None
        ):
            super().__init__(sdf_version)
            self.name = name
            self.uris = uris or []

        def add_uri(self, *items: str):
            if self.uris is None:
                self.uris = []
            self.uris.extend(items)

        def to_version(self, target_version: str) -> "Material.Script":
            kwargs = {"sdf_version": target_version}
            kwargs["name"] = self.name
            kwargs["uris"] = self.uris
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
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
            normal_map: str = "__default__",
            type: str = "pixel"
        ):
            super().__init__(sdf_version)
            self.normal_map = normal_map
            self.type = type

        def to_version(self, target_version: str) -> "Material.Shader":
            kwargs = {"sdf_version": target_version}
            kwargs["normal_map"] = self.normal_map
            kwargs["type"] = self.type
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
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
            _type = el.get("type", "pixel")
            if isinstance(_type, SDFError):
                return _type.extend("@type")
            return cls(sdf_version=version, normal_map=_normal_map, type=_type)

    def __init__(
        self,
        sdf_version: str | None = None,
        ambient: _ColorT = None,
        diffuse: _ColorT = None,
        double_sided: bool = False,
        emissive: _ColorT = None,
        lighting: bool = True,
        pbr: "Material.Pbr" = None,
        render_order: float = 0.0,
        script: "Material.Script" = None,
        shader: "Material.Shader" = None,
        shininess: float = 0,
        specular: _ColorT = None
    ):
        super().__init__(sdf_version)
        if ambient is None:
            ambient = _color("0 0 0 1")
        else:
            ambient = _color(ambient)
        if diffuse is None:
            diffuse = _color("0 0 0 1")
        else:
            diffuse = _color(diffuse)
        if emissive is None:
            emissive = _color("0 0 0 1")
        else:
            emissive = _color(emissive)
        if specular is None:
            specular = _color("0 0 0 1")
        else:
            specular = _color(specular)
        self.ambient = ambient
        self.diffuse = diffuse
        self.double_sided = double_sided
        self.emissive = emissive
        self.lighting = lighting
        self.pbr = pbr
        self.render_order = render_order
        self.script = script
        self.shader = shader
        self.shininess = shininess
        self.specular = specular
        if self.pbr is not None and hasattr(self.pbr, 'to_version'):
            if getattr(self.pbr, '__version__', None) is None:
                self.pbr.__version__ = self.__version__
            elif getattr(self.pbr, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pbr = self.pbr.to_version(self.__version__)
        if self.script is not None and hasattr(self.script, 'to_version'):
            if getattr(self.script, '__version__', None) is None:
                self.script.__version__ = self.__version__
            elif getattr(self.script, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.script = self.script.to_version(self.__version__)
        if self.shader is not None and hasattr(self.shader, 'to_version'):
            if getattr(self.shader, '__version__', None) is None:
                self.shader.__version__ = self.__version__
            elif getattr(self.shader, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.shader = self.shader.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Material":
        if self.double_sided is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {target_version} (added in 1.7)")
        if self.pbr is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'pbr' is not supported in SDF version {target_version} (added in 1.6)")
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        if self.shininess is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient
        kwargs["diffuse"] = self.diffuse
        kwargs["double_sided"] = self.double_sided
        kwargs["emissive"] = self.emissive
        kwargs["lighting"] = self.lighting
        kwargs["pbr"] = self.pbr.to_version(target_version) if hasattr(self.pbr, "to_version") else self.pbr
        kwargs["render_order"] = self.render_order
        kwargs["script"] = self.script.to_version(target_version) if hasattr(self.script, "to_version") else self.script
        kwargs["shader"] = self.shader.to_version(target_version) if hasattr(self.shader, "to_version") else self.shader
        kwargs["shininess"] = self.shininess
        kwargs["specular"] = self.specular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
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
            if hasattr(self.pbr, 'to_sdf'):
                _child_res = self.pbr.to_sdf(version)
            else:
                _child_res = str(self.pbr)
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
            if hasattr(self.script, 'to_sdf'):
                _child_res = self.script.to_sdf(version)
            else:
                _child_res = str(self.script)
            if isinstance(_child_res, str):
                _item_el = ET.Element('script')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.shader is not None:
            if hasattr(self.shader, 'to_sdf'):
                _child_res = self.shader.to_sdf(version)
            else:
                _child_res = str(self.shader)
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
