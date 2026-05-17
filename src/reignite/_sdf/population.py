### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3, _Vector3T, _vector3

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


def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


class Population(BaseModel):
    class Distribution(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            cols: int = 1,
            rows: int = 1,
            step: _Vector3T = None,
            type: str = "random"
        ):
            super().__init__(sdf_version)
            if step is None:
                step = _vector3("0.5 0.5 0")
            else:
                step = _vector3(step)
            self.cols = cols
            self.rows = rows
            self.step = step
            self.type = type

        def to_version(self, target_version: str) -> "Population.Distribution":
            kwargs = {"sdf_version": target_version}
            kwargs["cols"] = self.cols
            kwargs["rows"] = self.rows
            kwargs["step"] = self.step
            kwargs["type"] = self.type
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
                _c_tmp = ET.Element("cols")
                _c_tmp.text = str(self.cols)
                el.append(_c_tmp)
            if self.rows is not None:
                _c_tmp = ET.Element("rows")
                _c_tmp.text = str(self.rows)
                el.append(_c_tmp)
            if self.step is not None:
                _c_tmp = ET.Element("step")
                _c_tmp.text = str(self.step)
                el.append(_c_tmp)
            if self.type is not None:
                _c_tmp = ET.Element("type")
                _c_tmp.text = self.type
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Population.Distribution | SDFError":
            _c_tmp = el.find("cols")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 1
                _val = _parse_int32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("cols")
                _cols = _val
            else:
                _cols = None
            _c_tmp = el.find("rows")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 1
                _val = _parse_int32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("rows")
                _rows = _val
            else:
                _rows = None
            _c_tmp = el.find("step")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "0.5 0.5 0"
                _val = _parse_vector3(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("step")
                _step = _val
            else:
                _step = None
            _c_tmp = el.find("type")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "random"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("type")
                _type = _val
            else:
                _type = None
            return cls(sdf_version=version, cols=_cols, rows=_rows, step=_step, type=_type)

    def __init__(
        self,
        sdf_version: str | None = None,
        box: "Box" = None,
        cylinder: "Cylinder" = None,
        distribution: "Population.Distribution" = None,
        frames: List["Frame"] = None,
        model_count: int = 1,
        models: List["Model"] = None,
        name: str = "__default__",
        pose: "Pose" = None
    ):
        super().__init__(sdf_version)
        self.box = box
        self.cylinder = cylinder
        self.distribution = distribution
        self.frames = frames or []
        self.model_count = model_count
        self.models = models or []
        self.name = name
        self.pose = pose
        if self.box is not None and hasattr(self.box, 'to_version'):
            if getattr(self.box, '__version__', None) is None:
                self.box.__version__ = self.__version__
            elif getattr(self.box, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.box = self.box.to_version(self.__version__)
        if self.cylinder is not None and hasattr(self.cylinder, 'to_version'):
            if getattr(self.cylinder, '__version__', None) is None:
                self.cylinder.__version__ = self.__version__
            elif getattr(self.cylinder, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.cylinder = self.cylinder.to_version(self.__version__)
        if self.distribution is not None and hasattr(self.distribution, 'to_version'):
            if getattr(self.distribution, '__version__', None) is None:
                self.distribution.__version__ = self.__version__
            elif getattr(self.distribution, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.distribution = self.distribution.to_version(self.__version__)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frames[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.models):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.models[_i] = _c.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def add_frame(self, *items: "Frame"):
        if self.frames is None:
            self.frames = []
        self.frames.extend(items)

    def add_model(self, *items: "Model"):
        if self.models is None:
            self.models = []
        self.models.extend(items)

    def to_version(self, target_version: str) -> "Population":
        from ..elements.box import Box
        from ..elements.cylinder import Cylinder
        from ..elements.frame import Frame
        from ..elements.model import Model
        from ..elements.pose import Pose
        if self.frames is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["box"] = self.box.to_version(target_version) if hasattr(self.box, "to_version") else self.box
        kwargs["cylinder"] = self.cylinder.to_version(target_version) if hasattr(self.cylinder, "to_version") else self.cylinder
        kwargs["distribution"] = self.distribution.to_version(target_version) if hasattr(self.distribution, "to_version") else self.distribution
        kwargs["frames"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])]
        kwargs["model_count"] = self.model_count
        kwargs["models"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])]
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
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
            if hasattr(self.box, 'to_sdf'):
                _child_res = self.box.to_sdf(version)
            else:
                _child_res = str(self.box)
            if isinstance(_child_res, str):
                _item_el = ET.Element('box')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.cylinder is not None:
            if hasattr(self.cylinder, 'to_sdf'):
                _child_res = self.cylinder.to_sdf(version)
            else:
                _child_res = str(self.cylinder)
            if isinstance(_child_res, str):
                _item_el = ET.Element('cylinder')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.distribution is None:
            self.distribution = self.__class__.Distribution(sdf_version=version)
        if self.distribution is not None:
            if hasattr(self.distribution, 'to_sdf'):
                _child_res = self.distribution.to_sdf(version)
            else:
                _child_res = str(self.distribution)
            if isinstance(_child_res, str):
                _item_el = ET.Element('distribution')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.frames or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('frame')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.model_count is not None:
            _c_tmp = ET.Element("model_count")
            _c_tmp.text = str(self.model_count)
            el.append(_c_tmp)
        for item in (self.models or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('model')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            if hasattr(self.pose, 'to_sdf'):
                _child_res = self.pose.to_sdf(version)
            else:
                _child_res = str(self.pose)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Population | SDFError":
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
            _res = cls.Distribution._from_sdf(_c_distribution, version)
            if isinstance(_res, SDFError):
                return _res.extend("distribution")
            _distribution = _res
        else:
            _res = cls.Distribution._from_sdf(ET.Element("distribution"), version)
            if isinstance(_res, SDFError):
                return _res.extend("distribution")
            _distribution = _res
        _frames = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frames.append(_res)
        _c_tmp = el.find("model_count")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_int32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("model_count")
            _model_count = _val
        else:
            _model_count = None
        _models = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _models.append(_res)
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
        return cls(sdf_version=version, box=_box, cylinder=_cylinder, distribution=_distribution, frames=_frames, model_count=_model_count, models=_models, name=_name, pose=_pose)
