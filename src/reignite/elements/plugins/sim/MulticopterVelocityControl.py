from reignite.elements.plugin import Plugin


class MulticopterVelocityControl(Plugin):
    def __init__(
            self,
            angularRateGain: list[float] | str | None = None,
            maximumLinearAcceleration: list[float] | str | None = None,
            maximumLinearVelocity: list[float] | str | None = None,
            maximumAngularVelocity: list[float] | str | None = None,
            linearVelocityNoiseMean: list[float] | str | None = None,
            linearVelocityNoiseStdDev: list[float] | str | None = None,
            angularVelocityNoiseMean: list[float] | str | None = None,
            angularVelocityNoiseStdDev: list[float] | str | None = None,
            robotNamespace: str | None = None,
            commandSubTopic: str | None = None,
            enableSubTopic: str | None = None,
            **kwargs
    ):
        params = {
            "angularRateGain": angularRateGain,
            "maximumLinearAcceleration": maximumLinearAcceleration,
            "maximumLinearVelocity": maximumLinearVelocity,
            "maximumAngularVelocity": maximumAngularVelocity,
            "linearVelocityNoiseMean": linearVelocityNoiseMean,
            "linearVelocityNoiseStdDev": linearVelocityNoiseStdDev,
            "angularVelocityNoiseMean": angularVelocityNoiseMean,
            "angularVelocityNoiseStdDev": angularVelocityNoiseStdDev,
        }

        for k, v in params.items():
            if isinstance(v, list):
                params[k] = " ".join(map(str, v))

        super().__init__(
            filename="gz-sim-multicopter-control-system",
            name="gz::sim::systems::MulticopterVelocityControl",
            robotNamespace=robotNamespace,
            commandSubTopic=commandSubTopic,
            enableSubTopic=enableSubTopic,
            **params,
            **kwargs
        )
