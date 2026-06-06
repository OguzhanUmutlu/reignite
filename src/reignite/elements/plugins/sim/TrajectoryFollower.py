from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-trajectory-follower-system", "gz::sim::systems::TrajectoryFollower")
class TrajectoryFollowerPlugin(Plugin):
    class Waypoints(BaseModel):
        def __init__(self, waypoints: list[list[float]] | None = None):
            super().__init__(sdf_version=None)
            self.waypoints = waypoints or []

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            wp_els = el.findall("waypoint")
            waypoints = []
            for wp in wp_els:
                if wp.text:
                    parts = wp.text.split()
                    waypoints.append([float(p) for p in parts])
            return cls(waypoints=waypoints if waypoints else None)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("waypoints")
            if self.waypoints:
                for wp in self.waypoints:
                    child = ET.Element("waypoint")
                    child.text = " ".join(map(str, wp))
                    e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class Circle(BaseModel):
        def __init__(self, radius: float | None = None):
            super().__init__(sdf_version=None)
            self.radius = radius

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            r_el = el.find("radius")
            return cls(radius=float(r_el.text) if r_el is not None and r_el.text is not None else None)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("circle")
            if self.radius is not None:
                child = ET.Element("radius")
                child.text = str(self.radius)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class Line(BaseModel):
        def __init__(self, direction: float | None = None, length: float | None = None):
            super().__init__(sdf_version=None)
            self.direction = direction
            self.length = length

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            d_el = el.find("direction")
            l_el = el.find("length")
            return cls(
                direction=float(d_el.text) if d_el is not None and d_el.text is not None else None,
                length=float(l_el.text) if l_el is not None and l_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("line")
            if self.direction is not None:
                child = ET.Element("direction")
                child.text = str(self.direction)
                e.append(child)
            if self.length is not None:
                child = ET.Element("length")
                child.text = str(self.length)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            link_name: str | None = None,
            waypoints: Waypoints | list[list[float]] | None = None,
            circle: Circle | None = None,
            line: Line | None = None,
            loop: bool | None = None,
            force: float | None = None,
            torque: float | None = None,
            range_tolerance: float | None = None,
            bearing_tolerance: float | None = None,
            zero_vel_on_bearing_reached: bool | None = None,
            topic: str | None = None
    ):
        self.link_name = link_name
        self.waypoints = TrajectoryFollowerPlugin.Waypoints(waypoints) if isinstance(waypoints, list) else waypoints
        self.circle = circle
        self.line = line
        self.loop = loop
        self.force = force
        self.torque = torque
        self.range_tolerance = range_tolerance
        self.bearing_tolerance = bearing_tolerance
        self.zero_vel_on_bearing_reached = zero_vel_on_bearing_reached
        self.topic = topic

        super().__init__(
            sdf_version=None,
            filename="gz-sim-trajectory-follower-system",
            name="gz::sim::systems::TrajectoryFollower"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        ln_el = el.find("link_name")
        wp_el = el.find("waypoints")
        c_el = el.find("circle")
        l_el = el.find("line")
        lp_el = el.find("loop")
        f_el = el.find("force")
        t_el = el.find("torque")
        rt_el = el.find("range_tolerance")
        bt_el = el.find("bearing_tolerance")
        zv_el = el.find("zero_vel_on_bearing_reached")
        top_el = el.find("topic")

        return cls(
            link_name=ln_el.text if ln_el is not None else None,
            waypoints=cls.Waypoints._from_sdf(wp_el, version) if wp_el is not None else None,
            circle=cls.Circle._from_sdf(c_el, version) if c_el is not None else None,
            line=cls.Line._from_sdf(l_el, version) if l_el is not None else None,
            loop=lp_el.text.lower() == 'true' if lp_el is not None and lp_el.text is not None else None,
            force=float(f_el.text) if f_el is not None and f_el.text is not None else None,
            torque=float(t_el.text) if t_el is not None and t_el.text is not None else None,
            range_tolerance=float(rt_el.text) if rt_el is not None and rt_el.text is not None else None,
            bearing_tolerance=float(bt_el.text) if bt_el is not None and bt_el.text is not None else None,
            zero_vel_on_bearing_reached=zv_el.text.lower() == 'true' if zv_el is not None and zv_el.text is not None else None,
            topic=top_el.text if top_el is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::TrajectoryFollower",
                        filename="gz-sim-trajectory-follower-system")
        if self.waypoints is not None:
            el.append(self.waypoints.to_sdf(version))
        if self.circle is not None:
            el.append(self.circle.to_sdf(version))
        if self.line is not None:
            el.append(self.line.to_sdf(version))

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add("link_name", self.link_name)
        _add("loop", self.loop)
        _add("force", self.force)
        _add("torque", self.torque)
        _add("range_tolerance", self.range_tolerance)
        _add("bearing_tolerance", self.bearing_tolerance)
        _add("zero_vel_on_bearing_reached", self.zero_vel_on_bearing_reached)
        _add("topic", self.topic)

        return el

    def to_version(self, target_version: str):
        if self.waypoints is not None:
            self.waypoints.to_version(target_version)
        if self.circle is not None:
            self.circle.to_version(target_version)
        if self.line is not None:
            self.line.to_version(target_version)
        return self
