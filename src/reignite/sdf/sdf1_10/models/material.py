from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.material import Material as _PrevMaterial
from .script import Script
from .shader import Shader
from .render_order import RenderOrder
from .lighting import Lighting
from .ambient import Ambient
from .diffuse import Diffuse
from .specular import Specular
from .shininess import Shininess
from .emissive import Emissive
from .double_sided import DoubleSided
from .pbr import Pbr


class Material(_PrevMaterial):
    def __init__(
        self,
        script: "Script" = None,
        shader: "Shader" = None,
        render_order: "RenderOrder" = None,
        lighting: "Lighting" = None,
        ambient: "Ambient" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        shininess: "Shininess" = None,
        emissive: "Emissive" = None,
        double_sided: "DoubleSided" = None,
        pbr: "Pbr" = None
    ):
        super().__init__(script=script, shader=shader, render_order=render_order, lighting=lighting, ambient=ambient, diffuse=diffuse, specular=specular, shininess=shininess, emissive=emissive, double_sided=double_sided, pbr=pbr)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Material":
        _base = _PrevMaterial.from_sdf(el)
        return cls(script=_base.script, shader=_base.shader, render_order=_base.render_order, lighting=_base.lighting, ambient=_base.ambient, diffuse=_base.diffuse, specular=_base.specular, shininess=_base.shininess, emissive=_base.emissive, double_sided=_base.double_sided, pbr=_base.pbr)
