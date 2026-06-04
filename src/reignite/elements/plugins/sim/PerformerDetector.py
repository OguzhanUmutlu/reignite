from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-performer-detector-system", "gz::sim::systems::PerformerDetector")
class PerformerDetectorPlugin(Plugin):
    class Box(BaseModel):
        def __init__(self, size: list[float] | str | None = None):
            super().__init__(sdf_version=None)
            self.size = size

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            size_el = el.find("size")
            size_val = None
            if size_el is not None and size_el.text:
                parts = size_el.text.split()
                if len(parts) == 3:
                    size_val = [float(p) for p in parts]
                else:
                    size_val = size_el.text
            return cls(size=size_val)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("box")
            if self.size is not None:
                child = ET.Element("size")
                child.text = " ".join(map(str, self.size)) if isinstance(self.size, list) else str(self.size)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class Geometry(BaseModel):
        def __init__(self, box: "PerformerDetectorPlugin.Box | None" = None):
            super().__init__(sdf_version=None)
            self.box = box

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            box_el = el.find("box")
            return cls(box=PerformerDetectorPlugin.Box._from_sdf(box_el, version) if box_el is not None else None)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("geometry")
            if self.box is not None:
                e.append(self.box.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            if self.box is not None:
                self.box.to_version(target_version)
            return self

    class HeaderData(BaseModel):
        def __init__(self, key: str | None = None, value: str | None = None):
            super().__init__(sdf_version=None)
            self.key = key
            self.value = value

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            k_el = el.find("key")
            v_el = el.find("value")
            return cls(
                key=k_el.text if k_el is not None else None,
                value=v_el.text if v_el is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("header_data")
            if self.key is not None:
                child = ET.Element("key")
                child.text = str(self.key)
                e.append(child)
            if self.value is not None:
                child = ET.Element("value")
                child.text = str(self.value)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            geometry: Geometry | None = None,
            pose: list[float] | str | None = None,
            header_data: list[HeaderData] | HeaderData | None = None,
            topic: str | None = None,
    ):
        self.geometry = geometry
        self.pose = pose
        self.header_data = [header_data] if isinstance(header_data, PerformerDetectorPlugin.HeaderData) else (header_data or [])
        self.topic = topic

        super().__init__(
            sdf_version=None,
            filename="gz-sim-performer-detector-system",
            name="gz::sim::systems::PerformerDetector"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        g_el = el.find("geometry")
        p_el = el.find("pose")
        t_el = el.find("topic")
        hd_els = el.findall("header_data")

        pose_val = None
        if p_el is not None and p_el.text:
            parts = p_el.text.split()
            if len(parts) == 6:
                pose_val = [float(p) for p in parts]
            else:
                pose_val = p_el.text

        return cls(
            geometry=cls.Geometry._from_sdf(g_el, version) if g_el is not None else None,
            pose=pose_val,
            header_data=[cls.HeaderData._from_sdf(hd, version) for hd in hd_els] if hd_els else None,
            topic=t_el.text if t_el is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::PerformerDetector", filename="gz-sim-performer-detector-system")
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.pose is not None:
            child = ET.Element("pose")
            child.text = " ".join(map(str, self.pose)) if isinstance(self.pose, (list, tuple)) else str(self.pose)
            el.append(child)
        if self.header_data:
            for hd in self.header_data:
                el.append(hd.to_sdf(version))
        if self.topic is not None:
            child = ET.Element("topic")
            child.text = str(self.topic)
            el.append(child)
        return el

    def to_version(self, target_version: str):
        if self.geometry is not None:
            self.geometry.to_version(target_version)
        if self.header_data:
            for hd in self.header_data:
                hd.to_version(target_version)
        return self
