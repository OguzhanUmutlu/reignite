from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-touchplugin-system", "gz::sim::systems::TouchPlugin")
class TouchPlugin(Plugin):
    def __init__(
            self,
            target: str | None = None,
            time: float | None = None,
            collision: list[str] | str | None = None,
            create_contact_sensor_for_collision: bool | None = None,
            namespace: str | None = None,
            enabled: bool | None = None
    ):
        self.target = target
        self.time = time
        self.collision = [collision] if isinstance(collision, str) else (collision or [])
        self.create_contact_sensor_for_collision = create_contact_sensor_for_collision
        self.namespace = namespace
        self.enabled = enabled

        super().__init__(
            sdf_version=None,
            filename="gz-sim-touchplugin-system",
            name="gz::sim::systems::TouchPlugin"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        tar_el = el.find("target")
        t_el = el.find("time")
        c_els = el.findall("collision")
        cc_el = el.find("create_contact_sensor_for_collision")
        ns_el = el.find("namespace")
        en_el = el.find("enabled")

        return cls(
            target=tar_el.text if tar_el is not None else None,
            time=float(t_el.text) if t_el is not None and t_el.text is not None else None,
            collision=[c.text for c in c_els if c.text is not None] if c_els else None,
            create_contact_sensor_for_collision=cc_el.text.lower() == 'true' if cc_el is not None and cc_el.text is not None else None,
            namespace=ns_el.text if ns_el is not None else None,
            enabled=en_el.text.lower() == 'true' if en_el is not None and en_el.text is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::TouchPlugin", filename="gz-sim-touchplugin-system")
        if self.collision:
            for c in self.collision:
                child = ET.Element("collision")
                child.text = str(c)
                el.append(child)

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add("target", self.target)
        _add("time", self.time)
        _add("create_contact_sensor_for_collision", self.create_contact_sensor_for_collision)
        _add("namespace", self.namespace)
        _add("enabled", self.enabled)
        return el

    def to_version(self, target_version: str):
        return self
