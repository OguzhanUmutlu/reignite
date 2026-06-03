from ...plugin import Plugin


class LogRecordPlugin(Plugin):
    def __init__(
            self,
            record_resources: bool | None = None,
            record_period: float | None = None,
            compress: bool | None = None,
            compress_path: str | None = None,
            record_path: str | None = None,
            record_topic: list[str] | str | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-log-record-system",
            name="gz::sim::systems::LogRecord",
            record_resources=record_resources,
            record_period=record_period,
            compress=compress,
            compress_path=compress_path,
            record_path=record_path,
            record_topic=record_topic,
        )
