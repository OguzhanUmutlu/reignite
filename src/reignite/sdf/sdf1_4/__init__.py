from __future__ import annotations

from . import models as _models

Actor = _models.Actor
AudioSink = _models.AudioSink
AudioSource = _models.AudioSource
Box = _models.Box
Camera = _models.Camera
Collision = _models.Collision
CollisionEngine = _models.CollisionEngine
Contact = _models.Contact
Cylinder = _models.Cylinder
ForceTorque = _models.ForceTorque
Geometry = _models.Geometry
Gps = _models.Gps
Gripper = _models.Gripper
Gui = _models.Gui
Heightmap = _models.Heightmap
Image = _models.Image
Imu = _models.Imu
Inertial = _models.Inertial
Joint = _models.Joint
Light = _models.Light
Link = _models.Link
Mesh = _models.Mesh
Model = _models.Model
Noise = _models.Noise
Physics = _models.Physics
Plane = _models.Plane
Plugin = _models.Plugin
Projector = _models.Projector
Ray = _models.Ray
Rfid = _models.Rfid
Rfidtag = _models.Rfidtag
Road = _models.Road
Robot = _models.Robot
Scene = _models.Scene
Sdf = _models.Sdf
Sensor = _models.Sensor
Sonar = _models.Sonar
Sphere = _models.Sphere
SphericalCoordinates = _models.SphericalCoordinates
State = _models.State
Surface = _models.Surface
Transceiver = _models.Transceiver
Visual = _models.Visual
World = _models.World

TAG_NAMES: list[str] = ["actor", "audio_sink", "audio_source", "box", "camera", "collision", "collision_engine",
                        "contact", "cylinder", "force_torque", "geometry", "gps", "gripper", "gui", "heightmap",
                        "image", "imu", "inertial", "joint", "light", "link", "mesh", "model", "noise", "physics",
                        "plane", "plugin", "projector", "ray", "rfid", "rfidtag", "road", "robot", "scene", "sdf",
                        "sensor", "sonar", "sphere", "spherical_coordinates", "state", "surface", "transceiver",
                        "visual", "world"]
TAG_CLASS_MAP: dict[str, type] = {
    "actor": Actor,
    "audio_sink": AudioSink,
    "audio_source": AudioSource,
    "box": Box,
    "camera": Camera,
    "collision": Collision,
    "collision_engine": CollisionEngine,
    "contact": Contact,
    "cylinder": Cylinder,
    "force_torque": ForceTorque,
    "geometry": Geometry,
    "gps": Gps,
    "gripper": Gripper,
    "gui": Gui,
    "heightmap": Heightmap,
    "image": Image,
    "imu": Imu,
    "inertial": Inertial,
    "joint": Joint,
    "light": Light,
    "link": Link,
    "mesh": Mesh,
    "model": Model,
    "noise": Noise,
    "physics": Physics,
    "plane": Plane,
    "plugin": Plugin,
    "projector": Projector,
    "ray": Ray,
    "rfid": Rfid,
    "rfidtag": Rfidtag,
    "road": Road,
    "robot": Robot,
    "scene": Scene,
    "sdf": Sdf,
    "sensor": Sensor,
    "sonar": Sonar,
    "sphere": Sphere,
    "spherical_coordinates": SphericalCoordinates,
    "state": State,
    "surface": Surface,
    "transceiver": Transceiver,
    "visual": Visual,
    "world": World,
}


def get_tag_class(tag: str) -> type | None:
    return TAG_CLASS_MAP.get(tag)
