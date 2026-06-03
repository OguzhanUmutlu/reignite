from ...plugin import Plugin


class FreeSpaceExplorerPlugin(Plugin):
    def __init__(
            self,
            lidar_topic: str = "scan",
            image_topic: str = "scan_image",
            start_topic: str = "start",
            sensor_link: str = "link",
            width: int = 10,
            height: int = 10,
            resolution: float = 1.0
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-free-space-explorer-system",
            name="gz::sim::systems::FreeSpaceExplorer",
            lidar_topic=lidar_topic,
            image_topic=image_topic,
            start_topic=start_topic,
            sensor_link=sensor_link,
            width=width,
            height=height,
            resolution=resolution
        )
