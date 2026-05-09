from __future__ import annotations

from xml.etree import ElementTree as ET

from .ambient import Ambient
from .diffuse import Diffuse
from .double_sided import DoubleSided
from .emissive import Emissive
from .lighting import Lighting
from .pbr import Pbr
from .render_order import RenderOrder
from .script import Script
from .shader import Shader
from .shininess import Shininess
from .specular import Specular
from ...sdf1_6.models.material import Material as _PrevMaterial


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
        super().__init__(script=script, shader=shader, lighting=lighting, ambient=ambient, diffuse=diffuse,
                         specular=specular, emissive=emissive, pbr=pbr)
        self.render_order = render_order
        self.shininess = shininess
        self.double_sided = double_sided

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.render_order is not None:
            el.append(self.render_order.to_sdf())
        if self.shininess is not None:
            el.append(self.shininess.to_sdf())
        if self.double_sided is not None:
            el.append(self.double_sided.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Material":
        _base = _PrevMaterial.from_sdf(el)
        _c_render_order = el.find("render_order")
        _render_order = RenderOrder.from_sdf(_c_render_order) if _c_render_order is not None else None
        _c_shininess = el.find("shininess")
        _shininess = Shininess.from_sdf(_c_shininess) if _c_shininess is not None else None
        _c_double_sided = el.find("double_sided")
        _double_sided = DoubleSided.from_sdf(_c_double_sided) if _c_double_sided is not None else None
        return cls(script=_base.script, shader=_base.shader, render_order=_render_order, lighting=_base.lighting,
                   ambient=_base.ambient, diffuse=_base.diffuse, specular=_base.specular, shininess=_shininess,
                   emissive=_base.emissive, double_sided=_double_sided, pbr=_base.pbr)
