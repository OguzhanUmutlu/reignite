from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-lookup-wheel-slip-system", "gz::sim::systems::LookupWheelSlip")
class LookupWheelSlipPlugin(Plugin):
    def __init__(
            self,
            slip_map: str | None = None,
            size_x: float | None = None,
            size_y: float | None = None,
            wheel_link_name: list[str] | str | None = None,
            slip_compliance_lateral_delta: float | None = None,
            slip_compliance_longitudinal_delta: float | None = None,
            friction_delta: float | None = None,
            **kwargs,
    ):
        self.slip_map = slip_map
        self.size_x = size_x
        self.size_y = size_y
        self.wheel_link_name = wheel_link_name
        self.slip_compliance_lateral_delta = slip_compliance_lateral_delta
        self.slip_compliance_longitudinal_delta = slip_compliance_longitudinal_delta
        self.friction_delta = friction_delta
        super().__init__(sdf_version=None, filename="gz-sim-lookup-wheel-slip-system",
                         name="gz::sim::systems::LookupWheelSlip")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        slip_map_el = el.find('slip_map')
        size_x_el = el.find('size_x')
        size_y_el = el.find('size_y')
        wheel_link_name_els = el.findall('wheel_link_name')
        wheel_link_name_vals = [e.text for e in wheel_link_name_els if
                                e.text is not None] if wheel_link_name_els else None
        slip_compliance_lateral_delta_el = el.find('slip_compliance_lateral_delta')
        slip_compliance_longitudinal_delta_el = el.find('slip_compliance_longitudinal_delta')
        friction_delta_el = el.find('friction_delta')

        return cls(
            slip_map=slip_map_el.text if slip_map_el is not None and slip_map_el.text is not None else None,
            size_x=float(size_x_el.text) if size_x_el is not None and size_x_el.text is not None else None,
            size_y=float(size_y_el.text) if size_y_el is not None and size_y_el.text is not None else None,
            wheel_link_name=wheel_link_name_vals,
            slip_compliance_lateral_delta=float(
                slip_compliance_lateral_delta_el.text) if slip_compliance_lateral_delta_el is not None and slip_compliance_lateral_delta_el.text is not None else None,
            slip_compliance_longitudinal_delta=float(
                slip_compliance_longitudinal_delta_el.text) if slip_compliance_longitudinal_delta_el is not None and slip_compliance_longitudinal_delta_el.text is not None else None,
            friction_delta=float(
                friction_delta_el.text) if friction_delta_el is not None and friction_delta_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LookupWheelSlip",
                        filename="gz-sim-lookup-wheel-slip-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('slip_map', self.slip_map)
        _add('size_x', self.size_x)
        _add('size_y', self.size_y)
        if self.wheel_link_name is not None:
            for v in (self.wheel_link_name if isinstance(self.wheel_link_name, list) else [self.wheel_link_name]):
                _add('wheel_link_name', v)
        _add('slip_compliance_lateral_delta', self.slip_compliance_lateral_delta)
        _add('slip_compliance_longitudinal_delta', self.slip_compliance_longitudinal_delta)
        _add('friction_delta', self.friction_delta)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        slip_map_el = el.find('slip_map')
        size_x_el = el.find('size_x')
        size_y_el = el.find('size_y')
        wheel_link_name_els = el.findall('wheel_link_name')
        wheel_link_name_vals = [e.text for e in wheel_link_name_els if
                                e.text is not None] if wheel_link_name_els else None
        slip_compliance_lateral_delta_el = el.find('slip_compliance_lateral_delta')
        slip_compliance_longitudinal_delta_el = el.find('slip_compliance_longitudinal_delta')
        friction_delta_el = el.find('friction_delta')

        return cls(
            slip_map=slip_map_el.text if slip_map_el is not None and slip_map_el.text is not None else None,
            size_x=float(size_x_el.text) if size_x_el is not None and size_x_el.text is not None else None,
            size_y=float(size_y_el.text) if size_y_el is not None and size_y_el.text is not None else None,
            wheel_link_name=wheel_link_name_vals,
            slip_compliance_lateral_delta=float(
                slip_compliance_lateral_delta_el.text) if slip_compliance_lateral_delta_el is not None and slip_compliance_lateral_delta_el.text is not None else None,
            slip_compliance_longitudinal_delta=float(
                slip_compliance_longitudinal_delta_el.text) if slip_compliance_longitudinal_delta_el is not None and slip_compliance_longitudinal_delta_el.text is not None else None,
            friction_delta=float(
                friction_delta_el.text) if friction_delta_el is not None and friction_delta_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LookupWheelSlip",
                        filename="gz-sim-lookup-wheel-slip-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('slip_map', self.slip_map)
        _add('size_x', self.size_x)
        _add('size_y', self.size_y)
        if self.wheel_link_name is not None:
            for v in (self.wheel_link_name if isinstance(self.wheel_link_name, list) else [self.wheel_link_name]):
                _add('wheel_link_name', v)
        _add('slip_compliance_lateral_delta', self.slip_compliance_lateral_delta)
        _add('slip_compliance_longitudinal_delta', self.slip_compliance_longitudinal_delta)
        _add('friction_delta', self.friction_delta)

        return el

    def to_version(self, target_version: str):
        return self
