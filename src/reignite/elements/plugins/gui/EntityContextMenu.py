from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("EntityContextMenuPlugin", "Entity context menu")
class EntityContextMenuPlugin(Plugin):
    def __init__(
            self,
            name = "Entity context menu",
            **gui_kwargs
    ):
        self.name = name
        super().__init__(
            sdf_version=None,
            filename="EntityContextMenuPlugin",
            name=name,
        )
        gui_params = {'state': 'floating', 'width': 5.0, 'height': 5.0, 'show_title_bar': False}
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

        name = el.get('name')

        return cls(
            name=name if name is not None else "Entity context menu",
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="EntityContextMenuPlugin")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                

        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        return el

    def to_version(self, target_version: str):
        return self
