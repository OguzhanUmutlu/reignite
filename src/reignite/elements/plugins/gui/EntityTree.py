from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("EntityTree", "Entity tree")
class EntityTreePlugin(Plugin):
    def __init__(
            self,
            name = "Entity tree",
            **gui_kwargs
    ):
        self.name = name
        super().__init__(
            sdf_version=None,
            filename="EntityTree",
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

        name = el.get('name')

        return cls(
            name=name if name is not None else "Entity tree",
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="EntityTree")

        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        return el

    def to_version(self, target_version: str):
        return self
