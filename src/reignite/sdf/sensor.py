### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.pose import Pose as _SDFPose
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


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class AlwaysOn(BaseModel):
    def __init__(self, sdf_version: str, always_on: bool = False):
        self.__version__ = sdf_version
        self.always_on = always_on

    def to_version(self, target_version: str) -> "AlwaysOn":
        if self.always_on is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'always_on' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["always_on"] = self.always_on
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("always_on")
        if self.always_on is not None:
            el.text = str(self.always_on).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _always_on = str(_text).strip().lower() == 'true'
        if isinstance(_always_on, SDFError):
            return _always_on
        if _always_on is not None and cmp_version(version, "1.2") < 0:
            if _always_on != False:
                return SDFError(f"'always_on' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, always_on=_always_on)


class EnableMetrics(BaseModel):
    def __init__(self, sdf_version: str, enable_metrics: bool = False):
        self.__version__ = sdf_version
        self.enable_metrics = enable_metrics

    def to_version(self, target_version: str) -> "EnableMetrics":
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_metrics"] = self.enable_metrics
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_metrics")
        if self.enable_metrics is not None:
            el.text = str(self.enable_metrics).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _enable_metrics = str(_text).strip().lower() == 'true'
        if isinstance(_enable_metrics, SDFError):
            return _enable_metrics
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            if _enable_metrics != False:
                return SDFError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, enable_metrics=_enable_metrics)


class FrameId(BaseModel):
    def __init__(self, sdf_version: str, frame_id: str = ""):
        self.__version__ = sdf_version
        self.frame_id = frame_id

    def to_version(self, target_version: str) -> "FrameId":
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame_id"] = self.frame_id
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame_id")
        if self.frame_id is not None:
            el.text = self.frame_id
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _frame_id = _text
        if isinstance(_frame_id, SDFError):
            return _frame_id
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            if _frame_id != "":
                return SDFError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, frame_id=_frame_id)


class Origin(BaseModel):
    def __init__(self, sdf_version: str, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "Origin":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("origin")
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _pose = _SDFPose._from_sdf(el.get("pose", "0 0 0 0 0 0"), version)
        if isinstance(_pose, SDFError):
            return _pose.extend("@pose")
        return cls(sdf_version=version, pose=_pose)


class Sensor(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        air_pressure: "AirPressure" = None,
        air_speed: "AirSpeed" = None,
        altimeter: "Altimeter" = None,
        always_on: bool = False,
        camera: "Camera" = None,
        contact: "Contact" = None,
        enable_metrics: "EnableMetrics" = None,
        force_torque: "ForceTorque" = None,
        frame: List["Frame"] = None,
        frame_id: "FrameId" = None,
        gps: "Gps" = None,
        imu: "Imu" = None,
        lidar: "Lidar" = None,
        logical_camera: "LogicalCamera" = None,
        magnetometer: "Magnetometer" = None,
        name: str = "__default__",
        navsat: "Navsat" = None,
        origin: "Origin" = None,
        plugin: List["Plugin"] = None,
        pose: "Pose" = None,
        ray: "Ray" = None,
        rfid: "Rfid" = None,
        rfidtag: "Rfidtag" = None,
        sonar: "Sonar" = None,
        topic: "Topic" = None,
        transceiver: "Transceiver" = None,
        type: str = "__default__",
        update_rate: float = 0,
        visualize: bool = False
    ):
        self.__version__ = sdf_version
        self.air_pressure = air_pressure
        self.air_speed = air_speed
        self.altimeter = altimeter
        self.always_on = always_on
        self.camera = camera
        self.contact = contact
        self.enable_metrics = enable_metrics
        self.force_torque = force_torque
        self.frame = frame or []
        self.frame_id = frame_id
        self.gps = gps
        self.imu = imu
        self.lidar = lidar
        self.logical_camera = logical_camera
        self.magnetometer = magnetometer
        self.name = name
        self.navsat = navsat
        self.origin = origin
        self.plugin = plugin or []
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
        if self.always_on is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'always_on' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        if self.force_torque is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'force_torque' is not supported in SDF version {target_version} (added in 1.4)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
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
        if self.update_rate is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'update_rate' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.visualize is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["air_pressure"] = self.air_pressure.to_version(target_version) if self.air_pressure is not None else None
        kwargs["air_speed"] = self.air_speed.to_version(target_version) if self.air_speed is not None else None
        kwargs["altimeter"] = self.altimeter.to_version(target_version) if self.altimeter is not None else None
        kwargs["always_on"] = self.always_on
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["enable_metrics"] = self.enable_metrics.to_version(target_version) if self.enable_metrics is not None else None
        kwargs["force_torque"] = self.force_torque.to_version(target_version) if self.force_torque is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["frame_id"] = self.frame_id.to_version(target_version) if self.frame_id is not None else None
        kwargs["gps"] = self.gps.to_version(target_version) if self.gps is not None else None
        kwargs["imu"] = self.imu.to_version(target_version) if self.imu is not None else None
        kwargs["lidar"] = self.lidar.to_version(target_version) if self.lidar is not None else None
        kwargs["logical_camera"] = self.logical_camera.to_version(target_version) if self.logical_camera is not None else None
        kwargs["magnetometer"] = self.magnetometer.to_version(target_version) if self.magnetometer is not None else None
        kwargs["name"] = self.name
        kwargs["navsat"] = self.navsat.to_version(target_version) if self.navsat is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["ray"] = self.ray.to_version(target_version) if self.ray is not None else None
        kwargs["rfid"] = self.rfid.to_version(target_version) if self.rfid is not None else None
        kwargs["rfidtag"] = self.rfidtag.to_version(target_version) if self.rfidtag is not None else None
        kwargs["sonar"] = self.sonar.to_version(target_version) if self.sonar is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["transceiver"] = self.transceiver.to_version(target_version) if self.transceiver is not None else None
        kwargs["type"] = self.type
        kwargs["update_rate"] = self.update_rate
        kwargs["visualize"] = self.visualize
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
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
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sensor")
        if self.air_pressure is not None:
            el.append(self.air_pressure.to_sdf(version))
        if self.air_speed is not None:
            el.append(self.air_speed.to_sdf(version))
        if self.altimeter is not None:
            el.append(self.altimeter.to_sdf(version))
        if self.always_on is not None:
            el.set("always_on", str(self.always_on).lower())
        if self.camera is not None:
            el.append(self.camera.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        if self.enable_metrics is not None:
            el.append(self.enable_metrics.to_sdf(version))
        if self.force_torque is not None:
            el.append(self.force_torque.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.frame_id is not None:
            el.append(self.frame_id.to_sdf(version))
        if self.gps is not None:
            el.append(self.gps.to_sdf(version))
        if self.imu is not None:
            el.append(self.imu.to_sdf(version))
        if self.lidar is not None:
            el.append(self.lidar.to_sdf(version))
        if self.logical_camera is not None:
            el.append(self.logical_camera.to_sdf(version))
        if self.magnetometer is not None:
            el.append(self.magnetometer.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.navsat is not None:
            el.append(self.navsat.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.ray is not None:
            el.append(self.ray.to_sdf(version))
        if self.rfid is not None:
            el.append(self.rfid.to_sdf(version))
        if self.rfidtag is not None:
            el.append(self.rfidtag.to_sdf(version))
        if self.sonar is not None:
            el.append(self.sonar.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.transceiver is not None:
            el.append(self.transceiver.to_sdf(version))
        if self.type is not None:
            el.set("type", self.type)
        if self.update_rate is not None:
            el.set("update_rate", str(self.update_rate))
        if self.visualize is not None:
            el.set("visualize", str(self.visualize).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        _always_on = str(el.get("always_on", False)).strip().lower() == 'true'
        if isinstance(_always_on, SDFError):
            return _always_on.extend("@always_on")
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
        _c_enable_metrics = el.find("enable_metrics")
        if _c_enable_metrics is not None:
            _res = EnableMetrics._from_sdf(_c_enable_metrics, version)
            if isinstance(_res, SDFError):
                return _res.extend("enable_metrics")
            _enable_metrics = _res
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
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_frame_id = el.find("frame_id")
        if _c_frame_id is not None:
            _res = FrameId._from_sdf(_c_frame_id, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame_id")
            _frame_id = _res
        else:
            _frame_id = None
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            return SDFError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
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
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
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
            _res = Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
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
            _res = Rfid._from_sdf(_c_rfid, version)
            if isinstance(_res, SDFError):
                return _res.extend("rfid")
            _rfid = _res
        else:
            _rfid = None
        _c_rfidtag = el.find("rfidtag")
        if _c_rfidtag is not None:
            _res = Rfidtag._from_sdf(_c_rfidtag, version)
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
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = Topic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
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
        _type = el.get("type", "__default__")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _update_rate = _parse_double(el.get("update_rate", 0))
        if isinstance(_update_rate, SDFError):
            return _update_rate.extend("@update_rate")
        _visualize = str(el.get("visualize", False)).strip().lower() == 'true'
        if isinstance(_visualize, SDFError):
            return _visualize.extend("@visualize")
        return cls(sdf_version=version, air_pressure=_air_pressure, air_speed=_air_speed, altimeter=_altimeter, always_on=_always_on, camera=_camera, contact=_contact, enable_metrics=_enable_metrics, force_torque=_force_torque, frame=_frame, frame_id=_frame_id, gps=_gps, imu=_imu, lidar=_lidar, logical_camera=_logical_camera, magnetometer=_magnetometer, name=_name, navsat=_navsat, origin=_origin, plugin=_plugin, pose=_pose, ray=_ray, rfid=_rfid, rfidtag=_rfidtag, sonar=_sonar, topic=_topic, transceiver=_transceiver, type=_type, update_rate=_update_rate, visualize=_visualize)


class Topic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = "__default"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "Topic":
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default"
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


class UpdateRate(BaseModel):
    def __init__(self, sdf_version: str, update_rate: float = 0):
        self.__version__ = sdf_version
        self.update_rate = update_rate

    def to_version(self, target_version: str) -> "UpdateRate":
        if self.update_rate is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'update_rate' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["update_rate"] = self.update_rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("update_rate")
        if self.update_rate is not None:
            el.text = str(self.update_rate)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _update_rate = _parse_double(_text)
        if isinstance(_update_rate, SDFError):
            return _update_rate
        if _update_rate is not None and cmp_version(version, "1.2") < 0:
            if _update_rate != 0:
                return SDFError(f"'update_rate' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, update_rate=_update_rate)


class Visualize(BaseModel):
    def __init__(self, sdf_version: str, visualize: bool = False):
        self.__version__ = sdf_version
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Visualize":
        if self.visualize is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'visualize' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["visualize"] = self.visualize
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visualize")
        if self.visualize is not None:
            el.text = str(self.visualize).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _visualize = str(_text).strip().lower() == 'true'
        if isinstance(_visualize, SDFError):
            return _visualize
        if _visualize is not None and cmp_version(version, "1.2") < 0:
            if _visualize != False:
                return SDFError(f"'visualize' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, visualize=_visualize)
