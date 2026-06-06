from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-logical-audio-sensor-plugin-system", "gz::sim::systems::LogicalAudioSensorPlugin")
class LogicalAudioSensorPlugin(Plugin):
    class Source(BaseModel):
        def __init__(
                self,
                id: int | str | None = None,
                pose: list[float] | str | None = None,
                attenuation_function: str | None = None,
                attenuation_shape: str | None = None,
                inner_radius: float | None = None,
                falloff_distance: float | None = None,
                volume_level: float | None = None,
                playing: bool | None = None,
                play_duration: float | None = None
        ):
            super().__init__(sdf_version=None)
            self.id = id
            self.pose = pose
            self.attenuation_function = attenuation_function
            self.attenuation_shape = attenuation_shape
            self.inner_radius = inner_radius
            self.falloff_distance = falloff_distance
            self.volume_level = volume_level
            self.playing = playing
            self.play_duration = play_duration

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            id_el = el.find("id")
            pose_el = el.find("pose")
            af_el = el.find("attenuation_function")
            ash_el = el.find("attenuation_shape")
            ir_el = el.find("inner_radius")
            fd_el = el.find("falloff_distance")
            vl_el = el.find("volume_level")
            p_el = el.find("playing")
            pd_el = el.find("play_duration")

            pose_val = None
            if pose_el is not None and pose_el.text:
                parts = pose_el.text.split()
                if len(parts) == 6:
                    pose_val = [float(p) for p in parts]
                else:
                    pose_val = pose_el.text

            return cls(
                id=int(id_el.text) if id_el is not None and id_el.text is not None and id_el.text.isdigit() else (
                    id_el.text if id_el is not None else None),
                pose=pose_val,
                attenuation_function=af_el.text if af_el is not None else None,
                attenuation_shape=ash_el.text if ash_el is not None else None,
                inner_radius=float(ir_el.text) if ir_el is not None and ir_el.text is not None else None,
                falloff_distance=float(fd_el.text) if fd_el is not None and fd_el.text is not None else None,
                volume_level=float(vl_el.text) if vl_el is not None and vl_el.text is not None else None,
                playing=p_el.text.lower() == 'true' if p_el is not None and p_el.text is not None else None,
                play_duration=float(pd_el.text) if pd_el is not None and pd_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("source")

            def _add(k, v):
                if v is not None:
                    child = ET.Element(k)
                    if isinstance(v, bool):
                        child.text = "true" if v else "false"
                    elif isinstance(v, (list, tuple)):
                        child.text = " ".join(map(str, v))
                    else:
                        child.text = str(v)
                    e.append(child)

            _add("id", self.id)
            _add("pose", self.pose)
            _add("attenuation_function", self.attenuation_function)
            _add("attenuation_shape", self.attenuation_shape)
            _add("inner_radius", self.inner_radius)
            _add("falloff_distance", self.falloff_distance)
            _add("volume_level", self.volume_level)
            _add("playing", self.playing)
            _add("play_duration", self.play_duration)
            return e

        def to_version(self, target_version: str):
            return self

    class Microphone(BaseModel):
        def __init__(
                self,
                id: int | str | None = None,
                pose: list[float] | str | None = None,
                volume_threshold: float | None = None
        ):
            super().__init__(sdf_version=None)
            self.id = id
            self.pose = pose
            self.volume_threshold = volume_threshold

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            id_el = el.find("id")
            pose_el = el.find("pose")
            vt_el = el.find("volume_threshold")

            pose_val = None
            if pose_el is not None and pose_el.text:
                parts = pose_el.text.split()
                if len(parts) == 6:
                    pose_val = [float(p) for p in parts]
                else:
                    pose_val = pose_el.text

            return cls(
                id=int(id_el.text) if id_el is not None and id_el.text is not None and id_el.text.isdigit() else (
                    id_el.text if id_el is not None else None),
                pose=pose_val,
                volume_threshold=float(vt_el.text) if vt_el is not None and vt_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("microphone")
            if self.id is not None:
                child = ET.Element("id")
                child.text = str(self.id)
                e.append(child)
            if self.pose is not None:
                child = ET.Element("pose")
                child.text = " ".join(map(str, self.pose)) if isinstance(self.pose, (list, tuple)) else str(self.pose)
                e.append(child)
            if self.volume_threshold is not None:
                child = ET.Element("volume_threshold")
                child.text = str(self.volume_threshold)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            source: list[Source] | Source | None = None,
            microphone: list[Microphone] | Microphone | None = None,
    ):
        self.source = [source] if isinstance(source, LogicalAudioSensorPlugin.Source) else (source or [])
        self.microphone = [microphone] if isinstance(microphone, LogicalAudioSensorPlugin.Microphone) else (
                    microphone or [])

        super().__init__(
            sdf_version=None,
            filename="gz-sim-logical-audio-sensor-plugin-system",
            name="gz::sim::systems::LogicalAudioSensorPlugin"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        src_els = el.findall("source")
        mic_els = el.findall("microphone")

        return cls(
            source=[cls.Source._from_sdf(s, version) for s in src_els] if src_els else None,
            microphone=[cls.Microphone._from_sdf(m, version) for m in mic_els] if mic_els else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::LogicalAudioSensorPlugin",
                        filename="gz-sim-logical-audio-sensor-plugin-system")
        if self.source:
            for s in self.source:
                el.append(s.to_sdf(version))
        if self.microphone:
            for m in self.microphone:
                el.append(m.to_sdf(version))
        return el

    def to_version(self, target_version: str):
        if self.source:
            for s in self.source:
                s.to_version(target_version)
        if self.microphone:
            for m in self.microphone:
                m.to_version(target_version)
        return self
