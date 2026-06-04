from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-free-space-explorer-system", "gz::sim::systems::FreeSpaceExplorer")
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
        self.lidar_topic = lidar_topic
        self.image_topic = image_topic
        self.start_topic = start_topic
        self.sensor_link = sensor_link
        self.width = width
        self.height = height
        self.resolution = resolution
        super().__init__(sdf_version=None, filename="gz-sim-free-space-explorer-system", name="gz::sim::systems::FreeSpaceExplorer")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        lidar_topic_el = el.find('lidar_topic')
        image_topic_el = el.find('image_topic')
        start_topic_el = el.find('start_topic')
        sensor_link_el = el.find('sensor_link')
        width_el = el.find('width')
        height_el = el.find('height')
        resolution_el = el.find('resolution')

        return cls(
            lidar_topic=lidar_topic_el.text if lidar_topic_el is not None and lidar_topic_el.text is not None else None,
            image_topic=image_topic_el.text if image_topic_el is not None and image_topic_el.text is not None else None,
            start_topic=start_topic_el.text if start_topic_el is not None and start_topic_el.text is not None else None,
            sensor_link=sensor_link_el.text if sensor_link_el is not None and sensor_link_el.text is not None else None,
            width=int(width_el.text) if width_el is not None and width_el.text is not None else None,
            height=int(height_el.text) if height_el is not None and height_el.text is not None else None,
            resolution=float(resolution_el.text) if resolution_el is not None and resolution_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::FreeSpaceExplorer", filename="gz-sim-free-space-explorer-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('lidar_topic', self.lidar_topic)
        _add('image_topic', self.image_topic)
        _add('start_topic', self.start_topic)
        _add('sensor_link', self.sensor_link)
        _add('width', self.width)
        _add('height', self.height)
        _add('resolution', self.resolution)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        lidar_topic_el = el.find('lidar_topic')
        image_topic_el = el.find('image_topic')
        start_topic_el = el.find('start_topic')
        sensor_link_el = el.find('sensor_link')
        width_el = el.find('width')
        height_el = el.find('height')
        resolution_el = el.find('resolution')

        return cls(
            lidar_topic=lidar_topic_el.text if lidar_topic_el is not None and lidar_topic_el.text is not None else None,
            image_topic=image_topic_el.text if image_topic_el is not None and image_topic_el.text is not None else None,
            start_topic=start_topic_el.text if start_topic_el is not None and start_topic_el.text is not None else None,
            sensor_link=sensor_link_el.text if sensor_link_el is not None and sensor_link_el.text is not None else None,
            width=int(width_el.text) if width_el is not None and width_el.text is not None else None,
            height=int(height_el.text) if height_el is not None and height_el.text is not None else None,
            resolution=float(resolution_el.text) if resolution_el is not None and resolution_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::FreeSpaceExplorer", filename="gz-sim-free-space-explorer-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('lidar_topic', self.lidar_topic)
        _add('image_topic', self.image_topic)
        _add('start_topic', self.start_topic)
        _add('sensor_link', self.sensor_link)
        _add('width', self.width)
        _add('height', self.height)
        _add('resolution', self.resolution)
            
        return el

    def to_version(self, target_version: str):
        return self
