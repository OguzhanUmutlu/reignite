from xml.etree import ElementTree as ET

from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("NavSatMap", "NavSatMap")
class NavSatMapPlugin(Plugin):
    def __init__(
            self,
            topic: str | None = None,
            topic_picker: bool | None = None,
            name: str = "NavSatMap",
            **gui_kwargs
    ):
        self.topic = topic
        self.topic_picker = topic_picker
        self.name = name
        super().__init__(
            sdf_version=None,
            filename="NavSatMap",
            name=name,
        )
        self.gz_gui = GzGui(**gui_kwargs)

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        gui_el = el.find("gz-gui")
        gui_kwargs = {}
        if gui_el is not None:
            gui = GzGui._from_sdf(gui_el, version)
            for k in ["anchors", "anchor", "state", "z", "height", "width", "resizable", "show_title_bar",
                      "delete_later", "title"]:
                if hasattr(gui, k) and getattr(gui, k) is not None:
                    gui_kwargs[k] = getattr(gui, k)

        topic_el = el.find('topic')
        topic_picker_el = el.find('topic_picker')
        name = el.get('name')

        return cls(
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            topic_picker=topic_picker_el.text.lower() == 'true' if topic_picker_el is not None and topic_picker_el.text is not None else None,
            name=name if name is not None else "NavSatMap",
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="NavSatMap")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('topic', self.topic)
        _add('topic_picker', self.topic_picker)
        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))

        return el

    def to_version(self, target_version: str):
        return self
