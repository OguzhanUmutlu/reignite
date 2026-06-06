from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-environment-preload-system", "gz::sim::systems::EnvironmentPreload")
class EnvironmentPreloadPlugin(Plugin):
    def __init__(
            self,
            data: str,
            ignore_time: bool = False,
            time: str = "t",
            reference: str = "global",
            units: str = "radians",
            x: str = "x",
            y: str = "y",
            z: str = "z"
    ):
        if not data:
            raise ValueError("data (environmental data file path) is required.")

        if reference not in ["global", "spherical", "ecef"]:
            raise ValueError(f"Unknown reference '{reference}'. Must be 'global', 'spherical', or 'ecef'.")

        if reference == "spherical" and units not in ["degrees", "radians"]:
            raise ValueError(f"Unrecognized unit '{units}'. Must be 'degrees' or 'radians'.")

        self.data = data
        self.ignore_time = ignore_time
        self.time = time
        self.reference = reference
        self.units = units
        self.x = x
        self.y = y
        self.z = z
        super().__init__(sdf_version=None, filename="gz-sim-environment-preload-system",
                         name="gz::sim::systems::EnvironmentPreload")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        data_el = el.find('data')
        ignore_time_el = el.find('ignore_time')
        time_el = el.find('time')
        reference_el = el.find('reference')
        units_el = el.find('units')
        x_el = el.find('x')
        y_el = el.find('y')
        z_el = el.find('z')

        return cls(
            data=data_el.text if data_el is not None and data_el.text is not None else None,
            ignore_time=ignore_time_el.text.lower() == 'true' if ignore_time_el is not None and ignore_time_el.text is not None else None,
            time=time_el.text if time_el is not None and time_el.text is not None else None,
            reference=reference_el.text if reference_el is not None and reference_el.text is not None else None,
            units=units_el.text if units_el is not None and units_el.text is not None else None,
            x=x_el.text if x_el is not None and x_el.text is not None else None,
            y=y_el.text if y_el is not None and y_el.text is not None else None,
            z=z_el.text if z_el is not None and z_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::EnvironmentPreload",
                        filename="gz-sim-environment-preload-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('data', self.data)
        _add('ignore_time', self.ignore_time)
        _add('time', self.time)
        _add('reference', self.reference)
        _add('units', self.units)
        _add('x', self.x)
        _add('y', self.y)
        _add('z', self.z)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        data_el = el.find('data')
        ignore_time_el = el.find('ignore_time')
        time_el = el.find('time')
        reference_el = el.find('reference')
        units_el = el.find('units')
        x_el = el.find('x')
        y_el = el.find('y')
        z_el = el.find('z')

        return cls(
            data=data_el.text if data_el is not None and data_el.text is not None else None,
            ignore_time=ignore_time_el.text.lower() == 'true' if ignore_time_el is not None and ignore_time_el.text is not None else None,
            time=time_el.text if time_el is not None and time_el.text is not None else None,
            reference=reference_el.text if reference_el is not None and reference_el.text is not None else None,
            units=units_el.text if units_el is not None and units_el.text is not None else None,
            x=x_el.text if x_el is not None and x_el.text is not None else None,
            y=y_el.text if y_el is not None and y_el.text is not None else None,
            z=z_el.text if z_el is not None and z_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::EnvironmentPreload",
                        filename="gz-sim-environment-preload-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('data', self.data)
        _add('ignore_time', self.ignore_time)
        _add('time', self.time)
        _add('reference', self.reference)
        _add('units', self.units)
        _add('x', self.x)
        _add('y', self.y)
        _add('z', self.z)

        return el

    def to_version(self, target_version: str):
        return self
