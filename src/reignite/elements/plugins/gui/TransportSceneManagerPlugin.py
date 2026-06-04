from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("TransportSceneManager", "TransportSceneManager")
class TransportSceneManagerPlugin(Plugin):
    def __init__(
            self,
            deletion_topic: str | None = None,
            pose_topic: str | None = None,
            scene_topic: str | None = None,
            service: str | None = None,
            name: str = "TransportSceneManager",
            **gui_kwargs
    ):
        self.deletion_topic = deletion_topic
        self.pose_topic = pose_topic
        self.scene_topic = scene_topic
        self.service = service
        self.name = name
        self.gz_gui = GzGui(**gui_kwargs)
        
        super().__init__(
            sdf_version=None,
            filename="TransportSceneManager",
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
        deletion_topic_el = el.find("deletion_topic")
        pose_topic_el = el.find("pose_topic")
        scene_topic_el = el.find("scene_topic")
        service_el = el.find("service")

        return cls(
            name=name if name is not None else "TransportSceneManager",
            deletion_topic=deletion_topic_el.text if deletion_topic_el is not None and deletion_topic_el.text is not None else None,
            pose_topic=pose_topic_el.text if pose_topic_el is not None and pose_topic_el.text is not None else None,
            scene_topic=scene_topic_el.text if scene_topic_el is not None and scene_topic_el.text is not None else None,
            service=service_el.text if service_el is not None and service_el.text is not None else None,
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="TransportSceneManager")
        
        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                child.text = str(v)
                el.append(child)
                
        _add("deletion_topic", self.deletion_topic)
        _add("pose_topic", self.pose_topic)
        _add("scene_topic", self.scene_topic)
        _add("service", self.service)

        return el

    def to_version(self, target_version: str):
        return self
