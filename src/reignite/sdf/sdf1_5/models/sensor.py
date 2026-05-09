from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .altimeter import Altimeter
from .always_on import AlwaysOn
from .camera import Camera
from .force_torque import ForceTorque
from .frame import Frame
from .gps import Gps
from .imu import Imu
from .logical_camera import LogicalCamera
from .magnetometer import Magnetometer
from .plugin import Plugin
from .pose import Pose
from .ray import Ray
from .rfid import Rfid
from .rfidtag import Rfidtag
from .sonar import Sonar
from .topic import Topic
from .transceiver import Transceiver
from .update_rate import UpdateRate
from .visualize import Visualize
from ...sdf1_4.models.bullet import Bullet as _PrevBullet
from ...sdf1_4.models.contact import Contact as _PrevContact
from ...sdf1_4.models.ode import Ode as _PrevOde
from ...sdf1_4.models.sensor import Sensor as _PrevSensor


class Ode(_PrevOde):
    def __init__(self, slip: "Slip" = None):
        super().__init__()
        self.slip = slip

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.slip is not None:
            el.append(self.slip.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_slip = el.find("slip")
        _slip = Slip.from_sdf(_c_slip) if _c_slip is not None else None
        return cls(slip=_slip)


class Bullet(_PrevBullet):
    def __init__(
            self,
            friction: "Friction" = None,
            friction2: "Friction2" = None,
            fdir1: "Fdir1" = None,
            rolling_friction: "RollingFriction" = None
    ):
        super().__init__()
        self.friction = friction
        self.friction2 = friction2
        self.fdir1 = fdir1
        self.rolling_friction = rolling_friction

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        if self.friction2 is not None:
            el.append(self.friction2.to_sdf())
        if self.fdir1 is not None:
            el.append(self.fdir1.to_sdf())
        if self.rolling_friction is not None:
            el.append(self.rolling_friction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        _c_friction2 = el.find("friction2")
        _friction2 = Friction2.from_sdf(_c_friction2) if _c_friction2 is not None else None
        _c_fdir1 = el.find("fdir1")
        _fdir1 = Fdir1.from_sdf(_c_fdir1) if _c_fdir1 is not None else None
        _c_rolling_friction = el.find("rolling_friction")
        _rolling_friction = RollingFriction.from_sdf(_c_rolling_friction) if _c_rolling_friction is not None else None
        return cls(friction=_friction, friction2=_friction2, fdir1=_fdir1, rolling_friction=_rolling_friction)


class Contact(_PrevContact):
    def __init__(
            self,
            collide_without_contact: "CollideWithoutContact" = None,
            collide_without_contact_bitmask: "CollideWithoutContactBitmask" = None,
            collide_bitmask: "CollideBitmask" = None,
            poissons_ratio: "PoissonsRatio" = None,
            elastic_modulus: "ElasticModulus" = None,
            ode: "Ode" = None,
            bullet: "Bullet" = None
    ):
        super().__init__()
        self.collide_without_contact = collide_without_contact
        self.collide_without_contact_bitmask = collide_without_contact_bitmask
        self.collide_bitmask = collide_bitmask
        self.poissons_ratio = poissons_ratio
        self.elastic_modulus = elastic_modulus
        self.ode = ode
        self.bullet = bullet

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.collide_without_contact is not None:
            el.append(self.collide_without_contact.to_sdf())
        if self.collide_without_contact_bitmask is not None:
            el.append(self.collide_without_contact_bitmask.to_sdf())
        if self.collide_bitmask is not None:
            el.append(self.collide_bitmask.to_sdf())
        if self.poissons_ratio is not None:
            el.append(self.poissons_ratio.to_sdf())
        if self.elastic_modulus is not None:
            el.append(self.elastic_modulus.to_sdf())
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Contact":
        _c_collide_without_contact = el.find("collide_without_contact")
        _collide_without_contact = CollideWithoutContact.from_sdf(
            _c_collide_without_contact) if _c_collide_without_contact is not None else None
        _c_collide_without_contact_bitmask = el.find("collide_without_contact_bitmask")
        _collide_without_contact_bitmask = CollideWithoutContactBitmask.from_sdf(
            _c_collide_without_contact_bitmask) if _c_collide_without_contact_bitmask is not None else None
        _c_collide_bitmask = el.find("collide_bitmask")
        _collide_bitmask = CollideBitmask.from_sdf(_c_collide_bitmask) if _c_collide_bitmask is not None else None
        _c_poissons_ratio = el.find("poissons_ratio")
        _poissons_ratio = PoissonsRatio.from_sdf(_c_poissons_ratio) if _c_poissons_ratio is not None else None
        _c_elastic_modulus = el.find("elastic_modulus")
        _elastic_modulus = ElasticModulus.from_sdf(_c_elastic_modulus) if _c_elastic_modulus is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(collide_without_contact=_collide_without_contact,
                   collide_without_contact_bitmask=_collide_without_contact_bitmask, collide_bitmask=_collide_bitmask,
                   poissons_ratio=_poissons_ratio, elastic_modulus=_elastic_modulus, ode=_ode, bullet=_bullet)


class Sensor(_PrevSensor):
    def __init__(
            self,
            name: str = "__default__",
            type: str = "__default__",
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            plugin: List["Plugin"] = None,
            altimeter: "Altimeter" = None,
            camera: "Camera" = None,
            contact: "Contact" = None,
            force_torque: "ForceTorque" = None,
            gps: "Gps" = None,
            imu: "Imu" = None,
            logical_camera: "LogicalCamera" = None,
            magnetometer: "Magnetometer" = None,
            ray: "Ray" = None,
            rfidtag: "Rfidtag" = None,
            rfid: "Rfid" = None,
            sonar: "Sonar" = None,
            transceiver: "Transceiver" = None,
            always_on: "AlwaysOn" = None,
            update_rate: "UpdateRate" = None,
            visualize: "Visualize" = None,
            topic: "Topic" = None
    ):
        super().__init__(name=name, type=type, pose=pose, plugin=plugin, camera=camera, contact=contact,
                         force_torque=force_torque, gps=gps, imu=imu, ray=ray, rfidtag=rfidtag, rfid=rfid, sonar=sonar,
                         transceiver=transceiver, always_on=always_on, update_rate=update_rate, visualize=visualize,
                         topic=topic)
        self.frame = frame or []
        self.altimeter = altimeter
        self.logical_camera = logical_camera
        self.magnetometer = magnetometer

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        if self.altimeter is not None:
            el.append(self.altimeter.to_sdf())
        if self.logical_camera is not None:
            el.append(self.logical_camera.to_sdf())
        if self.magnetometer is not None:
            el.append(self.magnetometer.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sensor":
        _base = _PrevSensor.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _c_altimeter = el.find("altimeter")
        _altimeter = Altimeter.from_sdf(_c_altimeter) if _c_altimeter is not None else None
        _c_logical_camera = el.find("logical_camera")
        _logical_camera = LogicalCamera.from_sdf(_c_logical_camera) if _c_logical_camera is not None else None
        _c_magnetometer = el.find("magnetometer")
        _magnetometer = Magnetometer.from_sdf(_c_magnetometer) if _c_magnetometer is not None else None
        return cls(name=_base.name, type=_base.type, frame=_frame, pose=_base.pose, plugin=_base.plugin,
                   altimeter=_altimeter, camera=_base.camera, contact=_base.contact, force_torque=_base.force_torque,
                   gps=_base.gps, imu=_base.imu, logical_camera=_logical_camera, magnetometer=_magnetometer,
                   ray=_base.ray, rfidtag=_base.rfidtag, rfid=_base.rfid, sonar=_base.sonar,
                   transceiver=_base.transceiver, always_on=_base.always_on, update_rate=_base.update_rate,
                   visualize=_base.visualize, topic=_base.topic)
