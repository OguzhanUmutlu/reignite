from __future__ import annotations

from xml.etree import ElementTree as ET

from .ambient import Ambient
from .diffuse import Diffuse
from .emissive import Emissive
from .script import Script
from .shader import Shader
from .specular import Specular
from ...sdf1_0.models.material import Material as _PrevMaterial


class Material(_PrevMaterial):
    def __init__(
            self,
            script: "Script" = None,
            shader: "Shader" = None,
            ambient: "Ambient" = None,
            diffuse: "Diffuse" = None,
            specular: "Specular" = None,
            emissive: "Emissive" = None
    ):
        super().__init__(script=script, shader=shader, ambient=ambient, diffuse=diffuse, specular=specular,
                         emissive=emissive)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Material":
        _base = _PrevMaterial.from_sdf(el)
        return cls(script=_base.script, shader=_base.shader, ambient=_base.ambient, diffuse=_base.diffuse,
                   specular=_base.specular, emissive=_base.emissive)
