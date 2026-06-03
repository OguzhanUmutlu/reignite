from reignite.elements.plugin import Plugin


class TrackController(Plugin):
    def __init__(
            self,
            link: str,
            velocity_topic: str | None = None,
            center_of_rotation_topic: str | None = None,
            odometry_topic: str | None = None,
            odometry_publish_frequency: float | None = None,
            track_orientation: list[float] | str | None = None,
            max_command_age: float | None = None,
            min_velocity: float | None = None,
            max_velocity: float | None = None,
            min_acceleration: float | None = None,
            max_acceleration: float | None = None,
            min_jerk: float | None = None,
            max_jerk: float | None = None,
            debug: bool | None = None,
            **kwargs
    ):
        super().__init__(
            filename="gz-sim-track-controller-system",
            name="gz::sim::systems::TrackController",
            link=link,
            velocity_topic=velocity_topic,
            center_of_rotation_topic=center_of_rotation_topic,
            odometry_topic=odometry_topic,
            odometry_publish_frequency=odometry_publish_frequency,
            track_orientation=track_orientation,
            max_command_age=max_command_age,
            min_velocity=min_velocity,
            max_velocity=max_velocity,
            min_acceleration=min_acceleration,
            max_acceleration=max_acceleration,
            min_jerk=min_jerk,
            max_jerk=max_jerk,
            debug=debug,
            **kwargs
        )
