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
                if cmp_version(version, "1.2") >= 0:
                    el.text = self.rgba.to_sdf(version)
                else:
                    el.set("rgba", self.rgba.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Ambient | SDFError":
            _text = el.text or "0.0 0.0 0.0 1.0"
            _ambient = _SDFColor._from_sdf(_text, version)
            if isinstance(_ambient, SDFError):
                return _ambient
            _raw_rgba = None
            if cmp_version(version, "1.2") >= 0:
                _raw_rgba = el.text
            else:
                _raw_rgba = el.get("rgba")
            if _raw_rgba is None: _raw_rgba = "0.0 0.0 0.0 1.0"
            _rgba = _SDFColor._from_sdf(_raw_rgba, version)
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
            if self.sky is not None and hasattr(self.sky, 'to_version'):
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
            kwargs["sky"] = self.sky.to_version(target_version) if hasattr(self.sky, "to_version") else self.sky
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
                if cmp_version(version, "1.2") >= 0:
                    el.text = self.rgba.to_sdf(version)
                else:
                    el.set("rgba", self.rgba.to_sdf(version))
            if self.sky is not None:
                if hasattr(self.sky, 'to_sdf'):
                    _child_res = self.sky.to_sdf(version)
                else:
                    _child_res = str(self.sky)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('sky')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Background | SDFError":
            _raw_rgba = None
            if cmp_version(version, "1.2") >= 0:
                _raw_rgba = el.text
            else:
                _raw_rgba = el.get("rgba")
            if _raw_rgba is None: _raw_rgba = ".7 .7 .7 1"
            _rgba = _SDFColor._from_sdf(_raw_rgba, version)
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
        def __init__(
            self,
            sdf_version: str | None = None,
            color: _SDFColor = None,
            density: float = 1.0,
            end: float = 100.0,
            rgba: _SDFColor = None,
            start: float = 1.0,
            type: str = "linear"
        ):
            super().__init__(sdf_version)
            if color is None:
                color = _SDFColor.from_sdf("1 1 1 1", version=sdf_version)
            if rgba is None:
                rgba = _SDFColor.from_sdf("1 1 1 1", version=sdf_version)
            self.color = color
            self.density = density
            self.end = end
            self.rgba = rgba
            self.start = start
            self.type = type

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
            kwargs["color"] = self.color
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
                _c_tmp = ET.Element("color")
                _c_tmp.text = self.color.to_sdf(version)
                el.append(_c_tmp)
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
            _c_tmp = el.find("color")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1 1"
                _val = _SDFColor._from_sdf(_text, version)
                if isinstance(_val, SDFError):
                    return _val.extend("color")
                _color = _val
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
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.enabled).lower()
                else:
                    el.set("enabled", str(self.enabled).lower())
            if self.grid is not None:
                el.text = str(self.grid).lower()
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Grid | SDFError":
            _raw_enabled = None
            if cmp_version(version, "1.2") >= 0:
                _raw_enabled = el.text
            else:
                _raw_enabled = el.get("enabled")
            if _raw_enabled is None: _raw_enabled = True
            _enabled = str(_raw_enabled).strip().lower() == 'true'
            if isinstance(_enabled, SDFError):
                return _enabled.extend("@enabled")
            _text = el.text or True
            _grid = str(_text).strip().lower() == 'true'
            if isinstance(_grid, SDFError):
                return _grid
            return cls(sdf_version=version, enabled=_enabled, grid=_grid)

    class SceneSky(BaseModel):
        class Clouds(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                ambient: _SDFColor = None,
                direction: float = 0.0,
                humidity: float = 0.5,
                mean_size: float = 0.5,
                speed: float = 0.6
            ):
                super().__init__(sdf_version)
                if ambient is None:
                    ambient = _SDFColor.from_sdf(".8 .8 .8 1", version=sdf_version)
                self.ambient = ambient
                self.direction = direction
                self.humidity = humidity
                self.mean_size = mean_size
                self.speed = speed

            def to_version(self, target_version: str) -> "Scene.SceneSky.Clouds":
                kwargs = {"sdf_version": target_version}
                kwargs["ambient"] = self.ambient
                kwargs["direction"] = self.direction
                kwargs["humidity"] = self.humidity
                kwargs["mean_size"] = self.mean_size
                kwargs["speed"] = self.speed
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
                    _c_tmp = ET.Element("ambient")
                    _c_tmp.text = self.ambient.to_sdf(version)
                    el.append(_c_tmp)
                if self.direction is not None:
                    _c_tmp = ET.Element("direction")
                    _c_tmp.text = str(self.direction)
                    el.append(_c_tmp)
                if self.humidity is not None:
                    _c_tmp = ET.Element("humidity")
                    _c_tmp.text = str(self.humidity)
                    el.append(_c_tmp)
                if self.mean_size is not None:
                    _c_tmp = ET.Element("mean_size")
                    _c_tmp.text = str(self.mean_size)
                    el.append(_c_tmp)
                if self.speed is not None:
                    _c_tmp = ET.Element("speed")
                    _c_tmp.text = str(self.speed)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.SceneSky.Clouds | SDFError":
                _c_tmp = el.find("ambient")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else ".8 .8 .8 1"
                    _val = _SDFColor._from_sdf(_text, version)
                    if isinstance(_val, SDFError):
                        return _val.extend("ambient")
                    _ambient = _val
                else:
                    _ambient = None
                _c_tmp = el.find("direction")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("direction")
                    _direction = _val
                else:
                    _direction = None
                _c_tmp = el.find("humidity")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.5
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("humidity")
                    _humidity = _val
                else:
                    _humidity = None
                _c_tmp = el.find("mean_size")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.5
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("mean_size")
                    _mean_size = _val
                else:
                    _mean_size = None
                _c_tmp = el.find("speed")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.6
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("speed")
                    _speed = _val
                else:
                    _speed = None
                return cls(sdf_version=version, ambient=_ambient, direction=_direction, humidity=_humidity, mean_size=_mean_size, speed=_speed)

        def __init__(
            self,
            sdf_version: str | None = None,
            clouds: "Scene.SceneSky.Clouds" = None,
            cubemap_uri: str = "",
            sunrise: float = 6.0,
            sunset: float = 20.0,
            time: float = 10.0
        ):
            super().__init__(sdf_version)
            self.clouds = clouds
            self.cubemap_uri = cubemap_uri
            self.sunrise = sunrise
            self.sunset = sunset
            self.time = time
            if self.clouds is not None and hasattr(self.clouds, 'to_version'):
                if getattr(self.clouds, '__version__', None) is None:
                    self.clouds.__version__ = self.__version__
                elif getattr(self.clouds, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.clouds = self.clouds.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Scene.SceneSky":
            if self.cubemap_uri is not None and cmp_version(target_version, "1.9") < 0:
                raise ValueError(f"'cubemap_uri' is not supported in SDF version {target_version} (added in 1.9)")
            kwargs = {"sdf_version": target_version}
            kwargs["clouds"] = self.clouds.to_version(target_version) if hasattr(self.clouds, "to_version") else self.clouds
            kwargs["cubemap_uri"] = self.cubemap_uri
            kwargs["sunrise"] = self.sunrise
            kwargs["sunset"] = self.sunset
            kwargs["time"] = self.time
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
                if hasattr(self.clouds, 'to_sdf'):
                    _child_res = self.clouds.to_sdf(version)
                else:
                    _child_res = str(self.clouds)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('clouds')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.cubemap_uri is not None:
                _c_tmp = ET.Element("cubemap_uri")
                _c_tmp.text = self.cubemap_uri
                el.append(_c_tmp)
            if self.sunrise is not None:
                _c_tmp = ET.Element("sunrise")
                _c_tmp.text = str(self.sunrise)
                el.append(_c_tmp)
            if self.sunset is not None:
                _c_tmp = ET.Element("sunset")
                _c_tmp.text = str(self.sunset)
                el.append(_c_tmp)
            if self.time is not None:
                _c_tmp = ET.Element("time")
                _c_tmp.text = str(self.time)
                el.append(_c_tmp)
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
            _c_tmp = el.find("cubemap_uri")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else ""
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("cubemap_uri")
                _cubemap_uri = _val
            else:
                _cubemap_uri = None
            if _cubemap_uri is not None and cmp_version(version, "1.9") < 0:
                return SDFError(f"'cubemap_uri' is not supported in SDF version {version} (added in 1.9)")
            _c_tmp = el.find("sunrise")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 6.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("sunrise")
                _sunrise = _val
            else:
                _sunrise = None
            _c_tmp = el.find("sunset")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 20.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("sunset")
                _sunset = _val
            else:
                _sunset = None
            _c_tmp = el.find("time")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 10.0
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("time")
                _time = _val
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
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.enabled).lower()
                else:
                    el.set("enabled", str(self.enabled).lower())
            if self.shadows is not None:
                el.text = str(self.shadows).lower()
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Shadows | SDFError":
            _raw_enabled = None
            if cmp_version(version, "1.2") >= 0:
                _raw_enabled = el.text
            else:
                _raw_enabled = el.get("enabled")
            if _raw_enabled is None: _raw_enabled = True
            _enabled = str(_raw_enabled).strip().lower() == 'true'
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
        origin_visual: bool = True,
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
        if self.ambient is not None and hasattr(self.ambient, 'to_version'):
            if getattr(self.ambient, '__version__', None) is None:
                self.ambient.__version__ = self.__version__
            elif getattr(self.ambient, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.ambient = self.ambient.to_version(self.__version__)
        if self.background is not None and hasattr(self.background, 'to_version'):
            if getattr(self.background, '__version__', None) is None:
                self.background.__version__ = self.__version__
            elif getattr(self.background, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.background = self.background.to_version(self.__version__)
        if self.fog is not None and hasattr(self.fog, 'to_version'):
            if getattr(self.fog, '__version__', None) is None:
                self.fog.__version__ = self.__version__
            elif getattr(self.fog, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.fog = self.fog.to_version(self.__version__)
        if self.grid is not None and hasattr(self.grid, 'to_version'):
            if getattr(self.grid, '__version__', None) is None:
                self.grid.__version__ = self.__version__
            elif getattr(self.grid, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.grid = self.grid.to_version(self.__version__)
        if self.shadows is not None and hasattr(self.shadows, 'to_version'):
            if getattr(self.shadows, '__version__', None) is None:
                self.shadows.__version__ = self.__version__
            elif getattr(self.shadows, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.shadows = self.shadows.to_version(self.__version__)
        if self.sky is not None and hasattr(self.sky, 'to_version'):
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
        kwargs["ambient"] = self.ambient.to_version(target_version) if hasattr(self.ambient, "to_version") else self.ambient
        kwargs["background"] = self.background.to_version(target_version) if hasattr(self.background, "to_version") else self.background
        kwargs["fog"] = self.fog.to_version(target_version) if hasattr(self.fog, "to_version") else self.fog
        kwargs["grid"] = self.grid.to_version(target_version) if hasattr(self.grid, "to_version") else self.grid
        kwargs["origin_visual"] = self.origin_visual
        kwargs["shadows"] = self.shadows.to_version(target_version) if hasattr(self.shadows, "to_version") else self.shadows
        kwargs["sky"] = self.sky.to_version(target_version) if hasattr(self.sky, "to_version") else self.sky
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
            if hasattr(self.ambient, 'to_sdf'):
                _child_res = self.ambient.to_sdf(version)
            else:
                _child_res = str(self.ambient)
            if isinstance(_child_res, str):
                _item_el = ET.Element('ambient')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.background is not None:
            if hasattr(self.background, 'to_sdf'):
                _child_res = self.background.to_sdf(version)
            else:
                _child_res = str(self.background)
            if isinstance(_child_res, str):
                _item_el = ET.Element('background')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.fog is not None:
            if hasattr(self.fog, 'to_sdf'):
                _child_res = self.fog.to_sdf(version)
            else:
                _child_res = str(self.fog)
            if isinstance(_child_res, str):
                _item_el = ET.Element('fog')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.grid is not None:
            if hasattr(self.grid, 'to_sdf'):
                _child_res = self.grid.to_sdf(version)
            else:
                _child_res = str(self.grid)
            if isinstance(_child_res, str):
                _item_el = ET.Element('grid')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.origin_visual is not None:
            _c_tmp = ET.Element("origin_visual")
            _c_tmp.text = str(self.origin_visual).lower()
            el.append(_c_tmp)
        if self.shadows is not None:
            if hasattr(self.shadows, 'to_sdf'):
                _child_res = self.shadows.to_sdf(version)
            else:
                _child_res = str(self.shadows)
            if isinstance(_child_res, str):
                _item_el = ET.Element('shadows')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.sky is not None:
            if hasattr(self.sky, 'to_sdf'):
                _child_res = self.sky.to_sdf(version)
            else:
                _child_res = str(self.sky)
            if isinstance(_child_res, str):
                _item_el = ET.Element('sky')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
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
        _c_tmp = el.find("origin_visual")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else True
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("origin_visual")
            _origin_visual = _val
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
