from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_3.models.camera import Camera as _PrevCamera
from ...sdf1_3.models.gui import Gui as _PrevGui


class Camera(_PrevCamera):
    def __init__(
        self,
        name: str = "user_camera",
        view_controller: "ViewController" = None,
        pose: "Pose" = None,
        track_visual: "TrackVisual" = None
    ):
        super().__init__(name=name, pose=pose)
        self.view_controller = view_controller
        self.track_visual = track_visual

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.view_controller is not None:
            el.append(self.view_controller.to_sdf())
        if self.track_visual is not None:
            el.append(self.track_visual.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _base = _PrevCamera.from_sdf(el)
        _c_view_controller = el.find("view_controller")
        _view_controller = ViewController.from_sdf(_c_view_controller) if _c_view_controller is not None else None
        _c_track_visual = el.find("track_visual")
        _track_visual = TrackVisual.from_sdf(_c_track_visual) if _c_track_visual is not None else None
        return cls(name=_base.name, view_controller=_view_controller, pose=_base.pose, track_visual=_track_visual)


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
