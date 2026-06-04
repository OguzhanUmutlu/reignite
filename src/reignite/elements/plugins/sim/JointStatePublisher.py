from xml.etree import ElementTree as ET
from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-joint-state-publisher-system", "gz::sim::systems::JointStatePublisher")
class JointStatePublisherPlugin(Plugin):
    def __init__(
            self,
            joint_name: str | Joint | list[str | Joint] | None = None,
            topic: str | None = None,
            update_rate: float | None = None
    ):
        def _get_names(joints):
            if joints is None:
                return None
            if isinstance(joints, list):
                return [j.name if isinstance(j, Joint) else j for j in joints]
            return joints.name if isinstance(joints, Joint) else joints

        self.joint_name = _get_names(joint_name)
        self.topic = topic
        self.update_rate = update_rate
        super().__init__(sdf_version=None, filename="gz-sim-joint-state-publisher-system", name="gz::sim::systems::JointStatePublisher")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_els = el.findall('joint_name')
        joint_name_vals = [e.text for e in joint_name_els if e.text is not None] if joint_name_els else None
        topic_el = el.find('topic')
        update_rate_el = el.find('update_rate')

        return cls(
            joint_name=joint_name_vals,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            update_rate=float(update_rate_el.text) if update_rate_el is not None and update_rate_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::JointStatePublisher", filename="gz-sim-joint-state-publisher-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.joint_name is not None:
            for v in (self.joint_name if isinstance(self.joint_name, list) else [self.joint_name]):
                _add('joint_name', v)
        _add('topic', self.topic)
        _add('update_rate', self.update_rate)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_els = el.findall('joint_name')
        joint_name_vals = [e.text for e in joint_name_els if e.text is not None] if joint_name_els else None
        topic_el = el.find('topic')
        update_rate_el = el.find('update_rate')

        return cls(
            joint_name=joint_name_vals,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            update_rate=float(update_rate_el.text) if update_rate_el is not None and update_rate_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::JointStatePublisher", filename="gz-sim-joint-state-publisher-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.joint_name is not None:
            for v in (self.joint_name if isinstance(self.joint_name, list) else [self.joint_name]):
                _add('joint_name', v)
        _add('topic', self.topic)
        _add('update_rate', self.update_rate)
            
        return el

    def to_version(self, target_version: str):
        return self
