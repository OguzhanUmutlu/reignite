from reignite.elements.plugin import Plugin, ParentElement, TextElement


class TrackedVehicle(Plugin):
    class Track(ParentElement):
        def __init__(
                self,
                side: str,
                link: str,
                velocity_topic: str | None = None,
                center_of_rotation_topic: str | None = None
        ):
            if side not in ("left", "right"):
                raise ValueError("Track side must be 'left' or 'right'")
            super().__init__(
                f"{side}_track",
                TextElement("link", link),
                TextElement("velocity_topic", velocity_topic) if velocity_topic else None,
                TextElement("center_of_rotation_topic", center_of_rotation_topic) if center_of_rotation_topic else None
            )

    class VelocityLimiter(ParentElement):
        def __init__(
                self,
                type: str,
                min_velocity: float | None = None,
                max_velocity: float | None = None,
                min_acceleration: float | None = None,
                max_acceleration: float | None = None,
                min_jerk: float | None = None,
                max_jerk: float | None = None
        ):
            if type not in ("linear", "angular"):
                raise ValueError("VelocityLimiter type must be 'linear' or 'angular'")
            super().__init__(
                f"{type}_velocity",
                TextElement("min_velocity", str(min_velocity)) if min_velocity is not None else None,
                TextElement("max_velocity", str(max_velocity)) if max_velocity is not None else None,
                TextElement("min_acceleration", str(min_acceleration)) if min_acceleration is not None else None,
                TextElement("max_acceleration", str(max_acceleration)) if max_acceleration is not None else None,
                TextElement("min_jerk", str(min_jerk)) if min_jerk is not None else None,
                TextElement("max_jerk", str(max_jerk)) if max_jerk is not None else None
            )

    def __init__(
            self,
            left_track: list[Track] | Track | str | None = None,
            right_track: list[Track] | Track | str | None = None,
            body_link: str | None = None,
            tracks_separation: float | None = None,
            steering_efficiency: float | None = None,
            linear_velocity: VelocityLimiter | None = None,
            angular_velocity: VelocityLimiter | None = None,
            odom_publish_frequency: float | None = None,
            topic: str | None = None,
            odom_topic: str | None = None,
            tf_topic: str | None = None,
            steering_efficiency_topic: str | None = None,
            frame_id: str | None = None,
            child_frame_id: str | None = None,
            debug: bool | None = None,
            **kwargs
    ):
        elements = []
        if left_track is not None:
            if isinstance(left_track, str):
                left_track = [TrackedVehicle.Track("left", left_track)]
            elif isinstance(left_track, TrackedVehicle.Track):
                left_track = [left_track]
            elements.extend(left_track)

        if right_track is not None:
            if isinstance(right_track, str):
                right_track = [TrackedVehicle.Track("right", right_track)]
            elif isinstance(right_track, TrackedVehicle.Track):
                right_track = [right_track]
            elements.extend(right_track)

        if linear_velocity is not None:
            elements.append(linear_velocity)

        if angular_velocity is not None:
            elements.append(angular_velocity)

        super().__init__(
            filename="gz-sim-tracked-vehicle-system",
            name="gz::sim::systems::TrackedVehicle",
            elements=elements,
            body_link=body_link,
            tracks_separation=tracks_separation,
            steering_efficiency=steering_efficiency,
            odom_publish_frequency=odom_publish_frequency,
            topic=topic,
            odom_topic=odom_topic,
            tf_topic=tf_topic,
            steering_efficiency_topic=steering_efficiency_topic,
            frame_id=frame_id,
            child_frame_id=child_frame_id,
            debug=debug,
            **kwargs
        )
