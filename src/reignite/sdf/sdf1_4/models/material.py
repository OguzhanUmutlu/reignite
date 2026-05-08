from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_3.models.diffuse import Diffuse as _PrevDiffuse
from ...sdf1_3.models.material import Material as _PrevMaterial
from .script import Script
from .shader import Shader
from .lighting import Lighting
from .ambient import Ambient
from .specular import Specular
from .emissive import Emissive


class Diffuse(_PrevDiffuse):
    def __init__(self, diffuse: str = "__default__"):
        super().__init__(diffuse=diffuse)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _base = _PrevDiffuse.from_sdf(el)
        return cls(diffuse=_base.diffuse)


class Material(_PrevMaterial):
    def __init__(
        self,
        script: "Script" = None,
        shader: "Shader" = None,
        lighting: "Lighting" = None,
        ambient: "Ambient" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        emissive: "Emissive" = None
    ):
        super().__init__(script=script, shader=shader, ambient=ambient, diffuse=diffuse, specular=specular, emissive=emissive)
        self.lighting = lighting

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.lighting is not None:
            el.append(self.lighting.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Material":
        _base = _PrevMaterial.from_sdf(el)
        _c_lighting = el.find("lighting")
        _lighting = Lighting.from_sdf(_c_lighting) if _c_lighting is not None else None
        return cls(script=_base.script, shader=_base.shader, lighting=_lighting, ambient=_base.ambient, diffuse=_base.diffuse, specular=_base.specular, emissive=_base.emissive)
