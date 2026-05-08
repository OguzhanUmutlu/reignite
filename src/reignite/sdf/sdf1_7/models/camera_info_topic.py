from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class CameraInfoTopic(Model):
    def __init__(self, camera_info_topic: str = "__default__"):
        self.camera_info_topic = camera_info_topic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("camera_info_topic")
        if self.camera_info_topic is not None:
            el.text = self.camera_info_topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CameraInfoTopic":
        _text = el.text or "__default__"
        _camera_info_topic = _text
        return cls(camera_info_topic=_camera_info_topic)
