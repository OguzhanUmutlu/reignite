### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color
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



class Ambient(BaseModel):
    def __init__(self, sdf_version: str, ambient: Color = None, rgba: Color = None):
        self.__version__ = sdf_version
        if ambient is None:
            ambient = Color.from_sdf("0.0 0.0 0.0 1.0")
        if rgba is None:
            rgba = Color.from_sdf("0.0 0.0 0.0 1.0")
        self.ambient = ambient
        self.rgba = rgba

    def to_version(self, target_version: str) -> "Ambient":
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        if cmp_version(version, "1.2") < 0:
            if self.rgba is None:
                raise ValueError(f"'rgba' is required in SDF version {version}")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.0 0.0 0.0 1.0"
        _ambient = Color._from_sdf(_text, version)
        if isinstance(_ambient, SDFError):
            return _ambient
        if cmp_version(version, "1.2") < 0:
            if el.get("rgba") is None:
                return SDFError(f"'rgba' is required in SDF version {version}")
        _rgba = Color._from_sdf(el.get("rgba", "0.0 0.0 0.0 1.0"), version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        return cls(sdf_version=version, ambient=_ambient, rgba=_rgba)


class Sky(BaseModel):
    def __init__(self, sdf_version: str, material: str = "Gazebo/CloudySky"):
        self.__version__ = sdf_version
        self.material = material

    def to_version(self, target_version: str) -> "Sky":
        kwargs = {"sdf_version": target_version}
        kwargs["material"] = self.material
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sky")
        if self.material is None:
            raise ValueError(f"'material' is required in SDF version {version}")
        if self.material is not None:
            el.set("material", self.material)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("material") is None:
            return SDFError(f"'material' is required in SDF version {version}")
        _material = el.get("material", "Gazebo/CloudySky")
        if isinstance(_material, SDFError):
            return _material.extend("@material")
        return cls(sdf_version=version, material=_material)


class Background(BaseModel):
    def __init__(self, sdf_version: str, rgba: Color = None, sky: "Sky" = None):
        self.__version__ = sdf_version
        if rgba is None:
            rgba = Color.from_sdf(".7 .7 .7 1")
        self.rgba = rgba
        self.sky = sky

    def to_version(self, target_version: str) -> "Background":
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.sky is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'sky' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["rgba"] = self.rgba
        kwargs["sky"] = self.sky.to_version(target_version) if self.sky is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("background")
        if cmp_version(version, "1.2") < 0:
            if self.rgba is None:
                raise ValueError(f"'rgba' is required in SDF version {version}")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        if self.sky is not None:
            el.append(self.sky.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if cmp_version(version, "1.2") < 0:
            if el.get("rgba") is None:
                return SDFError(f"'rgba' is required in SDF version {version}")
        _rgba = Color._from_sdf(el.get("rgba", ".7 .7 .7 1"), version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        _c_sky = el.find("sky")
        if _c_sky is not None:
            _res = Sky._from_sdf(_c_sky, version)
            if isinstance(_res, SDFError):
                return _res.extend("sky")
            _sky = _res
        else:
            _sky = None
        return cls(sdf_version=version, rgba=_rgba, sky=_sky)


class Shadows(BaseModel):
    def __init__(self, sdf_version: str, shadows: bool = True, enabled: bool = True):
        self.__version__ = sdf_version
        self.shadows = shadows
        self.enabled = enabled

    def to_version(self, target_version: str) -> "Shadows":
        if self.enabled is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'enabled' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["shadows"] = self.shadows
        kwargs["enabled"] = self.enabled
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("shadows")
        if self.shadows is not None:
            el.text = str(self.shadows).lower()
        if cmp_version(version, "1.2") < 0:
            if self.enabled is None:
                raise ValueError(f"'enabled' is required in SDF version {version}")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _shadows = str(_text).strip().lower() == 'true'
        if isinstance(_shadows, SDFError):
            return _shadows
        if cmp_version(version, "1.2") < 0:
            if el.get("enabled") is None:
                return SDFError(f"'enabled' is required in SDF version {version}")
        _enabled = str(el.get("enabled", True)).strip().lower() == 'true'
        if isinstance(_enabled, SDFError):
            return _enabled.extend("@enabled")
        return cls(sdf_version=version, shadows=_shadows, enabled=_enabled)


class Color(BaseModel):
    def __init__(self, sdf_version: str, color: Color = None):
        self.__version__ = sdf_version
        if color is None:
            color = Color.from_sdf("1 1 1 1")
        self.color = color

    def to_version(self, target_version: str) -> "Color":
        if self.color is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'color' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["color"] = self.color
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("color")
        if self.color is not None:
            el.text = self.color.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1 1"
        _color = Color._from_sdf(_text, version)
        if isinstance(_color, SDFError):
            return _color
        if _color is not None and cmp_version(version, "1.2") < 0:
            if _color != "1 1 1 1":
                return SDFError(f"'color' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, color=_color)


class Density(BaseModel):
    def __init__(self, sdf_version: str, density: float = 1.0):
        self.__version__ = sdf_version
        self.density = density

    def to_version(self, target_version: str) -> "Density":
        if self.density is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["density"] = self.density
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("density")
        if self.density is not None:
            el.text = str(self.density)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _density = _parse_double(_text)
        if isinstance(_density, SDFError):
            return _density
        if _density is not None and cmp_version(version, "1.2") < 0:
            if _density != 1.0:
                return SDFError(f"'density' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, density=_density)


class End(BaseModel):
    def __init__(self, sdf_version: str, end: float = 100.0):
        self.__version__ = sdf_version
        self.end = end

    def to_version(self, target_version: str) -> "End":
        if self.end is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'end' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["end"] = self.end
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("end")
        if self.end is not None:
            el.text = str(self.end)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100.0
        _end = _parse_double(_text)
        if isinstance(_end, SDFError):
            return _end
        if _end is not None and cmp_version(version, "1.2") < 0:
            if _end != 100.0:
                return SDFError(f"'end' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, end=_end)


class Type(BaseModel):
    def __init__(self, sdf_version: str, type: str = "none"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Type":
        if self.type is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'type' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "none"
        _type = _text
        if isinstance(_type, SDFError):
            return _type
        if _type is not None and cmp_version(version, "1.2") < 0:
            if _type != "none":
                return SDFError(f"'type' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, type=_type)


class Start(BaseModel):
    def __init__(self, sdf_version: str, start: float = 1.0):
        self.__version__ = sdf_version
        self.start = start

    def to_version(self, target_version: str) -> "Start":
        if self.start is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'start' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["start"] = self.start
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("start")
        if self.start is not None:
            el.text = str(self.start)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _start = _parse_double(_text)
        if isinstance(_start, SDFError):
            return _start
        if _start is not None and cmp_version(version, "1.2") < 0:
            if _start != 1.0:
                return SDFError(f"'start' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, start=_start)


class Fog(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        rgba: Color = None,
        type: str = "linear",
        start: float = 1.0,
        end: float = 100.0,
        density: float = 1.0,
        color: "Color" = None
    ):
        self.__version__ = sdf_version
        if rgba is None:
            rgba = Color.from_sdf("1 1 1 1")
        self.rgba = rgba
        self.type = type
        self.start = start
        self.end = end
        self.density = density
        self.color = color

    def to_version(self, target_version: str) -> "Fog":
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.type is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'type' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.start is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'start' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.end is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'end' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.density is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.color is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'color' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["rgba"] = self.rgba
        kwargs["type"] = self.type
        kwargs["start"] = self.start
        kwargs["end"] = self.end
        kwargs["density"] = self.density
        kwargs["color"] = self.color.to_version(target_version) if self.color is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fog")
        if self.rgba is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("color")
                _c_tmp.text = self.rgba.to_sdf()
                el.append(_c_tmp)
            else:
                el.set("rgba", self.rgba.to_sdf())
        if self.type is not None:
            el.set("type", self.type)
        if self.start is not None:
            el.set("start", str(self.start))
        if self.end is not None:
            el.set("end", str(self.end))
        if self.density is not None:
            el.set("density", str(self.density))
        if self.color is not None:
            el.append(self.color.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _raw_rgba = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("color")
            if _c_tmp is not None: _raw_rgba = _c_tmp.text
        else:
            _raw_rgba = el.get("rgba")
        if _raw_rgba is None: _raw_rgba = "1 1 1 1"
        _rgba = Color._from_sdf(_raw_rgba, version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        _type = el.get("type", "linear")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _start = _parse_double(el.get("start", 1.0))
        if isinstance(_start, SDFError):
            return _start.extend("@start")
        _end = _parse_double(el.get("end", 100.0))
        if isinstance(_end, SDFError):
            return _end.extend("@end")
        _density = _parse_double(el.get("density", 1.0))
        if isinstance(_density, SDFError):
            return _density.extend("@density")
        _c_color = el.find("color")
        if _c_color is not None:
            _res = Color._from_sdf(_c_color, version)
            if isinstance(_res, SDFError):
                return _res.extend("color")
            _color = _res
        else:
            _color = None
        if _color is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'color' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, rgba=_rgba, type=_type, start=_start, end=_end, density=_density, color=_color)


class Grid(BaseModel):
    def __init__(self, sdf_version: str, grid: bool = True, enabled: bool = True):
        self.__version__ = sdf_version
        self.grid = grid
        self.enabled = enabled

    def to_version(self, target_version: str) -> "Grid":
        if self.enabled is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'enabled' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["grid"] = self.grid
        kwargs["enabled"] = self.enabled
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grid")
        if self.grid is not None:
            el.text = str(self.grid).lower()
        if cmp_version(version, "1.2") < 0:
            if self.enabled is None:
                raise ValueError(f"'enabled' is required in SDF version {version}")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _grid = str(_text).strip().lower() == 'true'
        if isinstance(_grid, SDFError):
            return _grid
        if cmp_version(version, "1.2") < 0:
            if el.get("enabled") is None:
                return SDFError(f"'enabled' is required in SDF version {version}")
        _enabled = str(el.get("enabled", True)).strip().lower() == 'true'
        if isinstance(_enabled, SDFError):
            return _enabled.extend("@enabled")
        return cls(sdf_version=version, grid=_grid, enabled=_enabled)


class OriginVisual(BaseModel):
    def __init__(self, sdf_version: str, origin_visual: bool = True):
        self.__version__ = sdf_version
        self.origin_visual = origin_visual

    def to_version(self, target_version: str) -> "OriginVisual":
        if self.origin_visual is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'origin_visual' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["origin_visual"] = self.origin_visual
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("origin_visual")
        if self.origin_visual is not None:
            el.text = str(self.origin_visual).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _origin_visual = str(_text).strip().lower() == 'true'
        if isinstance(_origin_visual, SDFError):
            return _origin_visual
        if _origin_visual is not None and cmp_version(version, "1.5") < 0:
            if _origin_visual != True:
                return SDFError(f"'origin_visual' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, origin_visual=_origin_visual)


class Scene(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        ambient: "Ambient" = None,
        background: "Background" = None,
        shadows: "Shadows" = None,
        fog: "Fog" = None,
        grid: "Grid" = None,
        sky: "Sky" = None,
        origin_visual: "OriginVisual" = None
    ):
        self.__version__ = sdf_version
        self.ambient = ambient
        self.background = background
        self.shadows = shadows
        self.fog = fog
        self.grid = grid
        self.sky = sky
        self.origin_visual = origin_visual

    def to_version(self, target_version: str) -> "Scene":
        if self.sky is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'sky' is not supported in SDF version {target_version} (added in 1.2)")
        if self.origin_visual is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'origin_visual' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
        kwargs["background"] = self.background.to_version(target_version) if self.background is not None else None
        kwargs["shadows"] = self.shadows.to_version(target_version) if self.shadows is not None else None
        kwargs["fog"] = self.fog.to_version(target_version) if self.fog is not None else None
        kwargs["grid"] = self.grid.to_version(target_version) if self.grid is not None else None
        kwargs["sky"] = self.sky.to_version(target_version) if self.sky is not None else None
        kwargs["origin_visual"] = self.origin_visual.to_version(target_version) if self.origin_visual is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scene")
        if self.ambient is not None:
            el.append(self.ambient.to_sdf(version))
        if self.background is not None:
            el.append(self.background.to_sdf(version))
        if self.shadows is not None:
            el.append(self.shadows.to_sdf(version))
        if self.fog is not None:
            el.append(self.fog.to_sdf(version))
        if self.grid is not None:
            el.append(self.grid.to_sdf(version))
        if self.sky is not None:
            el.append(self.sky.to_sdf(version))
        if self.origin_visual is not None:
            el.append(self.origin_visual.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_ambient = el.find("ambient")
        if _c_ambient is not None:
            _res = Ambient._from_sdf(_c_ambient, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient")
            _ambient = _res
        else:
            _ambient = None
        _c_background = el.find("background")
        if _c_background is not None:
            _res = Background._from_sdf(_c_background, version)
            if isinstance(_res, SDFError):
                return _res.extend("background")
            _background = _res
        else:
            _background = None
        _c_shadows = el.find("shadows")
        if _c_shadows is not None:
            _res = Shadows._from_sdf(_c_shadows, version)
            if isinstance(_res, SDFError):
                return _res.extend("shadows")
            _shadows = _res
        else:
            _shadows = None
        _c_fog = el.find("fog")
        if _c_fog is not None:
            _res = Fog._from_sdf(_c_fog, version)
            if isinstance(_res, SDFError):
                return _res.extend("fog")
            _fog = _res
        else:
            _fog = None
        _c_grid = el.find("grid")
        if _c_grid is not None:
            _res = Grid._from_sdf(_c_grid, version)
            if isinstance(_res, SDFError):
                return _res.extend("grid")
            _grid = _res
        else:
            _grid = None
        _c_sky = el.find("sky")
        if _c_sky is not None:
            _res = Sky._from_sdf(_c_sky, version)
            if isinstance(_res, SDFError):
                return _res.extend("sky")
            _sky = _res
        else:
            _sky = None
        if _sky is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'sky' is not supported in SDF version {version} (added in 1.2)")
        _c_origin_visual = el.find("origin_visual")
        if _c_origin_visual is not None:
            _res = OriginVisual._from_sdf(_c_origin_visual, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin_visual")
            _origin_visual = _res
        else:
            _origin_visual = None
        if _origin_visual is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'origin_visual' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, ambient=_ambient, background=_background, shadows=_shadows, fog=_fog, grid=_grid, sky=_sky, origin_visual=_origin_visual)
