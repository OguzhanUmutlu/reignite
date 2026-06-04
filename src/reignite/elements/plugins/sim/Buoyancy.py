from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-buoyancy-system", "gz::sim::systems::Buoyancy")
class BuoyancyPlugin(Plugin):
    class DensityChange(BaseModel):
        def __init__(self, above_depth: float | None = None, density: float | None = None):
            super().__init__(sdf_version=None)
            self.above_depth = above_depth
            self.density = density

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            above_depth_el = el.find("above_depth")
            density_el = el.find("density")
            return cls(
                above_depth=float(above_depth_el.text) if above_depth_el is not None and above_depth_el.text is not None else None,
                density=float(density_el.text) if density_el is not None and density_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("density_change")
            if self.above_depth is not None:
                child = ET.Element("above_depth")
                child.text = str(self.above_depth)
                e.append(child)
            if self.density is not None:
                child = ET.Element("density")
                child.text = str(self.density)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class GradedBuoyancy(BaseModel):
        def __init__(self, default_density: float | None = None,
                     density_changes: list["BuoyancyPlugin.DensityChange"] | None = None):
            super().__init__(sdf_version=None)
            self.default_density = default_density
            self.density_changes = density_changes or []

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            dd_el = el.find("default_density")
            dc_els = el.findall("density_change")
            return cls(
                default_density=float(dd_el.text) if dd_el is not None and dd_el.text is not None else None,
                density_changes=[BuoyancyPlugin.DensityChange._from_sdf(dc, version) for dc in dc_els] if dc_els else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("graded_buoyancy")
            if self.default_density is not None:
                child = ET.Element("default_density")
                child.text = str(self.default_density)
                e.append(child)
            if self.density_changes:
                for dc in self.density_changes:
                    e.append(dc.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            if self.density_changes:
                for dc in self.density_changes:
                    dc.to_version(target_version)
            return self

    def __init__(
            self,
            uniform_fluid_density: float | None = None,
            graded_buoyancy: GradedBuoyancy | None = None,
            enable: str | list[str] | None = None
    ):
        self.uniform_fluid_density = uniform_fluid_density
        self.graded_buoyancy = graded_buoyancy
        self.enable = [enable] if isinstance(enable, str) else (enable or [])

        super().__init__(
            sdf_version=None,
            filename="gz-sim-buoyancy-system",
            name="gz::sim::systems::Buoyancy",
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        ufd_el = el.find("uniform_fluid_density")
        gb_el = el.find("graded_buoyancy")
        en_els = el.findall("enable")

        return cls(
            uniform_fluid_density=float(ufd_el.text) if ufd_el is not None and ufd_el.text is not None else None,
            graded_buoyancy=cls.GradedBuoyancy._from_sdf(gb_el, version) if gb_el is not None else None,
            enable=[e.text for e in en_els if e.text is not None] if en_els else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::Buoyancy", filename="gz-sim-buoyancy-system")
        if self.uniform_fluid_density is not None:
            child = ET.Element("uniform_fluid_density")
            child.text = str(self.uniform_fluid_density)
            el.append(child)
        if self.graded_buoyancy is not None:
            el.append(self.graded_buoyancy.to_sdf(version))
        if self.enable:
            for e in self.enable:
                child = ET.Element("enable")
                child.text = str(e)
                el.append(child)
        return el

    def to_version(self, target_version: str):
        if self.graded_buoyancy is not None:
            self.graded_buoyancy.to_version(target_version)
        return self
