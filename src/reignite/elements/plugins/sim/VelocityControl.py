from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-velocity-control-system", "gz::sim::systems::VelocityControl")
class VelocityControlPlugin(Plugin):
    def __init__(
            self,
            initial_linear: list[float] | str | None = None,
            initial_angular: list[float] | str | None = None,
            topic: str | None = None,
            link_name: str | list[str] | None = None
    ):
        self.initial_linear = initial_linear
        self.initial_angular = initial_angular
        self.topic = topic
        self.link_name = [link_name] if isinstance(link_name, str) else (link_name or [])

        super().__init__(
            sdf_version=None,
            filename="gz-sim-velocity-control-system",
            name="gz::sim::systems::VelocityControl"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        il_el = el.find("initial_linear")
        ia_el = el.find("initial_angular")
        t_el = el.find("topic")
        ln_els = el.findall("link_name")

        il_val = None
        if il_el is not None and il_el.text:
            parts = il_el.text.split()
            if len(parts) == 3:
                il_val = [float(p) for p in parts]
            else:
                il_val = il_el.text

        ia_val = None
        if ia_el is not None and ia_el.text:
            parts = ia_el.text.split()
            if len(parts) == 3:
                ia_val = [float(p) for p in parts]
            else:
                ia_val = ia_el.text

        return cls(
            initial_linear=il_val,
            initial_angular=ia_val,
            topic=t_el.text if t_el is not None else None,
            link_name=[ln.text for ln in ln_els if ln.text is not None] if ln_els else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::VelocityControl", filename="gz-sim-velocity-control-system")
        if self.initial_linear is not None:
            child = ET.Element("initial_linear")
            child.text = " ".join(map(str, self.initial_linear)) if isinstance(self.initial_linear, list) else str(self.initial_linear)
            el.append(child)
        if self.initial_angular is not None:
            child = ET.Element("initial_angular")
            child.text = " ".join(map(str, self.initial_angular)) if isinstance(self.initial_angular, list) else str(self.initial_angular)
            el.append(child)
        if self.topic is not None:
            child = ET.Element("topic")
            child.text = str(self.topic)
            el.append(child)
        if self.link_name:
            for ln in self.link_name:
                child = ET.Element("link_name")
                child.text = str(ln)
                el.append(child)
        return el

    def to_version(self, target_version: str):
        return self
