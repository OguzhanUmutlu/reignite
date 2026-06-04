from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-user-commands-system", "gz::sim::systems::UserCommands")
class UserCommandsPlugin(Plugin):
    def __init__(
            self,
            set_all_light_entities: bool | None = None,
    ):
        self.set_all_light_entities = set_all_light_entities
        super().__init__(sdf_version=None, filename="gz-sim-user-commands-system", name="gz::sim::systems::UserCommands")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        set_all_light_entities_el = el.find('set_all_light_entities')

        return cls(
            set_all_light_entities=set_all_light_entities_el.text.lower() == 'true' if set_all_light_entities_el is not None and set_all_light_entities_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::UserCommands", filename="gz-sim-user-commands-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('set_all_light_entities', self.set_all_light_entities)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        set_all_light_entities_el = el.find('set_all_light_entities')

        return cls(
            set_all_light_entities=set_all_light_entities_el.text.lower() == 'true' if set_all_light_entities_el is not None and set_all_light_entities_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::UserCommands", filename="gz-sim-user-commands-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('set_all_light_entities', self.set_all_light_entities)
            
        return el

    def to_version(self, target_version: str):
        return self
