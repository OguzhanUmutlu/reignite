from reignite.elements.plugin import Plugin, ParentElement, TextElement


class PerformerDetectorPlugin(Plugin):
    class Box(ParentElement):
        def __init__(self, size: list[float] | str):
            if isinstance(size, list):
                size = " ".join(map(str, size))
            super().__init__("box", TextElement("size", size))

    class Geometry(ParentElement):
        def __init__(self, box: "PerformerDetectorPlugin.Box"):
            super().__init__("geometry", box)

    class HeaderData(ParentElement):
        def __init__(self, key: str, value: str):
            super().__init__(
                "header_data",
                TextElement("key", key),
                TextElement("value", value)
            )

    def __init__(
            self,
            geometry: Geometry | None = None,
            pose: list[float] | str | None = None,
            header_data: list[HeaderData] | HeaderData | None = None,
            topic: str | None = None,
    ):
        if isinstance(pose, list):
            pose = " ".join(map(str, pose))

        elements = []
        if geometry is not None:
            elements.append(geometry)
        if header_data is not None:
            if isinstance(header_data, PerformerDetectorPlugin.HeaderData):
                header_data = [header_data]
            elements.extend(header_data)

        super().__init__(
            sdf_version=None,
            filename="gz-sim-performer-detector-system",
            name="gz::sim::systems::PerformerDetector",
            elements=elements,
            pose=pose,
            topic=topic,
        )
