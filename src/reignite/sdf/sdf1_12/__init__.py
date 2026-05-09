from __future__ import annotations

from . import models as _models

Actor = _models.Actor
AirPressure = _models.AirPressure
AirSpeed = _models.AirSpeed
Altimeter = _models.Altimeter
Atmosphere = _models.Atmosphere
AudioSink = _models.AudioSink
AudioSource = _models.AudioSource
Battery = _models.Battery
Box = _models.Box
Camera = _models.Camera
Capsule = _models.Capsule
Collision = _models.Collision
Cone = _models.Cone
Contact = _models.Contact
Cylinder = _models.Cylinder
Ellipsoid = _models.Ellipsoid
ForceTorque = _models.ForceTorque
Frame = _models.Frame
Geometry = _models.Geometry
Gps = _models.Gps
Gripper = _models.Gripper
Gui = _models.Gui
Heightmap = _models.Heightmap
Image = _models.Image
Imu = _models.Imu
Inertial = _models.Inertial
Joint = _models.Joint
JointState = _models.JointState
Lidar = _models.Lidar
Light = _models.Light
LightState = _models.LightState
Link = _models.Link
LinkState = _models.LinkState
LogicalCamera = _models.LogicalCamera
Magnetometer = _models.Magnetometer
Material = _models.Material
Mesh = _models.Mesh
Mimic = _models.Mimic
Model = _models.Model
ModelState = _models.ModelState
Navsat = _models.Navsat
Noise = _models.Noise
ParticleEmitter = _models.ParticleEmitter
Physics = _models.Physics
Plane = _models.Plane
Plugin = _models.Plugin
Polyline = _models.Polyline
Population = _models.Population
Pose = _models.Pose
Projector = _models.Projector
Ray = _models.Ray
Rfid = _models.Rfid
Rfidtag = _models.Rfidtag
Road = _models.Road
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

TAG_NAMES: list[str] = ["actor", "air_pressure", "air_speed", "altimeter", "atmosphere", "audio_sink", "audio_source",
                        "battery", "box", "camera", "capsule", "collision", "cone", "contact", "cylinder", "ellipsoid",
                        "force_torque", "frame", "geometry", "gps", "gripper", "gui", "heightmap", "image", "imu",
                        "inertial", "joint", "joint_state", "lidar", "light", "light_state", "link", "link_state",
                        "logical_camera", "magnetometer", "material", "mesh", "mimic", "model", "model_state", "navsat",
                        "noise", "particle_emitter", "physics", "plane", "plugin", "polyline", "population", "pose",
                        "projector", "ray", "rfid", "rfidtag", "road", "scene", "sdf", "sensor", "sonar", "sphere",
                        "spherical_coordinates", "state", "surface", "transceiver", "visual", "world"]
TAG_CLASS_MAP: dict[str, type] = {
    "actor": Actor,
    "air_pressure": AirPressure,
    "air_speed": AirSpeed,
    "altimeter": Altimeter,
    "atmosphere": Atmosphere,
    "audio_sink": AudioSink,
    "audio_source": AudioSource,
    "battery": Battery,
    "box": Box,
    "camera": Camera,
    "capsule": Capsule,
    "collision": Collision,
    "cone": Cone,
    "contact": Contact,
    "cylinder": Cylinder,
    "ellipsoid": Ellipsoid,
    "force_torque": ForceTorque,
    "frame": Frame,
    "geometry": Geometry,
    "gps": Gps,
    "gripper": Gripper,
    "gui": Gui,
    "heightmap": Heightmap,
    "image": Image,
    "imu": Imu,
    "inertial": Inertial,
    "joint": Joint,
    "joint_state": JointState,
    "lidar": Lidar,
    "light": Light,
    "light_state": LightState,
    "link": Link,
    "link_state": LinkState,
    "logical_camera": LogicalCamera,
    "magnetometer": Magnetometer,
    "material": Material,
    "mesh": Mesh,
    "mimic": Mimic,
    "model": Model,
    "model_state": ModelState,
    "navsat": Navsat,
    "noise": Noise,
    "particle_emitter": ParticleEmitter,
    "physics": Physics,
    "plane": Plane,
    "plugin": Plugin,
    "polyline": Polyline,
    "population": Population,
    "pose": Pose,
    "projector": Projector,
    "ray": Ray,
    "rfid": Rfid,
    "rfidtag": Rfidtag,
    "road": Road,
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
