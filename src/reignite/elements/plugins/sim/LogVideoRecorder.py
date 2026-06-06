from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-log-video-recorder-system", "gz::sim::systems::LogVideoRecorder")
class LogVideoRecorderPlugin(Plugin):
    class Region(BaseModel):
        def __init__(self, min: list[float] | tuple[float, float, float] | str | None = None,
                     max: list[float] | tuple[float, float, float] | str | None = None):
            super().__init__(sdf_version=None)
            self.min = min
            self.max = max

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            min_el = el.find("min")
            max_el = el.find("max")
            min_val = None
            max_val = None

            if min_el is not None and min_el.text:
                parts = min_el.text.split()
                if len(parts) == 3:
                    min_val = [float(p) for p in parts]
                else:
                    min_val = min_el.text

            if max_el is not None and max_el.text:
                parts = max_el.text.split()
                if len(parts) == 3:
                    max_val = [float(p) for p in parts]
                else:
                    max_val = max_el.text

            return cls(min=min_val, max=max_val)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("region")
            if self.min is not None:
                child = ET.Element("min")
                child.text = " ".join(map(str, self.min)) if isinstance(self.min, (list, tuple)) else str(self.min)
                e.append(child)
            if self.max is not None:
                child = ET.Element("max")
                child.text = " ".join(map(str, self.max)) if isinstance(self.max, (list, tuple)) else str(self.max)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            entity: str | list[str] | None = None,
            region: Region | list[Region] | None = None,
            start_time: float | None = None,
            end_time: float | None = None,
            exit_on_finish: bool | None = None,
    ):
        self.entity = [entity] if isinstance(entity, str) else (entity or [])
        self.region = [region] if isinstance(region, LogVideoRecorderPlugin.Region) else (region or [])
        self.start_time = start_time
        self.end_time = end_time
        self.exit_on_finish = exit_on_finish

        super().__init__(
            sdf_version=None,
            filename="gz-sim-log-video-recorder-system",
            name="gz::sim::systems::LogVideoRecorder"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        ent_els = el.findall("entity")
        reg_els = el.findall("region")
        st_el = el.find("start_time")
        et_el = el.find("end_time")
        eof_el = el.find("exit_on_finish")

        return cls(
            entity=[e.text for e in ent_els if e.text is not None] if ent_els else None,
            region=[cls.Region._from_sdf(r, version) for r in reg_els] if reg_els else None,
            start_time=float(st_el.text) if st_el is not None and st_el.text is not None else None,
            end_time=float(et_el.text) if et_el is not None and et_el.text is not None else None,
            exit_on_finish=eof_el.text.lower() == 'true' if eof_el is not None and eof_el.text is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::LogVideoRecorder",
                        filename="gz-sim-log-video-recorder-system")
        if self.entity:
            for e in self.entity:
                child = ET.Element("entity")
                child.text = str(e)
                el.append(child)
        if self.region:
            for r in self.region:
                el.append(r.to_sdf(version))

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add("start_time", self.start_time)
        _add("end_time", self.end_time)
        _add("exit_on_finish", self.exit_on_finish)
        return el

    def to_version(self, target_version: str):
        if self.region:
            for r in self.region:
                r.to_version(target_version)
        return self
