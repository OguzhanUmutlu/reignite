from __future__ import annotations

from . import models as _models

Actor = _models.Actor
Camera = _models.Camera
Collision = _models.Collision
Contact = _models.Contact
Gazebo = _models.Gazebo
Geometry = _models.Geometry
Gripper = _models.Gripper
Gui = _models.Gui
Inertial = _models.Inertial
Joint = _models.Joint
Light = _models.Light
Link = _models.Link
Model = _models.Model
Physics = _models.Physics
Plugin = _models.Plugin
Projector = _models.Projector
Ray = _models.Ray
Rfid = _models.Rfid
Rfidtag = _models.Rfidtag
Road = _models.Road
Robot = _models.Robot
Scene = _models.Scene
Sensor = _models.Sensor
State = _models.State
Surface = _models.Surface
Visual = _models.Visual
World = _models.World

TAG_NAMES: list[str] = ["actor", "camera", "collision", "contact", "gazebo", "geometry", "gripper", "gui", "inertial",
                        "joint", "light", "link", "model", "physics", "plugin", "projector", "ray", "rfid", "rfidtag",
                        "road", "robot", "scene", "sensor", "state", "surface", "visual", "world"]
TAG_CLASS_MAP: dict[str, type] = {
    "actor": Actor,
    "camera": Camera,
    "collision": Collision,
    "contact": Contact,
    "gazebo": Gazebo,
    "geometry": Geometry,
    "gripper": Gripper,
    "gui": Gui,
    "inertial": Inertial,
    "joint": Joint,
    "light": Light,
    "link": Link,
    "model": Model,
    "physics": Physics,
    "plugin": Plugin,
    "projector": Projector,
    "ray": Ray,
    "rfid": Rfid,
    "rfidtag": Rfidtag,
    "road": Road,
    "robot": Robot,
    "scene": Scene,
    "sensor": Sensor,
    "state": State,
    "surface": Surface,
    "visual": Visual,
    "world": World,
}


def get_tag_class(tag: str) -> type | None:
    return TAG_CLASS_MAP.get(tag)
