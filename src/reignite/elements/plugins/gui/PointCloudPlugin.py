from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("PointCloud", "PointCloud")
class PointCloudPlugin(Plugin):
    def __init__(
            self,
            float_v_topic: str | None = None,
            point_cloud_topic: str | None = None,
            name: str = "PointCloud",
            **gui_kwargs
    ):
        self.float_v_topic = float_v_topic
        self.point_cloud_topic = point_cloud_topic
        self.name = name
        super().__init__(
            sdf_version=None,
            filename="PointCloud",
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

        float_v_topic_el = el.find('float_v_topic')
        point_cloud_topic_el = el.find('point_cloud_topic')
        name = el.get('name')

        return cls(
            float_v_topic=float_v_topic_el.text if float_v_topic_el is not None and float_v_topic_el.text is not None else None,
            point_cloud_topic=point_cloud_topic_el.text if point_cloud_topic_el is not None and point_cloud_topic_el.text is not None else None,
            name=name if name is not None else "PointCloud",
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="PointCloud")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('float_v_topic', self.float_v_topic)
        _add('point_cloud_topic', self.point_cloud_topic)
        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        return el

    def to_version(self, target_version: str):
        return self
