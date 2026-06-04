from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-thermal-sensor-system", "gz::sim::systems::ThermalSensor")
class ThermalSensorPlugin(Plugin):
    def __init__(
            self,
            resolution: float | None = None,
            min_temp: float | None = None,
            max_temp: float | None = None,
    ):
        self.resolution = resolution
        self.min_temp = min_temp
        self.max_temp = max_temp
        super().__init__(sdf_version=None, filename="gz-sim-thermal-sensor-system", name="gz::sim::systems::ThermalSensor")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        resolution_el = el.find('resolution')
        min_temp_el = el.find('min_temp')
        max_temp_el = el.find('max_temp')

        return cls(
            resolution=float(resolution_el.text) if resolution_el is not None and resolution_el.text is not None else None,
            min_temp=float(min_temp_el.text) if min_temp_el is not None and min_temp_el.text is not None else None,
            max_temp=float(max_temp_el.text) if max_temp_el is not None and max_temp_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::ThermalSensor", filename="gz-sim-thermal-sensor-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('resolution', self.resolution)
        _add('min_temp', self.min_temp)
        _add('max_temp', self.max_temp)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        resolution_el = el.find('resolution')
        min_temp_el = el.find('min_temp')
        max_temp_el = el.find('max_temp')

        return cls(
            resolution=float(resolution_el.text) if resolution_el is not None and resolution_el.text is not None else None,
            min_temp=float(min_temp_el.text) if min_temp_el is not None and min_temp_el.text is not None else None,
            max_temp=float(max_temp_el.text) if max_temp_el is not None and max_temp_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::ThermalSensor", filename="gz-sim-thermal-sensor-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('resolution', self.resolution)
        _add('min_temp', self.min_temp)
        _add('max_temp', self.max_temp)
            
        return el

    def to_version(self, target_version: str):
        return self
