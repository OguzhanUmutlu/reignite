### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color as _SDFColor
from ..utils.version import cmp_version


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class Scene(BaseModel):
    class Ambient(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            ambient: _SDFColor = None,
            rgba: _SDFColor = None
        ):
            super().__init__(sdf_version)
            if ambient is None:
                ambient = _SDFColor.from_sdf("0.0 0.0 0.0 1.0", version=sdf_version)
            if rgba is None:
                rgba = _SDFColor.from_sdf("0.0 0.0 0.0 1.0", version=sdf_version)
            self.ambient = ambient
            self.rgba = rgba

        def to_version(self, target_version: str) -> "Scene.Ambient":
            if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["ambient"] = self.ambient
            kwargs["rgba"] = self.rgba
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("ambient")
            if self.ambient is not None:
                el.text = self.ambient.to_sdf(version)
            if self.rgba is not None:
                el.set("rgba", self.rgba.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Ambient | SDFError":
            _text = el.text or "0.0 0.0 0.0 1.0"
            _ambient = _SDFColor._from_sdf(_text, version)
            if isinstance(_ambient, SDFError):
                return _ambient
            _rgba = _SDFColor._from_sdf(el.get("rgba", "0.0 0.0 0.0 1.0"), version)
            if isinstance(_rgba, SDFError):
                return _rgba.extend("@rgba")
            return cls(sdf_version=version, ambient=_ambient, rgba=_rgba)

    class Background(BaseModel):
        class Sky(BaseModel):
            def __init__(self, sdf_version: str | None = None, material: str = "Gazebo/CloudySky"):
                super().__init__(sdf_version)
                self.material = material

            def to_version(self, target_version: str) -> "Scene.Background.Sky":
                kwargs = {"sdf_version": target_version}
                kwargs["material"] = self.material
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("sky")
                if self.material is not None:
                    el.set("material", self.material)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Background.Sky | SDFError":
                _material = el.get("material", "Gazebo/CloudySky")
                if isinstance(_material, SDFError):
                    return _material.extend("@material")
                return cls(sdf_version=version, material=_material)

        def __init__(
            self,
            sdf_version: str | None = None,
            rgba: _SDFColor = None,
            sky: "Scene.Background.Sky" = None
        ):
            super().__init__(sdf_version)
            if rgba is None:
                rgba = _SDFColor.from_sdf(".7 .7 .7 1", version=sdf_version)
            self.rgba = rgba
            self.sky = sky
            if self.sky is not None:
                if getattr(self.sky, '__version__', None) is None:
                    self.sky.__version__ = self.__version__
                elif getattr(self.sky, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.sky = self.sky.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Scene.Background":
            if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.sky is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'sky' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["rgba"] = self.rgba
            kwargs["sky"] = self.sky.to_version(target_version) if self.sky is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("background")
            if self.rgba is not None:
                el.set("rgba", self.rgba.to_sdf(version))
            if self.sky is not None:
                el.append(self.sky.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Background | SDFError":
            _rgba = _SDFColor._from_sdf(el.get("rgba", ".7 .7 .7 1"), version)
            if isinstance(_rgba, SDFError):
                return _rgba.extend("@rgba")
            _c_sky = el.find("sky")
            if _c_sky is not None:
                _res = cls.Sky._from_sdf(_c_sky, version)
                if isinstance(_res, SDFError):
                    return _res.extend("sky")
                _sky = _res
            else:
                _sky = None
            return cls(sdf_version=version, rgba=_rgba, sky=_sky)

    class Fog(BaseModel):
        class Color(BaseModel):
            def __init__(self, sdf_version: str | None = None, color: _SDFColor = None):
                super().__init__(sdf_version)
                if color is None:
                    color = _SDFColor.from_sdf("1 1 1 1", version=sdf_version)
                self.color = color

            def to_version(self, target_version: str) -> "Scene.Fog.Color":
                if self.color is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'color' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["color"] = self.color
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("color")
                if self.color is not None:
                    el.text = self.color.to_sdf(version)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Fog.Color | SDFError":
                _text = el.text or "1 1 1 1"
                _color = _SDFColor._from_sdf(_text, version)
                if isinstance(_color, SDFError):
                    return _color
                if _color is not None and cmp_version(version, "1.2") < 0:
                    if _color != "1 1 1 1":
                        return SDFError(f"'color' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, color=_color)

        class Density(BaseModel):
            def __init__(self, sdf_version: str | None = None, density: float = 1.0):
                super().__init__(sdf_version)
                self.density = density

            def to_version(self, target_version: str) -> "Scene.Fog.Density":
                if self.density is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["density"] = self.density
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("density")
                if self.density is not None:
                    el.text = str(self.density)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Fog.Density | SDFError":
                _text = el.text or 1.0
                _density = _parse_double(_text)
                if isinstance(_density, SDFError):
                    return _density
                if _density is not None and cmp_version(version, "1.2") < 0:
                    if _density != 1.0:
                        return SDFError(f"'density' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, density=_density)

        class End(BaseModel):
            def __init__(self, sdf_version: str | None = None, end: float = 100.0):
                super().__init__(sdf_version)
                self.end = end

            def to_version(self, target_version: str) -> "Scene.Fog.End":
                if self.end is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'end' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["end"] = self.end
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("end")
                if self.end is not None:
                    el.text = str(self.end)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Fog.End | SDFError":
                _text = el.text or 100.0
                _end = _parse_double(_text)
                if isinstance(_end, SDFError):
                    return _end
                if _end is not None and cmp_version(version, "1.2") < 0:
                    if _end != 100.0:
                        return SDFError(f"'end' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, end=_end)

        class Start(BaseModel):
            def __init__(self, sdf_version: str | None = None, start: float = 1.0):
                super().__init__(sdf_version)
                self.start = start

            def to_version(self, target_version: str) -> "Scene.Fog.Start":
                if self.start is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'start' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["start"] = self.start
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("start")
                if self.start is not None:
                    el.text = str(self.start)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Fog.Start | SDFError":
                _text = el.text or 1.0
                _start = _parse_double(_text)
                if isinstance(_start, SDFError):
                    return _start
                if _start is not None and cmp_version(version, "1.2") < 0:
                    if _start != 1.0:
                        return SDFError(f"'start' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, start=_start)

        class Type(BaseModel):
            def __init__(self, sdf_version: str | None = None, type: str = "none"):
                super().__init__(sdf_version)
                self.type = type

            def to_version(self, target_version: str) -> "Scene.Fog.Type":
                if self.type is not None and cmp_version(target_version, "1.2") < 0:
                    raise ValueError(f"'type' is not supported in SDF version {target_version} (added in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["type"] = self.type
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("type")
                if self.type is not None:
                    el.text = self.type
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Fog.Type | SDFError":
                _text = el.text or "none"
                _type = _text
                if isinstance(_type, SDFError):
                    return _type
                if _type is not None and cmp_version(version, "1.2") < 0:
                    if _type != "none":
                        return SDFError(f"'type' is not supported in SDF version {version} (added in 1.2)")
                return cls(sdf_version=version, type=_type)

        def __init__(
            self,
            sdf_version: str | None = None,
            color: "Scene.Fog.Color" = None,
            density: float = 1.0,
            end: float = 100.0,
            rgba: _SDFColor = None,
            start: float = 1.0,
            type: str = "linear"
        ):
            super().__init__(sdf_version)
            if rgba is None:
                rgba = _SDFColor.from_sdf("1 1 1 1", version=sdf_version)
            self.color = color
            self.density = density
            self.end = end
            self.rgba = rgba
            self.start = start
            self.type = type
            if self.color is not None:
                if getattr(self.color, '__version__', None) is None:
                    self.color.__version__ = self.__version__
                elif getattr(self.color, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.color = self.color.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Scene.Fog":
            if self.color is not None and cmp_version(target_version, "1.2") < 0:
                raise ValueError(f"'color' is not supported in SDF version {target_version} (added in 1.2)")
            if self.density is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'density' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.end is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'end' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.start is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'start' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.type is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'type' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["color"] = self.color.to_version(target_version) if self.color is not None else None
            kwargs["density"] = self.density
            kwargs["end"] = self.end
            kwargs["rgba"] = self.rgba
            kwargs["start"] = self.start
            kwargs["type"] = self.type
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("fog")
            if self.color is not None:
                el.append(self.color.to_sdf(version))
            if self.density is not None:
                el.set("density", str(self.density))
            if self.end is not None:
                el.set("end", str(self.end))
            if self.rgba is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("color")
                    _c_tmp.text = self.rgba.to_sdf(version)
                    el.append(_c_tmp)
                else:
                    el.set("rgba", self.rgba.to_sdf(version))
            if self.start is not None:
                el.set("start", str(self.start))
            if self.type is not None:
                el.set("type", self.type)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Fog | SDFError":
            _c_color = el.find("color")
            if _c_color is not None:
                _res = cls.Color._from_sdf(_c_color, version)
                if isinstance(_res, SDFError):
                    return _res.extend("color")
                _color = _res
            else:
                _color = None
            if _color is not None and cmp_version(version, "1.2") < 0:
                return SDFError(f"'color' is not supported in SDF version {version} (added in 1.2)")
            _density = _parse_double(el.get("density", 1.0))
            if isinstance(_density, SDFError):
                return _density.extend("@density")
            _end = _parse_double(el.get("end", 100.0))
            if isinstance(_end, SDFError):
                return _end.extend("@end")
            _raw_rgba = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("color")
                if _c_tmp is not None: _raw_rgba = _c_tmp.text
            else:
                _raw_rgba = el.get("rgba")
            if _raw_rgba is None: _raw_rgba = "1 1 1 1"
            _rgba = _SDFColor._from_sdf(_raw_rgba, version)
            if isinstance(_rgba, SDFError):
                return _rgba.extend("@rgba")
            _start = _parse_double(el.get("start", 1.0))
            if isinstance(_start, SDFError):
                return _start.extend("@start")
            _type = el.get("type", "linear")
            if isinstance(_type, SDFError):
                return _type.extend("@type")
            return cls(sdf_version=version, color=_color, density=_density, end=_end, rgba=_rgba, start=_start, type=_type)

    class Grid(BaseModel):
        def __init__(self, sdf_version: str | None = None, enabled: bool = True, grid: bool = True):
            super().__init__(sdf_version)
            self.enabled = enabled
            self.grid = grid

        def to_version(self, target_version: str) -> "Scene.Grid":
            if self.enabled is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'enabled' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["enabled"] = self.enabled
            kwargs["grid"] = self.grid
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("grid")
            if self.enabled is not None:
                el.set("enabled", str(self.enabled).lower())
            if self.grid is not None:
                el.text = str(self.grid).lower()
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Grid | SDFError":
            _enabled = str(el.get("enabled", True)).strip().lower() == 'true'
            if isinstance(_enabled, SDFError):
                return _enabled.extend("@enabled")
            _text = el.text or True
            _grid = str(_text).strip().lower() == 'true'
            if isinstance(_grid, SDFError):
                return _grid
            return cls(sdf_version=version, enabled=_enabled, grid=_grid)

    class OriginVisual(BaseModel):
        def __init__(self, sdf_version: str | None = None, origin_visual: bool = True):
            super().__init__(sdf_version)
            self.origin_visual = origin_visual

        def to_version(self, target_version: str) -> "Scene.OriginVisual":
            if self.origin_visual is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'origin_visual' is not supported in SDF version {target_version} (added in 1.5)")
            kwargs = {"sdf_version": target_version}
            kwargs["origin_visual"] = self.origin_visual
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("origin_visual")
            if self.origin_visual is not None:
                el.text = str(self.origin_visual).lower()
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.OriginVisual | SDFError":
            _text = el.text or True
            _origin_visual = str(_text).strip().lower() == 'true'
            if isinstance(_origin_visual, SDFError):
                return _origin_visual
            if _origin_visual is not None and cmp_version(version, "1.5") < 0:
                if _origin_visual != True:
                    return SDFError(f"'origin_visual' is not supported in SDF version {version} (added in 1.5)")
            return cls(sdf_version=version, origin_visual=_origin_visual)

    class SceneSky(BaseModel):
        class Clouds(BaseModel):
            class CloudsAmbient(BaseModel):
                def __init__(self, sdf_version: str | None = None, ambient: _SDFColor = None):
                    super().__init__(sdf_version)
                    if ambient is None:
                        ambient = _SDFColor.from_sdf(".8 .8 .8 1", version=sdf_version)
                    self.ambient = ambient

                def to_version(self, target_version: str) -> "Scene.SceneSky.Clouds.CloudsAmbient":
                    kwargs = {"sdf_version": target_version}
                    kwargs["ambient"] = self.ambient
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("ambient")
                    if self.ambient is not None:
                        el.text = self.ambient.to_sdf(version)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Clouds.CloudsAmbient | SDFError":
                    _text = el.text or ".8 .8 .8 1"
                    _ambient = _SDFColor._from_sdf(_text, version)
                    if isinstance(_ambient, SDFError):
                        return _ambient
                    return cls(sdf_version=version, ambient=_ambient)

            class Direction(BaseModel):
                def __init__(self, sdf_version: str | None = None, direction: float = 0.0):
                    super().__init__(sdf_version)
                    self.direction = direction

                def to_version(self, target_version: str) -> "Scene.SceneSky.Clouds.Direction":
                    kwargs = {"sdf_version": target_version}
                    kwargs["direction"] = self.direction
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("direction")
                    if self.direction is not None:
                        el.text = str(self.direction)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Clouds.Direction | SDFError":
                    _text = el.text or 0.0
                    _direction = _parse_double(_text)
                    if isinstance(_direction, SDFError):
                        return _direction
                    return cls(sdf_version=version, direction=_direction)

            class Humidity(BaseModel):
                def __init__(self, sdf_version: str | None = None, humidity: float = 0.5):
                    super().__init__(sdf_version)
                    self.humidity = humidity

                def to_version(self, target_version: str) -> "Scene.SceneSky.Clouds.Humidity":
                    kwargs = {"sdf_version": target_version}
                    kwargs["humidity"] = self.humidity
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("humidity")
                    if self.humidity is not None:
                        el.text = str(self.humidity)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Clouds.Humidity | SDFError":
                    _text = el.text or 0.5
                    _humidity = _parse_double(_text)
                    if isinstance(_humidity, SDFError):
                        return _humidity
                    return cls(sdf_version=version, humidity=_humidity)

            class MeanSize(BaseModel):
                def __init__(self, sdf_version: str | None = None, mean_size: float = 0.5):
                    super().__init__(sdf_version)
                    self.mean_size = mean_size

                def to_version(self, target_version: str) -> "Scene.SceneSky.Clouds.MeanSize":
                    kwargs = {"sdf_version": target_version}
                    kwargs["mean_size"] = self.mean_size
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("mean_size")
                    if self.mean_size is not None:
                        el.text = str(self.mean_size)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Clouds.MeanSize | SDFError":
                    _text = el.text or 0.5
                    _mean_size = _parse_double(_text)
                    if isinstance(_mean_size, SDFError):
                        return _mean_size
                    return cls(sdf_version=version, mean_size=_mean_size)

            class Speed(BaseModel):
                def __init__(self, sdf_version: str | None = None, speed: float = 0.6):
                    super().__init__(sdf_version)
                    self.speed = speed

                def to_version(self, target_version: str) -> "Scene.SceneSky.Clouds.Speed":
                    kwargs = {"sdf_version": target_version}
                    kwargs["speed"] = self.speed
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("speed")
                    if self.speed is not None:
                        el.text = str(self.speed)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Clouds.Speed | SDFError":
                    _text = el.text or 0.6
                    _speed = _parse_double(_text)
                    if isinstance(_speed, SDFError):
                        return _speed
                    return cls(sdf_version=version, speed=_speed)

            def __init__(
                self,
                sdf_version: str | None = None,
                ambient: "Scene.SceneSky.Clouds.CloudsAmbient" = None,
                direction: "Scene.SceneSky.Clouds.Direction" = None,
                humidity: "Scene.SceneSky.Clouds.Humidity" = None,
                mean_size: "Scene.SceneSky.Clouds.MeanSize" = None,
                speed: "Scene.SceneSky.Clouds.Speed" = None
            ):
                super().__init__(sdf_version)
                self.ambient = ambient
                self.direction = direction
                self.humidity = humidity
                self.mean_size = mean_size
                self.speed = speed
                if self.ambient is not None:
                    if getattr(self.ambient, '__version__', None) is None:
                        self.ambient.__version__ = self.__version__
                    elif getattr(self.ambient, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.ambient = self.ambient.to_version(self.__version__)
                if self.direction is not None:
                    if getattr(self.direction, '__version__', None) is None:
                        self.direction.__version__ = self.__version__
                    elif getattr(self.direction, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.direction = self.direction.to_version(self.__version__)
                if self.humidity is not None:
                    if getattr(self.humidity, '__version__', None) is None:
                        self.humidity.__version__ = self.__version__
                    elif getattr(self.humidity, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.humidity = self.humidity.to_version(self.__version__)
                if self.mean_size is not None:
                    if getattr(self.mean_size, '__version__', None) is None:
                        self.mean_size.__version__ = self.__version__
                    elif getattr(self.mean_size, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.mean_size = self.mean_size.to_version(self.__version__)
                if self.speed is not None:
                    if getattr(self.speed, '__version__', None) is None:
                        self.speed.__version__ = self.__version__
                    elif getattr(self.speed, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.speed = self.speed.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Scene.SceneSky.Clouds":
                kwargs = {"sdf_version": target_version}
                kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
                kwargs["direction"] = self.direction.to_version(target_version) if self.direction is not None else None
                kwargs["humidity"] = self.humidity.to_version(target_version) if self.humidity is not None else None
                kwargs["mean_size"] = self.mean_size.to_version(target_version) if self.mean_size is not None else None
                kwargs["speed"] = self.speed.to_version(target_version) if self.speed is not None else None
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("clouds")
                if self.ambient is not None:
                    el.append(self.ambient.to_sdf(version))
                if self.direction is not None:
                    el.append(self.direction.to_sdf(version))
                if self.humidity is not None:
                    el.append(self.humidity.to_sdf(version))
                if self.mean_size is not None:
                    el.append(self.mean_size.to_sdf(version))
                if self.speed is not None:
                    el.append(self.speed.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Clouds | SDFError":
                _c_ambient = el.find("ambient")
                if _c_ambient is not None:
                    _res = cls.CloudsAmbient._from_sdf(_c_ambient, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("ambient")
                    _ambient = _res
                else:
                    _ambient = None
                _c_direction = el.find("direction")
                if _c_direction is not None:
                    _res = cls.Direction._from_sdf(_c_direction, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("direction")
                    _direction = _res
                else:
                    _direction = None
                _c_humidity = el.find("humidity")
                if _c_humidity is not None:
                    _res = cls.Humidity._from_sdf(_c_humidity, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("humidity")
                    _humidity = _res
                else:
                    _humidity = None
                _c_mean_size = el.find("mean_size")
                if _c_mean_size is not None:
                    _res = cls.MeanSize._from_sdf(_c_mean_size, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("mean_size")
                    _mean_size = _res
                else:
                    _mean_size = None
                _c_speed = el.find("speed")
                if _c_speed is not None:
                    _res = cls.Speed._from_sdf(_c_speed, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("speed")
                    _speed = _res
                else:
                    _speed = None
                return cls(sdf_version=version, ambient=_ambient, direction=_direction, humidity=_humidity, mean_size=_mean_size, speed=_speed)

        class CubemapUri(BaseModel):
            def __init__(self, sdf_version: str | None = None, cubemap_uri: str = ""):
                super().__init__(sdf_version)
                self.cubemap_uri = cubemap_uri

            def to_version(self, target_version: str) -> "Scene.SceneSky.CubemapUri":
                if self.cubemap_uri is not None and cmp_version(target_version, "1.9") < 0:
                    raise ValueError(f"'cubemap_uri' is not supported in SDF version {target_version} (added in 1.9)")
                kwargs = {"sdf_version": target_version}
                kwargs["cubemap_uri"] = self.cubemap_uri
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("cubemap_uri")
                if self.cubemap_uri is not None:
                    el.text = self.cubemap_uri
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.CubemapUri | SDFError":
                _text = el.text or ""
                _cubemap_uri = _text
                if isinstance(_cubemap_uri, SDFError):
                    return _cubemap_uri
                if _cubemap_uri is not None and cmp_version(version, "1.9") < 0:
                    if _cubemap_uri != "":
                        return SDFError(f"'cubemap_uri' is not supported in SDF version {version} (added in 1.9)")
                return cls(sdf_version=version, cubemap_uri=_cubemap_uri)

        class Sunrise(BaseModel):
            def __init__(self, sdf_version: str | None = None, sunrise: float = 6.0):
                super().__init__(sdf_version)
                self.sunrise = sunrise

            def to_version(self, target_version: str) -> "Scene.SceneSky.Sunrise":
                kwargs = {"sdf_version": target_version}
                kwargs["sunrise"] = self.sunrise
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("sunrise")
                if self.sunrise is not None:
                    el.text = str(self.sunrise)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Sunrise | SDFError":
                _text = el.text or 6.0
                _sunrise = _parse_double(_text)
                if isinstance(_sunrise, SDFError):
                    return _sunrise
                return cls(sdf_version=version, sunrise=_sunrise)

        class Sunset(BaseModel):
            def __init__(self, sdf_version: str | None = None, sunset: float = 20.0):
                super().__init__(sdf_version)
                self.sunset = sunset

            def to_version(self, target_version: str) -> "Scene.SceneSky.Sunset":
                kwargs = {"sdf_version": target_version}
                kwargs["sunset"] = self.sunset
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("sunset")
                if self.sunset is not None:
                    el.text = str(self.sunset)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Sunset | SDFError":
                _text = el.text or 20.0
                _sunset = _parse_double(_text)
                if isinstance(_sunset, SDFError):
                    return _sunset
                return cls(sdf_version=version, sunset=_sunset)

        class Time(BaseModel):
            def __init__(self, sdf_version: str | None = None, time: float = 10.0):
                super().__init__(sdf_version)
                self.time = time

            def to_version(self, target_version: str) -> "Scene.SceneSky.Time":
                kwargs = {"sdf_version": target_version}
                kwargs["time"] = self.time
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("time")
                if self.time is not None:
                    el.text = str(self.time)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Time | SDFError":
                _text = el.text or 10.0
                _time = _parse_double(_text)
                if isinstance(_time, SDFError):
                    return _time
                return cls(sdf_version=version, time=_time)

        def __init__(
            self,
            sdf_version: str | None = None,
            clouds: "Scene.SceneSky.Clouds" = None,
            cubemap_uri: "Scene.SceneSky.CubemapUri" = None,
            sunrise: "Scene.SceneSky.Sunrise" = None,
            sunset: "Scene.SceneSky.Sunset" = None,
            time: "Scene.SceneSky.Time" = None
        ):
            super().__init__(sdf_version)
            self.clouds = clouds
            self.cubemap_uri = cubemap_uri
            self.sunrise = sunrise
            self.sunset = sunset
            self.time = time
            if self.clouds is not None:
                if getattr(self.clouds, '__version__', None) is None:
                    self.clouds.__version__ = self.__version__
                elif getattr(self.clouds, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.clouds = self.clouds.to_version(self.__version__)
            if self.cubemap_uri is not None:
                if getattr(self.cubemap_uri, '__version__', None) is None:
                    self.cubemap_uri.__version__ = self.__version__
                elif getattr(self.cubemap_uri, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.cubemap_uri = self.cubemap_uri.to_version(self.__version__)
            if self.sunrise is not None:
                if getattr(self.sunrise, '__version__', None) is None:
                    self.sunrise.__version__ = self.__version__
                elif getattr(self.sunrise, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.sunrise = self.sunrise.to_version(self.__version__)
            if self.sunset is not None:
                if getattr(self.sunset, '__version__', None) is None:
                    self.sunset.__version__ = self.__version__
                elif getattr(self.sunset, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.sunset = self.sunset.to_version(self.__version__)
            if self.time is not None:
                if getattr(self.time, '__version__', None) is None:
                    self.time.__version__ = self.__version__
                elif getattr(self.time, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.time = self.time.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Scene.SceneSky":
            if self.cubemap_uri is not None and cmp_version(target_version, "1.9") < 0:
                raise ValueError(f"'cubemap_uri' is not supported in SDF version {target_version} (added in 1.9)")
            kwargs = {"sdf_version": target_version}
            kwargs["clouds"] = self.clouds.to_version(target_version) if self.clouds is not None else None
            kwargs["cubemap_uri"] = self.cubemap_uri.to_version(target_version) if self.cubemap_uri is not None else None
            kwargs["sunrise"] = self.sunrise.to_version(target_version) if self.sunrise is not None else None
            kwargs["sunset"] = self.sunset.to_version(target_version) if self.sunset is not None else None
            kwargs["time"] = self.time.to_version(target_version) if self.time is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("sky")
            if self.clouds is not None:
                el.append(self.clouds.to_sdf(version))
            if self.cubemap_uri is not None:
                el.append(self.cubemap_uri.to_sdf(version))
            if self.sunrise is not None:
                el.append(self.sunrise.to_sdf(version))
            if self.sunset is not None:
                el.append(self.sunset.to_sdf(version))
            if self.time is not None:
                el.append(self.time.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky | SDFError":
            _c_clouds = el.find("clouds")
            if _c_clouds is not None:
                _res = cls.Clouds._from_sdf(_c_clouds, version)
                if isinstance(_res, SDFError):
                    return _res.extend("clouds")
                _clouds = _res
            else:
                _clouds = None
            _c_cubemap_uri = el.find("cubemap_uri")
            if _c_cubemap_uri is not None:
                _res = cls.CubemapUri._from_sdf(_c_cubemap_uri, version)
                if isinstance(_res, SDFError):
                    return _res.extend("cubemap_uri")
                _cubemap_uri = _res
            else:
                _cubemap_uri = None
            if _cubemap_uri is not None and cmp_version(version, "1.9") < 0:
                return SDFError(f"'cubemap_uri' is not supported in SDF version {version} (added in 1.9)")
            _c_sunrise = el.find("sunrise")
            if _c_sunrise is not None:
                _res = cls.Sunrise._from_sdf(_c_sunrise, version)
                if isinstance(_res, SDFError):
                    return _res.extend("sunrise")
                _sunrise = _res
            else:
                _sunrise = None
            _c_sunset = el.find("sunset")
            if _c_sunset is not None:
                _res = cls.Sunset._from_sdf(_c_sunset, version)
                if isinstance(_res, SDFError):
                    return _res.extend("sunset")
                _sunset = _res
            else:
                _sunset = None
            _c_time = el.find("time")
            if _c_time is not None:
                _res = cls.Time._from_sdf(_c_time, version)
                if isinstance(_res, SDFError):
                    return _res.extend("time")
                _time = _res
            else:
                _time = None
            return cls(sdf_version=version, clouds=_clouds, cubemap_uri=_cubemap_uri, sunrise=_sunrise, sunset=_sunset, time=_time)

    class Shadows(BaseModel):
        def __init__(self, sdf_version: str | None = None, enabled: bool = True, shadows: bool = True):
            super().__init__(sdf_version)
            self.enabled = enabled
            self.shadows = shadows

        def to_version(self, target_version: str) -> "Scene.Shadows":
            if self.enabled is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'enabled' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["enabled"] = self.enabled
            kwargs["shadows"] = self.shadows
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("shadows")
            if self.enabled is not None:
                el.set("enabled", str(self.enabled).lower())
            if self.shadows is not None:
                el.text = str(self.shadows).lower()
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Shadows | SDFError":
            _enabled = str(el.get("enabled", True)).strip().lower() == 'true'
            if isinstance(_enabled, SDFError):
                return _enabled.extend("@enabled")
            _text = el.text or True
            _shadows = str(_text).strip().lower() == 'true'
            if isinstance(_shadows, SDFError):
                return _shadows
            return cls(sdf_version=version, enabled=_enabled, shadows=_shadows)

    def __init__(
        self,
        sdf_version: str | None = None,
        ambient: "Scene.Ambient" = None,
        background: "Scene.Background" = None,
        fog: "Scene.Fog" = None,
        grid: "Scene.Grid" = None,
        origin_visual: "Scene.OriginVisual" = None,
        shadows: "Scene.Shadows" = None,
        sky: "Scene.SceneSky" = None
    ):
        super().__init__(sdf_version)
        self.ambient = ambient
        self.background = background
        self.fog = fog
        self.grid = grid
        self.origin_visual = origin_visual
        self.shadows = shadows
        self.sky = sky
        if self.ambient is not None:
            if getattr(self.ambient, '__version__', None) is None:
                self.ambient.__version__ = self.__version__
            elif getattr(self.ambient, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.ambient = self.ambient.to_version(self.__version__)
        if self.background is not None:
            if getattr(self.background, '__version__', None) is None:
                self.background.__version__ = self.__version__
            elif getattr(self.background, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.background = self.background.to_version(self.__version__)
        if self.fog is not None:
            if getattr(self.fog, '__version__', None) is None:
                self.fog.__version__ = self.__version__
            elif getattr(self.fog, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.fog = self.fog.to_version(self.__version__)
        if self.grid is not None:
            if getattr(self.grid, '__version__', None) is None:
                self.grid.__version__ = self.__version__
            elif getattr(self.grid, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.grid = self.grid.to_version(self.__version__)
        if self.origin_visual is not None:
            if getattr(self.origin_visual, '__version__', None) is None:
                self.origin_visual.__version__ = self.__version__
            elif getattr(self.origin_visual, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.origin_visual = self.origin_visual.to_version(self.__version__)
        if self.shadows is not None:
            if getattr(self.shadows, '__version__', None) is None:
                self.shadows.__version__ = self.__version__
            elif getattr(self.shadows, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.shadows = self.shadows.to_version(self.__version__)
        if self.sky is not None:
            if getattr(self.sky, '__version__', None) is None:
                self.sky.__version__ = self.__version__
            elif getattr(self.sky, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.sky = self.sky.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Scene":
        if self.origin_visual is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'origin_visual' is not supported in SDF version {target_version} (added in 1.5)")
        if self.sky is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'sky' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
        kwargs["background"] = self.background.to_version(target_version) if self.background is not None else None
        kwargs["fog"] = self.fog.to_version(target_version) if self.fog is not None else None
        kwargs["grid"] = self.grid.to_version(target_version) if self.grid is not None else None
        kwargs["origin_visual"] = self.origin_visual.to_version(target_version) if self.origin_visual is not None else None
        kwargs["shadows"] = self.shadows.to_version(target_version) if self.shadows is not None else None
        kwargs["sky"] = self.sky.to_version(target_version) if self.sky is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("scene")
        if self.ambient is not None:
            el.append(self.ambient.to_sdf(version))
        if self.background is not None:
            el.append(self.background.to_sdf(version))
        if self.fog is not None:
            el.append(self.fog.to_sdf(version))
        if self.grid is not None:
            el.append(self.grid.to_sdf(version))
        if self.origin_visual is not None:
            el.append(self.origin_visual.to_sdf(version))
        if self.shadows is not None:
            el.append(self.shadows.to_sdf(version))
        if self.sky is not None:
            el.append(self.sky.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Scene | SDFError":
        _c_ambient = el.find("ambient")
        if _c_ambient is not None:
            _res = cls.Ambient._from_sdf(_c_ambient, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient")
            _ambient = _res
        else:
            _ambient = None
        _c_background = el.find("background")
        if _c_background is not None:
            _res = cls.Background._from_sdf(_c_background, version)
            if isinstance(_res, SDFError):
                return _res.extend("background")
            _background = _res
        else:
            _background = None
        _c_fog = el.find("fog")
        if _c_fog is not None:
            _res = cls.Fog._from_sdf(_c_fog, version)
            if isinstance(_res, SDFError):
                return _res.extend("fog")
            _fog = _res
        else:
            _fog = None
        _c_grid = el.find("grid")
        if _c_grid is not None:
            _res = cls.Grid._from_sdf(_c_grid, version)
            if isinstance(_res, SDFError):
                return _res.extend("grid")
            _grid = _res
        else:
            _grid = None
        _c_origin_visual = el.find("origin_visual")
        if _c_origin_visual is not None:
            _res = cls.OriginVisual._from_sdf(_c_origin_visual, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin_visual")
            _origin_visual = _res
        else:
            _origin_visual = None
        if _origin_visual is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'origin_visual' is not supported in SDF version {version} (added in 1.5)")
        _c_shadows = el.find("shadows")
        if _c_shadows is not None:
            _res = cls.Shadows._from_sdf(_c_shadows, version)
            if isinstance(_res, SDFError):
                return _res.extend("shadows")
            _shadows = _res
        else:
            _shadows = None
        _c_sky = el.find("sky")
        if _c_sky is not None:
            _res = cls.SceneSky._from_sdf(_c_sky, version)
            if isinstance(_res, SDFError):
                return _res.extend("sky")
            _sky = _res
        else:
            _sky = None
        if _sky is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'sky' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, ambient=_ambient, background=_background, fog=_fog, grid=_grid, origin_visual=_origin_visual, shadows=_shadows, sky=_sky)
