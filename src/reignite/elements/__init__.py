### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from .actor import Actor
from .air_pressure import AirPressure
from .air_speed import AirSpeed
from .altimeter import Altimeter
from .atmosphere import Atmosphere
from .audio_sink import AudioSink
from .audio_source import AudioSource
from .battery import Battery
from .box import Box
from .camera import Camera
from .capsule import Capsule
from .collision import Collision
from .collision_engine import CollisionEngine
from .cone import Cone
from .contact import Contact
from .cylinder import Cylinder
from .ellipsoid import Ellipsoid
from .force_torque import ForceTorque
from .frame import Frame
from .gazebo import Gazebo
from .geometry import Geometry
from .gps import Gps
from .gripper import Gripper
from .gui import Gui
from .heightmap import Heightmap
from .image import Image
from .imu import Imu
from .inertial import Inertial
from .joint import Joint
from .joint_state import JointState
from .lidar import Lidar
from .light import Light
from .light_state import LightState
from .link import Link
from .link_state import LinkState
from .logical_camera import LogicalCamera
from .magnetometer import Magnetometer
from .material import Material
from .mesh import Mesh
from .mimic import Mimic
from .model import Model
from .model_state import ModelState
from .navsat import Navsat
from .noise import Noise
from .particle_emitter import ParticleEmitter
from .physics import Physics
from .plane import Plane
from .plugin import Plugin
from .polyline import Polyline
from .population import Population
from .projector import Projector
from .ray import Ray
from .rfid import Rfid
from .rfidtag import Rfidtag
from .road import Road
from .robot import Robot
from .scene import Scene
from .sdf import Sdf
from .sensor import Sensor
from .sonar import Sonar
from .sphere import Sphere
from .spherical_coordinates import SphericalCoordinates
from .state import State
from .surface import Surface
from .transceiver import Transceiver
from .visual import Visual
from .world import World

ELEMENT_NAMES: list[str] = ["actor", "air_pressure", "air_speed", "altimeter", "atmosphere", "audio_sink", "audio_source", "battery", "box", "camera", "capsule", "collision", "collision_engine", "cone", "contact", "cylinder", "ellipsoid", "force_torque", "frame", "gazebo", "geometry", "gps", "gripper", "gui", "heightmap", "image", "imu", "inertial", "joint", "joint_state", "lidar", "light", "light_state", "link", "link_state", "logical_camera", "magnetometer", "material", "mesh", "mimic", "model", "model_state", "navsat", "noise", "particle_emitter", "physics", "plane", "plugin", "polyline", "population", "projector", "ray", "rfid", "rfidtag", "road", "robot", "scene", "sdf", "sensor", "sonar", "sphere", "spherical_coordinates", "state", "surface", "transceiver", "visual", "world"]

ELEMENT_CLASS_MAP: dict[str, type] = {
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
    "collision_engine": CollisionEngine,
    "cone": Cone,
    "contact": Contact,
    "cylinder": Cylinder,
    "ellipsoid": Ellipsoid,
    "force_torque": ForceTorque,
    "frame": Frame,
    "gazebo": Gazebo,
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

def get_element_class(element: str) -> type | None:
    return ELEMENT_CLASS_MAP.get(element)
