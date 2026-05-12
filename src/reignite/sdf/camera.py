### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector2d import Vector2d as _SDFVector2d
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.pose import Pose


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class AntiAliasing(BaseModel):
    def __init__(self, sdf_version: str | None = None, anti_aliasing: int = 4):
        self.__version__ = sdf_version
        self.anti_aliasing = anti_aliasing

    def to_version(self, target_version: str) -> "AntiAliasing":
        if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["anti_aliasing"] = self.anti_aliasing
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("anti_aliasing")
        if self.anti_aliasing is not None:
            el.text = str(self.anti_aliasing)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4
        _anti_aliasing = _parse_int32(_text)
        if isinstance(_anti_aliasing, SDFError):
            return _anti_aliasing
        if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
            if _anti_aliasing != 4:
                return SDFError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, anti_aliasing=_anti_aliasing)


class BoxType(BaseModel):
    def __init__(self, sdf_version: str | None = None, box_type: str = "2d"):
        self.__version__ = sdf_version
        self.box_type = box_type

    def to_version(self, target_version: str) -> "BoxType":
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["box_type"] = self.box_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("box_type")
        if self.box_type is not None:
            el.text = self.box_type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "2d"
        _box_type = _text
        if isinstance(_box_type, SDFError):
            return _box_type
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            if _box_type != "2d":
                return SDFError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, box_type=_box_type)


class C1(BaseModel):
    def __init__(self, sdf_version: str | None = None, c1: float = 1):
        self.__version__ = sdf_version
        self.c1 = c1

    def to_version(self, target_version: str) -> "C1":
        kwargs = {"sdf_version": target_version}
        kwargs["c1"] = self.c1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("c1")
        if self.c1 is not None:
            el.text = str(self.c1)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _c1 = _parse_double(_text)
        if isinstance(_c1, SDFError):
            return _c1
        return cls(sdf_version=version, c1=_c1)


class C2(BaseModel):
    def __init__(self, sdf_version: str | None = None, c2: float = 1):
        self.__version__ = sdf_version
        self.c2 = c2

    def to_version(self, target_version: str) -> "C2":
        kwargs = {"sdf_version": target_version}
        kwargs["c2"] = self.c2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("c2")
        if self.c2 is not None:
            el.text = str(self.c2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _c2 = _parse_double(_text)
        if isinstance(_c2, SDFError):
            return _c2
        return cls(sdf_version=version, c2=_c2)


class C3(BaseModel):
    def __init__(self, sdf_version: str | None = None, c3: float = 0):
        self.__version__ = sdf_version
        self.c3 = c3

    def to_version(self, target_version: str) -> "C3":
        kwargs = {"sdf_version": target_version}
        kwargs["c3"] = self.c3
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("c3")
        if self.c3 is not None:
            el.text = str(self.c3)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _c3 = _parse_double(_text)
        if isinstance(_c3, SDFError):
            return _c3
        return cls(sdf_version=version, c3=_c3)


class Camera(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        box_type: "BoxType" = None,
        camera_info_topic: "CameraInfoTopic" = None,
        clip: "Clip" = None,
        depth_camera: "DepthCamera" = None,
        distortion: "Distortion" = None,
        frames: List["Frame"] = None,
        horizontal_fov: "HorizontalFov" = None,
        image: "Image" = None,
        lens: "Lens" = None,
        name: str = "__default__",
        noise: "Noise" = None,
        optical_frame_id: "OpticalFrameId" = None,
        pose: "Pose" = None,
        save: "Save" = None,
        segmentation_type: "SegmentationType" = None,
        trigger_topic: "TriggerTopic" = None,
        triggered: "Triggered" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.box_type = box_type
        self.camera_info_topic = camera_info_topic
        self.clip = clip
        self.depth_camera = depth_camera
        self.distortion = distortion
        self.frames = frames or []
        self.horizontal_fov = horizontal_fov
        self.image = image
        self.lens = lens
        self.name = name
        self.noise = noise
        self.optical_frame_id = optical_frame_id
        self.pose = pose
        self.save = save
        self.segmentation_type = segmentation_type
        self.trigger_topic = trigger_topic
        self.triggered = triggered
        self.visibility_mask = visibility_mask
        if self.box_type is not None:
            if getattr(self.box_type, '__version__', None) is None:
                self.box_type.__version__ = self.__version__
            elif getattr(self.box_type, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.box_type = self.box_type.to_version(self.__version__)
        if self.camera_info_topic is not None:
            if getattr(self.camera_info_topic, '__version__', None) is None:
                self.camera_info_topic.__version__ = self.__version__
            elif getattr(self.camera_info_topic, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.camera_info_topic = self.camera_info_topic.to_version(self.__version__)
        if self.clip is not None:
            if getattr(self.clip, '__version__', None) is None:
                self.clip.__version__ = self.__version__
            elif getattr(self.clip, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.clip = self.clip.to_version(self.__version__)
        if self.depth_camera is not None:
            if getattr(self.depth_camera, '__version__', None) is None:
                self.depth_camera.__version__ = self.__version__
            elif getattr(self.depth_camera, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.depth_camera = self.depth_camera.to_version(self.__version__)
        if self.distortion is not None:
            if getattr(self.distortion, '__version__', None) is None:
                self.distortion.__version__ = self.__version__
            elif getattr(self.distortion, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.distortion = self.distortion.to_version(self.__version__)
        for _i, _c in enumerate(self.frames):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        if self.horizontal_fov is not None:
            if getattr(self.horizontal_fov, '__version__', None) is None:
                self.horizontal_fov.__version__ = self.__version__
            elif getattr(self.horizontal_fov, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.horizontal_fov = self.horizontal_fov.to_version(self.__version__)
        if self.image is not None:
            if getattr(self.image, '__version__', None) is None:
                self.image.__version__ = self.__version__
            elif getattr(self.image, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.image = self.image.to_version(self.__version__)
        if self.lens is not None:
            if getattr(self.lens, '__version__', None) is None:
                self.lens.__version__ = self.__version__
            elif getattr(self.lens, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.lens = self.lens.to_version(self.__version__)
        if self.noise is not None:
            if getattr(self.noise, '__version__', None) is None:
                self.noise.__version__ = self.__version__
            elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.noise = self.noise.to_version(self.__version__)
        if self.optical_frame_id is not None:
            if getattr(self.optical_frame_id, '__version__', None) is None:
                self.optical_frame_id.__version__ = self.__version__
            elif getattr(self.optical_frame_id, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.optical_frame_id = self.optical_frame_id.to_version(self.__version__)
        if self.pose is not None:
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)
        if self.save is not None:
            if getattr(self.save, '__version__', None) is None:
                self.save.__version__ = self.__version__
            elif getattr(self.save, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.save = self.save.to_version(self.__version__)
        if self.segmentation_type is not None:
            if getattr(self.segmentation_type, '__version__', None) is None:
                self.segmentation_type.__version__ = self.__version__
            elif getattr(self.segmentation_type, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.segmentation_type = self.segmentation_type.to_version(self.__version__)
        if self.trigger_topic is not None:
            if getattr(self.trigger_topic, '__version__', None) is None:
                self.trigger_topic.__version__ = self.__version__
            elif getattr(self.trigger_topic, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.trigger_topic = self.trigger_topic.to_version(self.__version__)
        if self.triggered is not None:
            if getattr(self.triggered, '__version__', None) is None:
                self.triggered.__version__ = self.__version__
            elif getattr(self.triggered, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.triggered = self.triggered.to_version(self.__version__)
        if self.visibility_mask is not None:
            if getattr(self.visibility_mask, '__version__', None) is None:
                self.visibility_mask.__version__ = self.__version__
            elif getattr(self.visibility_mask, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.visibility_mask = self.visibility_mask.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Camera":
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        if self.distortion is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'distortion' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.lens is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'lens' is not supported in SDF version {target_version} (added in 1.5)")
        if self.name is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (added in 1.3)")
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        if self.pose is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.3)")
        if self.segmentation_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.9)")
        if self.trigger_topic is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.9)")
        if self.triggered is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.9)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["box_type"] = self.box_type.to_version(target_version) if self.box_type is not None else None
        kwargs["camera_info_topic"] = self.camera_info_topic.to_version(target_version) if self.camera_info_topic is not None else None
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        kwargs["depth_camera"] = self.depth_camera.to_version(target_version) if self.depth_camera is not None else None
        kwargs["distortion"] = self.distortion.to_version(target_version) if self.distortion is not None else None
        kwargs["frames"] = [c.to_version(target_version) for c in (self.frames or [])]
        kwargs["horizontal_fov"] = self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["lens"] = self.lens.to_version(target_version) if self.lens is not None else None
        kwargs["name"] = self.name
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["optical_frame_id"] = self.optical_frame_id.to_version(target_version) if self.optical_frame_id is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["save"] = self.save.to_version(target_version) if self.save is not None else None
        kwargs["segmentation_type"] = self.segmentation_type.to_version(target_version) if self.segmentation_type is not None else None
        kwargs["trigger_topic"] = self.trigger_topic.to_version(target_version) if self.trigger_topic is not None else None
        kwargs["triggered"] = self.triggered.to_version(target_version) if self.triggered is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("camera")
        if self.box_type is not None:
            el.append(self.box_type.to_sdf(version))
        if self.camera_info_topic is not None:
            el.append(self.camera_info_topic.to_sdf(version))
        if self.clip is None:
            self.clip = Clip(sdf_version=version)
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        if self.depth_camera is not None:
            el.append(self.depth_camera.to_sdf(version))
        if self.distortion is not None:
            el.append(self.distortion.to_sdf(version))
        for item in (self.frames or []):
            el.append(item.to_sdf(version))
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf(version))
        if self.image is None:
            self.image = Image(sdf_version=version)
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.lens is not None:
            el.append(self.lens.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.optical_frame_id is not None:
            el.append(self.optical_frame_id.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.save is not None:
            el.append(self.save.to_sdf(version))
        if self.segmentation_type is not None:
            el.append(self.segmentation_type.to_sdf(version))
        if self.trigger_topic is not None:
            el.append(self.trigger_topic.to_sdf(version))
        if self.triggered is not None:
            el.append(self.triggered.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        _c_box_type = el.find("box_type")
        if _c_box_type is not None:
            _res = BoxType._from_sdf(_c_box_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("box_type")
            _box_type = _res
        else:
            _box_type = None
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        _c_camera_info_topic = el.find("camera_info_topic")
        if _c_camera_info_topic is not None:
            _res = CameraInfoTopic._from_sdf(_c_camera_info_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("camera_info_topic")
            _camera_info_topic = _res
        else:
            _camera_info_topic = None
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        _c_clip = el.find("clip")
        if _c_clip is not None:
            _res = Clip._from_sdf(_c_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        else:
            _res = Clip._from_sdf(ET.Element("clip"), version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        _c_depth_camera = el.find("depth_camera")
        if _c_depth_camera is not None:
            _res = DepthCamera._from_sdf(_c_depth_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("depth_camera")
            _depth_camera = _res
        else:
            _depth_camera = None
        _c_distortion = el.find("distortion")
        if _c_distortion is not None:
            _res = Distortion._from_sdf(_c_distortion, version)
            if isinstance(_res, SDFError):
                return _res.extend("distortion")
            _distortion = _res
        else:
            _distortion = None
        if _distortion is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'distortion' is not supported in SDF version {version} (added in 1.5)")
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        if _frames and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frames' is not supported in SDF version {version} (added in 1.5)")
        _c_horizontal_fov = el.find("horizontal_fov")
        if _c_horizontal_fov is not None:
            _res = HorizontalFov._from_sdf(_c_horizontal_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal_fov")
            _horizontal_fov = _res
        else:
            _horizontal_fov = None
        _c_image = el.find("image")
        if _c_image is not None:
            _res = Image._from_sdf(_c_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        else:
            _res = Image._from_sdf(ET.Element("image"), version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        _c_lens = el.find("lens")
        if _c_lens is not None:
            _res = Lens._from_sdf(_c_lens, version)
            if isinstance(_res, SDFError):
                return _res.extend("lens")
            _lens = _res
        else:
            _lens = None
        if _lens is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'lens' is not supported in SDF version {version} (added in 1.5)")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        if _name is not None and cmp_version(version, "1.3") < 0:
            if _name != "__default__":
                return SDFError(f"'name' is not supported in SDF version {version} (added in 1.3)")
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_optical_frame_id = el.find("optical_frame_id")
        if _c_optical_frame_id is not None:
            _res = OpticalFrameId._from_sdf(_c_optical_frame_id, version)
            if isinstance(_res, SDFError):
                return _res.extend("optical_frame_id")
            _optical_frame_id = _res
        else:
            _optical_frame_id = None
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.3)")
        _c_save = el.find("save")
        if _c_save is not None:
            _res = Save._from_sdf(_c_save, version)
            if isinstance(_res, SDFError):
                return _res.extend("save")
            _save = _res
        else:
            _save = None
        _c_segmentation_type = el.find("segmentation_type")
        if _c_segmentation_type is not None:
            _res = SegmentationType._from_sdf(_c_segmentation_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("segmentation_type")
            _segmentation_type = _res
        else:
            _segmentation_type = None
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        _c_trigger_topic = el.find("trigger_topic")
        if _c_trigger_topic is not None:
            _res = TriggerTopic._from_sdf(_c_trigger_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("trigger_topic")
            _trigger_topic = _res
        else:
            _trigger_topic = None
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        _c_triggered = el.find("triggered")
        if _c_triggered is not None:
            _res = Triggered._from_sdf(_c_triggered, version)
            if isinstance(_res, SDFError):
                return _res.extend("triggered")
            _triggered = _res
        else:
            _triggered = None
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        _c_visibility_mask = el.find("visibility_mask")
        if _c_visibility_mask is not None:
            _res = VisibilityMask._from_sdf(_c_visibility_mask, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_mask")
            _visibility_mask = _res
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, box_type=_box_type, camera_info_topic=_camera_info_topic, clip=_clip, depth_camera=_depth_camera, distortion=_distortion, frames=_frames, horizontal_fov=_horizontal_fov, image=_image, lens=_lens, name=_name, noise=_noise, optical_frame_id=_optical_frame_id, pose=_pose, save=_save, segmentation_type=_segmentation_type, trigger_topic=_trigger_topic, triggered=_triggered, visibility_mask=_visibility_mask)


class CameraInfoTopic(BaseModel):
    def __init__(self, sdf_version: str | None = None, camera_info_topic: str = "__default__"):
        self.__version__ = sdf_version
        self.camera_info_topic = camera_info_topic

    def to_version(self, target_version: str) -> "CameraInfoTopic":
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["camera_info_topic"] = self.camera_info_topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("camera_info_topic")
        if self.camera_info_topic is not None:
            el.text = self.camera_info_topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _camera_info_topic = _text
        if isinstance(_camera_info_topic, SDFError):
            return _camera_info_topic
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            if _camera_info_topic != "__default__":
                return SDFError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, camera_info_topic=_camera_info_topic)


class Center(BaseModel):
    def __init__(self, sdf_version: str | None = None, center: _SDFVector2d = None):
        self.__version__ = sdf_version
        if center is None:
            center = _SDFVector2d.from_sdf("0.5 0.5", version=sdf_version)
        self.center = center

    def to_version(self, target_version: str) -> "Center":
        kwargs = {"sdf_version": target_version}
        kwargs["center"] = self.center
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("center")
        if self.center is not None:
            el.text = self.center.to_sdf(version)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.5 0.5"
        _center = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_center, SDFError):
            return _center
        return cls(sdf_version=version, center=_center)


class Clip(BaseModel):
    def __init__(self, sdf_version: str | None = None, far: float = 100, near: float = .1):
        self.__version__ = sdf_version
        self.far = far
        self.near = near

    def to_version(self, target_version: str) -> "Clip":
        if self.far is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'far' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.near is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'near' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        kwargs["near"] = self.near
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("clip")
        if self.far is not None:
            el.set("far", str(self.far))
        if self.near is not None:
            el.set("near", str(self.near))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _far = _parse_double(el.get("far", 100))
        if isinstance(_far, SDFError):
            return _far.extend("@far")
        _near = _parse_double(el.get("near", .1))
        if isinstance(_near, SDFError):
            return _near.extend("@near")
        return cls(sdf_version=version, far=_far, near=_near)


class ClipFar(BaseModel):
    def __init__(self, sdf_version: str | None = None, far: float = 10.0):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "ClipFar":
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("far")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10.0
        _far = _parse_double(_text)
        if isinstance(_far, SDFError):
            return _far
        return cls(sdf_version=version, far=_far)


class CustomFunction(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        c1: "C1" = None,
        c2: "C2" = None,
        c3: "C3" = None,
        f: "F" = None,
        fun: "Fun" = None
    ):
        self.__version__ = sdf_version
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.f = f
        self.fun = fun
        if self.c1 is not None:
            if getattr(self.c1, '__version__', None) is None:
                self.c1.__version__ = self.__version__
            elif getattr(self.c1, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.c1 = self.c1.to_version(self.__version__)
        if self.c2 is not None:
            if getattr(self.c2, '__version__', None) is None:
                self.c2.__version__ = self.__version__
            elif getattr(self.c2, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.c2 = self.c2.to_version(self.__version__)
        if self.c3 is not None:
            if getattr(self.c3, '__version__', None) is None:
                self.c3.__version__ = self.__version__
            elif getattr(self.c3, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.c3 = self.c3.to_version(self.__version__)
        if self.f is not None:
            if getattr(self.f, '__version__', None) is None:
                self.f.__version__ = self.__version__
            elif getattr(self.f, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.f = self.f.to_version(self.__version__)
        if self.fun is not None:
            if getattr(self.fun, '__version__', None) is None:
                self.fun.__version__ = self.__version__
            elif getattr(self.fun, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.fun = self.fun.to_version(self.__version__)

    def to_version(self, target_version: str) -> "CustomFunction":
        kwargs = {"sdf_version": target_version}
        kwargs["c1"] = self.c1.to_version(target_version) if self.c1 is not None else None
        kwargs["c2"] = self.c2.to_version(target_version) if self.c2 is not None else None
        kwargs["c3"] = self.c3.to_version(target_version) if self.c3 is not None else None
        kwargs["f"] = self.f.to_version(target_version) if self.f is not None else None
        kwargs["fun"] = self.fun.to_version(target_version) if self.fun is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("custom_function")
        if self.c1 is not None:
            el.append(self.c1.to_sdf(version))
        if self.c2 is not None:
            el.append(self.c2.to_sdf(version))
        if self.c3 is not None:
            el.append(self.c3.to_sdf(version))
        if self.f is not None:
            el.append(self.f.to_sdf(version))
        if self.fun is not None:
            el.append(self.fun.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_c1 = el.find("c1")
        if _c_c1 is not None:
            _res = C1._from_sdf(_c_c1, version)
            if isinstance(_res, SDFError):
                return _res.extend("c1")
            _c1 = _res
        else:
            _c1 = None
        _c_c2 = el.find("c2")
        if _c_c2 is not None:
            _res = C2._from_sdf(_c_c2, version)
            if isinstance(_res, SDFError):
                return _res.extend("c2")
            _c2 = _res
        else:
            _c2 = None
        _c_c3 = el.find("c3")
        if _c_c3 is not None:
            _res = C3._from_sdf(_c_c3, version)
            if isinstance(_res, SDFError):
                return _res.extend("c3")
            _c3 = _res
        else:
            _c3 = None
        _c_f = el.find("f")
        if _c_f is not None:
            _res = F._from_sdf(_c_f, version)
            if isinstance(_res, SDFError):
                return _res.extend("f")
            _f = _res
        else:
            _f = None
        _c_fun = el.find("fun")
        if _c_fun is not None:
            _res = Fun._from_sdf(_c_fun, version)
            if isinstance(_res, SDFError):
                return _res.extend("fun")
            _fun = _res
        else:
            _fun = None
        return cls(sdf_version=version, c1=_c1, c2=_c2, c3=_c3, f=_f, fun=_fun)


class CutoffAngle(BaseModel):
    def __init__(self, sdf_version: str | None = None, cutoff_angle: float = 1.5707):
        self.__version__ = sdf_version
        self.cutoff_angle = cutoff_angle

    def to_version(self, target_version: str) -> "CutoffAngle":
        kwargs = {"sdf_version": target_version}
        kwargs["cutoff_angle"] = self.cutoff_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("cutoff_angle")
        if self.cutoff_angle is not None:
            el.text = str(self.cutoff_angle)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.5707
        _cutoff_angle = _parse_double(_text)
        if isinstance(_cutoff_angle, SDFError):
            return _cutoff_angle
        return cls(sdf_version=version, cutoff_angle=_cutoff_angle)


class Cx(BaseModel):
    def __init__(self, sdf_version: str | None = None, cx: float = 160):
        self.__version__ = sdf_version
        self.cx = cx

    def to_version(self, target_version: str) -> "Cx":
        kwargs = {"sdf_version": target_version}
        kwargs["cx"] = self.cx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("cx")
        if self.cx is not None:
            el.text = str(self.cx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 160
        _cx = _parse_double(_text)
        if isinstance(_cx, SDFError):
            return _cx
        return cls(sdf_version=version, cx=_cx)


class Cy(BaseModel):
    def __init__(self, sdf_version: str | None = None, cy: float = 120):
        self.__version__ = sdf_version
        self.cy = cy

    def to_version(self, target_version: str) -> "Cy":
        kwargs = {"sdf_version": target_version}
        kwargs["cy"] = self.cy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("cy")
        if self.cy is not None:
            el.text = str(self.cy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 120
        _cy = _parse_double(_text)
        if isinstance(_cy, SDFError):
            return _cy
        return cls(sdf_version=version, cy=_cy)


class DepthCamera(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        clip: "DepthCameraClip" = None,
        output: str = "depths"
    ):
        self.__version__ = sdf_version
        self.clip = clip
        self.output = output
        if self.clip is not None:
            if getattr(self.clip, '__version__', None) is None:
                self.clip.__version__ = self.__version__
            elif getattr(self.clip, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.clip = self.clip.to_version(self.__version__)

    def to_version(self, target_version: str) -> "DepthCamera":
        if self.clip is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'clip' is not supported in SDF version {target_version} (added in 1.6)")
        if self.output is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'output' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        kwargs["output"] = self.output
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("depth_camera")
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        if self.output is not None:
            el.set("output", self.output)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_clip = el.find("clip")
        if _c_clip is not None:
            _res = DepthCameraClip._from_sdf(_c_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        else:
            _clip = None
        if _clip is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'clip' is not supported in SDF version {version} (added in 1.6)")
        _output = el.get("output", "depths")
        if isinstance(_output, SDFError):
            return _output.extend("@output")
        return cls(sdf_version=version, clip=_clip, output=_output)


class DepthCameraClip(BaseModel):
    def __init__(self, sdf_version: str | None = None, far: "ClipFar" = None, near: "Near" = None):
        self.__version__ = sdf_version
        self.far = far
        self.near = near
        if self.far is not None:
            if getattr(self.far, '__version__', None) is None:
                self.far.__version__ = self.__version__
            elif getattr(self.far, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.far = self.far.to_version(self.__version__)
        if self.near is not None:
            if getattr(self.near, '__version__', None) is None:
                self.near.__version__ = self.__version__
            elif getattr(self.near, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.near = self.near.to_version(self.__version__)

    def to_version(self, target_version: str) -> "DepthCameraClip":
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far.to_version(target_version) if self.far is not None else None
        kwargs["near"] = self.near.to_version(target_version) if self.near is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("clip")
        if self.far is not None:
            el.append(self.far.to_sdf(version))
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_far = el.find("far")
        if _c_far is not None:
            _res = ClipFar._from_sdf(_c_far, version)
            if isinstance(_res, SDFError):
                return _res.extend("far")
            _far = _res
        else:
            _far = None
        _c_near = el.find("near")
        if _c_near is not None:
            _res = Near._from_sdf(_c_near, version)
            if isinstance(_res, SDFError):
                return _res.extend("near")
            _near = _res
        else:
            _near = None
        return cls(sdf_version=version, far=_far, near=_near)


class Distortion(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        center: "Center" = None,
        k1: "K1" = None,
        k2: "K2" = None,
        k3: "K3" = None,
        p1: "P1" = None,
        p2: "P2" = None
    ):
        self.__version__ = sdf_version
        self.center = center
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.p1 = p1
        self.p2 = p2
        if self.center is not None:
            if getattr(self.center, '__version__', None) is None:
                self.center.__version__ = self.__version__
            elif getattr(self.center, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.center = self.center.to_version(self.__version__)
        if self.k1 is not None:
            if getattr(self.k1, '__version__', None) is None:
                self.k1.__version__ = self.__version__
            elif getattr(self.k1, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.k1 = self.k1.to_version(self.__version__)
        if self.k2 is not None:
            if getattr(self.k2, '__version__', None) is None:
                self.k2.__version__ = self.__version__
            elif getattr(self.k2, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.k2 = self.k2.to_version(self.__version__)
        if self.k3 is not None:
            if getattr(self.k3, '__version__', None) is None:
                self.k3.__version__ = self.__version__
            elif getattr(self.k3, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.k3 = self.k3.to_version(self.__version__)
        if self.p1 is not None:
            if getattr(self.p1, '__version__', None) is None:
                self.p1.__version__ = self.__version__
            elif getattr(self.p1, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.p1 = self.p1.to_version(self.__version__)
        if self.p2 is not None:
            if getattr(self.p2, '__version__', None) is None:
                self.p2.__version__ = self.__version__
            elif getattr(self.p2, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.p2 = self.p2.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Distortion":
        kwargs = {"sdf_version": target_version}
        kwargs["center"] = self.center.to_version(target_version) if self.center is not None else None
        kwargs["k1"] = self.k1.to_version(target_version) if self.k1 is not None else None
        kwargs["k2"] = self.k2.to_version(target_version) if self.k2 is not None else None
        kwargs["k3"] = self.k3.to_version(target_version) if self.k3 is not None else None
        kwargs["p1"] = self.p1.to_version(target_version) if self.p1 is not None else None
        kwargs["p2"] = self.p2.to_version(target_version) if self.p2 is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("distortion")
        if self.center is not None:
            el.append(self.center.to_sdf(version))
        if self.k1 is not None:
            el.append(self.k1.to_sdf(version))
        if self.k2 is not None:
            el.append(self.k2.to_sdf(version))
        if self.k3 is not None:
            el.append(self.k3.to_sdf(version))
        if self.p1 is not None:
            el.append(self.p1.to_sdf(version))
        if self.p2 is not None:
            el.append(self.p2.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_center = el.find("center")
        if _c_center is not None:
            _res = Center._from_sdf(_c_center, version)
            if isinstance(_res, SDFError):
                return _res.extend("center")
            _center = _res
        else:
            _center = None
        _c_k1 = el.find("k1")
        if _c_k1 is not None:
            _res = K1._from_sdf(_c_k1, version)
            if isinstance(_res, SDFError):
                return _res.extend("k1")
            _k1 = _res
        else:
            _k1 = None
        _c_k2 = el.find("k2")
        if _c_k2 is not None:
            _res = K2._from_sdf(_c_k2, version)
            if isinstance(_res, SDFError):
                return _res.extend("k2")
            _k2 = _res
        else:
            _k2 = None
        _c_k3 = el.find("k3")
        if _c_k3 is not None:
            _res = K3._from_sdf(_c_k3, version)
            if isinstance(_res, SDFError):
                return _res.extend("k3")
            _k3 = _res
        else:
            _k3 = None
        _c_p1 = el.find("p1")
        if _c_p1 is not None:
            _res = P1._from_sdf(_c_p1, version)
            if isinstance(_res, SDFError):
                return _res.extend("p1")
            _p1 = _res
        else:
            _p1 = None
        _c_p2 = el.find("p2")
        if _c_p2 is not None:
            _res = P2._from_sdf(_c_p2, version)
            if isinstance(_res, SDFError):
                return _res.extend("p2")
            _p2 = _res
        else:
            _p2 = None
        return cls(sdf_version=version, center=_center, k1=_k1, k2=_k2, k3=_k3, p1=_p1, p2=_p2)


class EnvTextureSize(BaseModel):
    def __init__(self, sdf_version: str | None = None, env_texture_size: int = 256):
        self.__version__ = sdf_version
        self.env_texture_size = env_texture_size

    def to_version(self, target_version: str) -> "EnvTextureSize":
        kwargs = {"sdf_version": target_version}
        kwargs["env_texture_size"] = self.env_texture_size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("env_texture_size")
        if self.env_texture_size is not None:
            el.text = str(self.env_texture_size)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 256
        _env_texture_size = _parse_int32(_text)
        if isinstance(_env_texture_size, SDFError):
            return _env_texture_size
        return cls(sdf_version=version, env_texture_size=_env_texture_size)


class F(BaseModel):
    def __init__(self, sdf_version: str | None = None, f: float = 1):
        self.__version__ = sdf_version
        self.f = f

    def to_version(self, target_version: str) -> "F":
        kwargs = {"sdf_version": target_version}
        kwargs["f"] = self.f
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("f")
        if self.f is not None:
            el.text = str(self.f)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _f = _parse_double(_text)
        if isinstance(_f, SDFError):
            return _f
        return cls(sdf_version=version, f=_f)


class Far(BaseModel):
    def __init__(self, sdf_version: str | None = None, far: float = 100):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "Far":
        if self.far is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'far' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("far")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100
        _far = _parse_double(_text)
        if isinstance(_far, SDFError):
            return _far
        if _far is not None and cmp_version(version, "1.2") < 0:
            if _far != 100:
                return SDFError(f"'far' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, far=_far)


class Format(BaseModel):
    def __init__(self, sdf_version: str | None = None, format: str = "R8G8B8"):
        self.__version__ = sdf_version
        self.format = format

    def to_version(self, target_version: str) -> "Format":
        if self.format is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'format' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["format"] = self.format
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("format")
        if self.format is not None:
            el.text = self.format
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "R8G8B8"
        _format = _text
        if isinstance(_format, SDFError):
            return _format
        if _format is not None and cmp_version(version, "1.2") < 0:
            if _format != "R8G8B8":
                return SDFError(f"'format' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, format=_format)


class Fun(BaseModel):
    def __init__(self, sdf_version: str | None = None, fun: str = "tan"):
        self.__version__ = sdf_version
        self.fun = fun

    def to_version(self, target_version: str) -> "Fun":
        kwargs = {"sdf_version": target_version}
        kwargs["fun"] = self.fun
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("fun")
        if self.fun is not None:
            el.text = self.fun
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "tan"
        _fun = _text
        if isinstance(_fun, SDFError):
            return _fun
        return cls(sdf_version=version, fun=_fun)


class Fx(BaseModel):
    def __init__(self, sdf_version: str | None = None, fx: float = 277):
        self.__version__ = sdf_version
        self.fx = fx

    def to_version(self, target_version: str) -> "Fx":
        kwargs = {"sdf_version": target_version}
        kwargs["fx"] = self.fx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("fx")
        if self.fx is not None:
            el.text = str(self.fx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _fx = _parse_double(_text)
        if isinstance(_fx, SDFError):
            return _fx
        return cls(sdf_version=version, fx=_fx)


class Fy(BaseModel):
    def __init__(self, sdf_version: str | None = None, fy: float = 277):
        self.__version__ = sdf_version
        self.fy = fy

    def to_version(self, target_version: str) -> "Fy":
        kwargs = {"sdf_version": target_version}
        kwargs["fy"] = self.fy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("fy")
        if self.fy is not None:
            el.text = str(self.fy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _fy = _parse_double(_text)
        if isinstance(_fy, SDFError):
            return _fy
        return cls(sdf_version=version, fy=_fy)


class Height(BaseModel):
    def __init__(self, sdf_version: str | None = None, height: int = 240):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
        if self.height is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'height' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("height")
        if self.height is not None:
            el.text = str(self.height)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 240
        _height = _parse_int32(_text)
        if isinstance(_height, SDFError):
            return _height
        if _height is not None and cmp_version(version, "1.2") < 0:
            if _height != 240:
                return SDFError(f"'height' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, height=_height)


class HorizontalFov(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        angle: float = 1.047,
        horizontal_fov: float = 1.047
    ):
        self.__version__ = sdf_version
        self.angle = angle
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "HorizontalFov":
        if self.angle is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'angle' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["angle"] = self.angle
        kwargs["horizontal_fov"] = self.horizontal_fov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("horizontal_fov")
        if self.angle is not None:
            el.set("angle", str(self.angle))
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _angle = _parse_double(el.get("angle", 1.047))
        if isinstance(_angle, SDFError):
            return _angle.extend("@angle")
        _text = el.text or 1.047
        _horizontal_fov = _parse_double(_text)
        if isinstance(_horizontal_fov, SDFError):
            return _horizontal_fov
        return cls(sdf_version=version, angle=_angle, horizontal_fov=_horizontal_fov)


class Image(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        anti_aliasing: "AntiAliasing" = None,
        format: str = "R8G8B8",
        height: int = 240,
        width: int = 320
    ):
        self.__version__ = sdf_version
        self.anti_aliasing = anti_aliasing
        self.format = format
        self.height = height
        self.width = width
        if self.anti_aliasing is not None:
            if getattr(self.anti_aliasing, '__version__', None) is None:
                self.anti_aliasing.__version__ = self.__version__
            elif getattr(self.anti_aliasing, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.anti_aliasing = self.anti_aliasing.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Image":
        if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
        if self.format is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'format' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.height is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'height' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.width is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'width' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["anti_aliasing"] = self.anti_aliasing.to_version(target_version) if self.anti_aliasing is not None else None
        kwargs["format"] = self.format
        kwargs["height"] = self.height
        kwargs["width"] = self.width
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("image")
        if self.anti_aliasing is not None:
            el.append(self.anti_aliasing.to_sdf(version))
        if self.format is not None:
            el.set("format", self.format)
        if self.height is not None:
            el.set("height", str(self.height))
        if self.width is not None:
            el.set("width", str(self.width))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_anti_aliasing = el.find("anti_aliasing")
        if _c_anti_aliasing is not None:
            _res = AntiAliasing._from_sdf(_c_anti_aliasing, version)
            if isinstance(_res, SDFError):
                return _res.extend("anti_aliasing")
            _anti_aliasing = _res
        else:
            _anti_aliasing = None
        if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
        _format = el.get("format", "R8G8B8")
        if isinstance(_format, SDFError):
            return _format.extend("@format")
        _height = _parse_int32(el.get("height", 240))
        if isinstance(_height, SDFError):
            return _height.extend("@height")
        _width = _parse_int32(el.get("width", 320))
        if isinstance(_width, SDFError):
            return _width.extend("@width")
        return cls(sdf_version=version, anti_aliasing=_anti_aliasing, format=_format, height=_height, width=_width)


class Intrinsics(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        cx: "Cx" = None,
        cy: "Cy" = None,
        fx: "Fx" = None,
        fy: "Fy" = None,
        s: "S" = None
    ):
        self.__version__ = sdf_version
        self.cx = cx
        self.cy = cy
        self.fx = fx
        self.fy = fy
        self.s = s
        if self.cx is not None:
            if getattr(self.cx, '__version__', None) is None:
                self.cx.__version__ = self.__version__
            elif getattr(self.cx, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.cx = self.cx.to_version(self.__version__)
        if self.cy is not None:
            if getattr(self.cy, '__version__', None) is None:
                self.cy.__version__ = self.__version__
            elif getattr(self.cy, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.cy = self.cy.to_version(self.__version__)
        if self.fx is not None:
            if getattr(self.fx, '__version__', None) is None:
                self.fx.__version__ = self.__version__
            elif getattr(self.fx, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.fx = self.fx.to_version(self.__version__)
        if self.fy is not None:
            if getattr(self.fy, '__version__', None) is None:
                self.fy.__version__ = self.__version__
            elif getattr(self.fy, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.fy = self.fy.to_version(self.__version__)
        if self.s is not None:
            if getattr(self.s, '__version__', None) is None:
                self.s.__version__ = self.__version__
            elif getattr(self.s, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.s = self.s.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Intrinsics":
        kwargs = {"sdf_version": target_version}
        kwargs["cx"] = self.cx.to_version(target_version) if self.cx is not None else None
        kwargs["cy"] = self.cy.to_version(target_version) if self.cy is not None else None
        kwargs["fx"] = self.fx.to_version(target_version) if self.fx is not None else None
        kwargs["fy"] = self.fy.to_version(target_version) if self.fy is not None else None
        kwargs["s"] = self.s.to_version(target_version) if self.s is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("intrinsics")
        if self.cx is not None:
            el.append(self.cx.to_sdf(version))
        if self.cy is not None:
            el.append(self.cy.to_sdf(version))
        if self.fx is not None:
            el.append(self.fx.to_sdf(version))
        if self.fy is not None:
            el.append(self.fy.to_sdf(version))
        if self.s is not None:
            el.append(self.s.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_cx = el.find("cx")
        if _c_cx is not None:
            _res = Cx._from_sdf(_c_cx, version)
            if isinstance(_res, SDFError):
                return _res.extend("cx")
            _cx = _res
        else:
            _cx = None
        _c_cy = el.find("cy")
        if _c_cy is not None:
            _res = Cy._from_sdf(_c_cy, version)
            if isinstance(_res, SDFError):
                return _res.extend("cy")
            _cy = _res
        else:
            _cy = None
        _c_fx = el.find("fx")
        if _c_fx is not None:
            _res = Fx._from_sdf(_c_fx, version)
            if isinstance(_res, SDFError):
                return _res.extend("fx")
            _fx = _res
        else:
            _fx = None
        _c_fy = el.find("fy")
        if _c_fy is not None:
            _res = Fy._from_sdf(_c_fy, version)
            if isinstance(_res, SDFError):
                return _res.extend("fy")
            _fy = _res
        else:
            _fy = None
        _c_s = el.find("s")
        if _c_s is not None:
            _res = S._from_sdf(_c_s, version)
            if isinstance(_res, SDFError):
                return _res.extend("s")
            _s = _res
        else:
            _s = None
        return cls(sdf_version=version, cx=_cx, cy=_cy, fx=_fx, fy=_fy, s=_s)


class K1(BaseModel):
    def __init__(self, sdf_version: str | None = None, k1: float = 0.0):
        self.__version__ = sdf_version
        self.k1 = k1

    def to_version(self, target_version: str) -> "K1":
        kwargs = {"sdf_version": target_version}
        kwargs["k1"] = self.k1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("k1")
        if self.k1 is not None:
            el.text = str(self.k1)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k1 = _parse_double(_text)
        if isinstance(_k1, SDFError):
            return _k1
        return cls(sdf_version=version, k1=_k1)


class K2(BaseModel):
    def __init__(self, sdf_version: str | None = None, k2: float = 0.0):
        self.__version__ = sdf_version
        self.k2 = k2

    def to_version(self, target_version: str) -> "K2":
        kwargs = {"sdf_version": target_version}
        kwargs["k2"] = self.k2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("k2")
        if self.k2 is not None:
            el.text = str(self.k2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k2 = _parse_double(_text)
        if isinstance(_k2, SDFError):
            return _k2
        return cls(sdf_version=version, k2=_k2)


class K3(BaseModel):
    def __init__(self, sdf_version: str | None = None, k3: float = 0.0):
        self.__version__ = sdf_version
        self.k3 = k3

    def to_version(self, target_version: str) -> "K3":
        kwargs = {"sdf_version": target_version}
        kwargs["k3"] = self.k3
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("k3")
        if self.k3 is not None:
            el.text = str(self.k3)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _k3 = _parse_double(_text)
        if isinstance(_k3, SDFError):
            return _k3
        return cls(sdf_version=version, k3=_k3)


class Lens(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        custom_function: "CustomFunction" = None,
        cutoff_angle: "CutoffAngle" = None,
        env_texture_size: "EnvTextureSize" = None,
        intrinsics: "Intrinsics" = None,
        projection: "Projection" = None,
        scale_to_hfov: "ScaleToHfov" = None,
        type: "LensType" = None
    ):
        self.__version__ = sdf_version
        self.custom_function = custom_function
        self.cutoff_angle = cutoff_angle
        self.env_texture_size = env_texture_size
        self.intrinsics = intrinsics
        self.projection = projection
        self.scale_to_hfov = scale_to_hfov
        self.type = type
        if self.custom_function is not None:
            if getattr(self.custom_function, '__version__', None) is None:
                self.custom_function.__version__ = self.__version__
            elif getattr(self.custom_function, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.custom_function = self.custom_function.to_version(self.__version__)
        if self.cutoff_angle is not None:
            if getattr(self.cutoff_angle, '__version__', None) is None:
                self.cutoff_angle.__version__ = self.__version__
            elif getattr(self.cutoff_angle, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.cutoff_angle = self.cutoff_angle.to_version(self.__version__)
        if self.env_texture_size is not None:
            if getattr(self.env_texture_size, '__version__', None) is None:
                self.env_texture_size.__version__ = self.__version__
            elif getattr(self.env_texture_size, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.env_texture_size = self.env_texture_size.to_version(self.__version__)
        if self.intrinsics is not None:
            if getattr(self.intrinsics, '__version__', None) is None:
                self.intrinsics.__version__ = self.__version__
            elif getattr(self.intrinsics, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.intrinsics = self.intrinsics.to_version(self.__version__)
        if self.projection is not None:
            if getattr(self.projection, '__version__', None) is None:
                self.projection.__version__ = self.__version__
            elif getattr(self.projection, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.projection = self.projection.to_version(self.__version__)
        if self.scale_to_hfov is not None:
            if getattr(self.scale_to_hfov, '__version__', None) is None:
                self.scale_to_hfov.__version__ = self.__version__
            elif getattr(self.scale_to_hfov, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.scale_to_hfov = self.scale_to_hfov.to_version(self.__version__)
        if self.type is not None:
            if getattr(self.type, '__version__', None) is None:
                self.type.__version__ = self.__version__
            elif getattr(self.type, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.type = self.type.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Lens":
        if self.intrinsics is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'intrinsics' is not supported in SDF version {target_version} (added in 1.6)")
        if self.projection is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'projection' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["custom_function"] = self.custom_function.to_version(target_version) if self.custom_function is not None else None
        kwargs["cutoff_angle"] = self.cutoff_angle.to_version(target_version) if self.cutoff_angle is not None else None
        kwargs["env_texture_size"] = self.env_texture_size.to_version(target_version) if self.env_texture_size is not None else None
        kwargs["intrinsics"] = self.intrinsics.to_version(target_version) if self.intrinsics is not None else None
        kwargs["projection"] = self.projection.to_version(target_version) if self.projection is not None else None
        kwargs["scale_to_hfov"] = self.scale_to_hfov.to_version(target_version) if self.scale_to_hfov is not None else None
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("lens")
        if self.custom_function is not None:
            el.append(self.custom_function.to_sdf(version))
        if self.cutoff_angle is not None:
            el.append(self.cutoff_angle.to_sdf(version))
        if self.env_texture_size is not None:
            el.append(self.env_texture_size.to_sdf(version))
        if self.intrinsics is not None:
            el.append(self.intrinsics.to_sdf(version))
        if self.projection is not None:
            el.append(self.projection.to_sdf(version))
        if self.scale_to_hfov is not None:
            el.append(self.scale_to_hfov.to_sdf(version))
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_custom_function = el.find("custom_function")
        if _c_custom_function is not None:
            _res = CustomFunction._from_sdf(_c_custom_function, version)
            if isinstance(_res, SDFError):
                return _res.extend("custom_function")
            _custom_function = _res
        else:
            _custom_function = None
        _c_cutoff_angle = el.find("cutoff_angle")
        if _c_cutoff_angle is not None:
            _res = CutoffAngle._from_sdf(_c_cutoff_angle, version)
            if isinstance(_res, SDFError):
                return _res.extend("cutoff_angle")
            _cutoff_angle = _res
        else:
            _cutoff_angle = None
        _c_env_texture_size = el.find("env_texture_size")
        if _c_env_texture_size is not None:
            _res = EnvTextureSize._from_sdf(_c_env_texture_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("env_texture_size")
            _env_texture_size = _res
        else:
            _env_texture_size = None
        _c_intrinsics = el.find("intrinsics")
        if _c_intrinsics is not None:
            _res = Intrinsics._from_sdf(_c_intrinsics, version)
            if isinstance(_res, SDFError):
                return _res.extend("intrinsics")
            _intrinsics = _res
        else:
            _intrinsics = None
        if _intrinsics is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'intrinsics' is not supported in SDF version {version} (added in 1.6)")
        _c_projection = el.find("projection")
        if _c_projection is not None:
            _res = Projection._from_sdf(_c_projection, version)
            if isinstance(_res, SDFError):
                return _res.extend("projection")
            _projection = _res
        else:
            _projection = None
        if _projection is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'projection' is not supported in SDF version {version} (added in 1.7)")
        _c_scale_to_hfov = el.find("scale_to_hfov")
        if _c_scale_to_hfov is not None:
            _res = ScaleToHfov._from_sdf(_c_scale_to_hfov, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale_to_hfov")
            _scale_to_hfov = _res
        else:
            _scale_to_hfov = None
        _c_type = el.find("type")
        if _c_type is not None:
            _res = LensType._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        return cls(sdf_version=version, custom_function=_custom_function, cutoff_angle=_cutoff_angle, env_texture_size=_env_texture_size, intrinsics=_intrinsics, projection=_projection, scale_to_hfov=_scale_to_hfov, type=_type)


class LensType(BaseModel):
    def __init__(self, sdf_version: str | None = None, type: str = "stereographic"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "LensType":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "stereographic"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        return cls(sdf_version=version, type=_type)


class Mean(BaseModel):
    def __init__(self, sdf_version: str | None = None, mean: float = 0.0):
        self.__version__ = sdf_version
        self.mean = mean

    def to_version(self, target_version: str) -> "Mean":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("mean")
        if self.mean is not None:
            el.text = str(self.mean)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _mean = _parse_double(_text)
        if isinstance(_mean, SDFError):
            return _mean
        return cls(sdf_version=version, mean=_mean)


class Near(BaseModel):
    def __init__(self, sdf_version: str | None = None, near: float = .1):
        self.__version__ = sdf_version
        self.near = near

    def to_version(self, target_version: str) -> "Near":
        if self.near is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'near' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("near")
        if self.near is not None:
            el.text = str(self.near)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or .1
        _near = _parse_double(_text)
        if isinstance(_near, SDFError):
            return _near
        if _near is not None and cmp_version(version, "1.2") < 0:
            if _near != .1:
                return SDFError(f"'near' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, near=_near)


class Noise(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        mean: "Mean" = None,
        stddev: "Stddev" = None,
        type: "Type" = None
    ):
        self.__version__ = sdf_version
        self.mean = mean
        self.stddev = stddev
        self.type = type
        if self.mean is not None:
            if getattr(self.mean, '__version__', None) is None:
                self.mean.__version__ = self.__version__
            elif getattr(self.mean, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.mean = self.mean.to_version(self.__version__)
        if self.stddev is not None:
            if getattr(self.stddev, '__version__', None) is None:
                self.stddev.__version__ = self.__version__
            elif getattr(self.stddev, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.stddev = self.stddev.to_version(self.__version__)
        if self.type is not None:
            if getattr(self.type, '__version__', None) is None:
                self.type.__version__ = self.__version__
            elif getattr(self.type, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.type = self.type.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Noise":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("noise")
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_mean = el.find("mean")
        if _c_mean is not None:
            _res = Mean._from_sdf(_c_mean, version)
            if isinstance(_res, SDFError):
                return _res.extend("mean")
            _mean = _res
        else:
            _mean = None
        _c_stddev = el.find("stddev")
        if _c_stddev is not None:
            _res = Stddev._from_sdf(_c_stddev, version)
            if isinstance(_res, SDFError):
                return _res.extend("stddev")
            _stddev = _res
        else:
            _stddev = None
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        return cls(sdf_version=version, mean=_mean, stddev=_stddev, type=_type)


class OpticalFrameId(BaseModel):
    def __init__(self, sdf_version: str | None = None, optical_frame_id: str = ""):
        self.__version__ = sdf_version
        self.optical_frame_id = optical_frame_id

    def to_version(self, target_version: str) -> "OpticalFrameId":
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["optical_frame_id"] = self.optical_frame_id
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("optical_frame_id")
        if self.optical_frame_id is not None:
            el.text = self.optical_frame_id
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _optical_frame_id = _text
        if isinstance(_optical_frame_id, SDFError):
            return _optical_frame_id
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            if _optical_frame_id != "":
                return SDFError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, optical_frame_id=_optical_frame_id)


class Output(BaseModel):
    def __init__(self, sdf_version: str | None = None, output: str = "depths"):
        self.__version__ = sdf_version
        self.output = output

    def to_version(self, target_version: str) -> "Output":
        if self.output is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'output' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["output"] = self.output
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("output")
        if self.output is not None:
            el.text = self.output
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "depths"
        _output = _text
        if isinstance(_output, SDFError):
            return _output
        if _output is not None and cmp_version(version, "1.2") < 0:
            if _output != "depths":
                return SDFError(f"'output' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, output=_output)


class P1(BaseModel):
    def __init__(self, sdf_version: str | None = None, p1: float = 0.0):
        self.__version__ = sdf_version
        self.p1 = p1

    def to_version(self, target_version: str) -> "P1":
        kwargs = {"sdf_version": target_version}
        kwargs["p1"] = self.p1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("p1")
        if self.p1 is not None:
            el.text = str(self.p1)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _p1 = _parse_double(_text)
        if isinstance(_p1, SDFError):
            return _p1
        return cls(sdf_version=version, p1=_p1)


class P2(BaseModel):
    def __init__(self, sdf_version: str | None = None, p2: float = 0.0):
        self.__version__ = sdf_version
        self.p2 = p2

    def to_version(self, target_version: str) -> "P2":
        kwargs = {"sdf_version": target_version}
        kwargs["p2"] = self.p2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("p2")
        if self.p2 is not None:
            el.text = str(self.p2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _p2 = _parse_double(_text)
        if isinstance(_p2, SDFError):
            return _p2
        return cls(sdf_version=version, p2=_p2)


class PCx(BaseModel):
    def __init__(self, sdf_version: str | None = None, p_cx: float = 160):
        self.__version__ = sdf_version
        self.p_cx = p_cx

    def to_version(self, target_version: str) -> "PCx":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cx"] = self.p_cx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("p_cx")
        if self.p_cx is not None:
            el.text = str(self.p_cx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 160
        _p_cx = _parse_double(_text)
        if isinstance(_p_cx, SDFError):
            return _p_cx
        return cls(sdf_version=version, p_cx=_p_cx)


class PCy(BaseModel):
    def __init__(self, sdf_version: str | None = None, p_cy: float = 120):
        self.__version__ = sdf_version
        self.p_cy = p_cy

    def to_version(self, target_version: str) -> "PCy":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cy"] = self.p_cy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("p_cy")
        if self.p_cy is not None:
            el.text = str(self.p_cy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 120
        _p_cy = _parse_double(_text)
        if isinstance(_p_cy, SDFError):
            return _p_cy
        return cls(sdf_version=version, p_cy=_p_cy)


class PFx(BaseModel):
    def __init__(self, sdf_version: str | None = None, p_fx: float = 277):
        self.__version__ = sdf_version
        self.p_fx = p_fx

    def to_version(self, target_version: str) -> "PFx":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fx"] = self.p_fx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("p_fx")
        if self.p_fx is not None:
            el.text = str(self.p_fx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _p_fx = _parse_double(_text)
        if isinstance(_p_fx, SDFError):
            return _p_fx
        return cls(sdf_version=version, p_fx=_p_fx)


class PFy(BaseModel):
    def __init__(self, sdf_version: str | None = None, p_fy: float = 277):
        self.__version__ = sdf_version
        self.p_fy = p_fy

    def to_version(self, target_version: str) -> "PFy":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fy"] = self.p_fy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("p_fy")
        if self.p_fy is not None:
            el.text = str(self.p_fy)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 277
        _p_fy = _parse_double(_text)
        if isinstance(_p_fy, SDFError):
            return _p_fy
        return cls(sdf_version=version, p_fy=_p_fy)


class Path(BaseModel):
    def __init__(self, sdf_version: str | None = None, path: str = "__default__"):
        self.__version__ = sdf_version
        self.path = path

    def to_version(self, target_version: str) -> "Path":
        if self.path is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'path' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["path"] = self.path
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("path")
        if self.path is not None:
            el.text = self.path
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _path = _text
        if isinstance(_path, SDFError):
            return _path
        if _path is not None and cmp_version(version, "1.2") < 0:
            if _path != "__default__":
                return SDFError(f"'path' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, path=_path)


class Projection(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        p_cx: "PCx" = None,
        p_cy: "PCy" = None,
        p_fx: "PFx" = None,
        p_fy: "PFy" = None,
        tx: "Tx" = None,
        ty: "Ty" = None
    ):
        self.__version__ = sdf_version
        self.p_cx = p_cx
        self.p_cy = p_cy
        self.p_fx = p_fx
        self.p_fy = p_fy
        self.tx = tx
        self.ty = ty
        if self.p_cx is not None:
            if getattr(self.p_cx, '__version__', None) is None:
                self.p_cx.__version__ = self.__version__
            elif getattr(self.p_cx, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.p_cx = self.p_cx.to_version(self.__version__)
        if self.p_cy is not None:
            if getattr(self.p_cy, '__version__', None) is None:
                self.p_cy.__version__ = self.__version__
            elif getattr(self.p_cy, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.p_cy = self.p_cy.to_version(self.__version__)
        if self.p_fx is not None:
            if getattr(self.p_fx, '__version__', None) is None:
                self.p_fx.__version__ = self.__version__
            elif getattr(self.p_fx, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.p_fx = self.p_fx.to_version(self.__version__)
        if self.p_fy is not None:
            if getattr(self.p_fy, '__version__', None) is None:
                self.p_fy.__version__ = self.__version__
            elif getattr(self.p_fy, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.p_fy = self.p_fy.to_version(self.__version__)
        if self.tx is not None:
            if getattr(self.tx, '__version__', None) is None:
                self.tx.__version__ = self.__version__
            elif getattr(self.tx, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.tx = self.tx.to_version(self.__version__)
        if self.ty is not None:
            if getattr(self.ty, '__version__', None) is None:
                self.ty.__version__ = self.__version__
            elif getattr(self.ty, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.ty = self.ty.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Projection":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cx"] = self.p_cx.to_version(target_version) if self.p_cx is not None else None
        kwargs["p_cy"] = self.p_cy.to_version(target_version) if self.p_cy is not None else None
        kwargs["p_fx"] = self.p_fx.to_version(target_version) if self.p_fx is not None else None
        kwargs["p_fy"] = self.p_fy.to_version(target_version) if self.p_fy is not None else None
        kwargs["tx"] = self.tx.to_version(target_version) if self.tx is not None else None
        kwargs["ty"] = self.ty.to_version(target_version) if self.ty is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("projection")
        if self.p_cx is not None:
            el.append(self.p_cx.to_sdf(version))
        if self.p_cy is not None:
            el.append(self.p_cy.to_sdf(version))
        if self.p_fx is not None:
            el.append(self.p_fx.to_sdf(version))
        if self.p_fy is not None:
            el.append(self.p_fy.to_sdf(version))
        if self.tx is not None:
            el.append(self.tx.to_sdf(version))
        if self.ty is not None:
            el.append(self.ty.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_p_cx = el.find("p_cx")
        if _c_p_cx is not None:
            _res = PCx._from_sdf(_c_p_cx, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_cx")
            _p_cx = _res
        else:
            _p_cx = None
        _c_p_cy = el.find("p_cy")
        if _c_p_cy is not None:
            _res = PCy._from_sdf(_c_p_cy, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_cy")
            _p_cy = _res
        else:
            _p_cy = None
        _c_p_fx = el.find("p_fx")
        if _c_p_fx is not None:
            _res = PFx._from_sdf(_c_p_fx, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_fx")
            _p_fx = _res
        else:
            _p_fx = None
        _c_p_fy = el.find("p_fy")
        if _c_p_fy is not None:
            _res = PFy._from_sdf(_c_p_fy, version)
            if isinstance(_res, SDFError):
                return _res.extend("p_fy")
            _p_fy = _res
        else:
            _p_fy = None
        _c_tx = el.find("tx")
        if _c_tx is not None:
            _res = Tx._from_sdf(_c_tx, version)
            if isinstance(_res, SDFError):
                return _res.extend("tx")
            _tx = _res
        else:
            _tx = None
        _c_ty = el.find("ty")
        if _c_ty is not None:
            _res = Ty._from_sdf(_c_ty, version)
            if isinstance(_res, SDFError):
                return _res.extend("ty")
            _ty = _res
        else:
            _ty = None
        return cls(sdf_version=version, p_cx=_p_cx, p_cy=_p_cy, p_fx=_p_fx, p_fy=_p_fy, tx=_tx, ty=_ty)


class S(BaseModel):
    def __init__(self, sdf_version: str | None = None, s: float = 0.0):
        self.__version__ = sdf_version
        self.s = s

    def to_version(self, target_version: str) -> "S":
        kwargs = {"sdf_version": target_version}
        kwargs["s"] = self.s
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("s")
        if self.s is not None:
            el.text = str(self.s)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _s = _parse_double(_text)
        if isinstance(_s, SDFError):
            return _s
        return cls(sdf_version=version, s=_s)


class Save(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        enabled: bool = False,
        path: str = "__default__"
    ):
        self.__version__ = sdf_version
        self.enabled = enabled
        self.path = path

    def to_version(self, target_version: str) -> "Save":
        if self.path is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'path' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["enabled"] = self.enabled
        kwargs["path"] = self.path
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("save")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        if self.path is not None:
            el.set("path", self.path)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _enabled = str(el.get("enabled", False)).strip().lower() == 'true'
        if isinstance(_enabled, SDFError):
            return _enabled.extend("@enabled")
        _path = el.get("path", "__default__")
        if isinstance(_path, SDFError):
            return _path.extend("@path")
        return cls(sdf_version=version, enabled=_enabled, path=_path)


class ScaleToHfov(BaseModel):
    def __init__(self, sdf_version: str | None = None, scale_to_hfov: bool = True):
        self.__version__ = sdf_version
        self.scale_to_hfov = scale_to_hfov

    def to_version(self, target_version: str) -> "ScaleToHfov":
        kwargs = {"sdf_version": target_version}
        kwargs["scale_to_hfov"] = self.scale_to_hfov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("scale_to_hfov")
        if self.scale_to_hfov is not None:
            el.text = str(self.scale_to_hfov).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _scale_to_hfov = str(_text).strip().lower() == 'true'
        if isinstance(_scale_to_hfov, SDFError):
            return _scale_to_hfov
        return cls(sdf_version=version, scale_to_hfov=_scale_to_hfov)


class SegmentationType(BaseModel):
    def __init__(self, sdf_version: str | None = None, segmentation_type: str = "semantic"):
        self.__version__ = sdf_version
        self.segmentation_type = segmentation_type

    def to_version(self, target_version: str) -> "SegmentationType":
        if self.segmentation_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["segmentation_type"] = self.segmentation_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("segmentation_type")
        if self.segmentation_type is not None:
            el.text = self.segmentation_type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "semantic"
        _segmentation_type = _text
        if isinstance(_segmentation_type, SDFError):
            return _segmentation_type
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            if _segmentation_type != "semantic":
                return SDFError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, segmentation_type=_segmentation_type)


class Stddev(BaseModel):
    def __init__(self, sdf_version: str | None = None, stddev: float = 0.0):
        self.__version__ = sdf_version
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Stddev":
        kwargs = {"sdf_version": target_version}
        kwargs["stddev"] = self.stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("stddev")
        if self.stddev is not None:
            el.text = str(self.stddev)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _stddev = _parse_double(_text)
        if isinstance(_stddev, SDFError):
            return _stddev
        return cls(sdf_version=version, stddev=_stddev)


class TriggerTopic(BaseModel):
    def __init__(self, sdf_version: str | None = None, trigger_topic: str = ""):
        self.__version__ = sdf_version
        self.trigger_topic = trigger_topic

    def to_version(self, target_version: str) -> "TriggerTopic":
        if self.trigger_topic is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["trigger_topic"] = self.trigger_topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("trigger_topic")
        if self.trigger_topic is not None:
            el.text = self.trigger_topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _trigger_topic = _text
        if isinstance(_trigger_topic, SDFError):
            return _trigger_topic
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            if _trigger_topic != "":
                return SDFError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, trigger_topic=_trigger_topic)


class Triggered(BaseModel):
    def __init__(self, sdf_version: str | None = None, triggered: bool = False):
        self.__version__ = sdf_version
        self.triggered = triggered

    def to_version(self, target_version: str) -> "Triggered":
        if self.triggered is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["triggered"] = self.triggered
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("triggered")
        if self.triggered is not None:
            el.text = str(self.triggered).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _triggered = str(_text).strip().lower() == 'true'
        if isinstance(_triggered, SDFError):
            return _triggered
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            if _triggered != False:
                return SDFError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, triggered=_triggered)


class Tx(BaseModel):
    def __init__(self, sdf_version: str | None = None, tx: float = 0.0):
        self.__version__ = sdf_version
        self.tx = tx

    def to_version(self, target_version: str) -> "Tx":
        kwargs = {"sdf_version": target_version}
        kwargs["tx"] = self.tx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("tx")
        if self.tx is not None:
            el.text = str(self.tx)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _tx = _parse_double(_text)
        if isinstance(_tx, SDFError):
            return _tx
        return cls(sdf_version=version, tx=_tx)


class Ty(BaseModel):
    def __init__(self, sdf_version: str | None = None, ty: float = 0.0):
        self.__version__ = sdf_version
        self.ty = ty

    def to_version(self, target_version: str) -> "Ty":
        kwargs = {"sdf_version": target_version}
        kwargs["ty"] = self.ty
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("ty")
        if self.ty is not None:
            el.text = str(self.ty)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _ty = _parse_double(_text)
        if isinstance(_ty, SDFError):
            return _ty
        return cls(sdf_version=version, ty=_ty)


class Type(BaseModel):
    def __init__(self, sdf_version: str | None = None, type: str = "gaussian"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Type":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "gaussian"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        return cls(sdf_version=version, type=_type)


class VisibilityMask(BaseModel):
    def __init__(self, sdf_version: str | None = None, visibility_mask: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "VisibilityMask":
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_mask"] = self.visibility_mask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("visibility_mask")
        if self.visibility_mask is not None:
            el.text = str(self.visibility_mask)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4294967295
        _visibility_mask = _parse_uint32(_text)
        if isinstance(_visibility_mask, SDFError):
            return _visibility_mask
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            if _visibility_mask != 4294967295:
                return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_mask=_visibility_mask)


class Width(BaseModel):
    def __init__(self, sdf_version: str | None = None, width: int = 320):
        self.__version__ = sdf_version
        self.width = width

    def to_version(self, target_version: str) -> "Width":
        if self.width is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'width' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["width"] = self.width
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("width")
        if self.width is not None:
            el.text = str(self.width)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 320
        _width = _parse_int32(_text)
        if isinstance(_width, SDFError):
            return _width
        if _width is not None and cmp_version(version, "1.2") < 0:
            if _width != 320:
                return SDFError(f"'width' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, width=_width)
