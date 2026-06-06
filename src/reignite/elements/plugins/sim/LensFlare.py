from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-lens-flare-system", "gz::sim::systems::LensFlare")
class LensFlarePlugin(Plugin):
    def __init__(
            self,
            camera_name: str,
            light_name: str | None = None,
            scale: float = 1.0,
            color: tuple[float, float, float] = (1.4, 1.2, 1.0),
            occlusion_steps: int = 10
    ):
        self.camera_name = camera_name
        self.light_name = light_name
        self.scale = scale
        self.color = color
        self.occlusion_steps = occlusion_steps
        super().__init__(sdf_version=None, filename="gz-sim-lens-flare-system", name="gz::sim::systems::LensFlare")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        camera_name_el = el.find('camera_name')
        light_name_el = el.find('light_name')
        scale_el = el.find('scale')
        color_el = el.find('color')
        occlusion_steps_el = el.find('occlusion_steps')

        def _parse_tuple(el_node):
            if el_node is None or not el_node.text: return None
            parts = el_node.text.split()
            if len(parts) in (3, 4):
                return tuple(float(p) for p in parts)
            return None

        return cls(
            camera_name=camera_name_el.text if camera_name_el is not None and camera_name_el.text is not None else None,
            light_name=light_name_el.text if light_name_el is not None and light_name_el.text is not None else None,
            scale=float(scale_el.text) if scale_el is not None and scale_el.text is not None else None,
            color=_parse_tuple(color_el),
            occlusion_steps=int(
                occlusion_steps_el.text) if occlusion_steps_el is not None and occlusion_steps_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LensFlare",
                        filename="gz-sim-lens-flare-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                elif isinstance(v, tuple):
                    child.text = " ".join(map(str, v))
                else:
                    child.text = str(v)
                el.append(child)

        _add('camera_name', self.camera_name)
        _add('light_name', self.light_name)
