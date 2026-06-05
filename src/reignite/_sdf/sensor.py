### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import _PoseT, _pose
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.air_pressure import AirPressure
    from ..elements.air_speed import AirSpeed
    from ..elements.altimeter import Altimeter
    from ..elements.camera import Camera
    from ..elements.contact import Contact
    from ..elements.force_torque import ForceTorque
    from ..elements.frame import Frame
    from ..elements.gps import Gps
    from ..elements.imu import Imu
    from ..elements.lidar import Lidar
    from ..elements.logical_camera import LogicalCamera
    from ..elements.magnetometer import Magnetometer
    from ..elements.navsat import Navsat
    from ..elements.plugin import Plugin
    from ..elements.pose import Pose
    from ..elements.ray import Ray
    from ..elements.rfid import Rfid
    from ..elements.rfidtag import Rfidtag
    from ..elements.sonar import Sonar
    from ..elements.transceiver import Transceiver

def _parse_pose(raw: str) -> _PoseT | SDFError:
    try:
        return _pose(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Sensor(BaseModel):
    class Origin(BaseModel):
        def __init__(self, sdf_version: str | None = None, pose: _PoseT | None = None):
            super().__init__(sdf_version)
            self.pose = _pose(pose) if pose is not None else None

        def to_version(self, target_version: str) -> "Sensor.Origin":
            kwargs: dict = {"sdf_version": target_version, "pose": self.pose}
            return Sensor.Origin(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("origin")
            if self.pose is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("pose")
                    _c_tmp.text = str(self.pose)
                    el.append(_c_tmp)
                else:
                    el.set("pose", str(self.pose))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Sensor.Origin | SDFError":
            _raw_pose = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("pose")
                if _c_tmp is not None: _raw_pose = _c_tmp.text
            else:
                _raw_pose = el.get("pose")
            if _raw_pose is not None:
                _pose = _parse_pose(_raw_pose)
                if isinstance(_pose, SDFError):
                    return _pose.extend("@pose")
            else:
                _pose = None
            return cls(sdf_version=version, pose=_pose)

    def __init__(
        self,
        sdf_version: str | None = None,
        air_pressure: "AirPressure" = None,
        air_speed: "AirSpeed" = None,
        altimeter: "Altimeter" = None,
        always_on: bool | None = None,
        camera: "Camera" = None,
        contact: "Contact" = None,
        enable_metrics: bool | None = None,
        force_torque: "ForceTorque" = None,
        frame_id: str | None = None,
        frames: List["Frame"] = None,
        gps: "Gps" = None,
        imu: "Imu" = None,
        lidar: "Lidar" = None,
        logical_camera: "LogicalCamera" = None,
        magnetometer: "Magnetometer" = None,
        name: str | None = None,
        navsat: "Navsat" = None,
        origin: "Sensor.Origin" = None,
        plugins: List["Plugin"] = None,
        pose: "Pose" = None,
        ray: "Ray" = None,
        rfid: "Rfidtag" = None,
        rfidtag: "Rfid" = None,
        sonar: "Sonar" = None,
        topic: str | None = None,
        transceiver: "Transceiver" = None,
        type: str | None = None,
        update_rate: float | None = None,
        visualize: bool | None = None
    ):
        super().__init__(sdf_version)
        self.air_pressure = air_pressure
        self.air_speed = air_speed
        self.altimeter = altimeter
        self.always_on = always_on
        self.camera = camera
        self.contact = contact
        self.enable_metrics = enable_metrics
        self.force_torque = force_torque
        self.frame_id = frame_id
        self.frames = frames or []
        self.gps = gps
        self.imu = imu
        self.lidar = lidar
        self.logical_camera = logical_camera
        self.magnetometer = magnetometer
        self.name = name
        self.navsat = navsat
        self.origin = origin
        self.plugins = plugins or []
        self.pose = pose
        self.ray = ray
        self.rfid = rfid
        self.rfidtag = rfidtag
        self.sonar = sonar
        self.topic = topic
        self.transceiver = transceiver
        self.type = type
        self.update_rate = update_rate
        self.visualize = visualize
        if self.air_pressure is not None and hasattr(self.air_pressure, 'to_version'):
            if getattr(self.air_pressure, 'sdfversion', None) is None:
                self.air_pressure.sdfversion = self.sdfversion
            elif getattr(self.air_pressure, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.air_pressure = self.air_pressure.to_version(self.sdfversion)
        if self.air_speed is not None and hasattr(self.air_speed, 'to_version'):
            if getattr(self.air_speed, 'sdfversion', None) is None:
                self.air_speed.sdfversion = self.sdfversion
            elif getattr(self.air_speed, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.air_speed = self.air_speed.to_version(self.sdfversion)
        if self.altimeter is not None and hasattr(self.altimeter, 'to_version'):
            if getattr(self.altimeter, 'sdfversion', None) is None:
                self.altimeter.sdfversion = self.sdfversion
            elif getattr(self.altimeter, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.altimeter = self.altimeter.to_version(self.sdfversion)
        if self.camera is not None and hasattr(self.camera, 'to_version'):
            if getattr(self.camera, 'sdfversion', None) is None:
                self.camera.sdfversion = self.sdfversion
            elif getattr(self.camera, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.camera = self.camera.to_version(self.sdfversion)
        if self.contact is not None and hasattr(self.contact, 'to_version'):
            if getattr(self.contact, 'sdfversion', None) is None:
                self.contact.sdfversion = self.sdfversion
            elif getattr(self.contact, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.contact = self.contact.to_version(self.sdfversion)
        if self.force_torque is not None and hasattr(self.force_torque, 'to_version'):
            if getattr(self.force_torque, 'sdfversion', None) is None:
                self.force_torque.sdfversion = self.sdfversion
            elif getattr(self.force_torque, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.force_torque = self.force_torque.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.gps is not None and hasattr(self.gps, 'to_version'):
            if getattr(self.gps, 'sdfversion', None) is None:
                self.gps.sdfversion = self.sdfversion
            elif getattr(self.gps, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.gps = self.gps.to_version(self.sdfversion)
        if self.imu is not None and hasattr(self.imu, 'to_version'):
            if getattr(self.imu, 'sdfversion', None) is None:
                self.imu.sdfversion = self.sdfversion
            elif getattr(self.imu, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.imu = self.imu.to_version(self.sdfversion)
        if self.lidar is not None and hasattr(self.lidar, 'to_version'):
            if getattr(self.lidar, 'sdfversion', None) is None:
                self.lidar.sdfversion = self.sdfversion
            elif getattr(self.lidar, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.lidar = self.lidar.to_version(self.sdfversion)
        if self.logical_camera is not None and hasattr(self.logical_camera, 'to_version'):
            if getattr(self.logical_camera, 'sdfversion', None) is None:
                self.logical_camera.sdfversion = self.sdfversion
            elif getattr(self.logical_camera, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.logical_camera = self.logical_camera.to_version(self.sdfversion)
        if self.magnetometer is not None and hasattr(self.magnetometer, 'to_version'):
            if getattr(self.magnetometer, 'sdfversion', None) is None:
                self.magnetometer.sdfversion = self.sdfversion
            elif getattr(self.magnetometer, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.magnetometer = self.magnetometer.to_version(self.sdfversion)
        if self.navsat is not None and hasattr(self.navsat, 'to_version'):
            if getattr(self.navsat, 'sdfversion', None) is None:
                self.navsat.sdfversion = self.sdfversion
            elif getattr(self.navsat, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.navsat = self.navsat.to_version(self.sdfversion)
        if self.origin is not None and hasattr(self.origin, 'to_version'):
            if getattr(self.origin, 'sdfversion', None) is None:
                self.origin.sdfversion = self.sdfversion
            elif getattr(self.origin, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.origin = self.origin.to_version(self.sdfversion)
        for _i, _c in enumerate(self.plugins):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.plugins[_i] = _c.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)
        if self.ray is not None and hasattr(self.ray, 'to_version'):
            if getattr(self.ray, 'sdfversion', None) is None:
                self.ray.sdfversion = self.sdfversion
            elif getattr(self.ray, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.ray = self.ray.to_version(self.sdfversion)
        if self.rfid is not None and hasattr(self.rfid, 'to_version'):
            if getattr(self.rfid, 'sdfversion', None) is None:
                self.rfid.sdfversion = self.sdfversion
            elif getattr(self.rfid, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.rfid = self.rfid.to_version(self.sdfversion)
        if self.rfidtag is not None and hasattr(self.rfidtag, 'to_version'):
            if getattr(self.rfidtag, 'sdfversion', None) is None:
                self.rfidtag.sdfversion = self.sdfversion
            elif getattr(self.rfidtag, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.rfidtag = self.rfidtag.to_version(self.sdfversion)
        if self.sonar is not None and hasattr(self.sonar, 'to_version'):
            if getattr(self.sonar, 'sdfversion', None) is None:
                self.sonar.sdfversion = self.sdfversion
            elif getattr(self.sonar, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.sonar = self.sonar.to_version(self.sdfversion)
        if self.transceiver is not None and hasattr(self.transceiver, 'to_version'):
            if getattr(self.transceiver, 'sdfversion', None) is None:
                self.transceiver.sdfversion = self.sdfversion
            elif getattr(self.transceiver, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.transceiver = self.transceiver.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_plugin(self, *items: "Plugin"):
        if self.plugins is None:
            self.plugins = []
        self.plugins.extend(items)

    def to_version(self, target_version: str) -> "Sensor":
        from ..elements.air_pressure import AirPressure
        from ..elements.air_speed import AirSpeed
        from ..elements.altimeter import Altimeter
        from ..elements.camera import Camera
        from ..elements.contact import Contact
        from ..elements.force_torque import ForceTorque
        from ..elements.frame import Frame
        from ..elements.gps import Gps
        from ..elements.imu import Imu
        from ..elements.lidar import Lidar
        from ..elements.logical_camera import LogicalCamera
        from ..elements.magnetometer import Magnetometer
        from ..elements.navsat import Navsat
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        from ..elements.ray import Ray
        from ..elements.rfid import Rfid
        from ..elements.rfidtag import Rfidtag
        from ..elements.sonar import Sonar
        from ..elements.transceiver import Transceiver
        if self.air_pressure is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'air_pressure' is not supported in SDF version {target_version} (added in 1.6)")
        if self.air_speed is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'air_speed' is not supported in SDF version {target_version} (added in 1.10)")
        if self.altimeter is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'altimeter' is not supported in SDF version {target_version} (added in 1.5)")
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        if self.force_torque is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'force_torque' is not supported in SDF version {target_version} (added in 1.4)")
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.gps is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gps' is not supported in SDF version {target_version} (added in 1.4)")
        if self.imu is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'imu' is not supported in SDF version {target_version} (added in 1.3)")
        if self.lidar is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'lidar' is not supported in SDF version {target_version} (added in 1.6)")
        if self.logical_camera is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'logical_camera' is not supported in SDF version {target_version} (added in 1.5)")
        if self.magnetometer is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'magnetometer' is not supported in SDF version {target_version} (added in 1.5)")
        if self.navsat is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'navsat' is not supported in SDF version {target_version} (added in 1.7)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.sonar is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'sonar' is not supported in SDF version {target_version} (added in 1.4)")
        if self.transceiver is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'transceiver' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs: dict = {"sdf_version": target_version, "air_pressure": self.air_pressure.to_version(target_version) if self.air_pressure is not None and hasattr(self.air_pressure, "to_version") else self.air_pressure, "air_speed": self.air_speed.to_version(target_version) if self.air_speed is not None and hasattr(self.air_speed, "to_version") else self.air_speed, "altimeter": self.altimeter.to_version(target_version) if self.altimeter is not None and hasattr(self.altimeter, "to_version") else self.altimeter, "always_on": self.always_on, "camera": self.camera.to_version(target_version) if self.camera is not None and hasattr(self.camera, "to_version") else self.camera, "contact": self.contact.to_version(target_version) if self.contact is not None and hasattr(self.contact, "to_version") else self.contact, "enable_metrics": self.enable_metrics, "force_torque": self.force_torque.to_version(target_version) if self.force_torque is not None and hasattr(self.force_torque, "to_version") else self.force_torque, "frame_id": self.frame_id, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "gps": self.gps.to_version(target_version) if self.gps is not None and hasattr(self.gps, "to_version") else self.gps, "imu": self.imu.to_version(target_version) if self.imu is not None and hasattr(self.imu, "to_version") else self.imu, "lidar": self.lidar.to_version(target_version) if self.lidar is not None and hasattr(self.lidar, "to_version") else self.lidar, "logical_camera": self.logical_camera.to_version(target_version) if self.logical_camera is not None and hasattr(self.logical_camera, "to_version") else self.logical_camera, "magnetometer": self.magnetometer.to_version(target_version) if self.magnetometer is not None and hasattr(self.magnetometer, "to_version") else self.magnetometer, "name": self.name, "navsat": self.navsat.to_version(target_version) if self.navsat is not None and hasattr(self.navsat, "to_version") else self.navsat, "origin": self.origin.to_version(target_version) if self.origin is not None and hasattr(self.origin, "to_version") else self.origin, "plugins": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.plugins or [])], "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "ray": self.ray.to_version(target_version) if self.ray is not None and hasattr(self.ray, "to_version") else self.ray, "rfid": self.rfid.to_version(target_version) if self.rfid is not None and hasattr(self.rfid, "to_version") else self.rfid, "rfidtag": self.rfidtag.to_version(target_version) if self.rfidtag is not None and hasattr(self.rfidtag, "to_version") else self.rfidtag, "sonar": self.sonar.to_version(target_version) if self.sonar is not None and hasattr(self.sonar, "to_version") else self.sonar, "topic": self.topic, "transceiver": self.transceiver.to_version(target_version) if self.transceiver is not None and hasattr(self.transceiver, "to_version") else self.transceiver, "type": self.type, "update_rate": self.update_rate, "visualize": self.visualize}
        return Sensor(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.air_pressure import AirPressure
        from ..elements.air_speed import AirSpeed
        from ..elements.altimeter import Altimeter
        from ..elements.camera import Camera
        from ..elements.contact import Contact
        from ..elements.force_torque import ForceTorque
        from ..elements.frame import Frame
        from ..elements.gps import Gps
        from ..elements.imu import Imu
        from ..elements.lidar import Lidar
        from ..elements.logical_camera import LogicalCamera
        from ..elements.magnetometer import Magnetometer
        from ..elements.navsat import Navsat
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        from ..elements.ray import Ray
        from ..elements.rfid import Rfid
        from ..elements.rfidtag import Rfidtag
        from ..elements.sonar import Sonar
        from ..elements.transceiver import Transceiver
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("sensor")
        if self.air_pressure is not None:
            _child_res = self.air_pressure.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('air_pressure')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.air_speed is not None:
            _child_res = self.air_speed.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('air_speed')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.altimeter is not None:
            _child_res = self.altimeter.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('altimeter')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.always_on is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("always_on")
                _c_tmp.text = str(self.always_on).lower()
                el.append(_c_tmp)
            else:
                el.set("always_on", str(self.always_on).lower())
        if self.camera is not None:
            _child_res = self.camera.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('camera')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.contact is not None:
            _child_res = self.contact.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('contact')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.enable_metrics is not None:
            _c_tmp = ET.Element("enable_metrics")
            _c_tmp.text = str(self.enable_metrics).lower()
            el.append(_c_tmp)
        if self.force_torque is not None:
            _child_res = self.force_torque.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('force_torque')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.frame_id is not None:
            _c_tmp = ET.Element("frame_id")
            _c_tmp.text = self.frame_id
            el.append(_c_tmp)
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.gps is not None:
            _child_res = self.gps.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('gps')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.imu is not None:
            _child_res = self.imu.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('imu')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.lidar is not None:
            _child_res = self.lidar.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('lidar')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.logical_camera is not None:
            _child_res = self.logical_camera.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('logical_camera')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.magnetometer is not None:
            _child_res = self.magnetometer.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('magnetometer')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        if self.navsat is not None:
            _child_res = self.navsat.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('navsat')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.origin is not None:
            _child_res = self.origin.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('origin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.plugins or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('plugin')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pose is not None:
            _child_res = self.pose.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.ray is not None:
            _child_res = self.ray.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('ray')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.rfid is not None:
            _child_res = self.rfid.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('rfid')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.rfidtag is not None:
            _child_res = self.rfidtag.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('rfidtag')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.sonar is not None:
            _child_res = self.sonar.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('sonar')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.topic is not None:
            _c_tmp = ET.Element("topic")
            _c_tmp.text = self.topic
            el.append(_c_tmp)
        if self.transceiver is not None:
            _child_res = self.transceiver.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('transceiver')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.type is not None:
            el.set("type", self.type)
        if self.update_rate is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("update_rate")
                _c_tmp.text = str(self.update_rate)
                el.append(_c_tmp)
            else:
                el.set("update_rate", str(self.update_rate))
        if self.visualize is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("visualize")
                _c_tmp.text = str(self.visualize).lower()
                el.append(_c_tmp)
            else:
                el.set("visualize", str(self.visualize).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Sensor | SDFError":
        from ..elements.air_pressure import AirPressure
        from ..elements.air_speed import AirSpeed
        from ..elements.altimeter import Altimeter
        from ..elements.camera import Camera
        from ..elements.contact import Contact
        from ..elements.force_torque import ForceTorque
        from ..elements.frame import Frame
        from ..elements.gps import Gps
        from ..elements.imu import Imu
        from ..elements.lidar import Lidar
        from ..elements.logical_camera import LogicalCamera
        from ..elements.magnetometer import Magnetometer
        from ..elements.navsat import Navsat
        from ..elements.plugin import Plugin
        from ..elements.pose import Pose
        from ..elements.ray import Ray
        from ..elements.rfid import Rfid
        from ..elements.rfidtag import Rfidtag
        from ..elements.sonar import Sonar
        from ..elements.transceiver import Transceiver
        _c_air_pressure = el.find("air_pressure")
        if _c_air_pressure is not None:
            _res = AirPressure._from_sdf(_c_air_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("air_pressure")
            _air_pressure = _res
        else:
            _air_pressure = None
        if _air_pressure is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'air_pressure' is not supported in SDF version {version} (added in 1.6)")
        _c_air_speed = el.find("air_speed")
        if _c_air_speed is not None:
            _res = AirSpeed._from_sdf(_c_air_speed, version)
            if isinstance(_res, SDFError):
                return _res.extend("air_speed")
            _air_speed = _res
        else:
            _air_speed = None
        if _air_speed is not None and cmp_version(version, "1.10") < 0:
            return SDFError(f"'air_speed' is not supported in SDF version {version} (added in 1.10)")
        _c_altimeter = el.find("altimeter")
        if _c_altimeter is not None:
            _res = Altimeter._from_sdf(_c_altimeter, version)
            if isinstance(_res, SDFError):
                return _res.extend("altimeter")
            _altimeter = _res
        else:
            _altimeter = None
        if _altimeter is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'altimeter' is not supported in SDF version {version} (added in 1.5)")
        _raw_always_on = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("always_on")
            if _c_tmp is not None: _raw_always_on = _c_tmp.text
        else:
            _raw_always_on = el.get("always_on")
        if _raw_always_on is not None:
            _always_on = str(_raw_always_on).strip().lower() == 'true'
            if isinstance(_always_on, SDFError):
                return _always_on.extend("@always_on")
        else:
            _always_on = None
        _c_camera = el.find("camera")
        if _c_camera is not None:
            _res = Camera._from_sdf(_c_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera")
            _camera = _res
        else:
            _camera = None
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = Contact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _c_tmp = el.find("enable_metrics")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("enable_metrics")
            _enable_metrics = _val
        else:
            _enable_metrics = None
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        _c_force_torque = el.find("force_torque")
        if _c_force_torque is not None:
            _res = ForceTorque._from_sdf(_c_force_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("force_torque")
            _force_torque = _res
        else:
            _force_torque = None
        if _force_torque is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'force_torque' is not supported in SDF version {version} (added in 1.4)")
        _c_tmp = el.find("frame_id")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else None
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("frame_id")
            _frame_id = _val
        else:
            _frame_id = None
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _c_gps = el.find("gps")
        if _c_gps is not None:
            _res = Gps._from_sdf(_c_gps, version)
            if isinstance(_res, SDFError):
                return _res.extend("gps")
            _gps = _res
        else:
            _gps = None
        if _gps is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'gps' is not supported in SDF version {version} (added in 1.4)")
        _c_imu = el.find("imu")
        if _c_imu is not None:
            _res = Imu._from_sdf(_c_imu, version)
            if isinstance(_res, SDFError):
                return _res.extend("imu")
            _imu = _res
        else:
            _imu = None
        if _imu is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'imu' is not supported in SDF version {version} (added in 1.3)")
        _c_lidar = el.find("lidar")
        if _c_lidar is not None:
            _res = Lidar._from_sdf(_c_lidar, version)
            if isinstance(_res, SDFError):
                return _res.extend("lidar")
            _lidar = _res
        else:
            _lidar = None
        if _lidar is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'lidar' is not supported in SDF version {version} (added in 1.6)")
        _c_logical_camera = el.find("logical_camera")
        if _c_logical_camera is not None:
            _res = LogicalCamera._from_sdf(_c_logical_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("logical_camera")
            _logical_camera = _res
        else:
            _logical_camera = None
        if _logical_camera is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'logical_camera' is not supported in SDF version {version} (added in 1.5)")
        _c_magnetometer = el.find("magnetometer")
        if _c_magnetometer is not None:
            _res = Magnetometer._from_sdf(_c_magnetometer, version)
            if isinstance(_res, SDFError):
                return _res.extend("magnetometer")
            _magnetometer = _res
        else:
            _magnetometer = None
        if _magnetometer is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'magnetometer' is not supported in SDF version {version} (added in 1.5)")
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        _c_navsat = el.find("navsat")
        if _c_navsat is not None:
            _res = Navsat._from_sdf(_c_navsat, version)
            if isinstance(_res, SDFError):
                return _res.extend("navsat")
            _navsat = _res
        else:
            _navsat = None
        if _navsat is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'navsat' is not supported in SDF version {version} (added in 1.7)")
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = cls.Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
        _plugins = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugins.append(_res)
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _c_ray = el.find("ray")
        if _c_ray is not None:
            _res = Ray._from_sdf(_c_ray, version)
            if isinstance(_res, SDFError):
                return _res.extend("ray")
            _ray = _res
        else:
            _ray = None
        _c_rfid = el.find("rfid")
        if _c_rfid is not None:
            _res = Rfidtag._from_sdf(_c_rfid, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfid")
            _rfid = _res
        else:
            _rfid = None
        _c_rfidtag = el.find("rfidtag")
        if _c_rfidtag is not None:
            _res = Rfid._from_sdf(_c_rfidtag, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfidtag")
            _rfidtag = _res
        else:
            _rfidtag = None
        _c_sonar = el.find("sonar")
        if _c_sonar is not None:
            _res = Sonar._from_sdf(_c_sonar, version)
            if isinstance(_res, SDFError):
                return _res.extend("sonar")
            _sonar = _res
        else:
            _sonar = None
        if _sonar is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'sonar' is not supported in SDF version {version} (added in 1.4)")
        _c_tmp = el.find("topic")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("topic")
            _topic = _val
        else:
            _topic = None
        _c_transceiver = el.find("transceiver")
        if _c_transceiver is not None:
            _res = Transceiver._from_sdf(_c_transceiver, version)
            if isinstance(_res, SDFError):
                return _res.extend("transceiver")
            _transceiver = _res
        else:
            _transceiver = None
        if _transceiver is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'transceiver' is not supported in SDF version {version} (added in 1.4)")
        _raw_type = el.get("type")
        if _raw_type is not None:
            _type = _raw_type
            if isinstance(_type, SDFError):
                return _type.extend("@type")
        else:
            _type = None
        _raw_update_rate = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("update_rate")
            if _c_tmp is not None: _raw_update_rate = _c_tmp.text
        else:
            _raw_update_rate = el.get("update_rate")
        if _raw_update_rate is not None:
            _update_rate = _parse_double(_raw_update_rate)
            if isinstance(_update_rate, SDFError):
                return _update_rate.extend("@update_rate")
        else:
            _update_rate = None
        _raw_visualize = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("visualize")
            if _c_tmp is not None: _raw_visualize = _c_tmp.text
        else:
            _raw_visualize = el.get("visualize")
        if _raw_visualize is not None:
            _visualize = str(_raw_visualize).strip().lower() == 'true'
            if isinstance(_visualize, SDFError):
                return _visualize.extend("@visualize")
        else:
            _visualize = None
        return cls(sdf_version=version, air_pressure=_air_pressure, air_speed=_air_speed, altimeter=_altimeter, always_on=_always_on, camera=_camera, contact=_contact, enable_metrics=_enable_metrics, force_torque=_force_torque, frame_id=_frame_id, frames=_frames, gps=_gps, imu=_imu, lidar=_lidar, logical_camera=_logical_camera, magnetometer=_magnetometer, name=_name, navsat=_navsat, origin=_origin, plugins=_plugins, pose=_pose, ray=_ray, rfid=_rfid, rfidtag=_rfidtag, sonar=_sonar, topic=_topic, transceiver=_transceiver, type=_type, update_rate=_update_rate, visualize=_visualize)
