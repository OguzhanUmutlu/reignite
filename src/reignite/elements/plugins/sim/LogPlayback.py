from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-log-playback-system", "gz::sim::systems::LogPlayback")
class LogPlaybackPlugin(Plugin):
    def __init__(
            self,
            playback_path: str | None = None,
    ):
        self.playback_path = playback_path
        super().__init__(sdf_version=None, filename="gz-sim-log-playback-system", name="gz::sim::systems::LogPlayback")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        playback_path_el = el.find('playback_path')

        return cls(
            playback_path=playback_path_el.text if playback_path_el is not None and playback_path_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LogPlayback",
                        filename="gz-sim-log-playback-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('playback_path', self.playback_path)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        playback_path_el = el.find('playback_path')

        return cls(
            playback_path=playback_path_el.text if playback_path_el is not None and playback_path_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LogPlayback",
                        filename="gz-sim-log-playback-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('playback_path', self.playback_path)

        return el

    def to_version(self, target_version: str):
        return self
