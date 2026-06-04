### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_uint32
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


# noinspection PyUnusedImports
class Ray(BaseModel):
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

        def to_version(self, target_version: str) -> "Ray.Noise":
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
            max: float | None = 0,
            min: float | None = 0,
            resolution: float | None = 0
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
            kwargs: dict = {"sdf_version": target_version, "max": self.max, "min": self.min, "resolution": self.resolution}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
                max_angle: float | None = 0,
                min_angle: float | None = 0,
                resolution: float | None = 1,
                samples: int | None = 1
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
                kwargs: dict = {"sdf_version": target_version, "max_angle": self.max_angle, "min_angle": self.min_angle, "resolution": self.resolution, "samples": self.samples}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
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
                max_angle: float | None = 0,
                min_angle: float | None = 0,
                resolution: float | None = 1,
                samples: int | None = 1
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
                kwargs: dict = {"sdf_version": target_version, "max_angle": self.max_angle, "min_angle": self.min_angle, "resolution": self.resolution, "samples": self.samples}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
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
                if getattr(self.horizontal, 'sdfversion', None) is None:
                    self.horizontal.sdfversion = self.sdfversion
                elif getattr(self.horizontal, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.horizontal = self.horizontal.to_version(self.sdfversion)
            if self.vertical is not None and hasattr(self.vertical, 'to_version'):
                if getattr(self.vertical, 'sdfversion', None) is None:
                    self.vertical.sdfversion = self.sdfversion
                elif getattr(self.vertical, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.vertical = self.vertical.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Ray.Scan":
            kwargs: dict = {"sdf_version": target_version, "horizontal": self.horizontal.to_version(target_version) if self.horizontal is not None and hasattr(self.horizontal, "to_version") else self.horizontal, "vertical": self.vertical.to_version(target_version) if self.vertical is not None and hasattr(self.vertical, "to_version") else self.vertical}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("scan")
            if self.horizontal is not None:
                _child_res = self.horizontal.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('horizontal')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.vertical is not None:
                _child_res = self.vertical.to_sdf(version)
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
                _horizontal = None
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
        visibility_mask: int | None = None
    ):
        super().__init__(sdf_version)
        self.noise = noise
        self.range = range
        self.scan = scan
        self.visibility_mask = visibility_mask
        if self.noise is not None and hasattr(self.noise, 'to_version'):
            if getattr(self.noise, 'sdfversion', None) is None:
                self.noise.sdfversion = self.sdfversion
            elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.noise = self.noise.to_version(self.sdfversion)
        if self.range is not None and hasattr(self.range, 'to_version'):
            if getattr(self.range, 'sdfversion', None) is None:
                self.range.sdfversion = self.sdfversion
            elif getattr(self.range, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.range = self.range.to_version(self.sdfversion)
        if self.scan is not None and hasattr(self.scan, 'to_version'):
            if getattr(self.scan, 'sdfversion', None) is None:
                self.scan.sdfversion = self.sdfversion
            elif getattr(self.scan, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.scan = self.scan.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Ray":
        if self.noise is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'noise' is not supported in SDF version {target_version} (added in 1.4)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise, "range": self.range.to_version(target_version) if self.range is not None and hasattr(self.range, "to_version") else self.range, "scan": self.scan.to_version(target_version) if self.scan is not None and hasattr(self.scan, "to_version") else self.scan, "visibility_mask": self.visibility_mask}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("ray")
        if self.noise is not None:
            _child_res = self.noise.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('noise')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.range is not None:
            _child_res = self.range.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('range')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.scan is not None:
            _child_res = self.scan.to_sdf(version)
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
            _range = None
        _c_scan = el.find("scan")
        if _c_scan is not None:
            _res = cls.Scan._from_sdf(_c_scan, version)
            if isinstance(_res, SDFError):
                return _res.extend("scan")
            _scan = _res
        else:
            _scan = None
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
