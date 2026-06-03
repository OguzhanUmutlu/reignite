from reignite.elements.plugin import Plugin, ParentElement, TextElement


class ShaderParamPlugin(Plugin):
    class Param(ParentElement):
        def __init__(self, name: str, shader: str, type: str | None = None, value: str | None = None,
                     arg: str | None = None):
            elements = [
                TextElement("name", name),
                TextElement("shader", shader),
            ]
            if type is not None:
                elements.append(TextElement("type", type))
            if value is not None:
                elements.append(TextElement("value", value))
            if arg is not None:
                elements.append(TextElement("arg", arg))
            super().__init__("param", *elements)

    class Shader(ParentElement):
        def __init__(self, vertex: str, fragment: str, language: str | None = None):
            super().__init__(
                "shader",
                TextElement("vertex", vertex),
                TextElement("fragment", fragment),
                language=language
            )

    def __init__(
            self,
            param: list[Param] | Param | None = None,
            shader: list[Shader] | Shader | None = None,
    ):
        elements = []
        if param is not None:
            if isinstance(param, ShaderParamPlugin.Param):
                param = [param]
            elements.extend(param)
        if shader is not None:
            if isinstance(shader, ShaderParamPlugin.Shader):
                shader = [shader]
            elements.extend(shader)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-shader-param-system",
            name="gz::sim::systems::ShaderParam",
            elements=elements,
        )
