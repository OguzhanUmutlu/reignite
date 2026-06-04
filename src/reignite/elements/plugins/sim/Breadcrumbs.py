from reignite import BaseModel
from reignite.elements.plugin import Plugin, ParentElement, TextElement


@Plugin.register("gz-sim-breadcrumbs-system", "gz::sim::systems::Breadcrumbs")
class BreadcrumbsPlugin(Plugin):
    class Box(ParentElement):
        def __init__(self, size: list[float] | str):
            if isinstance(size, list):
                size = " ".join(map(str, size))
            super().__init__("box", [TextElement("size", size)])

    class Geometry(ParentElement):
        def __init__(self, box: "BreadcrumbsPlugin.Box"):
            super().__init__("geometry", [box])

    class PerformerVolume(ParentElement):
        def __init__(self, geometry: "BreadcrumbsPlugin.Geometry"):
            super().__init__("performer_volume", [geometry])

    class Breadcrumb(ParentElement):
        def __init__(self, sdf: str):
            super().__init__("breadcrumb", [TextElement("sdf", sdf)])

    def __init__(
            self,
            breadcrumb: Breadcrumb | str,
            max_deployments: int | None = None,
            disable_physics_time: float = 0.0,
            allow_renaming: bool | None = None,
            performer_volume: PerformerVolume | None = None,
            topic: str | None = None,
            topic_statistics: bool | None = None
    ):
        if isinstance(breadcrumb, str):
            breadcrumb = BreadcrumbsPlugin.Breadcrumb(breadcrumb)

        elements: list[BaseModel] = [breadcrumb]
        if performer_volume is not None:
            elements.append(performer_volume)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-breadcrumbs-system",
            name="gz::sim::systems::Breadcrumbs",
            elements=elements,
            max_deployments=max_deployments,
            disable_physics_time=disable_physics_time,
            allow_renaming=allow_renaming,
            topic=topic,
            topic_statistics=topic_statistics
        )
