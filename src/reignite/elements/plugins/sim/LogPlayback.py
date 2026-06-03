from ...plugin import Plugin


class LogPlaybackPlugin(Plugin):
    def __init__(
            self,
            playback_path: str | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-log-playback-system",
            name="gz::sim::systems::LogPlayback",
            playback_path=playback_path,
        )
