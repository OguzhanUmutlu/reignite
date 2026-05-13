### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


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



class Ray(BaseModel):
    class Noise(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            mean: float = 0.0,
            stddev: float = 0.0,
            type: str = "gaussian"
        ):
            super().__init__(sdf_version)
            self.mean = mean
            self.stddev = stddev
            self.type = type

        def to_version(self, target_version: str) -> "Ray.Noise":
            kwargs = {"sdf_version": target_version}
            kwargs["mean"] = self.mean
            kwargs["stddev"] = self.stddev
            kwargs["type"] = self.type
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Ray.Noise | SDFError":
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

    class Range(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            max: float = 0,
            min: float = 0,
            resolution: float = 0
        ):
            super().__init__(sdf_version)
            self.max = max
            self.min = min
            self.resolution = resolution

        def to_version(self, target_version: str) -> "Ray.Range":
            if self.max is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'max' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.min is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'min' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["max"] = self.max
            kwargs["min"] = self.min
            kwargs["resolution"] = self.resolution
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("range")
            if self.max is not None:
                el.set("max", str(self.max))
            if self.min is not None:
                el.set("min", str(self.min))
            if self.resolution is not None:
                el.set("resolution", str(self.resolution))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Ray.Range | SDFError":
            _max = _parse_double(el.get("max", 0))
            if isinstance(_max, SDFError):
                return _max.extend("@max")
            _min = _parse_double(el.get("min", 0))
            if isinstance(_min, SDFError):
                return _min.extend("@min")
            _resolution = _parse_double(el.get("resolution", 0))
            if isinstance(_resolution, SDFError):
                return _resolution.extend("@resolution")
            return cls(sdf_version=version, max=_max, min=_min, resolution=_resolution)

    class Scan(BaseModel):
        class Horizontal(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                max_angle: float = 0,
                min_angle: float = 0,
                resolution: float = 1,
                samples: int = 1
            ):
                super().__init__(sdf_version)
                self.max_angle = max_angle
                self.min_angle = min_angle
                self.resolution = resolution
                self.samples = samples

            def to_version(self, target_version: str) -> "Ray.Scan.Horizontal":
                if self.max_angle is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.min_angle is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.samples is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'samples' is not supported in SDF version {target_version} (removed in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["max_angle"] = self.max_angle
                kwargs["min_angle"] = self.min_angle
                kwargs["resolution"] = self.resolution
                kwargs["samples"] = self.samples
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("horizontal")
                if self.max_angle is not None:
                    el.set("max_angle", str(self.max_angle))
                if self.min_angle is not None:
                    el.set("min_angle", str(self.min_angle))
                if self.resolution is not None:
                    el.set("resolution", str(self.resolution))
                if self.samples is not None:
                    el.set("samples", str(self.samples))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Ray.Scan.Horizontal | SDFError":
                _max_angle = _parse_double(el.get("max_angle", 0))
                if isinstance(_max_angle, SDFError):
                    return _max_angle.extend("@max_angle")
                _min_angle = _parse_double(el.get("min_angle", 0))
                if isinstance(_min_angle, SDFError):
                    return _min_angle.extend("@min_angle")
                _resolution = _parse_double(el.get("resolution", 1))
                if isinstance(_resolution, SDFError):
                    return _resolution.extend("@resolution")
                _samples = _parse_uint32(el.get("samples", 1))
                if isinstance(_samples, SDFError):
                    return _samples.extend("@samples")
                return cls(sdf_version=version, max_angle=_max_angle, min_angle=_min_angle, resolution=_resolution, samples=_samples)

        class Vertical(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                max_angle: float = 0,
                min_angle: float = 0,
                resolution: float = 1,
                samples: int = 1
            ):
                super().__init__(sdf_version)
                self.max_angle = max_angle
                self.min_angle = min_angle
                self.resolution = resolution
                self.samples = samples

            def to_version(self, target_version: str) -> "Ray.Scan.Vertical":
                if self.max_angle is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'max_angle' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.min_angle is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'min_angle' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.resolution is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'resolution' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.samples is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'samples' is not supported in SDF version {target_version} (removed in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["max_angle"] = self.max_angle
                kwargs["min_angle"] = self.min_angle
                kwargs["resolution"] = self.resolution
                kwargs["samples"] = self.samples
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("vertical")
                if self.max_angle is not None:
                    el.set("max_angle", str(self.max_angle))
                if self.min_angle is not None:
                    el.set("min_angle", str(self.min_angle))
                if self.resolution is not None:
                    el.set("resolution", str(self.resolution))
                if self.samples is not None:
                    el.set("samples", str(self.samples))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Ray.Scan.Vertical | SDFError":
                _max_angle = _parse_double(el.get("max_angle", 0))
                if isinstance(_max_angle, SDFError):
                    return _max_angle.extend("@max_angle")
                _min_angle = _parse_double(el.get("min_angle", 0))
                if isinstance(_min_angle, SDFError):
                    return _min_angle.extend("@min_angle")
                _resolution = _parse_double(el.get("resolution", 1))
                if isinstance(_resolution, SDFError):
                    return _resolution.extend("@resolution")
                _samples = _parse_uint32(el.get("samples", 1))
                if isinstance(_samples, SDFError):
                    return _samples.extend("@samples")
                return cls(sdf_version=version, max_angle=_max_angle, min_angle=_min_angle, resolution=_resolution, samples=_samples)

        def __init__(
            self,
            sdf_version: str | None = None,
            horizontal: "Ray.Scan.Horizontal" = None,
            vertical: "Ray.Scan.Vertical" = None
        ):
            super().__init__(sdf_version)
            self.horizontal = horizontal
            self.vertical = vertical
            if self.horizontal is not None and hasattr(self.horizontal, 'to_version'):
                if getattr(self.horizontal, '__version__', None) is None:
                    self.horizontal.__version__ = self.__version__
                elif getattr(self.horizontal, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.horizontal = self.horizontal.to_version(self.__version__)
            if self.vertical is not None and hasattr(self.vertical, 'to_version'):
                if getattr(self.vertical, '__version__', None) is None:
                    self.vertical.__version__ = self.__version__
                elif getattr(self.vertical, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.vertical = self.vertical.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Ray.Scan":
            kwargs = {"sdf_version": target_version}
            kwargs["horizontal"] = self.horizontal.to_version(target_version) if hasattr(self.horizontal, "to_version") else self.horizontal
            kwargs["vertical"] = self.vertical.to_version(target_version) if hasattr(self.vertical, "to_version") else self.vertical
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("scan")
            if self.horizontal is None:
                self.horizontal = self.__class__.Horizontal(sdf_version=version)
            if self.horizontal is not None:
                if hasattr(self.horizontal, 'to_sdf'):
                    _child_res = self.horizontal.to_sdf(version)
                else:
                    _child_res = str(self.horizontal)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('horizontal')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.vertical is not None:
                if hasattr(self.vertical, 'to_sdf'):
                    _child_res = self.vertical.to_sdf(version)
                else:
                    _child_res = str(self.vertical)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('vertical')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Ray.Scan | SDFError":
            _c_horizontal = el.find("horizontal")
            if _c_horizontal is not None:
                _res = cls.Horizontal._from_sdf(_c_horizontal, version)
                if isinstance(_res, SDFError):
                    return _res.extend("horizontal")
                _horizontal = _res
            else:
                _res = cls.Horizontal._from_sdf(ET.Element("horizontal"), version)
                if isinstance(_res, SDFError):
                    return _res.extend("horizontal")
                _horizontal = _res
            _c_vertical = el.find("vertical")
            if _c_vertical is not None:
                _res = cls.Vertical._from_sdf(_c_vertical, version)
                if isinstance(_res, SDFError):
                    return _res.extend("vertical")
                _vertical = _res
            else:
                _vertical = None
            return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)

    def __init__(
        self,
        sdf_version: str | None = None,
        noise: "Ray.Noise" = None,
        range: "Ray.Range" = None,
        scan: "Ray.Scan" = None,
        visibility_mask: int = 4294967295
    ):
        super().__init__(sdf_version)
        self.noise = noise
        self.range = range
        self.scan = scan
        self.visibility_mask = visibility_mask
        if self.noise is not None and hasattr(self.noise, 'to_version'):
            if getattr(self.noise, '__version__', None) is None:
                self.noise.__version__ = self.__version__
            elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.noise = self.noise.to_version(self.__version__)
        if self.range is not None and hasattr(self.range, 'to_version'):
            if getattr(self.range, '__version__', None) is None:
                self.range.__version__ = self.__version__
            elif getattr(self.range, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.range = self.range.to_version(self.__version__)
        if self.scan is not None and hasattr(self.scan, 'to_version'):
            if getattr(self.scan, '__version__', None) is None:
                self.scan.__version__ = self.__version__
            elif getattr(self.scan, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.scan = self.scan.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Ray":
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if hasattr(self.noise, "to_version") else self.noise
        kwargs["range"] = self.range.to_version(target_version) if hasattr(self.range, "to_version") else self.range
        kwargs["scan"] = self.scan.to_version(target_version) if hasattr(self.scan, "to_version") else self.scan
        kwargs["visibility_mask"] = self.visibility_mask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("ray")
        if self.noise is not None:
            if hasattr(self.noise, 'to_sdf'):
                _child_res = self.noise.to_sdf(version)
            else:
                _child_res = str(self.noise)
            if isinstance(_child_res, str):
                _item_el = ET.Element('noise')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.range is None:
            self.range = self.__class__.Range(sdf_version=version)
        if self.range is not None:
            if hasattr(self.range, 'to_sdf'):
                _child_res = self.range.to_sdf(version)
            else:
                _child_res = str(self.range)
            if isinstance(_child_res, str):
                _item_el = ET.Element('range')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.scan is None:
            self.scan = self.__class__.Scan(sdf_version=version)
        if self.scan is not None:
            if hasattr(self.scan, 'to_sdf'):
                _child_res = self.scan.to_sdf(version)
            else:
                _child_res = str(self.scan)
            if isinstance(_child_res, str):
                _item_el = ET.Element('scan')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.visibility_mask is not None:
            _c_tmp = ET.Element("visibility_mask")
            _c_tmp.text = str(self.visibility_mask)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Ray | SDFError":
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
        _c_range = el.find("range")
        if _c_range is not None:
            _res = cls.Range._from_sdf(_c_range, version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        else:
            _res = cls.Range._from_sdf(ET.Element("range"), version)
            if isinstance(_res, SDFError):
                return _res.extend("range")
            _range = _res
        _c_scan = el.find("scan")
        if _c_scan is not None:
            _res = cls.Scan._from_sdf(_c_scan, version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        else:
            _res = cls.Scan._from_sdf(ET.Element("scan"), version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        _c_tmp = el.find("visibility_mask")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 4294967295
            _val = _parse_uint32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("visibility_mask")
            _visibility_mask = _val
        else:
            _visibility_mask = None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            return SDFError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, noise=_noise, range=_range, scan=_scan, visibility_mask=_visibility_mask)
