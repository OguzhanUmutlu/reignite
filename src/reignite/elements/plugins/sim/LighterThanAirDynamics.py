from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-lighter-than-air-dynamics-system", "gz::sim::systems::LighterThanAirDynamics")
class LighterThanAirDynamicsPlugin(Plugin):
    def __init__(
            self,
            air_density: float | None = None,
            link_name: str | None = None,
            moment_inviscid_coeff: float | None = None,
            moment_viscous_coeff: float | None = None,
            force_inviscid_coeff: float | None = None,
            force_viscous_coeff: float | None = None,
            eps_v: float | None = None,
            axial_drag_coeff: float | None = None,
    ):
        self.air_density = air_density
        self.link_name = link_name
        self.moment_inviscid_coeff = moment_inviscid_coeff
        self.moment_viscous_coeff = moment_viscous_coeff
        self.force_inviscid_coeff = force_inviscid_coeff
        self.force_viscous_coeff = force_viscous_coeff
        self.eps_v = eps_v
        self.axial_drag_coeff = axial_drag_coeff
        super().__init__(sdf_version=None, filename="gz-sim-lighter-than-air-dynamics-system",
                         name="gz::sim::systems::LighterThanAirDynamics")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        air_density_el = el.find('air_density')
        link_name_el = el.find('link_name')
        moment_inviscid_coeff_el = el.find('moment_inviscid_coeff')
        moment_viscous_coeff_el = el.find('moment_viscous_coeff')
        force_inviscid_coeff_el = el.find('force_inviscid_coeff')
        force_viscous_coeff_el = el.find('force_viscous_coeff')
        eps_v_el = el.find('eps_v')
        axial_drag_coeff_el = el.find('axial_drag_coeff')

        return cls(
            air_density=float(
                air_density_el.text) if air_density_el is not None and air_density_el.text is not None else None,
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            moment_inviscid_coeff=float(
                moment_inviscid_coeff_el.text) if moment_inviscid_coeff_el is not None and moment_inviscid_coeff_el.text is not None else None,
            moment_viscous_coeff=float(
                moment_viscous_coeff_el.text) if moment_viscous_coeff_el is not None and moment_viscous_coeff_el.text is not None else None,
            force_inviscid_coeff=float(
                force_inviscid_coeff_el.text) if force_inviscid_coeff_el is not None and force_inviscid_coeff_el.text is not None else None,
            force_viscous_coeff=float(
                force_viscous_coeff_el.text) if force_viscous_coeff_el is not None and force_viscous_coeff_el.text is not None else None,
            eps_v=float(eps_v_el.text) if eps_v_el is not None and eps_v_el.text is not None else None,
            axial_drag_coeff=float(
                axial_drag_coeff_el.text) if axial_drag_coeff_el is not None and axial_drag_coeff_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::LighterThanAirDynamics",
                        filename="gz-sim-lighter-than-air-dynamics-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('air_density', self.air_density)
        _add('link_name', self.link_name)
        _add('moment_inviscid_coeff', self.moment_inviscid_coeff)
        _add('moment_viscous_coeff', self.moment_viscous_coeff)
        _add('force_inviscid_coeff', self.force_inviscid_coeff)
        _add('force_viscous_coeff', self.force_viscous_coeff)
        _add('eps_v', self.eps_v)
        _add('axial_drag_coeff', self.axial_drag_coeff)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        air_density_el = el.find('air_density')
        link_name_el = el.find('link_name')
        moment_inviscid_coeff_el = el.find('moment_inviscid_coeff')
        moment_viscous_coeff_el = el.find('moment_viscous_coeff')
        force_inviscid_coeff_el = el.find('force_inviscid_coeff')
        force_viscous_coeff_el = el.find('force_viscous_coeff')
        eps_v_el = el.find('eps_v')
        axial_drag_coeff_el = el.find('axial_drag_coeff')

        return cls(
            air_density=float(
                air_density_el.text) if air_density_el is not None and air_density_el.text is not None else None,
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            moment_inviscid_coeff=float(
                moment_inviscid_coeff_el.text) if moment_inviscid_coeff_el is not None and moment_inviscid_coeff_el.text is not None else None,
            moment_viscous_coeff=float(
                moment_viscous_coeff_el.text) if moment_viscous_coeff_el is not None and moment_viscous_coeff_el.text is not None else None,
            force_inviscid_coeff=float(
                force_inviscid_coeff_el.text) if force_inviscid_coeff_el is not None and force_inviscid_coeff_el.text is not None else None,
            force_viscous_coeff=float(
                force_viscous_coeff_el.text) if force_viscous_coeff_el is not None and force_viscous_coeff_el.text is not None else None,
            eps_v=float(eps_v_el.text) if eps_v_el is not None and eps_v_el.text is not None else None,
            axial_drag_coeff=float(
                axial_drag_coeff_el.text) if axial_drag_coeff_el is not None and axial_drag_coeff_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::LighterThanAirDynamics",
                        filename="gz-sim-lighter-than-air-dynamics-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('air_density', self.air_density)
        _add('link_name', self.link_name)
        _add('moment_inviscid_coeff', self.moment_inviscid_coeff)
        _add('moment_viscous_coeff', self.moment_viscous_coeff)
        _add('force_inviscid_coeff', self.force_inviscid_coeff)
        _add('force_viscous_coeff', self.force_viscous_coeff)
        _add('eps_v', self.eps_v)
        _add('axial_drag_coeff', self.axial_drag_coeff)

        return el

    def to_version(self, target_version: str):
        return self
