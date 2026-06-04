from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-shader-param-system", "gz::sim::systems::ShaderParam")
class ShaderParamPlugin(Plugin):
    class Param(BaseModel):
        def __init__(self, name: str | None = None, shader: str | None = None, type: str | None = None, value: str | None = None,
                     arg: str | None = None):
            super().__init__(sdf_version=None)
            self.name = name
            self.shader = shader
            self.type = type
            self.value = value
            self.arg = arg

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            n_el = el.find("name")
            s_el = el.find("shader")
            t_el = el.find("type")
            v_el = el.find("value")
            a_el = el.find("arg")
            return cls(
                name=n_el.text if n_el is not None else None,
                shader=s_el.text if s_el is not None else None,
                type=t_el.text if t_el is not None else None,
                value=v_el.text if v_el is not None else None,
                arg=a_el.text if a_el is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("param")
            if self.name is not None:
                child = ET.Element("name")
                child.text = str(self.name)
                e.append(child)
            if self.shader is not None:
                child = ET.Element("shader")
                child.text = str(self.shader)
                e.append(child)
            if self.type is not None:
                child = ET.Element("type")
                child.text = str(self.type)
                e.append(child)
            if self.value is not None:
                child = ET.Element("value")
                child.text = str(self.value)
                e.append(child)
            if self.arg is not None:
                child = ET.Element("arg")
                child.text = str(self.arg)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class Shader(BaseModel):
        def __init__(self, vertex: str | None = None, fragment: str | None = None, language: str | None = None):
            super().__init__(sdf_version=None)
            self.vertex = vertex
            self.fragment = fragment
            self.language = language

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            lang_attr = el.get("language")
            v_el = el.find("vertex")
            f_el = el.find("fragment")
            return cls(
                vertex=v_el.text if v_el is not None else None,
                fragment=f_el.text if f_el is not None else None,
                language=lang_attr
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("shader")
            if self.language is not None:
                e.set("language", str(self.language))
            if self.vertex is not None:
                child = ET.Element("vertex")
                child.text = str(self.vertex)
                e.append(child)
            if self.fragment is not None:
                child = ET.Element("fragment")
                child.text = str(self.fragment)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            param: list[Param] | Param | None = None,
            shader: list[Shader] | Shader | None = None,
    ):
        self.param = [param] if isinstance(param, ShaderParamPlugin.Param) else (param or [])
        self.shader = [shader] if isinstance(shader, ShaderParamPlugin.Shader) else (shader or [])

        super().__init__(
            sdf_version=None,
            filename="gz-sim-shader-param-system",
            name="gz::sim::systems::ShaderParam"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        p_els = el.findall("param")
        s_els = el.findall("shader")

        return cls(
            param=[cls.Param._from_sdf(p, version) for p in p_els] if p_els else None,
            shader=[cls.Shader._from_sdf(s, version) for s in s_els] if s_els else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::ShaderParam", filename="gz-sim-shader-param-system")
        if self.param:
            for p in self.param:
                el.append(p.to_sdf(version))
        if self.shader:
            for s in self.shader:
                el.append(s.to_sdf(version))
        return el

    def to_version(self, target_version: str):
        if self.param:
            for p in self.param:
                p.to_version(target_version)
        if self.shader:
            for s in self.shader:
                s.to_version(target_version)
        return self
