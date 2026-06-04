from reignite.elements.plugin import Plugin, ParentElement, TextElement


@Plugin.register("gz-sim-trajectory-follower-system", "gz::sim::systems::TrajectoryFollower")
class TrajectoryFollowerPlugin(Plugin):
    class Waypoints(ParentElement):
        def __init__(self, waypoints: list[list[float]]):
            children = [TextElement("waypoint", " ".join(map(str, wp))) for wp in waypoints]
            super().__init__("waypoints", *children)

    class Circle(ParentElement):
        def __init__(self, radius: float):
            super().__init__("circle", [TextElement("radius", str(radius))])

    class Line(ParentElement):
        def __init__(self, direction: float, length: float):
            super().__init__(
                "line",
                [
                    TextElement("direction", str(direction)),
                    TextElement("length", str(length))
                ]
            )

    def __init__(
            self,
            link_name: str,
            waypoints: Waypoints | list[list[float]] | None = None,
            circle: Circle | None = None,
            line: Line | None = None,
            loop: bool | None = None,
            force: float | None = None,
            torque: float | None = None,
            range_tolerance: float | None = None,
            bearing_tolerance: float | None = None,
            zero_vel_on_bearing_reached: bool | None = None,
            topic: str | None = None,
            **kwargs
    ):
        elements = []
        if isinstance(waypoints, list):
            waypoints = TrajectoryFollowerPlugin.Waypoints(waypoints)
        if waypoints is not None:
            elements.append(waypoints)
        if circle is not None:
            elements.append(circle)
        if line is not None:
            elements.append(line)

        super().__init__(
            filename="gz-sim-trajectory-follower-system",
            name="gz::sim::systems::TrajectoryFollower",
            elements=elements,
            link_name=link_name,
            loop=loop,
            force=force,
            torque=torque,
            range_tolerance=range_tolerance,
            bearing_tolerance=bearing_tolerance,
            zero_vel_on_bearing_reached=zero_vel_on_bearing_reached,
            topic=topic,
            **kwargs
        )
