from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("Publisher", "Publisher")
class PublisherPlugin(Plugin):
    def __init__(
            self,
            frequency: float | None = None,
            message: str | None = None,
            message_type: str | None = None,
            topic: str | None = None,
            name: str = "Publisher",
            **gui_kwargs
    ):
        self.frequency = frequency
        self.message = message
        self.message_type = message_type
        self.topic = topic
        self.name = name
        super().__init__(
            sdf_version=None,
            filename="Publisher",
            name=name,
        )
        self.gz_gui = GzGui(**gui_kwargs)

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        gui_el = el.find("gz-gui")
        gui_kwargs = {}
        if gui_el is not None:
            gui = GzGui._from_sdf(gui_el, version)
            for k in ["anchors", "anchor", "state", "z", "height", "width", "resizable", "show_title_bar", "delete_later", "title"]:
                if hasattr(gui, k) and getattr(gui, k) is not None:
                    gui_kwargs[k] = getattr(gui, k)

        frequency_el = el.find('frequency')
        message_el = el.find('message')
        message_type_el = el.find('message_type')
        topic_el = el.find('topic')
        name = el.get('name')

        return cls(
            frequency=float(frequency_el.text) if frequency_el is not None and frequency_el.text is not None else None,
            message=message_el.text if message_el is not None and message_el.text is not None else None,
            message_type=message_type_el.text if message_type_el is not None and message_type_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            name=name if name is not None else "Publisher",
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="Publisher")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('frequency', self.frequency)
        _add('message', self.message)
        _add('message_type', self.message_type)
        _add('topic', self.topic)
        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        return el

    def to_version(self, target_version: str):
        return self
