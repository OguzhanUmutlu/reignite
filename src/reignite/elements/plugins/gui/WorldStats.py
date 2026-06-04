from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("WorldStats", "World stats")
class WorldStatsPlugin(Plugin):
    def __init__(self,
                 sim_time: bool | None = True,
                 real_time: bool | None = True,
                 real_time_factor: bool | None = True,
                 iterations: bool | None = True,
                 topic: str | None = None,
                 name: str = "World stats", 
                 **gui_kwargs
                 ):
        self.sim_time = sim_time
        self.real_time = real_time
        self.real_time_factor = real_time_factor
        self.iterations = iterations
        self.topic = topic
        self.name = name

        gui_params = {
            "title": "World stats", "show_title_bar": False, "resizable": False, 
            "height": 110.0, "width": 290.0, "z": 1.0, "state": "floating", 
            "anchor": "3D View", "anchors": [
                GzGui.Anchor("right", "right"),
                GzGui.Anchor("bottom", "bottom")
            ]
        }
        gui_params.update(gui_kwargs)
        self.gz_gui = GzGui(**gui_params)
        
        super().__init__(
            sdf_version=None,
            filename="WorldStats",
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
        sim_time_el = el.find("sim_time")
        real_time_el = el.find("real_time")
        real_time_factor_el = el.find("real_time_factor")
        iterations_el = el.find("iterations")
        topic_el = el.find("topic")

        return cls(
            name=name if name is not None else "World stats",
            sim_time=sim_time_el.text.lower() == "true" if sim_time_el is not None and sim_time_el.text is not None else None,
            real_time=real_time_el.text.lower() == "true" if real_time_el is not None and real_time_el.text is not None else None,
            real_time_factor=real_time_factor_el.text.lower() == "true" if real_time_factor_el is not None and real_time_factor_el.text is not None else None,
            iterations=iterations_el.text.lower() == "true" if iterations_el is not None and iterations_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="WorldStats")
        
        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add("sim_time", self.sim_time)
        _add("real_time", self.real_time)
        _add("real_time_factor", self.real_time_factor)
        _add("iterations", self.iterations)
        _add("topic", self.topic)

        return el

    def to_version(self, target_version: str):
        return self
