### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3, _Vector3T, _vector3
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


def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


class Surface(BaseModel):
    class Bounce(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            restitution_coefficient: float = 0,
            threshold: float = 100000
        ):
            super().__init__(sdf_version)
            self.restitution_coefficient = restitution_coefficient
            self.threshold = threshold

        def to_version(self, target_version: str) -> "Surface.Bounce":
            if self.restitution_coefficient is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'restitution_coefficient' is not supported in SDF version {target_version} (removed in 1.2)")
            if self.threshold is not None and cmp_version(target_version, "1.2") >= 0:
                raise ValueError(f"'threshold' is not supported in SDF version {target_version} (removed in 1.2)")
            kwargs = {"sdf_version": target_version}
            kwargs["restitution_coefficient"] = self.restitution_coefficient
            kwargs["threshold"] = self.threshold
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("bounce")
            if self.restitution_coefficient is not None:
                el.set("restitution_coefficient", str(self.restitution_coefficient))
            if self.threshold is not None:
                el.set("threshold", str(self.threshold))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Bounce | SDFError":
            _restitution_coefficient = _parse_double(el.get("restitution_coefficient", 0))
            if isinstance(_restitution_coefficient, SDFError):
                return _restitution_coefficient.extend("@restitution_coefficient")
            _threshold = _parse_double(el.get("threshold", 100000))
            if isinstance(_threshold, SDFError):
                return _threshold.extend("@threshold")
            return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient, threshold=_threshold)

    class Contact(BaseModel):
        class Bullet(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                kd: float = 1.0,
                kp: float = 1000000000000.0,
                soft_cfm: float = 0,
                soft_erp: float = 0.2,
                split_impulse: bool = True,
                split_impulse_penetration_threshold: float = -0.01
            ):
                super().__init__(sdf_version)
                self.kd = kd
                self.kp = kp
                self.soft_cfm = soft_cfm
                self.soft_erp = soft_erp
                self.split_impulse = split_impulse
                self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

            def to_version(self, target_version: str) -> "Surface.Contact.Bullet":
                kwargs = {"sdf_version": target_version}
                kwargs["kd"] = self.kd
                kwargs["kp"] = self.kp
                kwargs["soft_cfm"] = self.soft_cfm
                kwargs["soft_erp"] = self.soft_erp
                kwargs["split_impulse"] = self.split_impulse
                kwargs["split_impulse_penetration_threshold"] = self.split_impulse_penetration_threshold
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("bullet")
                if self.kd is not None:
                    _c_tmp = ET.Element("kd")
                    _c_tmp.text = str(self.kd)
                    el.append(_c_tmp)
                if self.kp is not None:
                    _c_tmp = ET.Element("kp")
                    _c_tmp.text = str(self.kp)
                    el.append(_c_tmp)
                if self.soft_cfm is not None:
                    _c_tmp = ET.Element("soft_cfm")
                    _c_tmp.text = str(self.soft_cfm)
                    el.append(_c_tmp)
                if self.soft_erp is not None:
                    _c_tmp = ET.Element("soft_erp")
                    _c_tmp.text = str(self.soft_erp)
                    el.append(_c_tmp)
                if self.split_impulse is not None:
                    _c_tmp = ET.Element("split_impulse")
                    _c_tmp.text = str(self.split_impulse).lower()
                    el.append(_c_tmp)
                if self.split_impulse_penetration_threshold is not None:
                    _c_tmp = ET.Element("split_impulse_penetration_threshold")
                    _c_tmp.text = str(self.split_impulse_penetration_threshold)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Contact.Bullet | SDFError":
                _c_tmp = el.find("kd")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("kd")
                    _kd = _val
                else:
                    _kd = None
                _c_tmp = el.find("kp")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1000000000000.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("kp")
                    _kp = _val
                else:
                    _kp = None
                _c_tmp = el.find("soft_cfm")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("soft_cfm")
                    _soft_cfm = _val
                else:
                    _soft_cfm = None
                _c_tmp = el.find("soft_erp")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.2
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("soft_erp")
                    _soft_erp = _val
                else:
                    _soft_erp = None
                _c_tmp = el.find("split_impulse")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else True
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("split_impulse")
                    _split_impulse = _val
                else:
                    _split_impulse = None
                _c_tmp = el.find("split_impulse_penetration_threshold")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else -0.01
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("split_impulse_penetration_threshold")
                    _split_impulse_penetration_threshold = _val
                else:
                    _split_impulse_penetration_threshold = None
                return cls(sdf_version=version, kd=_kd, kp=_kp, soft_cfm=_soft_cfm, soft_erp=_soft_erp, split_impulse=_split_impulse, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)

        class Ode(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                kd: float = 1.0,
                kp: float = 1000000000000.0,
                max_vel: float = 0.01,
                min_depth: float = 0,
                soft_cfm: float = 0,
                soft_erp: float = 0.2
            ):
                super().__init__(sdf_version)
                self.kd = kd
                self.kp = kp
                self.max_vel = max_vel
                self.min_depth = min_depth
                self.soft_cfm = soft_cfm
                self.soft_erp = soft_erp

            def to_version(self, target_version: str) -> "Surface.Contact.Ode":
                if self.kd is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'kd' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.kp is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'kp' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.max_vel is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'max_vel' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.min_depth is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'min_depth' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.soft_cfm is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'soft_cfm' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.soft_erp is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'soft_erp' is not supported in SDF version {target_version} (removed in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["kd"] = self.kd
                kwargs["kp"] = self.kp
                kwargs["max_vel"] = self.max_vel
                kwargs["min_depth"] = self.min_depth
                kwargs["soft_cfm"] = self.soft_cfm
                kwargs["soft_erp"] = self.soft_erp
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("ode")
                if self.kd is not None:
                    el.set("kd", str(self.kd))
                if self.kp is not None:
                    el.set("kp", str(self.kp))
                if self.max_vel is not None:
                    el.set("max_vel", str(self.max_vel))
                if self.min_depth is not None:
                    el.set("min_depth", str(self.min_depth))
                if self.soft_cfm is not None:
                    el.set("soft_cfm", str(self.soft_cfm))
                if self.soft_erp is not None:
                    el.set("soft_erp", str(self.soft_erp))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Contact.Ode | SDFError":
                _kd = _parse_double(el.get("kd", 1.0))
                if isinstance(_kd, SDFError):
                    return _kd.extend("@kd")
                _kp = _parse_double(el.get("kp", 1000000000000.0))
                if isinstance(_kp, SDFError):
                    return _kp.extend("@kp")
                _max_vel = _parse_double(el.get("max_vel", 0.01))
                if isinstance(_max_vel, SDFError):
                    return _max_vel.extend("@max_vel")
                _min_depth = _parse_double(el.get("min_depth", 0))
                if isinstance(_min_depth, SDFError):
                    return _min_depth.extend("@min_depth")
                _soft_cfm = _parse_double(el.get("soft_cfm", 0))
                if isinstance(_soft_cfm, SDFError):
                    return _soft_cfm.extend("@soft_cfm")
                _soft_erp = _parse_double(el.get("soft_erp", 0.2))
                if isinstance(_soft_erp, SDFError):
                    return _soft_erp.extend("@soft_erp")
                return cls(sdf_version=version, kd=_kd, kp=_kp, max_vel=_max_vel, min_depth=_min_depth, soft_cfm=_soft_cfm, soft_erp=_soft_erp)

        def __init__(
            self,
            sdf_version: str | None = None,
            bullet: "Surface.Contact.Bullet" = None,
            category_bitmask: int = 65535,
            collide_bitmask: int = 1,
            collide_without_contact: bool = False,
            collide_without_contact_bitmask: int = 1,
            elastic_modulus: float = -1,
            ode: "Surface.Contact.Ode" = None,
            poissons_ratio: float = 0.3
        ):
            super().__init__(sdf_version)
            self.bullet = bullet
            self.category_bitmask = category_bitmask
            self.collide_bitmask = collide_bitmask
            self.collide_without_contact = collide_without_contact
            self.collide_without_contact_bitmask = collide_without_contact_bitmask
            self.elastic_modulus = elastic_modulus
            self.ode = ode
            self.poissons_ratio = poissons_ratio
            if self.bullet is not None and hasattr(self.bullet, 'to_version'):
                if getattr(self.bullet, '__version__', None) is None:
                    self.bullet.__version__ = self.__version__
                elif getattr(self.bullet, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.bullet = self.bullet.to_version(self.__version__)
            if self.ode is not None and hasattr(self.ode, 'to_version'):
                if getattr(self.ode, '__version__', None) is None:
                    self.ode.__version__ = self.__version__
                elif getattr(self.ode, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.ode = self.ode.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Surface.Contact":
            if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
            if self.category_bitmask is not None and cmp_version(target_version, "1.6") < 0:
                raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.6)")
            if self.collide_bitmask is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'collide_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
            if self.collide_without_contact is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'collide_without_contact' is not supported in SDF version {target_version} (added in 1.4)")
            if self.collide_without_contact_bitmask is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
            if self.elastic_modulus is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.5)")
            if self.poissons_ratio is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.5)")
            kwargs = {"sdf_version": target_version}
            kwargs["bullet"] = self.bullet.to_version(target_version) if hasattr(self.bullet, "to_version") else self.bullet
            kwargs["category_bitmask"] = self.category_bitmask
            kwargs["collide_bitmask"] = self.collide_bitmask
            kwargs["collide_without_contact"] = self.collide_without_contact
            kwargs["collide_without_contact_bitmask"] = self.collide_without_contact_bitmask
            kwargs["elastic_modulus"] = self.elastic_modulus
            kwargs["ode"] = self.ode.to_version(target_version) if hasattr(self.ode, "to_version") else self.ode
            kwargs["poissons_ratio"] = self.poissons_ratio
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("contact")
            if self.bullet is not None:
                if hasattr(self.bullet, 'to_sdf'):
                    _child_res = self.bullet.to_sdf(version)
                else:
                    _child_res = str(self.bullet)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('bullet')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.category_bitmask is not None:
                _c_tmp = ET.Element("category_bitmask")
                _c_tmp.text = str(self.category_bitmask)
                el.append(_c_tmp)
            if self.collide_bitmask is not None:
                _c_tmp = ET.Element("collide_bitmask")
                _c_tmp.text = str(self.collide_bitmask)
                el.append(_c_tmp)
            if self.collide_without_contact is not None:
                _c_tmp = ET.Element("collide_without_contact")
                _c_tmp.text = str(self.collide_without_contact).lower()
                el.append(_c_tmp)
            if self.collide_without_contact_bitmask is not None:
                _c_tmp = ET.Element("collide_without_contact_bitmask")
                _c_tmp.text = str(self.collide_without_contact_bitmask)
                el.append(_c_tmp)
            if self.elastic_modulus is not None:
                _c_tmp = ET.Element("elastic_modulus")
                _c_tmp.text = str(self.elastic_modulus)
                el.append(_c_tmp)
            if self.ode is not None:
                if hasattr(self.ode, 'to_sdf'):
                    _child_res = self.ode.to_sdf(version)
                else:
                    _child_res = str(self.ode)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('ode')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.poissons_ratio is not None:
                _c_tmp = ET.Element("poissons_ratio")
                _c_tmp.text = str(self.poissons_ratio)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Contact | SDFError":
            _c_bullet = el.find("bullet")
            if _c_bullet is not None:
                _res = cls.Bullet._from_sdf(_c_bullet, version)
                if isinstance(_res, SDFError):
                    return _res.extend("bullet")
                _bullet = _res
            else:
                _bullet = None
            if _bullet is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
            _c_tmp = el.find("category_bitmask")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 65535
                _val = _parse_uint32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("category_bitmask")
                _category_bitmask = _val
            else:
                _category_bitmask = None
            if _category_bitmask is not None and cmp_version(version, "1.6") < 0:
                return SDFError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.6)")
            _c_tmp = el.find("collide_bitmask")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 1
                _val = _parse_uint32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("collide_bitmask")
                _collide_bitmask = _val
            else:
                _collide_bitmask = None
            if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
            _c_tmp = el.find("collide_without_contact")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else False
                _val = str(_text).strip().lower() == 'true'
                if isinstance(_val, SDFError):
                    return _val.extend("collide_without_contact")
                _collide_without_contact = _val
            else:
                _collide_without_contact = None
            if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
            _c_tmp = el.find("collide_without_contact_bitmask")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 1
                _val = _parse_uint32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("collide_without_contact_bitmask")
                _collide_without_contact_bitmask = _val
            else:
                _collide_without_contact_bitmask = None
            if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
            _c_tmp = el.find("elastic_modulus")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else -1
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("elastic_modulus")
                _elastic_modulus = _val
            else:
                _elastic_modulus = None
            if _elastic_modulus is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.5)")
            _c_ode = el.find("ode")
            if _c_ode is not None:
                _res = cls.Ode._from_sdf(_c_ode, version)
                if isinstance(_res, SDFError):
                    return _res.extend("ode")
                _ode = _res
            else:
                _ode = None
            _c_tmp = el.find("poissons_ratio")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 0.3
                _val = _parse_double(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("poissons_ratio")
                _poissons_ratio = _val
            else:
                _poissons_ratio = None
            if _poissons_ratio is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.5)")
            return cls(sdf_version=version, bullet=_bullet, category_bitmask=_category_bitmask, collide_bitmask=_collide_bitmask, collide_without_contact=_collide_without_contact, collide_without_contact_bitmask=_collide_without_contact_bitmask, elastic_modulus=_elastic_modulus, ode=_ode, poissons_ratio=_poissons_ratio)

    class Friction(BaseModel):
        class FrictionBullet(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                fdir1: _Vector3T = None,
                friction: float = 1,
                friction2: float = 1,
                rolling_friction: float = 1
            ):
                super().__init__(sdf_version)
                if fdir1 is None:
                    fdir1 = _vector3("0 0 0")
                else:
                    fdir1 = _vector3(fdir1)
                self.fdir1 = fdir1
                self.friction = friction
                self.friction2 = friction2
                self.rolling_friction = rolling_friction

            def to_version(self, target_version: str) -> "Surface.Friction.FrictionBullet":
                kwargs = {"sdf_version": target_version}
                kwargs["fdir1"] = self.fdir1
                kwargs["friction"] = self.friction
                kwargs["friction2"] = self.friction2
                kwargs["rolling_friction"] = self.rolling_friction
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("bullet")
                if self.fdir1 is not None:
                    _c_tmp = ET.Element("fdir1")
                    _c_tmp.text = str(self.fdir1)
                    el.append(_c_tmp)
                if self.friction is not None:
                    _c_tmp = ET.Element("friction")
                    _c_tmp.text = str(self.friction)
                    el.append(_c_tmp)
                if self.friction2 is not None:
                    _c_tmp = ET.Element("friction2")
                    _c_tmp.text = str(self.friction2)
                    el.append(_c_tmp)
                if self.rolling_friction is not None:
                    _c_tmp = ET.Element("rolling_friction")
                    _c_tmp.text = str(self.rolling_friction)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Friction.FrictionBullet | SDFError":
                _c_tmp = el.find("fdir1")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else "0 0 0"
                    _val = _parse_vector3(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("fdir1")
                    _fdir1 = _val
                else:
                    _fdir1 = None
                _c_tmp = el.find("friction")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("friction")
                    _friction = _val
                else:
                    _friction = None
                _c_tmp = el.find("friction2")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("friction2")
                    _friction2 = _val
                else:
                    _friction2 = None
                _c_tmp = el.find("rolling_friction")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("rolling_friction")
                    _rolling_friction = _val
                else:
                    _rolling_friction = None
                return cls(sdf_version=version, fdir1=_fdir1, friction=_friction, friction2=_friction2, rolling_friction=_rolling_friction)

        class FrictionOde(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                fdir1: _Vector3T = None,
                mu: float = -1,
                mu2: float = -1,
                slip1: float = 0.0,
                slip2: float = 0.0
            ):
                super().__init__(sdf_version)
                if fdir1 is None:
                    fdir1 = _vector3("0 0 0")
                else:
                    fdir1 = _vector3(fdir1)
                self.fdir1 = fdir1
                self.mu = mu
                self.mu2 = mu2
                self.slip1 = slip1
                self.slip2 = slip2

            def to_version(self, target_version: str) -> "Surface.Friction.FrictionOde":
                if self.fdir1 is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'fdir1' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.mu is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'mu' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.mu2 is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'mu2' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.slip1 is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'slip1' is not supported in SDF version {target_version} (removed in 1.2)")
                if self.slip2 is not None and cmp_version(target_version, "1.2") >= 0:
                    raise ValueError(f"'slip2' is not supported in SDF version {target_version} (removed in 1.2)")
                kwargs = {"sdf_version": target_version}
                kwargs["fdir1"] = self.fdir1
                kwargs["mu"] = self.mu
                kwargs["mu2"] = self.mu2
                kwargs["slip1"] = self.slip1
                kwargs["slip2"] = self.slip2
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("ode")
                if self.fdir1 is not None:
                    el.set("fdir1", str(self.fdir1))
                if self.mu is not None:
                    el.set("mu", str(self.mu))
                if self.mu2 is not None:
                    el.set("mu2", str(self.mu2))
                if self.slip1 is not None:
                    el.set("slip1", str(self.slip1))
                if self.slip2 is not None:
                    el.set("slip2", str(self.slip2))
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Friction.FrictionOde | SDFError":
                _fdir1 = _parse_vector3(el.get("fdir1", "0 0 0"))
                if isinstance(_fdir1, SDFError):
                    return _fdir1.extend("@fdir1")
                _mu = _parse_double(el.get("mu", -1))
                if isinstance(_mu, SDFError):
                    return _mu.extend("@mu")
                _mu2 = _parse_double(el.get("mu2", -1))
                if isinstance(_mu2, SDFError):
                    return _mu2.extend("@mu2")
                _slip1 = _parse_double(el.get("slip1", 0.0))
                if isinstance(_slip1, SDFError):
                    return _slip1.extend("@slip1")
                _slip2 = _parse_double(el.get("slip2", 0.0))
                if isinstance(_slip2, SDFError):
                    return _slip2.extend("@slip2")
                return cls(sdf_version=version, fdir1=_fdir1, mu=_mu, mu2=_mu2, slip1=_slip1, slip2=_slip2)

        class Torsional(BaseModel):
            class TorsionalOde(BaseModel):
                def __init__(self, sdf_version: str | None = None, slip: float = 0.0):
                    super().__init__(sdf_version)
                    self.slip = slip

                def to_version(self, target_version: str) -> "Surface.Friction.Torsional.TorsionalOde":
                    kwargs = {"sdf_version": target_version}
                    kwargs["slip"] = self.slip
                    new_obj = self.__class__(**kwargs)
                    return new_obj

                def to_sdf(self, version: str | None = None) -> ET.Element:
                    if self.__version__ is None and version is not None:
                        self.__version__ = version
                    elif version is not None and version != self.__version__:
                        return self.to_version(version).to_sdf()
                    version = self.__version__ or version
                    el = ET.Element("ode")
                    if self.slip is not None:
                        _c_tmp = ET.Element("slip")
                        _c_tmp.text = str(self.slip)
                        el.append(_c_tmp)
                    return el

                @classmethod
                def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Friction.Torsional.TorsionalOde | SDFError":
                    _c_tmp = el.find("slip")
                    if _c_tmp is not None:
                        _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                        _val = _parse_double(_text)
                        if isinstance(_val, SDFError):
                            return _val.extend("slip")
                        _slip = _val
                    else:
                        _slip = None
                    return cls(sdf_version=version, slip=_slip)

            def __init__(
                self,
                sdf_version: str | None = None,
                coefficient: float = 1.0,
                ode: "Surface.Friction.Torsional.TorsionalOde" = None,
                patch_radius: float = 0,
                surface_radius: float = 0.0,
                use_patch_radius: bool = True
            ):
                super().__init__(sdf_version)
                self.coefficient = coefficient
                self.ode = ode
                self.patch_radius = patch_radius
                self.surface_radius = surface_radius
                self.use_patch_radius = use_patch_radius
                if self.ode is not None and hasattr(self.ode, 'to_version'):
                    if getattr(self.ode, '__version__', None) is None:
                        self.ode.__version__ = self.__version__
                    elif getattr(self.ode, '__version__', None) != self.__version__ and self.__version__ is not None:
                        self.ode = self.ode.to_version(self.__version__)

            def to_version(self, target_version: str) -> "Surface.Friction.Torsional":
                kwargs = {"sdf_version": target_version}
                kwargs["coefficient"] = self.coefficient
                kwargs["ode"] = self.ode.to_version(target_version) if hasattr(self.ode, "to_version") else self.ode
                kwargs["patch_radius"] = self.patch_radius
                kwargs["surface_radius"] = self.surface_radius
                kwargs["use_patch_radius"] = self.use_patch_radius
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("torsional")
                if self.coefficient is not None:
                    _c_tmp = ET.Element("coefficient")
                    _c_tmp.text = str(self.coefficient)
                    el.append(_c_tmp)
                if self.ode is not None:
                    if hasattr(self.ode, 'to_sdf'):
                        _child_res = self.ode.to_sdf(version)
                    else:
                        _child_res = str(self.ode)
                    if isinstance(_child_res, str):
                        _item_el = ET.Element('ode')
                        _item_el.text = _child_res
                    else:
                        _item_el = _child_res
                    el.append(_item_el)
                if self.patch_radius is not None:
                    _c_tmp = ET.Element("patch_radius")
                    _c_tmp.text = str(self.patch_radius)
                    el.append(_c_tmp)
                if self.surface_radius is not None:
                    _c_tmp = ET.Element("surface_radius")
                    _c_tmp.text = str(self.surface_radius)
                    el.append(_c_tmp)
                if self.use_patch_radius is not None:
                    _c_tmp = ET.Element("use_patch_radius")
                    _c_tmp.text = str(self.use_patch_radius).lower()
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Friction.Torsional | SDFError":
                _c_tmp = el.find("coefficient")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 1.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("coefficient")
                    _coefficient = _val
                else:
                    _coefficient = None
                _c_ode = el.find("ode")
                if _c_ode is not None:
                    _res = cls.TorsionalOde._from_sdf(_c_ode, version)
                    if isinstance(_res, SDFError):
                        return _res.extend("ode")
                    _ode = _res
                else:
                    _ode = None
                _c_tmp = el.find("patch_radius")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("patch_radius")
                    _patch_radius = _val
                else:
                    _patch_radius = None
                _c_tmp = el.find("surface_radius")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("surface_radius")
                    _surface_radius = _val
                else:
                    _surface_radius = None
                _c_tmp = el.find("use_patch_radius")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else True
                    _val = str(_text).strip().lower() == 'true'
                    if isinstance(_val, SDFError):
                        return _val.extend("use_patch_radius")
                    _use_patch_radius = _val
                else:
                    _use_patch_radius = None
                return cls(sdf_version=version, coefficient=_coefficient, ode=_ode, patch_radius=_patch_radius, surface_radius=_surface_radius, use_patch_radius=_use_patch_radius)

        def __init__(
            self,
            sdf_version: str | None = None,
            bullet: "Surface.Friction.FrictionBullet" = None,
            ode: "Surface.Friction.FrictionOde" = None,
            torsional: "Surface.Friction.Torsional" = None
        ):
            super().__init__(sdf_version)
            self.bullet = bullet
            self.ode = ode
            self.torsional = torsional
            if self.bullet is not None and hasattr(self.bullet, 'to_version'):
                if getattr(self.bullet, '__version__', None) is None:
                    self.bullet.__version__ = self.__version__
                elif getattr(self.bullet, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.bullet = self.bullet.to_version(self.__version__)
            if self.ode is not None and hasattr(self.ode, 'to_version'):
                if getattr(self.ode, '__version__', None) is None:
                    self.ode.__version__ = self.__version__
                elif getattr(self.ode, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.ode = self.ode.to_version(self.__version__)
            if self.torsional is not None and hasattr(self.torsional, 'to_version'):
                if getattr(self.torsional, '__version__', None) is None:
                    self.torsional.__version__ = self.__version__
                elif getattr(self.torsional, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.torsional = self.torsional.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Surface.Friction":
            if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
                raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
            if self.torsional is not None and cmp_version(target_version, "1.5") < 0:
                raise ValueError(f"'torsional' is not supported in SDF version {target_version} (added in 1.5)")
            kwargs = {"sdf_version": target_version}
            kwargs["bullet"] = self.bullet.to_version(target_version) if hasattr(self.bullet, "to_version") else self.bullet
            kwargs["ode"] = self.ode.to_version(target_version) if hasattr(self.ode, "to_version") else self.ode
            kwargs["torsional"] = self.torsional.to_version(target_version) if hasattr(self.torsional, "to_version") else self.torsional
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("friction")
            if self.bullet is not None:
                if hasattr(self.bullet, 'to_sdf'):
                    _child_res = self.bullet.to_sdf(version)
                else:
                    _child_res = str(self.bullet)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('bullet')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.ode is not None:
                if hasattr(self.ode, 'to_sdf'):
                    _child_res = self.ode.to_sdf(version)
                else:
                    _child_res = str(self.ode)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('ode')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            if self.torsional is not None:
                if hasattr(self.torsional, 'to_sdf'):
                    _child_res = self.torsional.to_sdf(version)
                else:
                    _child_res = str(self.torsional)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('torsional')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.Friction | SDFError":
            _c_bullet = el.find("bullet")
            if _c_bullet is not None:
                _res = cls.FrictionBullet._from_sdf(_c_bullet, version)
                if isinstance(_res, SDFError):
                    return _res.extend("bullet")
                _bullet = _res
            else:
                _bullet = None
            if _bullet is not None and cmp_version(version, "1.4") < 0:
                return SDFError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
            _c_ode = el.find("ode")
            if _c_ode is not None:
                _res = cls.FrictionOde._from_sdf(_c_ode, version)
                if isinstance(_res, SDFError):
                    return _res.extend("ode")
                _ode = _res
            else:
                _ode = None
            _c_torsional = el.find("torsional")
            if _c_torsional is not None:
                _res = cls.Torsional._from_sdf(_c_torsional, version)
                if isinstance(_res, SDFError):
                    return _res.extend("torsional")
                _torsional = _res
            else:
                _torsional = None
            if _torsional is not None and cmp_version(version, "1.5") < 0:
                return SDFError(f"'torsional' is not supported in SDF version {version} (added in 1.5)")
            return cls(sdf_version=version, bullet=_bullet, ode=_ode, torsional=_torsional)

    class SoftContact(BaseModel):
        class Dart(BaseModel):
            def __init__(
                self,
                sdf_version: str | None = None,
                bone_attachment: float = 100.0,
                damping: float = 10.0,
                flesh_mass_fraction: float = 0.05,
                stiffness: float = 100.0
            ):
                super().__init__(sdf_version)
                self.bone_attachment = bone_attachment
                self.damping = damping
                self.flesh_mass_fraction = flesh_mass_fraction
                self.stiffness = stiffness

            def to_version(self, target_version: str) -> "Surface.SoftContact.Dart":
                kwargs = {"sdf_version": target_version}
                kwargs["bone_attachment"] = self.bone_attachment
                kwargs["damping"] = self.damping
                kwargs["flesh_mass_fraction"] = self.flesh_mass_fraction
                kwargs["stiffness"] = self.stiffness
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("dart")
                if self.bone_attachment is not None:
                    _c_tmp = ET.Element("bone_attachment")
                    _c_tmp.text = str(self.bone_attachment)
                    el.append(_c_tmp)
                if self.damping is not None:
                    _c_tmp = ET.Element("damping")
                    _c_tmp.text = str(self.damping)
                    el.append(_c_tmp)
                if self.flesh_mass_fraction is not None:
                    _c_tmp = ET.Element("flesh_mass_fraction")
                    _c_tmp.text = str(self.flesh_mass_fraction)
                    el.append(_c_tmp)
                if self.stiffness is not None:
                    _c_tmp = ET.Element("stiffness")
                    _c_tmp.text = str(self.stiffness)
                    el.append(_c_tmp)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.SoftContact.Dart | SDFError":
                _c_tmp = el.find("bone_attachment")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 100.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("bone_attachment")
                    _bone_attachment = _val
                else:
                    _bone_attachment = None
                _c_tmp = el.find("damping")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 10.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("damping")
                    _damping = _val
                else:
                    _damping = None
                _c_tmp = el.find("flesh_mass_fraction")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 0.05
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("flesh_mass_fraction")
                    _flesh_mass_fraction = _val
                else:
                    _flesh_mass_fraction = None
                _c_tmp = el.find("stiffness")
                if _c_tmp is not None:
                    _text = _c_tmp.text if _c_tmp.text is not None else 100.0
                    _val = _parse_double(_text)
                    if isinstance(_val, SDFError):
                        return _val.extend("stiffness")
                    _stiffness = _val
                else:
                    _stiffness = None
                return cls(sdf_version=version, bone_attachment=_bone_attachment, damping=_damping, flesh_mass_fraction=_flesh_mass_fraction, stiffness=_stiffness)

        def __init__(self, sdf_version: str | None = None, dart: "Surface.SoftContact.Dart" = None):
            super().__init__(sdf_version)
            self.dart = dart
            if self.dart is not None and hasattr(self.dart, 'to_version'):
                if getattr(self.dart, '__version__', None) is None:
                    self.dart.__version__ = self.__version__
                elif getattr(self.dart, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.dart = self.dart.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Surface.SoftContact":
            kwargs = {"sdf_version": target_version}
            kwargs["dart"] = self.dart.to_version(target_version) if hasattr(self.dart, "to_version") else self.dart
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("soft_contact")
            if self.dart is not None:
                if hasattr(self.dart, 'to_sdf'):
                    _child_res = self.dart.to_sdf(version)
                else:
                    _child_res = str(self.dart)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('dart')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Surface.SoftContact | SDFError":
            _c_dart = el.find("dart")
            if _c_dart is not None:
                _res = cls.Dart._from_sdf(_c_dart, version)
                if isinstance(_res, SDFError):
                    return _res.extend("dart")
                _dart = _res
            else:
                _dart = None
            return cls(sdf_version=version, dart=_dart)

    def __init__(
        self,
        sdf_version: str | None = None,
        bounce: "Surface.Bounce" = None,
        contact: "Surface.Contact" = None,
        friction: "Surface.Friction" = None,
        soft_contact: "Surface.SoftContact" = None
    ):
        super().__init__(sdf_version)
        self.bounce = bounce
        self.contact = contact
        self.friction = friction
        self.soft_contact = soft_contact
        if self.bounce is not None and hasattr(self.bounce, 'to_version'):
            if getattr(self.bounce, '__version__', None) is None:
                self.bounce.__version__ = self.__version__
            elif getattr(self.bounce, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.bounce = self.bounce.to_version(self.__version__)
        if self.contact is not None and hasattr(self.contact, 'to_version'):
            if getattr(self.contact, '__version__', None) is None:
                self.contact.__version__ = self.__version__
            elif getattr(self.contact, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.contact = self.contact.to_version(self.__version__)
        if self.friction is not None and hasattr(self.friction, 'to_version'):
            if getattr(self.friction, '__version__', None) is None:
                self.friction.__version__ = self.__version__
            elif getattr(self.friction, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.friction = self.friction.to_version(self.__version__)
        if self.soft_contact is not None and hasattr(self.soft_contact, 'to_version'):
            if getattr(self.soft_contact, '__version__', None) is None:
                self.soft_contact.__version__ = self.__version__
            elif getattr(self.soft_contact, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.soft_contact = self.soft_contact.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Surface":
        if self.soft_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'soft_contact' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["bounce"] = self.bounce.to_version(target_version) if hasattr(self.bounce, "to_version") else self.bounce
        kwargs["contact"] = self.contact.to_version(target_version) if hasattr(self.contact, "to_version") else self.contact
        kwargs["friction"] = self.friction.to_version(target_version) if hasattr(self.friction, "to_version") else self.friction
        kwargs["soft_contact"] = self.soft_contact.to_version(target_version) if hasattr(self.soft_contact, "to_version") else self.soft_contact
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("surface")
        if self.bounce is not None:
            if hasattr(self.bounce, 'to_sdf'):
                _child_res = self.bounce.to_sdf(version)
            else:
                _child_res = str(self.bounce)
            if isinstance(_child_res, str):
                _item_el = ET.Element('bounce')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.contact is not None:
            if hasattr(self.contact, 'to_sdf'):
                _child_res = self.contact.to_sdf(version)
            else:
                _child_res = str(self.contact)
            if isinstance(_child_res, str):
                _item_el = ET.Element('contact')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.friction is not None:
            if hasattr(self.friction, 'to_sdf'):
                _child_res = self.friction.to_sdf(version)
            else:
                _child_res = str(self.friction)
            if isinstance(_child_res, str):
                _item_el = ET.Element('friction')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.soft_contact is not None:
            if hasattr(self.soft_contact, 'to_sdf'):
                _child_res = self.soft_contact.to_sdf(version)
            else:
                _child_res = str(self.soft_contact)
            if isinstance(_child_res, str):
                _item_el = ET.Element('soft_contact')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Surface | SDFError":
        _c_bounce = el.find("bounce")
        if _c_bounce is not None:
            _res = cls.Bounce._from_sdf(_c_bounce, version)
            if isinstance(_res, SDFError):
                return _res.extend("bounce")
            _bounce = _res
        else:
            _bounce = None
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = cls.Contact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _c_friction = el.find("friction")
        if _c_friction is not None:
            _res = cls.Friction._from_sdf(_c_friction, version)
            if isinstance(_res, SDFError):
                return _res.extend("friction")
            _friction = _res
        else:
            _friction = None
        _c_soft_contact = el.find("soft_contact")
        if _c_soft_contact is not None:
            _res = cls.SoftContact._from_sdf(_c_soft_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_contact")
            _soft_contact = _res
        else:
            _soft_contact = None
        if _soft_contact is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'soft_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, bounce=_bounce, contact=_contact, friction=_friction, soft_contact=_soft_contact)
