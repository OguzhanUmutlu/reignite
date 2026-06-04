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
            channel_attr = el.get("channel")
            if channel_attr is not None:
                channel = int(channel_attr)
            else:
                channel_el = el.find("channel")
                channel = int(channel_el.text) if channel_el is not None and channel_el.text is not None else None

            _type = el.find("type")
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
                channel=channel,
                type=_type.text if _type is not None and _type.text is not None else None,
                use_force=use_force.text.lower() == "true" if use_force is not None and use_force.text is not None else None,
                joint=joint_name.text if joint_name is not None and joint_name.text is not None else None,
                cmd_topic=cmd_topic.text if cmd_topic is not None and cmd_topic.text is not None else None,
                multiplier=float(multiplier.text) if multiplier is not None and multiplier.text is not None else None,
                offset=float(offset.text) if offset is not None and offset.text is not None else None,
                servo_min=float(servo_min.text) if servo_min is not None and servo_min.text is not None else None,
                servo_max=float(servo_max.text) if servo_max is not None and servo_max.text is not None else None,
                rotor_velocity_slowdown_sim=float(rotor_velocity_slowdown_sim.text) if rotor_velocity_slowdown_sim is not None and rotor_velocity_slowdown_sim.text is not None else None,
                frequency_cutoff=float(frequency_cutoff.text) if frequency_cutoff is not None and frequency_cutoff.text is not None else None,
                sampling_rate=float(sampling_rate.text) if sampling_rate is not None and sampling_rate.text is not None else None,
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
            if self.channel is not None:
                el.set("channel", str(self.channel))

            def _add(k, v):
                if v is not None:
                    child = ET.Element(k)
                    if isinstance(v, bool):
                        child.text = "true" if v else "false"
                    else:
                        child.text = str(v)
                    el.append(child)

            _add("type", self.type)
            _add("useForce", self.use_force)
            _add("jointName", self.joint_name)
            _add("cmd_topic", self.cmd_topic)
            _add("multiplier", self.multiplier)
            _add("offset", self.offset)
            _add("servo_min", self.servo_min)
            _add("servo_max", self.servo_max)
            _add("rotorVelocitySlowdownSim", self.rotor_velocity_slowdown_sim)
            _add("frequencyCutoff", self.frequency_cutoff)
            _add("samplingRate", self.sampling_rate)
            _add("p_gain", self.p_gain)
            _add("i_gain", self.i_gain)
            _add("d_gain", self.d_gain)
            _add("i_max", self.i_max)
            _add("i_min", self.i_min)
            _add("cmd_max", self.cmd_max)
            _add("cmd_min", self.cmd_min)
            
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
            
            def _add(k, v):
                if v is not None:
                    child = ET.Element(k)
                    if isinstance(v, bool):
                        child.text = "true" if v else "false"
                    else:
                        child.text = str(v)
                    el.append(child)

            _add("type", self.type)
            _add("index", self.index)
            _add("topic", self.topic)
            return el

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            pose_transform: _PoseT | None = None,
            gazebo_to_ned: _PoseT | None = None,
            connection_timeout_max_count: int | None = None,
            lock_step: bool | None = None,
            no_time_sync: bool | None = None,
            have_32_channels: bool | None = None,
            imu_name: str | None = None,
            anemometer: str | None = None,
            fdm_addr: str | None = None,
            fdm_port_in: int | None = None,
            controls: list[Control] | None = None,
            sensors: list[Sensor] | None = None
    ):
        self.pose_transform = pose_transform
        self.gazebo_to_ned = gazebo_to_ned
        self.connection_timeout_max_count = connection_timeout_max_count
        self.lock_step = lock_step
        self.no_time_sync = no_time_sync
        self.have_32_channels = have_32_channels
        self.imu_name = imu_name
        self.anemometer = anemometer
        self.fdm_addr = fdm_addr
        self.fdm_port_in = fdm_port_in
        self.controls = controls or []
        self.sensors = sensors or []
        super().__init__(
            sdf_version=None,
            filename="ArduPilotPlugin",
            name="ArduPilotPlugin"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        pose_el = el.find("modelXYZToAirplaneXForwardZDown")
        pose_transform = pose_el.text if pose_el is not None and pose_el.text is not None else None
        
        gazebo_el = el.find("gazeboXYZToNED")
        gazebo_to_ned = gazebo_el.text if gazebo_el is not None and gazebo_el.text is not None else None
        
        ctmc_el = el.find("connectionTimeoutMaxCount")
        connection_timeout_max_count = int(ctmc_el.text) if ctmc_el is not None and ctmc_el.text is not None else None
        
        ls_el = el.find("lock_step")
        lock_step = ls_el.text.lower() == "true" if ls_el is not None and ls_el.text is not None else None
        
        nts_el = el.find("no_time_sync")
        no_time_sync = nts_el.text.lower() == "true" if nts_el is not None and nts_el.text is not None else None
        
        h32_el = el.find("have_32_channels")
        have_32_channels = h32_el.text.lower() == "true" if h32_el is not None and h32_el.text is not None else None
        
        imu_el = el.find("imuName")
        imu_name = imu_el.text if imu_el is not None and imu_el.text is not None else None
        
        ane_el = el.find("anemometer")
        anemometer = ane_el.text if ane_el is not None and ane_el.text is not None else None
        
        fdma_el = el.find("fdm_addr")
        fdm_addr = fdma_el.text if fdma_el is not None and fdma_el.text is not None else None
        
        fdmp_el = el.find("fdm_port_in")
        fdm_port_in = int(fdmp_el.text) if fdmp_el is not None and fdmp_el.text is not None else None
        
        controls = []
        for c_el in el.findall("control"):
            controls.append(cls.Control._from_sdf(c_el, version))
            
        sensors = []
        for s_el in el.findall("sensor"):
            sensors.append(cls.Sensor._from_sdf(s_el, version))

        return cls(
            pose_transform=pose_transform,
            gazebo_to_ned=gazebo_to_ned,
            connection_timeout_max_count=connection_timeout_max_count,
            lock_step=lock_step,
            no_time_sync=no_time_sync,
            have_32_channels=have_32_channels,
            imu_name=imu_name,
            anemometer=anemometer,
            fdm_addr=fdm_addr,
            fdm_port_in=fdm_port_in,
            controls=controls,
            sensors=sensors
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = super().to_sdf(version)
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
        
        if self.pose_transform is not None:
            _add("modelXYZToAirplaneXForwardZDown", _pose(self.pose_transform).to_sdf())
        if self.gazebo_to_ned is not None:
            _add("gazeboXYZToNED", _pose(self.gazebo_to_ned).to_sdf())
            
        _add("connectionTimeoutMaxCount", self.connection_timeout_max_count)
        _add("lock_step", self.lock_step)
        _add("no_time_sync", self.no_time_sync)
        _add("have_32_channels", self.have_32_channels)
        _add("imuName", self.imu_name)
        _add("anemometer", self.anemometer)
        _add("fdm_addr", self.fdm_addr)
        _add("fdm_port_in", self.fdm_port_in)
        
        for c in self.controls:
            el.append(c.to_sdf(version))
            
        for s in self.sensors:
            el.append(s.to_sdf(version))
            
        return el

    def to_version(self, target_version: str):
        return self
