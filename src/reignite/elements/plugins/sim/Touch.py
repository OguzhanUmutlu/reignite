from reignite.elements.plugin import Plugin, TextElement


@Plugin.register("gz-sim-touchplugin-system", "gz::sim::systems::TouchPlugin")
class TouchPlugin(Plugin):
    def __init__(
            self,
            target: str,
            time: float,
            collision: list[str] | str | None = None,
            create_contact_sensor_for_collision: bool | None = None,
            namespace: str | None = None,
            enabled: bool | None = None,
            **kwargs
    ):
        elements = []
        if collision is not None:
            if isinstance(collision, str):
                collision = [collision]
            for c in collision:
                elements.append(TextElement("collision", c))

        super().__init__(
            filename="gz-sim-touchplugin-system",
            name="gz::sim::systems::TouchPlugin",
            elements=elements,
            target=target,
            time=time,
            create_contact_sensor_for_collision=create_contact_sensor_for_collision,
            namespace=namespace,
            enabled=enabled,
            **kwargs
        )
