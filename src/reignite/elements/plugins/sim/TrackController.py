from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-track-controller-system", "gz::sim::systems::TrackController")
class TrackControllerPlugin(Plugin):
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
        self.link = link
        self.velocity_topic = velocity_topic
        self.center_of_rotation_topic = center_of_rotation_topic
        self.odometry_topic = odometry_topic
        self.odometry_publish_frequency = odometry_publish_frequency
        self.track_orientation = track_orientation
        self.max_command_age = max_command_age
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.min_acceleration = min_acceleration
        self.max_acceleration = max_acceleration
        self.min_jerk = min_jerk
        self.max_jerk = max_jerk
        self.debug = debug
        super().__init__(sdf_version=None, filename="gz-sim-track-controller-system", name="gz::sim::systems::TrackController")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_el = el.find('link')
        velocity_topic_el = el.find('velocity_topic')
        center_of_rotation_topic_el = el.find('center_of_rotation_topic')
        odometry_topic_el = el.find('odometry_topic')
        odometry_publish_frequency_el = el.find('odometry_publish_frequency')
        track_orientation_els = el.findall('track_orientation')
        track_orientation_vals = [e.text for e in track_orientation_els if e.text is not None] if track_orientation_els else None
        max_command_age_el = el.find('max_command_age')
        min_velocity_el = el.find('min_velocity')
        max_velocity_el = el.find('max_velocity')
        min_acceleration_el = el.find('min_acceleration')
        max_acceleration_el = el.find('max_acceleration')
        min_jerk_el = el.find('min_jerk')
        max_jerk_el = el.find('max_jerk')
        debug_el = el.find('debug')

        return cls(
            link=link_el.text if link_el is not None and link_el.text is not None else None,
            velocity_topic=velocity_topic_el.text if velocity_topic_el is not None and velocity_topic_el.text is not None else None,
            center_of_rotation_topic=center_of_rotation_topic_el.text if center_of_rotation_topic_el is not None and center_of_rotation_topic_el.text is not None else None,
            odometry_topic=odometry_topic_el.text if odometry_topic_el is not None and odometry_topic_el.text is not None else None,
            odometry_publish_frequency=float(odometry_publish_frequency_el.text) if odometry_publish_frequency_el is not None and odometry_publish_frequency_el.text is not None else None,
            track_orientation=track_orientation_vals,
            max_command_age=float(max_command_age_el.text) if max_command_age_el is not None and max_command_age_el.text is not None else None,
            min_velocity=float(min_velocity_el.text) if min_velocity_el is not None and min_velocity_el.text is not None else None,
            max_velocity=float(max_velocity_el.text) if max_velocity_el is not None and max_velocity_el.text is not None else None,
            min_acceleration=float(min_acceleration_el.text) if min_acceleration_el is not None and min_acceleration_el.text is not None else None,
            max_acceleration=float(max_acceleration_el.text) if max_acceleration_el is not None and max_acceleration_el.text is not None else None,
            min_jerk=float(min_jerk_el.text) if min_jerk_el is not None and min_jerk_el.text is not None else None,
            max_jerk=float(max_jerk_el.text) if max_jerk_el is not None and max_jerk_el.text is not None else None,
            debug=debug_el.text.lower() == 'true' if debug_el is not None and debug_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::TrackController", filename="gz-sim-track-controller-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link', self.link)
        _add('velocity_topic', self.velocity_topic)
        _add('center_of_rotation_topic', self.center_of_rotation_topic)
        _add('odometry_topic', self.odometry_topic)
        _add('odometry_publish_frequency', self.odometry_publish_frequency)
        if self.track_orientation is not None:
            for v in (self.track_orientation if isinstance(self.track_orientation, list) else [self.track_orientation]):
                _add('track_orientation', v)
        _add('max_command_age', self.max_command_age)
        _add('min_velocity', self.min_velocity)
        _add('max_velocity', self.max_velocity)
        _add('min_acceleration', self.min_acceleration)
        _add('max_acceleration', self.max_acceleration)
        _add('min_jerk', self.min_jerk)
        _add('max_jerk', self.max_jerk)
        _add('debug', self.debug)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_el = el.find('link')
        velocity_topic_el = el.find('velocity_topic')
        center_of_rotation_topic_el = el.find('center_of_rotation_topic')
        odometry_topic_el = el.find('odometry_topic')
        odometry_publish_frequency_el = el.find('odometry_publish_frequency')
        track_orientation_els = el.findall('track_orientation')
        track_orientation_vals = [e.text for e in track_orientation_els if e.text is not None] if track_orientation_els else None
        max_command_age_el = el.find('max_command_age')
        min_velocity_el = el.find('min_velocity')
        max_velocity_el = el.find('max_velocity')
        min_acceleration_el = el.find('min_acceleration')
        max_acceleration_el = el.find('max_acceleration')
        min_jerk_el = el.find('min_jerk')
        max_jerk_el = el.find('max_jerk')
        debug_el = el.find('debug')

        return cls(
            link=link_el.text if link_el is not None and link_el.text is not None else None,
            velocity_topic=velocity_topic_el.text if velocity_topic_el is not None and velocity_topic_el.text is not None else None,
            center_of_rotation_topic=center_of_rotation_topic_el.text if center_of_rotation_topic_el is not None and center_of_rotation_topic_el.text is not None else None,
            odometry_topic=odometry_topic_el.text if odometry_topic_el is not None and odometry_topic_el.text is not None else None,
            odometry_publish_frequency=float(odometry_publish_frequency_el.text) if odometry_publish_frequency_el is not None and odometry_publish_frequency_el.text is not None else None,
            track_orientation=track_orientation_vals,
            max_command_age=float(max_command_age_el.text) if max_command_age_el is not None and max_command_age_el.text is not None else None,
            min_velocity=float(min_velocity_el.text) if min_velocity_el is not None and min_velocity_el.text is not None else None,
            max_velocity=float(max_velocity_el.text) if max_velocity_el is not None and max_velocity_el.text is not None else None,
            min_acceleration=float(min_acceleration_el.text) if min_acceleration_el is not None and min_acceleration_el.text is not None else None,
            max_acceleration=float(max_acceleration_el.text) if max_acceleration_el is not None and max_acceleration_el.text is not None else None,
            min_jerk=float(min_jerk_el.text) if min_jerk_el is not None and min_jerk_el.text is not None else None,
            max_jerk=float(max_jerk_el.text) if max_jerk_el is not None and max_jerk_el.text is not None else None,
            debug=debug_el.text.lower() == 'true' if debug_el is not None and debug_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::TrackController", filename="gz-sim-track-controller-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link', self.link)
        _add('velocity_topic', self.velocity_topic)
        _add('center_of_rotation_topic', self.center_of_rotation_topic)
        _add('odometry_topic', self.odometry_topic)
        _add('odometry_publish_frequency', self.odometry_publish_frequency)
        if self.track_orientation is not None:
            for v in (self.track_orientation if isinstance(self.track_orientation, list) else [self.track_orientation]):
                _add('track_orientation', v)
        _add('max_command_age', self.max_command_age)
        _add('min_velocity', self.min_velocity)
        _add('max_velocity', self.max_velocity)
        _add('min_acceleration', self.min_acceleration)
        _add('max_acceleration', self.max_acceleration)
        _add('min_jerk', self.min_jerk)
        _add('max_jerk', self.max_jerk)
        _add('debug', self.debug)
            
        return el

    def to_version(self, target_version: str):
        return self
