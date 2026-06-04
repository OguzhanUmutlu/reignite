from reignite.elements.plugin import Plugin, ParentElement, TextElement


@Plugin.register("gz-sim-logical-audio-sensor-plugin-system", "gz::sim::systems::LogicalAudioSensorPlugin")
class LogicalAudioSensorPlugin(Plugin):
    class Source(ParentElement):
        def __init__(
                self,
                id: int | str,
                pose: list[float] | str,
                attenuation_function: str,
                attenuation_shape: str,
                inner_radius: float,
                falloff_distance: float,
                volume_level: float,
                playing: bool | None = None,
                play_duration: float | None = None
        ):
            if isinstance(pose, list):
                pose = " ".join(map(str, pose))

            super().__init__(
                "source",
                TextElement("id", str(id)),
                TextElement("pose", pose),
                TextElement("attenuation_function", attenuation_function),
                TextElement("attenuation_shape", attenuation_shape),
                TextElement("inner_radius", str(inner_radius)),
                TextElement("falloff_distance", str(falloff_distance)),
                TextElement("volume_level", str(volume_level)),
                TextElement("playing", playing) if playing is not None else None,
                TextElement("play_duration", str(play_duration)) if play_duration is not None else None
            )

    class Microphone(ParentElement):
        def __init__(
                self,
                id: int | str,
                pose: list[float] | str,
                volume_threshold: float
        ):
            if isinstance(pose, list):
                pose = " ".join(map(str, pose))

            super().__init__(
                "microphone",
                TextElement("id", str(id)),
                TextElement("pose", pose),
                TextElement("volume_threshold", str(volume_threshold))
            )

    def __init__(
            self,
            source: list[Source] | Source | None = None,
            microphone: list[Microphone] | Microphone | None = None,
    ):
        elements = []
        if source is not None:
            if isinstance(source, LogicalAudioSensorPlugin.Source):
                source = [source]
            elements.extend(source)
        if microphone is not None:
            if isinstance(microphone, LogicalAudioSensorPlugin.Microphone):
                microphone = [microphone]
            elements.extend(microphone)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-logical-audio-sensor-plugin-system",
            name="gz::sim::systems::LogicalAudioSensorPlugin",
            elements=elements,
        )
