from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-scene-broadcaster-system", "gz::sim::systems::SceneBroadcaster")
class SceneBroadcasterPlugin(Plugin):
    def __init__(
            self,
            dynamic_pose_hertz: int | None = None,
            state_hertz: float | None = None,
    ):
        self.dynamic_pose_hertz = dynamic_pose_hertz
        self.state_hertz = state_hertz
        super().__init__(sdf_version=None, filename="gz-sim-scene-broadcaster-system", name="gz::sim::systems::SceneBroadcaster")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        dynamic_pose_hertz_el = el.find('dynamic_pose_hertz')
        state_hertz_el = el.find('state_hertz')

        return cls(
            dynamic_pose_hertz=int(dynamic_pose_hertz_el.text) if dynamic_pose_hertz_el is not None and dynamic_pose_hertz_el.text is not None else None,
            state_hertz=float(state_hertz_el.text) if state_hertz_el is not None and state_hertz_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::SceneBroadcaster", filename="gz-sim-scene-broadcaster-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('dynamic_pose_hertz', self.dynamic_pose_hertz)
        _add('state_hertz', self.state_hertz)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        dynamic_pose_hertz_el = el.find('dynamic_pose_hertz')
        state_hertz_el = el.find('state_hertz')

        return cls(
            dynamic_pose_hertz=int(dynamic_pose_hertz_el.text) if dynamic_pose_hertz_el is not None and dynamic_pose_hertz_el.text is not None else None,
            state_hertz=float(state_hertz_el.text) if state_hertz_el is not None and state_hertz_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::SceneBroadcaster", filename="gz-sim-scene-broadcaster-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('dynamic_pose_hertz', self.dynamic_pose_hertz)
        _add('state_hertz', self.state_hertz)
            
        return el

    def to_version(self, target_version: str):
        return self
