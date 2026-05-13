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


class Sdf(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        actors: List["Actor"] = None,
        lights: List["Light"] = None,
        models: List["Model"] = None,
        version: str = "1.3",
        worlds: List["World"] = None
    ):
        super().__init__(sdf_version)
        self.actors = actors or []
        self.lights = lights or []
        self.models = models or []
        self.version = version
        self.worlds = worlds or []
        for _i, _c in enumerate(self.actors):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.actors[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.lights):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.lights[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.models):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.models[_i] = _c.to_version(self.__version__)
        for _i, _c in enumerate(self.worlds):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.worlds[_i] = _c.to_version(self.__version__)

    def add_actor(self, *items: "Actor"):
        if self.actors is None:
            self.actors = []
        self.actors.extend(items)

    def add_light(self, *items: "Light"):
        if self.lights is None:
            self.lights = []
        self.lights.extend(items)

    def add_model(self, *items: "Model"):
        if self.models is None:
            self.models = []
        self.models.extend(items)

    def add_world(self, *items: "World"):
        if self.worlds is None:
            self.worlds = []
        self.worlds.extend(items)

    def to_version(self, target_version: str) -> "Sdf":
        from ..elements.actor import Actor
        from ..elements.light import Light
        from ..elements.model import Model
        from ..elements.world import World
        kwargs = {"sdf_version": target_version}
        kwargs["actors"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.actors or [])]
        kwargs["lights"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.lights or [])]
        kwargs["models"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.models or [])]
        kwargs["version"] = self.version
        kwargs["worlds"] = [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.worlds or [])]
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
        el = ET.Element("sdf")
        for item in (self.actors or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('actor')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        for item in (self.lights or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('light')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
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
        if self.version is not None:
            el.set("version", self.version)
        for item in (self.worlds or []):
            if hasattr(item, 'to_sdf'):
                _child_res = item.to_sdf(version)
            else:
                _child_res = str(item)
            if isinstance(_child_res, str):
                _item_el = ET.Element('world')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Sdf | SDFError":
        from ..elements.actor import Actor
        from ..elements.light import Light
        from ..elements.model import Model
        from ..elements.world import World
        _actors = []
        for c in el.findall("actor"):
            _res = Actor._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("actor")
            _actors.append(_res)
        _lights = []
        for c in el.findall("light"):
            _res = Light._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("light")
            _lights.append(_res)
        _models = []
        for c in el.findall("model"):
            _res = Model._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("model")
            _models.append(_res)
        _version = el.get("version", "1.3")
        if isinstance(_version, SDFError):
            return _version.extend("@version")
        _worlds = []
        for c in el.findall("world"):
            _res = World._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("world")
            _worlds.append(_res)
        return cls(sdf_version=version, actors=_actors, lights=_lights, models=_models, version=_version, worlds=_worlds)
