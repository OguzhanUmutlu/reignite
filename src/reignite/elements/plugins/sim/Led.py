from reignite.elements.plugin import Plugin, ParentElement, TextElement


class LedPlugin(Plugin):
    class DefaultState(ParentElement):
        def __init__(self, color: list[float] | str | None = None, intensity: float | None = None):
            if isinstance(color, list):
                color = " ".join(map(str, color))
            super().__init__(
                "default_state",
                TextElement("color", color) if color is not None else None,
                TextElement("intensity", str(intensity)) if intensity is not None else None
            )

    class Led(ParentElement):
        def __init__(
                self,
                name: str,
                visual_name: str | None = None,
                light_name: str | None = None,
                default_state: "LedPlugin.DefaultState" | None = None
        ):
            super().__init__(
                "led",
                TextElement("name", name),
                TextElement("visual_name", visual_name) if visual_name is not None else None,
                TextElement("light_name", light_name) if light_name is not None else None,
                default_state
            )

    class ActiveLeds(ParentElement):
        def __init__(self, leds: list[str]):
            elements = [TextElement("led", led) for led in leds]
            super().__init__("active_leds", *elements)

    class Step(ParentElement):
        def __init__(
                self,
                always_on: bool | None = None,
                color: list[float] | str | None = None,
                duration: float | None = None,
                intensity: float | None = None
        ):
            if isinstance(color, list):
                color = " ".join(map(str, color))
            super().__init__(
                "step",
                TextElement("always_on", always_on) if always_on is not None else None,
                TextElement("color", color) if color is not None else None,
                TextElement("duration", str(duration)) if duration is not None else None,
                TextElement("intensity", str(intensity)) if intensity is not None else None
            )

    class Mode(ParentElement):
        def __init__(
                self,
                name: str,
                active_leds: "LedPlugin.ActiveLeds" | list[str] | None = None,
                steps: list["LedPlugin.Step"] | None = None
        ):
            if isinstance(active_leds, list):
                active_leds = LedPlugin.ActiveLeds(active_leds)

            elements = [TextElement("name", name)]
            if active_leds is not None:
                elements.append(active_leds)
            if steps is not None:
                elements.extend(steps)

            super().__init__("mode", *elements)

    def __init__(
            self,
            leds: list[Led] | Led,
            modes: list[Mode] | Mode,
            led_group_name: str | None = None,
            startup_mode: str | None = None
    ):
        if not leds:
            raise ValueError("At least one LED must be specified in the 'leds' list.")

        if not modes:
            raise ValueError("At least one LED Mode must be specified in the 'modes' list.")

        elements = []
        if isinstance(leds, LedPlugin.Led):
            leds = [leds]
        elements.extend(leds)

        if isinstance(modes, LedPlugin.Mode):
            modes = [modes]
        elements.extend(modes)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-led-plugin-system",
            name="gz::sim::systems::LedPlugin",
            elements=elements,
            led_group_name=led_group_name,
            startup_mode=startup_mode,
        )
