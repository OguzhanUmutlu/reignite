from __future__ import annotations

from .actor import Actor
from .camera import Camera
from .collision import Collision
from .contact import Contact
from .geometry import Geometry
from .gripper import Gripper
from .gui import Gui
from .imu import Imu
from .inertial import Inertial
from .joint import Joint
from .light import Light
from .link import Link
from .model import Model
from .physics import Physics
from .plugin import Plugin
from .projector import Projector
from .ray import Ray
from .rfid import Rfid
from .rfidtag import Rfidtag
from .road import Road
from .robot import Robot
from .scene import Scene
from .sdf import Sdf
from .sensor import Sensor
from .state import State
from .surface import Surface
from .visual import Visual
from .world import World

TAG_NAMES: list[str] = ["actor", "camera", "collision", "contact", "geometry", "gripper", "gui", "imu", "inertial",
                        "joint", "light", "link", "model", "physics", "plugin", "projector", "ray", "rfid", "rfidtag",
                        "road", "robot", "scene", "sdf", "sensor", "state", "surface", "visual", "world"]
