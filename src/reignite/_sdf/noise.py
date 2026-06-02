### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


# noinspection PyUnusedImports
class Noise(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        bias_mean: float | None = 0.0,
        bias_stddev: float | None = 0.0,
        dynamic_bias_correlation_time: float | None = 0.0,
        dynamic_bias_stddev: float | None = 0.0,
        mean: float | None = 0.0,
        precision: float | None = 0.0,
        stddev: float | None = 0.0,
        type: str | None = "none"
    ):
        super().__init__(sdf_version)
        self.bias_mean = bias_mean if bias_mean is not None else 0.0
        self.bias_stddev = bias_stddev if bias_stddev is not None else 0.0
        self.dynamic_bias_correlation_time = dynamic_bias_correlation_time if dynamic_bias_correlation_time is not None else 0.0
        self.dynamic_bias_stddev = dynamic_bias_stddev if dynamic_bias_stddev is not None else 0.0
        self.mean = mean if mean is not None else 0.0
        self.precision = precision if precision is not None else 0.0
        self.stddev = stddev if stddev is not None else 0.0
        self.type = type if type is not None else "none"

    def to_version(self, target_version: str) -> "Noise":
        if self.dynamic_bias_correlation_time is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_correlation_time' is not supported in SDF version {target_version} (added in 1.6)")
        if self.dynamic_bias_stddev is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'dynamic_bias_stddev' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs: dict = {"sdf_version": target_version, "bias_mean": self.bias_mean, "bias_stddev": self.bias_stddev, "dynamic_bias_correlation_time": self.dynamic_bias_correlation_time, "dynamic_bias_stddev": self.dynamic_bias_stddev, "mean": self.mean, "precision": self.precision, "stddev": self.stddev, "type": self.type}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("noise")
        if self.bias_mean is not None:
            _c_tmp = ET.Element("bias_mean")
            _c_tmp.text = str(self.bias_mean)
            el.append(_c_tmp)
        if self.bias_stddev is not None:
            _c_tmp = ET.Element("bias_stddev")
            _c_tmp.text = str(self.bias_stddev)
            el.append(_c_tmp)
        if self.dynamic_bias_correlation_time is not None:
            _c_tmp = ET.Element("dynamic_bias_correlation_time")
            _c_tmp.text = str(self.dynamic_bias_correlation_time)
            el.append(_c_tmp)
        if self.dynamic_bias_stddev is not None:
            _c_tmp = ET.Element("dynamic_bias_stddev")
            _c_tmp.text = str(self.dynamic_bias_stddev)
            el.append(_c_tmp)
        if self.mean is not None:
            _c_tmp = ET.Element("mean")
            _c_tmp.text = str(self.mean)
            el.append(_c_tmp)
        if self.precision is not None:
            _c_tmp = ET.Element("precision")
            _c_tmp.text = str(self.precision)
            el.append(_c_tmp)
        if self.stddev is not None:
            _c_tmp = ET.Element("stddev")
            _c_tmp.text = str(self.stddev)
            el.append(_c_tmp)
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Noise | SDFError":
        _c_tmp = el.find("bias_mean")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("bias_mean")
            _bias_mean = _val
        else:
            _bias_mean = None
        _c_tmp = el.find("bias_stddev")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("bias_stddev")
            _bias_stddev = _val
        else:
            _bias_stddev = None
        _c_tmp = el.find("dynamic_bias_correlation_time")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("dynamic_bias_correlation_time")
            _dynamic_bias_correlation_time = _val
        else:
            _dynamic_bias_correlation_time = None
        if _dynamic_bias_correlation_time is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_correlation_time' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("dynamic_bias_stddev")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("dynamic_bias_stddev")
            _dynamic_bias_stddev = _val
        else:
            _dynamic_bias_stddev = None
        if _dynamic_bias_stddev is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'dynamic_bias_stddev' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("mean")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("mean")
            _mean = _val
        else:
            _mean = None
        _c_tmp = el.find("precision")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("precision")
            _precision = _val
        else:
            _precision = None
        _c_tmp = el.find("stddev")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("stddev")
            _stddev = _val
        else:
            _stddev = None
        _type = el.get("type", "none")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, bias_mean=_bias_mean, bias_stddev=_bias_stddev, dynamic_bias_correlation_time=_dynamic_bias_correlation_time, dynamic_bias_stddev=_dynamic_bias_stddev, mean=_mean, precision=_precision, stddev=_stddev, type=_type)
