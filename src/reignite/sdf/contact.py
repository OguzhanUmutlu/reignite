### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


class Collision(BaseModel):
    def __init__(self, sdf_version: str, collision: str = "__default__", name: str = "__default__"):
        self.__version__ = sdf_version
        self.collision = collision
        self.name = name

    def to_version(self, target_version: str) -> "Collision":
        if self.name is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'name' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = self.collision
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision")
        if self.collision is not None:
            el.text = self.collision
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _collision = _text
        if isinstance(_collision, SDFError):
            return _collision
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, collision=_collision, name=_name)


class Topic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = "__default_topic__"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "Topic":
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default_topic__"
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)


class Contact(BaseModel):
    def __init__(self, sdf_version: str, collision: "Collision" = None, topic: "Topic" = None):
        self.__version__ = sdf_version
        self.collision = collision
        self.topic = topic

    def to_version(self, target_version: str) -> "Contact":
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = self.collision.to_version(target_version) if self.collision is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.collision is not None:
            el.append(self.collision.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_collision = el.find("collision")
        if _c_collision is not None:
            _res = Collision._from_sdf(_c_collision, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collision = _res
        else:
            _collision = None
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = Topic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        return cls(sdf_version=version, collision=_collision, topic=_topic)
