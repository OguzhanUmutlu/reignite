from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin

@Plugin.register("WorldControl", "World control")
class WorldControlPlugin(Plugin):
    def __init__(self,
                 play_pause: bool | None = True,
                 step: bool | None = True,
                 start_paused: bool | None = False,
                 use_event: bool | None = True,
                 stats_topic: str | None = None,
                 name: str = "World control", 
                 **gui_kwargs
                 ):
        self.play_pause = play_pause
        self.step = step
        self.start_paused = start_paused
        self.use_event = use_event
        self.stats_topic = stats_topic
        self.name = name

        gui_params = {
            "show_title_bar": False, "resizable": False, "height": 72.0, "z": 1.0, "state": "floating",
            "anchor": "3D View", "anchors": [
                GzGui.Anchor("left", "left"),
                GzGui.Anchor("bottom", "bottom")
            ]
        }
        gui_params.update(gui_kwargs)
        self.gz_gui = GzGui(**gui_params)
        
        super().__init__(
            sdf_version=None,
            filename="WorldControl",
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
        play_pause_el = el.find("play_pause")
        step_el = el.find("step")
        start_paused_el = el.find("start_paused")
        use_event_el = el.find("use_event")
        stats_topic_el = el.find("stats_topic")

        return cls(
            name=name if name is not None else "World control",
            play_pause=play_pause_el.text.lower() == "true" if play_pause_el is not None and play_pause_el.text is not None else None,
            step=step_el.text.lower() == "true" if step_el is not None and step_el.text is not None else None,
            start_paused=start_paused_el.text.lower() == "true" if start_paused_el is not None and start_paused_el.text is not None else None,
            use_event=use_event_el.text.lower() == "true" if use_event_el is not None and use_event_el.text is not None else None,
            stats_topic=stats_topic_el.text if stats_topic_el is not None and stats_topic_el.text is not None else None,
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="WorldControl")
        
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
                
        _add("play_pause", self.play_pause)
        _add("step", self.step)
        _add("start_paused", self.start_paused)
        _add("use_event", self.use_event)
        _add("stats_topic", self.stats_topic)

        return el

    def to_version(self, target_version: str):
        return self
