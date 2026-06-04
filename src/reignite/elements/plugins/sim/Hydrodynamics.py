from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-hydrodynamics-system", "gz::sim::systems::Hydrodynamics")
class HydrodynamicsPlugin(Plugin):
    def __init__(
            self,
            link_name: str,
            namespace: str | None = None,
            disable_coriolis: bool = False,
            disable_added_mass: bool = False,
            default_current: list[float] | tuple[float, float, float] | None = None,
            lookup_current_x: str | None = None,
            lookup_current_y: str | None = None,
            lookup_current_z: str | None = None,
            **stability_derivatives: float
    ):
        if not link_name:
            raise ValueError("link_name is strictly required for the Hydrodynamics plugin to act upon.")

        if default_current is not None and len(default_current) != 3:
            raise ValueError("default_current must be a 3-dimensional vector (x, y, z) if specified.")

        # The C++ plugin expects stability derivatives in SNAME 1950 convention.
        # e.g., xU, yV, xUU, xUabsU, xDotU. We pass any additional kwargs directly.
        self.link_name = link_name
        self.namespace = namespace
        self.disable_coriolis = disable_coriolis
        self.disable_added_mass = disable_added_mass
        self.default_current = default_current
        self.lookup_current_x = lookup_current_x
        self.lookup_current_y = lookup_current_y
        self.lookup_current_z = lookup_current_z
        self.stability_derivatives = stability_derivatives
        
        super().__init__(sdf_version=None, filename="gz-sim-hydrodynamics-system", name="gz::sim::systems::Hydrodynamics")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        namespace_el = el.find('namespace')
        disable_coriolis_el = el.find('disable_coriolis')
        disable_added_mass_el = el.find('disable_added_mass')
        default_current_el = el.find('default_current')
        lookup_current_x_el = el.find('lookup_current_x')
        lookup_current_y_el = el.find('lookup_current_y')
        lookup_current_z_el = el.find('lookup_current_z')
        
        kwargs = {}
        for c in el:
            if c.tag not in ['link_name', 'namespace', 'disable_coriolis', 'disable_added_mass', 'default_current', 'lookup_current_x', 'lookup_current_y', 'lookup_current_z', 'plugin']:
                if c.text is not None:
                    kwargs[c.tag] = float(c.text)

        default_current = None
        if default_current_el is not None and default_current_el.text:
            parts = default_current_el.text.split()
            if len(parts) == 3:
                default_current = [float(p) for p in parts]

        return cls(
            link_name=link_name_el.text if link_name_el is not None else "",
            namespace=namespace_el.text if namespace_el is not None else None,
            disable_coriolis=disable_coriolis_el.text.lower() == 'true' if disable_coriolis_el is not None and disable_coriolis_el.text is not None else False,
            disable_added_mass=disable_added_mass_el.text.lower() == 'true' if disable_added_mass_el is not None and disable_added_mass_el.text is not None else False,
            default_current=default_current,
            lookup_current_x=lookup_current_x_el.text if lookup_current_x_el is not None else None,
            lookup_current_y=lookup_current_y_el.text if lookup_current_y_el is not None else None,
            lookup_current_z=lookup_current_z_el.text if lookup_current_z_el is not None else None,
            **kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::Hydrodynamics", filename="gz-sim-hydrodynamics-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                elif isinstance(v, (list, tuple)):
                    child.text = " ".join(str(x) for x in v)
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link_name', self.link_name)
        _add('namespace', self.namespace)
        _add('disable_coriolis', self.disable_coriolis)
        _add('disable_added_mass', self.disable_added_mass)
        _add('default_current', self.default_current)
        _add('lookup_current_x', self.lookup_current_x)
        _add('lookup_current_y', self.lookup_current_y)
        _add('lookup_current_z', self.lookup_current_z)
        
        if self.stability_derivatives:
            for k, v in self.stability_derivatives.items():
                _add(k, v)
            
        return el

    def to_version(self, target_version: str):
        return self
