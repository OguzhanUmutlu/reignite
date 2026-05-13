### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


class Altimeter(BaseModel):
    class VerticalPosition(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, '__version__', None) is None:
                    self.noise.__version__ = self.__version__
                elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.noise = self.noise.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Altimeter.VerticalPosition":
            from ..elements.noise import Noise
            kwargs = {"sdf_version": target_version}
            kwargs["noise"] = self.noise.to_version(target_version) if hasattr(self.noise, "to_version") else self.noise
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("vertical_position")
            if self.noise is None:
                self.noise = Noise(sdf_version=version)
            if self.noise is not None:
                if hasattr(self.noise, 'to_sdf'):
                    _child_res = self.noise.to_sdf(version)
                else:
                    _child_res = str(self.noise)
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
                _res = Noise._from_sdf(ET.Element("noise"), version)
                if isinstance(_res, SDFError):
                    return _res.extend("noise")
                _noise = _res
            return cls(sdf_version=version, noise=_noise)

    class VerticalVelocity(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, '__version__', None) is None:
                    self.noise.__version__ = self.__version__
                elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.noise = self.noise.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Altimeter.VerticalVelocity":
            from ..elements.noise import Noise
            kwargs = {"sdf_version": target_version}
            kwargs["noise"] = self.noise.to_version(target_version) if hasattr(self.noise, "to_version") else self.noise
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("vertical_velocity")
            if self.noise is None:
                self.noise = Noise(sdf_version=version)
            if self.noise is not None:
                if hasattr(self.noise, 'to_sdf'):
                    _child_res = self.noise.to_sdf(version)
                else:
                    _child_res = str(self.noise)
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
                _res = Noise._from_sdf(ET.Element("noise"), version)
                if isinstance(_res, SDFError):
                    return _res.extend("noise")
                _noise = _res
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
            if getattr(self.vertical_position, '__version__', None) is None:
                self.vertical_position.__version__ = self.__version__
            elif getattr(self.vertical_position, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.vertical_position = self.vertical_position.to_version(self.__version__)
        if self.vertical_velocity is not None and hasattr(self.vertical_velocity, 'to_version'):
            if getattr(self.vertical_velocity, '__version__', None) is None:
                self.vertical_velocity.__version__ = self.__version__
            elif getattr(self.vertical_velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.vertical_velocity = self.vertical_velocity.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Altimeter":
        kwargs = {"sdf_version": target_version}
        kwargs["vertical_position"] = self.vertical_position.to_version(target_version) if hasattr(self.vertical_position, "to_version") else self.vertical_position
        kwargs["vertical_velocity"] = self.vertical_velocity.to_version(target_version) if hasattr(self.vertical_velocity, "to_version") else self.vertical_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("altimeter")
        if self.vertical_position is not None:
            if hasattr(self.vertical_position, 'to_sdf'):
                _child_res = self.vertical_position.to_sdf(version)
            else:
                _child_res = str(self.vertical_position)
            if isinstance(_child_res, str):
                _item_el = ET.Element('vertical_position')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.vertical_velocity is not None:
            if hasattr(self.vertical_velocity, 'to_sdf'):
                _child_res = self.vertical_velocity.to_sdf(version)
            else:
                _child_res = str(self.vertical_velocity)
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
