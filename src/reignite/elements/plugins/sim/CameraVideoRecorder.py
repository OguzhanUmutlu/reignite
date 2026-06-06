from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-camera-video-recorder-system", "gz::sim::systems::CameraVideoRecorder")
class CameraVideoRecorderPlugin(Plugin):
    def __init__(
            self,
            service: str | None = None,
            use_sim_time: bool = False,
            bitrate: int = 2070000,
            fps: int = 25
    ):
        self.service = service
        self.use_sim_time = use_sim_time
        self.bitrate = bitrate
        self.fps = fps
        super().__init__(sdf_version=None, filename="gz-sim-camera-video-recorder-system",
                         name="gz::sim::systems::CameraVideoRecorder")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        service_el = el.find('service')
        use_sim_time_el = el.find('use_sim_time')
        bitrate_el = el.find('bitrate')
        fps_el = el.find('fps')

        return cls(
            service=service_el.text if service_el is not None and service_el.text is not None else None,
            use_sim_time=use_sim_time_el.text.lower() == 'true' if use_sim_time_el is not None and use_sim_time_el.text is not None else None,
            bitrate=int(bitrate_el.text) if bitrate_el is not None and bitrate_el.text is not None else None,
            fps=int(fps_el.text) if fps_el is not None and fps_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::CameraVideoRecorder",
                        filename="gz-sim-camera-video-recorder-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('service', self.service)
        _add('use_sim_time', self.use_sim_time)
        _add('bitrate', self.bitrate)
        _add('fps', self.fps)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        service_el = el.find('service')
        use_sim_time_el = el.find('use_sim_time')
        bitrate_el = el.find('bitrate')
        fps_el = el.find('fps')

        return cls(
            service=service_el.text if service_el is not None and service_el.text is not None else None,
            use_sim_time=use_sim_time_el.text.lower() == 'true' if use_sim_time_el is not None and use_sim_time_el.text is not None else None,
            bitrate=int(bitrate_el.text) if bitrate_el is not None and bitrate_el.text is not None else None,
            fps=int(fps_el.text) if fps_el is not None and fps_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::CameraVideoRecorder",
                        filename="gz-sim-camera-video-recorder-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('service', self.service)
        _add('use_sim_time', self.use_sim_time)
        _add('bitrate', self.bitrate)
        _add('fps', self.fps)

        return el

    def to_version(self, target_version: str):
        return self
