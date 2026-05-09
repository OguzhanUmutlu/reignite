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
from .cone import Cone
from .contact import Contact
from .cylinder import Cylinder
from .ellipsoid import Ellipsoid
from .force_torque import ForceTorque
from .frame import Frame
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
from .pose import Pose
from .projector import Projector
from .ray import Ray
from .rfid import Rfid
from .rfidtag import Rfidtag
from .road import Road
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

TAG_NAMES: list[str] = ["actor", "air_pressure", "air_speed", "altimeter", "atmosphere", "audio_sink", "audio_source",
                        "battery", "box", "camera", "capsule", "collision", "cone", "contact", "cylinder", "ellipsoid",
                        "force_torque", "frame", "geometry", "gps", "gripper", "gui", "heightmap", "image", "imu",
                        "inertial", "joint", "joint_state", "lidar", "light", "light_state", "link", "link_state",
                        "logical_camera", "magnetometer", "material", "mesh", "mimic", "model", "model_state", "navsat",
                        "noise", "particle_emitter", "physics", "plane", "plugin", "polyline", "population", "pose",
                        "projector", "ray", "rfid", "rfidtag", "road", "scene", "sdf", "sensor", "sonar", "sphere",
                        "spherical_coordinates", "state", "surface", "transceiver", "visual", "world"]
