### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.actor import Actor
    from ..elements.light import Light
    from ..elements.model import Model
    from ..elements.world import World


class Gazebo(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        actor: List["Actor"] = None,
        light: List["Light"] = None,
        model: List["Model"] = None,
        version: str = "1.0",
        world: List["World"] = None
    ):
        self.__version__ = sdf_version
        self.actor = actor or []
        self.light = light or []
        self.model = model or []
        self.version = version
        self.world = world or []
        for _i, _c in enumerate(self.actor):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.actor[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.light):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.light[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.model):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.model[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.world):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.world[_i] = _c.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Gazebo":
        from ..elements.actor import Actor
        from ..elements.light import Light
        from ..elements.model import Model
        from ..elements.world import World
        kwargs = {"sdf_version": target_version}
        kwargs["actor"] = [c.to_version(target_version) for c in (self.actor or [])]
        kwargs["light"] = [c.to_version(target_version) for c in (self.light or [])]
        kwargs["model"] = [c.to_version(target_version) for c in (self.model or [])]
        kwargs["version"] = self.version
        kwargs["world"] = [c.to_version(target_version) for c in (self.world or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.actor import Actor
        from ..elements.light import Light
        from ..elements.model import Model
        from ..elements.world import World
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("gazebo")
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
        from ..elements.actor import Actor
        from ..elements.light import Light
        from ..elements.model import Model
        from ..elements.world import World
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
        _version = el.get("version", "1.0")
        if isinstance(_version, SDFError):
            return _version.extend("@version")
        _world = []
        for c in el.findall("world"):
            _res = World._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("world")
            _world.append(_res)
        return cls(sdf_version=version, actor=_actor, light=_light, model=_model, version=_version, world=_world)
