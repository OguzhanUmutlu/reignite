from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-wind-effects-system", "gz::sim::systems::WindEffects")
class WindEffectsPlugin(Plugin):
    class Sin(BaseModel):
        def __init__(self, amplitude: float | None = None, amplitude_percent: float | None = None,
                     period: float | None = None):
            super().__init__(sdf_version=None)
            self.amplitude = amplitude
            self.amplitude_percent = amplitude_percent
            self.period = period

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            amp_el = el.find("amplitude")
            ampp_el = el.find("amplitude_percent")
            per_el = el.find("period")
            return cls(
                amplitude=float(amp_el.text) if amp_el is not None and amp_el.text is not None else None,
                amplitude_percent=float(ampp_el.text) if ampp_el is not None and ampp_el.text is not None else None,
                period=float(per_el.text) if per_el is not None and per_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("sin")
            if self.amplitude is not None:
                child = ET.Element("amplitude")
                child.text = str(self.amplitude)
                e.append(child)
            if self.amplitude_percent is not None:
                child = ET.Element("amplitude_percent")
                child.text = str(self.amplitude_percent)
                e.append(child)
            if self.period is not None:
                child = ET.Element("period")
                child.text = str(self.period)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class Magnitude(BaseModel):
        def __init__(self, time_for_rise: float | None = None, sin: "WindEffectsPlugin.Sin | None" = None,
                     noise: ET.Element | None = None):
            super().__init__(sdf_version=None)
            self.time_for_rise = time_for_rise
            self.sin = sin
            self.noise = noise

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            tfr_el = el.find("time_for_rise")
            sin_el = el.find("sin")
            noise_el = el.find("noise")
            return cls(
                time_for_rise=float(tfr_el.text) if tfr_el is not None and tfr_el.text is not None else None,
                sin=WindEffectsPlugin.Sin._from_sdf(sin_el, version) if sin_el is not None else None,
                noise=noise_el
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("magnitude")
            if self.time_for_rise is not None:
                child = ET.Element("time_for_rise")
                child.text = str(self.time_for_rise)
                e.append(child)
            if self.sin is not None:
                e.append(self.sin.to_sdf(version))
            if self.noise is not None:
                e.append(self.noise)
            return e

        def to_version(self, target_version: str):
            if self.sin is not None:
                self.sin.to_version(target_version)
            return self

    class Direction(BaseModel):
        def __init__(self, time_for_rise: float | None = None, sin: "WindEffectsPlugin.Sin | None" = None,
                     noise: ET.Element | None = None):
            super().__init__(sdf_version=None)
            self.time_for_rise = time_for_rise
            self.sin = sin
            self.noise = noise

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            tfr_el = el.find("time_for_rise")
            sin_el = el.find("sin")
            noise_el = el.find("noise")
            return cls(
                time_for_rise=float(tfr_el.text) if tfr_el is not None and tfr_el.text is not None else None,
                sin=WindEffectsPlugin.Sin._from_sdf(sin_el, version) if sin_el is not None else None,
                noise=noise_el
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("direction")
            if self.time_for_rise is not None:
                child = ET.Element("time_for_rise")
                child.text = str(self.time_for_rise)
                e.append(child)
            if self.sin is not None:
                e.append(self.sin.to_sdf(version))
            if self.noise is not None:
                e.append(self.noise)
            return e

        def to_version(self, target_version: str):
            if self.sin is not None:
                self.sin.to_version(target_version)
            return self

    class Horizontal(BaseModel):
        def __init__(self, magnitude: "WindEffectsPlugin.Magnitude | None" = None,
                     direction: "WindEffectsPlugin.Direction | None" = None):
            super().__init__(sdf_version=None)
            self.magnitude = magnitude
            self.direction = direction

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            mag_el = el.find("magnitude")
            dir_el = el.find("direction")
            return cls(
                magnitude=WindEffectsPlugin.Magnitude._from_sdf(mag_el, version) if mag_el is not None else None,
                direction=WindEffectsPlugin.Direction._from_sdf(dir_el, version) if dir_el is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("horizontal")
            if self.magnitude is not None:
                e.append(self.magnitude.to_sdf(version))
            if self.direction is not None:
                e.append(self.direction.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            if self.magnitude is not None:
                self.magnitude.to_version(target_version)
            if self.direction is not None:
                self.direction.to_version(target_version)
            return self

    class Vertical(BaseModel):
        def __init__(self, time_for_rise: float | None = None, noise: ET.Element | None = None):
            super().__init__(sdf_version=None)
            self.time_for_rise = time_for_rise
            self.noise = noise

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            tfr_el = el.find("time_for_rise")
            noise_el = el.find("noise")
            return cls(
                time_for_rise=float(tfr_el.text) if tfr_el is not None and tfr_el.text is not None else None,
                noise=noise_el
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("vertical")
            if self.time_for_rise is not None:
                child = ET.Element("time_for_rise")
                child.text = str(self.time_for_rise)
                e.append(child)
            if self.noise is not None:
                e.append(self.noise)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            horizontal: Horizontal | None = None,
            vertical: Vertical | None = None,
            force_approximation_scaling_factor: ET.Element | None = None
    ):
        self.horizontal = horizontal
        self.vertical = vertical
        self.force_approximation_scaling_factor = force_approximation_scaling_factor

        super().__init__(
            sdf_version=None,
            filename="gz-sim-wind-effects-system",
            name="gz::sim::systems::WindEffects"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        h_el = el.find("horizontal")
        v_el = el.find("vertical")
        fasf_el = el.find("force_approximation_scaling_factor")

        return cls(
            horizontal=cls.Horizontal._from_sdf(h_el, version) if h_el is not None else None,
            vertical=cls.Vertical._from_sdf(v_el, version) if v_el is not None else None,
            force_approximation_scaling_factor=fasf_el
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::WindEffects", filename="gz-sim-wind-effects-system")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        if self.force_approximation_scaling_factor is not None:
            el.append(self.force_approximation_scaling_factor)
        return el

    def to_version(self, target_version: str):
        if self.horizontal is not None:
            self.horizontal.to_version(target_version)
        if self.vertical is not None:
            self.vertical.to_version(target_version)
        return self
