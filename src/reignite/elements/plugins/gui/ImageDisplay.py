from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("WorldControl", "Camera")
class ImageDisplayPlugin(Plugin):
    def __init__(
            self,
            topic: str = None,
            topic_picker: bool = True,
            show_depth_flip: bool = True,
            name = "Camera",
            **gui_kwargs
    ):
        self.topic = topic
        self.topic_picker = topic_picker
        self.show_depth_flip = show_depth_flip
        self.name = name
        super().__init__(
            sdf_version=None,
            filename="ImageDisplay",
            name=name,
        )
        gui_params = {'state': 'docked'}
        gui_params.update(gui_kwargs)
        self.gz_gui = GzGui(**gui_params)

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        gui_el = el.find("gz-gui")
        gui_kwargs = {}
        if gui_el is not None:
            gui = GzGui._from_sdf(gui_el, version)
            for k in ["anchors", "anchor", "state", "z", "height", "width", "resizable", "show_title_bar", "delete_later", "title"]:
                if hasattr(gui, k) and getattr(gui, k) is not None:
                    gui_kwargs[k] = getattr(gui, k)

        topic_el = el.find('topic')
        topic_picker_el = el.find('topic_picker')
        show_depth_flip_el = el.find('show_depth_flip')
        name = el.get('name')

        return cls(
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            topic_picker=topic_picker_el.text.lower() == 'true' if topic_picker_el is not None and topic_picker_el.text is not None else None,
            show_depth_flip=show_depth_flip_el.text.lower() == 'true' if show_depth_flip_el is not None and show_depth_flip_el.text is not None else None,
            name=name if name is not None else "ImageDisplay",
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="WorldControl")
        
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
        _add('show_depth_flip', self.show_depth_flip)
        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        return el

    def to_version(self, target_version: str):
        return self
