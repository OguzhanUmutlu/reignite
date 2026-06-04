from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-tracked-vehicle-system", "gz::sim::systems::TrackedVehicle")
class TrackedVehiclePlugin(Plugin):
    class Track(BaseModel):
        def __init__(
                self,
                side: str,
                link: str | None = None,
                velocity_topic: str | None = None,
                center_of_rotation_topic: str | None = None
        ):
            super().__init__(sdf_version=None)
            self.side = side
            self.link = link
            self.velocity_topic = velocity_topic
            self.center_of_rotation_topic = center_of_rotation_topic

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            tag = el.tag
            side = "left" if tag == "left_track" else "right"
            
            l_el = el.find("link")
            vt_el = el.find("velocity_topic")
            cort_el = el.find("center_of_rotation_topic")
            return cls(
                side=side,
                link=l_el.text if l_el is not None else None,
                velocity_topic=vt_el.text if vt_el is not None else None,
                center_of_rotation_topic=cort_el.text if cort_el is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element(f"{self.side}_track")
            if self.link is not None:
                child = ET.Element("link")
                child.text = str(self.link)
                e.append(child)
            if self.velocity_topic is not None:
                child = ET.Element("velocity_topic")
                child.text = str(self.velocity_topic)
                e.append(child)
            if self.center_of_rotation_topic is not None:
                child = ET.Element("center_of_rotation_topic")
                child.text = str(self.center_of_rotation_topic)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class VelocityLimiter(BaseModel):
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
            super().__init__(sdf_version=None)
            self.type = type
            self.min_velocity = min_velocity
            self.max_velocity = max_velocity
            self.min_acceleration = min_acceleration
            self.max_acceleration = max_acceleration
            self.min_jerk = min_jerk
            self.max_jerk = max_jerk

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            tag = el.tag
            vtype = "linear" if tag == "linear_velocity" else "angular"
            
            minv_el = el.find("min_velocity")
            maxv_el = el.find("max_velocity")
            mina_el = el.find("min_acceleration")
            maxa_el = el.find("max_acceleration")
            minj_el = el.find("min_jerk")
            maxj_el = el.find("max_jerk")
            
            return cls(
                type=vtype,
                min_velocity=float(minv_el.text) if minv_el is not None and minv_el.text is not None else None,
                max_velocity=float(maxv_el.text) if maxv_el is not None and maxv_el.text is not None else None,
                min_acceleration=float(mina_el.text) if mina_el is not None and mina_el.text is not None else None,
                max_acceleration=float(maxa_el.text) if maxa_el is not None and maxa_el.text is not None else None,
                min_jerk=float(minj_el.text) if minj_el is not None and minj_el.text is not None else None,
                max_jerk=float(maxj_el.text) if maxj_el is not None and maxj_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element(f"{self.type}_velocity")
            
            def _add(k, v):
                if v is not None:
                    child = ET.Element(k)
                    child.text = str(v)
                    e.append(child)
                    
            _add("min_velocity", self.min_velocity)
            _add("max_velocity", self.max_velocity)
            _add("min_acceleration", self.min_acceleration)
            _add("max_acceleration", self.max_acceleration)
            _add("min_jerk", self.min_jerk)
            _add("max_jerk", self.max_jerk)
            return e

        def to_version(self, target_version: str):
            return self

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
            debug: bool | None = None
    ):
        if isinstance(left_track, str):
            self.left_track = [TrackedVehiclePlugin.Track("left", left_track)]
        else:
            self.left_track = [left_track] if isinstance(left_track, TrackedVehiclePlugin.Track) else (left_track or [])

        if isinstance(right_track, str):
            self.right_track = [TrackedVehiclePlugin.Track("right", right_track)]
        else:
            self.right_track = [right_track] if isinstance(right_track, TrackedVehiclePlugin.Track) else (right_track or [])

        self.linear_velocity = linear_velocity
        self.angular_velocity = angular_velocity
        self.body_link = body_link
        self.tracks_separation = tracks_separation
        self.steering_efficiency = steering_efficiency
        self.odom_publish_frequency = odom_publish_frequency
        self.topic = topic
        self.odom_topic = odom_topic
        self.tf_topic = tf_topic
        self.steering_efficiency_topic = steering_efficiency_topic
        self.frame_id = frame_id
        self.child_frame_id = child_frame_id
        self.debug = debug

        super().__init__(
            sdf_version=None,
            filename="gz-sim-tracked-vehicle-system",
            name="gz::sim::systems::TrackedVehicle"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        lt_els = el.findall("left_track")
        rt_els = el.findall("right_track")
        lv_el = el.find("linear_velocity")
        av_el = el.find("angular_velocity")
        
        bl_el = el.find("body_link")
        ts_el = el.find("tracks_separation")
        se_el = el.find("steering_efficiency")
        opf_el = el.find("odom_publish_frequency")
        t_el = el.find("topic")
        ot_el = el.find("odom_topic")
        tt_el = el.find("tf_topic")
        set_el = el.find("steering_efficiency_topic")
        fi_el = el.find("frame_id")
        cfi_el = el.find("child_frame_id")
        d_el = el.find("debug")

        return cls(
            left_track=[cls.Track._from_sdf(t, version) for t in lt_els] if lt_els else None,
            right_track=[cls.Track._from_sdf(t, version) for t in rt_els] if rt_els else None,
            linear_velocity=cls.VelocityLimiter._from_sdf(lv_el, version) if lv_el is not None else None,
            angular_velocity=cls.VelocityLimiter._from_sdf(av_el, version) if av_el is not None else None,
            body_link=bl_el.text if bl_el is not None else None,
            tracks_separation=float(ts_el.text) if ts_el is not None and ts_el.text is not None else None,
            steering_efficiency=float(se_el.text) if se_el is not None and se_el.text is not None else None,
            odom_publish_frequency=float(opf_el.text) if opf_el is not None and opf_el.text is not None else None,
            topic=t_el.text if t_el is not None else None,
            odom_topic=ot_el.text if ot_el is not None else None,
            tf_topic=tt_el.text if tt_el is not None else None,
            steering_efficiency_topic=set_el.text if set_el is not None else None,
            frame_id=fi_el.text if fi_el is not None else None,
            child_frame_id=cfi_el.text if cfi_el is not None else None,
            debug=d_el.text.lower() == 'true' if d_el is not None and d_el.text is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::TrackedVehicle", filename="gz-sim-tracked-vehicle-system")
        if self.left_track:
            for t in self.left_track:
                el.append(t.to_sdf(version))
        if self.right_track:
            for t in self.right_track:
                el.append(t.to_sdf(version))
        if self.linear_velocity is not None:
            el.append(self.linear_velocity.to_sdf(version))
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
            
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add("body_link", self.body_link)
        _add("tracks_separation", self.tracks_separation)
        _add("steering_efficiency", self.steering_efficiency)
        _add("odom_publish_frequency", self.odom_publish_frequency)
        _add("topic", self.topic)
        _add("odom_topic", self.odom_topic)
        _add("tf_topic", self.tf_topic)
        _add("steering_efficiency_topic", self.steering_efficiency_topic)
        _add("frame_id", self.frame_id)
        _add("child_frame_id", self.child_frame_id)
        _add("debug", self.debug)
        return el

    def to_version(self, target_version: str):
        if self.left_track:
            for t in self.left_track:
                t.to_version(target_version)
        if self.right_track:
            for t in self.right_track:
                t.to_version(target_version)
        if self.linear_velocity is not None:
            self.linear_velocity.to_version(target_version)
        if self.angular_velocity is not None:
            self.angular_velocity.to_version(target_version)
        return self
