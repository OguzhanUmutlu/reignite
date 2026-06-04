### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


# noinspection PyUnusedImports
class Gps(BaseModel):
    class PositionSensing(BaseModel):
        class Horizontal(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, 'sdfversion', None) is None:
                        self.noise.sdfversion = self.sdfversion
                    elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.noise = self.noise.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "Gps.PositionSensing.Horizontal":
                from ..elements.noise import Noise
                kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                from ..elements.noise import Noise
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("horizontal")
                if self.noise is not None:
                    _child_res = self.noise.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('noise')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Gps.PositionSensing.Horizontal | SDFError":
                from ..elements.noise import Noise
                _c_noise = el.find("noise")
                if _c_noise is not None:
                    _res = Noise._from_sdf(_c_noise, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("noise")
                    _noise = _res
                else:
                    _noise = None
                return cls(sdf_version=version, noise=_noise)

        class Vertical(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, 'sdfversion', None) is None:
                        self.noise.sdfversion = self.sdfversion
                    elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.noise = self.noise.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "Gps.PositionSensing.Vertical":
                from ..elements.noise import Noise
                kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
                return self.__class__(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                from ..elements.noise import Noise
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("vertical")
                if self.noise is not None:
                    _child_res = self.noise.to_sdf(version)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('noise')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Gps.PositionSensing.Vertical | SDFError":
                from ..elements.noise import Noise
                _c_noise = el.find("noise")
                if _c_noise is not None:
                    _res = Noise._from_sdf(_c_noise, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("noise")
                    _noise = _res
                else:
                    _noise = None
                return cls(sdf_version=version, noise=_noise)

        def __init__(
            self,
            sdf_version: str | None = None,
            horizontal: "Gps.PositionSensing.Horizontal" = None,
            vertical: "Gps.PositionSensing.Vertical" = None
        ):
            super().__init__(sdf_version)
            self.horizontal = horizontal
            self.vertical = vertical
            if self.horizontal is not None and hasattr(self.horizontal, 'to_version'):
                if getattr(self.horizontal, 'sdfversion', None) is None:
                    self.horizontal.sdfversion = self.sdfversion
                elif getattr(self.horizontal, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.horizontal = self.horizontal.to_version(self.sdfversion)
            if self.vertical is not None and hasattr(self.vertical, 'to_version'):
                if getattr(self.vertical, 'sdfversion', None) is None:
                    self.vertical.sdfversion = self.sdfversion
                elif getattr(self.vertical, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.vertical = self.vertical.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Gps.PositionSensing":
            kwargs: dict = {"sdf_version": target_version, "horizontal": self.horizontal.to_version(target_version) if self.horizontal is not None and hasattr(self.horizontal, "to_version") else self.horizontal, "vertical": self.vertical.to_version(target_version) if self.vertical is not None and hasattr(self.vertical, "to_version") else self.vertical}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("position_sensing")
            if self.horizontal is not None:
                _child_res = self.horizontal.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('horizontal')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.vertical is not None:
                _child_res = self.vertical.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('vertical')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Gps.PositionSensing | SDFError":
            _c_horizontal = el.find("horizontal")
            if _c_horizontal is not None:
                _res = cls.Horizontal._from_sdf(_c_horizontal, version)
                if isinstance(_res, SDFError):
                    return _res.extend("horizontal")
                _horizontal = _res
            else:
                _horizontal = None
            _c_vertical = el.find("vertical")
            if _c_vertical is not None:
                _res = cls.Vertical._from_sdf(_c_vertical, version)
                if isinstance(_res, SDFError):
                    return _res.extend("vertical")
                _vertical = _res
            else:
                _vertical = None
            return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)

    class VelocitySensing(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            horizontal: "Horizontal" = None,
            vertical: "Vertical" = None
        ):
            super().__init__(sdf_version)
            self.horizontal = horizontal
            self.vertical = vertical
            if self.horizontal is not None and hasattr(self.horizontal, 'to_version'):
                if getattr(self.horizontal, 'sdfversion', None) is None:
                    self.horizontal.sdfversion = self.sdfversion
                elif getattr(self.horizontal, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.horizontal = self.horizontal.to_version(self.sdfversion)
            if self.vertical is not None and hasattr(self.vertical, 'to_version'):
                if getattr(self.vertical, 'sdfversion', None) is None:
                    self.vertical.sdfversion = self.sdfversion
                elif getattr(self.vertical, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.vertical = self.vertical.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Gps.VelocitySensing":
            kwargs: dict = {"sdf_version": target_version, "horizontal": self.horizontal.to_version(target_version) if self.horizontal is not None and hasattr(self.horizontal, "to_version") else self.horizontal, "vertical": self.vertical.to_version(target_version) if self.vertical is not None and hasattr(self.vertical, "to_version") else self.vertical}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("velocity_sensing")
            if self.horizontal is not None:
                _child_res = self.horizontal.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('horizontal')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.vertical is not None:
                _child_res = self.vertical.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('vertical')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Gps.VelocitySensing | SDFError":
            _c_horizontal = el.find("horizontal")
            if _c_horizontal is not None:
                _res = Horizontal._from_sdf(_c_horizontal, version)
                if isinstance(_res, SDFError):
                    return _res.extend("horizontal")
                _horizontal = _res
            else:
                _horizontal = None
            _c_vertical = el.find("vertical")
            if _c_vertical is not None:
                _res = Vertical._from_sdf(_c_vertical, version)
                if isinstance(_res, SDFError):
                    return _res.extend("vertical")
                _vertical = _res
            else:
                _vertical = None
            return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)

    def __init__(
        self,
        sdf_version: str | None = None,
        position_sensing: "Gps.PositionSensing" = None,
        velocity_sensing: "Gps.VelocitySensing" = None
    ):
        super().__init__(sdf_version)
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing
        if self.position_sensing is not None and hasattr(self.position_sensing, 'to_version'):
            if getattr(self.position_sensing, 'sdfversion', None) is None:
                self.position_sensing.sdfversion = self.sdfversion
            elif getattr(self.position_sensing, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.position_sensing = self.position_sensing.to_version(self.sdfversion)
        if self.velocity_sensing is not None and hasattr(self.velocity_sensing, 'to_version'):
            if getattr(self.velocity_sensing, 'sdfversion', None) is None:
                self.velocity_sensing.sdfversion = self.sdfversion
            elif getattr(self.velocity_sensing, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.velocity_sensing = self.velocity_sensing.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Gps":
        kwargs: dict = {"sdf_version": target_version, "position_sensing": self.position_sensing.to_version(target_version) if self.position_sensing is not None and hasattr(self.position_sensing, "to_version") else self.position_sensing, "velocity_sensing": self.velocity_sensing.to_version(target_version) if self.velocity_sensing is not None and hasattr(self.velocity_sensing, "to_version") else self.velocity_sensing}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("gps")
        if self.position_sensing is not None:
            _child_res = self.position_sensing.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('position_sensing')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.velocity_sensing is not None:
            _child_res = self.velocity_sensing.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('velocity_sensing')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Gps | SDFError":
        _c_position_sensing = el.find("position_sensing")
        if _c_position_sensing is not None:
            _res = cls.PositionSensing._from_sdf(_c_position_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("position_sensing")
            _position_sensing = _res
        else:
            _position_sensing = None
        _c_velocity_sensing = el.find("velocity_sensing")
        if _c_velocity_sensing is not None:
            _res = cls.VelocitySensing._from_sdf(_c_velocity_sensing, version)
            if isinstance(_res, SDFError):
                return _res.extend("velocity_sensing")
            _velocity_sensing = _res
        else:
            _velocity_sensing = None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)
