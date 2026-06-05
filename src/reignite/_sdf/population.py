### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_int32
import typing
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.box import Box
    from ..elements.cylinder import Cylinder
    from ..elements.frame import Frame
    from ..elements.model import Model
    from ..elements.pose import Pose

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Population(BaseModel):
    class Distribution(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            cols: int | None = None,
            rows: int | None = None,
            step: _Vector3T | None = None,
            type: str | None = None
        ):
            super().__init__(sdf_version)
            self.cols = cols
            self.rows = rows
            self.step = _vector3(step) if step is not None else None
            self.type = type

        def to_version(self, target_version: str) -> "Population.Distribution":
            kwargs: dict = {"sdf_version": target_version, "cols": self.cols, "rows": self.rows, "step": self.step, "type": self.type}
            return Population.Distribution(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
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
        model_count: int | None = None,
        models: List["Model"] = None,
        name: str | None = None,
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
            if getattr(self.box, 'sdfversion', None) is None:
                self.box.sdfversion = self.sdfversion
            elif getattr(self.box, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.box = self.box.to_version(self.sdfversion)
        if self.cylinder is not None and hasattr(self.cylinder, 'to_version'):
            if getattr(self.cylinder, 'sdfversion', None) is None:
                self.cylinder.sdfversion = self.sdfversion
            elif getattr(self.cylinder, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.cylinder = self.cylinder.to_version(self.sdfversion)
        if self.distribution is not None and hasattr(self.distribution, 'to_version'):
            if getattr(self.distribution, 'sdfversion', None) is None:
                self.distribution.sdfversion = self.sdfversion
            elif getattr(self.distribution, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.distribution = self.distribution.to_version(self.sdfversion)
        for _i, _c in enumerate(self.frames):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.frames[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.models):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.models[_i] = _c.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)

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
        if self.frames and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frames' is not supported in SDF version {target_version} (removed in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "box": self.box.to_version(target_version) if self.box is not None and hasattr(self.box, "to_version") else self.box, "cylinder": self.cylinder.to_version(target_version) if self.cylinder is not None and hasattr(self.cylinder, "to_version") else self.cylinder, "distribution": self.distribution.to_version(target_version) if self.distribution is not None and hasattr(self.distribution, "to_version") else self.distribution, "frames": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.frames or [])], "model_count": self.model_count, "models": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])], "name": self.name, "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose}
        return Population(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.box import Box
        from ..elements.cylinder import Cylinder
        from ..elements.frame import Frame
        from ..elements.model import Model
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("population")
        if self.box is not None:
            _child_res = self.box.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('box')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.cylinder is not None:
            _child_res = self.cylinder.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('cylinder')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.distribution is not None:
            _child_res = self.distribution.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('distribution')
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
        if self.model_count is not None:
            _c_tmp = ET.Element("model_count")
            _c_tmp.text = str(self.model_count)
            el.append(_c_tmp)
        for item in (self.models or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('model')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            _child_res = self.pose.to_sdf(version)
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
            _distribution = None
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
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, box=_box, cylinder=_cylinder, distribution=_distribution, frames=_frames, model_count=_model_count, models=_models, name=_name, pose=_pose)
