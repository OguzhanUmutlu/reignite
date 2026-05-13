### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


class Magnetometer(BaseModel):
    class X(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, '__version__', None) is None:
                    self.noise.__version__ = self.__version__
                elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.noise = self.noise.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Magnetometer.X":
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
            el = ET.Element("x")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer.X | SDFError":
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

    class Y(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, '__version__', None) is None:
                    self.noise.__version__ = self.__version__
                elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.noise = self.noise.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Magnetometer.Y":
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
            el = ET.Element("y")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer.Y | SDFError":
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

    class Z(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, '__version__', None) is None:
                    self.noise.__version__ = self.__version__
                elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.noise = self.noise.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Magnetometer.Z":
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
            el = ET.Element("z")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer.Z | SDFError":
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
        x: "Magnetometer.X" = None,
        y: "Magnetometer.Y" = None,
        z: "Magnetometer.Z" = None
    ):
        super().__init__(sdf_version)
        self.x = x
        self.y = y
        self.z = z
        if self.x is not None and hasattr(self.x, 'to_version'):
            if getattr(self.x, '__version__', None) is None:
                self.x.__version__ = self.__version__
            elif getattr(self.x, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.x = self.x.to_version(self.__version__)
        if self.y is not None and hasattr(self.y, 'to_version'):
            if getattr(self.y, '__version__', None) is None:
                self.y.__version__ = self.__version__
            elif getattr(self.y, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.y = self.y.to_version(self.__version__)
        if self.z is not None and hasattr(self.z, 'to_version'):
            if getattr(self.z, '__version__', None) is None:
                self.z.__version__ = self.__version__
            elif getattr(self.z, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.z = self.z.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Magnetometer":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if hasattr(self.x, "to_version") else self.x
        kwargs["y"] = self.y.to_version(target_version) if hasattr(self.y, "to_version") else self.y
        kwargs["z"] = self.z.to_version(target_version) if hasattr(self.z, "to_version") else self.z
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("magnetometer")
        if self.x is not None:
            if hasattr(self.x, 'to_sdf'):
                _child_res = self.x.to_sdf(version)
            else:
                _child_res = str(self.x)
            if isinstance(_child_res, str):
                _item_el = ET.Element('x')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.y is not None:
            if hasattr(self.y, 'to_sdf'):
                _child_res = self.y.to_sdf(version)
            else:
                _child_res = str(self.y)
            if isinstance(_child_res, str):
                _item_el = ET.Element('y')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.z is not None:
            if hasattr(self.z, 'to_sdf'):
                _child_res = self.z.to_sdf(version)
            else:
                _child_res = str(self.z)
            if isinstance(_child_res, str):
                _item_el = ET.Element('z')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer | SDFError":
        _c_x = el.find("x")
        if _c_x is not None:
            _res = cls.X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = cls.Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = cls.Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)
