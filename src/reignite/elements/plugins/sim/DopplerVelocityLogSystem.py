from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-doppler-velocity-log-system", "gz::sim::systems::DopplerVelocityLogSystem")
class DopplerVelocityLogSystemPlugin(Plugin):
    def __init__(self):
        super().__init__(sdf_version=None, filename="gz-sim-doppler-velocity-log-system",
                         name="gz::sim::systems::DopplerVelocityLogSystem")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):

        return cls(

        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::DopplerVelocityLogSystem",
                        filename="gz-sim-doppler-velocity-log-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):

        return cls(

        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin",
                        name=self.name if hasattr(self, 'name') else "gz::sim::systems::DopplerVelocityLogSystem",
                        filename="gz-sim-doppler-velocity-log-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        return el

    def to_version(self, target_version: str):
        return self
