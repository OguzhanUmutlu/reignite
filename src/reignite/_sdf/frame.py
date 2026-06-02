### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.pose import Pose


# noinspection PyUnusedImports
class Frame(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        attached_to: str | None = "",
        name: str | None = "",
        pose: "Pose" = None
    ):
        super().__init__(sdf_version)
        self.attached_to = attached_to if attached_to is not None else ""
        self.name = name if name is not None else ""
        self.pose = pose
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Frame":
        from ..elements.pose import Pose
        if self.attached_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'attached_to' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "attached_to": self.attached_to, "name": self.name, "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("frame")
        if self.attached_to is not None:
            el.set("attached_to", self.attached_to)
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
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
    def _from_sdf(cls, el: ET.Element, version: str) -> "Frame | SDFError":
        from ..elements.pose import Pose
        _attached_to = el.get("attached_to", "")
        if isinstance(_attached_to, SDFError):
            return _attached_to.extend("@attached_to")
        if _attached_to is not None and cmp_version(version, "1.7") < 0:
            if _attached_to != "":
                return SDFError(f"'attached_to' is not supported in SDF version {version} (added in 1.7)")
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "")
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
        return cls(sdf_version=version, attached_to=_attached_to, name=_name, pose=_pose)
