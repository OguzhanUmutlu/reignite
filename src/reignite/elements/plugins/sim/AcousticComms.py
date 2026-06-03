from reignite.elements.plugin import Plugin, ParentElement, TextElement


class AcousticCommsPlugin(Plugin):
    class PropagationModel(ParentElement):
        def __init__(
                self,
                source_power: float,
                noise_level: float,
                spectral_efficiency: float,
                seed: int
        ):
            super().__init__(
                "propagation_model",
                [
                    TextElement("source_power", str(source_power)),
                    TextElement("noise_level", str(noise_level)),
                    TextElement("spectral_efficiency", str(spectral_efficiency)),
                    TextElement("seed", str(seed))
                ]
            )

    def __init__(
            self,
            max_range: float = 1000.0,
            speed_of_sound: float = 343.0,
            collision_time_per_byte: float = 0.0,
            propagation_model: PropagationModel | None = None
    ):
        elements = []
        if propagation_model is not None:
            elements.append(propagation_model)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-acoustic-comms-system",
            name="gz::sim::systems::AcousticComms",
            elements=elements,
            max_range=max_range,
            speed_of_sound=speed_of_sound,
            collision_time_per_byte=collision_time_per_byte
        )
