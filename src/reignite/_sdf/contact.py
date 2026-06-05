### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version


# noinspection PyUnusedImports
class Contact(BaseModel):
    class Collision(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            collision: str | None = None,
            name: str | None = None
        ):
            super().__init__(sdf_version)
            self.collision = collision
            self.name = name

        def to_version(self, target_version: str) -> "Contact.Collision":
            if self.name is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'name' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs: dict = {"sdf_version": target_version, "collision": self.collision, "name": self.name}
            return Contact.Collision(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("collision")
            if self.collision is not None:
                el.text = self.collision
            if self.name is not None:
                el.set("name", self.name)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Contact.Collision | SDFError":
            _raw_collision = el.text
            if _raw_collision is not None:
                _collision = _raw_collision
                if isinstance(_collision, SDFError):
                    return _collision
            else:
                _collision = None
            _raw_name = el.get("name")
            if _raw_name is not None:
                _name = _raw_name
                if isinstance(_name, SDFError):
                    return _name.extend("@name")
            else:
                _name = None
            return cls(sdf_version=version, collision=_collision, name=_name)

    def __init__(
        self,
        sdf_version: str | None = None,
        collision: "Contact.Collision" = None,
        topic: str | None = None
    ):
        super().__init__(sdf_version)
        self.collision = collision
        self.topic = topic
        if self.collision is not None and hasattr(self.collision, 'to_version'):
            if getattr(self.collision, 'sdfversion', None) is None:
                self.collision.sdfversion = self.sdfversion
            elif getattr(self.collision, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.collision = self.collision.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Contact":
        kwargs: dict = {"sdf_version": target_version, "collision": self.collision.to_version(target_version) if self.collision is not None and hasattr(self.collision, "to_version") else self.collision, "topic": self.topic}
        return Contact(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("contact")
        if self.collision is not None:
            _child_res = self.collision.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('collision')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.topic is not None:
            _c_tmp = ET.Element("topic")
            _c_tmp.text = self.topic
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Contact | SDFError":
        _c_collision = el.find("collision")
        if _c_collision is not None:
            _res = cls.Collision._from_sdf(_c_collision, version)
            if isinstance(_res, SDFError):
                return _res.extend("collision")
            _collision = _res
        else:
            _collision = None
        _c_tmp = el.find("topic")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default_topic__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("topic")
            _topic = _val
        else:
            _topic = None
        return cls(sdf_version=version, collision=_collision, topic=_topic)
