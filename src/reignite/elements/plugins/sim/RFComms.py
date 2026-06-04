from reignite.elements.plugin import Plugin


class RFCommsPlugin(Plugin):
    def __init__(
            self,
            max_range: float | None = None,
            fading_exponent: float | None = None,
            l0: float | None = None,
            sigma: float | None = None,
            capacity: float | None = None,
            tx_power: float | None = None,
            modulation: str | None = None,
            noise_floor: float | None = None,
            **kwargs
    ):
        super().__init__(
            filename="gz-sim-rf-comms-system",
            name="gz::sim::systems::RFComms",
            max_range=max_range,
            fading_exponent=fading_exponent,
            l0=l0,
            sigma=sigma,
            capacity=capacity,
            tx_power=tx_power,
            modulation=modulation,
            noise_floor=noise_floor,
            **kwargs
        )
