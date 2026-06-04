from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("MarkerManager", "MarkerManager")
class MarkerManagerPlugin(Plugin):
    def __init__(
            self,
            stats_topic: str | None = None,
            topic_name: str | None = None,
            warn_on_action_failure: bool | None = None,
            name: str = "MarkerManager",
            **gui_kwargs
    ):
        self.stats_topic = stats_topic
        self.topic_name = topic_name
        self.warn_on_action_failure = warn_on_action_failure
        self.name = name
        self.gz_gui = GzGui(**gui_kwargs)
        
        super().__init__(
            sdf_version=None,
            filename="MarkerManager",
            name=name
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        gui_el = el.find("gz-gui")
        gui_kwargs = {}
        if gui_el is not None:
            gui = GzGui._from_sdf(gui_el, version)
            for k in ["anchors", "anchor", "state", "z", "height", "width", "resizable", "show_title_bar", "delete_later", "title"]:
                if hasattr(gui, k) and getattr(gui, k) is not None:
                    gui_kwargs[k] = getattr(gui, k)

        name = el.get("name")
        stats_topic_el = el.find("stats_topic")
        topic_name_el = el.find("topic_name")
        warn_on_action_failure_el = el.find("warn_on_action_failure")

        return cls(
            name=name if name is not None else "MarkerManager",
            stats_topic=stats_topic_el.text if stats_topic_el is not None and stats_topic_el.text is not None else None,
            topic_name=topic_name_el.text if topic_name_el is not None and topic_name_el.text is not None else None,
            warn_on_action_failure=warn_on_action_failure_el.text.lower() == "true" if warn_on_action_failure_el is not None and warn_on_action_failure_el.text is not None else None,
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="MarkerManager")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add("stats_topic", self.stats_topic)
        _add("topic_name", self.topic_name)
        _add("warn_on_action_failure", self.warn_on_action_failure)
        
        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        return el

    def to_version(self, target_version: str):
        return self
