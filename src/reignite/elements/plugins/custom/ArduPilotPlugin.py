from xml.etree import ElementTree as ET

from reignite import BaseModel
from ...joint import Joint
from ...plugin import Plugin
from ....utils.pose import _PoseT, _pose


@Plugin.register("ArduPilotPlugin", "ArduPilotPlugin")
class ArduPilotPlugin(Plugin):
    class Control(BaseModel):
        def __init__(
                self,
                channel: int | None = None,
                type: str | None = None,
                use_force: bool | None = None,
                joint: str | Joint | None = None,
                cmd_topic: str | None = None,
                multiplier: float | None = None,
                offset: float | None = None,
                servo_min: float | None = None,
                servo_max: float | None = None,
                rotor_velocity_slowdown_sim: float | None = None,
                frequency_cutoff: float | None = None,
                sampling_rate: float | None = None,
                p_gain: float | None = None,
                i_gain: float | None = None,
                d_gain: float | None = None,
                i_max: float | None = None,
                i_min: float | None = None,
                cmd_max: float | None = None,
                cmd_min: float | None = None,
        ):
            """
            Defaults:
            type: "VELOCITY"
            use_force: True
            multiplier: 1.0
            offset: 0.0
            servo_min: 1000.0
            servo_max: 2000.0
            rotor_velocity_slowdown_sim: 1.0
            frequency_cutoff: 5.0
            sampling_rate: 0.2
            p_gain: 0.1
            i_gain: 0.0
            d_gain: 0.0
            i_max: 0.0
            i_min: 0.0
            cmd_max: 1.0
            cmd_min: -1.0
            """
            self.channel = channel
            self.type = type
            self.use_force = use_force
            if isinstance(joint, Joint):
                joint = joint.name
            self.joint_name = joint
            self.cmd_topic = cmd_topic
            self.multiplier = multiplier
            self.offset = offset
            self.servo_min = servo_min
            self.servo_max = servo_max
            self.rotor_velocity_slowdown_sim = rotor_velocity_slowdown_sim
            self.frequency_cutoff = frequency_cutoff
            self.sampling_rate = sampling_rate
            self.p_gain = p_gain
            self.i_gain = i_gain
            self.d_gain = d_gain
            self.i_max = i_max
            self.i_min = i_min
            self.cmd_max = cmd_max
            self.cmd_min = cmd_min
            super().__init__(sdf_version=None)

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            channel = el.find("channel")
            _type = el.find("type"),
            use_force = el.find("useForce")
            joint_name = el.find("jointName")
            cmd_topic = el.find("cmd_topic")
            multiplier = el.find("multiplier")
            offset = el.find("offset")
            servo_min = el.find("servo_min")
            servo_max = el.find("servo_max")
            rotor_velocity_slowdown_sim = el.find("rotorVelocitySlowdownSim")
            frequency_cutoff = el.find("frequencyCutoff")
            sampling_rate = el.find("samplingRate")
            p_gain = el.find("p_gain")
            i_gain = el.find("i_gain")
            d_gain = el.find("d_gain")
            i_max = el.find("i_max")
            i_min = el.find("i_min")
            cmd_max = el.find("cmd_max")
            cmd_min = el.find("cmd_min")
            return cls(
                channel=int(channel.text) if channel is not None and channel.text is not None else None,
                type=_type.text if _type is not None and _type.text is not None else None,
                use_force=use_force.text.lower() == "true" if use_force is not None and use_force.text is not None else True,
                joint=joint_name.text if joint_name is not None and joint_name.text is not None else None,
                cmd_topic=cmd_topic.text if cmd_topic is not None and cmd_topic.text is not None else None,
                multiplier=float(multiplier.text) if multiplier is not None and multiplier.text is not None else None,
                offset=float(offset.text) if offset is not None and offset.text is not None else None,
                servo_min=float(servo_min.text) if servo_min is not None and servo_min.text is not None else None,
                servo_max=float(servo_max.text) if servo_max is not None and servo_max.text is not None else None,
                rotor_velocity_slowdown_sim=float(
                    rotor_velocity_slowdown_sim.text) if rotor_velocity_slowdown_sim is not None and rotor_velocity_slowdown_sim.text is not None else None,
                frequency_cutoff=float(
                    frequency_cutoff.text) if frequency_cutoff is not None and frequency_cutoff.text is not None else None,
                sampling_rate=float(
                    sampling_rate.text) if sampling_rate is not None and sampling_rate.text is not None else None,
                p_gain=float(p_gain.text) if p_gain is not None and p_gain.text is not None else None,
                i_gain=float(i_gain.text) if i_gain is not None and i_gain.text is not None else None,
                d_gain=float(d_gain.text) if d_gain is not None and d_gain.text is not None else None,
                i_max=float(i_max.text) if i_max is not None and i_max.text is not None else None,
                i_min=float(i_min.text) if i_min is not None and i_min.text is not None else None,
                cmd_max=float(cmd_max.text) if cmd_max is not None and cmd_max.text is not None else None,
                cmd_min=float(cmd_min.text) if cmd_min is not None and cmd_min.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            el = ET.Element("control")
            for key, value in self.__dict__.items():
                if key == "joint":
                    child = ET.Element("jointName")
                    child.text = str(value)
                    el.append(child)
                    continue
                if key == "channel" and value is not None:
                    child = ET.Element("channel")
                    child.text = str(value)
                    el.append(child)
                if value is not None:
                    child = ET.Element(key)
                    child.text = str(value)
                    el.append(child)
            return el

        def to_version(self, target_version: str):
            return self

    class Sensor(BaseModel):
        def __init__(self, type=None, index=None, topic=None):
            self.type = type
            self.index = index
            self.topic = topic
            super().__init__(sdf_version=None)

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            type_el = el.find("type")
            index_el = el.find("index")
            topic_el = el.find("topic")
            return cls(
                type=type_el.text if type_el is not None and type_el.text is not None else None,
                index=int(index_el.text) if index_el is not None and index_el.text is not None else None,
                topic=topic_el.text if topic_el is not None and topic_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            el = ET.Element("sensor")
            for key, value in self.__dict__.items():
                if value is not None:
                    child = ET.Element(key)
                    child.text = str(value)
                    el.append(child)
            return el

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            pose_transform: _PoseT | None = None,
            gazebo_to_ned: _PoseT | None = None,
            connection_timeout_max_count=None,
            lock_step=None,
            no_time_sync=None,
            have_32_channels=None,
            imu_name=None,
            anemometer=None,
            fdm_addr=None,
            fdm_port_in=None,
            controls: list[Control] | None = None,
            sensors: list[Sensor] | None = None
    ):
        """
        Defaults:
        pose_transform: "0 0 0 3.14159 0 0"
        gazebo_to_ned: "0 0 0 3.14159 0 0"
        connection_timeout_max_count: 10
        lock_step: False
        no_time_sync: True
        have_32_channels: False
        imu_name: "imu_sensor"
        anemometer: ""
        fdm_addr: "127.0.0.1"
        fdm_port_in: 9002
        """
        super().__init__(
            sdf_version=None,
            filename="ArduPilotPlugin",
            name="ArduPilotPlugin",
            elements=[*(controls or []), *(sensors or [])],
            modelXYZToAirplaneXForwardZDown=_pose(pose_transform).to_sdf() if pose_transform is not None else None,
            gazeboXYZToNED=_pose(gazebo_to_ned).to_sdf() if gazebo_to_ned is not None else None,
            connectionTimeoutMaxCount=connection_timeout_max_count,
            lock_step=lock_step,
            no_time_sync=no_time_sync,
            have_32_channels=have_32_channels,
            imuName=imu_name,
            anemometer=anemometer,
            fdm_addr=fdm_addr,
            fdm_port_in=fdm_port_in,
        )
