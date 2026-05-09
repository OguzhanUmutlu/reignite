from __future__ import annotations

from xml.etree import ElementTree as ET

from .clip import Clip
from .depth_camera import DepthCamera
from .horizontal_fov import HorizontalFov
from .image import Image
from .pose import Pose
from .save import Save
from ...sdf1_2.models.camera import Camera as _PrevCamera


class Camera(_PrevCamera):
    def __init__(
            self,
            name: str = "__default__",
            pose: "Pose" = None,
            horizontal_fov: "HorizontalFov" = None,
            image: "Image" = None,
            clip: "Clip" = None,
            save: "Save" = None,
            depth_camera: "DepthCamera" = None
    ):
        super().__init__(horizontal_fov=horizontal_fov, image=image, clip=clip, save=save, depth_camera=depth_camera)
        self.name = name
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _base = _PrevCamera.from_sdf(el)
        _name = el.get("name", "__default__")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_name, pose=_pose, horizontal_fov=_base.horizontal_fov, image=_base.image, clip=_base.clip,
                   save=_base.save, depth_camera=_base.depth_camera)
