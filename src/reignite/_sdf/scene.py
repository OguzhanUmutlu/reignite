### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import _ColorT, _color
from ..utils.version import cmp_version

def _parse_color(raw: str) -> _ColorT | SDFError:
    try:
        return _color(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Scene(BaseModel):
    class Ambient(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            ambient: _ColorT | None = None,
            rgba: _ColorT | None = None
        ):
            super().__init__(sdf_version)
            self.ambient = _color(ambient) if ambient is not None else None
            self.rgba = _color(rgba) if rgba is not None else None

        def to_version(self, target_version: str) -> "Scene.Ambient":
            kwargs: dict = {"sdf_version": target_version, "ambient": self.ambient, "rgba": self.rgba}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("ambient")
            if self.ambient is not None:
                el.text = str(self.ambient)
            if self.rgba is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.rgba)
                else:
                    el.set("rgba", str(self.rgba))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Ambient | SDFError":
            _raw_ambient = el.text
            if _raw_ambient is not None:
                _ambient = _parse_color(_raw_ambient)
                if isinstance(_ambient, SDFError):
                    return _ambient
            else:
                _ambient = None
            _raw_rgba = None
            if cmp_version(version, "1.2") >= 0:
                _raw_rgba = el.text
            else:
                _raw_rgba = el.get("rgba")
            if _raw_rgba is not None:
                _rgba = _parse_color(_raw_rgba)
                if isinstance(_rgba, SDFError):
                    return _rgba.extend("@rgba")
            else:
                _rgba = None
            return cls(sdf_version=version, ambient=_ambient, rgba=_rgba)

    class Background(BaseModel):
        class Sky(BaseModel):
            def __init__(self, sdf_version: str | None = None, material: str | None = None):
                super().__init__(sdf_version)
                self.material = material

            def to_version(self, target_version: str) -> "Scene.Background.Sky":
                kwargs: dict = {"sdf_version": target_version, "material": self.material}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("sky")
                if self.material is not None:
                    el.set("material", self.material)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Background.Sky | SDFError":
                _raw_material = el.get("material")
                if _raw_material is not None:
                    _material = _raw_material
                    if isinstance(_material, SDFError):
                        return _material.extend("@material")
                else:
                    _material = None
                return cls(sdf_version=version, material=_material)

        def __init__(
            self,
            sdf_version: str | None = None,
            rgba: _ColorT | None = None,
            sky: "Scene.Background.Sky" = None
        ):
            super().__init__(sdf_version)
            self.rgba = _color(rgba) if rgba is not None else None
            self.sky = sky
            if self.sky is not None and hasattr(self.sky, 'to_version'):
                if getattr(self.sky, 'sdfversion', None) is None:
                    self.sky.sdfversion = self.sdfversion
                elif getattr(self.sky, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.sky = self.sky.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Scene.Background":
            if self.sky is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'sky' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs: dict = {"sdf_version": target_version, "rgba": self.rgba, "sky": self.sky.to_version(target_version) if self.sky is not None and hasattr(self.sky, "to_version") else self.sky}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("background")
            if self.rgba is not None:
                if cmp_version(version, "1.2") >= 0:
                    el.text = str(self.rgba)
                else:
                    el.set("rgba", str(self.rgba))
            if self.sky is not None:
                _child_res = self.sky.to_sdf(version)
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
            if _raw_rgba is not None:
                _rgba = _parse_color(_raw_rgba)
                if isinstance(_rgba, SDFError):
                    return _rgba.extend("@rgba")
            else:
                _rgba = None
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
            color: _ColorT | None = None,
            density: float | None = None,
            end: float | None = None,
            rgba: _ColorT | None = None,
            start: float | None = None,
            type: str | None = None
        ):
            super().__init__(sdf_version)
            self.color = _color(color) if color is not None else None
            self.density = density
            self.end = end
            self.rgba = _color(rgba) if rgba is not None else None
            self.start = start
            self.type = type

        def to_version(self, target_version: str) -> "Scene.Fog":
            if self.color is not None and cmp_version(target_version, "1.2") < 0:
                raise ValueError(f"'color' is not supported in SDF version {target_version} (added in 1.2)")
            kwargs: dict = {"sdf_version": target_version, "color": self.color, "density": self.density, "end": self.end, "rgba": self.rgba, "start": self.start, "type": self.type}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("fog")
            if self.color is not None:
                _c_tmp = ET.Element("color")
                _c_tmp.text = str(self.color)
                el.append(_c_tmp)
            if self.density is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("density")
                    _c_tmp.text = str(self.density)
                    el.append(_c_tmp)
                else:
                    el.set("density", str(self.density))
            if self.end is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("end")
                    _c_tmp.text = str(self.end)
                    el.append(_c_tmp)
                else:
                    el.set("end", str(self.end))
            if self.rgba is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("color")
                    _c_tmp.text = str(self.rgba)
                    el.append(_c_tmp)
                else:
                    el.set("rgba", str(self.rgba))
            if self.start is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("start")
                    _c_tmp.text = str(self.start)
                    el.append(_c_tmp)
                else:
                    el.set("start", str(self.start))
            if self.type is not None:
                if cmp_version(version, "1.2") >= 0:
                    _c_tmp = ET.Element("type")
                    _c_tmp.text = self.type
                    el.append(_c_tmp)
                else:
                    el.set("type", self.type)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Scene.Fog | SDFError":
            _c_tmp = el.find("color")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1 1"
                _val = _parse_color(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("color")
                _color = _val
            else:
                _color = None
            if _color is not None and cmp_version(version, "1.2") < 0:
                return SDFError(f"'color' is not supported in SDF version {version} (added in 1.2)")
            _raw_density = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("density")
                if _c_tmp is not None: _raw_density = _c_tmp.text
            else:
                _raw_density = el.get("density")
            if _raw_density is not None:
                _density = _parse_double(_raw_density)
                if isinstance(_density, SDFError):
                    return _density.extend("@density")
            else:
                _density = None
            _raw_end = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("end")
                if _c_tmp is not None: _raw_end = _c_tmp.text
            else:
                _raw_end = el.get("end")
            if _raw_end is not None:
                _end = _parse_double(_raw_end)
                if isinstance(_end, SDFError):
                    return _end.extend("@end")
            else:
                _end = None
            _raw_rgba = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("color")
                if _c_tmp is not None: _raw_rgba = _c_tmp.text
            else:
                _raw_rgba = el.get("rgba")
            if _raw_rgba is not None:
                _rgba = _parse_color(_raw_rgba)
                if isinstance(_rgba, SDFError):
                    return _rgba.extend("@rgba")
            else:
                _rgba = None
            _raw_start = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("start")
                if _c_tmp is not None: _raw_start = _c_tmp.text
            else:
                _raw_start = el.get("start")
            if _raw_start is not None:
                _start = _parse_double(_raw_start)
                if isinstance(_start, SDFError):
                    return _start.extend("@start")
            else:
                _start = None
            _raw_type = None
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = el.find("type")
                if _c_tmp is not None: _raw_type = _c_tmp.text
            else:
                _raw_type = el.get("type")
            if _raw_type is not None:
                _type = _raw_type
                if isinstance(_type, SDFError):
                    return _type.extend("@type")
            else:
                _type = None
            return cls(sdf_version=version, color=_color, density=_density, end=_end, rgba=_rgba, start=_start, type=_type)

    class Grid(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            enabled: bool | None = None,
            grid: bool | None = None
        ):
            super().__init__(sdf_version)
            self.enabled = enabled
            self.grid = grid

        def to_version(self, target_version: str) -> "Scene.Grid":
            kwargs: dict = {"sdf_version": target_version, "enabled": self.enabled, "grid": self.grid}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
            if _raw_enabled is not None:
                _enabled = str(_raw_enabled).strip().lower() == 'true'
                if isinstance(_enabled, SDFError):
                    return _enabled.extend("@enabled")
            else:
                _enabled = None
            _raw_grid = el.text
            if _raw_grid is not None:
                _grid = str(_raw_grid).strip().lower() == 'true'
                if isinstance(_grid, SDFError):
                    return _grid
            else:
                _grid = None
            return cls(sdf_version=version, enabled=_enabled, grid=_grid)

    class SceneSky(BaseModel):
        class Clouds(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                ambient: _ColorT | None = None,
                direction: float | None = None,
                humidity: float | None = None,
                mean_size: float | None = None,
                speed: float | None = None
            ):
                super().__init__(sdf_version)
                self.ambient = _color(ambient) if ambient is not None else None
                self.direction = direction
                self.humidity = humidity
                self.mean_size = mean_size
                self.speed = speed

            def to_version(self, target_version: str) -> "Scene.SceneSky.Clouds":
                kwargs: dict = {"sdf_version": target_version, "ambient": self.ambient, "direction": self.direction, "humidity": self.humidity, "mean_size": self.mean_size, "speed": self.speed}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf()
                el = ET.Element("clouds")
                if self.ambient is not None:
                    _c_tmp = ET.Element("ambient")
                    _c_tmp.text = str(self.ambient)
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
                    _val = _parse_color(_text)
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
            cubemap_uri: str | None = None,
            sunrise: float | None = None,
            sunset: float | None = None,
            time: float | None = None
        ):
            super().__init__(sdf_version)
            self.clouds = clouds
            self.cubemap_uri = cubemap_uri
            self.sunrise = sunrise
            self.sunset = sunset
            self.time = time
            if self.clouds is not None and hasattr(self.clouds, 'to_version'):
                if getattr(self.clouds, 'sdfversion', None) is None:
                    self.clouds.sdfversion = self.sdfversion
                elif getattr(self.clouds, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.clouds = self.clouds.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Scene.SceneSky":
            if self.cubemap_uri is not None and cmp_version(target_version, "1.9") < 0:
                raise ValueError(f"'cubemap_uri' is not supported in SDF version {target_version} (added in 1.9)")
            kwargs: dict = {"sdf_version": target_version, "clouds": self.clouds.to_version(target_version) if self.clouds is not None and hasattr(self.clouds, "to_version") else self.clouds, "cubemap_uri": self.cubemap_uri, "sunrise": self.sunrise, "sunset": self.sunset, "time": self.time}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("sky")
            if self.clouds is not None:
                _child_res = self.clouds.to_sdf(version)
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
                _text = _c_tmp.text if _c_tmp.text is not None else None
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
        def __init__(
            self,
            sdf_version: str | None = None,
            enabled: bool | None = None,
            shadows: bool | None = None
        ):
            super().__init__(sdf_version)
            self.enabled = enabled
            self.shadows = shadows

        def to_version(self, target_version: str) -> "Scene.Shadows":
            kwargs: dict = {"sdf_version": target_version, "enabled": self.enabled, "shadows": self.shadows}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
            if _raw_enabled is not None:
                _enabled = str(_raw_enabled).strip().lower() == 'true'
                if isinstance(_enabled, SDFError):
                    return _enabled.extend("@enabled")
            else:
                _enabled = None
            _raw_shadows = el.text
            if _raw_shadows is not None:
                _shadows = str(_raw_shadows).strip().lower() == 'true'
                if isinstance(_shadows, SDFError):
                    return _shadows
            else:
                _shadows = None
            return cls(sdf_version=version, enabled=_enabled, shadows=_shadows)

    def __init__(
        self,
        sdf_version: str | None = None,
        ambient: "Scene.Ambient" = None,
        background: "Scene.Background" = None,
        fog: "Scene.Fog" = None,
        grid: "Scene.Grid" = None,
        origin_visual: bool | None = None,
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
            if getattr(self.ambient, 'sdfversion', None) is None:
                self.ambient.sdfversion = self.sdfversion
            elif getattr(self.ambient, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.ambient = self.ambient.to_version(self.sdfversion)
        if self.background is not None and hasattr(self.background, 'to_version'):
            if getattr(self.background, 'sdfversion', None) is None:
                self.background.sdfversion = self.sdfversion
            elif getattr(self.background, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.background = self.background.to_version(self.sdfversion)
        if self.fog is not None and hasattr(self.fog, 'to_version'):
            if getattr(self.fog, 'sdfversion', None) is None:
                self.fog.sdfversion = self.sdfversion
            elif getattr(self.fog, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.fog = self.fog.to_version(self.sdfversion)
        if self.grid is not None and hasattr(self.grid, 'to_version'):
            if getattr(self.grid, 'sdfversion', None) is None:
                self.grid.sdfversion = self.sdfversion
            elif getattr(self.grid, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.grid = self.grid.to_version(self.sdfversion)
        if self.shadows is not None and hasattr(self.shadows, 'to_version'):
            if getattr(self.shadows, 'sdfversion', None) is None:
                self.shadows.sdfversion = self.sdfversion
            elif getattr(self.shadows, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.shadows = self.shadows.to_version(self.sdfversion)
        if self.sky is not None and hasattr(self.sky, 'to_version'):
            if getattr(self.sky, 'sdfversion', None) is None:
                self.sky.sdfversion = self.sdfversion
            elif getattr(self.sky, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.sky = self.sky.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Scene":
        if self.origin_visual is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'origin_visual' is not supported in SDF version {target_version} (added in 1.5)")
        if self.sky is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'sky' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs: dict = {"sdf_version": target_version, "ambient": self.ambient.to_version(target_version) if self.ambient is not None and hasattr(self.ambient, "to_version") else self.ambient, "background": self.background.to_version(target_version) if self.background is not None and hasattr(self.background, "to_version") else self.background, "fog": self.fog.to_version(target_version) if self.fog is not None and hasattr(self.fog, "to_version") else self.fog, "grid": self.grid.to_version(target_version) if self.grid is not None and hasattr(self.grid, "to_version") else self.grid, "origin_visual": self.origin_visual, "shadows": self.shadows.to_version(target_version) if self.shadows is not None and hasattr(self.shadows, "to_version") else self.shadows, "sky": self.sky.to_version(target_version) if self.sky is not None and hasattr(self.sky, "to_version") else self.sky}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("scene")
        if self.ambient is not None:
            _child_res = self.ambient.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('ambient')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.background is not None:
            _child_res = self.background.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('background')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.fog is not None:
            _child_res = self.fog.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('fog')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.grid is not None:
            _child_res = self.grid.to_sdf(version)
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
            _child_res = self.shadows.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('shadows')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.sky is not None:
            _child_res = self.sky.to_sdf(version)
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
