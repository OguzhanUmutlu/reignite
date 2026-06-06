from xml.etree import ElementTree as ET

from reignite import BaseModel
from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-breadcrumbs-system", "gz::sim::systems::Breadcrumbs")
class BreadcrumbsPlugin(Plugin):
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
        def __init__(self, box: "BreadcrumbsPlugin.Box | None" = None):
            super().__init__(sdf_version=None)
            self.box = box

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            box_el = el.find("box")
            return cls(box=BreadcrumbsPlugin.Box._from_sdf(box_el, version) if box_el is not None else None)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("geometry")
            if self.box is not None:
                e.append(self.box.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            if self.box is not None:
                self.box.to_version(target_version)
            return self

    class PerformerVolume(BaseModel):
        def __init__(self, geometry: "BreadcrumbsPlugin.Geometry | None" = None):
            super().__init__(sdf_version=None)
            self.geometry = geometry

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            geom_el = el.find("geometry")
            return cls(geometry=BreadcrumbsPlugin.Geometry._from_sdf(geom_el, version) if geom_el is not None else None)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("performer_volume")
            if self.geometry is not None:
                e.append(self.geometry.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            if self.geometry is not None:
                self.geometry.to_version(target_version)
            return self

    class Breadcrumb(BaseModel):
        def __init__(self, sdf: str | None = None):
            super().__init__(sdf_version=None)
            self.sdf = sdf

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            sdf_el = el.find("sdf")
            return cls(sdf=sdf_el.text if sdf_el is not None else None)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("breadcrumb")
            if self.sdf is not None:
                child = ET.Element("sdf")
                child.text = str(self.sdf)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            breadcrumb: Breadcrumb | str | None = None,
            max_deployments: int | None = None,
            disable_physics_time: float | None = None,
            allow_renaming: bool | None = None,
            performer_volume: PerformerVolume | None = None,
            topic: str | None = None,
            topic_statistics: bool | None = None
    ):
        if isinstance(breadcrumb, str):
            breadcrumb = BreadcrumbsPlugin.Breadcrumb(breadcrumb)

        self.breadcrumb = breadcrumb
        self.max_deployments = max_deployments
        self.disable_physics_time = disable_physics_time
        self.allow_renaming = allow_renaming
        self.performer_volume = performer_volume
        self.topic = topic
        self.topic_statistics = topic_statistics

        super().__init__(
            sdf_version=None,
            filename="gz-sim-breadcrumbs-system",
            name="gz::sim::systems::Breadcrumbs"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        breadcrumb_el = el.find("breadcrumb")
        pv_el = el.find("performer_volume")
        md_el = el.find("max_deployments")
        dpt_el = el.find("disable_physics_time")
        ar_el = el.find("allow_renaming")
        topic_el = el.find("topic")
        ts_el = el.find("topic_statistics")

        return cls(
            breadcrumb=cls.Breadcrumb._from_sdf(breadcrumb_el, version) if breadcrumb_el is not None else None,
            max_deployments=int(md_el.text) if md_el is not None and md_el.text is not None else None,
            disable_physics_time=float(dpt_el.text) if dpt_el is not None and dpt_el.text is not None else None,
            allow_renaming=ar_el.text.lower() == 'true' if ar_el is not None and ar_el.text is not None else None,
            performer_volume=cls.PerformerVolume._from_sdf(pv_el, version) if pv_el is not None else None,
            topic=topic_el.text if topic_el is not None else None,
            topic_statistics=ts_el.text.lower() == 'true' if ts_el is not None and ts_el.text is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::Breadcrumbs", filename="gz-sim-breadcrumbs-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        if self.breadcrumb is not None:
            el.append(self.breadcrumb.to_sdf(version))
        _add("max_deployments", self.max_deployments)
        _add("disable_physics_time", self.disable_physics_time)
        _add("allow_renaming", self.allow_renaming)
        if self.performer_volume is not None:
            el.append(self.performer_volume.to_sdf(version))
        _add("topic", self.topic)
        _add("topic_statistics", self.topic_statistics)

        return el

    def to_version(self, target_version: str):
        if self.breadcrumb is not None:
            self.breadcrumb.to_version(target_version)
        if self.performer_volume is not None:
            self.performer_volume.to_version(target_version)
        return self
