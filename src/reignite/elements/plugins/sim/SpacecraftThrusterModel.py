from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-spacecraft-thruster-model-system", "gz::sim::systems::SpacecraftThrusterModel")
class SpacecraftThrusterModelPlugin(Plugin):
    def __init__(
            self,
            topic: str | None = None,
            link_name: str | None = None,
            actuator_number: int | None = None,
            max_thrust: float | None = None,
            duty_cycle_frequency: float | None = None,
            sub_topic: str | None = None,
    ):
        self.topic = topic
        self.link_name = link_name
        self.actuator_number = actuator_number
        self.max_thrust = max_thrust
        self.duty_cycle_frequency = duty_cycle_frequency
        self.sub_topic = sub_topic
        super().__init__(sdf_version=None, filename="gz-sim-spacecraft-thruster-model-system",
                         name="gz::sim::systems::SpacecraftThrusterModel")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        topic_el = el.find('topic')
        link_name_el = el.find('link_name')
        actuator_number_el = el.find('actuator_number')
        max_thrust_el = el.find('max_thrust')
        duty_cycle_frequency_el = el.find('duty_cycle_frequency')
        sub_topic_el = el.find('sub_topic')

        return cls(
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            actuator_number=int(
                actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            max_thrust=float(
                max_thrust_el.text) if max_thrust_el is not None and max_thrust_el.text is not None else None,
            duty_cycle_frequency=float(
                duty_cycle_frequency_el.text) if duty_cycle_frequency_el is not None and duty_cycle_frequency_el.text is not None else None,
            sub_topic=sub_topic_el.text if sub_topic_el is not None and sub_topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::SpacecraftThrusterModel",
                        filename="gz-sim-spacecraft-thruster-model-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('topic', self.topic)
        _add('link_name', self.link_name)
        _add('actuator_number', self.actuator_number)
        _add('max_thrust', self.max_thrust)
        _add('duty_cycle_frequency', self.duty_cycle_frequency)
        _add('sub_topic', self.sub_topic)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        topic_el = el.find('topic')
        link_name_el = el.find('link_name')
        actuator_number_el = el.find('actuator_number')
        max_thrust_el = el.find('max_thrust')
        duty_cycle_frequency_el = el.find('duty_cycle_frequency')
        sub_topic_el = el.find('sub_topic')

        return cls(
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            actuator_number=int(
                actuator_number_el.text) if actuator_number_el is not None and actuator_number_el.text is not None else None,
            max_thrust=float(
                max_thrust_el.text) if max_thrust_el is not None and max_thrust_el.text is not None else None,
            duty_cycle_frequency=float(
                duty_cycle_frequency_el.text) if duty_cycle_frequency_el is not None and duty_cycle_frequency_el.text is not None else None,
            sub_topic=sub_topic_el.text if sub_topic_el is not None and sub_topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::SpacecraftThrusterModel",
                        filename="gz-sim-spacecraft-thruster-model-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('topic', self.topic)
        _add('link_name', self.link_name)
        _add('actuator_number', self.actuator_number)
        _add('max_thrust', self.max_thrust)
        _add('duty_cycle_frequency', self.duty_cycle_frequency)
        _add('sub_topic', self.sub_topic)

        return el

    def to_version(self, target_version: str):
        return self
