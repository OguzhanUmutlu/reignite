### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


# noinspection PyUnusedImports
class ForceTorque(BaseModel):
    class Force(BaseModel):
        class X(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, 'sdfversion', None) is None:
                        self.noise.sdfversion = self.sdfversion
                    elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.noise = self.noise.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "ForceTorque.Force.X":
                from ..elements.noise import Noise
                kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
                return ForceTorque.Force.X(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                from ..elements.noise import Noise
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("x")
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
            def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Force.X | SDFError":
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

        class Y(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, 'sdfversion', None) is None:
                        self.noise.sdfversion = self.sdfversion
                    elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.noise = self.noise.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "ForceTorque.Force.Y":
                from ..elements.noise import Noise
                kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
                return ForceTorque.Force.Y(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                from ..elements.noise import Noise
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("y")
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
            def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Force.Y | SDFError":
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

        class Z(BaseModel):
            def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
                super().__init__(sdf_version)
                self.noise = noise
                if self.noise is not None and hasattr(self.noise, 'to_version'):
                    if getattr(self.noise, 'sdfversion', None) is None:
                        self.noise.sdfversion = self.sdfversion
                    elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                        self.noise = self.noise.to_version(self.sdfversion)

            def to_version(self, target_version: str) -> "ForceTorque.Force.Z":
                from ..elements.noise import Noise
                kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
                return ForceTorque.Force.Z(**kwargs)

            def to_sdf(self, version: str | None = None) -> ET.Element:
                from ..elements.noise import Noise
                if self.sdfversion is None and version is not None:
                    self.sdfversion = version
                elif version is not None and version != self.sdfversion:
                    return self.to_version(str(version)).to_sdf(version)
                if version is None:
                    version = self.sdfversion or "1.12"
                el = ET.Element("z")
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
            def _from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque.Force.Z | SDFError":
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
            x: "ForceTorque.Force.X" = None,
            y: "ForceTorque.Force.Y" = None,
            z: "ForceTorque.Force.Z" = None
        ):
            super().__init__(sdf_version)
            self.x = x
            self.y = y
            self.z = z
            if self.x is not None and hasattr(self.x, 'to_version'):
                if getattr(self.x, 'sdfversion', None) is None:
                    self.x.sdfversion = self.sdfversion
                elif getattr(self.x, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.x = self.x.to_version(self.sdfversion)
            if self.y is not None and hasattr(self.y, 'to_version'):
                if getattr(self.y, 'sdfversion', None) is None:
                    self.y.sdfversion = self.sdfversion
                elif getattr(self.y, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.y = self.y.to_version(self.sdfversion)
            if self.z is not None and hasattr(self.z, 'to_version'):
                if getattr(self.z, 'sdfversion', None) is None:
                    self.z.sdfversion = self.sdfversion
                elif getattr(self.z, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.z = self.z.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "ForceTorque.Force":
            kwargs: dict = {"sdf_version": target_version, "x": self.x.to_version(target_version) if self.x is not None and hasattr(self.x, "to_version") else self.x, "y": self.y.to_version(target_version) if self.y is not None and hasattr(self.y, "to_version") else self.y, "z": self.z.to_version(target_version) if self.z is not None and hasattr(self.z, "to_version") else self.z}
            return ForceTorque.Force(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("force")
            if self.x is not None:
                _child_res = self.x.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('x')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.y is not None:
                _child_res = self.y.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('y')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.z is not None:
                _child_res = self.z.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('z')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
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

    class Torque(BaseModel):
        def __init__(self, sdf_version: str | None = None, x: "X" = None, y: "Y" = None, z: "Z" = None):
            super().__init__(sdf_version)
            self.x = x
            self.y = y
            self.z = z
            if self.x is not None and hasattr(self.x, 'to_version'):
                if getattr(self.x, 'sdfversion', None) is None:
                    self.x.sdfversion = self.sdfversion
                elif getattr(self.x, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.x = self.x.to_version(self.sdfversion)
            if self.y is not None and hasattr(self.y, 'to_version'):
                if getattr(self.y, 'sdfversion', None) is None:
                    self.y.sdfversion = self.sdfversion
                elif getattr(self.y, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.y = self.y.to_version(self.sdfversion)
            if self.z is not None and hasattr(self.z, 'to_version'):
                if getattr(self.z, 'sdfversion', None) is None:
                    self.z.sdfversion = self.sdfversion
                elif getattr(self.z, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.z = self.z.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "ForceTorque.Torque":
            kwargs: dict = {"sdf_version": target_version, "x": self.x.to_version(target_version) if self.x is not None and hasattr(self.x, "to_version") else self.x, "y": self.y.to_version(target_version) if self.y is not None and hasattr(self.y, "to_version") else self.y, "z": self.z.to_version(target_version) if self.z is not None and hasattr(self.z, "to_version") else self.z}
            return ForceTorque.Torque(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("torque")
            if self.x is not None:
                _child_res = self.x.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('x')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.y is not None:
                _child_res = self.y.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('y')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.z is not None:
                _child_res = self.z.to_sdf(version)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('z')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
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
        frame: str | None = None,
        measure_direction: str | None = None,
        torque: "ForceTorque.Torque" = None
    ):
        super().__init__(sdf_version)
        self.force = force
        self.frame = frame
        self.measure_direction = measure_direction
        self.torque = torque
        if self.force is not None and hasattr(self.force, 'to_version'):
            if getattr(self.force, 'sdfversion', None) is None:
                self.force.sdfversion = self.sdfversion
            elif getattr(self.force, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.force = self.force.to_version(self.sdfversion)
        if self.torque is not None and hasattr(self.torque, 'to_version'):
            if getattr(self.torque, 'sdfversion', None) is None:
                self.torque.sdfversion = self.sdfversion
            elif getattr(self.torque, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.torque = self.torque.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "ForceTorque":
        if self.force is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {target_version} (added in 1.7)")
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        if self.torque is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs: dict = {"sdf_version": target_version, "force": self.force.to_version(target_version) if self.force is not None and hasattr(self.force, "to_version") else self.force, "frame": self.frame, "measure_direction": self.measure_direction, "torque": self.torque.to_version(target_version) if self.torque is not None and hasattr(self.torque, "to_version") else self.torque}
        return ForceTorque(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("force_torque")
        if self.force is not None:
            _child_res = self.force.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('force')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.frame is not None:
            _c_tmp = ET.Element("frame")
            _c_tmp.text = self.frame
            el.append(_c_tmp)
        if self.measure_direction is not None:
            _c_tmp = ET.Element("measure_direction")
            _c_tmp.text = self.measure_direction
            el.append(_c_tmp)
        if self.torque is not None:
            _child_res = self.torque.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('torque')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
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
        _c_tmp = el.find("frame")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "parent"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("frame")
            _frame = _val
        else:
            _frame = None
        _c_tmp = el.find("measure_direction")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "child_to_parent"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("measure_direction")
            _measure_direction = _val
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
