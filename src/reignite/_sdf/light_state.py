### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.pose import Pose


class LightState(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        name: str = "__default__",
        pose: "Pose" = None
    ):
        super().__init__(sdf_version)
        self.name = name
        self.pose = pose
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def to_version(self, target_version: str) -> "LightState":
        from ..elements.pose import Pose
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("light_state")
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
    def _from_sdf(cls, el: ET.Element, version: str) -> "LightState | SDFError":
        from ..elements.pose import Pose
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
        return cls(sdf_version=version, name=_name, pose=_pose)
