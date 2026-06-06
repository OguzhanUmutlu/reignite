from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-kinetic-energy-monitor-system", "gz::sim::systems::KineticEnergyMonitor")
class KineticEnergyMonitorPlugin(Plugin):
    def __init__(
            self,
            link_name: str,
            kinetic_energy_threshold: float = 7.0,
            topic: str | None = None
    ):
        if not link_name:
            raise ValueError("link_name is required.")

        self.link_name = link_name
        self.kinetic_energy_threshold = kinetic_energy_threshold
        self.topic = topic
        super().__init__(sdf_version=None, filename="gz-sim-kinetic-energy-monitor-system",
                         name="gz::sim::systems::KineticEnergyMonitor")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        kinetic_energy_threshold_el = el.find('kinetic_energy_threshold')
        topic_el = el.find('topic')

        return cls(
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            kinetic_energy_threshold=float(
                kinetic_energy_threshold_el.text) if kinetic_energy_threshold_el is not None and kinetic_energy_threshold_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::KineticEnergyMonitor",
                        filename="gz-sim-kinetic-energy-monitor-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('link_name', self.link_name)
        _add('kinetic_energy_threshold', self.kinetic_energy_threshold)
        _add('topic', self.topic)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        kinetic_energy_threshold_el = el.find('kinetic_energy_threshold')
        topic_el = el.find('topic')

        return cls(
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            kinetic_energy_threshold=float(
                kinetic_energy_threshold_el.text) if kinetic_energy_threshold_el is not None and kinetic_energy_threshold_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::KineticEnergyMonitor",
                        filename="gz-sim-kinetic-energy-monitor-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('link_name', self.link_name)
        _add('kinetic_energy_threshold', self.kinetic_energy_threshold)
        _add('topic', self.topic)

        return el

    def to_version(self, target_version: str):
        return self
