### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_uint32
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


# noinspection PyUnusedImports
class Lidar(BaseModel):
    class Noise(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            mean: float | None = 0.0,
            stddev: float | None = 0.0,
            type: str | None = "gaussian"
        ):
            super().__init__(sdf_version)
            self.mean = mean if mean is not None else 0.0
            self.stddev = stddev if stddev is not None else 0.0
            self.type = type if type is not None else "gaussian"

        def to_version(self, target_version: str) -> "Lidar.Noise":
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Lidar.Noise | SDFError":
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
            self.max = max if max is not None else 0
            self.min = min if min is not None else 0
            self.resolution = resolution if resolution is not None else 0

        def to_version(self, target_version: str) -> "Lidar.Range":
            kwargs: dict = {"sdf_version": target_version, "max": self.max, "min": self.min, "resolution": self.resolution}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("range")
            if self.max is not None:
                _c_tmp = ET.Element("max")
                _c_tmp.text = str(self.max)
                el.append(_c_tmp)
            if self.min is not None:
                _c_tmp = ET.Element("min")
                _c_tmp.text = str(self.min)
                el.append(_c_tmp)
            if self.resolution is not None:
                _c_tmp = ET.Element("resolution")
                _c_tmp.text = str(self.resolution)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Lidar.Range | SDFError":
            _c_tmp = el.find("max")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("max")
                _max = _val
            else:
                _max = None
            _c_tmp = el.find("min")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("min")
                _min = _val
            else:
                _min = None
            _c_tmp = el.find("resolution")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("resolution")
                _resolution = _val
            else:
                _resolution = None
            return cls(sdf_version=version, max=_max, min=_min, resolution=_resolution)

    class Scan(BaseModel):
        class Horizontal(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                max_angle: float | None = 0,
                min_angle: float | None = 0,
                resolution: float | None = 1,
                samples: int | None = 640
            ):
                super().__init__(sdf_version)
                self.max_angle = max_angle if max_angle is not None else 0
                self.min_angle = min_angle if min_angle is not None else 0
                self.resolution = resolution if resolution is not None else 1
                self.samples = samples if samples is not None else 640

            def to_version(self, target_version: str) -> "Lidar.Scan.Horizontal":
                kwargs: dict = {"sdf_version": target_version, "max_angle": self.max_angle, "min_angle": self.min_angle, "resolution": self.resolution, "samples": self.samples}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("horizontal")
                if self.max_angle is not None:
                    _c_tmp = ET.Element("max_angle")
                    _c_tmp.text = str(self.max_angle)
                    el.append(_c_tmp)
                if self.min_angle is not None:
                    _c_tmp = ET.Element("min_angle")
                    _c_tmp.text = str(self.min_angle)
                    el.append(_c_tmp)
                if self.resolution is not None:
                    _c_tmp = ET.Element("resolution")
                    _c_tmp.text = str(self.resolution)
                    el.append(_c_tmp)
                if self.samples is not None:
                    _c_tmp = ET.Element("samples")
                    _c_tmp.text = str(self.samples)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Lidar.Scan.Horizontal | SDFError":
                _c_tmp = el.find("max_angle")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("max_angle")
                    _max_angle = _val
                else:
                    _max_angle = None
                _c_tmp = el.find("min_angle")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("min_angle")
                    _min_angle = _val
                else:
                    _min_angle = None
                _c_tmp = el.find("resolution")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("resolution")
                    _resolution = _val
                else:
                    _resolution = None
                _c_tmp = el.find("samples")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 640
                    _val = _parse_uint32(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("samples")
                    _samples = _val
                else:
                    _samples = None
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
                self.max_angle = max_angle if max_angle is not None else 0
                self.min_angle = min_angle if min_angle is not None else 0
                self.resolution = resolution if resolution is not None else 1
                self.samples = samples if samples is not None else 1

            def to_version(self, target_version: str) -> "Lidar.Scan.Vertical":
                kwargs: dict = {"sdf_version": target_version, "max_angle": self.max_angle, "min_angle": self.min_angle, "resolution": self.resolution, "samples": self.samples}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("vertical")
                if self.max_angle is not None:
                    _c_tmp = ET.Element("max_angle")
                    _c_tmp.text = str(self.max_angle)
                    el.append(_c_tmp)
                if self.min_angle is not None:
                    _c_tmp = ET.Element("min_angle")
                    _c_tmp.text = str(self.min_angle)
                    el.append(_c_tmp)
                if self.resolution is not None:
                    _c_tmp = ET.Element("resolution")
                    _c_tmp.text = str(self.resolution)
                    el.append(_c_tmp)
                if self.samples is not None:
                    _c_tmp = ET.Element("samples")
                    _c_tmp.text = str(self.samples)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Lidar.Scan.Vertical | SDFError":
                _c_tmp = el.find("max_angle")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("max_angle")
                    _max_angle = _val
                else:
                    _max_angle = None
                _c_tmp = el.find("min_angle")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("min_angle")
                    _min_angle = _val
                else:
                    _min_angle = None
                _c_tmp = el.find("resolution")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("resolution")
                    _resolution = _val
                else:
                    _resolution = None
                _c_tmp = el.find("samples")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_uint32(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("samples")
                    _samples = _val
                else:
                    _samples = None
                return cls(sdf_version=version, max_angle=_max_angle, min_angle=_min_angle, resolution=_resolution, samples=_samples)

        def __init__(
            self,
            sdf_version: str | None = None,
            horizontal: "Lidar.Scan.Horizontal" = None,
            vertical: "Lidar.Scan.Vertical" = None
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

        def to_version(self, target_version: str) -> "Lidar.Scan":
            kwargs: dict = {"sdf_version": target_version, "horizontal": self.horizontal.to_version(target_version) if self.horizontal is not None and hasattr(self.horizontal, "to_version") else self.horizontal, "vertical": self.vertical.to_version(target_version) if self.vertical is not None and hasattr(self.vertical, "to_version") else self.vertical}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("scan")
            if self.horizontal is None:
                self.horizontal = self.__class__.Horizontal(sdf_version=version)
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Lidar.Scan | SDFError":
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
        noise: "Lidar.Noise" = None,
        range: "Lidar.Range" = None,
        scan: "Lidar.Scan" = None,
        visibility_mask: int | None = 4294967295
    ):
        super().__init__(sdf_version)
        self.noise = noise
        self.range = range
        self.scan = scan
        self.visibility_mask = visibility_mask if visibility_mask is not None else 4294967295
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

    def to_version(self, target_version: str) -> "Lidar":
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise, "range": self.range.to_version(target_version) if self.range is not None and hasattr(self.range, "to_version") else self.range, "scan": self.scan.to_version(target_version) if self.scan is not None and hasattr(self.scan, "to_version") else self.scan, "visibility_mask": self.visibility_mask}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("lidar")
        if self.noise is not None:
            _child_res = self.noise.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('noise')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.range is None:
            self.range = self.__class__.Range(sdf_version=version)
        if self.range is not None:
            _child_res = self.range.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('range')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.scan is None:
            self.scan = self.__class__.Scan(sdf_version=version)
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
    def _from_sdf(cls, el: ET.Element, version: str) -> "Lidar | SDFError":
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = cls.Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _noise = None
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
