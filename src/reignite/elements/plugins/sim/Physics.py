from reignite.elements.plugin import Plugin, ParentElement, TextElement


class PhysicsPlugin(Plugin):
    class Engine(ParentElement):
        def __init__(self, filename: str):
            super().__init__("engine", TextElement("filename", filename))

    def __init__(
            self,
            enforce_fixed_constraint: bool | None = None,
            include_entity_names: bool | None = None,
            engine: Engine | str | None = None,
    ):
        elements = []
        if engine is not None:
            if isinstance(engine, str):
                engine = PhysicsPlugin.Engine(engine)
            elements.append(engine)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-physics-system",
            name="gz::sim::systems::Physics",
            elements=elements,
            enforce_fixed_constraint=enforce_fixed_constraint,
            include_entity_names=include_entity_names,
        )
