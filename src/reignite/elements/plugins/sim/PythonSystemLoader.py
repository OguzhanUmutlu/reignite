from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-python-system-loader-system", "gz::sim::systems::PythonSystemLoader")
class PythonSystemLoaderPlugin(Plugin):
    def __init__(
            self,
            module_name: str | None = None,
    ):
        self.module_name = module_name
        super().__init__(sdf_version=None, filename="gz-sim-python-system-loader-system", name="gz::sim::systems::PythonSystemLoader")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        module_name_el = el.find('module_name')

        return cls(
            module_name=module_name_el.text if module_name_el is not None and module_name_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::PythonSystemLoader", filename="gz-sim-python-system-loader-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('module_name', self.module_name)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        module_name_el = el.find('module_name')

        return cls(
            module_name=module_name_el.text if module_name_el is not None and module_name_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::PythonSystemLoader", filename="gz-sim-python-system-loader-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('module_name', self.module_name)
            
        return el

    def to_version(self, target_version: str):
        return self
