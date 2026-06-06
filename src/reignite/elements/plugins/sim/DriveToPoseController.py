from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-drive-to-pose-controller-system", "gz::sim::systems::DriveToPoseController")
class DriveToPoseControllerPlugin(Plugin):
    def __init__(
            self,
            linear_p_gain: float = 1.0,
            angular_p_gain: float = 2.0,
            linear_deviation: float = 0.1,
            angular_deviation: float = 0.05
    ):
        if linear_p_gain < 0.0 or angular_p_gain < 0.0:
            raise ValueError("Proportional gains (linear_p_gain, angular_p_gain) must be non-negative.")

        if linear_deviation < 0.0 or angular_deviation < 0.0:
            raise ValueError("Allowable deviations (linear_deviation, angular_deviation) must be non-negative.")

        self.linear_p_gain = linear_p_gain
        self.angular_p_gain = angular_p_gain
        self.linear_deviation = linear_deviation
        self.angular_deviation = angular_deviation
        super().__init__(sdf_version=None, filename="gz-sim-drive-to-pose-controller-system",
                         name="gz::sim::systems::DriveToPoseController")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        linear_p_gain_el = el.find('linear_p_gain')
        angular_p_gain_el = el.find('angular_p_gain')
        linear_deviation_el = el.find('linear_deviation')
        angular_deviation_el = el.find('angular_deviation')

        return cls(
            linear_p_gain=float(
                linear_p_gain_el.text) if linear_p_gain_el is not None and linear_p_gain_el.text is not None else None,
            angular_p_gain=float(
                angular_p_gain_el.text) if angular_p_gain_el is not None and angular_p_gain_el.text is not None else None,
            linear_deviation=float(
                linear_deviation_el.text) if linear_deviation_el is not None and linear_deviation_el.text is not None else None,
            angular_deviation=float(
                angular_deviation_el.text) if angular_deviation_el is not None and angular_deviation_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::DriveToPoseController",
                        filename="gz-sim-drive-to-pose-controller-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('linear_p_gain', self.linear_p_gain)
        _add('angular_p_gain', self.angular_p_gain)
        _add('linear_deviation', self.linear_deviation)
        _add('angular_deviation', self.angular_deviation)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        linear_p_gain_el = el.find('linear_p_gain')
        angular_p_gain_el = el.find('angular_p_gain')
        linear_deviation_el = el.find('linear_deviation')
        angular_deviation_el = el.find('angular_deviation')

        return cls(
            linear_p_gain=float(
                linear_p_gain_el.text) if linear_p_gain_el is not None and linear_p_gain_el.text is not None else None,
            angular_p_gain=float(
                angular_p_gain_el.text) if angular_p_gain_el is not None and angular_p_gain_el.text is not None else None,
            linear_deviation=float(
                linear_deviation_el.text) if linear_deviation_el is not None and linear_deviation_el.text is not None else None,
            angular_deviation=float(
                angular_deviation_el.text) if angular_deviation_el is not None and angular_deviation_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::DriveToPoseController",
                        filename="gz-sim-drive-to-pose-controller-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('linear_p_gain', self.linear_p_gain)
        _add('angular_p_gain', self.angular_p_gain)
        _add('linear_deviation', self.linear_deviation)
        _add('angular_deviation', self.angular_deviation)

        return el

    def to_version(self, target_version: str):
        return self
