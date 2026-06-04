from reignite.elements.plugin import Plugin


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
        super().__init__(
            filename="gz-sim-odometry-publisher-system",
            name="gz::sim::systems::OdometryPublisher",
            odom_frame=odom_frame,
            odom_publish_frequency=odom_publish_frequency,
            odom_topic=odom_topic,
            odom_covariance_topic=odom_covariance_topic,
            tf_topic=tf_topic,
            robot_base_frame=robot_base_frame,
            dimensions=dimensions,
            gaussian_noise=gaussian_noise,
            **kwargs
        )
