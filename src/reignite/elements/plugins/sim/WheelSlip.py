from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-wheel-slip-system", "gz::sim::systems::WheelSlip")
class WheelSlipPlugin(Plugin):
    class Wheel(BaseModel):
        def __init__(
                self,
                link_name: str | None = None,
                slip_compliance_lateral: float | None = None,
                slip_compliance_longitudinal: float | None = None,
                wheel_normal_force: float | None = None,
                wheel_radius: float | None = None
        ):
            super().__init__(sdf_version=None)
            self.link_name = link_name
            self.slip_compliance_lateral = slip_compliance_lateral
            self.slip_compliance_longitudinal = slip_compliance_longitudinal
            self.wheel_normal_force = wheel_normal_force
            self.wheel_radius = wheel_radius

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            ln_attr = el.get("link_name")
            scl_attr = el.get("slip_compliance_lateral")
            sclong_attr = el.get("slip_compliance_longitudinal")
            wnf_attr = el.get("wheel_normal_force")
            wr_attr = el.get("wheel_radius")
            return cls(
                link_name=ln_attr,
                slip_compliance_lateral=float(scl_attr) if scl_attr is not None else None,
                slip_compliance_longitudinal=float(sclong_attr) if sclong_attr is not None else None,
                wheel_normal_force=float(wnf_attr) if wnf_attr is not None else None,
                wheel_radius=float(wr_attr) if wr_attr is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("wheel")
            if self.link_name is not None:
                e.set("link_name", str(self.link_name))
            if self.slip_compliance_lateral is not None:
                e.set("slip_compliance_lateral", str(self.slip_compliance_lateral))
            if self.slip_compliance_longitudinal is not None:
                e.set("slip_compliance_longitudinal", str(self.slip_compliance_longitudinal))
            if self.wheel_normal_force is not None:
                e.set("wheel_normal_force", str(self.wheel_normal_force))
            if self.wheel_radius is not None:
                e.set("wheel_radius", str(self.wheel_radius))
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            wheel: list[Wheel] | Wheel | None = None,
    ):
        self.wheel = [wheel] if isinstance(wheel, WheelSlipPlugin.Wheel) else (wheel or [])

        super().__init__(
            sdf_version=None,
            filename="gz-sim-wheel-slip-system",
            name="gz::sim::systems::WheelSlip"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        w_els = el.findall("wheel")
        return cls(
            wheel=[cls.Wheel._from_sdf(w, version) for w in w_els] if w_els else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::WheelSlip", filename="gz-sim-wheel-slip-system")
        if self.wheel:
            for w in self.wheel:
                el.append(w.to_sdf(version))
        return el

    def to_version(self, target_version: str):
        if self.wheel:
            for w in self.wheel:
                w.to_version(target_version)
        return self
