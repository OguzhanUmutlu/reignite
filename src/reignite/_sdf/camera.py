### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_int32, _parse_uint32
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector2d import _Vector2dT, _vector2d
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.frame import Frame
    from ..elements.pose import Pose

def _parse_vector2d(raw: str) -> _Vector2dT | SDFError:
    try:
        return _vector2d(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Camera(BaseModel):
    class Clip(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            far: float | None = None,
            near: float | None = None
        ):
            super().__init__(sdf_version)
            self.far = far
            self.near = near

        def to_version(self, target_version: str) -> "Camera.Clip":
            kwargs: dict = {"sdf_version": target_version, "far": self.far, "near": self.near}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("clip")
            if self.far is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("far")
                    _c_tmp.text = str(self.far)
                    el.append(_c_tmp)
                else:
                    el.set("far", str(self.far))
            if self.near is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("near")
                    _c_tmp.text = str(self.near)
                    el.append(_c_tmp)
                else:
                    el.set("near", str(self.near))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Clip | SDFError":
            _raw_far = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("far")
                if _c_tmp is not None: _raw_far = _c_tmp.text
            else:
                _raw_far = el.get("far")
            if _raw_far is None: _raw_far = 100
            _far = _parse_double(_raw_far)
            if isinstance(_far, SDFError):
                return _far.extend("@far")
            _raw_near = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("near")
                if _c_tmp is not None: _raw_near = _c_tmp.text
            else:
                _raw_near = el.get("near")
            if _raw_near is None: _raw_near = .1
            _near = _parse_double(_raw_near)
            if isinstance(_near, SDFError):
                return _near.extend("@near")
            return cls(sdf_version=version, far=_far, near=_near)

    class DepthCamera(BaseModel):
        class DepthCameraClip(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                far: float | None = None,
                near: float | None = None
            ):
                super().__init__(sdf_version)
                self.far = far
                self.near = near

            def to_version(self, target_version: str) -> "Camera.DepthCamera.DepthCameraClip":
                kwargs: dict = {"sdf_version": target_version, "far": self.far, "near": self.near}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("clip")
                if self.far is not None:
                    _c_tmp = ET.Element("far")
                    _c_tmp.text = str(self.far)
                    el.append(_c_tmp)
                if self.near is not None:
                    _c_tmp = ET.Element("near")
                    _c_tmp.text = str(self.near)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.DepthCamera.DepthCameraClip | SDFError":
                _c_tmp = el.find("far")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 10.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("far")
                    _far = _val
                else:
                    _far = None
                _c_tmp = el.find("near")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else .1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("near")
                    _near = _val
                else:
                    _near = None
                return cls(sdf_version=version, far=_far, near=_near)

        def __init__(
            self,
            sdf_version: str | None = None,
            clip: "Camera.DepthCamera.DepthCameraClip" = None,
            output: str | None = None
        ):
            super().__init__(sdf_version)
            self.clip = clip
            self.output = output
            if self.clip is not None and hasattr(self.clip, 'to_version'):
                if getattr(self.clip, 'sdfversion', None) is None:
                    self.clip.sdfversion = self.sdfversion
                elif getattr(self.clip, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.clip = self.clip.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Camera.DepthCamera":
            if self.clip is not None and cmp_version(target_version, "1.6") < 0:
                raise ValueError(f"'clip' is not supported in SDF version {target_version} (added in 1.6)")
            kwargs: dict = {"sdf_version": target_version, "clip": self.clip.to_version(target_version) if self.clip is not None and hasattr(self.clip, "to_version") else self.clip, "output": self.output}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("depth_camera")
            if self.clip is not None:
                _child_res = self.clip.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('clip')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.output is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("output")
                    _c_tmp.text = self.output
                    el.append(_c_tmp)
                else:
                    el.set("output", self.output)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.DepthCamera | SDFError":
            _c_clip = el.find("clip")
            if _c_clip is not None:
                _res = cls.DepthCameraClip._from_sdf(_c_clip, version)
                if isinstance(_res, SDFError):
                    return _res.extend("clip")
                _clip = _res
            else:
                _clip = None
            if _clip is not None and cmp_version(version, "1.6") < 0:
                return SDFError(f"'clip' is not supported in SDF version {version} (added in 1.6)")
            _raw_output = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("output")
                if _c_tmp is not None: _raw_output = _c_tmp.text
            else:
                _raw_output = el.get("output")
            if _raw_output is None: _raw_output = "depths"
            _output = _raw_output
            if isinstance(_output, SDFError):
                return _output.extend("@output")
            return cls(sdf_version=version, clip=_clip, output=_output)

    class Distortion(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            center: _Vector2dT | None = None,
            k1: float | None = None,
            k2: float | None = None,
            k3: float | None = None,
            p1: float | None = None,
            p2: float | None = None
        ):
            super().__init__(sdf_version)
            self.center = _vector2d(center) if center is not None else None
            self.k1 = k1
            self.k2 = k2
            self.k3 = k3
            self.p1 = p1
            self.p2 = p2

        def to_version(self, target_version: str) -> "Camera.Distortion":
            kwargs: dict = {"sdf_version": target_version, "center": self.center, "k1": self.k1, "k2": self.k2, "k3": self.k3, "p1": self.p1, "p2": self.p2}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("distortion")
            if self.center is not None:
                _c_tmp = ET.Element("center")
                _c_tmp.text = str(self.center)
                el.append(_c_tmp)
            if self.k1 is not None:
                _c_tmp = ET.Element("k1")
                _c_tmp.text = str(self.k1)
                el.append(_c_tmp)
            if self.k2 is not None:
                _c_tmp = ET.Element("k2")
                _c_tmp.text = str(self.k2)
                el.append(_c_tmp)
            if self.k3 is not None:
                _c_tmp = ET.Element("k3")
                _c_tmp.text = str(self.k3)
                el.append(_c_tmp)
            if self.p1 is not None:
                _c_tmp = ET.Element("p1")
                _c_tmp.text = str(self.p1)
                el.append(_c_tmp)
            if self.p2 is not None:
                _c_tmp = ET.Element("p2")
                _c_tmp.text = str(self.p2)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Distortion | SDFError":
            _c_tmp = el.find("center")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "0.5 0.5"
                _val = _parse_vector2d(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("center")
                _center = _val
            else:
                _center = None
            _c_tmp = el.find("k1")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("k1")
                _k1 = _val
            else:
                _k1 = None
            _c_tmp = el.find("k2")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("k2")
                _k2 = _val
            else:
                _k2 = None
            _c_tmp = el.find("k3")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("k3")
                _k3 = _val
            else:
                _k3 = None
            _c_tmp = el.find("p1")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("p1")
                _p1 = _val
            else:
                _p1 = None
            _c_tmp = el.find("p2")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("p2")
                _p2 = _val
            else:
                _p2 = None
            return cls(sdf_version=version, center=_center, k1=_k1, k2=_k2, k3=_k3, p1=_p1, p2=_p2)

    class HorizontalFov(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            angle: float | None = None,
            horizontal_fov: float | None = None
        ):
            super().__init__(sdf_version)
            self.angle = angle
            self.horizontal_fov = horizontal_fov

        def to_version(self, target_version: str) -> "Camera.HorizontalFov":
            kwargs: dict = {"sdf_version": target_version, "angle": self.angle, "horizontal_fov": self.horizontal_fov}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("horizontal_fov")
            if self.angle is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.angle)
                else:
                    el.set("angle", str(self.angle))
            if self.horizontal_fov is not None:
                el.text = str(self.horizontal_fov)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.HorizontalFov | SDFError":
            _raw_angle = None
            if cmp_version(version, "1.2") >= 0:
                _raw_angle = el.text
            else:
                _raw_angle = el.get("angle")
            if _raw_angle is None: _raw_angle = 1.047
            _angle = _parse_double(_raw_angle)
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
            anti_aliasing: int | None = None,
            format: str | None = None,
            height: int | None = None,
            width: int | None = None
        ):
            super().__init__(sdf_version)
            self.anti_aliasing = anti_aliasing
            self.format = format
            self.height = height
            self.width = width

        def to_version(self, target_version: str) -> "Camera.Image":
            if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
                raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
            kwargs: dict = {"sdf_version": target_version, "anti_aliasing": self.anti_aliasing, "format": self.format, "height": self.height, "width": self.width}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("image")
            if self.anti_aliasing is not None:
                _c_tmp = ET.Element("anti_aliasing")
                _c_tmp.text = str(self.anti_aliasing)
                el.append(_c_tmp)
            if self.format is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("format")
                    _c_tmp.text = self.format
                    el.append(_c_tmp)
                else:
                    el.set("format", self.format)
            if self.height is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("height")
                    _c_tmp.text = str(self.height)
                    el.append(_c_tmp)
                else:
                    el.set("height", str(self.height))
            if self.width is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("width")
                    _c_tmp.text = str(self.width)
                    el.append(_c_tmp)
                else:
                    el.set("width", str(self.width))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Image | SDFError":
            _c_tmp = el.find("anti_aliasing")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 4
                _val = _parse_int32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("anti_aliasing")
                _anti_aliasing = _val
            else:
                _anti_aliasing = None
            if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
                return SDFError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
            _raw_format = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("format")
                if _c_tmp is not None: _raw_format = _c_tmp.text
            else:
                _raw_format = el.get("format")
            if _raw_format is None: _raw_format = "R8G8B8"
            _format = _raw_format
            if isinstance(_format, SDFError):
                return _format.extend("@format")
            _raw_height = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("height")
                if _c_tmp is not None: _raw_height = _c_tmp.text
            else:
                _raw_height = el.get("height")
            if _raw_height is None: _raw_height = 240
            _height = _parse_int32(_raw_height)
            if isinstance(_height, SDFError):
                return _height.extend("@height")
            _raw_width = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("width")
                if _c_tmp is not None: _raw_width = _c_tmp.text
            else:
                _raw_width = el.get("width")
            if _raw_width is None: _raw_width = 320
            _width = _parse_int32(_raw_width)
            if isinstance(_width, SDFError):
                return _width.extend("@width")
            return cls(sdf_version=version, anti_aliasing=_anti_aliasing, format=_format, height=_height, width=_width)

    class Lens(BaseModel):
        class CustomFunction(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                c1: float | None = None,
                c2: float | None = None,
                c3: float | None = None,
                f: float | None = None,
                fun: str | None = None
            ):
                super().__init__(sdf_version)
                self.c1 = c1
                self.c2 = c2
                self.c3 = c3
                self.f = f
                self.fun = fun

            def to_version(self, target_version: str) -> "Camera.Lens.CustomFunction":
                kwargs: dict = {"sdf_version": target_version, "c1": self.c1, "c2": self.c2, "c3": self.c3, "f": self.f, "fun": self.fun}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("custom_function")
                if self.c1 is not None:
                    _c_tmp = ET.Element("c1")
                    _c_tmp.text = str(self.c1)
                    el.append(_c_tmp)
                if self.c2 is not None:
                    _c_tmp = ET.Element("c2")
                    _c_tmp.text = str(self.c2)
                    el.append(_c_tmp)
                if self.c3 is not None:
                    _c_tmp = ET.Element("c3")
                    _c_tmp.text = str(self.c3)
                    el.append(_c_tmp)
                if self.f is not None:
                    _c_tmp = ET.Element("f")
                    _c_tmp.text = str(self.f)
                    el.append(_c_tmp)
                if self.fun is not None:
                    _c_tmp = ET.Element("fun")
                    _c_tmp.text = self.fun
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Lens.CustomFunction | SDFError":
                _c_tmp = el.find("c1")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("c1")
                    _c1 = _val
                else:
                    _c1 = None
                _c_tmp = el.find("c2")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("c2")
                    _c2 = _val
                else:
                    _c2 = None
                _c_tmp = el.find("c3")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("c3")
                    _c3 = _val
                else:
                    _c3 = None
                _c_tmp = el.find("f")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("f")
                    _f = _val
                else:
                    _f = None
                _c_tmp = el.find("fun")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "tan"
                    _val = _text
                    if isinstance(_val, SDFError):
                        return _val.extend("fun")
                    _fun = _val
                else:
                    _fun = None
                return cls(sdf_version=version, c1=_c1, c2=_c2, c3=_c3, f=_f, fun=_fun)

        class Intrinsics(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                cx: float | None = None,
                cy: float | None = None,
                fx: float | None = None,
                fy: float | None = None,
                s: float | None = None
            ):
                super().__init__(sdf_version)
                self.cx = cx
                self.cy = cy
                self.fx = fx
                self.fy = fy
                self.s = s

            def to_version(self, target_version: str) -> "Camera.Lens.Intrinsics":
                kwargs: dict = {"sdf_version": target_version, "cx": self.cx, "cy": self.cy, "fx": self.fx, "fy": self.fy, "s": self.s}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("intrinsics")
                if self.cx is not None:
                    _c_tmp = ET.Element("cx")
                    _c_tmp.text = str(self.cx)
                    el.append(_c_tmp)
                if self.cy is not None:
                    _c_tmp = ET.Element("cy")
                    _c_tmp.text = str(self.cy)
                    el.append(_c_tmp)
                if self.fx is not None:
                    _c_tmp = ET.Element("fx")
                    _c_tmp.text = str(self.fx)
                    el.append(_c_tmp)
                if self.fy is not None:
                    _c_tmp = ET.Element("fy")
                    _c_tmp.text = str(self.fy)
                    el.append(_c_tmp)
                if self.s is not None:
                    _c_tmp = ET.Element("s")
                    _c_tmp.text = str(self.s)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Lens.Intrinsics | SDFError":
                _c_tmp = el.find("cx")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 160
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("cx")
                    _cx = _val
                else:
                    _cx = None
                _c_tmp = el.find("cy")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 120
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("cy")
                    _cy = _val
                else:
                    _cy = None
                _c_tmp = el.find("fx")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 277
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("fx")
                    _fx = _val
                else:
                    _fx = None
                _c_tmp = el.find("fy")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 277
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("fy")
                    _fy = _val
                else:
                    _fy = None
                _c_tmp = el.find("s")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("s")
                    _s = _val
                else:
                    _s = None
                return cls(sdf_version=version, cx=_cx, cy=_cy, fx=_fx, fy=_fy, s=_s)

        class Projection(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                p_cx: float | None = None,
                p_cy: float | None = None,
                p_fx: float | None = None,
                p_fy: float | None = None,
                tx: float | None = None,
                ty: float | None = None
            ):
                super().__init__(sdf_version)
                self.p_cx = p_cx
                self.p_cy = p_cy
                self.p_fx = p_fx
                self.p_fy = p_fy
                self.tx = tx
                self.ty = ty

            def to_version(self, target_version: str) -> "Camera.Lens.Projection":
                kwargs: dict = {"sdf_version": target_version, "p_cx": self.p_cx, "p_cy": self.p_cy, "p_fx": self.p_fx, "p_fy": self.p_fy, "tx": self.tx, "ty": self.ty}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("projection")
                if self.p_cx is not None:
                    _c_tmp = ET.Element("p_cx")
                    _c_tmp.text = str(self.p_cx)
                    el.append(_c_tmp)
                if self.p_cy is not None:
                    _c_tmp = ET.Element("p_cy")
                    _c_tmp.text = str(self.p_cy)
                    el.append(_c_tmp)
                if self.p_fx is not None:
                    _c_tmp = ET.Element("p_fx")
                    _c_tmp.text = str(self.p_fx)
                    el.append(_c_tmp)
                if self.p_fy is not None:
                    _c_tmp = ET.Element("p_fy")
                    _c_tmp.text = str(self.p_fy)
                    el.append(_c_tmp)
                if self.tx is not None:
                    _c_tmp = ET.Element("tx")
                    _c_tmp.text = str(self.tx)
                    el.append(_c_tmp)
                if self.ty is not None:
                    _c_tmp = ET.Element("ty")
                    _c_tmp.text = str(self.ty)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Lens.Projection | SDFError":
                _c_tmp = el.find("p_cx")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 160
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("p_cx")
                    _p_cx = _val
                else:
                    _p_cx = None
                _c_tmp = el.find("p_cy")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 120
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("p_cy")
                    _p_cy = _val
                else:
                    _p_cy = None
                _c_tmp = el.find("p_fx")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 277
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("p_fx")
                    _p_fx = _val
                else:
                    _p_fx = None
                _c_tmp = el.find("p_fy")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 277
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("p_fy")
                    _p_fy = _val
                else:
                    _p_fy = None
                _c_tmp = el.find("tx")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("tx")
                    _tx = _val
                else:
                    _tx = None
                _c_tmp = el.find("ty")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("ty")
                    _ty = _val
                else:
                    _ty = None
                return cls(sdf_version=version, p_cx=_p_cx, p_cy=_p_cy, p_fx=_p_fx, p_fy=_p_fy, tx=_tx, ty=_ty)

        def __init__(
            self,
            sdf_version: str | None = None,
            custom_function: "Camera.Lens.CustomFunction" = None,
            cutoff_angle: float | None = None,
            env_texture_size: int | None = None,
            intrinsics: "Camera.Lens.Intrinsics" = None,
            projection: "Camera.Lens.Projection" = None,
            scale_to_hfov: bool | None = None,
            type: str | None = None
        ):
            super().__init__(sdf_version)
            self.custom_function = custom_function
            self.cutoff_angle = cutoff_angle
            self.env_texture_size = env_texture_size
            self.intrinsics = intrinsics
            self.projection = projection
            self.scale_to_hfov = scale_to_hfov
            self.type = type
            if self.custom_function is not None and hasattr(self.custom_function, 'to_version'):
                if getattr(self.custom_function, 'sdfversion', None) is None:
                    self.custom_function.sdfversion = self.sdfversion
                elif getattr(self.custom_function, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.custom_function = self.custom_function.to_version(self.sdfversion)
            if self.intrinsics is not None and hasattr(self.intrinsics, 'to_version'):
                if getattr(self.intrinsics, 'sdfversion', None) is None:
                    self.intrinsics.sdfversion = self.sdfversion
                elif getattr(self.intrinsics, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.intrinsics = self.intrinsics.to_version(self.sdfversion)
            if self.projection is not None and hasattr(self.projection, 'to_version'):
                if getattr(self.projection, 'sdfversion', None) is None:
                    self.projection.sdfversion = self.sdfversion
                elif getattr(self.projection, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.projection = self.projection.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Camera.Lens":
            if self.intrinsics is not None and cmp_version(target_version, "1.6") < 0:
                raise ValueError(f"'intrinsics' is not supported in SDF version {target_version} (added in 1.6)")
            if self.projection is not None and cmp_version(target_version, "1.7") < 0:
                raise ValueError(f"'projection' is not supported in SDF version {target_version} (added in 1.7)")
            kwargs: dict = {"sdf_version": target_version, "custom_function": self.custom_function.to_version(target_version) if self.custom_function is not None and hasattr(self.custom_function, "to_version") else self.custom_function, "cutoff_angle": self.cutoff_angle, "env_texture_size": self.env_texture_size, "intrinsics": self.intrinsics.to_version(target_version) if self.intrinsics is not None and hasattr(self.intrinsics, "to_version") else self.intrinsics, "projection": self.projection.to_version(target_version) if self.projection is not None and hasattr(self.projection, "to_version") else self.projection, "scale_to_hfov": self.scale_to_hfov, "type": self.type}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("lens")
            if self.custom_function is not None:
                _child_res = self.custom_function.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('custom_function')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.cutoff_angle is not None:
                _c_tmp = ET.Element("cutoff_angle")
                _c_tmp.text = str(self.cutoff_angle)
                el.append(_c_tmp)
            if self.env_texture_size is not None:
                _c_tmp = ET.Element("env_texture_size")
                _c_tmp.text = str(self.env_texture_size)
                el.append(_c_tmp)
            if self.intrinsics is not None:
                _child_res = self.intrinsics.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('intrinsics')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.projection is not None:
                _child_res = self.projection.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('projection')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.scale_to_hfov is not None:
                _c_tmp = ET.Element("scale_to_hfov")
                _c_tmp.text = str(self.scale_to_hfov).lower()
                el.append(_c_tmp)
            if self.type is not None:
                _c_tmp = ET.Element("type")
                _c_tmp.text = self.type
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Lens | SDFError":
            _c_custom_function = el.find("custom_function")
            if _c_custom_function is not None:
                _res = cls.CustomFunction._from_sdf(_c_custom_function, version)
                if isinstance(_res, SDFError):
                    return _res.extend("custom_function")
                _custom_function = _res
            else:
                _custom_function = None
            _c_tmp = el.find("cutoff_angle")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 1.5707
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("cutoff_angle")
                _cutoff_angle = _val
            else:
                _cutoff_angle = None
            _c_tmp = el.find("env_texture_size")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 256
                _val = _parse_int32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("env_texture_size")
                _env_texture_size = _val
            else:
                _env_texture_size = None
            _c_intrinsics = el.find("intrinsics")
            if _c_intrinsics is not None:
                _res = cls.Intrinsics._from_sdf(_c_intrinsics, version)
                if isinstance(_res, SDFError):
                    return _res.extend("intrinsics")
                _intrinsics = _res
            else:
                _intrinsics = None
            if _intrinsics is not None and cmp_version(version, "1.6") < 0:
                return SDFError(f"'intrinsics' is not supported in SDF version {version} (added in 1.6)")
            _c_projection = el.find("projection")
            if _c_projection is not None:
                _res = cls.Projection._from_sdf(_c_projection, version)
                if isinstance(_res, SDFError):
                    return _res.extend("projection")
                _projection = _res
            else:
                _projection = None
            if _projection is not None and cmp_version(version, "1.7") < 0:
                return SDFError(f"'projection' is not supported in SDF version {version} (added in 1.7)")
            _c_tmp = el.find("scale_to_hfov")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else True
                _val = str(_text).strip().lower() == 'true'
                if isinstance(_val, SDFError):
                    return _val.extend("scale_to_hfov")
                _scale_to_hfov = _val
            else:
                _scale_to_hfov = None
            _c_tmp = el.find("type")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "stereographic"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("type")
                _type = _val
            else:
                _type = None
            return cls(sdf_version=version, custom_function=_custom_function, cutoff_angle=_cutoff_angle, env_texture_size=_env_texture_size, intrinsics=_intrinsics, projection=_projection, scale_to_hfov=_scale_to_hfov, type=_type)

    class Noise(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            mean: float | None = None,
            stddev: float | None = None,
            type: str | None = None
        ):
            super().__init__(sdf_version)
            self.mean = mean
            self.stddev = stddev
            self.type = type

        def to_version(self, target_version: str) -> "Camera.Noise":
            kwargs: dict = {"sdf_version": target_version, "mean": self.mean, "stddev": self.stddev, "type": self.type}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("noise")
            if self.mean is not None:
                _c_tmp = ET.Element("mean")
                _c_tmp.text = str(self.mean)
                el.append(_c_tmp)
            if self.stddev is not None:
                _c_tmp = ET.Element("stddev")
                _c_tmp.text = str(self.stddev)
                el.append(_c_tmp)
            if self.type is not None:
                _c_tmp = ET.Element("type")
                _c_tmp.text = self.type
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Noise | SDFError":
            _c_tmp = el.find("mean")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("mean")
                _mean = _val
            else:
                _mean = None
            _c_tmp = el.find("stddev")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("stddev")
                _stddev = _val
            else:
                _stddev = None
            _c_tmp = el.find("type")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "gaussian"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("type")
                _type = _val
            else:
                _type = None
            return cls(sdf_version=version, mean=_mean, stddev=_stddev, type=_type)

    class Save(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            enabled: bool | None = None,
            path: str | None = None
        ):
            super().__init__(sdf_version)
            self.enabled = enabled
            self.path = path

        def to_version(self, target_version: str) -> "Camera.Save":
            if self.path is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'path' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs: dict = {"sdf_version": target_version, "enabled": self.enabled, "path": self.path}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("save")
            if self.enabled is not None:
                el.set("enabled", str(self.enabled).lower())
            if self.path is not None:
                el.set("path", self.path)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Camera.Save | SDFError":
            _enabled = str(el.get("enabled", False)).strip().lower() == 'true'
            if isinstance(_enabled, SDFError):
                return _enabled.extend("@enabled")
            _path = el.get("path", "__default__")
            if isinstance(_path, SDFError):
                return _path.extend("@path")
            return cls(sdf_version=version, enabled=_enabled, path=_path)

    def __init__(
        self,
        sdf_version: str | None = None,
        box_type: str | None = None,
        camera_info_topic: str | None = None,
        clip: "Camera.Clip" = None,
        depth_camera: "Camera.DepthCamera" = None,
        distortion: "Camera.Distortion" = None,
        frames: List["Frame"] = None,
        horizontal_fov: "Camera.HorizontalFov" = None,
        image: "Camera.Image" = None,
        lens: "Camera.Lens" = None,
        name: str | None = None,
        noise: "Camera.Noise" = None,
        optical_frame_id: str | None = None,
        pose: "Pose" = None,
        save: "Camera.Save" = None,
        segmentation_type: str | None = None,
        trigger_topic: str | None = None,
        triggered: bool | None = None,
        visibility_mask: int | None = None
    ):
        super().__init__(sdf_version)
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
        if self.clip is not None and hasattr(self.clip, 'to_version'):
            if getattr(self.clip, 'sdfversion', None) is None:
                self.clip.sdfversion = self.sdfversion
            elif getattr(self.clip, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.clip = self.clip.to_version(self.sdfversion)
        if self.depth_camera is not None and hasattr(self.depth_camera, 'to_version'):
            if getattr(self.depth_camera, 'sdfversion', None) is None:
                self.depth_camera.sdfversion = self.sdfversion
            elif getattr(self.depth_camera, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.depth_camera = self.depth_camera.to_version(self.sdfversion)
        if self.distortion is not None and hasattr(self.distortion, 'to_version'):
            if getattr(self.distortion, 'sdfversion', None) is None:
                self.distortion.sdfversion = self.sdfversion
            elif getattr(self.distortion, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.distortion = self.distortion.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        if self.horizontal_fov is not None and hasattr(self.horizontal_fov, 'to_version'):
            if getattr(self.horizontal_fov, 'sdfversion', None) is None:
                self.horizontal_fov.sdfversion = self.sdfversion
            elif getattr(self.horizontal_fov, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.horizontal_fov = self.horizontal_fov.to_version(self.sdfversion)
        if self.image is not None and hasattr(self.image, 'to_version'):
            if getattr(self.image, 'sdfversion', None) is None:
                self.image.sdfversion = self.sdfversion
            elif getattr(self.image, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.image = self.image.to_version(self.sdfversion)
        if self.lens is not None and hasattr(self.lens, 'to_version'):
            if getattr(self.lens, 'sdfversion', None) is None:
                self.lens.sdfversion = self.sdfversion
            elif getattr(self.lens, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.lens = self.lens.to_version(self.sdfversion)
        if self.noise is not None and hasattr(self.noise, 'to_version'):
            if getattr(self.noise, 'sdfversion', None) is None:
                self.noise.sdfversion = self.sdfversion
            elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.noise = self.noise.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)
        if self.save is not None and hasattr(self.save, 'to_version'):
            if getattr(self.save, 'sdfversion', None) is None:
                self.save.sdfversion = self.sdfversion
            elif getattr(self.save, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.save = self.save.to_version(self.sdfversion)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def to_version(self, target_version: str) -> "Camera":
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        if self.distortion is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'distortion' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frames and cmp_version(target_version, "1.7") >= 0:
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
        kwargs: dict = {"sdf_version": target_version, "box_type": self.box_type, "camera_info_topic": self.camera_info_topic, "clip": self.clip.to_version(target_version) if self.clip is not None and hasattr(self.clip, "to_version") else self.clip, "depth_camera": self.depth_camera.to_version(target_version) if self.depth_camera is not None and hasattr(self.depth_camera, "to_version") else self.depth_camera, "distortion": self.distortion.to_version(target_version) if self.distortion is not None and hasattr(self.distortion, "to_version") else self.distortion, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "horizontal_fov": self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None and hasattr(self.horizontal_fov, "to_version") else self.horizontal_fov, "image": self.image.to_version(target_version) if self.image is not None and hasattr(self.image, "to_version") else self.image, "lens": self.lens.to_version(target_version) if self.lens is not None and hasattr(self.lens, "to_version") else self.lens, "name": self.name, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise, "optical_frame_id": self.optical_frame_id, "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "save": self.save.to_version(target_version) if self.save is not None and hasattr(self.save, "to_version") else self.save, "segmentation_type": self.segmentation_type, "trigger_topic": self.trigger_topic, "triggered": self.triggered, "visibility_mask": self.visibility_mask}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("camera")
        if self.box_type is not None:
            _c_tmp = ET.Element("box_type")
            _c_tmp.text = self.box_type
            el.append(_c_tmp)
        if self.camera_info_topic is not None:
            _c_tmp = ET.Element("camera_info_topic")
            _c_tmp.text = self.camera_info_topic
            el.append(_c_tmp)
        if self.clip is not None:
            _child_res = self.clip.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('clip')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.depth_camera is not None:
            _child_res = self.depth_camera.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('depth_camera')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.distortion is not None:
            _child_res = self.distortion.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('distortion')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.frames or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.horizontal_fov is not None:
            _child_res = self.horizontal_fov.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('horizontal_fov')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.image is not None:
            _child_res = self.image.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('image')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.lens is not None:
            _child_res = self.lens.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('lens')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        if self.noise is not None:
            _child_res = self.noise.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('noise')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.optical_frame_id is not None:
            _c_tmp = ET.Element("optical_frame_id")
            _c_tmp.text = self.optical_frame_id
            el.append(_c_tmp)
        if self.pose is not None:
            _child_res = self.pose.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.save is not None:
            _child_res = self.save.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('save')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.segmentation_type is not None:
            _c_tmp = ET.Element("segmentation_type")
            _c_tmp.text = self.segmentation_type
            el.append(_c_tmp)
        if self.trigger_topic is not None:
            _c_tmp = ET.Element("trigger_topic")
            _c_tmp.text = self.trigger_topic
            el.append(_c_tmp)
        if self.triggered is not None:
            _c_tmp = ET.Element("triggered")
            _c_tmp.text = str(self.triggered).lower()
            el.append(_c_tmp)
        if self.visibility_mask is not None:
            _c_tmp = ET.Element("visibility_mask")
            _c_tmp.text = str(self.visibility_mask)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Camera | SDFError":
        from ..elements.frame import Frame
        from ..elements.pose import Pose
        _c_tmp = el.find("box_type")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "2d"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("box_type")
            _box_type = _val
        else:
            _box_type = None
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        _c_tmp = el.find("camera_info_topic")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("camera_info_topic")
            _camera_info_topic = _val
        else:
            _camera_info_topic = None
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        _c_clip = el.find("clip")
        if _c_clip is not None:
            _res = cls.Clip._from_sdf(_c_clip, version)
            if isinstance(_res, SDFError):
                return _res.extend("clip")
            _clip = _res
        else:
            _clip = None
        _c_depth_camera = el.find("depth_camera")
        if _c_depth_camera is not None:
            _res = cls.DepthCamera._from_sdf(_c_depth_camera, version)
            if isinstance(_res, SDFError):
                return _res.extend("depth_camera")
            _depth_camera = _res
        else:
            _depth_camera = None
        _c_distortion = el.find("distortion")
        if _c_distortion is not None:
            _res = cls.Distortion._from_sdf(_c_distortion, version)
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
            _res = cls.HorizontalFov._from_sdf(_c_horizontal_fov, version)
            if isinstance(_res, SDFError):
                return _res.extend("horizontal_fov")
            _horizontal_fov = _res
        else:
            _horizontal_fov = None
        _c_image = el.find("image")
        if _c_image is not None:
            _res = cls.Image._from_sdf(_c_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        else:
            _image = None
        _c_lens = el.find("lens")
        if _c_lens is not None:
            _res = cls.Lens._from_sdf(_c_lens, version)
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
            _res = cls.Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
        if _noise is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'noise' is not supported in SDF version {version} (added in 1.4)")
        _c_tmp = el.find("optical_frame_id")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else None
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("optical_frame_id")
            _optical_frame_id = _val
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
            _res = cls.Save._from_sdf(_c_save, version)
            if isinstance(_res, SDFError):
                return _res.extend("save")
            _save = _res
        else:
            _save = None
        _c_tmp = el.find("segmentation_type")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "semantic"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("segmentation_type")
            _segmentation_type = _val
        else:
            _segmentation_type = None
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        _c_tmp = el.find("trigger_topic")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else None
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("trigger_topic")
            _trigger_topic = _val
        else:
            _trigger_topic = None
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        _c_tmp = el.find("triggered")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("triggered")
            _triggered = _val
        else:
            _triggered = None
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        _c_tmp = el.find("visibility_mask")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 4294967295
            _val = _parse_uint32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("visibility_mask")
            _visibility_mask = _val
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, box_type=_box_type, camera_info_topic=_camera_info_topic, clip=_clip, depth_camera=_depth_camera, distortion=_distortion, frames=_frames, horizontal_fov=_horizontal_fov, image=_image, lens=_lens, name=_name, noise=_noise, optical_frame_id=_optical_frame_id, pose=_pose, save=_save, segmentation_type=_segmentation_type, trigger_topic=_trigger_topic, triggered=_triggered, visibility_mask=_visibility_mask)
