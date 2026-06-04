### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


# noinspection PyUnusedImports
class Altimeter(BaseModel):
    class VerticalPosition(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, 'sdfversion', None) is None:
                    self.noise.sdfversion = self.sdfversion
                elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.noise = self.noise.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Altimeter.VerticalPosition":
            from ..elements.noise import Noise
            kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("vertical_position")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Altimeter.VerticalPosition | SDFError":
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

    class VerticalVelocity(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, 'sdfversion', None) is None:
                    self.noise.sdfversion = self.sdfversion
                elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.noise = self.noise.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Altimeter.VerticalVelocity":
            from ..elements.noise import Noise
            kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("vertical_velocity")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Altimeter.VerticalVelocity | SDFError":
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
        vertical_position: "Altimeter.VerticalPosition" = None,
        vertical_velocity: "Altimeter.VerticalVelocity" = None
    ):
        super().__init__(sdf_version)
        self.vertical_position = vertical_position
        self.vertical_velocity = vertical_velocity
        if self.vertical_position is not None and hasattr(self.vertical_position, 'to_version'):
            if getattr(self.vertical_position, 'sdfversion', None) is None:
                self.vertical_position.sdfversion = self.sdfversion
            elif getattr(self.vertical_position, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.vertical_position = self.vertical_position.to_version(self.sdfversion)
        if self.vertical_velocity is not None and hasattr(self.vertical_velocity, 'to_version'):
            if getattr(self.vertical_velocity, 'sdfversion', None) is None:
                self.vertical_velocity.sdfversion = self.sdfversion
            elif getattr(self.vertical_velocity, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.vertical_velocity = self.vertical_velocity.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Altimeter":
        kwargs: dict = {"sdf_version": target_version, "vertical_position": self.vertical_position.to_version(target_version) if self.vertical_position is not None and hasattr(self.vertical_position, "to_version") else self.vertical_position, "vertical_velocity": self.vertical_velocity.to_version(target_version) if self.vertical_velocity is not None and hasattr(self.vertical_velocity, "to_version") else self.vertical_velocity}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("altimeter")
        if self.vertical_position is not None:
            _child_res = self.vertical_position.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('vertical_position')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.vertical_velocity is not None:
            _child_res = self.vertical_velocity.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('vertical_velocity')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Altimeter | SDFError":
        _c_vertical_position = el.find("vertical_position")
        if _c_vertical_position is not None:
            _res = cls.VerticalPosition._from_sdf(_c_vertical_position, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical_position")
            _vertical_position = _res
        else:
            _vertical_position = None
        _c_vertical_velocity = el.find("vertical_velocity")
        if _c_vertical_velocity is not None:
            _res = cls.VerticalVelocity._from_sdf(_c_vertical_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical_velocity")
            _vertical_velocity = _res
        else:
            _vertical_velocity = None
        return cls(sdf_version=version, vertical_position=_vertical_position, vertical_velocity=_vertical_velocity)
