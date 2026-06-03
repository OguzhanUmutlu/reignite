from ...plugin import Plugin


class FollowActorPlugin(Plugin):
    def __init__(
            self,
            target: str,
            velocity: float = 0.8,
            min_distance: float = 1.2,
            max_distance: float = 4.0,
            animation_x_vel: float = 2.0,
            animation: str | None = None
    ):
        if not target:
            raise ValueError("A 'target' must be specified for the FollowActor plugin.")

        if min_distance < 0 or max_distance < 0:
            raise ValueError("Distances cannot be negative.")

        if min_distance >= max_distance:
            raise ValueError("min_distance must be strictly less than max_distance.")

        super().__init__(
            sdf_version=None,
            filename="gz-sim-follow-actor-system",
            name="gz::sim::systems::FollowActor",
            target=target,
            velocity=velocity,
            min_distance=min_distance,
            max_distance=max_distance,
            animation_x_vel=animation_x_vel,
            animation=animation
        )
