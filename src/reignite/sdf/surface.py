### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import Model
from ..utils.vector3 import Vector3
from ..utils.version import cmp_version


import math

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > math.inf:
        raise ValueError(f"double out of range: {raw}")
    return v



class RestitutionCoefficient(Model):
    def __init__(self, sdf_version: str, restitution_coefficient: float = 0):
        self.__version__ = sdf_version
        self.restitution_coefficient = restitution_coefficient

    def to_version(self, target_version: str) -> "RestitutionCoefficient":
        if self.restitution_coefficient is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'restitution_coefficient' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["restitution_coefficient"] = self.restitution_coefficient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("restitution_coefficient")
        if self.restitution_coefficient is not None:
            el.text = str(self.restitution_coefficient)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "RestitutionCoefficient":
        _text = el.text or 0
        _restitution_coefficient = _parse_double(_text)
        if _restitution_coefficient is not None and cmp_version(version, "1.2") < 0:
            if _restitution_coefficient != 0:
                raise ValueError(f"'restitution_coefficient' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient)


class Threshold(Model):
    def __init__(self, sdf_version: str, threshold: float = 100000):
        self.__version__ = sdf_version
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Threshold":
        if self.threshold is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'threshold' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["threshold"] = self.threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("threshold")
        if self.threshold is not None:
            el.text = str(self.threshold)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Threshold":
        _text = el.text or 100000
        _threshold = _parse_double(_text)
        if _threshold is not None and cmp_version(version, "1.2") < 0:
            if _threshold != 100000:
                raise ValueError(f"'threshold' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, threshold=_threshold)


class Bounce(Model):
    def __init__(
        self,
        sdf_version: str,
        restitution_coefficient: float = 0,
        threshold: float = 100000
    ):
        self.__version__ = sdf_version
        self.restitution_coefficient = restitution_coefficient
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Bounce":
        kwargs = {"sdf_version": target_version}
        kwargs["restitution_coefficient"] = self.restitution_coefficient
        kwargs["threshold"] = self.threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bounce")
        if self.restitution_coefficient is not None:
            el.set("restitution_coefficient", str(self.restitution_coefficient))
        if self.threshold is not None:
            el.set("threshold", str(self.threshold))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Bounce":
        _restitution_coefficient = _parse_double(el.get("restitution_coefficient", 0))
        _threshold = _parse_double(el.get("threshold", 100000))
        return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient, threshold=_threshold)


class Mu(Model):
    def __init__(self, sdf_version: str, mu: float = -1):
        self.__version__ = sdf_version
        self.mu = mu

    def to_version(self, target_version: str) -> "Mu":
        if self.mu is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'mu' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mu"] = self.mu
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mu")
        if self.mu is not None:
            el.text = str(self.mu)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mu":
        _text = el.text or -1
        _mu = _parse_double(_text)
        if _mu is not None and cmp_version(version, "1.2") < 0:
            if _mu != -1:
                raise ValueError(f"'mu' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mu=_mu)


class Mu2(Model):
    def __init__(self, sdf_version: str, mu2: float = -1):
        self.__version__ = sdf_version
        self.mu2 = mu2

    def to_version(self, target_version: str) -> "Mu2":
        if self.mu2 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'mu2' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mu2"] = self.mu2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mu2")
        if self.mu2 is not None:
            el.text = str(self.mu2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mu2":
        _text = el.text or -1
        _mu2 = _parse_double(_text)
        if _mu2 is not None and cmp_version(version, "1.2") < 0:
            if _mu2 != -1:
                raise ValueError(f"'mu2' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mu2=_mu2)


class Fdir1(Model):
    def __init__(self, sdf_version: str, fdir1: Vector3 = None):
        self.__version__ = sdf_version
        if fdir1 is None:
            fdir1 = Vector3.from_sdf("0 0 0")
        self.fdir1 = fdir1

    def to_version(self, target_version: str) -> "Fdir1":
        if self.fdir1 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'fdir1' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["fdir1"] = self.fdir1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fdir1")
        if self.fdir1 is not None:
            el.text = self.fdir1.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fdir1":
        _text = el.text or "0 0 0"
        _fdir1 = Vector3.from_sdf(_text)
        if _fdir1 is not None and cmp_version(version, "1.2") < 0:
            if _fdir1 != "0 0 0":
                raise ValueError(f"'fdir1' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, fdir1=_fdir1)


class Slip1(Model):
    def __init__(self, sdf_version: str, slip1: float = 0.0):
        self.__version__ = sdf_version
        self.slip1 = slip1

    def to_version(self, target_version: str) -> "Slip1":
        if self.slip1 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'slip1' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["slip1"] = self.slip1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("slip1")
        if self.slip1 is not None:
            el.text = str(self.slip1)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Slip1":
        _text = el.text or 0.0
        _slip1 = _parse_double(_text)
        if _slip1 is not None and cmp_version(version, "1.2") < 0:
            if _slip1 != 0.0:
                raise ValueError(f"'slip1' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, slip1=_slip1)


class Slip2(Model):
    def __init__(self, sdf_version: str, slip2: float = 0.0):
        self.__version__ = sdf_version
        self.slip2 = slip2

    def to_version(self, target_version: str) -> "Slip2":
        if self.slip2 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'slip2' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["slip2"] = self.slip2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("slip2")
        if self.slip2 is not None:
            el.text = str(self.slip2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Slip2":
        _text = el.text or 0.0
        _slip2 = _parse_double(_text)
        if _slip2 is not None and cmp_version(version, "1.2") < 0:
            if _slip2 != 0.0:
                raise ValueError(f"'slip2' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, slip2=_slip2)


class Ode(Model):
    def __init__(
        self,
        sdf_version: str,
        mu: float = -1,
        mu2: float = -1,
        fdir1: Vector3 = None,
        slip1: float = 0.0,
        slip2: float = 0.0
    ):
        self.__version__ = sdf_version
        if fdir1 is None:
            fdir1 = Vector3.from_sdf("0 0 0")
        self.mu = mu
        self.mu2 = mu2
        self.fdir1 = fdir1
        self.slip1 = slip1
        self.slip2 = slip2

    def to_version(self, target_version: str) -> "Ode":
        kwargs = {"sdf_version": target_version}
        kwargs["mu"] = self.mu
        kwargs["mu2"] = self.mu2
        kwargs["fdir1"] = self.fdir1
        kwargs["slip1"] = self.slip1
        kwargs["slip2"] = self.slip2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.mu is not None:
            el.set("mu", str(self.mu))
        if self.mu2 is not None:
            el.set("mu2", str(self.mu2))
        if self.fdir1 is not None:
            el.set("fdir1", self.fdir1.to_sdf())
        if self.slip1 is not None:
            el.set("slip1", str(self.slip1))
        if self.slip2 is not None:
            el.set("slip2", str(self.slip2))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ode":
        _mu = _parse_double(el.get("mu", -1))
        _mu2 = _parse_double(el.get("mu2", -1))
        _fdir1 = Vector3.from_sdf(el.get("fdir1", "0 0 0"))
        _slip1 = _parse_double(el.get("slip1", 0.0))
        _slip2 = _parse_double(el.get("slip2", 0.0))
        return cls(sdf_version=version, mu=_mu, mu2=_mu2, fdir1=_fdir1, slip1=_slip1, slip2=_slip2)


class Friction2(Model):
    def __init__(self, sdf_version: str, friction2: float = 1):
        self.__version__ = sdf_version
        self.friction2 = friction2

    def to_version(self, target_version: str) -> "Friction2":
        kwargs = {"sdf_version": target_version}
        kwargs["friction2"] = self.friction2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction2")
        if self.friction2 is not None:
            el.text = str(self.friction2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Friction2":
        _text = el.text or 1
        _friction2 = _parse_double(_text)
        return cls(sdf_version=version, friction2=_friction2)


class RollingFriction(Model):
    def __init__(self, sdf_version: str, rolling_friction: float = 1):
        self.__version__ = sdf_version
        self.rolling_friction = rolling_friction

    def to_version(self, target_version: str) -> "RollingFriction":
        kwargs = {"sdf_version": target_version}
        kwargs["rolling_friction"] = self.rolling_friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rolling_friction")
        if self.rolling_friction is not None:
            el.text = str(self.rolling_friction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "RollingFriction":
        _text = el.text or 1
        _rolling_friction = _parse_double(_text)
        return cls(sdf_version=version, rolling_friction=_rolling_friction)


class Bullet(Model):
    def __init__(
        self,
        sdf_version: str,
        friction: "Friction" = None,
        friction2: "Friction2" = None,
        fdir1: "Fdir1" = None,
        rolling_friction: "RollingFriction" = None
    ):
        self.__version__ = sdf_version
        self.friction = friction
        self.friction2 = friction2
        self.fdir1 = fdir1
        self.rolling_friction = rolling_friction

    def to_version(self, target_version: str) -> "Bullet":
        kwargs = {"sdf_version": target_version}
        kwargs["friction"] = self.friction.to_version(target_version) if self.friction is not None else None
        kwargs["friction2"] = self.friction2.to_version(target_version) if self.friction2 is not None else None
        kwargs["fdir1"] = self.fdir1.to_version(target_version) if self.fdir1 is not None else None
        kwargs["rolling_friction"] = self.rolling_friction.to_version(target_version) if self.rolling_friction is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bullet")
        if self.friction is not None:
            el.append(self.friction.to_sdf(version))
        if self.friction2 is not None:
            el.append(self.friction2.to_sdf(version))
        if self.fdir1 is not None:
            el.append(self.fdir1.to_sdf(version))
        if self.rolling_friction is not None:
            el.append(self.rolling_friction.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Bullet":
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction, version) if _c_friction is not None else None
        _c_friction2 = el.find("friction2")
        _friction2 = Friction2.from_sdf(_c_friction2, version) if _c_friction2 is not None else None
        _c_fdir1 = el.find("fdir1")
        _fdir1 = Fdir1.from_sdf(_c_fdir1, version) if _c_fdir1 is not None else None
        _c_rolling_friction = el.find("rolling_friction")
        _rolling_friction = RollingFriction.from_sdf(_c_rolling_friction, version) if _c_rolling_friction is not None else None
        return cls(sdf_version=version, friction=_friction, friction2=_friction2, fdir1=_fdir1, rolling_friction=_rolling_friction)


class Coefficient(Model):
    def __init__(self, sdf_version: str, coefficient: float = 1.0):
        self.__version__ = sdf_version
        self.coefficient = coefficient

    def to_version(self, target_version: str) -> "Coefficient":
        kwargs = {"sdf_version": target_version}
        kwargs["coefficient"] = self.coefficient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("coefficient")
        if self.coefficient is not None:
            el.text = str(self.coefficient)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Coefficient":
        _text = el.text or 1.0
        _coefficient = _parse_double(_text)
        return cls(sdf_version=version, coefficient=_coefficient)


class UsePatchRadius(Model):
    def __init__(self, sdf_version: str, use_patch_radius: bool = True):
        self.__version__ = sdf_version
        self.use_patch_radius = use_patch_radius

    def to_version(self, target_version: str) -> "UsePatchRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["use_patch_radius"] = self.use_patch_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("use_patch_radius")
        if self.use_patch_radius is not None:
            el.text = str(self.use_patch_radius).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "UsePatchRadius":
        _text = el.text or True
        _use_patch_radius = _text.strip().lower() == 'true'
        return cls(sdf_version=version, use_patch_radius=_use_patch_radius)


class PatchRadius(Model):
    def __init__(self, sdf_version: str, patch_radius: float = 0):
        self.__version__ = sdf_version
        self.patch_radius = patch_radius

    def to_version(self, target_version: str) -> "PatchRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["patch_radius"] = self.patch_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("patch_radius")
        if self.patch_radius is not None:
            el.text = str(self.patch_radius)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PatchRadius":
        _text = el.text or 0
        _patch_radius = _parse_double(_text)
        return cls(sdf_version=version, patch_radius=_patch_radius)


class SurfaceRadius(Model):
    def __init__(self, sdf_version: str, surface_radius: float = 0.0):
        self.__version__ = sdf_version
        self.surface_radius = surface_radius

    def to_version(self, target_version: str) -> "SurfaceRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["surface_radius"] = self.surface_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface_radius")
        if self.surface_radius is not None:
            el.text = str(self.surface_radius)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SurfaceRadius":
        _text = el.text or 0.0
        _surface_radius = _parse_double(_text)
        return cls(sdf_version=version, surface_radius=_surface_radius)


class Torsional(Model):
    def __init__(
        self,
        sdf_version: str,
        coefficient: "Coefficient" = None,
        use_patch_radius: "UsePatchRadius" = None,
        patch_radius: "PatchRadius" = None,
        surface_radius: "SurfaceRadius" = None,
        ode: "Ode" = None
    ):
        self.__version__ = sdf_version
        self.coefficient = coefficient
        self.use_patch_radius = use_patch_radius
        self.patch_radius = patch_radius
        self.surface_radius = surface_radius
        self.ode = ode

    def to_version(self, target_version: str) -> "Torsional":
        kwargs = {"sdf_version": target_version}
        kwargs["coefficient"] = self.coefficient.to_version(target_version) if self.coefficient is not None else None
        kwargs["use_patch_radius"] = self.use_patch_radius.to_version(target_version) if self.use_patch_radius is not None else None
        kwargs["patch_radius"] = self.patch_radius.to_version(target_version) if self.patch_radius is not None else None
        kwargs["surface_radius"] = self.surface_radius.to_version(target_version) if self.surface_radius is not None else None
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("torsional")
        if self.coefficient is not None:
            el.append(self.coefficient.to_sdf(version))
        if self.use_patch_radius is not None:
            el.append(self.use_patch_radius.to_sdf(version))
        if self.patch_radius is not None:
            el.append(self.patch_radius.to_sdf(version))
        if self.surface_radius is not None:
            el.append(self.surface_radius.to_sdf(version))
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Torsional":
        _c_coefficient = el.find("coefficient")
        _coefficient = Coefficient.from_sdf(_c_coefficient, version) if _c_coefficient is not None else None
        _c_use_patch_radius = el.find("use_patch_radius")
        _use_patch_radius = UsePatchRadius.from_sdf(_c_use_patch_radius, version) if _c_use_patch_radius is not None else None
        _c_patch_radius = el.find("patch_radius")
        _patch_radius = PatchRadius.from_sdf(_c_patch_radius, version) if _c_patch_radius is not None else None
        _c_surface_radius = el.find("surface_radius")
        _surface_radius = SurfaceRadius.from_sdf(_c_surface_radius, version) if _c_surface_radius is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        return cls(sdf_version=version, coefficient=_coefficient, use_patch_radius=_use_patch_radius, patch_radius=_patch_radius, surface_radius=_surface_radius, ode=_ode)


class Friction(Model):
    def __init__(
        self,
        sdf_version: str,
        ode: "Ode" = None,
        bullet: "Bullet" = None,
        torsional: "Torsional" = None
    ):
        self.__version__ = sdf_version
        self.ode = ode
        self.bullet = bullet
        self.torsional = torsional

    def to_version(self, target_version: str) -> "Friction":
        if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
        if self.torsional is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'torsional' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["torsional"] = self.torsional.to_version(target_version) if self.torsional is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.torsional is not None:
            el.append(self.torsional.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Friction":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet, version) if _c_bullet is not None else None
        if _bullet is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
        _c_torsional = el.find("torsional")
        _torsional = Torsional.from_sdf(_c_torsional, version) if _c_torsional is not None else None
        if _torsional is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'torsional' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, ode=_ode, bullet=_bullet, torsional=_torsional)


class CollideWithoutContact(Model):
    def __init__(self, sdf_version: str, collide_without_contact: bool = False):
        self.__version__ = sdf_version
        self.collide_without_contact = collide_without_contact

    def to_version(self, target_version: str) -> "CollideWithoutContact":
        if self.collide_without_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_without_contact"] = self.collide_without_contact
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_without_contact")
        if self.collide_without_contact is not None:
            el.text = str(self.collide_without_contact).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CollideWithoutContact":
        _text = el.text or False
        _collide_without_contact = _text.strip().lower() == 'true'
        if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
            if _collide_without_contact != False:
                raise ValueError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_without_contact=_collide_without_contact)


class CollideWithoutContactBitmask(Model):
    def __init__(self, sdf_version: str, collide_without_contact_bitmask: int = 1):
        self.__version__ = sdf_version
        self.collide_without_contact_bitmask = collide_without_contact_bitmask

    def to_version(self, target_version: str) -> "CollideWithoutContactBitmask":
        if self.collide_without_contact_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_without_contact_bitmask"] = self.collide_without_contact_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_without_contact_bitmask")
        if self.collide_without_contact_bitmask is not None:
            el.text = str(self.collide_without_contact_bitmask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CollideWithoutContactBitmask":
        _text = el.text or 1
        _collide_without_contact_bitmask = _parse_uint32(_text)
        if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
            if _collide_without_contact_bitmask != 1:
                raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_without_contact_bitmask=_collide_without_contact_bitmask)


class CollideBitmask(Model):
    def __init__(self, sdf_version: str, collide_bitmask: int = 1):
        self.__version__ = sdf_version
        self.collide_bitmask = collide_bitmask

    def to_version(self, target_version: str) -> "CollideBitmask":
        if self.collide_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_bitmask"] = self.collide_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_bitmask")
        if self.collide_bitmask is not None:
            el.text = str(self.collide_bitmask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CollideBitmask":
        _text = el.text or 1
        _collide_bitmask = _parse_uint32(_text)
        if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
            if _collide_bitmask != 1:
                raise ValueError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_bitmask=_collide_bitmask)


class PoissonsRatio(Model):
    def __init__(self, sdf_version: str, poissons_ratio: float = 0.3):
        self.__version__ = sdf_version
        self.poissons_ratio = poissons_ratio

    def to_version(self, target_version: str) -> "PoissonsRatio":
        if self.poissons_ratio is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["poissons_ratio"] = self.poissons_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("poissons_ratio")
        if self.poissons_ratio is not None:
            el.text = str(self.poissons_ratio)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PoissonsRatio":
        _text = el.text or 0.3
        _poissons_ratio = _parse_double(_text)
        if _poissons_ratio is not None and cmp_version(version, "1.5") < 0:
            if _poissons_ratio != 0.3:
                raise ValueError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, poissons_ratio=_poissons_ratio)


class ElasticModulus(Model):
    def __init__(self, sdf_version: str, elastic_modulus: float = -1):
        self.__version__ = sdf_version
        self.elastic_modulus = elastic_modulus

    def to_version(self, target_version: str) -> "ElasticModulus":
        if self.elastic_modulus is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["elastic_modulus"] = self.elastic_modulus
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("elastic_modulus")
        if self.elastic_modulus is not None:
            el.text = str(self.elastic_modulus)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ElasticModulus":
        _text = el.text or -1
        _elastic_modulus = _parse_double(_text)
        if _elastic_modulus is not None and cmp_version(version, "1.5") < 0:
            if _elastic_modulus != -1:
                raise ValueError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, elastic_modulus=_elastic_modulus)


class CategoryBitmask(Model):
    def __init__(self, sdf_version: str, category_bitmask: int = 65535):
        self.__version__ = sdf_version
        self.category_bitmask = category_bitmask

    def to_version(self, target_version: str) -> "CategoryBitmask":
        if self.category_bitmask is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["category_bitmask"] = self.category_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("category_bitmask")
        if self.category_bitmask is not None:
            el.text = str(self.category_bitmask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CategoryBitmask":
        _text = el.text or 65535
        _category_bitmask = _parse_uint32(_text)
        if _category_bitmask is not None and cmp_version(version, "1.6") < 0:
            if _category_bitmask != 65535:
                raise ValueError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, category_bitmask=_category_bitmask)


class Contact(Model):
    def __init__(
        self,
        sdf_version: str,
        ode: "Ode" = None,
        collide_without_contact: "CollideWithoutContact" = None,
        collide_without_contact_bitmask: "CollideWithoutContactBitmask" = None,
        collide_bitmask: "CollideBitmask" = None,
        bullet: "Bullet" = None,
        poissons_ratio: "PoissonsRatio" = None,
        elastic_modulus: "ElasticModulus" = None,
        category_bitmask: "CategoryBitmask" = None
    ):
        self.__version__ = sdf_version
        self.ode = ode
        self.collide_without_contact = collide_without_contact
        self.collide_without_contact_bitmask = collide_without_contact_bitmask
        self.collide_bitmask = collide_bitmask
        self.bullet = bullet
        self.poissons_ratio = poissons_ratio
        self.elastic_modulus = elastic_modulus
        self.category_bitmask = category_bitmask

    def to_version(self, target_version: str) -> "Contact":
        if self.collide_without_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {target_version} (added in 1.4)")
        if self.collide_without_contact_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        if self.collide_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
        if self.poissons_ratio is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.5)")
        if self.elastic_modulus is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.5)")
        if self.category_bitmask is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["collide_without_contact"] = self.collide_without_contact.to_version(target_version) if self.collide_without_contact is not None else None
        kwargs["collide_without_contact_bitmask"] = self.collide_without_contact_bitmask.to_version(target_version) if self.collide_without_contact_bitmask is not None else None
        kwargs["collide_bitmask"] = self.collide_bitmask.to_version(target_version) if self.collide_bitmask is not None else None
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["poissons_ratio"] = self.poissons_ratio.to_version(target_version) if self.poissons_ratio is not None else None
        kwargs["elastic_modulus"] = self.elastic_modulus.to_version(target_version) if self.elastic_modulus is not None else None
        kwargs["category_bitmask"] = self.category_bitmask.to_version(target_version) if self.category_bitmask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.collide_without_contact is not None:
            el.append(self.collide_without_contact.to_sdf(version))
        if self.collide_without_contact_bitmask is not None:
            el.append(self.collide_without_contact_bitmask.to_sdf(version))
        if self.collide_bitmask is not None:
            el.append(self.collide_bitmask.to_sdf(version))
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.poissons_ratio is not None:
            el.append(self.poissons_ratio.to_sdf(version))
        if self.elastic_modulus is not None:
            el.append(self.elastic_modulus.to_sdf(version))
        if self.category_bitmask is not None:
            el.append(self.category_bitmask.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Contact":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        _c_collide_without_contact = el.find("collide_without_contact")
        _collide_without_contact = CollideWithoutContact.from_sdf(_c_collide_without_contact, version) if _c_collide_without_contact is not None else None
        if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
        _c_collide_without_contact_bitmask = el.find("collide_without_contact_bitmask")
        _collide_without_contact_bitmask = CollideWithoutContactBitmask.from_sdf(_c_collide_without_contact_bitmask, version) if _c_collide_without_contact_bitmask is not None else None
        if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
        _c_collide_bitmask = el.find("collide_bitmask")
        _collide_bitmask = CollideBitmask.from_sdf(_c_collide_bitmask, version) if _c_collide_bitmask is not None else None
        if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet, version) if _c_bullet is not None else None
        if _bullet is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
        _c_poissons_ratio = el.find("poissons_ratio")
        _poissons_ratio = PoissonsRatio.from_sdf(_c_poissons_ratio, version) if _c_poissons_ratio is not None else None
        if _poissons_ratio is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.5)")
        _c_elastic_modulus = el.find("elastic_modulus")
        _elastic_modulus = ElasticModulus.from_sdf(_c_elastic_modulus, version) if _c_elastic_modulus is not None else None
        if _elastic_modulus is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.5)")
        _c_category_bitmask = el.find("category_bitmask")
        _category_bitmask = CategoryBitmask.from_sdf(_c_category_bitmask, version) if _c_category_bitmask is not None else None
        if _category_bitmask is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, ode=_ode, collide_without_contact=_collide_without_contact, collide_without_contact_bitmask=_collide_without_contact_bitmask, collide_bitmask=_collide_bitmask, bullet=_bullet, poissons_ratio=_poissons_ratio, elastic_modulus=_elastic_modulus, category_bitmask=_category_bitmask)


class BoneAttachment(Model):
    def __init__(self, sdf_version: str, bone_attachment: float = 100.0):
        self.__version__ = sdf_version
        self.bone_attachment = bone_attachment

    def to_version(self, target_version: str) -> "BoneAttachment":
        kwargs = {"sdf_version": target_version}
        kwargs["bone_attachment"] = self.bone_attachment
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bone_attachment")
        if self.bone_attachment is not None:
            el.text = str(self.bone_attachment)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "BoneAttachment":
        _text = el.text or 100.0
        _bone_attachment = _parse_double(_text)
        return cls(sdf_version=version, bone_attachment=_bone_attachment)


class Stiffness(Model):
    def __init__(self, sdf_version: str, stiffness: float = 100.0):
        self.__version__ = sdf_version
        self.stiffness = stiffness

    def to_version(self, target_version: str) -> "Stiffness":
        kwargs = {"sdf_version": target_version}
        kwargs["stiffness"] = self.stiffness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("stiffness")
        if self.stiffness is not None:
            el.text = str(self.stiffness)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Stiffness":
        _text = el.text or 100.0
        _stiffness = _parse_double(_text)
        return cls(sdf_version=version, stiffness=_stiffness)


class Damping(Model):
    def __init__(self, sdf_version: str, damping: float = 10.0):
        self.__version__ = sdf_version
        self.damping = damping

    def to_version(self, target_version: str) -> "Damping":
        kwargs = {"sdf_version": target_version}
        kwargs["damping"] = self.damping
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("damping")
        if self.damping is not None:
            el.text = str(self.damping)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Damping":
        _text = el.text or 10.0
        _damping = _parse_double(_text)
        return cls(sdf_version=version, damping=_damping)


class FleshMassFraction(Model):
    def __init__(self, sdf_version: str, flesh_mass_fraction: float = 0.05):
        self.__version__ = sdf_version
        self.flesh_mass_fraction = flesh_mass_fraction

    def to_version(self, target_version: str) -> "FleshMassFraction":
        kwargs = {"sdf_version": target_version}
        kwargs["flesh_mass_fraction"] = self.flesh_mass_fraction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("flesh_mass_fraction")
        if self.flesh_mass_fraction is not None:
            el.text = str(self.flesh_mass_fraction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "FleshMassFraction":
        _text = el.text or 0.05
        _flesh_mass_fraction = _parse_double(_text)
        return cls(sdf_version=version, flesh_mass_fraction=_flesh_mass_fraction)


class Dart(Model):
    def __init__(
        self,
        sdf_version: str,
        bone_attachment: "BoneAttachment" = None,
        stiffness: "Stiffness" = None,
        damping: "Damping" = None,
        flesh_mass_fraction: "FleshMassFraction" = None
    ):
        self.__version__ = sdf_version
        self.bone_attachment = bone_attachment
        self.stiffness = stiffness
        self.damping = damping
        self.flesh_mass_fraction = flesh_mass_fraction

    def to_version(self, target_version: str) -> "Dart":
        kwargs = {"sdf_version": target_version}
        kwargs["bone_attachment"] = self.bone_attachment.to_version(target_version) if self.bone_attachment is not None else None
        kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
        kwargs["damping"] = self.damping.to_version(target_version) if self.damping is not None else None
        kwargs["flesh_mass_fraction"] = self.flesh_mass_fraction.to_version(target_version) if self.flesh_mass_fraction is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dart")
        if self.bone_attachment is not None:
            el.append(self.bone_attachment.to_sdf(version))
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        if self.damping is not None:
            el.append(self.damping.to_sdf(version))
        if self.flesh_mass_fraction is not None:
            el.append(self.flesh_mass_fraction.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Dart":
        _c_bone_attachment = el.find("bone_attachment")
        _bone_attachment = BoneAttachment.from_sdf(_c_bone_attachment, version) if _c_bone_attachment is not None else None
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness, version) if _c_stiffness is not None else None
        _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping, version) if _c_damping is not None else None
        _c_flesh_mass_fraction = el.find("flesh_mass_fraction")
        _flesh_mass_fraction = FleshMassFraction.from_sdf(_c_flesh_mass_fraction, version) if _c_flesh_mass_fraction is not None else None
        return cls(sdf_version=version, bone_attachment=_bone_attachment, stiffness=_stiffness, damping=_damping, flesh_mass_fraction=_flesh_mass_fraction)


class SoftContact(Model):
    def __init__(self, sdf_version: str, dart: "Dart" = None):
        self.__version__ = sdf_version
        self.dart = dart

    def to_version(self, target_version: str) -> "SoftContact":
        kwargs = {"sdf_version": target_version}
        kwargs["dart"] = self.dart.to_version(target_version) if self.dart is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("soft_contact")
        if self.dart is not None:
            el.append(self.dart.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SoftContact":
        _c_dart = el.find("dart")
        _dart = Dart.from_sdf(_c_dart, version) if _c_dart is not None else None
        return cls(sdf_version=version, dart=_dart)


class Surface(Model):
    def __init__(
        self,
        sdf_version: str,
        bounce: "Bounce" = None,
        friction: "Friction" = None,
        contact: "Contact" = None,
        soft_contact: "SoftContact" = None
    ):
        self.__version__ = sdf_version
        self.bounce = bounce
        self.friction = friction
        self.contact = contact
        self.soft_contact = soft_contact

    def to_version(self, target_version: str) -> "Surface":
        if self.soft_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'soft_contact' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["bounce"] = self.bounce.to_version(target_version) if self.bounce is not None else None
        kwargs["friction"] = self.friction.to_version(target_version) if self.friction is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["soft_contact"] = self.soft_contact.to_version(target_version) if self.soft_contact is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface")
        if self.bounce is not None:
            el.append(self.bounce.to_sdf(version))
        if self.friction is not None:
            el.append(self.friction.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        if self.soft_contact is not None:
            el.append(self.soft_contact.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Surface":
        _c_bounce = el.find("bounce")
        _bounce = Bounce.from_sdf(_c_bounce, version) if _c_bounce is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction, version) if _c_friction is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact, version) if _c_contact is not None else None
        _c_soft_contact = el.find("soft_contact")
        _soft_contact = SoftContact.from_sdf(_c_soft_contact, version) if _c_soft_contact is not None else None
        if _soft_contact is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'soft_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, bounce=_bounce, friction=_friction, contact=_contact, soft_contact=_soft_contact)
