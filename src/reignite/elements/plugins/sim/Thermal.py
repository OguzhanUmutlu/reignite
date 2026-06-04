from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-thermal-system", "gz::sim::systems::Thermal")
class ThermalPlugin(Plugin):
    def __init__(
            self,
            temperature: float | None = None,
            heat_signature: str | None = None,
            min_temp: float | None = None,
            max_temp: float | None = None,
    ):
        self.temperature = temperature
        self.heat_signature = heat_signature
        self.min_temp = min_temp
        self.max_temp = max_temp
        super().__init__(sdf_version=None, filename="gz-sim-thermal-system", name="gz::sim::systems::Thermal")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        temperature_el = el.find('temperature')
        heat_signature_el = el.find('heat_signature')
        min_temp_el = el.find('min_temp')
        max_temp_el = el.find('max_temp')

        return cls(
            temperature=float(temperature_el.text) if temperature_el is not None and temperature_el.text is not None else None,
            heat_signature=heat_signature_el.text if heat_signature_el is not None and heat_signature_el.text is not None else None,
            min_temp=float(min_temp_el.text) if min_temp_el is not None and min_temp_el.text is not None else None,
            max_temp=float(max_temp_el.text) if max_temp_el is not None and max_temp_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Thermal", filename="gz-sim-thermal-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('temperature', self.temperature)
        _add('heat_signature', self.heat_signature)
        _add('min_temp', self.min_temp)
        _add('max_temp', self.max_temp)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        temperature_el = el.find('temperature')
        heat_signature_el = el.find('heat_signature')
        min_temp_el = el.find('min_temp')
        max_temp_el = el.find('max_temp')

        return cls(
            temperature=float(temperature_el.text) if temperature_el is not None and temperature_el.text is not None else None,
            heat_signature=heat_signature_el.text if heat_signature_el is not None and heat_signature_el.text is not None else None,
            min_temp=float(min_temp_el.text) if min_temp_el is not None and min_temp_el.text is not None else None,
            max_temp=float(max_temp_el.text) if max_temp_el is not None and max_temp_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Thermal", filename="gz-sim-thermal-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('temperature', self.temperature)
        _add('heat_signature', self.heat_signature)
        _add('min_temp', self.min_temp)
        _add('max_temp', self.max_temp)
            
        return el

    def to_version(self, target_version: str):
        return self
