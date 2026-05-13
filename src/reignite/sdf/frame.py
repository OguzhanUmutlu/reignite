### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.pose import Pose


class Frame(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        attached_to: str = "",
        name: str = "",
        pose: "Pose" = None
    ):
        super().__init__(sdf_version)
        self.attached_to = attached_to
        self.name = name
        self.pose = pose
        if self.pose is not None:
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Frame":
        from ..elements.pose import Pose
        if self.attached_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'attached_to' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["attached_to"] = self.attached_to
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("frame")
        if self.attached_to is not None:
            el.set("attached_to", self.attached_to)
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
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
