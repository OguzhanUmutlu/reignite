from xml.etree import ElementTree as ET

from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-elevator-system", "gz::sim::systems::Elevator")
class ElevatorPlugin(Plugin):
    def __init__(
            self,
            cabin_joint: str | Joint = "lift",
            update_rate: float = 10.0,
            floor_link_prefix: str = "floor_",
            door_joint_prefix: str = "door_",
            open_door_wait_duration: float = 5.0,
            state_topic: str | None = None,
            state_publish_rate: float = 5.0,
            cmd_topic: str | None = None
    ):
        def _get_name(joint):
            if joint is None:
                return None
            return joint.name if isinstance(joint, Joint) else joint

        self.cabin_joint = _get_name(cabin_joint)
        self.update_rate = update_rate
        self.floor_link_prefix = floor_link_prefix
        self.door_joint_prefix = door_joint_prefix
        self.open_door_wait_duration = open_door_wait_duration
        self.state_topic = state_topic
        self.state_publish_rate = state_publish_rate
        self.cmd_topic = cmd_topic
        super().__init__(sdf_version=None, filename="gz-sim-elevator-system", name="gz::sim::systems::Elevator")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        cabin_joint_el = el.find('cabin_joint')
        update_rate_el = el.find('update_rate')
        floor_link_prefix_el = el.find('floor_link_prefix')
        door_joint_prefix_el = el.find('door_joint_prefix')
        open_door_wait_duration_el = el.find('open_door_wait_duration')
        state_topic_el = el.find('state_topic')
        state_publish_rate_el = el.find('state_publish_rate')
        cmd_topic_el = el.find('cmd_topic')

        return cls(
            cabin_joint=int(
                cabin_joint_el.text) if cabin_joint_el is not None and cabin_joint_el.text is not None else None,
            update_rate=float(
                update_rate_el.text) if update_rate_el is not None and update_rate_el.text is not None else None,
            floor_link_prefix=floor_link_prefix_el.text if floor_link_prefix_el is not None and floor_link_prefix_el.text is not None else None,
            door_joint_prefix=door_joint_prefix_el.text if door_joint_prefix_el is not None and door_joint_prefix_el.text is not None else None,
            open_door_wait_duration=float(
                open_door_wait_duration_el.text) if open_door_wait_duration_el is not None and open_door_wait_duration_el.text is not None else None,
            state_topic=state_topic_el.text if state_topic_el is not None and state_topic_el.text is not None else None,
            state_publish_rate=float(
                state_publish_rate_el.text) if state_publish_rate_el is not None and state_publish_rate_el.text is not None else None,
            cmd_topic=cmd_topic_el.text if cmd_topic_el is not None and cmd_topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Elevator",
                        filename="gz-sim-elevator-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('cabin_joint', self.cabin_joint)
        _add('update_rate', self.update_rate)
        _add('floor_link_prefix', self.floor_link_prefix)
        _add('door_joint_prefix', self.door_joint_prefix)
        _add('open_door_wait_duration', self.open_door_wait_duration)
        _add('state_topic', self.state_topic)
        _add('state_publish_rate', self.state_publish_rate)
        _add('cmd_topic', self.cmd_topic)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        cabin_joint_el = el.find('cabin_joint')
        update_rate_el = el.find('update_rate')
        floor_link_prefix_el = el.find('floor_link_prefix')
        door_joint_prefix_el = el.find('door_joint_prefix')
        open_door_wait_duration_el = el.find('open_door_wait_duration')
        state_topic_el = el.find('state_topic')
        state_publish_rate_el = el.find('state_publish_rate')
        cmd_topic_el = el.find('cmd_topic')

        return cls(
            cabin_joint=int(
                cabin_joint_el.text) if cabin_joint_el is not None and cabin_joint_el.text is not None else None,
            update_rate=float(
                update_rate_el.text) if update_rate_el is not None and update_rate_el.text is not None else None,
            floor_link_prefix=floor_link_prefix_el.text if floor_link_prefix_el is not None and floor_link_prefix_el.text is not None else None,
            door_joint_prefix=door_joint_prefix_el.text if door_joint_prefix_el is not None and door_joint_prefix_el.text is not None else None,
            open_door_wait_duration=float(
                open_door_wait_duration_el.text) if open_door_wait_duration_el is not None and open_door_wait_duration_el.text is not None else None,
            state_topic=state_topic_el.text if state_topic_el is not None and state_topic_el.text is not None else None,
            state_publish_rate=float(
                state_publish_rate_el.text) if state_publish_rate_el is not None and state_publish_rate_el.text is not None else None,
            cmd_topic=cmd_topic_el.text if cmd_topic_el is not None and cmd_topic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Elevator",
                        filename="gz-sim-elevator-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('cabin_joint', self.cabin_joint)
        _add('update_rate', self.update_rate)
        _add('floor_link_prefix', self.floor_link_prefix)
        _add('door_joint_prefix', self.door_joint_prefix)
        _add('open_door_wait_duration', self.open_door_wait_duration)
        _add('state_topic', self.state_topic)
        _add('state_publish_rate', self.state_publish_rate)
        _add('cmd_topic', self.cmd_topic)

        return el

    def to_version(self, target_version: str):
        return self
