from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-odometry-publisher-system", "gz::sim::systems::OdometryPublisher")
class OdometryPublisherPlugin(Plugin):
    def __init__(
            self,
            odom_frame: str | None = None,
            odom_publish_frequency: float | None = None,
            odom_topic: str | None = None,
            odom_covariance_topic: str | None = None,
            tf_topic: str | None = None,
            robot_base_frame: str | None = None,
            dimensions: int | None = None,
            gaussian_noise: float | None = None,
            **kwargs
    ):
        self.odom_frame = odom_frame
        self.odom_publish_frequency = odom_publish_frequency
        self.odom_topic = odom_topic
        self.odom_covariance_topic = odom_covariance_topic
        self.tf_topic = tf_topic
        self.robot_base_frame = robot_base_frame
        self.dimensions = dimensions
        self.gaussian_noise = gaussian_noise
        super().__init__(sdf_version=None, filename="gz-sim-odometry-publisher-system", name="gz::sim::systems::OdometryPublisher")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        odom_frame_el = el.find('odom_frame')
        odom_publish_frequency_el = el.find('odom_publish_frequency')
        odom_topic_el = el.find('odom_topic')
        odom_covariance_topic_el = el.find('odom_covariance_topic')
        tf_topic_el = el.find('tf_topic')
        robot_base_frame_el = el.find('robot_base_frame')
        dimensions_el = el.find('dimensions')
        gaussian_noise_el = el.find('gaussian_noise')

        return cls(
            odom_frame=odom_frame_el.text if odom_frame_el is not None and odom_frame_el.text is not None else None,
            odom_publish_frequency=float(odom_publish_frequency_el.text) if odom_publish_frequency_el is not None and odom_publish_frequency_el.text is not None else None,
            odom_topic=odom_topic_el.text if odom_topic_el is not None and odom_topic_el.text is not None else None,
            odom_covariance_topic=odom_covariance_topic_el.text if odom_covariance_topic_el is not None and odom_covariance_topic_el.text is not None else None,
            tf_topic=tf_topic_el.text if tf_topic_el is not None and tf_topic_el.text is not None else None,
            robot_base_frame=robot_base_frame_el.text if robot_base_frame_el is not None and robot_base_frame_el.text is not None else None,
            dimensions=int(dimensions_el.text) if dimensions_el is not None and dimensions_el.text is not None else None,
            gaussian_noise=float(gaussian_noise_el.text) if gaussian_noise_el is not None and gaussian_noise_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::OdometryPublisher", filename="gz-sim-odometry-publisher-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('odom_frame', self.odom_frame)
        _add('odom_publish_frequency', self.odom_publish_frequency)
        _add('odom_topic', self.odom_topic)
        _add('odom_covariance_topic', self.odom_covariance_topic)
        _add('tf_topic', self.tf_topic)
        _add('robot_base_frame', self.robot_base_frame)
        _add('dimensions', self.dimensions)
        _add('gaussian_noise', self.gaussian_noise)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        odom_frame_el = el.find('odom_frame')
        odom_publish_frequency_el = el.find('odom_publish_frequency')
        odom_topic_el = el.find('odom_topic')
        odom_covariance_topic_el = el.find('odom_covariance_topic')
        tf_topic_el = el.find('tf_topic')
        robot_base_frame_el = el.find('robot_base_frame')
        dimensions_el = el.find('dimensions')
        gaussian_noise_el = el.find('gaussian_noise')

        return cls(
            odom_frame=odom_frame_el.text if odom_frame_el is not None and odom_frame_el.text is not None else None,
            odom_publish_frequency=float(odom_publish_frequency_el.text) if odom_publish_frequency_el is not None and odom_publish_frequency_el.text is not None else None,
            odom_topic=odom_topic_el.text if odom_topic_el is not None and odom_topic_el.text is not None else None,
            odom_covariance_topic=odom_covariance_topic_el.text if odom_covariance_topic_el is not None and odom_covariance_topic_el.text is not None else None,
            tf_topic=tf_topic_el.text if tf_topic_el is not None and tf_topic_el.text is not None else None,
            robot_base_frame=robot_base_frame_el.text if robot_base_frame_el is not None and robot_base_frame_el.text is not None else None,
            dimensions=int(dimensions_el.text) if dimensions_el is not None and dimensions_el.text is not None else None,
            gaussian_noise=float(gaussian_noise_el.text) if gaussian_noise_el is not None and gaussian_noise_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::OdometryPublisher", filename="gz-sim-odometry-publisher-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('odom_frame', self.odom_frame)
        _add('odom_publish_frequency', self.odom_publish_frequency)
        _add('odom_topic', self.odom_topic)
        _add('odom_covariance_topic', self.odom_covariance_topic)
        _add('tf_topic', self.tf_topic)
        _add('robot_base_frame', self.robot_base_frame)
        _add('dimensions', self.dimensions)
        _add('gaussian_noise', self.gaussian_noise)
            
        return el

    def to_version(self, target_version: str):
        return self
