from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-optical-tactile-plugin-system", "gz::sim::systems::OpticalTactilePlugin")
class OpticalTactilePlugin(Plugin):
    def __init__(
            self,
            enabled: bool | None = None,
            visualization_resolution: int | None = None,
            visualize_forces: bool | None = None,
            visualize_contacts: bool | None = None,
            extended_sensing: float | None = None,
            visualize_sensor: bool | None = None,
            force_length: float | None = None,
            namespace: str | None = None,
            size: list[float] | str | None = None,
            **kwargs
    ):
        if isinstance(size, list):
            size = " ".join(map(str, size))

        self.enabled = enabled
        self.visualization_resolution = visualization_resolution
        self.visualize_forces = visualize_forces
        self.visualize_contacts = visualize_contacts
        self.extended_sensing = extended_sensing
        self.visualize_sensor = visualize_sensor
        self.force_length = force_length
        self.namespace = namespace
        self.size = size
        super().__init__(sdf_version=None, filename="gz-sim-optical-tactile-plugin-system",
                         name="gz::sim::systems::OpticalTactilePlugin")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        enabled_el = el.find('enabled')
        visualization_resolution_el = el.find('visualization_resolution')
        visualize_forces_el = el.find('visualize_forces')
        visualize_contacts_el = el.find('visualize_contacts')
        extended_sensing_el = el.find('extended_sensing')
        visualize_sensor_el = el.find('visualize_sensor')
        force_length_el = el.find('force_length')
        namespace_el = el.find('namespace')
        size_els = el.findall('size')
        size_vals = [e.text for e in size_els if e.text is not None] if size_els else None

        return cls(
            enabled=enabled_el.text.lower() == 'true' if enabled_el is not None and enabled_el.text is not None else None,
            visualization_resolution=int(
                visualization_resolution_el.text) if visualization_resolution_el is not None and visualization_resolution_el.text is not None else None,
            visualize_forces=visualize_forces_el.text.lower() == 'true' if visualize_forces_el is not None and visualize_forces_el.text is not None else None,
            visualize_contacts=visualize_contacts_el.text.lower() == 'true' if visualize_contacts_el is not None and visualize_contacts_el.text is not None else None,
            extended_sensing=float(
                extended_sensing_el.text) if extended_sensing_el is not None and extended_sensing_el.text is not None else None,
            visualize_sensor=visualize_sensor_el.text.lower() == 'true' if visualize_sensor_el is not None and visualize_sensor_el.text is not None else None,
            force_length=float(
                force_length_el.text) if force_length_el is not None and force_length_el.text is not None else None,
            namespace=namespace_el.text if namespace_el is not None and namespace_el.text is not None else None,
            size=size_vals,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::OpticalTactilePlugin",
                        filename="gz-sim-optical-tactile-plugin-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('enabled', self.enabled)
        _add('visualization_resolution', self.visualization_resolution)
        _add('visualize_forces', self.visualize_forces)
        _add('visualize_contacts', self.visualize_contacts)
        _add('extended_sensing', self.extended_sensing)
        _add('visualize_sensor', self.visualize_sensor)
        _add('force_length', self.force_length)
        _add('namespace', self.namespace)
        if self.size is not None:
            for v in (self.size if isinstance(self.size, list) else [self.size]):
                _add('size', v)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        enabled_el = el.find('enabled')
        visualization_resolution_el = el.find('visualization_resolution')
        visualize_forces_el = el.find('visualize_forces')
        visualize_contacts_el = el.find('visualize_contacts')
        extended_sensing_el = el.find('extended_sensing')
        visualize_sensor_el = el.find('visualize_sensor')
        force_length_el = el.find('force_length')
        namespace_el = el.find('namespace')
        size_els = el.findall('size')
        size_vals = [e.text for e in size_els if e.text is not None] if size_els else None

        return cls(
            enabled=enabled_el.text.lower() == 'true' if enabled_el is not None and enabled_el.text is not None else None,
            visualization_resolution=int(
                visualization_resolution_el.text) if visualization_resolution_el is not None and visualization_resolution_el.text is not None else None,
            visualize_forces=visualize_forces_el.text.lower() == 'true' if visualize_forces_el is not None and visualize_forces_el.text is not None else None,
            visualize_contacts=visualize_contacts_el.text.lower() == 'true' if visualize_contacts_el is not None and visualize_contacts_el.text is not None else None,
            extended_sensing=float(
                extended_sensing_el.text) if extended_sensing_el is not None and extended_sensing_el.text is not None else None,
            visualize_sensor=visualize_sensor_el.text.lower() == 'true' if visualize_sensor_el is not None and visualize_sensor_el.text is not None else None,
            force_length=float(
                force_length_el.text) if force_length_el is not None and force_length_el.text is not None else None,
            namespace=namespace_el.text if namespace_el is not None and namespace_el.text is not None else None,
            size=size_vals,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::OpticalTactilePlugin",
                        filename="gz-sim-optical-tactile-plugin-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('enabled', self.enabled)
        _add('visualization_resolution', self.visualization_resolution)
        _add('visualize_forces', self.visualize_forces)
        _add('visualize_contacts', self.visualize_contacts)
        _add('extended_sensing', self.extended_sensing)
        _add('visualize_sensor', self.visualize_sensor)
        _add('force_length', self.force_length)
        _add('namespace', self.namespace)
        if self.size is not None:
            for v in (self.size if isinstance(self.size, list) else [self.size]):
                _add('size', v)

        return el

    def to_version(self, target_version: str):
        return self
