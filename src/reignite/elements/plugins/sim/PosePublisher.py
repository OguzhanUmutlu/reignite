from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-pose-publisher-system", "gz::sim::systems::PosePublisher")
class PosePublisherPlugin(Plugin):
    def __init__(
            self,
            publish_link_pose: bool | None = None,
            publish_nested_model_pose: bool | None = None,
            publish_model_pose: bool | None = None,
            publish_visual_pose: bool | None = None,
            publish_collision_pose: bool | None = None,
            publish_sensor_pose: bool | None = None,
            update_frequency: float | None = None,
            static_publisher: bool | None = None,
            static_update_frequency: float | None = None,
            use_pose_vector_msg: bool | None = None,
            topic: str | None = None,
            **kwargs
    ):
        super().__init__(
            filename="gz-sim-pose-publisher-system",
            name="gz::sim::systems::PosePublisher",
            publish_link_pose=publish_link_pose,
            publish_nested_model_pose=publish_nested_model_pose,
            publish_model_pose=publish_model_pose,
            publish_visual_pose=publish_visual_pose,
            publish_collision_pose=publish_collision_pose,
            publish_sensor_pose=publish_sensor_pose,
            update_frequency=update_frequency,
            static_publisher=static_publisher,
            static_update_frequency=static_update_frequency,
            use_pose_vector_msg=use_pose_vector_msg,
            topic=topic,
            **kwargs
        )
