from ...plugin import Plugin


class CameraVideoRecorderPlugin(Plugin):
    def __init__(
            self,
            service: str | None = None,
            use_sim_time: bool = False,
            bitrate: int = 2070000,
            fps: int = 25
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-camera-video-recorder-system",
            name="gz::sim::systems::CameraVideoRecorder",
            service=service,
            use_sim_time=use_sim_time,
            bitrate=bitrate,
            fps=fps
        )
