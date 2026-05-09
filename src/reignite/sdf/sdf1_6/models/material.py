from __future__ import annotations

from xml.etree import ElementTree as ET

from .ambient import Ambient
from .diffuse import Diffuse
from .emissive import Emissive
from .lighting import Lighting
from .pbr import Pbr
from .script import Script
from .shader import Shader
from .specular import Specular
from ...sdf1_5.models.material import Material as _PrevMaterial


class Material(_PrevMaterial):
    def __init__(
            self,
            script: "Script" = None,
            shader: "Shader" = None,
            lighting: "Lighting" = None,
            ambient: "Ambient" = None,
            diffuse: "Diffuse" = None,
            specular: "Specular" = None,
            emissive: "Emissive" = None,
            pbr: "Pbr" = None
    ):
        super().__init__(script=script, shader=shader, lighting=lighting, ambient=ambient, diffuse=diffuse,
                         specular=specular, emissive=emissive)
        self.pbr = pbr

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pbr is not None:
            el.append(self.pbr.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Material":
        _base = _PrevMaterial.from_sdf(el)
        _c_pbr = el.find("pbr")
        _pbr = Pbr.from_sdf(_c_pbr) if _c_pbr is not None else None
        return cls(script=_base.script, shader=_base.shader, lighting=_base.lighting, ambient=_base.ambient,
                   diffuse=_base.diffuse, specular=_base.specular, emissive=_base.emissive, pbr=_pbr)
