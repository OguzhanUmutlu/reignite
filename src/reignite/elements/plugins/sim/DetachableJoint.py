from xml.etree import ElementTree as ET

from ...link import Link
from ...model import Model
from ...plugin import Plugin


@Plugin.register("gz-sim-detachable-joint-system", "gz::sim:systems::DetachableJoint")
class DetachableJointPlugin(Plugin):
    def __init__(
            self,
            parent_link: Link | str,
            child_model: Model | str,
            child_link: Link | str,
            detach_topic: str | None = None,
            topic: str | None = None,
            attach_topic: str | None = None,
            output_topic: str | None = None,
            suppress_child_warning: bool = True
    ):
        self.parent_link = parent_link if isinstance(parent_link, str) else parent_link.name
        self.child_model = child_model if isinstance(child_model, str) else child_model.name
        self.child_link = child_link if isinstance(child_link, str) else child_link.name
        self.detach_topic = detach_topic
        self.topic = topic
        self.attach_topic = attach_topic
        self.output_topic = output_topic
        self.suppress_child_warning = suppress_child_warning
        super().__init__(sdf_version=None, filename="gz-sim-detachable-joint-system",
                         name="gz::sim:systems::DetachableJoint")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        parent_link_el = el.find('parent_link')
        child_model_el = el.find('child_model')
        child_link_el = el.find('child_link')
        detach_topic_el = el.find('detach_topic')
        topic_el = el.find('topic')
        attach_topic_el = el.find('attach_topic')
        output_topic_el = el.find('output_topic')
        suppress_child_warning_el = el.find('suppress_child_warning')

        return cls(
            parent_link=parent_link_el.text if parent_link_el is not None and parent_link_el.text is not None else None,
            child_model=child_model_el.text if child_model_el is not None and child_model_el.text is not None else None,
            child_link=child_link_el.text if child_link_el is not None and child_link_el.text is not None else None,
            detach_topic=detach_topic_el.text if detach_topic_el is not None and detach_topic_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            attach_topic=attach_topic_el.text if attach_topic_el is not None and attach_topic_el.text is not None else None,
            output_topic=output_topic_el.text if output_topic_el is not None and output_topic_el.text is not None else None,
            suppress_child_warning=suppress_child_warning_el.text.lower() == 'true' if suppress_child_warning_el is not None and suppress_child_warning_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim:systems::DetachableJoint",
                        filename="gz-sim-detachable-joint-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('parent_link', self.parent_link)
        _add('child_model', self.child_model)
        _add('child_link', self.child_link)
        _add('detach_topic', self.detach_topic)
        _add('topic', self.topic)
        _add('attach_topic', self.attach_topic)
        _add('output_topic', self.output_topic)
        _add('suppress_child_warning', self.suppress_child_warning)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        parent_link_el = el.find('parent_link')
        child_model_el = el.find('child_model')
        child_link_el = el.find('child_link')
        detach_topic_el = el.find('detach_topic')
        topic_el = el.find('topic')
        attach_topic_el = el.find('attach_topic')
        output_topic_el = el.find('output_topic')
        suppress_child_warning_el = el.find('suppress_child_warning')

        return cls(
            parent_link=parent_link_el.text if parent_link_el is not None and parent_link_el.text is not None else None,
            child_model=child_model_el.text if child_model_el is not None and child_model_el.text is not None else None,
            child_link=child_link_el.text if child_link_el is not None and child_link_el.text is not None else None,
            detach_topic=detach_topic_el.text if detach_topic_el is not None and detach_topic_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            attach_topic=attach_topic_el.text if attach_topic_el is not None and attach_topic_el.text is not None else None,
            output_topic=output_topic_el.text if output_topic_el is not None and output_topic_el.text is not None else None,
            suppress_child_warning=suppress_child_warning_el.text.lower() == 'true' if suppress_child_warning_el is not None and suppress_child_warning_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim:systems::DetachableJoint",
                        filename="gz-sim-detachable-joint-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('parent_link', self.parent_link)
        _add('child_model', self.child_model)
        _add('child_link', self.child_link)
        _add('detach_topic', self.detach_topic)
        _add('topic', self.topic)
        _add('attach_topic', self.attach_topic)
        _add('output_topic', self.output_topic)
        _add('suppress_child_warning', self.suppress_child_warning)

        return el

    def to_version(self, target_version: str):
        return self
