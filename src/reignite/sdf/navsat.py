### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


class Navsat(BaseModel):
    class PositionSensing(BaseModel):
        class Horizontal(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, '__version__', None) is None:
                        self.noise.__version__ = self.__version__
                    elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.noise = self.noise.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Navsat.PositionSensing.Horizontal":
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
                el = ET.Element("horizontal")
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
            def _from_sdf(cls, el: ET.Element, version: str) -> "Navsat.PositionSensing.Horizontal | SDFError":
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

        class Vertical(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, '__version__', None) is None:
                        self.noise.__version__ = self.__version__
                    elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.noise = self.noise.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Navsat.PositionSensing.Vertical":
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
                el = ET.Element("vertical")
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
            def _from_sdf(cls, el: ET.Element, version: str) -> "Navsat.PositionSensing.Vertical | SDFError":
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
            horizontal: "Navsat.PositionSensing.Horizontal" = None,
            vertical: "Navsat.PositionSensing.Vertical" = None
        ):
            super().__init__(sdf_version)
            self.horizontal = horizontal
            self.vertical = vertical
            if self.horizontal is not None and hasattr(self.horizontal, 'to_version'):
                if getattr(self.horizontal, '__version__', None) is None:
                    self.horizontal.__version__ = self.__version__
                elif getattr(self.horizontal, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.horizontal = self.horizontal.to_version(self.__version__)
            if self.vertical is not None and hasattr(self.vertical, 'to_version'):
                if getattr(self.vertical, '__version__', None) is None:
                    self.vertical.__version__ = self.__version__
                elif getattr(self.vertical, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.vertical = self.vertical.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Navsat.PositionSensing":
            kwargs = {"sdf_version": target_version}
            kwargs["horizontal"] = self.horizontal.to_version(target_version) if hasattr(self.horizontal, "to_version") else self.horizontal
            kwargs["vertical"] = self.vertical.to_version(target_version) if hasattr(self.vertical, "to_version") else self.vertical
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("position_sensing")
            if self.horizontal is not None:
                if hasattr(self.horizontal, 'to_sdf'):
                    _child_res = self.horizontal.to_sdf(version)
                else:
                    _child_res = str(self.horizontal)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('horizontal')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.vertical is not None:
                if hasattr(self.vertical, 'to_sdf'):
                    _child_res = self.vertical.to_sdf(version)
                else:
                    _child_res = str(self.vertical)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('vertical')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Navsat.PositionSensing | SDFError":
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
                if getattr(self.horizontal, '__version__', None) is None:
                    self.horizontal.__version__ = self.__version__
                elif getattr(self.horizontal, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.horizontal = self.horizontal.to_version(self.__version__)
            if self.vertical is not None and hasattr(self.vertical, 'to_version'):
                if getattr(self.vertical, '__version__', None) is None:
                    self.vertical.__version__ = self.__version__
                elif getattr(self.vertical, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.vertical = self.vertical.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Navsat.VelocitySensing":
            kwargs = {"sdf_version": target_version}
            kwargs["horizontal"] = self.horizontal.to_version(target_version) if hasattr(self.horizontal, "to_version") else self.horizontal
            kwargs["vertical"] = self.vertical.to_version(target_version) if hasattr(self.vertical, "to_version") else self.vertical
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("velocity_sensing")
            if self.horizontal is not None:
                if hasattr(self.horizontal, 'to_sdf'):
                    _child_res = self.horizontal.to_sdf(version)
                else:
                    _child_res = str(self.horizontal)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('horizontal')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.vertical is not None:
                if hasattr(self.vertical, 'to_sdf'):
                    _child_res = self.vertical.to_sdf(version)
                else:
                    _child_res = str(self.vertical)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('vertical')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Navsat.VelocitySensing | SDFError":
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
        position_sensing: "Navsat.PositionSensing" = None,
        velocity_sensing: "Navsat.VelocitySensing" = None
    ):
        super().__init__(sdf_version)
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing
        if self.position_sensing is not None and hasattr(self.position_sensing, 'to_version'):
            if getattr(self.position_sensing, '__version__', None) is None:
                self.position_sensing.__version__ = self.__version__
            elif getattr(self.position_sensing, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.position_sensing = self.position_sensing.to_version(self.__version__)
        if self.velocity_sensing is not None and hasattr(self.velocity_sensing, 'to_version'):
            if getattr(self.velocity_sensing, '__version__', None) is None:
                self.velocity_sensing.__version__ = self.__version__
            elif getattr(self.velocity_sensing, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.velocity_sensing = self.velocity_sensing.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Navsat":
        kwargs = {"sdf_version": target_version}
        kwargs["position_sensing"] = self.position_sensing.to_version(target_version) if hasattr(self.position_sensing, "to_version") else self.position_sensing
        kwargs["velocity_sensing"] = self.velocity_sensing.to_version(target_version) if hasattr(self.velocity_sensing, "to_version") else self.velocity_sensing
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("navsat")
        if self.position_sensing is not None:
            if hasattr(self.position_sensing, 'to_sdf'):
                _child_res = self.position_sensing.to_sdf(version)
            else:
                _child_res = str(self.position_sensing)
            if isinstance(_child_res, str):
                _item_el = ET.Element('position_sensing')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.velocity_sensing is not None:
            if hasattr(self.velocity_sensing, 'to_sdf'):
                _child_res = self.velocity_sensing.to_sdf(version)
            else:
                _child_res = str(self.velocity_sensing)
            if isinstance(_child_res, str):
                _item_el = ET.Element('velocity_sensing')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Navsat | SDFError":
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
