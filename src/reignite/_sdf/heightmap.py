### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double, _parse_uint32
from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import _Vector3T, _vector3
from ..utils.version import cmp_version

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Heightmap(BaseModel):
    class Blend(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            fade_dist: float | None = None,
            min_height: float | None = None
        ):
            super().__init__(sdf_version)
            self.fade_dist = fade_dist
            self.min_height = min_height

        def to_version(self, target_version: str) -> "Heightmap.Blend":
            kwargs: dict = {"sdf_version": target_version, "fade_dist": self.fade_dist, "min_height": self.min_height}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("blend")
            if self.fade_dist is not None:
                _c_tmp = ET.Element("fade_dist")
                _c_tmp.text = str(self.fade_dist)
                el.append(_c_tmp)
            if self.min_height is not None:
                _c_tmp = ET.Element("min_height")
                _c_tmp.text = str(self.min_height)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Heightmap.Blend | SDFError":
            _c_tmp = el.find("fade_dist")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("fade_dist")
                _fade_dist = _val
            else:
                _fade_dist = None
            _c_tmp = el.find("min_height")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("min_height")
                _min_height = _val
            else:
                _min_height = None
            return cls(sdf_version=version, fade_dist=_fade_dist, min_height=_min_height)

    class Texture(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            diffuse: str | None = None,
            normal: str | None = None,
            size: float | None = None
        ):
            super().__init__(sdf_version)
            self.diffuse = diffuse
            self.normal = normal
            self.size = size

        def to_version(self, target_version: str) -> "Heightmap.Texture":
            kwargs: dict = {"sdf_version": target_version, "diffuse": self.diffuse, "normal": self.normal, "size": self.size}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("texture")
            if self.diffuse is not None:
                _c_tmp = ET.Element("diffuse")
                _c_tmp.text = self.diffuse
                el.append(_c_tmp)
            if self.normal is not None:
                _c_tmp = ET.Element("normal")
                _c_tmp.text = self.normal
                el.append(_c_tmp)
            if self.size is not None:
                _c_tmp = ET.Element("size")
                _c_tmp.text = str(self.size)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Heightmap.Texture | SDFError":
            _c_tmp = el.find("diffuse")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("diffuse")
                _diffuse = _val
            else:
                _diffuse = None
            _c_tmp = el.find("normal")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("normal")
                _normal = _val
            else:
                _normal = None
            _c_tmp = el.find("size")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 10
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("size")
                _size = _val
            else:
                _size = None
            return cls(sdf_version=version, diffuse=_diffuse, normal=_normal, size=_size)

    def __init__(
        self,
        sdf_version: str | None = None,
        blends: List["Heightmap.Blend"] = None,
        pos: _Vector3T | None = None,
        sampling: int | None = None,
        size: _Vector3T | None = None,
        textures: List["Heightmap.Texture"] = None,
        uri: str | None = None,
        use_terrain_paging: bool | None = None
    ):
        super().__init__(sdf_version)
        self.blends = blends or []
        self.pos = _vector3(pos) if pos is not None else None
        self.sampling = sampling
        self.size = _vector3(size) if size is not None else None
        self.textures = textures or []
        self.uri = uri
        self.use_terrain_paging = use_terrain_paging
        for _i, _c in enumerate(self.blends):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.blends[_i] = _c.to_version(self.sdfversion)
        for _i, _c in enumerate(self.textures):
            if not hasattr(_c, 'to_version'): continue
            if getattr(_c, 'sdfversion', None) is None:
                _c.sdfversion = self.sdfversion
            elif getattr(_c, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.textures[_i] = _c.to_version(self.sdfversion)

    def add_blend(self, *items: "Heightmap.Blend"):
        if self.blends is None:
            self.blends = []
        self.blends.extend(items)

    def add_texture(self, *items: "Heightmap.Texture"):
        if self.textures is None:
            self.textures = []
        self.textures.extend(items)

    def to_version(self, target_version: str) -> "Heightmap":
        if self.sampling is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs: dict = {"sdf_version": target_version, "blends": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.blends or [])], "pos": self.pos, "sampling": self.sampling, "size": self.size, "textures": [c.to_version(target_version) if hasattr(c, "to_version") else c for c in (self.textures or [])], "uri": self.uri, "use_terrain_paging": self.use_terrain_paging}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("heightmap")
        for item in (self.blends or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('blend')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.pos is not None:
            _c_tmp = ET.Element("pos")
            _c_tmp.text = str(self.pos)
            el.append(_c_tmp)
        if self.sampling is not None:
            _c_tmp = ET.Element("sampling")
            _c_tmp.text = str(self.sampling)
            el.append(_c_tmp)
        if self.size is not None:
            _c_tmp = ET.Element("size")
            _c_tmp.text = str(self.size)
            el.append(_c_tmp)
        for item in (self.textures or []):
            _child_res = item.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('texture')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.uri is not None:
            _c_tmp = ET.Element("uri")
            _c_tmp.text = self.uri
            el.append(_c_tmp)
        if self.use_terrain_paging is not None:
            _c_tmp = ET.Element("use_terrain_paging")
            _c_tmp.text = str(self.use_terrain_paging).lower()
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Heightmap | SDFError":
        _blends = []
        for c in el.findall("blend"):
            _res = cls.Blend._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("blend")
            _blends.append(_res)
        _c_tmp = el.find("pos")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("pos")
            _pos = _val
        else:
            _pos = None
        _c_tmp = el.find("sampling")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 2
            _val = _parse_uint32(_text)
            if isinstance(_val, SDFError):
                return _val.extend("sampling")
            _sampling = _val
        else:
            _sampling = None
        if _sampling is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'sampling' is not supported in SDF version {version} (added in 1.6)")
        _c_tmp = el.find("size")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("size")
            _size = _val
        else:
            _size = None
        _textures = []
        for c in el.findall("texture"):
            _res = cls.Texture._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("texture")
            _textures.append(_res)
        _c_tmp = el.find("uri")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("uri")
            _uri = _val
        else:
            _uri = None
        _c_tmp = el.find("use_terrain_paging")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else False
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("use_terrain_paging")
            _use_terrain_paging = _val
        else:
            _use_terrain_paging = None
        return cls(sdf_version=version, blends=_blends, pos=_pos, sampling=_sampling, size=_size, textures=_textures, uri=_uri, use_terrain_paging=_use_terrain_paging)
