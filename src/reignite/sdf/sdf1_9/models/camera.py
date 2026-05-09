from __future__ import annotations

from xml.etree import ElementTree as ET

from .box_type import BoxType
from .camera_info_topic import CameraInfoTopic
from .clip import Clip
from .depth_camera import DepthCamera
from .distortion import Distortion
from .horizontal_fov import HorizontalFov
from .image import Image
from .lens import Lens
from .optical_frame_id import OpticalFrameId
from .pose import Pose
from .save import Save
from .segmentation_type import SegmentationType
from .trigger_topic import TriggerTopic
from .triggered import Triggered
from .visibility_mask import VisibilityMask
from ...sdf1_8.models.camera import Camera as _PrevCamera
from ...sdf1_8.models.noise import Noise as _PrevNoise


class Noise(_PrevNoise):
    def __init__(
            self,
            type: str = "none",
            mean: "Mean" = None,
            stddev: "Stddev" = None,
            bias_mean: "BiasMean" = None,
            bias_stddev: "BiasStddev" = None,
            dynamic_bias_stddev: "DynamicBiasStddev" = None,
            dynamic_bias_correlation_time: "DynamicBiasCorrelationTime" = None,
            precision: "Precision" = None
    ):
        super().__init__(type=type, mean=mean, stddev=stddev)
        self.bias_mean = bias_mean
        self.bias_stddev = bias_stddev
        self.dynamic_bias_stddev = dynamic_bias_stddev
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time
        self.precision = precision

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.bias_mean is not None:
            el.append(self.bias_mean.to_sdf())
        if self.bias_stddev is not None:
            el.append(self.bias_stddev.to_sdf())
        if self.dynamic_bias_stddev is not None:
            el.append(self.dynamic_bias_stddev.to_sdf())
        if self.dynamic_bias_correlation_time is not None:
            el.append(self.dynamic_bias_correlation_time.to_sdf())
        if self.precision is not None:
            el.append(self.precision.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Noise":
        _base = _PrevNoise.from_sdf(el)
        _c_bias_mean = el.find("bias_mean")
        _bias_mean = BiasMean.from_sdf(_c_bias_mean) if _c_bias_mean is not None else None
        _c_bias_stddev = el.find("bias_stddev")
        _bias_stddev = BiasStddev.from_sdf(_c_bias_stddev) if _c_bias_stddev is not None else None
        _c_dynamic_bias_stddev = el.find("dynamic_bias_stddev")
        _dynamic_bias_stddev = DynamicBiasStddev.from_sdf(
            _c_dynamic_bias_stddev) if _c_dynamic_bias_stddev is not None else None
        _c_dynamic_bias_correlation_time = el.find("dynamic_bias_correlation_time")
        _dynamic_bias_correlation_time = DynamicBiasCorrelationTime.from_sdf(
            _c_dynamic_bias_correlation_time) if _c_dynamic_bias_correlation_time is not None else None
        _c_precision = el.find("precision")
        _precision = Precision.from_sdf(_c_precision) if _c_precision is not None else None
        return cls(type=_base.type, mean=_base.mean, stddev=_base.stddev, bias_mean=_bias_mean,
                   bias_stddev=_bias_stddev, dynamic_bias_stddev=_dynamic_bias_stddev,
                   dynamic_bias_correlation_time=_dynamic_bias_correlation_time, precision=_precision)


class Camera(_PrevCamera):
    def __init__(
            self,
            name: str = "__default__",
            pose: "Pose" = None,
            camera_info_topic: "CameraInfoTopic" = None,
            triggered: "Triggered" = None,
            trigger_topic: "TriggerTopic" = None,
            horizontal_fov: "HorizontalFov" = None,
            image: "Image" = None,
            clip: "Clip" = None,
            save: "Save" = None,
            depth_camera: "DepthCamera" = None,
            segmentation_type: "SegmentationType" = None,
            box_type: "BoxType" = None,
            noise: "Noise" = None,
            distortion: "Distortion" = None,
            lens: "Lens" = None,
            visibility_mask: "VisibilityMask" = None,
            optical_frame_id: "OpticalFrameId" = None
    ):
        super().__init__(name=name, pose=pose, camera_info_topic=camera_info_topic, horizontal_fov=horizontal_fov,
                         image=image, clip=clip, save=save, depth_camera=depth_camera, noise=noise,
                         distortion=distortion, lens=lens, visibility_mask=visibility_mask,
                         optical_frame_id=optical_frame_id)
        self.triggered = triggered
        self.trigger_topic = trigger_topic
        self.segmentation_type = segmentation_type
        self.box_type = box_type

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.triggered is not None:
            el.append(self.triggered.to_sdf())
        if self.trigger_topic is not None:
            el.append(self.trigger_topic.to_sdf())
        if self.segmentation_type is not None:
            el.append(self.segmentation_type.to_sdf())
        if self.box_type is not None:
            el.append(self.box_type.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Camera":
        _base = _PrevCamera.from_sdf(el)
        _c_triggered = el.find("triggered")
        _triggered = Triggered.from_sdf(_c_triggered) if _c_triggered is not None else None
        _c_trigger_topic = el.find("trigger_topic")
        _trigger_topic = TriggerTopic.from_sdf(_c_trigger_topic) if _c_trigger_topic is not None else None
        _c_segmentation_type = el.find("segmentation_type")
        _segmentation_type = SegmentationType.from_sdf(
            _c_segmentation_type) if _c_segmentation_type is not None else None
        _c_box_type = el.find("box_type")
        _box_type = BoxType.from_sdf(_c_box_type) if _c_box_type is not None else None
        return cls(name=_base.name, pose=_base.pose, camera_info_topic=_base.camera_info_topic, triggered=_triggered,
                   trigger_topic=_trigger_topic, horizontal_fov=_base.horizontal_fov, image=_base.image,
                   clip=_base.clip, save=_base.save, depth_camera=_base.depth_camera,
                   segmentation_type=_segmentation_type, box_type=_box_type, noise=_base.noise,
                   distortion=_base.distortion, lens=_base.lens, visibility_mask=_base.visibility_mask,
                   optical_frame_id=_base.optical_frame_id)
