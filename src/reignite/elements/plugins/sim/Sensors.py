from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-sensors-system", "gz::sim::systems::Sensors")
class SensorsPlugin(Plugin):
    class GlobalIllumination(BaseModel):
        def __init__(
                self,
                type: str | None = "vct",
                enabled: bool | None = None,
                resolution: list[int] | str | None = None,
                octant_count: list[int] | str | None = None,
                bounce_count: int | None = None,
                high_quality: bool | None = None,
                anisotropic: bool | None = None,
                thin_wall_counter: float | None = None,
                conserve_memory: bool | None = None,
                debug_vis_mode: str | None = None
        ):
            super().__init__(sdf_version=None)
            self.type = type
            self.enabled = enabled
            self.resolution = resolution
            self.octant_count = octant_count
            self.bounce_count = bounce_count
            self.high_quality = high_quality
            self.anisotropic = anisotropic
            self.thin_wall_counter = thin_wall_counter
            self.conserve_memory = conserve_memory
            self.debug_vis_mode = debug_vis_mode

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            type_attr = el.get("type", "vct")

            en_el = el.find("enabled")
            res_el = el.find("resolution")
            oc_el = el.find("octant_count")
            bc_el = el.find("bounce_count")
            hq_el = el.find("high_quality")
            an_el = el.find("anisotropic")
            twc_el = el.find("thin_wall_counter")
            cm_el = el.find("conserve_memory")
            dvm_el = el.find("debug_vis_mode")

            res_val = None
            if res_el is not None and res_el.text:
                parts = res_el.text.split()
                if len(parts) == 3:
                    res_val = [int(p) for p in parts]
                else:
                    res_val = res_el.text

            oc_val = None
            if oc_el is not None and oc_el.text:
                parts = oc_el.text.split()
                if len(parts) == 3:
                    oc_val = [int(p) for p in parts]
                else:
                    oc_val = oc_el.text

            return cls(
                type=type_attr,
                enabled=en_el.text.lower() == 'true' if en_el is not None and en_el.text is not None else None,
                resolution=res_val,
                octant_count=oc_val,
                bounce_count=int(bc_el.text) if bc_el is not None and bc_el.text is not None else None,
                high_quality=hq_el.text.lower() == 'true' if hq_el is not None and hq_el.text is not None else None,
                anisotropic=an_el.text.lower() == 'true' if an_el is not None and an_el.text is not None else None,
                thin_wall_counter=float(twc_el.text) if twc_el is not None and twc_el.text is not None else None,
                conserve_memory=cm_el.text.lower() == 'true' if cm_el is not None and cm_el.text is not None else None,
                debug_vis_mode=dvm_el.text if dvm_el is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("global_illumination")
            if self.type is not None:
                e.set("type", str(self.type))

            def _add(k, v):
                if v is not None:
                    child = ET.Element(k)
                    if isinstance(v, bool):
                        child.text = "true" if v else "false"
                    elif isinstance(v, (list, tuple)):
                        child.text = " ".join(map(str, v))
                    else:
                        child.text = str(v)
                    e.append(child)

            _add("enabled", self.enabled)
            _add("resolution", self.resolution)
            _add("octant_count", self.octant_count)
            _add("bounce_count", self.bounce_count)
            _add("high_quality", self.high_quality)
            _add("anisotropic", self.anisotropic)
            _add("thin_wall_counter", self.thin_wall_counter)
            _add("conserve_memory", self.conserve_memory)
            _add("debug_vis_mode", self.debug_vis_mode)

            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            render_engine: str | None = None,
            render_engine_api_backend: str | None = None,
            disable_on_drained_battery: bool | None = None,
            background_color: list[float] | str | None = None,
            ambient_light: list[float] | str | None = None,
            global_illumination: GlobalIllumination | None = None,
    ):
        self.render_engine = render_engine
        self.render_engine_api_backend = render_engine_api_backend
        self.disable_on_drained_battery = disable_on_drained_battery
        self.background_color = background_color
        self.ambient_light = ambient_light
        self.global_illumination = global_illumination

        super().__init__(
            sdf_version=None,
            filename="gz-sim-sensors-system",
            name="gz::sim::systems::Sensors"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        re_el = el.find("render_engine")
        reab_el = el.find("render_engine_api_backend")
        dod_el = el.find("disable_on_drained_battery")
        bg_el = el.find("background_color")
        al_el = el.find("ambient_light")
        gi_el = el.find("global_illumination")

        bg_val = None
        if bg_el is not None and bg_el.text:
            parts = bg_el.text.split()
            if len(parts) in (3, 4):
                bg_val = [float(p) for p in parts]
            else:
                bg_val = bg_el.text

        al_val = None
        if al_el is not None and al_el.text:
            parts = al_el.text.split()
            if len(parts) in (3, 4):
                al_val = [float(p) for p in parts]
            else:
                al_val = al_el.text

        return cls(
            render_engine=re_el.text if re_el is not None else None,
            render_engine_api_backend=reab_el.text if reab_el is not None else None,
            disable_on_drained_battery=dod_el.text.lower() == 'true' if dod_el is not None and dod_el.text is not None else None,
            background_color=bg_val,
            ambient_light=al_val,
            global_illumination=cls.GlobalIllumination._from_sdf(gi_el, version) if gi_el is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::Sensors", filename="gz-sim-sensors-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                elif isinstance(v, (list, tuple)):
                    child.text = " ".join(map(str, v))
                else:
                    child.text = str(v)
                el.append(child)

        _add("render_engine", self.render_engine)
        _add("render_engine_api_backend", self.render_engine_api_backend)
        _add("disable_on_drained_battery", self.disable_on_drained_battery)
        _add("background_color", self.background_color)
        _add("ambient_light", self.ambient_light)
        if self.global_illumination is not None:
            el.append(self.global_illumination.to_sdf(version))

        return el

    def to_version(self, target_version: str):
        if self.global_illumination is not None:
            self.global_illumination.to_version(target_version)
        return self
