### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError

from .actor import Actor
from .light import Light
from .model import Model
from .world import World


class Sdf(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        actor: List["Actor"] = None,
        light: List["Light"] = None,
        model: List["Model"] = None,
        version: str = "1.3",
        world: List["World"] = None
    ):
        self.__version__ = sdf_version
        self.actor = actor or []
        self.light = light or []
        self.model = model or []
        self.version = version
        self.world = world or []

    def to_version(self, target_version: str) -> "Sdf":
        kwargs = {"sdf_version": target_version}
        kwargs["actor"] = [c.to_version(target_version) for c in (self.actor or [])]
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["version"] = self.version
        kwargs["world"] = [c.to_version(target_version) for c in (self.world or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sdf")
        for item in (self.actor or []):
            el.append(item.to_sdf(version))
        for item in (self.light or []):
            el.append(item.to_sdf(version))
        for item in (self.model or []):
            el.append(item.to_sdf(version))
        if self.version is not None:
            el.set("version", self.version)
        for item in (self.world or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _actor = []
        for c in el.findall("actor"):
            _res = Actor._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("actor")
            _actor.append(_res)
        _light = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _light.append(_res)
        _model = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _model.append(_res)
        _version = el.get("version", "1.3")
        if isinstance(_version, SDFError):
            return _version.extend("@version")
        _world = []
        for c in el.findall("world"):
            _res = World._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("world")
            _world.append(_res)
        return cls(sdf_version=version, actor=_actor, light=_light, model=_model, version=_version, world=_world)
