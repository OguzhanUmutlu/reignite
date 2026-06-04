from reignite.elements.plugin import Plugin, TextElement


class VelocityControlPlugin(Plugin):
    def __init__(
            self,
            initial_linear: list[float] | str | None = None,
            initial_angular: list[float] | str | None = None,
            topic: str | None = None,
            link_name: str | list[str] | None = None,
            **kwargs
    ):
        if isinstance(initial_linear, list):
            initial_linear = " ".join(map(str, initial_linear))
        if isinstance(initial_angular, list):
            initial_angular = " ".join(map(str, initial_angular))

        elements = []
        if isinstance(link_name, list):
            for ln in link_name:
                elements.append(TextElement("link_name", ln))
            link_name = None

        super().__init__(
            filename="gz-sim-velocity-control-system",
            name="gz::sim::systems::VelocityControl",
            elements=elements,
            initial_linear=initial_linear,
            initial_angular=initial_angular,
            topic=topic,
            link_name=link_name,
            **kwargs
        )
