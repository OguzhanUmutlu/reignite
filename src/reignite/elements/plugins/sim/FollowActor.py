from xml.etree import ElementTree as ET
from ...plugin import Plugin


@Plugin.register("gz-sim-follow-actor-system", "gz::sim::systems::FollowActor")
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

        self.target = target
        self.velocity = velocity
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.animation_x_vel = animation_x_vel
        self.animation = animation
        super().__init__(sdf_version=None, filename="gz-sim-follow-actor-system", name="gz::sim::systems::FollowActor")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        target_el = el.find('target')
        velocity_el = el.find('velocity')
        min_distance_el = el.find('min_distance')
        max_distance_el = el.find('max_distance')
        animation_x_vel_el = el.find('animation_x_vel')
        animation_el = el.find('animation')

        return cls(
            target=target_el.text if target_el is not None and target_el.text is not None else None,
            velocity=float(velocity_el.text) if velocity_el is not None and velocity_el.text is not None else None,
            min_distance=float(min_distance_el.text) if min_distance_el is not None and min_distance_el.text is not None else None,
            max_distance=float(max_distance_el.text) if max_distance_el is not None and max_distance_el.text is not None else None,
            animation_x_vel=float(animation_x_vel_el.text) if animation_x_vel_el is not None and animation_x_vel_el.text is not None else None,
            animation=animation_el.text if animation_el is not None and animation_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::FollowActor", filename="gz-sim-follow-actor-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('target', self.target)
        _add('velocity', self.velocity)
        _add('min_distance', self.min_distance)
        _add('max_distance', self.max_distance)
        _add('animation_x_vel', self.animation_x_vel)
        _add('animation', self.animation)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        target_el = el.find('target')
        velocity_el = el.find('velocity')
        min_distance_el = el.find('min_distance')
        max_distance_el = el.find('max_distance')
        animation_x_vel_el = el.find('animation_x_vel')
        animation_el = el.find('animation')

        return cls(
            target=target_el.text if target_el is not None and target_el.text is not None else None,
            velocity=float(velocity_el.text) if velocity_el is not None and velocity_el.text is not None else None,
            min_distance=float(min_distance_el.text) if min_distance_el is not None and min_distance_el.text is not None else None,
            max_distance=float(max_distance_el.text) if max_distance_el is not None and max_distance_el.text is not None else None,
            animation_x_vel=float(animation_x_vel_el.text) if animation_x_vel_el is not None and animation_x_vel_el.text is not None else None,
            animation=animation_el.text if animation_el is not None and animation_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::FollowActor", filename="gz-sim-follow-actor-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('target', self.target)
        _add('velocity', self.velocity)
        _add('min_distance', self.min_distance)
        _add('max_distance', self.max_distance)
        _add('animation_x_vel', self.animation_x_vel)
        _add('animation', self.animation)
            
        return el

    def to_version(self, target_version: str):
        return self
