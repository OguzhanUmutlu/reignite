from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-rf-comms-system", "gz::sim::systems::RFComms")
class RFCommsPlugin(Plugin):
    def __init__(
            self,
            max_range: float | None = None,
            fading_exponent: float | None = None,
            l0: float | None = None,
            sigma: float | None = None,
            capacity: float | None = None,
            tx_power: float | None = None,
            modulation: str | None = None,
            noise_floor: float | None = None,
            **kwargs
    ):
        self.max_range = max_range
        self.fading_exponent = fading_exponent
        self.l0 = l0
        self.sigma = sigma
        self.capacity = capacity
        self.tx_power = tx_power
        self.modulation = modulation
        self.noise_floor = noise_floor
        super().__init__(sdf_version=None, filename="gz-sim-rf-comms-system", name="gz::sim::systems::RFComms")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        max_range_el = el.find('max_range')
        fading_exponent_el = el.find('fading_exponent')
        l0_el = el.find('l0')
        sigma_el = el.find('sigma')
        capacity_el = el.find('capacity')
        tx_power_el = el.find('tx_power')
        modulation_el = el.find('modulation')
        noise_floor_el = el.find('noise_floor')

        return cls(
            max_range=float(max_range_el.text) if max_range_el is not None and max_range_el.text is not None else None,
            fading_exponent=float(
                fading_exponent_el.text) if fading_exponent_el is not None and fading_exponent_el.text is not None else None,
            l0=float(l0_el.text) if l0_el is not None and l0_el.text is not None else None,
            sigma=float(sigma_el.text) if sigma_el is not None and sigma_el.text is not None else None,
            capacity=float(capacity_el.text) if capacity_el is not None and capacity_el.text is not None else None,
            tx_power=float(tx_power_el.text) if tx_power_el is not None and tx_power_el.text is not None else None,
            modulation=modulation_el.text if modulation_el is not None and modulation_el.text is not None else None,
            noise_floor=float(
                noise_floor_el.text) if noise_floor_el is not None and noise_floor_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::RFComms",
                        filename="gz-sim-rf-comms-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('max_range', self.max_range)
        _add('fading_exponent', self.fading_exponent)
        _add('l0', self.l0)
        _add('sigma', self.sigma)
        _add('capacity', self.capacity)
        _add('tx_power', self.tx_power)
        _add('modulation', self.modulation)
        _add('noise_floor', self.noise_floor)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        max_range_el = el.find('max_range')
        fading_exponent_el = el.find('fading_exponent')
        l0_el = el.find('l0')
        sigma_el = el.find('sigma')
        capacity_el = el.find('capacity')
        tx_power_el = el.find('tx_power')
        modulation_el = el.find('modulation')
        noise_floor_el = el.find('noise_floor')

        return cls(
            max_range=float(max_range_el.text) if max_range_el is not None and max_range_el.text is not None else None,
            fading_exponent=float(
                fading_exponent_el.text) if fading_exponent_el is not None and fading_exponent_el.text is not None else None,
            l0=float(l0_el.text) if l0_el is not None and l0_el.text is not None else None,
            sigma=float(sigma_el.text) if sigma_el is not None and sigma_el.text is not None else None,
            capacity=float(capacity_el.text) if capacity_el is not None and capacity_el.text is not None else None,
            tx_power=float(tx_power_el.text) if tx_power_el is not None and tx_power_el.text is not None else None,
            modulation=modulation_el.text if modulation_el is not None and modulation_el.text is not None else None,
            noise_floor=float(
                noise_floor_el.text) if noise_floor_el is not None and noise_floor_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::RFComms",
                        filename="gz-sim-rf-comms-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('max_range', self.max_range)
        _add('fading_exponent', self.fading_exponent)
        _add('l0', self.l0)
        _add('sigma', self.sigma)
        _add('capacity', self.capacity)
        _add('tx_power', self.tx_power)
        _add('modulation', self.modulation)
        _add('noise_floor', self.noise_floor)

        return el

    def to_version(self, target_version: str):
        return self
