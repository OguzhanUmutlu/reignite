from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-magnetometer-system", "gz::sim::systems::Magnetometer")
class MagnetometerPlugin(Plugin):
    def __init__(
            self,
            use_units_gauss: bool | None = None,
            use_earth_frame_ned: bool | None = None,
    ):
        self.use_units_gauss = use_units_gauss
        self.use_earth_frame_ned = use_earth_frame_ned
        super().__init__(sdf_version=None, filename="gz-sim-magnetometer-system", name="gz::sim::systems::Magnetometer")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        use_units_gauss_el = el.find('use_units_gauss')
        use_earth_frame_ned_el = el.find('use_earth_frame_ned')

        return cls(
            use_units_gauss=use_units_gauss_el.text.lower() == 'true' if use_units_gauss_el is not None and use_units_gauss_el.text is not None else None,
            use_earth_frame_ned=use_earth_frame_ned_el.text.lower() == 'true' if use_earth_frame_ned_el is not None and use_earth_frame_ned_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Magnetometer", filename="gz-sim-magnetometer-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('use_units_gauss', self.use_units_gauss)
        _add('use_earth_frame_ned', self.use_earth_frame_ned)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        use_units_gauss_el = el.find('use_units_gauss')
        use_earth_frame_ned_el = el.find('use_earth_frame_ned')

        return cls(
            use_units_gauss=use_units_gauss_el.text.lower() == 'true' if use_units_gauss_el is not None and use_units_gauss_el.text is not None else None,
            use_earth_frame_ned=use_earth_frame_ned_el.text.lower() == 'true' if use_earth_frame_ned_el is not None and use_earth_frame_ned_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Magnetometer", filename="gz-sim-magnetometer-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('use_units_gauss', self.use_units_gauss)
        _add('use_earth_frame_ned', self.use_earth_frame_ned)
            
        return el

    def to_version(self, target_version: str):
        return self
