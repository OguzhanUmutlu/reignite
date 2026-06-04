from reignite.elements.plugin import Plugin


class MulticopterMotorModelPlugin(Plugin):
    def __init__(
            self,
            robotNamespace: str | None = None,
            jointName: str | None = None,
            linkName: str | None = None,
            actuator_number: int | None = None,
            motorNumber: int | None = None,
            turningDirection: str | None = None,
            motorType: str | None = None,
            commandSubTopic: str | None = None,
            rotorDragCoefficient: float | None = None,
            rollingMomentCoefficient: float | None = None,
            maxRotVelocity: float | None = None,
            motorConstant: float | None = None,
            momentConstant: float | None = None,
            timeConstantUp: float | None = None,
            timeConstantDown: float | None = None,
            rotorVelocitySlowdownSim: float | None = None,
            **kwargs
    ):
        super().__init__(
            filename="gz-sim-multicopter-motor-model-system",
            name="gz::sim::systems::MulticopterMotorModel",
            robotNamespace=robotNamespace,
            jointName=jointName,
            linkName=linkName,
            actuator_number=actuator_number,
            motorNumber=motorNumber,
            turningDirection=turningDirection,
            motorType=motorType,
            commandSubTopic=commandSubTopic,
            rotorDragCoefficient=rotorDragCoefficient,
            rollingMomentCoefficient=rollingMomentCoefficient,
            maxRotVelocity=maxRotVelocity,
            motorConstant=motorConstant,
            momentConstant=momentConstant,
            timeConstantUp=timeConstantUp,
            timeConstantDown=timeConstantDown,
            rotorVelocitySlowdownSim=rotorVelocitySlowdownSim,
            **kwargs
        )
