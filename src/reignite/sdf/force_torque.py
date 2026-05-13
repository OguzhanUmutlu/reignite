### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


class ForceTorque(BaseModel):
    class Force(BaseModel):
        class X(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None:
                    if getattr(self.noise, '__version__', None) is None:
                        self.noise.__version__ = self.__version__
                    elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.noise = self.noise.to_version(self.__version__)

            def to_version(self, target_version: str) -> "ForceTorque.Force.X":
                from ..elements.noise import Noise
                kwargs = {"sdf_version": target_version}
                kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
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
                    el.append(self.noise.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Force.X | SDFError":
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
                if self.noise is not None:
                    if getattr(self.noise, '__version__', None) is None:
                        self.noise.__version__ = self.__version__
                    elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.noise = self.noise.to_version(self.__version__)

            def to_version(self, target_version: str) -> "ForceTorque.Force.Y":
                from ..elements.noise import Noise
                kwargs = {"sdf_version": target_version}
                kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
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
                    el.append(self.noise.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Force.Y | SDFError":
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
                if self.noise is not None:
                    if getattr(self.noise, '__version__', None) is None:
                        self.noise.__version__ = self.__version__
                    elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.noise = self.noise.to_version(self.__version__)

            def to_version(self, target_version: str) -> "ForceTorque.Force.Z":
                from ..elements.noise import Noise
                kwargs = {"sdf_version": target_version}
                kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
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
                    el.append(self.noise.to_sdf(version))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Force.Z | SDFError":
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
            x: "ForceTorque.Force.X" = None,
            y: "ForceTorque.Force.Y" = None,
            z: "ForceTorque.Force.Z" = None
        ):
            super().__init__(sdf_version)
            self.x = x
            self.y = y
            self.z = z
            if self.x is not None:
                if getattr(self.x, '__version__', None) is None:
                    self.x.__version__ = self.__version__
                elif getattr(self.x, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.x = self.x.to_version(self.__version__)
            if self.y is not None:
                if getattr(self.y, '__version__', None) is None:
                    self.y.__version__ = self.__version__
                elif getattr(self.y, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.y = self.y.to_version(self.__version__)
            if self.z is not None:
                if getattr(self.z, '__version__', None) is None:
                    self.z.__version__ = self.__version__
                elif getattr(self.z, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.z = self.z.to_version(self.__version__)

        def to_version(self, target_version: str) -> "ForceTorque.Force":
            kwargs = {"sdf_version": target_version}
            kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
            kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
            kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("force")
            if self.x is not None:
                el.append(self.x.to_sdf(version))
            if self.y is not None:
                el.append(self.y.to_sdf(version))
            if self.z is not None:
                el.append(self.z.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Force | SDFError":
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

    class Frame(BaseModel):
        def __init__(self, sdf_version: str | None = None, frame: str = "parent"):
            super().__init__(sdf_version)
            self.frame = frame

        def to_version(self, target_version: str) -> "ForceTorque.Frame":
            kwargs = {"sdf_version": target_version}
            kwargs["frame"] = self.frame
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("frame")
            if self.frame is not None:
                el.text = self.frame
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Frame | SDFError":
            _text = el.text or "parent"
            _frame = _text
            if isinstance(_frame, SDFError):
                return _frame
            return cls(sdf_version=version, frame=_frame)

    class MeasureDirection(BaseModel):
        def __init__(self, sdf_version: str | None = None, measure_direction: str = "child_to_parent"):
            super().__init__(sdf_version)
            self.measure_direction = measure_direction

        def to_version(self, target_version: str) -> "ForceTorque.MeasureDirection":
            if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
            kwargs = {"sdf_version": target_version}
            kwargs["measure_direction"] = self.measure_direction
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("measure_direction")
            if self.measure_direction is not None:
                el.text = self.measure_direction
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.MeasureDirection | SDFError":
            _text = el.text or "child_to_parent"
            _measure_direction = _text
            if isinstance(_measure_direction, SDFError):
                return _measure_direction
            if _measure_direction is not None and cmp_version(version, "1.5") < 0:
                if _measure_direction != "child_to_parent":
                    return SDFError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
            return cls(sdf_version=version, measure_direction=_measure_direction)

    class Torque(BaseModel):
        def __init__(self, sdf_version: str | None = None, x: "X" = None, y: "Y" = None, z: "Z" = None):
            super().__init__(sdf_version)
            self.x = x
            self.y = y
            self.z = z
            if self.x is not None:
                if getattr(self.x, '__version__', None) is None:
                    self.x.__version__ = self.__version__
                elif getattr(self.x, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.x = self.x.to_version(self.__version__)
            if self.y is not None:
                if getattr(self.y, '__version__', None) is None:
                    self.y.__version__ = self.__version__
                elif getattr(self.y, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.y = self.y.to_version(self.__version__)
            if self.z is not None:
                if getattr(self.z, '__version__', None) is None:
                    self.z.__version__ = self.__version__
                elif getattr(self.z, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.z = self.z.to_version(self.__version__)

        def to_version(self, target_version: str) -> "ForceTorque.Torque":
            kwargs = {"sdf_version": target_version}
            kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
            kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
            kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("torque")
            if self.x is not None:
                el.append(self.x.to_sdf(version))
            if self.y is not None:
                el.append(self.y.to_sdf(version))
            if self.z is not None:
                el.append(self.z.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Torque | SDFError":
            _c_x = el.find("x")
            if _c_x is not None:
                _res = X._from_sdf(_c_x, version)
                if isinstance(_res, SDFError):
                    return _res.extend("x")
                _x = _res
            else:
                _x = None
            _c_y = el.find("y")
            if _c_y is not None:
                _res = Y._from_sdf(_c_y, version)
                if isinstance(_res, SDFError):
                    return _res.extend("y")
                _y = _res
            else:
                _y = None
            _c_z = el.find("z")
            if _c_z is not None:
                _res = Z._from_sdf(_c_z, version)
                if isinstance(_res, SDFError):
                    return _res.extend("z")
                _z = _res
            else:
                _z = None
            return cls(sdf_version=version, x=_x, y=_y, z=_z)

    def __init__(
        self,
        sdf_version: str | None = None,
        force: "ForceTorque.Force" = None,
        frame: "ForceTorque.Frame" = None,
        measure_direction: "ForceTorque.MeasureDirection" = None,
        torque: "ForceTorque.Torque" = None
    ):
        super().__init__(sdf_version)
        self.force = force
        self.frame = frame
        self.measure_direction = measure_direction
        self.torque = torque
        if self.force is not None:
            if getattr(self.force, '__version__', None) is None:
                self.force.__version__ = self.__version__
            elif getattr(self.force, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.force = self.force.to_version(self.__version__)
        if self.frame is not None:
            if getattr(self.frame, '__version__', None) is None:
                self.frame.__version__ = self.__version__
            elif getattr(self.frame, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.frame = self.frame.to_version(self.__version__)
        if self.measure_direction is not None:
            if getattr(self.measure_direction, '__version__', None) is None:
                self.measure_direction.__version__ = self.__version__
            elif getattr(self.measure_direction, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.measure_direction = self.measure_direction.to_version(self.__version__)
        if self.torque is not None:
            if getattr(self.torque, '__version__', None) is None:
                self.torque.__version__ = self.__version__
            elif getattr(self.torque, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.torque = self.torque.to_version(self.__version__)

    def to_version(self, target_version: str) -> "ForceTorque":
        if self.force is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {target_version} (added in 1.7)")
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        if self.torque is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
        kwargs["frame"] = self.frame.to_version(target_version) if self.frame is not None else None
        kwargs["measure_direction"] = self.measure_direction.to_version(target_version) if self.measure_direction is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("force_torque")
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        if self.frame is not None:
            el.append(self.frame.to_sdf(version))
        if self.measure_direction is not None:
            el.append(self.measure_direction.to_sdf(version))
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque | SDFError":
        _c_force = el.find("force")
        if _c_force is not None:
            _res = cls.Force._from_sdf(_c_force, version)
            if isinstance(_res, SDFError):
                return _res.extend("force")
            _force = _res
        else:
            _force = None
        if _force is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'force' is not supported in SDF version {version} (added in 1.7)")
        _c_frame = el.find("frame")
        if _c_frame is not None:
            _res = cls.Frame._from_sdf(_c_frame, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame = _res
        else:
            _frame = None
        _c_measure_direction = el.find("measure_direction")
        if _c_measure_direction is not None:
            _res = cls.MeasureDirection._from_sdf(_c_measure_direction, version)
            if isinstance(_res, SDFError):
                return _res.extend("measure_direction")
            _measure_direction = _res
        else:
            _measure_direction = None
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        _c_torque = el.find("torque")
        if _c_torque is not None:
            _res = cls.Torque._from_sdf(_c_torque, version)
            if isinstance(_res, SDFError):
                return _res.extend("torque")
            _torque = _res
        else:
            _torque = None
        if _torque is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'torque' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, force=_force, frame=_frame, measure_direction=_measure_direction, torque=_torque)
