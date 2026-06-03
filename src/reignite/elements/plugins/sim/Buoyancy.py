from reignite.elements.plugin import Plugin, ParentElement, TextElement


class BuoyancyPlugin(Plugin):
    class DensityChange(ParentElement):
        def __init__(self, above_depth: float, density: float):
            super().__init__(
                "density_change",
                [
                    TextElement("above_depth", str(above_depth)),
                    TextElement("density", str(density))
                ]
            )

    class GradedBuoyancy(ParentElement):
        def __init__(self, default_density: float | None = None,
                     density_changes: list["BuoyancyPlugin.DensityChange"] | None = None):
            elements = []
            if default_density is not None:
                elements.append(TextElement("default_density", str(default_density)))
            if density_changes is not None:
                elements.extend(density_changes)
            super().__init__("graded_buoyancy", *elements)

    def __init__(
            self,
            uniform_fluid_density: float | None = None,
            graded_buoyancy: GradedBuoyancy | None = None,
            enable: str | list[str] | None = None
    ):
        elements = []
        if graded_buoyancy is not None:
            elements.append(graded_buoyancy)

        if enable is not None:
            if isinstance(enable, str):
                enable = [enable]
            for e in enable:
                elements.append(TextElement("enable", e))

        super().__init__(
            sdf_version=None,
            filename="gz-sim-buoyancy-system",
            name="gz::sim::systems::Buoyancy",
            elements=elements,
            uniform_fluid_density=uniform_fluid_density,
        )
