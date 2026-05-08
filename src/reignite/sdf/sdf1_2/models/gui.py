from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.camera import Camera as _PrevCamera
from ...sdf1_0.models.gui import Gui as _PrevGui


class Camera(_PrevCamera):
    def __init__(
        self,
        name: str = "user_camera",
        view_controller: "ViewController" = None,
        pose: "Pose" = None,
        track_visual: "TrackVisual" = None
    ):
        super().__init__()
        self.name = name
        self.view_controller = view_controller
        self.pose = pose
        self.track_visual = track_visual

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
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


class Gui(_PrevGui):
    def __init__(self, fullscreen: bool = False, camera: "Camera" = None):
        super().__init__(fullscreen=fullscreen, camera=camera)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gui":
        _base = _PrevGui.from_sdf(el)
        return cls(fullscreen=_base.fullscreen, camera=_base.camera)
