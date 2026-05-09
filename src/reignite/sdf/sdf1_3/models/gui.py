from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.pose import Pose


class Pose(Model):
    def __init__(self, pose: Pose = None):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        return cls(pose=_pose)


class Camera(Model):
    def __init__(
            self,
            name: str = "user_camera",
            view_controller: "ViewController" = None,
            pose: "Pose" = None,
            track_visual: "TrackVisual" = None
    ):
        self.name = name
        self.view_controller = view_controller
        self.pose = pose
        self.track_visual = track_visual

    def to_sdf(self) -> ET.Element:
        el = ET.Element("camera")
        if self.name is not None:
            el.set("name", self.name)
        if self.view_controller is not None:
            el.append(self.view_controller.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.track_visual is not None:
            el.append(self.track_visual.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _name = el.get("name", "user_camera")
        _c_view_controller = el.find("view_controller")
        _view_controller = ViewController.from_sdf(_c_view_controller) if _c_view_controller is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_track_visual = el.find("track_visual")
        _track_visual = TrackVisual.from_sdf(_c_track_visual) if _c_track_visual is not None else None
        return cls(name=_name, view_controller=_view_controller, pose=_pose, track_visual=_track_visual)


class Gui(Model):
    def __init__(self, fullscreen: bool = False, camera: "Camera" = None):
        self.fullscreen = fullscreen
        self.camera = camera

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gui")
        if self.fullscreen is not None:
            el.set("fullscreen", str(self.fullscreen).lower())
        if self.camera is not None:
            el.append(self.camera.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gui":
        _fullscreen = el.get("fullscreen", False).strip().lower() == 'true'
        _c_camera = el.find("camera")
        _camera = Camera.from_sdf(_c_camera) if _c_camera is not None else None
        return cls(fullscreen=_fullscreen, camera=_camera)
