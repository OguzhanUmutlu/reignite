from __future__ import annotations

from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-led-plugin-system", "gz::sim::systems::LedPlugin")
class LedPlugin(Plugin):
    class DefaultState(BaseModel):
        def __init__(self, color: list[float] | str | None = None, intensity: float | None = None):
            super().__init__(sdf_version=None)
            self.color = color
            self.intensity = intensity

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            c_el = el.find("color")
            i_el = el.find("intensity")
            color_val = None
            if c_el is not None and c_el.text:
                parts = c_el.text.split()
                if len(parts) == 3 or len(parts) == 4:
                    color_val = [float(p) for p in parts]
                else:
                    color_val = c_el.text
            return cls(
                color=color_val,
                intensity=float(i_el.text) if i_el is not None and i_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("default_state")
            if self.color is not None:
                child = ET.Element("color")
                child.text = " ".join(map(str, self.color)) if isinstance(self.color, list) else str(self.color)
                e.append(child)
            if self.intensity is not None:
                child = ET.Element("intensity")
                child.text = str(self.intensity)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class Led(BaseModel):
        def __init__(
                self,
                name: str,
                visual_name: str | None = None,
                light_name: str | None = None,
                default_state: "LedPlugin.DefaultState | None" = None
        ):
            super().__init__(sdf_version=None)
            self.name = name
            self.visual_name = visual_name
            self.light_name = light_name
            self.default_state = default_state

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            n_el = el.find("name")
            vn_el = el.find("visual_name")
            ln_el = el.find("light_name")
            ds_el = el.find("default_state")
            return cls(
                name=n_el.text if n_el is not None and n_el.text is not None else "",
                visual_name=vn_el.text if vn_el is not None else None,
                light_name=ln_el.text if ln_el is not None else None,
                default_state=LedPlugin.DefaultState._from_sdf(ds_el, version) if ds_el is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("led")
            child = ET.Element("name")
            child.text = str(self.name)
            e.append(child)
            if self.visual_name is not None:
                child = ET.Element("visual_name")
                child.text = str(self.visual_name)
                e.append(child)
            if self.light_name is not None:
                child = ET.Element("light_name")
                child.text = str(self.light_name)
                e.append(child)
            if self.default_state is not None:
                e.append(self.default_state.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            if self.default_state is not None:
                self.default_state.to_version(target_version)
            return self

    class ActiveLeds(BaseModel):
        def __init__(self, leds: list[str] | None = None):
            super().__init__(sdf_version=None)
            self.leds = leds or []

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            led_els = el.findall("led")
            return cls(leds=[e.text for e in led_els if e.text is not None] if led_els else None)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("active_leds")
            if self.leds:
                for l in self.leds:
                    child = ET.Element("led")
                    child.text = str(l)
                    e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class Step(BaseModel):
        def __init__(
                self,
                always_on: bool | None = None,
                color: list[float] | str | None = None,
                duration: float | None = None,
                intensity: float | None = None
        ):
            super().__init__(sdf_version=None)
            self.always_on = always_on
            self.color = color
            self.duration = duration
            self.intensity = intensity

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            ao_el = el.find("always_on")
            c_el = el.find("color")
            d_el = el.find("duration")
            i_el = el.find("intensity")
            color_val = None
            if c_el is not None and c_el.text:
                parts = c_el.text.split()
                if len(parts) in (3, 4):
                    color_val = [float(p) for p in parts]
                else:
                    color_val = c_el.text
            return cls(
                always_on=ao_el.text.lower() == 'true' if ao_el is not None and ao_el.text is not None else None,
                color=color_val,
                duration=float(d_el.text) if d_el is not None and d_el.text is not None else None,
                intensity=float(i_el.text) if i_el is not None and i_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("step")
            if self.always_on is not None:
                child = ET.Element("always_on")
                child.text = "true" if self.always_on else "false"
                e.append(child)
            if self.color is not None:
                child = ET.Element("color")
                child.text = " ".join(map(str, self.color)) if isinstance(self.color, list) else str(self.color)
                e.append(child)
            if self.duration is not None:
                child = ET.Element("duration")
                child.text = str(self.duration)
                e.append(child)
            if self.intensity is not None:
                child = ET.Element("intensity")
                child.text = str(self.intensity)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class Mode(BaseModel):
        def __init__(
                self,
                name: str,
                active_leds: "LedPlugin.ActiveLeds | list[str] | None" = None,
                steps: list["LedPlugin.Step"] | None = None
        ):
            super().__init__(sdf_version=None)
            self.name = name
            if isinstance(active_leds, list):
                active_leds = LedPlugin.ActiveLeds(active_leds)
            self.active_leds = active_leds
            self.steps = steps or []

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            n_el = el.find("name")
            al_el = el.find("active_leds")
            st_els = el.findall("step")
            return cls(
                name=n_el.text if n_el is not None and n_el.text is not None else "",
                active_leds=LedPlugin.ActiveLeds._from_sdf(al_el, version) if al_el is not None else None,
                steps=[LedPlugin.Step._from_sdf(s, version) for s in st_els] if st_els else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("mode")
            child = ET.Element("name")
            child.text = str(self.name)
            e.append(child)
            if self.active_leds is not None:
                e.append(self.active_leds.to_sdf(version))
            if self.steps:
                for s in self.steps:
                    e.append(s.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            if self.active_leds is not None:
                self.active_leds.to_version(target_version)
            if self.steps:
                for s in self.steps:
                    s.to_version(target_version)
            return self

    def __init__(
            self,
            leds: list[Led] | Led | None = None,
            modes: list[Mode] | Mode | None = None,
            led_group_name: str | None = None,
            startup_mode: str | None = None
    ):
        self.leds = [leds] if isinstance(leds, LedPlugin.Led) else (leds or [])
        self.modes = [modes] if isinstance(modes, LedPlugin.Mode) else (modes or [])
        self.led_group_name = led_group_name
        self.startup_mode = startup_mode

        super().__init__(
            sdf_version=None,
            filename="gz-sim-led-plugin-system",
            name="gz::sim::systems::LedPlugin"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        l_els = el.findall("led")
        m_els = el.findall("mode")
        lgn_el = el.find("led_group_name")
        sm_el = el.find("startup_mode")
        
        return cls(
            leds=[cls.Led._from_sdf(l, version) for l in l_els],
            modes=[cls.Mode._from_sdf(m, version) for m in m_els],
            led_group_name=lgn_el.text if lgn_el is not None else None,
            startup_mode=sm_el.text if sm_el is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::LedPlugin", filename="gz-sim-led-plugin-system")
        if self.leds:
            for l in self.leds:
                el.append(l.to_sdf(version))
        if self.modes:
            for m in self.modes:
                el.append(m.to_sdf(version))
        if self.led_group_name is not None:
            child = ET.Element("led_group_name")
            child.text = str(self.led_group_name)
            el.append(child)
        if self.startup_mode is not None:
            child = ET.Element("startup_mode")
            child.text = str(self.startup_mode)
            el.append(child)
        return el

    def to_version(self, target_version: str):
        if self.leds:
            for l in self.leds:
                l.to_version(target_version)
        if self.modes:
            for m in self.modes:
                m.to_version(target_version)
        return self
