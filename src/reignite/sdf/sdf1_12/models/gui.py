from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_11.models.pose import Pose as _PrevPose
from ...sdf1_11.models.camera import Camera as _PrevCamera
from ...sdf1_11.models.gui import Gui as _PrevGui
from ....utils.pose import Pose
from .plugin import Plugin


class Pose(_PrevPose):
    def __init__(
        self,
        pose: Pose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(pose=pose, relative_to=relative_to, rotation_format=rotation_format, degrees=degrees)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pose":
        _base = _PrevPose.from_sdf(el)
        return cls(pose=_base.pose, relative_to=_base.relative_to, rotation_format=_base.rotation_format, degrees=_base.degrees)


class Camera(_PrevCamera):
    def __init__(
        self,
        name: str = "user_camera",
        pose: "Pose" = None,
        view_controller: "ViewController" = None,
        projection_type: "ProjectionType" = None,
        track_visual: "TrackVisual" = None
    ):
        super().__init__(name=name, pose=pose)
        self.view_controller = view_controller
        self.projection_type = projection_type
        self.track_visual = track_visual

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.view_controller is not None:
            el.append(self.view_controller.to_sdf())
        if self.projection_type is not None:
            el.append(self.projection_type.to_sdf())
        if self.track_visual is not None:
            el.append(self.track_visual.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _base = _PrevCamera.from_sdf(el)
        _c_view_controller = el.find("view_controller")
        _view_controller = ViewController.from_sdf(_c_view_controller) if _c_view_controller is not None else None
        _c_projection_type = el.find("projection_type")
        _projection_type = ProjectionType.from_sdf(_c_projection_type) if _c_projection_type is not None else None
        _c_track_visual = el.find("track_visual")
        _track_visual = TrackVisual.from_sdf(_c_track_visual) if _c_track_visual is not None else None
        return cls(name=_base.name, pose=_base.pose, view_controller=_view_controller, projection_type=_projection_type, track_visual=_track_visual)


class Gui(_PrevGui):
    def __init__(
        self,
        fullscreen: bool = False,
        plugin: List["Plugin"] = None,
        camera: "Camera" = None
    ):
        super().__init__(fullscreen=fullscreen, plugin=plugin, camera=camera)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gui":
        _base = _PrevGui.from_sdf(el)
        return cls(fullscreen=_base.fullscreen, plugin=_base.plugin, camera=_base.camera)
