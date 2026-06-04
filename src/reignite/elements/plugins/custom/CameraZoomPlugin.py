from xml.etree import ElementTree as ET
from typing import Optional
from ...plugin import Plugin

@Plugin.register("CameraZoomPlugin", "CameraZoomPlugin")
class CameraZoomPlugin(Plugin):
    def __init__(
            self,
            max_zoom: float | None = None,
            slew_rate: float | None = None,
            topic: str | list[str] | None = None,
            **kwargs
    ):
        self.max_zoom = max_zoom
        self.slew_rate = slew_rate
        self.topic = topic
        super().__init__(
            sdf_version=None,
            filename="CameraZoomPlugin",
            name="CameraZoomPlugin",
            **kwargs
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        max_zoom_el = el.find("max_zoom")
        slew_rate_el = el.find("slew_rate")
        topic_els = el.findall("topic")
        
        max_zoom = float(max_zoom_el.text) if max_zoom_el is not None and max_zoom_el.text is not None else None
        slew_rate = float(slew_rate_el.text) if slew_rate_el is not None and slew_rate_el.text is not None else None
        
        if len(topic_els) == 1:
            topic = topic_els[0].text if topic_els[0].text is not None else None
        elif len(topic_els) > 1:
            topic = [t.text for t in topic_els if t.text is not None]
        else:
            topic = None

        return cls(
            max_zoom=max_zoom,
            slew_rate=slew_rate,
            topic=topic
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = super().to_sdf(version)
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add("max_zoom", self.max_zoom)
        _add("slew_rate", self.slew_rate)
        
        if isinstance(self.topic, list):
            for t in self.topic:
                _add("topic", t)
        else:
            _add("topic", self.topic)
            
        return el

    def to_version(self, target_version: str):
        return self
