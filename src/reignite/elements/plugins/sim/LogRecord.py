from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-log-record-system", "gz::sim::systems::LogRecord")
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
        self.record_resources = record_resources
        self.record_period = record_period
        self.compress = compress
        self.compress_path = compress_path
        self.record_path = record_path
        self.record_topic = record_topic
        super().__init__(sdf_version=None, filename="gz-sim-log-record-system", name="gz::sim::systems::LogRecord")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        record_resources_el = el.find('record_resources')
        record_period_el = el.find('record_period')
        compress_el = el.find('compress')
        compress_path_el = el.find('compress_path')
        record_path_el = el.find('record_path')
        record_topic_els = el.findall('record_topic')
        record_topic_vals = [e.text for e in record_topic_els if e.text is not None] if record_topic_els else None

        return cls(
            record_resources=record_resources_el.text.lower() == 'true' if record_resources_el is not None and record_resources_el.text is not None else None,
            record_period=float(
                record_period_el.text) if record_period_el is not None and record_period_el.text is not None else None,
            compress=compress_el.text.lower() == 'true' if compress_el is not None and compress_el.text is not None else None,
            compress_path=compress_path_el.text if compress_path_el is not None and compress_path_el.text is not None else None,
            record_path=record_path_el.text if record_path_el is not None and record_path_el.text is not None else None,
            record_topic=record_topic_vals,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LogRecord",
                        filename="gz-sim-log-record-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('record_resources', self.record_resources)
        _add('record_period', self.record_period)
        _add('compress', self.compress)
        _add('compress_path', self.compress_path)
        _add('record_path', self.record_path)
        if self.record_topic is not None:
            for v in (self.record_topic if isinstance(self.record_topic, list) else [self.record_topic]):
                _add('record_topic', v)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        record_resources_el = el.find('record_resources')
        record_period_el = el.find('record_period')
        compress_el = el.find('compress')
        compress_path_el = el.find('compress_path')
        record_path_el = el.find('record_path')
        record_topic_els = el.findall('record_topic')
        record_topic_vals = [e.text for e in record_topic_els if e.text is not None] if record_topic_els else None

        return cls(
            record_resources=record_resources_el.text.lower() == 'true' if record_resources_el is not None and record_resources_el.text is not None else None,
            record_period=float(
                record_period_el.text) if record_period_el is not None and record_period_el.text is not None else None,
            compress=compress_el.text.lower() == 'true' if compress_el is not None and compress_el.text is not None else None,
            compress_path=compress_path_el.text if compress_path_el is not None and compress_path_el.text is not None else None,
            record_path=record_path_el.text if record_path_el is not None and record_path_el.text is not None else None,
            record_topic=record_topic_vals,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LogRecord",
                        filename="gz-sim-log-record-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('record_resources', self.record_resources)
        _add('record_period', self.record_period)
        _add('compress', self.compress)
        _add('compress_path', self.compress_path)
        _add('record_path', self.record_path)
        if self.record_topic is not None:
            for v in (self.record_topic if isinstance(self.record_topic, list) else [self.record_topic]):
                _add('record_topic', v)

        return el

    def to_version(self, target_version: str):
        return self
