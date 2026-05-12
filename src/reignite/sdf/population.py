### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3

if typing.TYPE_CHECKING:
    from ..elements.box import Box
    from ..elements.cylinder import Cylinder
    from ..elements.frame import Frame
    from ..elements.model import Model
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



class Cols(BaseModel):
    def __init__(self, sdf_version: str | None = None, cols: int = 1):
        self.__version__ = sdf_version
        self.cols = cols

    def to_version(self, target_version: str) -> "Cols":
        kwargs = {"sdf_version": target_version}
        kwargs["cols"] = self.cols
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("cols")
        if self.cols is not None:
            el.text = str(self.cols)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _cols = _parse_int32(_text)
        if isinstance(_cols, SDFError):
            return _cols
        return cls(sdf_version=version, cols=_cols)


class Distribution(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        cols: "Cols" = None,
        rows: "Rows" = None,
        step: "Step" = None,
        type: "Type" = None
    ):
        self.__version__ = sdf_version
        self.cols = cols
        self.rows = rows
        self.step = step
        self.type = type
        if self.cols is not None:
            if getattr(self.cols, '__version__', None) is None:
                self.cols.__version__ = self.__version__
            elif getattr(self.cols, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.cols = self.cols.to_version(self.__version__)
        if self.rows is not None:
            if getattr(self.rows, '__version__', None) is None:
                self.rows.__version__ = self.__version__
            elif getattr(self.rows, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.rows = self.rows.to_version(self.__version__)
        if self.step is not None:
            if getattr(self.step, '__version__', None) is None:
                self.step.__version__ = self.__version__
            elif getattr(self.step, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.step = self.step.to_version(self.__version__)
        if self.type is not None:
            if getattr(self.type, '__version__', None) is None:
                self.type.__version__ = self.__version__
            elif getattr(self.type, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.type = self.type.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Distribution":
        kwargs = {"sdf_version": target_version}
        kwargs["cols"] = self.cols.to_version(target_version) if self.cols is not None else None
        kwargs["rows"] = self.rows.to_version(target_version) if self.rows is not None else None
        kwargs["step"] = self.step.to_version(target_version) if self.step is not None else None
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("distribution")
        if self.cols is not None:
            el.append(self.cols.to_sdf(version))
        if self.rows is not None:
            el.append(self.rows.to_sdf(version))
        if self.step is not None:
            el.append(self.step.to_sdf(version))
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_cols = el.find("cols")
        if _c_cols is not None:
            _res = Cols._from_sdf(_c_cols, version)
            if isinstance(_res, SDFError):
                return _res.extend("cols")
            _cols = _res
        else:
            _cols = None
        _c_rows = el.find("rows")
        if _c_rows is not None:
            _res = Rows._from_sdf(_c_rows, version)
            if isinstance(_res, SDFError):
                return _res.extend("rows")
            _rows = _res
        else:
            _rows = None
        _c_step = el.find("step")
        if _c_step is not None:
            _res = Step._from_sdf(_c_step, version)
            if isinstance(_res, SDFError):
                return _res.extend("step")
            _step = _res
        else:
            _step = None
        _c_type = el.find("type")
        if _c_type is not None:
            _res = Type._from_sdf(_c_type, version)
            if isinstance(_res, SDFError):
                return _res.extend("type")
            _type = _res
        else:
            _type = None
        return cls(sdf_version=version, cols=_cols, rows=_rows, step=_step, type=_type)


class ModelCount(BaseModel):
    def __init__(self, sdf_version: str | None = None, model_count: int = 1):
        self.__version__ = sdf_version
        self.model_count = model_count

    def to_version(self, target_version: str) -> "ModelCount":
        kwargs = {"sdf_version": target_version}
        kwargs["model_count"] = self.model_count
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("model_count")
        if self.model_count is not None:
            el.text = str(self.model_count)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _model_count = _parse_int32(_text)
        if isinstance(_model_count, SDFError):
            return _model_count
        return cls(sdf_version=version, model_count=_model_count)


class Population(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        box: "Box" = None,
        cylinder: "Cylinder" = None,
        distribution: "Distribution" = None,
        frame: List["Frame"] = None,
        model: List["Model"] = None,
        model_count: "ModelCount" = None,
        name: str = "__default__",
        pose: "Pose" = None
    ):
        self.__version__ = sdf_version
        self.box = box
        self.cylinder = cylinder
        self.distribution = distribution
        self.frame = frame or []
        self.model = model or []
        self.model_count = model_count
        self.name = name
        self.pose = pose
        if self.box is not None:
            if getattr(self.box, '__version__', None) is None:
                self.box.__version__ = self.__version__
            elif getattr(self.box, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.box = self.box.to_version(self.__version__)
        if self.cylinder is not None:
            if getattr(self.cylinder, '__version__', None) is None:
                self.cylinder.__version__ = self.__version__
            elif getattr(self.cylinder, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.cylinder = self.cylinder.to_version(self.__version__)
        if self.distribution is not None:
            if getattr(self.distribution, '__version__', None) is None:
                self.distribution.__version__ = self.__version__
            elif getattr(self.distribution, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.distribution = self.distribution.to_version(self.__version__)
        for _i, _c in enumerate(self.frame):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frame[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.model):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.model[_i] = _c.to_version(self.__version__)
        if self.model_count is not None:
            if getattr(self.model_count, '__version__', None) is None:
                self.model_count.__version__ = self.__version__
            elif getattr(self.model_count, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.model_count = self.model_count.to_version(self.__version__)
        if self.pose is not None:
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Population":
        from ..elements.box import Box
        from ..elements.cylinder import Cylinder
        from ..elements.frame import Frame
        from ..elements.model import Model
        from ..elements.pose import Pose
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["box"] = self.box.to_version(target_version) if self.box is not None else None
        kwargs["cylinder"] = self.cylinder.to_version(target_version) if self.cylinder is not None else None
        kwargs["distribution"] = self.distribution.to_version(target_version) if self.distribution is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["model_count"] = self.model_count.to_version(target_version) if self.model_count is not None else None
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.box import Box
        from ..elements.cylinder import Cylinder
        from ..elements.frame import Frame
        from ..elements.model import Model
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("population")
        if self.box is not None:
            el.append(self.box.to_sdf(version))
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf(version))
        if self.distribution is None:
            self.distribution = Distribution(sdf_version=version)
        if self.distribution is not None:
            el.append(self.distribution.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        if self.model_count is not None:
            el.append(self.model_count.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.box import Box
        from ..elements.cylinder import Cylinder
        from ..elements.frame import Frame
        from ..elements.model import Model
        from ..elements.pose import Pose
        _c_box = el.find("box")
        if _c_box is not None:
            _res = Box._from_sdf(_c_box, version)
            if isinstance(_res, SDFError):
                return _res.extend("box")
            _box = _res
        else:
            _box = None
        _c_cylinder = el.find("cylinder")
        if _c_cylinder is not None:
            _res = Cylinder._from_sdf(_c_cylinder, version)
            if isinstance(_res, SDFError):
                return _res.extend("cylinder")
            _cylinder = _res
        else:
            _cylinder = None
        _c_distribution = el.find("distribution")
        if _c_distribution is not None:
            _res = Distribution._from_sdf(_c_distribution, version)
            if isinstance(_res, SDFError):
                return _res.extend("distribution")
            _distribution = _res
        else:
            _res = Distribution._from_sdf(ET.Element("distribution"), version)
            if isinstance(_res, SDFError):
                return _res.extend("distribution")
            _distribution = _res
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        _model = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _model.append(_res)
        _c_model_count = el.find("model_count")
        if _c_model_count is not None:
            _res = ModelCount._from_sdf(_c_model_count, version)
            if isinstance(_res, SDFError):
                return _res.extend("model_count")
            _model_count = _res
        else:
            _model_count = None
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, box=_box, cylinder=_cylinder, distribution=_distribution, frame=_frame, model=_model, model_count=_model_count, name=_name, pose=_pose)


class Rows(BaseModel):
    def __init__(self, sdf_version: str | None = None, rows: int = 1):
        self.__version__ = sdf_version
        self.rows = rows

    def to_version(self, target_version: str) -> "Rows":
        kwargs = {"sdf_version": target_version}
        kwargs["rows"] = self.rows
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("rows")
        if self.rows is not None:
            el.text = str(self.rows)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _rows = _parse_int32(_text)
        if isinstance(_rows, SDFError):
            return _rows
        return cls(sdf_version=version, rows=_rows)


class Step(BaseModel):
    def __init__(self, sdf_version: str | None = None, step: _SDFVector3 = None):
        self.__version__ = sdf_version
        if step is None:
            step = _SDFVector3.from_sdf("0.5 0.5 0", version=sdf_version)
        self.step = step

    def to_version(self, target_version: str) -> "Step":
        kwargs = {"sdf_version": target_version}
        kwargs["step"] = self.step
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("step")
        if self.step is not None:
            el.text = self.step.to_sdf(version)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.5 0.5 0"
        _step = _SDFVector3._from_sdf(_text, version)
        if isinstance(_step, SDFError):
            return _step
        return cls(sdf_version=version, step=_step)


class Type(BaseModel):
    def __init__(self, sdf_version: str | None = None, type: str = "random"):
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
        _text = el.text or "random"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        return cls(sdf_version=version, type=_type)
