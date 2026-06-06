from xml.etree import ElementTree as ET

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
        self.publish_link_pose = publish_link_pose
        self.publish_nested_model_pose = publish_nested_model_pose
        self.publish_model_pose = publish_model_pose
        self.publish_visual_pose = publish_visual_pose
        self.publish_collision_pose = publish_collision_pose
        self.publish_sensor_pose = publish_sensor_pose
        self.update_frequency = update_frequency
        self.static_publisher = static_publisher
        self.static_update_frequency = static_update_frequency
        self.use_pose_vector_msg = use_pose_vector_msg
        self.topic = topic
        super().__init__(sdf_version=None, filename="gz-sim-pose-publisher-system",
                         name="gz::sim::systems::PosePublisher")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        publish_link_pose_el = el.find('publish_link_pose')
        publish_nested_model_pose_el = el.find('publish_nested_model_pose')
        publish_model_pose_el = el.find('publish_model_pose')
        publish_visual_pose_el = el.find('publish_visual_pose')
        publish_collision_pose_el = el.find('publish_collision_pose')
        publish_sensor_pose_el = el.find('publish_sensor_pose')
        update_frequency_el = el.find('update_frequency')
        static_publisher_el = el.find('static_publisher')
        static_update_frequency_el = el.find('static_update_frequency')
        use_pose_vector_msg_el = el.find('use_pose_vector_msg')
        topic_el = el.find('topic')

        return cls(
            publish_link_pose=publish_link_pose_el.text.lower() == 'true' if publish_link_pose_el is not None and publish_link_pose_el.text is not None else None,
            publish_nested_model_pose=publish_nested_model_pose_el.text.lower() == 'true' if publish_nested_model_pose_el is not None and publish_nested_model_pose_el.text is not None else None,
            publish_model_pose=publish_model_pose_el.text.lower() == 'true' if publish_model_pose_el is not None and publish_model_pose_el.text is not None else None,
            publish_visual_pose=publish_visual_pose_el.text.lower() == 'true' if publish_visual_pose_el is not None and publish_visual_pose_el.text is not None else None,
            publish_collision_pose=publish_collision_pose_el.text.lower() == 'true' if publish_collision_pose_el is not None and publish_collision_pose_el.text is not None else None,
            publish_sensor_pose=publish_sensor_pose_el.text.lower() == 'true' if publish_sensor_pose_el is not None and publish_sensor_pose_el.text is not None else None,
            update_frequency=float(
                update_frequency_el.text) if update_frequency_el is not None and update_frequency_el.text is not None else None,
            static_publisher=static_publisher_el.text.lower() == 'true' if static_publisher_el is not None and static_publisher_el.text is not None else None,
            static_update_frequency=float(
                static_update_frequency_el.text) if static_update_frequency_el is not None and static_update_frequency_el.text is not None else None,
            use_pose_vector_msg=use_pose_vector_msg_el.text.lower() == 'true' if use_pose_vector_msg_el is not None and use_pose_vector_msg_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::PosePublisher",
                        filename="gz-sim-pose-publisher-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('publish_link_pose', self.publish_link_pose)
        _add('publish_nested_model_pose', self.publish_nested_model_pose)
        _add('publish_model_pose', self.publish_model_pose)
        _add('publish_visual_pose', self.publish_visual_pose)
        _add('publish_collision_pose', self.publish_collision_pose)
        _add('publish_sensor_pose', self.publish_sensor_pose)
        _add('update_frequency', self.update_frequency)
        _add('static_publisher', self.static_publisher)
        _add('static_update_frequency', self.static_update_frequency)
        _add('use_pose_vector_msg', self.use_pose_vector_msg)
        _add('topic', self.topic)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        publish_link_pose_el = el.find('publish_link_pose')
        publish_nested_model_pose_el = el.find('publish_nested_model_pose')
        publish_model_pose_el = el.find('publish_model_pose')
        publish_visual_pose_el = el.find('publish_visual_pose')
        publish_collision_pose_el = el.find('publish_collision_pose')
        publish_sensor_pose_el = el.find('publish_sensor_pose')
        update_frequency_el = el.find('update_frequency')
        static_publisher_el = el.find('static_publisher')
        static_update_frequency_el = el.find('static_update_frequency')
        use_pose_vector_msg_el = el.find('use_pose_vector_msg')
        topic_el = el.find('topic')

        return cls(
            publish_link_pose=publish_link_pose_el.text.lower() == 'true' if publish_link_pose_el is not None and publish_link_pose_el.text is not None else None,
            publish_nested_model_pose=publish_nested_model_pose_el.text.lower() == 'true' if publish_nested_model_pose_el is not None and publish_nested_model_pose_el.text is not None else None,
            publish_model_pose=publish_model_pose_el.text.lower() == 'true' if publish_model_pose_el is not None and publish_model_pose_el.text is not None else None,
            publish_visual_pose=publish_visual_pose_el.text.lower() == 'true' if publish_visual_pose_el is not None and publish_visual_pose_el.text is not None else None,
            publish_collision_pose=publish_collision_pose_el.text.lower() == 'true' if publish_collision_pose_el is not None and publish_collision_pose_el.text is not None else None,
            publish_sensor_pose=publish_sensor_pose_el.text.lower() == 'true' if publish_sensor_pose_el is not None and publish_sensor_pose_el.text is not None else None,
            update_frequency=float(
                update_frequency_el.text) if update_frequency_el is not None and update_frequency_el.text is not None else None,
            static_publisher=static_publisher_el.text.lower() == 'true' if static_publisher_el is not None and static_publisher_el.text is not None else None,
            static_update_frequency=float(
                static_update_frequency_el.text) if static_update_frequency_el is not None and static_update_frequency_el.text is not None else None,
            use_pose_vector_msg=use_pose_vector_msg_el.text.lower() == 'true' if use_pose_vector_msg_el is not None and use_pose_vector_msg_el.text is not None else None,
            topic=topic_el.text if topic_el is not None and topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::PosePublisher",
                        filename="gz-sim-pose-publisher-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('publish_link_pose', self.publish_link_pose)
        _add('publish_nested_model_pose', self.publish_nested_model_pose)
        _add('publish_model_pose', self.publish_model_pose)
        _add('publish_visual_pose', self.publish_visual_pose)
        _add('publish_collision_pose', self.publish_collision_pose)
        _add('publish_sensor_pose', self.publish_sensor_pose)
        _add('update_frequency', self.update_frequency)
        _add('static_publisher', self.static_publisher)
        _add('static_update_frequency', self.static_update_frequency)
        _add('use_pose_vector_msg', self.use_pose_vector_msg)
        _add('topic', self.topic)

        return el

    def to_version(self, target_version: str):
        return self
