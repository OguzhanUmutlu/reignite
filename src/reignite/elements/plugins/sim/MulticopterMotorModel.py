from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-multicopter-motor-model-system", "gz::sim::systems::MulticopterMotorModel")
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
        self.robotNamespace = robotNamespace
        self.jointName = jointName
        self.linkName = linkName
        self.actuator_number = actuator_number
        self.motorNumber = motorNumber
        self.turningDirection = turningDirection
        self.motorType = motorType
        self.commandSubTopic = commandSubTopic
        self.rotorDragCoefficient = rotorDragCoefficient
        self.rollingMomentCoefficient = rollingMomentCoefficient
        self.maxRotVelocity = maxRotVelocity
        self.motorConstant = motorConstant
        self.momentConstant = momentConstant
        self.timeConstantUp = timeConstantUp
        self.timeConstantDown = timeConstantDown
        self.rotorVelocitySlowdownSim = rotorVelocitySlowdownSim
        super().__init__(sdf_version=None, filename="gz-sim-multicopter-motor-model-system", name="gz::sim::systems::MulticopterMotorModel")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        robotNamespace_el = el.find('robotNamespace')
        jointName_el = el.find('jointName')
        linkName_el = el.find('linkName')
        actuator_number_el = el.find('actuator_number')
        motorNumber_el = el.find('motorNumber')
        turningDirection_el = el.find('turningDirection')
        motorType_el = el.find('motorType')
        commandSubTopic_el = el.find('commandSubTopic')
        rotorDragCoefficient_el = el.find('rotorDragCoefficient')
        rollingMomentCoefficient_el = el.find('rollingMomentCoefficient')
        maxRotVelocity_el = el.find('maxRotVelocity')
        motorConstant_el = el.find('motorConstant')
        momentConstant_el = el.find('momentConstant')
        timeConstantUp_el = el.find('timeConstantUp')
        timeConstantDown_el = el.find('timeConstantDown')
        rotorVelocitySlowdownSim_el = el.find('rotorVelocitySlowdownSim')

        return cls(
            robotNamespace=robotNamespace_el.text if robotNamespace_el is not None and robotNamespace_el.text is not None else None,
            jointName=jointName_el.text if jointName_el is not None and jointName_el.text is not None else None,
            linkName=linkName_el.text if linkName_el is not None and linkName_el.text is not None else None,
            actuator_number=int(actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            motorNumber=int(motorNumber_el.text) if motorNumber_el is not None and motorNumber_el.text is not None else None,
            turningDirection=turningDirection_el.text if turningDirection_el is not None and turningDirection_el.text is not None else None,
            motorType=motorType_el.text if motorType_el is not None and motorType_el.text is not None else None,
            commandSubTopic=commandSubTopic_el.text if commandSubTopic_el is not None and commandSubTopic_el.text is not None else None,
            rotorDragCoefficient=float(rotorDragCoefficient_el.text) if rotorDragCoefficient_el is not None and rotorDragCoefficient_el.text is not None else None,
            rollingMomentCoefficient=float(rollingMomentCoefficient_el.text) if rollingMomentCoefficient_el is not None and rollingMomentCoefficient_el.text is not None else None,
            maxRotVelocity=float(maxRotVelocity_el.text) if maxRotVelocity_el is not None and maxRotVelocity_el.text is not None else None,
            motorConstant=float(motorConstant_el.text) if motorConstant_el is not None and motorConstant_el.text is not None else None,
            momentConstant=float(momentConstant_el.text) if momentConstant_el is not None and momentConstant_el.text is not None else None,
            timeConstantUp=float(timeConstantUp_el.text) if timeConstantUp_el is not None and timeConstantUp_el.text is not None else None,
            timeConstantDown=float(timeConstantDown_el.text) if timeConstantDown_el is not None and timeConstantDown_el.text is not None else None,
            rotorVelocitySlowdownSim=float(rotorVelocitySlowdownSim_el.text) if rotorVelocitySlowdownSim_el is not None and rotorVelocitySlowdownSim_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::MulticopterMotorModel", filename="gz-sim-multicopter-motor-model-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('robotNamespace', self.robotNamespace)
        _add('jointName', self.jointName)
        _add('linkName', self.linkName)
        _add('actuator_number', self.actuator_number)
        _add('motorNumber', self.motorNumber)
        _add('turningDirection', self.turningDirection)
        _add('motorType', self.motorType)
        _add('commandSubTopic', self.commandSubTopic)
        _add('rotorDragCoefficient', self.rotorDragCoefficient)
        _add('rollingMomentCoefficient', self.rollingMomentCoefficient)
        _add('maxRotVelocity', self.maxRotVelocity)
        _add('motorConstant', self.motorConstant)
        _add('momentConstant', self.momentConstant)
        _add('timeConstantUp', self.timeConstantUp)
        _add('timeConstantDown', self.timeConstantDown)
        _add('rotorVelocitySlowdownSim', self.rotorVelocitySlowdownSim)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        robotNamespace_el = el.find('robotNamespace')
        jointName_el = el.find('jointName')
        linkName_el = el.find('linkName')
        actuator_number_el = el.find('actuator_number')
        motorNumber_el = el.find('motorNumber')
        turningDirection_el = el.find('turningDirection')
        motorType_el = el.find('motorType')
        commandSubTopic_el = el.find('commandSubTopic')
        rotorDragCoefficient_el = el.find('rotorDragCoefficient')
        rollingMomentCoefficient_el = el.find('rollingMomentCoefficient')
        maxRotVelocity_el = el.find('maxRotVelocity')
        motorConstant_el = el.find('motorConstant')
        momentConstant_el = el.find('momentConstant')
        timeConstantUp_el = el.find('timeConstantUp')
        timeConstantDown_el = el.find('timeConstantDown')
        rotorVelocitySlowdownSim_el = el.find('rotorVelocitySlowdownSim')

        return cls(
            robotNamespace=robotNamespace_el.text if robotNamespace_el is not None and robotNamespace_el.text is not None else None,
            jointName=jointName_el.text if jointName_el is not None and jointName_el.text is not None else None,
            linkName=linkName_el.text if linkName_el is not None and linkName_el.text is not None else None,
            actuator_number=int(actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            motorNumber=int(motorNumber_el.text) if motorNumber_el is not None and motorNumber_el.text is not None else None,
            turningDirection=turningDirection_el.text if turningDirection_el is not None and turningDirection_el.text is not None else None,
            motorType=motorType_el.text if motorType_el is not None and motorType_el.text is not None else None,
            commandSubTopic=commandSubTopic_el.text if commandSubTopic_el is not None and commandSubTopic_el.text is not None else None,
            rotorDragCoefficient=float(rotorDragCoefficient_el.text) if rotorDragCoefficient_el is not None and rotorDragCoefficient_el.text is not None else None,
            rollingMomentCoefficient=float(rollingMomentCoefficient_el.text) if rollingMomentCoefficient_el is not None and rollingMomentCoefficient_el.text is not None else None,
            maxRotVelocity=float(maxRotVelocity_el.text) if maxRotVelocity_el is not None and maxRotVelocity_el.text is not None else None,
            motorConstant=float(motorConstant_el.text) if motorConstant_el is not None and motorConstant_el.text is not None else None,
            momentConstant=float(momentConstant_el.text) if momentConstant_el is not None and momentConstant_el.text is not None else None,
            timeConstantUp=float(timeConstantUp_el.text) if timeConstantUp_el is not None and timeConstantUp_el.text is not None else None,
            timeConstantDown=float(timeConstantDown_el.text) if timeConstantDown_el is not None and timeConstantDown_el.text is not None else None,
            rotorVelocitySlowdownSim=float(rotorVelocitySlowdownSim_el.text) if rotorVelocitySlowdownSim_el is not None and rotorVelocitySlowdownSim_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::MulticopterMotorModel", filename="gz-sim-multicopter-motor-model-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('robotNamespace', self.robotNamespace)
        _add('jointName', self.jointName)
        _add('linkName', self.linkName)
        _add('actuator_number', self.actuator_number)
        _add('motorNumber', self.motorNumber)
        _add('turningDirection', self.turningDirection)
        _add('motorType', self.motorType)
        _add('commandSubTopic', self.commandSubTopic)
        _add('rotorDragCoefficient', self.rotorDragCoefficient)
        _add('rollingMomentCoefficient', self.rollingMomentCoefficient)
        _add('maxRotVelocity', self.maxRotVelocity)
        _add('motorConstant', self.motorConstant)
        _add('momentConstant', self.momentConstant)
        _add('timeConstantUp', self.timeConstantUp)
        _add('timeConstantDown', self.timeConstantDown)
        _add('rotorVelocitySlowdownSim', self.rotorVelocitySlowdownSim)
            
        return el

    def to_version(self, target_version: str):
        return self
