from xml.etree import ElementTree as ET
from ...link import Link
from ...plugin import Plugin


@Plugin.register("gz-sim-buoyancy-engine-system", "gz::sim::systems::BuoyancyEngine")
class BuoyancyEnginePlugin(Plugin):
    def __init__(
            self,
            link_name: str | Link,
            min_volume: float | None = None,
            max_volume: float | None = None,
            fluid_density: float | None = None,
            default_volume: float | None = None,
            neutral_volume: float | None = None,
            max_inflation_rate: float | None = None,
            surface: float | None = None,
            namespace: str | None = None
    ):
        self.link_name = link_name.name if isinstance(link_name, Link) else link_name
        self.min_volume = min_volume
        self.max_volume = max_volume
        self.fluid_density = fluid_density
        self.default_volume = default_volume
        self.neutral_volume = neutral_volume
        self.max_inflation_rate = max_inflation_rate
        self.surface = surface
        self.namespace = namespace
        super().__init__(sdf_version=None, filename="gz-sim-buoyancy-engine-system", name="gz::sim::systems::BuoyancyEngine")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        min_volume_el = el.find('min_volume')
        max_volume_el = el.find('max_volume')
        fluid_density_el = el.find('fluid_density')
        default_volume_el = el.find('default_volume')
        neutral_volume_el = el.find('neutral_volume')
        max_inflation_rate_el = el.find('max_inflation_rate')
        surface_el = el.find('surface')
        namespace_el = el.find('namespace')

        return cls(
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            min_volume=float(min_volume_el.text) if min_volume_el is not None and min_volume_el.text is not None else None,
            max_volume=float(max_volume_el.text) if max_volume_el is not None and max_volume_el.text is not None else None,
            fluid_density=float(fluid_density_el.text) if fluid_density_el is not None and fluid_density_el.text is not None else None,
            default_volume=float(default_volume_el.text) if default_volume_el is not None and default_volume_el.text is not None else None,
            neutral_volume=float(neutral_volume_el.text) if neutral_volume_el is not None and neutral_volume_el.text is not None else None,
            max_inflation_rate=float(max_inflation_rate_el.text) if max_inflation_rate_el is not None and max_inflation_rate_el.text is not None else None,
            surface=float(surface_el.text) if surface_el is not None and surface_el.text is not None else None,
            namespace=namespace_el.text if namespace_el is not None and namespace_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::BuoyancyEngine", filename="gz-sim-buoyancy-engine-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link_name', self.link_name)
        _add('min_volume', self.min_volume)
        _add('max_volume', self.max_volume)
        _add('fluid_density', self.fluid_density)
        _add('default_volume', self.default_volume)
        _add('neutral_volume', self.neutral_volume)
        _add('max_inflation_rate', self.max_inflation_rate)
        _add('surface', self.surface)
        _add('namespace', self.namespace)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        min_volume_el = el.find('min_volume')
        max_volume_el = el.find('max_volume')
        fluid_density_el = el.find('fluid_density')
        default_volume_el = el.find('default_volume')
        neutral_volume_el = el.find('neutral_volume')
        max_inflation_rate_el = el.find('max_inflation_rate')
        surface_el = el.find('surface')
        namespace_el = el.find('namespace')

        return cls(
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            min_volume=float(min_volume_el.text) if min_volume_el is not None and min_volume_el.text is not None else None,
            max_volume=float(max_volume_el.text) if max_volume_el is not None and max_volume_el.text is not None else None,
            fluid_density=float(fluid_density_el.text) if fluid_density_el is not None and fluid_density_el.text is not None else None,
            default_volume=float(default_volume_el.text) if default_volume_el is not None and default_volume_el.text is not None else None,
            neutral_volume=float(neutral_volume_el.text) if neutral_volume_el is not None and neutral_volume_el.text is not None else None,
            max_inflation_rate=float(max_inflation_rate_el.text) if max_inflation_rate_el is not None and max_inflation_rate_el.text is not None else None,
            surface=float(surface_el.text) if surface_el is not None and surface_el.text is not None else None,
            namespace=namespace_el.text if namespace_el is not None and namespace_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::BuoyancyEngine", filename="gz-sim-buoyancy-engine-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link_name', self.link_name)
        _add('min_volume', self.min_volume)
        _add('max_volume', self.max_volume)
        _add('fluid_density', self.fluid_density)
        _add('default_volume', self.default_volume)
        _add('neutral_volume', self.neutral_volume)
        _add('max_inflation_rate', self.max_inflation_rate)
        _add('surface', self.surface)
        _add('namespace', self.namespace)
            
        return el

    def to_version(self, target_version: str):
        return self
