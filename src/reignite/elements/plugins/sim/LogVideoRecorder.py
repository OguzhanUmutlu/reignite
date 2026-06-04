from reignite.elements.plugin import Plugin, ParentElement, TextElement


@Plugin.register("gz-sim-log-video-recorder-system", "gz::sim::systems::LogVideoRecorder")
class LogVideoRecorderPlugin(Plugin):
    class Region(ParentElement):
        def __init__(self, min: list[float] | tuple[float, float, float] | str,
                     max: list[float] | tuple[float, float, float] | str):
            if isinstance(min, (list, tuple)):
                min = " ".join(map(str, min))
            if isinstance(max, (list, tuple)):
                max = " ".join(map(str, max))
            super().__init__(
                "region",
                TextElement("min", min),
                TextElement("max", max)
            )

    def __init__(
            self,
            entity: str | list[str] | None = None,
            region: Region | list[Region] | None = None,
            start_time: float | None = None,
            end_time: float | None = None,
            exit_on_finish: bool | None = None,
    ):
        elements = []
        if entity is not None:
            if isinstance(entity, str):
                entity = [entity]
            for e in entity:
                elements.append(TextElement("entity", e))

        if region is not None:
            if isinstance(region, LogVideoRecorderPlugin.Region):
                region = [region]
            elements.extend(region)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-log-video-recorder-system",
            name="gz::sim::systems::LogVideoRecorder",
            elements=elements,
            start_time=start_time,
            end_time=end_time,
            exit_on_finish=exit_on_finish,
        )
