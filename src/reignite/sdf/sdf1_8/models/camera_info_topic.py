from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_7.models.camera_info_topic import CameraInfoTopic as _PrevCameraInfoTopic


class CameraInfoTopic(_PrevCameraInfoTopic):
    def __init__(self, camera_info_topic: str = "__default__"):
        super().__init__(camera_info_topic=camera_info_topic)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CameraInfoTopic":
        _base = _PrevCameraInfoTopic.from_sdf(el)
        return cls(camera_info_topic=_base.camera_info_topic)
