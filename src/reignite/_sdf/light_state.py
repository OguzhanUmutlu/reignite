### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.pose import Pose


# noinspection PyUnusedImports
class LightState(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        name: str | None = "__default__",
        pose: "Pose" = None
    ):
        super().__init__(sdf_version)
        self.name = name if name is not None else "__default__"
        self.pose = pose
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "LightState":
        from ..elements.pose import Pose
        kwargs: dict = {"sdf_version": target_version, "name": self.name, "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("light_state")
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
