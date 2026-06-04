from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-logical-camera-system", "gz::sim::systems::LogicalCamera")
class LogicalCameraPlugin(Plugin):
    def __init__(
            self,
            topic: str | None = None,
    ):
        self.topic = topic
        super().__init__(sdf_version=None, filename="gz-sim-logical-camera-system", name="gz::sim::systems::LogicalCamera")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        topic_el = el.find('topic')

        return cls(
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LogicalCamera", filename="gz-sim-logical-camera-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('topic', self.topic)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        topic_el = el.find('topic')

        return cls(
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LogicalCamera", filename="gz-sim-logical-camera-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('topic', self.topic)
            
        return el

    def to_version(self, target_version: str):
        return self
