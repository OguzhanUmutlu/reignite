from reignite.elements.plugin import Plugin, ParentElement, TextElement


@Plugin.register("gz-sim-wind-effects-system", "gz::sim::systems::WindEffects")
class WindEffectsPlugin(Plugin):
    class Sin(ParentElement):
        def __init__(self, amplitude: float | None = None, amplitude_percent: float | None = None,
                     period: float | None = None):
            elements = []
            if amplitude is not None:
                elements.append(TextElement("amplitude", str(amplitude)))
            if amplitude_percent is not None:
                elements.append(TextElement("amplitude_percent", str(amplitude_percent)))
            if period is not None:
                elements.append(TextElement("period", str(period)))
            super().__init__("sin", elements)

    class Magnitude(ParentElement):
        def __init__(self, time_for_rise: float | None = None, sin: "WindEffectsPlugin.Sin | None" = None,
                     noise: ParentElement | None = None):
            super().__init__(
                "magnitude",
                [
                    TextElement("time_for_rise", str(time_for_rise)) if time_for_rise is not None else None,
                    sin,
                    noise
                ]
            )

    class Direction(ParentElement):
        def __init__(self, time_for_rise: float | None = None, sin: "WindEffectsPlugin.Sin | None" = None,
                     noise: ParentElement | None = None):
            super().__init__(
                "direction",
                [
                    TextElement("time_for_rise", str(time_for_rise)) if time_for_rise is not None else None,
                    sin,
                    noise
                ]
            )

    class Horizontal(ParentElement):
        def __init__(self, magnitude: "WindEffectsPlugin.Magnitude | None" = None,
                     direction: "WindEffectsPlugin.Direction | None" = None):
            super().__init__("horizontal", [magnitude, direction])

    class Vertical(ParentElement):
        def __init__(self, time_for_rise: float | None = None, noise: ParentElement | None = None):
            super().__init__(
                "vertical",
                [
                    TextElement("time_for_rise", str(time_for_rise)) if time_for_rise is not None else None,
                    noise
                ]
            )

    def __init__(
            self,
            horizontal: Horizontal | None = None,
            vertical: Vertical | None = None,
            force_approximation_scaling_factor: ParentElement | None = None,
            **kwargs
    ):
        elements = []
        if horizontal is not None:
            elements.append(horizontal)
        if vertical is not None:
            elements.append(vertical)
        if force_approximation_scaling_factor is not None:
            elements.append(force_approximation_scaling_factor)

        super().__init__(
            filename="gz-sim-wind-effects-system",
            name="gz::sim::systems::WindEffects",
            elements=elements,
            **kwargs
        )
