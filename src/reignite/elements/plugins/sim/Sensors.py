from reignite.elements.plugin import Plugin, ParentElement, TextElement


@Plugin.register("gz-sim-sensors-system", "gz::sim::systems::Sensors")
class SensorsPlugin(Plugin):
    class GlobalIllumination(ParentElement):
        def __init__(
                self,
                type: str = "vct",
                enabled: bool | None = None,
                resolution: list[int] | str | None = None,
                octant_count: list[int] | str | None = None,
                bounce_count: int | None = None,
                high_quality: bool | None = None,
                anisotropic: bool | None = None,
                thin_wall_counter: float | None = None,
                conserve_memory: bool | None = None,
                debug_vis_mode: str | None = None
        ):
            if isinstance(resolution, list):
                resolution = " ".join(map(str, resolution))
            if isinstance(octant_count, list):
                octant_count = " ".join(map(str, octant_count))

            super().__init__(
                "global_illumination",
                [
                    TextElement("enabled", enabled) if enabled is not None else None,
                    TextElement("resolution", resolution) if resolution is not None else None,
                    TextElement("octant_count", octant_count) if octant_count is not None else None,
                    TextElement("bounce_count", str(bounce_count)) if bounce_count is not None else None,
                    TextElement("high_quality", high_quality) if high_quality is not None else None,
                    TextElement("anisotropic", anisotropic) if anisotropic is not None else None,
                    TextElement("thin_wall_counter", str(thin_wall_counter)) if thin_wall_counter is not None else None,
                    TextElement("conserve_memory", conserve_memory) if conserve_memory is not None else None,
                    TextElement("debug_vis_mode", debug_vis_mode) if debug_vis_mode is not None else None
                ],
                type=type
            )

    def __init__(
            self,
            render_engine: str | None = None,
            render_engine_api_backend: str | None = None,
            disable_on_drained_battery: bool | None = None,
            background_color: list[float] | str | None = None,
            ambient_light: list[float] | str | None = None,
            global_illumination: GlobalIllumination | None = None,
    ):
        if isinstance(background_color, list):
            background_color = " ".join(map(str, background_color))
        if isinstance(ambient_light, list):
            ambient_light = " ".join(map(str, ambient_light))

        elements = []
        if global_illumination is not None:
            elements.append(global_illumination)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-sensors-system",
            name="gz::sim::systems::Sensors",
            elements=elements,
            render_engine=render_engine,
            render_engine_api_backend=render_engine_api_backend,
            disable_on_drained_battery=disable_on_drained_battery,
            background_color=background_color,
            ambient_light=ambient_light,
        )
