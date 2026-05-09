### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import Model
from ..utils.pose import Pose
from ..utils.vector2d import Vector2d
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



class Parent(Model):
    def __init__(self, sdf_version: str, parent: str = "__default__", link: str = "__default__"):
        self.__version__ = sdf_version
        self.parent = parent
        self.link = link

    def to_version(self, target_version: str) -> "Parent":
        kwargs = {"sdf_version": target_version}
        kwargs["parent"] = self.parent
        kwargs["link"] = self.link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("parent")
        if self.parent is not None:
            el.text = self.parent
        if self.link is not None:
            el.set("link", self.link)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Parent":
        _text = el.text or "__default__"
        _parent = _text
        _link = el.get("link", "__default__")
        return cls(sdf_version=version, parent=_parent, link=_link)


class Child(Model):
    def __init__(self, sdf_version: str, child: str = "__default__", link: str = "__default__"):
        self.__version__ = sdf_version
        self.child = child
        self.link = link

    def to_version(self, target_version: str) -> "Child":
        kwargs = {"sdf_version": target_version}
        kwargs["child"] = self.child
        kwargs["link"] = self.link
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("child")
        if self.child is not None:
            el.text = self.child
        if self.link is not None:
            el.set("link", self.link)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Child":
        _text = el.text or "__default__"
        _child = _text
        _link = el.get("link", "__default__")
        return cls(sdf_version=version, child=_child, link=_link)


class Origin(Model):
    def __init__(self, sdf_version: str, pose: Pose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "Origin":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("origin")
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Origin":
        _pose = Pose.from_sdf(el.get("pose", "0 0 0 0 0 0"))
        return cls(sdf_version=version, pose=_pose)


class ThreadPitch(Model):
    def __init__(self, sdf_version: str, thread_pitch: float = 1.0):
        self.__version__ = sdf_version
        self.thread_pitch = thread_pitch

    def to_version(self, target_version: str) -> "ThreadPitch":
        kwargs = {"sdf_version": target_version}
        kwargs["thread_pitch"] = self.thread_pitch
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("thread_pitch")
        if self.thread_pitch is not None:
            el.text = str(self.thread_pitch)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ThreadPitch":
        _text = el.text or 1.0
        _thread_pitch = _parse_double(_text)
        return cls(sdf_version=version, thread_pitch=_thread_pitch)


class Damping(Model):
    def __init__(self, sdf_version: str, damping: float = 0):
        self.__version__ = sdf_version
        self.damping = damping

    def to_version(self, target_version: str) -> "Damping":
        if self.damping is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'damping' is not supported in SDF version {target_version} (added in 1.2)")
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
        _text = el.text or 0
        _damping = _parse_double(_text)
        if _damping is not None and cmp_version(version, "1.2") < 0:
            if _damping != 0:
                raise ValueError(f"'damping' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, damping=_damping)


class Friction(Model):
    def __init__(self, sdf_version: str, friction: float = 0):
        self.__version__ = sdf_version
        self.friction = friction

    def to_version(self, target_version: str) -> "Friction":
        if self.friction is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'friction' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["friction"] = self.friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction")
        if self.friction is not None:
            el.text = str(self.friction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Friction":
        _text = el.text or 0
        _friction = _parse_double(_text)
        if _friction is not None and cmp_version(version, "1.2") < 0:
            if _friction != 0:
                raise ValueError(f"'friction' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, friction=_friction)


class SpringReference(Model):
    def __init__(self, sdf_version: str, spring_reference: float = 0):
        self.__version__ = sdf_version
        self.spring_reference = spring_reference

    def to_version(self, target_version: str) -> "SpringReference":
        if self.spring_reference is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["spring_reference"] = self.spring_reference
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spring_reference")
        if self.spring_reference is not None:
            el.text = str(self.spring_reference)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SpringReference":
        _text = el.text or 0
        _spring_reference = _parse_double(_text)
        if _spring_reference is not None and cmp_version(version, "1.5") < 0:
            if _spring_reference != 0:
                raise ValueError(f"'spring_reference' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, spring_reference=_spring_reference)


class SpringStiffness(Model):
    def __init__(self, sdf_version: str, spring_stiffness: float = 0):
        self.__version__ = sdf_version
        self.spring_stiffness = spring_stiffness

    def to_version(self, target_version: str) -> "SpringStiffness":
        if self.spring_stiffness is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["spring_stiffness"] = self.spring_stiffness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("spring_stiffness")
        if self.spring_stiffness is not None:
            el.text = str(self.spring_stiffness)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SpringStiffness":
        _text = el.text or 0
        _spring_stiffness = _parse_double(_text)
        if _spring_stiffness is not None and cmp_version(version, "1.5") < 0:
            if _spring_stiffness != 0:
                raise ValueError(f"'spring_stiffness' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, spring_stiffness=_spring_stiffness)


class Dynamics(Model):
    def __init__(
        self,
        sdf_version: str,
        damping: float = 0,
        friction: float = 0,
        spring_reference: "SpringReference" = None,
        spring_stiffness: "SpringStiffness" = None
    ):
        self.__version__ = sdf_version
        self.damping = damping
        self.friction = friction
        self.spring_reference = spring_reference
        self.spring_stiffness = spring_stiffness

    def to_version(self, target_version: str) -> "Dynamics":
        if self.spring_reference is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {target_version} (added in 1.5)")
        if self.spring_stiffness is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["damping"] = self.damping
        kwargs["friction"] = self.friction
        kwargs["spring_reference"] = self.spring_reference.to_version(target_version) if self.spring_reference is not None else None
        kwargs["spring_stiffness"] = self.spring_stiffness.to_version(target_version) if self.spring_stiffness is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dynamics")
        if self.damping is not None:
            el.set("damping", str(self.damping))
        if self.friction is not None:
            el.set("friction", str(self.friction))
        if self.spring_reference is not None:
            el.append(self.spring_reference.to_sdf(version))
        if self.spring_stiffness is not None:
            el.append(self.spring_stiffness.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Dynamics":
        _damping = _parse_double(el.get("damping", 0))
        _friction = _parse_double(el.get("friction", 0))
        _c_spring_reference = el.find("spring_reference")
        _spring_reference = SpringReference.from_sdf(_c_spring_reference, version) if _c_spring_reference is not None else None
        if _spring_reference is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'spring_reference' is not supported in SDF version {version} (added in 1.5)")
        _c_spring_stiffness = el.find("spring_stiffness")
        _spring_stiffness = SpringStiffness.from_sdf(_c_spring_stiffness, version) if _c_spring_stiffness is not None else None
        if _spring_stiffness is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'spring_stiffness' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, damping=_damping, friction=_friction, spring_reference=_spring_reference, spring_stiffness=_spring_stiffness)


class Lower(Model):
    def __init__(self, sdf_version: str, lower: float = -1e16):
        self.__version__ = sdf_version
        self.lower = lower

    def to_version(self, target_version: str) -> "Lower":
        if self.lower is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'lower' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["lower"] = self.lower
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lower")
        if self.lower is not None:
            el.text = str(self.lower)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Lower":
        _text = el.text or -1e16
        _lower = _parse_double(_text)
        if _lower is not None and cmp_version(version, "1.2") < 0:
            if _lower != -1e16:
                raise ValueError(f"'lower' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, lower=_lower)


class Upper(Model):
    def __init__(self, sdf_version: str, upper: float = 1e16):
        self.__version__ = sdf_version
        self.upper = upper

    def to_version(self, target_version: str) -> "Upper":
        if self.upper is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'upper' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["upper"] = self.upper
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("upper")
        if self.upper is not None:
            el.text = str(self.upper)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Upper":
        _text = el.text or 1e16
        _upper = _parse_double(_text)
        if _upper is not None and cmp_version(version, "1.2") < 0:
            if _upper != 1e16:
                raise ValueError(f"'upper' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, upper=_upper)


class Effort(Model):
    def __init__(self, sdf_version: str, effort: float = 0):
        self.__version__ = sdf_version
        self.effort = effort

    def to_version(self, target_version: str) -> "Effort":
        if self.effort is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'effort' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["effort"] = self.effort
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("effort")
        if self.effort is not None:
            el.text = str(self.effort)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Effort":
        _text = el.text or 0
        _effort = _parse_double(_text)
        if _effort is not None and cmp_version(version, "1.2") < 0:
            if _effort != 0:
                raise ValueError(f"'effort' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, effort=_effort)


class Velocity(Model):
    def __init__(self, sdf_version: str, velocity: float = 0):
        self.__version__ = sdf_version
        self.velocity = velocity

    def to_version(self, target_version: str) -> "Velocity":
        if self.velocity is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'velocity' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["velocity"] = self.velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = str(self.velocity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Velocity":
        _text = el.text or 0
        _velocity = _parse_double(_text)
        if _velocity is not None and cmp_version(version, "1.2") < 0:
            if _velocity != 0:
                raise ValueError(f"'velocity' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, velocity=_velocity)


class Stiffness(Model):
    def __init__(self, sdf_version: str, stiffness: float = 1e8):
        self.__version__ = sdf_version
        self.stiffness = stiffness

    def to_version(self, target_version: str) -> "Stiffness":
        if self.stiffness is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'stiffness' is not supported in SDF version {target_version} (added in 1.4)")
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
        _text = el.text or 1e8
        _stiffness = _parse_double(_text)
        if _stiffness is not None and cmp_version(version, "1.4") < 0:
            if _stiffness != 1e8:
                raise ValueError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, stiffness=_stiffness)


class Dissipation(Model):
    def __init__(self, sdf_version: str, dissipation: float = 1.0):
        self.__version__ = sdf_version
        self.dissipation = dissipation

    def to_version(self, target_version: str) -> "Dissipation":
        if self.dissipation is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'dissipation' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["dissipation"] = self.dissipation
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dissipation")
        if self.dissipation is not None:
            el.text = str(self.dissipation)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Dissipation":
        _text = el.text or 1.0
        _dissipation = _parse_double(_text)
        if _dissipation is not None and cmp_version(version, "1.4") < 0:
            if _dissipation != 1.0:
                raise ValueError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, dissipation=_dissipation)


class Limit(Model):
    def __init__(
        self,
        sdf_version: str,
        lower: float = -1e16,
        upper: float = 1e16,
        effort: float = 0,
        velocity: float = 0,
        stiffness: "Stiffness" = None,
        dissipation: "Dissipation" = None
    ):
        self.__version__ = sdf_version
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity
        self.stiffness = stiffness
        self.dissipation = dissipation

    def to_version(self, target_version: str) -> "Limit":
        if self.stiffness is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'stiffness' is not supported in SDF version {target_version} (added in 1.4)")
        if self.dissipation is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'dissipation' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["lower"] = self.lower
        kwargs["upper"] = self.upper
        kwargs["effort"] = self.effort
        kwargs["velocity"] = self.velocity
        kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
        kwargs["dissipation"] = self.dissipation.to_version(target_version) if self.dissipation is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("limit")
        if self.lower is not None:
            el.set("lower", str(self.lower))
        if self.upper is not None:
            el.set("upper", str(self.upper))
        if self.effort is not None:
            el.set("effort", str(self.effort))
        if self.velocity is not None:
            el.set("velocity", str(self.velocity))
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Limit":
        _lower = _parse_double(el.get("lower", -1e16))
        _upper = _parse_double(el.get("upper", 1e16))
        _effort = _parse_double(el.get("effort", 0))
        _velocity = _parse_double(el.get("velocity", 0))
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness, version) if _c_stiffness is not None else None
        if _stiffness is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'stiffness' is not supported in SDF version {version} (added in 1.4)")
        _c_dissipation = el.find("dissipation")
        _dissipation = Dissipation.from_sdf(_c_dissipation, version) if _c_dissipation is not None else None
        if _dissipation is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'dissipation' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, lower=_lower, upper=_upper, effort=_effort, velocity=_velocity, stiffness=_stiffness, dissipation=_dissipation)


class Xyz(Model):
    def __init__(self, sdf_version: str, xyz: Vector3 = None, expressed_in: str = ""):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.expressed_in = expressed_in

    def to_version(self, target_version: str) -> "Xyz":
        if self.xyz is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'xyz' is not supported in SDF version {target_version} (added in 1.2)")
        if self.expressed_in is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'expressed_in' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        kwargs["expressed_in"] = self.expressed_in
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("xyz")
        if self.xyz is not None:
            el.text = self.xyz.to_sdf()
        if self.expressed_in is not None:
            el.set("expressed_in", self.expressed_in)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Xyz":
        _text = el.text or "0 0 1"
        _xyz = Vector3.from_sdf(_text)
        if _xyz is not None and cmp_version(version, "1.2") < 0:
            if _xyz != "0 0 1":
                raise ValueError(f"'xyz' is not supported in SDF version {version} (added in 1.2)")
        _expressed_in = el.get("expressed_in", "")
        if _expressed_in is not None and cmp_version(version, "1.7") < 0:
            if _expressed_in != "":
                raise ValueError(f"'expressed_in' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, xyz=_xyz, expressed_in=_expressed_in)


class UseParentModelFrame(Model):
    def __init__(self, sdf_version: str, use_parent_model_frame: bool = False):
        self.__version__ = sdf_version
        self.use_parent_model_frame = use_parent_model_frame

    def to_version(self, target_version: str) -> "UseParentModelFrame":
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["use_parent_model_frame"] = self.use_parent_model_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("use_parent_model_frame")
        if self.use_parent_model_frame is not None:
            el.text = str(self.use_parent_model_frame).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "UseParentModelFrame":
        _text = el.text or False
        _use_parent_model_frame = _text.strip().lower() == 'true'
        if _use_parent_model_frame is not None and cmp_version(version, "1.5") < 0:
            if _use_parent_model_frame != False:
                raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, use_parent_model_frame=_use_parent_model_frame)


class InitialPosition(Model):
    def __init__(self, sdf_version: str, initial_position: float = 0):
        self.__version__ = sdf_version
        self.initial_position = initial_position

    def to_version(self, target_version: str) -> "InitialPosition":
        if self.initial_position is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["initial_position"] = self.initial_position
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("initial_position")
        if self.initial_position is not None:
            el.text = str(self.initial_position)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "InitialPosition":
        _text = el.text or 0
        _initial_position = _parse_double(_text)
        if _initial_position is not None and cmp_version(version, "1.6") < 0:
            if _initial_position != 0:
                raise ValueError(f"'initial_position' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, initial_position=_initial_position)


class Multiplier(Model):
    def __init__(self, sdf_version: str, multiplier: float = 1.0):
        self.__version__ = sdf_version
        self.multiplier = multiplier

    def to_version(self, target_version: str) -> "Multiplier":
        kwargs = {"sdf_version": target_version}
        kwargs["multiplier"] = self.multiplier
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("multiplier")
        if self.multiplier is not None:
            el.text = str(self.multiplier)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Multiplier":
        _text = el.text or 1.0
        _multiplier = _parse_double(_text)
        return cls(sdf_version=version, multiplier=_multiplier)


class Offset(Model):
    def __init__(self, sdf_version: str, offset: float = 0):
        self.__version__ = sdf_version
        self.offset = offset

    def to_version(self, target_version: str) -> "Offset":
        kwargs = {"sdf_version": target_version}
        kwargs["offset"] = self.offset
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("offset")
        if self.offset is not None:
            el.text = str(self.offset)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Offset":
        _text = el.text or 0
        _offset = _parse_double(_text)
        return cls(sdf_version=version, offset=_offset)


class Reference(Model):
    def __init__(self, sdf_version: str, reference: float = 0):
        self.__version__ = sdf_version
        self.reference = reference

    def to_version(self, target_version: str) -> "Reference":
        kwargs = {"sdf_version": target_version}
        kwargs["reference"] = self.reference
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("reference")
        if self.reference is not None:
            el.text = str(self.reference)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Reference":
        _text = el.text or 0
        _reference = _parse_double(_text)
        return cls(sdf_version=version, reference=_reference)


class Mimic(Model):
    def __init__(
        self,
        sdf_version: str,
        joint: str = "",
        axis: str = "axis",
        multiplier: "Multiplier" = None,
        offset: "Offset" = None,
        reference: "Reference" = None
    ):
        self.__version__ = sdf_version
        self.joint = joint
        self.axis = axis
        self.multiplier = multiplier
        self.offset = offset
        self.reference = reference

    def to_version(self, target_version: str) -> "Mimic":
        kwargs = {"sdf_version": target_version}
        kwargs["joint"] = self.joint
        kwargs["axis"] = self.axis
        kwargs["multiplier"] = self.multiplier.to_version(target_version) if self.multiplier is not None else None
        kwargs["offset"] = self.offset.to_version(target_version) if self.offset is not None else None
        kwargs["reference"] = self.reference.to_version(target_version) if self.reference is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mimic")
        if self.joint is not None:
            el.set("joint", self.joint)
        if self.axis is not None:
            el.set("axis", self.axis)
        if self.multiplier is not None:
            el.append(self.multiplier.to_sdf(version))
        if self.offset is not None:
            el.append(self.offset.to_sdf(version))
        if self.reference is not None:
            el.append(self.reference.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mimic":
        _joint = el.get("joint", "")
        _axis = el.get("axis", "axis")
        _c_multiplier = el.find("multiplier")
        _multiplier = Multiplier.from_sdf(_c_multiplier, version) if _c_multiplier is not None else None
        _c_offset = el.find("offset")
        _offset = Offset.from_sdf(_c_offset, version) if _c_offset is not None else None
        _c_reference = el.find("reference")
        _reference = Reference.from_sdf(_c_reference, version) if _c_reference is not None else None
        return cls(sdf_version=version, joint=_joint, axis=_axis, multiplier=_multiplier, offset=_offset, reference=_reference)


class Axis(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        xyz: Vector3 = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None,
        use_parent_model_frame: "UseParentModelFrame" = None,
        initial_position: "InitialPosition" = None,
        mimic: "Mimic" = None
    ):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit
        self.use_parent_model_frame = use_parent_model_frame
        self.initial_position = initial_position
        self.mimic = mimic

    def to_version(self, target_version: str) -> "Axis":
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.initial_position is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.6)")
        if self.mimic is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["use_parent_model_frame"] = self.use_parent_model_frame.to_version(target_version) if self.use_parent_model_frame is not None else None
        kwargs["initial_position"] = self.initial_position.to_version(target_version) if self.initial_position is not None else None
        kwargs["mimic"] = self.mimic.to_version(target_version) if self.mimic is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis")
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf(version))
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf(version))
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf(version))
        if self.mimic is not None:
            el.append(self.mimic.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Axis":
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 1"))
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics, version) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit, version) if _c_limit is not None else None
        _c_use_parent_model_frame = el.find("use_parent_model_frame")
        _use_parent_model_frame = UseParentModelFrame.from_sdf(_c_use_parent_model_frame, version) if _c_use_parent_model_frame is not None else None
        if _use_parent_model_frame is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {version} (added in 1.5)")
        _c_initial_position = el.find("initial_position")
        _initial_position = InitialPosition.from_sdf(_c_initial_position, version) if _c_initial_position is not None else None
        if _initial_position is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {version} (added in 1.6)")
        _c_mimic = el.find("mimic")
        _mimic = Mimic.from_sdf(_c_mimic, version) if _c_mimic is not None else None
        if _mimic is not None and cmp_version(version, "1.11") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {version} (added in 1.11)")
        return cls(sdf_version=version, xyz=_xyz, dynamics=_dynamics, limit=_limit, use_parent_model_frame=_use_parent_model_frame, initial_position=_initial_position, mimic=_mimic)


class Axis2(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "map", "from": "use_parent_model_frame", "to": "xyz::expressed_in", "from_values": ["true", "True", "TRUE", "1"], "to_value": "__model__"}]}]

    def __init__(
        self,
        sdf_version: str,
        xyz: Vector3 = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None,
        use_parent_model_frame: "UseParentModelFrame" = None,
        initial_position: "InitialPosition" = None,
        mimic: "Mimic" = None
    ):
        self.__version__ = sdf_version
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 1")
        self.xyz = xyz
        self.dynamics = dynamics
        self.limit = limit
        self.use_parent_model_frame = use_parent_model_frame
        self.initial_position = initial_position
        self.mimic = mimic

    def to_version(self, target_version: str) -> "Axis2":
        if self.use_parent_model_frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.initial_position is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {target_version} (added in 1.6)")
        if self.mimic is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["xyz"] = self.xyz
        kwargs["dynamics"] = self.dynamics.to_version(target_version) if self.dynamics is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["use_parent_model_frame"] = self.use_parent_model_frame.to_version(target_version) if self.use_parent_model_frame is not None else None
        kwargs["initial_position"] = self.initial_position.to_version(target_version) if self.initial_position is not None else None
        kwargs["mimic"] = self.mimic.to_version(target_version) if self.mimic is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("axis2")
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        if self.dynamics is not None:
            el.append(self.dynamics.to_sdf(version))
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf(version))
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf(version))
        if self.mimic is not None:
            el.append(self.mimic.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Axis2":
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 1"))
        _c_dynamics = el.find("dynamics")
        _dynamics = Dynamics.from_sdf(_c_dynamics, version) if _c_dynamics is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit, version) if _c_limit is not None else None
        _c_use_parent_model_frame = el.find("use_parent_model_frame")
        _use_parent_model_frame = UseParentModelFrame.from_sdf(_c_use_parent_model_frame, version) if _c_use_parent_model_frame is not None else None
        if _use_parent_model_frame is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'use_parent_model_frame' is not supported in SDF version {version} (added in 1.5)")
        _c_initial_position = el.find("initial_position")
        _initial_position = InitialPosition.from_sdf(_c_initial_position, version) if _c_initial_position is not None else None
        if _initial_position is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'initial_position' is not supported in SDF version {version} (added in 1.6)")
        _c_mimic = el.find("mimic")
        _mimic = Mimic.from_sdf(_c_mimic, version) if _c_mimic is not None else None
        if _mimic is not None and cmp_version(version, "1.11") < 0:
            raise ValueError(f"'mimic' is not supported in SDF version {version} (added in 1.11)")
        return cls(sdf_version=version, xyz=_xyz, dynamics=_dynamics, limit=_limit, use_parent_model_frame=_use_parent_model_frame, initial_position=_initial_position, mimic=_mimic)


class FudgeFactor(Model):
    def __init__(self, sdf_version: str, fudge_factor: float = 0):
        self.__version__ = sdf_version
        self.fudge_factor = fudge_factor

    def to_version(self, target_version: str) -> "FudgeFactor":
        kwargs = {"sdf_version": target_version}
        kwargs["fudge_factor"] = self.fudge_factor
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fudge_factor")
        if self.fudge_factor is not None:
            el.text = str(self.fudge_factor)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "FudgeFactor":
        _text = el.text or 0
        _fudge_factor = _parse_double(_text)
        return cls(sdf_version=version, fudge_factor=_fudge_factor)


class Cfm(Model):
    def __init__(self, sdf_version: str, cfm: float = 0):
        self.__version__ = sdf_version
        self.cfm = cfm

    def to_version(self, target_version: str) -> "Cfm":
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cfm")
        if self.cfm is not None:
            el.text = str(self.cfm)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cfm":
        _text = el.text or 0
        _cfm = _parse_double(_text)
        return cls(sdf_version=version, cfm=_cfm)


class Bounce(Model):
    def __init__(self, sdf_version: str, bounce: float = 0):
        self.__version__ = sdf_version
        self.bounce = bounce

    def to_version(self, target_version: str) -> "Bounce":
        kwargs = {"sdf_version": target_version}
        kwargs["bounce"] = self.bounce
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bounce")
        if self.bounce is not None:
            el.text = str(self.bounce)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Bounce":
        _text = el.text or 0
        _bounce = _parse_double(_text)
        return cls(sdf_version=version, bounce=_bounce)


class MaxForce(Model):
    def __init__(self, sdf_version: str, max_force: float = 0):
        self.__version__ = sdf_version
        self.max_force = max_force

    def to_version(self, target_version: str) -> "MaxForce":
        kwargs = {"sdf_version": target_version}
        kwargs["max_force"] = self.max_force
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_force")
        if self.max_force is not None:
            el.text = str(self.max_force)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxForce":
        _text = el.text or 0
        _max_force = _parse_double(_text)
        return cls(sdf_version=version, max_force=_max_force)


class Erp(Model):
    def __init__(self, sdf_version: str, erp: float = 0.2):
        self.__version__ = sdf_version
        self.erp = erp

    def to_version(self, target_version: str) -> "Erp":
        if self.erp is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'erp' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["erp"] = self.erp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("erp")
        if self.erp is not None:
            el.text = str(self.erp)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Erp":
        _text = el.text or 0.2
        _erp = _parse_double(_text)
        if _erp is not None and cmp_version(version, "1.2") < 0:
            if _erp != 0.2:
                raise ValueError(f"'erp' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, erp=_erp)


class Suspension(Model):
    def __init__(self, sdf_version: str, cfm: float = 0.0, erp: float = 0.2):
        self.__version__ = sdf_version
        self.cfm = cfm
        self.erp = erp

    def to_version(self, target_version: str) -> "Suspension":
        kwargs = {"sdf_version": target_version}
        kwargs["cfm"] = self.cfm
        kwargs["erp"] = self.erp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("suspension")
        if self.cfm is not None:
            el.set("cfm", str(self.cfm))
        if self.erp is not None:
            el.set("erp", str(self.erp))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Suspension":
        _cfm = _parse_double(el.get("cfm", 0.0))
        _erp = _parse_double(el.get("erp", 0.2))
        return cls(sdf_version=version, cfm=_cfm, erp=_erp)


class ProvideFeedback(Model):
    def __init__(self, sdf_version: str, provide_feedback: bool = False):
        self.__version__ = sdf_version
        self.provide_feedback = provide_feedback

    def to_version(self, target_version: str) -> "ProvideFeedback":
        if self.provide_feedback is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["provide_feedback"] = self.provide_feedback
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("provide_feedback")
        if self.provide_feedback is not None:
            el.text = str(self.provide_feedback).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ProvideFeedback":
        _text = el.text or False
        _provide_feedback = _text.strip().lower() == 'true'
        if _provide_feedback is not None and cmp_version(version, "1.3") < 0:
            if _provide_feedback != False:
                raise ValueError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, provide_feedback=_provide_feedback)


class CfmDamping(Model):
    def __init__(self, sdf_version: str, cfm_damping: bool = False):
        self.__version__ = sdf_version
        self.cfm_damping = cfm_damping

    def to_version(self, target_version: str) -> "CfmDamping":
        if self.cfm_damping is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'cfm_damping' is not supported in SDF version {target_version} (added in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["cfm_damping"] = self.cfm_damping
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cfm_damping")
        if self.cfm_damping is not None:
            el.text = str(self.cfm_damping).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CfmDamping":
        _text = el.text or False
        _cfm_damping = _text.strip().lower() == 'true'
        if _cfm_damping is not None and cmp_version(version, "1.3") < 0:
            if _cfm_damping != False:
                raise ValueError(f"'cfm_damping' is not supported in SDF version {version} (added in 1.3)")
        return cls(sdf_version=version, cfm_damping=_cfm_damping)


class ImplicitSpringDamper(Model):
    def __init__(self, sdf_version: str, implicit_spring_damper: bool = False):
        self.__version__ = sdf_version
        self.implicit_spring_damper = implicit_spring_damper

    def to_version(self, target_version: str) -> "ImplicitSpringDamper":
        if self.implicit_spring_damper is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'implicit_spring_damper' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["implicit_spring_damper"] = self.implicit_spring_damper
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("implicit_spring_damper")
        if self.implicit_spring_damper is not None:
            el.text = str(self.implicit_spring_damper).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ImplicitSpringDamper":
        _text = el.text or False
        _implicit_spring_damper = _text.strip().lower() == 'true'
        if _implicit_spring_damper is not None and cmp_version(version, "1.4") < 0:
            if _implicit_spring_damper != False:
                raise ValueError(f"'implicit_spring_damper' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, implicit_spring_damper=_implicit_spring_damper)


class Ode(Model):
    def __init__(
        self,
        sdf_version: str,
        fudge_factor: "FudgeFactor" = None,
        cfm: "Cfm" = None,
        bounce: "Bounce" = None,
        max_force: "MaxForce" = None,
        velocity: "Velocity" = None,
        limit: "Limit" = None,
        suspension: "Suspension" = None,
        provide_feedback: "ProvideFeedback" = None,
        cfm_damping: "CfmDamping" = None,
        implicit_spring_damper: "ImplicitSpringDamper" = None,
        erp: "Erp" = None
    ):
        self.__version__ = sdf_version
        self.fudge_factor = fudge_factor
        self.cfm = cfm
        self.bounce = bounce
        self.max_force = max_force
        self.velocity = velocity
        self.limit = limit
        self.suspension = suspension
        self.provide_feedback = provide_feedback
        self.cfm_damping = cfm_damping
        self.implicit_spring_damper = implicit_spring_damper
        self.erp = erp

    def to_version(self, target_version: str) -> "Ode":
        if self.provide_feedback is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.3)")
        if self.cfm_damping is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'cfm_damping' is not supported in SDF version {target_version} (added in 1.3)")
        if self.implicit_spring_damper is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'implicit_spring_damper' is not supported in SDF version {target_version} (added in 1.4)")
        if self.erp is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'erp' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["fudge_factor"] = self.fudge_factor.to_version(target_version) if self.fudge_factor is not None else None
        kwargs["cfm"] = self.cfm.to_version(target_version) if self.cfm is not None else None
        kwargs["bounce"] = self.bounce.to_version(target_version) if self.bounce is not None else None
        kwargs["max_force"] = self.max_force.to_version(target_version) if self.max_force is not None else None
        kwargs["velocity"] = self.velocity.to_version(target_version) if self.velocity is not None else None
        kwargs["limit"] = self.limit.to_version(target_version) if self.limit is not None else None
        kwargs["suspension"] = self.suspension.to_version(target_version) if self.suspension is not None else None
        kwargs["provide_feedback"] = self.provide_feedback.to_version(target_version) if self.provide_feedback is not None else None
        kwargs["cfm_damping"] = self.cfm_damping.to_version(target_version) if self.cfm_damping is not None else None
        kwargs["implicit_spring_damper"] = self.implicit_spring_damper.to_version(target_version) if self.implicit_spring_damper is not None else None
        kwargs["erp"] = self.erp.to_version(target_version) if self.erp is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.fudge_factor is not None:
            el.append(self.fudge_factor.to_sdf(version))
        if self.cfm is not None:
            el.append(self.cfm.to_sdf(version))
        if self.bounce is not None:
            el.append(self.bounce.to_sdf(version))
        if self.max_force is not None:
            el.append(self.max_force.to_sdf(version))
        if self.velocity is not None:
            el.append(self.velocity.to_sdf(version))
        if self.limit is not None:
            el.append(self.limit.to_sdf(version))
        if self.suspension is not None:
            el.append(self.suspension.to_sdf(version))
        if self.provide_feedback is not None:
            el.append(self.provide_feedback.to_sdf(version))
        if self.cfm_damping is not None:
            el.append(self.cfm_damping.to_sdf(version))
        if self.implicit_spring_damper is not None:
            el.append(self.implicit_spring_damper.to_sdf(version))
        if self.erp is not None:
            el.append(self.erp.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ode":
        _c_fudge_factor = el.find("fudge_factor")
        _fudge_factor = FudgeFactor.from_sdf(_c_fudge_factor, version) if _c_fudge_factor is not None else None
        _c_cfm = el.find("cfm")
        _cfm = Cfm.from_sdf(_c_cfm, version) if _c_cfm is not None else None
        _c_bounce = el.find("bounce")
        _bounce = Bounce.from_sdf(_c_bounce, version) if _c_bounce is not None else None
        _c_max_force = el.find("max_force")
        _max_force = MaxForce.from_sdf(_c_max_force, version) if _c_max_force is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity, version) if _c_velocity is not None else None
        _c_limit = el.find("limit")
        _limit = Limit.from_sdf(_c_limit, version) if _c_limit is not None else None
        _c_suspension = el.find("suspension")
        _suspension = Suspension.from_sdf(_c_suspension, version) if _c_suspension is not None else None
        _c_provide_feedback = el.find("provide_feedback")
        _provide_feedback = ProvideFeedback.from_sdf(_c_provide_feedback, version) if _c_provide_feedback is not None else None
        if _provide_feedback is not None and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.3)")
        _c_cfm_damping = el.find("cfm_damping")
        _cfm_damping = CfmDamping.from_sdf(_c_cfm_damping, version) if _c_cfm_damping is not None else None
        if _cfm_damping is not None and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'cfm_damping' is not supported in SDF version {version} (added in 1.3)")
        _c_implicit_spring_damper = el.find("implicit_spring_damper")
        _implicit_spring_damper = ImplicitSpringDamper.from_sdf(_c_implicit_spring_damper, version) if _c_implicit_spring_damper is not None else None
        if _implicit_spring_damper is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'implicit_spring_damper' is not supported in SDF version {version} (added in 1.4)")
        _c_erp = el.find("erp")
        _erp = Erp.from_sdf(_c_erp, version) if _c_erp is not None else None
        if _erp is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'erp' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, fudge_factor=_fudge_factor, cfm=_cfm, bounce=_bounce, max_force=_max_force, velocity=_velocity, limit=_limit, suspension=_suspension, provide_feedback=_provide_feedback, cfm_damping=_cfm_damping, implicit_spring_damper=_implicit_spring_damper, erp=_erp)


class MustBeLoopJoint(Model):
    def __init__(self, sdf_version: str, must_be_loop_joint: bool = False):
        self.__version__ = sdf_version
        self.must_be_loop_joint = must_be_loop_joint

    def to_version(self, target_version: str) -> "MustBeLoopJoint":
        kwargs = {"sdf_version": target_version}
        kwargs["must_be_loop_joint"] = self.must_be_loop_joint
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("must_be_loop_joint")
        if self.must_be_loop_joint is not None:
            el.text = str(self.must_be_loop_joint).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MustBeLoopJoint":
        _text = el.text or False
        _must_be_loop_joint = _text.strip().lower() == 'true'
        return cls(sdf_version=version, must_be_loop_joint=_must_be_loop_joint)


class Simbody(Model):
    def __init__(self, sdf_version: str, must_be_loop_joint: "MustBeLoopJoint" = None):
        self.__version__ = sdf_version
        self.must_be_loop_joint = must_be_loop_joint

    def to_version(self, target_version: str) -> "Simbody":
        kwargs = {"sdf_version": target_version}
        kwargs["must_be_loop_joint"] = self.must_be_loop_joint.to_version(target_version) if self.must_be_loop_joint is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("simbody")
        if self.must_be_loop_joint is not None:
            el.append(self.must_be_loop_joint.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Simbody":
        _c_must_be_loop_joint = el.find("must_be_loop_joint")
        _must_be_loop_joint = MustBeLoopJoint.from_sdf(_c_must_be_loop_joint, version) if _c_must_be_loop_joint is not None else None
        return cls(sdf_version=version, must_be_loop_joint=_must_be_loop_joint)


class Physics(Model):
    _MIGRATIONS = [{"version": "1.4", "ops": [{"type": "move", "from": "update_rate", "to": "real_time_update_rate"}, {"type": "move", "from": "ode::solver::dt", "to": "max_step_size"}, {"type": "move", "from": "bullet::dt", "to": "max_step_size"}]}]

    def __init__(
        self,
        sdf_version: str,
        ode: "Ode" = None,
        simbody: "Simbody" = None,
        provide_feedback: "ProvideFeedback" = None
    ):
        self.__version__ = sdf_version
        self.ode = ode
        self.simbody = simbody
        self.provide_feedback = provide_feedback

    def to_version(self, target_version: str) -> "Physics":
        if self.simbody is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'simbody' is not supported in SDF version {target_version} (added in 1.4)")
        if self.provide_feedback is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["simbody"] = self.simbody.to_version(target_version) if self.simbody is not None else None
        kwargs["provide_feedback"] = self.provide_feedback.to_version(target_version) if self.provide_feedback is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("physics")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.simbody is not None:
            el.append(self.simbody.to_sdf(version))
        if self.provide_feedback is not None:
            el.append(self.provide_feedback.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Physics":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode, version) if _c_ode is not None else None
        _c_simbody = el.find("simbody")
        _simbody = Simbody.from_sdf(_c_simbody, version) if _c_simbody is not None else None
        if _simbody is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'simbody' is not supported in SDF version {version} (added in 1.4)")
        _c_provide_feedback = el.find("provide_feedback")
        _provide_feedback = ProvideFeedback.from_sdf(_c_provide_feedback, version) if _c_provide_feedback is not None else None
        if _provide_feedback is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'provide_feedback' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, ode=_ode, simbody=_simbody, provide_feedback=_provide_feedback)


class Pose(Model):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        pose: Pose = None,
        frame: str = "",
        relative_to: str = "",
        rotation_format: str = "euler_rpy",
        degrees: bool = False
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = Pose.from_sdf("0 0 0 0 0 0")
        self.pose = pose
        self.frame = frame
        self.relative_to = relative_to
        self.rotation_format = rotation_format
        self.degrees = degrees

    def to_version(self, target_version: str) -> "Pose":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        kwargs["frame"] = self.frame
        kwargs["relative_to"] = self.relative_to
        kwargs["rotation_format"] = self.rotation_format
        kwargs["degrees"] = self.degrees
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pose":
        _text = el.text or "0 0 0 0 0 0"
        _pose = Pose.from_sdf(_text)
        if _pose is not None and cmp_version(version, "1.2") < 0:
            if _pose != "0 0 0 0 0 0":
                raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _frame = el.get("frame", "")
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _relative_to = el.get("relative_to", "")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                raise ValueError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                raise ValueError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                raise ValueError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, pose=_pose, frame=_frame, relative_to=_relative_to, rotation_format=_rotation_format, degrees=_degrees)


class Plugin(Model):
    def __init__(self, sdf_version: str, name: str = "__default__", filename: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name
        self.filename = filename

    def to_version(self, target_version: str) -> "Plugin":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["filename"] = self.filename
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plugin")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.set("filename", self.filename)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Plugin":
        _name = el.get("name", "__default__")
        _filename = el.get("filename", "__default__")
        return cls(sdf_version=version, name=_name, filename=_filename)


class HorizontalFov(Model):
    def __init__(self, sdf_version: str, horizontal_fov: float = 1.047):
        self.__version__ = sdf_version
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "HorizontalFov":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal_fov"] = self.horizontal_fov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal_fov")
        if self.horizontal_fov is not None:
            el.text = str(self.horizontal_fov)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "HorizontalFov":
        _text = el.text or 1.047
        _horizontal_fov = _parse_double(_text)
        return cls(sdf_version=version, horizontal_fov=_horizontal_fov)


class Width(Model):
    def __init__(self, sdf_version: str, width: int = 320):
        self.__version__ = sdf_version
        self.width = width

    def to_version(self, target_version: str) -> "Width":
        kwargs = {"sdf_version": target_version}
        kwargs["width"] = self.width
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("width")
        if self.width is not None:
            el.text = str(self.width)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Width":
        _text = el.text or 320
        _width = _parse_int32(_text)
        return cls(sdf_version=version, width=_width)


class Height(Model):
    def __init__(self, sdf_version: str, height: int = 240):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("height")
        if self.height is not None:
            el.text = str(self.height)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Height":
        _text = el.text or 240
        _height = _parse_int32(_text)
        return cls(sdf_version=version, height=_height)


class Format(Model):
    def __init__(self, sdf_version: str, format: str = "R8G8B8"):
        self.__version__ = sdf_version
        self.format = format

    def to_version(self, target_version: str) -> "Format":
        kwargs = {"sdf_version": target_version}
        kwargs["format"] = self.format
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("format")
        if self.format is not None:
            el.text = self.format
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Format":
        _text = el.text or "R8G8B8"
        _format = _text
        return cls(sdf_version=version, format=_format)


class AntiAliasing(Model):
    def __init__(self, sdf_version: str, anti_aliasing: int = 4):
        self.__version__ = sdf_version
        self.anti_aliasing = anti_aliasing

    def to_version(self, target_version: str) -> "AntiAliasing":
        if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["anti_aliasing"] = self.anti_aliasing
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("anti_aliasing")
        if self.anti_aliasing is not None:
            el.text = str(self.anti_aliasing)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AntiAliasing":
        _text = el.text or 4
        _anti_aliasing = _parse_int32(_text)
        if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
            if _anti_aliasing != 4:
                raise ValueError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, anti_aliasing=_anti_aliasing)


class Image(Model):
    def __init__(
        self,
        sdf_version: str,
        width: "Width" = None,
        height: "Height" = None,
        format: "Format" = None,
        anti_aliasing: "AntiAliasing" = None
    ):
        self.__version__ = sdf_version
        self.width = width
        self.height = height
        self.format = format
        self.anti_aliasing = anti_aliasing

    def to_version(self, target_version: str) -> "Image":
        if self.anti_aliasing is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["width"] = self.width.to_version(target_version) if self.width is not None else None
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        kwargs["format"] = self.format.to_version(target_version) if self.format is not None else None
        kwargs["anti_aliasing"] = self.anti_aliasing.to_version(target_version) if self.anti_aliasing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("image")
        if self.width is not None:
            el.append(self.width.to_sdf(version))
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        if self.format is not None:
            el.append(self.format.to_sdf(version))
        if self.anti_aliasing is not None:
            el.append(self.anti_aliasing.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Image":
        _c_width = el.find("width")
        _width = Width.from_sdf(_c_width, version) if _c_width is not None else None
        _c_height = el.find("height")
        _height = Height.from_sdf(_c_height, version) if _c_height is not None else None
        _c_format = el.find("format")
        _format = Format.from_sdf(_c_format, version) if _c_format is not None else None
        _c_anti_aliasing = el.find("anti_aliasing")
        _anti_aliasing = AntiAliasing.from_sdf(_c_anti_aliasing, version) if _c_anti_aliasing is not None else None
        if _anti_aliasing is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'anti_aliasing' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, width=_width, height=_height, format=_format, anti_aliasing=_anti_aliasing)


class Near(Model):
    def __init__(self, sdf_version: str, near: float = .1):
        self.__version__ = sdf_version
        self.near = near

    def to_version(self, target_version: str) -> "Near":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("near")
        if self.near is not None:
            el.text = str(self.near)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Near":
        _text = el.text or .1
        _near = _parse_double(_text)
        return cls(sdf_version=version, near=_near)


class Far(Model):
    def __init__(self, sdf_version: str, far: float = 100):
        self.__version__ = sdf_version
        self.far = far

    def to_version(self, target_version: str) -> "Far":
        kwargs = {"sdf_version": target_version}
        kwargs["far"] = self.far
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("far")
        if self.far is not None:
            el.text = str(self.far)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Far":
        _text = el.text or 100
        _far = _parse_double(_text)
        return cls(sdf_version=version, far=_far)


class Clip(Model):
    def __init__(self, sdf_version: str, near: "Near" = None, far: "Far" = None):
        self.__version__ = sdf_version
        self.near = near
        self.far = far

    def to_version(self, target_version: str) -> "Clip":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near.to_version(target_version) if self.near is not None else None
        kwargs["far"] = self.far.to_version(target_version) if self.far is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("clip")
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        if self.far is not None:
            el.append(self.far.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Clip":
        _c_near = el.find("near")
        _near = Near.from_sdf(_c_near, version) if _c_near is not None else None
        _c_far = el.find("far")
        _far = Far.from_sdf(_c_far, version) if _c_far is not None else None
        return cls(sdf_version=version, near=_near, far=_far)


class Path(Model):
    def __init__(self, sdf_version: str, path: str = "__default__"):
        self.__version__ = sdf_version
        self.path = path

    def to_version(self, target_version: str) -> "Path":
        kwargs = {"sdf_version": target_version}
        kwargs["path"] = self.path
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("path")
        if self.path is not None:
            el.text = self.path
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Path":
        _text = el.text or "__default__"
        _path = _text
        return cls(sdf_version=version, path=_path)


class Save(Model):
    def __init__(self, sdf_version: str, enabled: bool = False, path: "Path" = None):
        self.__version__ = sdf_version
        self.enabled = enabled
        self.path = path

    def to_version(self, target_version: str) -> "Save":
        kwargs = {"sdf_version": target_version}
        kwargs["enabled"] = self.enabled
        kwargs["path"] = self.path.to_version(target_version) if self.path is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("save")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        if self.path is not None:
            el.append(self.path.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Save":
        _enabled = el.get("enabled", False).strip().lower() == 'true'
        _c_path = el.find("path")
        _path = Path.from_sdf(_c_path, version) if _c_path is not None else None
        return cls(sdf_version=version, enabled=_enabled, path=_path)


class Output(Model):
    def __init__(self, sdf_version: str, output: str = "depths"):
        self.__version__ = sdf_version
        self.output = output

    def to_version(self, target_version: str) -> "Output":
        kwargs = {"sdf_version": target_version}
        kwargs["output"] = self.output
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("output")
        if self.output is not None:
            el.text = self.output
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Output":
        _text = el.text or "depths"
        _output = _text
        return cls(sdf_version=version, output=_output)


class DepthCamera(Model):
    def __init__(self, sdf_version: str, output: "Output" = None, clip: "Clip" = None):
        self.__version__ = sdf_version
        self.output = output
        self.clip = clip

    def to_version(self, target_version: str) -> "DepthCamera":
        if self.clip is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'clip' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["output"] = self.output.to_version(target_version) if self.output is not None else None
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("depth_camera")
        if self.output is not None:
            el.append(self.output.to_sdf(version))
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "DepthCamera":
        _c_output = el.find("output")
        _output = Output.from_sdf(_c_output, version) if _c_output is not None else None
        _c_clip = el.find("clip")
        _clip = Clip.from_sdf(_c_clip, version) if _c_clip is not None else None
        if _clip is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'clip' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, output=_output, clip=_clip)


class Type(Model):
    def __init__(self, sdf_version: str, type: str = "gaussian"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Type":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Type":
        _text = el.text or "gaussian"
        _type = _text
        return cls(sdf_version=version, type=_type)


class Mean(Model):
    def __init__(self, sdf_version: str, mean: float = 0.0):
        self.__version__ = sdf_version
        self.mean = mean

    def to_version(self, target_version: str) -> "Mean":
        kwargs = {"sdf_version": target_version}
        kwargs["mean"] = self.mean
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mean")
        if self.mean is not None:
            el.text = str(self.mean)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mean":
        _text = el.text or 0.0
        _mean = _parse_double(_text)
        return cls(sdf_version=version, mean=_mean)


class Stddev(Model):
    def __init__(self, sdf_version: str, stddev: float = 0.0):
        self.__version__ = sdf_version
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Stddev":
        kwargs = {"sdf_version": target_version}
        kwargs["stddev"] = self.stddev
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("stddev")
        if self.stddev is not None:
            el.text = str(self.stddev)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Stddev":
        _text = el.text or 0.0
        _stddev = _parse_double(_text)
        return cls(sdf_version=version, stddev=_stddev)


class Noise(Model):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        mean: "Mean" = None,
        stddev: "Stddev" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.mean = mean
        self.stddev = stddev

    def to_version(self, target_version: str) -> "Noise":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["mean"] = self.mean.to_version(target_version) if self.mean is not None else None
        kwargs["stddev"] = self.stddev.to_version(target_version) if self.stddev is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("noise")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.mean is not None:
            el.append(self.mean.to_sdf(version))
        if self.stddev is not None:
            el.append(self.stddev.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Noise":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type, version) if _c_type is not None else None
        _c_mean = el.find("mean")
        _mean = Mean.from_sdf(_c_mean, version) if _c_mean is not None else None
        _c_stddev = el.find("stddev")
        _stddev = Stddev.from_sdf(_c_stddev, version) if _c_stddev is not None else None
        return cls(sdf_version=version, type=_type, mean=_mean, stddev=_stddev)


class Frame(Model):
    def __init__(self, sdf_version: str, name: str = "", pose: "Pose" = None):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "Frame":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Frame":
        _name = el.get("name", "")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        return cls(sdf_version=version, name=_name, pose=_pose)


class K1(Model):
    def __init__(self, sdf_version: str, k1: float = 0.0):
        self.__version__ = sdf_version
        self.k1 = k1

    def to_version(self, target_version: str) -> "K1":
        kwargs = {"sdf_version": target_version}
        kwargs["k1"] = self.k1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k1")
        if self.k1 is not None:
            el.text = str(self.k1)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "K1":
        _text = el.text or 0.0
        _k1 = _parse_double(_text)
        return cls(sdf_version=version, k1=_k1)


class K2(Model):
    def __init__(self, sdf_version: str, k2: float = 0.0):
        self.__version__ = sdf_version
        self.k2 = k2

    def to_version(self, target_version: str) -> "K2":
        kwargs = {"sdf_version": target_version}
        kwargs["k2"] = self.k2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k2")
        if self.k2 is not None:
            el.text = str(self.k2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "K2":
        _text = el.text or 0.0
        _k2 = _parse_double(_text)
        return cls(sdf_version=version, k2=_k2)


class K3(Model):
    def __init__(self, sdf_version: str, k3: float = 0.0):
        self.__version__ = sdf_version
        self.k3 = k3

    def to_version(self, target_version: str) -> "K3":
        kwargs = {"sdf_version": target_version}
        kwargs["k3"] = self.k3
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("k3")
        if self.k3 is not None:
            el.text = str(self.k3)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "K3":
        _text = el.text or 0.0
        _k3 = _parse_double(_text)
        return cls(sdf_version=version, k3=_k3)


class P1(Model):
    def __init__(self, sdf_version: str, p1: float = 0.0):
        self.__version__ = sdf_version
        self.p1 = p1

    def to_version(self, target_version: str) -> "P1":
        kwargs = {"sdf_version": target_version}
        kwargs["p1"] = self.p1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p1")
        if self.p1 is not None:
            el.text = str(self.p1)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "P1":
        _text = el.text or 0.0
        _p1 = _parse_double(_text)
        return cls(sdf_version=version, p1=_p1)


class P2(Model):
    def __init__(self, sdf_version: str, p2: float = 0.0):
        self.__version__ = sdf_version
        self.p2 = p2

    def to_version(self, target_version: str) -> "P2":
        kwargs = {"sdf_version": target_version}
        kwargs["p2"] = self.p2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p2")
        if self.p2 is not None:
            el.text = str(self.p2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "P2":
        _text = el.text or 0.0
        _p2 = _parse_double(_text)
        return cls(sdf_version=version, p2=_p2)


class Center(Model):
    def __init__(self, sdf_version: str, center: Vector2d = None):
        self.__version__ = sdf_version
        if center is None:
            center = Vector2d.from_sdf("0.5 0.5")
        self.center = center

    def to_version(self, target_version: str) -> "Center":
        kwargs = {"sdf_version": target_version}
        kwargs["center"] = self.center
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("center")
        if self.center is not None:
            el.text = self.center.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Center":
        _text = el.text or "0.5 0.5"
        _center = Vector2d.from_sdf(_text)
        return cls(sdf_version=version, center=_center)


class Distortion(Model):
    def __init__(
        self,
        sdf_version: str,
        k1: "K1" = None,
        k2: "K2" = None,
        k3: "K3" = None,
        p1: "P1" = None,
        p2: "P2" = None,
        center: "Center" = None
    ):
        self.__version__ = sdf_version
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.p1 = p1
        self.p2 = p2
        self.center = center

    def to_version(self, target_version: str) -> "Distortion":
        kwargs = {"sdf_version": target_version}
        kwargs["k1"] = self.k1.to_version(target_version) if self.k1 is not None else None
        kwargs["k2"] = self.k2.to_version(target_version) if self.k2 is not None else None
        kwargs["k3"] = self.k3.to_version(target_version) if self.k3 is not None else None
        kwargs["p1"] = self.p1.to_version(target_version) if self.p1 is not None else None
        kwargs["p2"] = self.p2.to_version(target_version) if self.p2 is not None else None
        kwargs["center"] = self.center.to_version(target_version) if self.center is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("distortion")
        if self.k1 is not None:
            el.append(self.k1.to_sdf(version))
        if self.k2 is not None:
            el.append(self.k2.to_sdf(version))
        if self.k3 is not None:
            el.append(self.k3.to_sdf(version))
        if self.p1 is not None:
            el.append(self.p1.to_sdf(version))
        if self.p2 is not None:
            el.append(self.p2.to_sdf(version))
        if self.center is not None:
            el.append(self.center.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Distortion":
        _c_k1 = el.find("k1")
        _k1 = K1.from_sdf(_c_k1, version) if _c_k1 is not None else None
        _c_k2 = el.find("k2")
        _k2 = K2.from_sdf(_c_k2, version) if _c_k2 is not None else None
        _c_k3 = el.find("k3")
        _k3 = K3.from_sdf(_c_k3, version) if _c_k3 is not None else None
        _c_p1 = el.find("p1")
        _p1 = P1.from_sdf(_c_p1, version) if _c_p1 is not None else None
        _c_p2 = el.find("p2")
        _p2 = P2.from_sdf(_c_p2, version) if _c_p2 is not None else None
        _c_center = el.find("center")
        _center = Center.from_sdf(_c_center, version) if _c_center is not None else None
        return cls(sdf_version=version, k1=_k1, k2=_k2, k3=_k3, p1=_p1, p2=_p2, center=_center)


class ScaleToHfov(Model):
    def __init__(self, sdf_version: str, scale_to_hfov: bool = True):
        self.__version__ = sdf_version
        self.scale_to_hfov = scale_to_hfov

    def to_version(self, target_version: str) -> "ScaleToHfov":
        kwargs = {"sdf_version": target_version}
        kwargs["scale_to_hfov"] = self.scale_to_hfov
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale_to_hfov")
        if self.scale_to_hfov is not None:
            el.text = str(self.scale_to_hfov).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ScaleToHfov":
        _text = el.text or True
        _scale_to_hfov = _text.strip().lower() == 'true'
        return cls(sdf_version=version, scale_to_hfov=_scale_to_hfov)


class C1(Model):
    def __init__(self, sdf_version: str, c1: float = 1):
        self.__version__ = sdf_version
        self.c1 = c1

    def to_version(self, target_version: str) -> "C1":
        kwargs = {"sdf_version": target_version}
        kwargs["c1"] = self.c1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c1")
        if self.c1 is not None:
            el.text = str(self.c1)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "C1":
        _text = el.text or 1
        _c1 = _parse_double(_text)
        return cls(sdf_version=version, c1=_c1)


class C2(Model):
    def __init__(self, sdf_version: str, c2: float = 1):
        self.__version__ = sdf_version
        self.c2 = c2

    def to_version(self, target_version: str) -> "C2":
        kwargs = {"sdf_version": target_version}
        kwargs["c2"] = self.c2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c2")
        if self.c2 is not None:
            el.text = str(self.c2)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "C2":
        _text = el.text or 1
        _c2 = _parse_double(_text)
        return cls(sdf_version=version, c2=_c2)


class C3(Model):
    def __init__(self, sdf_version: str, c3: float = 0):
        self.__version__ = sdf_version
        self.c3 = c3

    def to_version(self, target_version: str) -> "C3":
        kwargs = {"sdf_version": target_version}
        kwargs["c3"] = self.c3
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("c3")
        if self.c3 is not None:
            el.text = str(self.c3)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "C3":
        _text = el.text or 0
        _c3 = _parse_double(_text)
        return cls(sdf_version=version, c3=_c3)


class F(Model):
    def __init__(self, sdf_version: str, f: float = 1):
        self.__version__ = sdf_version
        self.f = f

    def to_version(self, target_version: str) -> "F":
        kwargs = {"sdf_version": target_version}
        kwargs["f"] = self.f
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("f")
        if self.f is not None:
            el.text = str(self.f)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "F":
        _text = el.text or 1
        _f = _parse_double(_text)
        return cls(sdf_version=version, f=_f)


class Fun(Model):
    def __init__(self, sdf_version: str, fun: str = "tan"):
        self.__version__ = sdf_version
        self.fun = fun

    def to_version(self, target_version: str) -> "Fun":
        kwargs = {"sdf_version": target_version}
        kwargs["fun"] = self.fun
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fun")
        if self.fun is not None:
            el.text = self.fun
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fun":
        _text = el.text or "tan"
        _fun = _text
        return cls(sdf_version=version, fun=_fun)


class CustomFunction(Model):
    def __init__(
        self,
        sdf_version: str,
        c1: "C1" = None,
        c2: "C2" = None,
        c3: "C3" = None,
        f: "F" = None,
        fun: "Fun" = None
    ):
        self.__version__ = sdf_version
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.f = f
        self.fun = fun

    def to_version(self, target_version: str) -> "CustomFunction":
        kwargs = {"sdf_version": target_version}
        kwargs["c1"] = self.c1.to_version(target_version) if self.c1 is not None else None
        kwargs["c2"] = self.c2.to_version(target_version) if self.c2 is not None else None
        kwargs["c3"] = self.c3.to_version(target_version) if self.c3 is not None else None
        kwargs["f"] = self.f.to_version(target_version) if self.f is not None else None
        kwargs["fun"] = self.fun.to_version(target_version) if self.fun is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("custom_function")
        if self.c1 is not None:
            el.append(self.c1.to_sdf(version))
        if self.c2 is not None:
            el.append(self.c2.to_sdf(version))
        if self.c3 is not None:
            el.append(self.c3.to_sdf(version))
        if self.f is not None:
            el.append(self.f.to_sdf(version))
        if self.fun is not None:
            el.append(self.fun.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CustomFunction":
        _c_c1 = el.find("c1")
        _c1 = C1.from_sdf(_c_c1, version) if _c_c1 is not None else None
        _c_c2 = el.find("c2")
        _c2 = C2.from_sdf(_c_c2, version) if _c_c2 is not None else None
        _c_c3 = el.find("c3")
        _c3 = C3.from_sdf(_c_c3, version) if _c_c3 is not None else None
        _c_f = el.find("f")
        _f = F.from_sdf(_c_f, version) if _c_f is not None else None
        _c_fun = el.find("fun")
        _fun = Fun.from_sdf(_c_fun, version) if _c_fun is not None else None
        return cls(sdf_version=version, c1=_c1, c2=_c2, c3=_c3, f=_f, fun=_fun)


class CutoffAngle(Model):
    def __init__(self, sdf_version: str, cutoff_angle: float = 1.5707):
        self.__version__ = sdf_version
        self.cutoff_angle = cutoff_angle

    def to_version(self, target_version: str) -> "CutoffAngle":
        kwargs = {"sdf_version": target_version}
        kwargs["cutoff_angle"] = self.cutoff_angle
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cutoff_angle")
        if self.cutoff_angle is not None:
            el.text = str(self.cutoff_angle)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CutoffAngle":
        _text = el.text or 1.5707
        _cutoff_angle = _parse_double(_text)
        return cls(sdf_version=version, cutoff_angle=_cutoff_angle)


class EnvTextureSize(Model):
    def __init__(self, sdf_version: str, env_texture_size: int = 256):
        self.__version__ = sdf_version
        self.env_texture_size = env_texture_size

    def to_version(self, target_version: str) -> "EnvTextureSize":
        kwargs = {"sdf_version": target_version}
        kwargs["env_texture_size"] = self.env_texture_size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("env_texture_size")
        if self.env_texture_size is not None:
            el.text = str(self.env_texture_size)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EnvTextureSize":
        _text = el.text or 256
        _env_texture_size = _parse_int32(_text)
        return cls(sdf_version=version, env_texture_size=_env_texture_size)


class Fx(Model):
    def __init__(self, sdf_version: str, fx: float = 277):
        self.__version__ = sdf_version
        self.fx = fx

    def to_version(self, target_version: str) -> "Fx":
        kwargs = {"sdf_version": target_version}
        kwargs["fx"] = self.fx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fx")
        if self.fx is not None:
            el.text = str(self.fx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fx":
        _text = el.text or 277
        _fx = _parse_double(_text)
        return cls(sdf_version=version, fx=_fx)


class Fy(Model):
    def __init__(self, sdf_version: str, fy: float = 277):
        self.__version__ = sdf_version
        self.fy = fy

    def to_version(self, target_version: str) -> "Fy":
        kwargs = {"sdf_version": target_version}
        kwargs["fy"] = self.fy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fy")
        if self.fy is not None:
            el.text = str(self.fy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Fy":
        _text = el.text or 277
        _fy = _parse_double(_text)
        return cls(sdf_version=version, fy=_fy)


class Cx(Model):
    def __init__(self, sdf_version: str, cx: float = 160):
        self.__version__ = sdf_version
        self.cx = cx

    def to_version(self, target_version: str) -> "Cx":
        kwargs = {"sdf_version": target_version}
        kwargs["cx"] = self.cx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cx")
        if self.cx is not None:
            el.text = str(self.cx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cx":
        _text = el.text or 160
        _cx = _parse_double(_text)
        return cls(sdf_version=version, cx=_cx)


class Cy(Model):
    def __init__(self, sdf_version: str, cy: float = 120):
        self.__version__ = sdf_version
        self.cy = cy

    def to_version(self, target_version: str) -> "Cy":
        kwargs = {"sdf_version": target_version}
        kwargs["cy"] = self.cy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cy")
        if self.cy is not None:
            el.text = str(self.cy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cy":
        _text = el.text or 120
        _cy = _parse_double(_text)
        return cls(sdf_version=version, cy=_cy)


class S(Model):
    def __init__(self, sdf_version: str, s: float = 0.0):
        self.__version__ = sdf_version
        self.s = s

    def to_version(self, target_version: str) -> "S":
        kwargs = {"sdf_version": target_version}
        kwargs["s"] = self.s
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("s")
        if self.s is not None:
            el.text = str(self.s)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "S":
        _text = el.text or 0.0
        _s = _parse_double(_text)
        return cls(sdf_version=version, s=_s)


class Intrinsics(Model):
    def __init__(
        self,
        sdf_version: str,
        fx: "Fx" = None,
        fy: "Fy" = None,
        cx: "Cx" = None,
        cy: "Cy" = None,
        s: "S" = None
    ):
        self.__version__ = sdf_version
        self.fx = fx
        self.fy = fy
        self.cx = cx
        self.cy = cy
        self.s = s

    def to_version(self, target_version: str) -> "Intrinsics":
        kwargs = {"sdf_version": target_version}
        kwargs["fx"] = self.fx.to_version(target_version) if self.fx is not None else None
        kwargs["fy"] = self.fy.to_version(target_version) if self.fy is not None else None
        kwargs["cx"] = self.cx.to_version(target_version) if self.cx is not None else None
        kwargs["cy"] = self.cy.to_version(target_version) if self.cy is not None else None
        kwargs["s"] = self.s.to_version(target_version) if self.s is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("intrinsics")
        if self.fx is not None:
            el.append(self.fx.to_sdf(version))
        if self.fy is not None:
            el.append(self.fy.to_sdf(version))
        if self.cx is not None:
            el.append(self.cx.to_sdf(version))
        if self.cy is not None:
            el.append(self.cy.to_sdf(version))
        if self.s is not None:
            el.append(self.s.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Intrinsics":
        _c_fx = el.find("fx")
        _fx = Fx.from_sdf(_c_fx, version) if _c_fx is not None else None
        _c_fy = el.find("fy")
        _fy = Fy.from_sdf(_c_fy, version) if _c_fy is not None else None
        _c_cx = el.find("cx")
        _cx = Cx.from_sdf(_c_cx, version) if _c_cx is not None else None
        _c_cy = el.find("cy")
        _cy = Cy.from_sdf(_c_cy, version) if _c_cy is not None else None
        _c_s = el.find("s")
        _s = S.from_sdf(_c_s, version) if _c_s is not None else None
        return cls(sdf_version=version, fx=_fx, fy=_fy, cx=_cx, cy=_cy, s=_s)


class PFx(Model):
    def __init__(self, sdf_version: str, p_fx: float = 277):
        self.__version__ = sdf_version
        self.p_fx = p_fx

    def to_version(self, target_version: str) -> "PFx":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fx"] = self.p_fx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_fx")
        if self.p_fx is not None:
            el.text = str(self.p_fx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PFx":
        _text = el.text or 277
        _p_fx = _parse_double(_text)
        return cls(sdf_version=version, p_fx=_p_fx)


class PFy(Model):
    def __init__(self, sdf_version: str, p_fy: float = 277):
        self.__version__ = sdf_version
        self.p_fy = p_fy

    def to_version(self, target_version: str) -> "PFy":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fy"] = self.p_fy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_fy")
        if self.p_fy is not None:
            el.text = str(self.p_fy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PFy":
        _text = el.text or 277
        _p_fy = _parse_double(_text)
        return cls(sdf_version=version, p_fy=_p_fy)


class PCx(Model):
    def __init__(self, sdf_version: str, p_cx: float = 160):
        self.__version__ = sdf_version
        self.p_cx = p_cx

    def to_version(self, target_version: str) -> "PCx":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cx"] = self.p_cx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_cx")
        if self.p_cx is not None:
            el.text = str(self.p_cx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PCx":
        _text = el.text or 160
        _p_cx = _parse_double(_text)
        return cls(sdf_version=version, p_cx=_p_cx)


class PCy(Model):
    def __init__(self, sdf_version: str, p_cy: float = 120):
        self.__version__ = sdf_version
        self.p_cy = p_cy

    def to_version(self, target_version: str) -> "PCy":
        kwargs = {"sdf_version": target_version}
        kwargs["p_cy"] = self.p_cy
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("p_cy")
        if self.p_cy is not None:
            el.text = str(self.p_cy)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PCy":
        _text = el.text or 120
        _p_cy = _parse_double(_text)
        return cls(sdf_version=version, p_cy=_p_cy)


class Tx(Model):
    def __init__(self, sdf_version: str, tx: float = 0.0):
        self.__version__ = sdf_version
        self.tx = tx

    def to_version(self, target_version: str) -> "Tx":
        kwargs = {"sdf_version": target_version}
        kwargs["tx"] = self.tx
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("tx")
        if self.tx is not None:
            el.text = str(self.tx)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Tx":
        _text = el.text or 0.0
        _tx = _parse_double(_text)
        return cls(sdf_version=version, tx=_tx)


class Ty(Model):
    def __init__(self, sdf_version: str, ty: float = 0.0):
        self.__version__ = sdf_version
        self.ty = ty

    def to_version(self, target_version: str) -> "Ty":
        kwargs = {"sdf_version": target_version}
        kwargs["ty"] = self.ty
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ty")
        if self.ty is not None:
            el.text = str(self.ty)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ty":
        _text = el.text or 0.0
        _ty = _parse_double(_text)
        return cls(sdf_version=version, ty=_ty)


class Projection(Model):
    def __init__(
        self,
        sdf_version: str,
        p_fx: "PFx" = None,
        p_fy: "PFy" = None,
        p_cx: "PCx" = None,
        p_cy: "PCy" = None,
        tx: "Tx" = None,
        ty: "Ty" = None
    ):
        self.__version__ = sdf_version
        self.p_fx = p_fx
        self.p_fy = p_fy
        self.p_cx = p_cx
        self.p_cy = p_cy
        self.tx = tx
        self.ty = ty

    def to_version(self, target_version: str) -> "Projection":
        kwargs = {"sdf_version": target_version}
        kwargs["p_fx"] = self.p_fx.to_version(target_version) if self.p_fx is not None else None
        kwargs["p_fy"] = self.p_fy.to_version(target_version) if self.p_fy is not None else None
        kwargs["p_cx"] = self.p_cx.to_version(target_version) if self.p_cx is not None else None
        kwargs["p_cy"] = self.p_cy.to_version(target_version) if self.p_cy is not None else None
        kwargs["tx"] = self.tx.to_version(target_version) if self.tx is not None else None
        kwargs["ty"] = self.ty.to_version(target_version) if self.ty is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("projection")
        if self.p_fx is not None:
            el.append(self.p_fx.to_sdf(version))
        if self.p_fy is not None:
            el.append(self.p_fy.to_sdf(version))
        if self.p_cx is not None:
            el.append(self.p_cx.to_sdf(version))
        if self.p_cy is not None:
            el.append(self.p_cy.to_sdf(version))
        if self.tx is not None:
            el.append(self.tx.to_sdf(version))
        if self.ty is not None:
            el.append(self.ty.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Projection":
        _c_p_fx = el.find("p_fx")
        _p_fx = PFx.from_sdf(_c_p_fx, version) if _c_p_fx is not None else None
        _c_p_fy = el.find("p_fy")
        _p_fy = PFy.from_sdf(_c_p_fy, version) if _c_p_fy is not None else None
        _c_p_cx = el.find("p_cx")
        _p_cx = PCx.from_sdf(_c_p_cx, version) if _c_p_cx is not None else None
        _c_p_cy = el.find("p_cy")
        _p_cy = PCy.from_sdf(_c_p_cy, version) if _c_p_cy is not None else None
        _c_tx = el.find("tx")
        _tx = Tx.from_sdf(_c_tx, version) if _c_tx is not None else None
        _c_ty = el.find("ty")
        _ty = Ty.from_sdf(_c_ty, version) if _c_ty is not None else None
        return cls(sdf_version=version, p_fx=_p_fx, p_fy=_p_fy, p_cx=_p_cx, p_cy=_p_cy, tx=_tx, ty=_ty)


class Lens(Model):
    def __init__(
        self,
        sdf_version: str,
        type: "Type" = None,
        scale_to_hfov: "ScaleToHfov" = None,
        custom_function: "CustomFunction" = None,
        cutoff_angle: "CutoffAngle" = None,
        env_texture_size: "EnvTextureSize" = None,
        intrinsics: "Intrinsics" = None,
        projection: "Projection" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.scale_to_hfov = scale_to_hfov
        self.custom_function = custom_function
        self.cutoff_angle = cutoff_angle
        self.env_texture_size = env_texture_size
        self.intrinsics = intrinsics
        self.projection = projection

    def to_version(self, target_version: str) -> "Lens":
        if self.intrinsics is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'intrinsics' is not supported in SDF version {target_version} (added in 1.6)")
        if self.projection is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'projection' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type.to_version(target_version) if self.type is not None else None
        kwargs["scale_to_hfov"] = self.scale_to_hfov.to_version(target_version) if self.scale_to_hfov is not None else None
        kwargs["custom_function"] = self.custom_function.to_version(target_version) if self.custom_function is not None else None
        kwargs["cutoff_angle"] = self.cutoff_angle.to_version(target_version) if self.cutoff_angle is not None else None
        kwargs["env_texture_size"] = self.env_texture_size.to_version(target_version) if self.env_texture_size is not None else None
        kwargs["intrinsics"] = self.intrinsics.to_version(target_version) if self.intrinsics is not None else None
        kwargs["projection"] = self.projection.to_version(target_version) if self.projection is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lens")
        if self.type is not None:
            el.append(self.type.to_sdf(version))
        if self.scale_to_hfov is not None:
            el.append(self.scale_to_hfov.to_sdf(version))
        if self.custom_function is not None:
            el.append(self.custom_function.to_sdf(version))
        if self.cutoff_angle is not None:
            el.append(self.cutoff_angle.to_sdf(version))
        if self.env_texture_size is not None:
            el.append(self.env_texture_size.to_sdf(version))
        if self.intrinsics is not None:
            el.append(self.intrinsics.to_sdf(version))
        if self.projection is not None:
            el.append(self.projection.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Lens":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type, version) if _c_type is not None else None
        _c_scale_to_hfov = el.find("scale_to_hfov")
        _scale_to_hfov = ScaleToHfov.from_sdf(_c_scale_to_hfov, version) if _c_scale_to_hfov is not None else None
        _c_custom_function = el.find("custom_function")
        _custom_function = CustomFunction.from_sdf(_c_custom_function, version) if _c_custom_function is not None else None
        _c_cutoff_angle = el.find("cutoff_angle")
        _cutoff_angle = CutoffAngle.from_sdf(_c_cutoff_angle, version) if _c_cutoff_angle is not None else None
        _c_env_texture_size = el.find("env_texture_size")
        _env_texture_size = EnvTextureSize.from_sdf(_c_env_texture_size, version) if _c_env_texture_size is not None else None
        _c_intrinsics = el.find("intrinsics")
        _intrinsics = Intrinsics.from_sdf(_c_intrinsics, version) if _c_intrinsics is not None else None
        if _intrinsics is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'intrinsics' is not supported in SDF version {version} (added in 1.6)")
        _c_projection = el.find("projection")
        _projection = Projection.from_sdf(_c_projection, version) if _c_projection is not None else None
        if _projection is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'projection' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, type=_type, scale_to_hfov=_scale_to_hfov, custom_function=_custom_function, cutoff_angle=_cutoff_angle, env_texture_size=_env_texture_size, intrinsics=_intrinsics, projection=_projection)


class CameraInfoTopic(Model):
    def __init__(self, sdf_version: str, camera_info_topic: str = "__default__"):
        self.__version__ = sdf_version
        self.camera_info_topic = camera_info_topic

    def to_version(self, target_version: str) -> "CameraInfoTopic":
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["camera_info_topic"] = self.camera_info_topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera_info_topic")
        if self.camera_info_topic is not None:
            el.text = self.camera_info_topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CameraInfoTopic":
        _text = el.text or "__default__"
        _camera_info_topic = _text
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            if _camera_info_topic != "__default__":
                raise ValueError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, camera_info_topic=_camera_info_topic)


class VisibilityMask(Model):
    def __init__(self, sdf_version: str, visibility_mask: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "VisibilityMask":
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_mask"] = self.visibility_mask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visibility_mask")
        if self.visibility_mask is not None:
            el.text = str(self.visibility_mask)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VisibilityMask":
        _text = el.text or 4294967295
        _visibility_mask = _parse_uint32(_text)
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            if _visibility_mask != 4294967295:
                raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_mask=_visibility_mask)


class OpticalFrameId(Model):
    def __init__(self, sdf_version: str, optical_frame_id: str = ""):
        self.__version__ = sdf_version
        self.optical_frame_id = optical_frame_id

    def to_version(self, target_version: str) -> "OpticalFrameId":
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["optical_frame_id"] = self.optical_frame_id
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("optical_frame_id")
        if self.optical_frame_id is not None:
            el.text = self.optical_frame_id
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "OpticalFrameId":
        _text = el.text or ""
        _optical_frame_id = _text
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            if _optical_frame_id != "":
                raise ValueError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, optical_frame_id=_optical_frame_id)


class Triggered(Model):
    def __init__(self, sdf_version: str, triggered: bool = False):
        self.__version__ = sdf_version
        self.triggered = triggered

    def to_version(self, target_version: str) -> "Triggered":
        if self.triggered is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["triggered"] = self.triggered
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("triggered")
        if self.triggered is not None:
            el.text = str(self.triggered).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Triggered":
        _text = el.text or False
        _triggered = _text.strip().lower() == 'true'
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            if _triggered != False:
                raise ValueError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, triggered=_triggered)


class TriggerTopic(Model):
    def __init__(self, sdf_version: str, trigger_topic: str = ""):
        self.__version__ = sdf_version
        self.trigger_topic = trigger_topic

    def to_version(self, target_version: str) -> "TriggerTopic":
        if self.trigger_topic is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["trigger_topic"] = self.trigger_topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("trigger_topic")
        if self.trigger_topic is not None:
            el.text = self.trigger_topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "TriggerTopic":
        _text = el.text or ""
        _trigger_topic = _text
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            if _trigger_topic != "":
                raise ValueError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, trigger_topic=_trigger_topic)


class SegmentationType(Model):
    def __init__(self, sdf_version: str, segmentation_type: str = "semantic"):
        self.__version__ = sdf_version
        self.segmentation_type = segmentation_type

    def to_version(self, target_version: str) -> "SegmentationType":
        if self.segmentation_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["segmentation_type"] = self.segmentation_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("segmentation_type")
        if self.segmentation_type is not None:
            el.text = self.segmentation_type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "SegmentationType":
        _text = el.text or "semantic"
        _segmentation_type = _text
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            if _segmentation_type != "semantic":
                raise ValueError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, segmentation_type=_segmentation_type)


class BoxType(Model):
    def __init__(self, sdf_version: str, box_type: str = "2d"):
        self.__version__ = sdf_version
        self.box_type = box_type

    def to_version(self, target_version: str) -> "BoxType":
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["box_type"] = self.box_type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("box_type")
        if self.box_type is not None:
            el.text = self.box_type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "BoxType":
        _text = el.text or "2d"
        _box_type = _text
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            if _box_type != "2d":
                raise ValueError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, box_type=_box_type)


class Camera(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        pose: "Pose" = None,
        horizontal_fov: "HorizontalFov" = None,
        image: "Image" = None,
        clip: "Clip" = None,
        save: "Save" = None,
        depth_camera: "DepthCamera" = None,
        noise: "Noise" = None,
        frame: List["Frame"] = None,
        distortion: "Distortion" = None,
        lens: "Lens" = None,
        camera_info_topic: "CameraInfoTopic" = None,
        visibility_mask: "VisibilityMask" = None,
        optical_frame_id: "OpticalFrameId" = None,
        triggered: "Triggered" = None,
        trigger_topic: "TriggerTopic" = None,
        segmentation_type: "SegmentationType" = None,
        box_type: "BoxType" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose
        self.horizontal_fov = horizontal_fov
        self.image = image
        self.clip = clip
        self.save = save
        self.depth_camera = depth_camera
        self.noise = noise
        self.frame = frame or []
        self.distortion = distortion
        self.lens = lens
        self.camera_info_topic = camera_info_topic
        self.visibility_mask = visibility_mask
        self.optical_frame_id = optical_frame_id
        self.triggered = triggered
        self.trigger_topic = trigger_topic
        self.segmentation_type = segmentation_type
        self.box_type = box_type

    def to_version(self, target_version: str) -> "Camera":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.distortion is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'distortion' is not supported in SDF version {target_version} (added in 1.5)")
        if self.lens is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'lens' is not supported in SDF version {target_version} (added in 1.5)")
        if self.camera_info_topic is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {target_version} (added in 1.7)")
        if self.visibility_mask is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.7)")
        if self.optical_frame_id is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {target_version} (added in 1.7)")
        if self.triggered is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {target_version} (added in 1.9)")
        if self.trigger_topic is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {target_version} (added in 1.9)")
        if self.segmentation_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {target_version} (added in 1.9)")
        if self.box_type is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["horizontal_fov"] = self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["clip"] = self.clip.to_version(target_version) if self.clip is not None else None
        kwargs["save"] = self.save.to_version(target_version) if self.save is not None else None
        kwargs["depth_camera"] = self.depth_camera.to_version(target_version) if self.depth_camera is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["distortion"] = self.distortion.to_version(target_version) if self.distortion is not None else None
        kwargs["lens"] = self.lens.to_version(target_version) if self.lens is not None else None
        kwargs["camera_info_topic"] = self.camera_info_topic.to_version(target_version) if self.camera_info_topic is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        kwargs["optical_frame_id"] = self.optical_frame_id.to_version(target_version) if self.optical_frame_id is not None else None
        kwargs["triggered"] = self.triggered.to_version(target_version) if self.triggered is not None else None
        kwargs["trigger_topic"] = self.trigger_topic.to_version(target_version) if self.trigger_topic is not None else None
        kwargs["segmentation_type"] = self.segmentation_type.to_version(target_version) if self.segmentation_type is not None else None
        kwargs["box_type"] = self.box_type.to_version(target_version) if self.box_type is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("camera")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf(version))
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.clip is not None:
            el.append(self.clip.to_sdf(version))
        if self.save is not None:
            el.append(self.save.to_sdf(version))
        if self.depth_camera is not None:
            el.append(self.depth_camera.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.distortion is not None:
            el.append(self.distortion.to_sdf(version))
        if self.lens is not None:
            el.append(self.lens.to_sdf(version))
        if self.camera_info_topic is not None:
            el.append(self.camera_info_topic.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        if self.optical_frame_id is not None:
            el.append(self.optical_frame_id.to_sdf(version))
        if self.triggered is not None:
            el.append(self.triggered.to_sdf(version))
        if self.trigger_topic is not None:
            el.append(self.trigger_topic.to_sdf(version))
        if self.segmentation_type is not None:
            el.append(self.segmentation_type.to_sdf(version))
        if self.box_type is not None:
            el.append(self.box_type.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Camera":
        _name = el.get("name", "__default__")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        _c_horizontal_fov = el.find("horizontal_fov")
        _horizontal_fov = HorizontalFov.from_sdf(_c_horizontal_fov, version) if _c_horizontal_fov is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image, version) if _c_image is not None else None
        _c_clip = el.find("clip")
        _clip = Clip.from_sdf(_c_clip, version) if _c_clip is not None else None
        _c_save = el.find("save")
        _save = Save.from_sdf(_c_save, version) if _c_save is not None else None
        _c_depth_camera = el.find("depth_camera")
        _depth_camera = DepthCamera.from_sdf(_c_depth_camera, version) if _c_depth_camera is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        _frame = [Frame.from_sdf(c, version) for c in el.findall("frame")]
        if _frame and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_distortion = el.find("distortion")
        _distortion = Distortion.from_sdf(_c_distortion, version) if _c_distortion is not None else None
        if _distortion is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'distortion' is not supported in SDF version {version} (added in 1.5)")
        _c_lens = el.find("lens")
        _lens = Lens.from_sdf(_c_lens, version) if _c_lens is not None else None
        if _lens is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'lens' is not supported in SDF version {version} (added in 1.5)")
        _c_camera_info_topic = el.find("camera_info_topic")
        _camera_info_topic = CameraInfoTopic.from_sdf(_c_camera_info_topic, version) if _c_camera_info_topic is not None else None
        if _camera_info_topic is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'camera_info_topic' is not supported in SDF version {version} (added in 1.7)")
        _c_visibility_mask = el.find("visibility_mask")
        _visibility_mask = VisibilityMask.from_sdf(_c_visibility_mask, version) if _c_visibility_mask is not None else None
        if _visibility_mask is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.7)")
        _c_optical_frame_id = el.find("optical_frame_id")
        _optical_frame_id = OpticalFrameId.from_sdf(_c_optical_frame_id, version) if _c_optical_frame_id is not None else None
        if _optical_frame_id is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'optical_frame_id' is not supported in SDF version {version} (added in 1.7)")
        _c_triggered = el.find("triggered")
        _triggered = Triggered.from_sdf(_c_triggered, version) if _c_triggered is not None else None
        if _triggered is not None and cmp_version(version, "1.9") < 0:
            raise ValueError(f"'triggered' is not supported in SDF version {version} (added in 1.9)")
        _c_trigger_topic = el.find("trigger_topic")
        _trigger_topic = TriggerTopic.from_sdf(_c_trigger_topic, version) if _c_trigger_topic is not None else None
        if _trigger_topic is not None and cmp_version(version, "1.9") < 0:
            raise ValueError(f"'trigger_topic' is not supported in SDF version {version} (added in 1.9)")
        _c_segmentation_type = el.find("segmentation_type")
        _segmentation_type = SegmentationType.from_sdf(_c_segmentation_type, version) if _c_segmentation_type is not None else None
        if _segmentation_type is not None and cmp_version(version, "1.9") < 0:
            raise ValueError(f"'segmentation_type' is not supported in SDF version {version} (added in 1.9)")
        _c_box_type = el.find("box_type")
        _box_type = BoxType.from_sdf(_c_box_type, version) if _c_box_type is not None else None
        if _box_type is not None and cmp_version(version, "1.9") < 0:
            raise ValueError(f"'box_type' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, name=_name, pose=_pose, horizontal_fov=_horizontal_fov, image=_image, clip=_clip, save=_save, depth_camera=_depth_camera, noise=_noise, frame=_frame, distortion=_distortion, lens=_lens, camera_info_topic=_camera_info_topic, visibility_mask=_visibility_mask, optical_frame_id=_optical_frame_id, triggered=_triggered, trigger_topic=_trigger_topic, segmentation_type=_segmentation_type, box_type=_box_type)


class Collision(Model):
    def __init__(self, sdf_version: str, collision: str = "__default__"):
        self.__version__ = sdf_version
        self.collision = collision

    def to_version(self, target_version: str) -> "Collision":
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = self.collision
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision")
        if self.collision is not None:
            el.text = self.collision
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Collision":
        _text = el.text or "__default__"
        _collision = _text
        return cls(sdf_version=version, collision=_collision)


class Topic(Model):
    def __init__(self, sdf_version: str, topic: str = "__default_topic__"):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "Topic":
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Topic":
        _text = el.text or "__default_topic__"
        _topic = _text
        return cls(sdf_version=version, topic=_topic)


class Contact(Model):
    def __init__(self, sdf_version: str, collision: "Collision" = None, topic: "Topic" = None):
        self.__version__ = sdf_version
        self.collision = collision
        self.topic = topic

    def to_version(self, target_version: str) -> "Contact":
        kwargs = {"sdf_version": target_version}
        kwargs["collision"] = self.collision.to_version(target_version) if self.collision is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.collision is not None:
            el.append(self.collision.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Contact":
        _c_collision = el.find("collision")
        _collision = Collision.from_sdf(_c_collision, version) if _c_collision is not None else None
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic, version) if _c_topic is not None else None
        return cls(sdf_version=version, collision=_collision, topic=_topic)


class MeasureDirection(Model):
    def __init__(self, sdf_version: str, measure_direction: str = "child_to_parent"):
        self.__version__ = sdf_version
        self.measure_direction = measure_direction

    def to_version(self, target_version: str) -> "MeasureDirection":
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["measure_direction"] = self.measure_direction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("measure_direction")
        if self.measure_direction is not None:
            el.text = self.measure_direction
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MeasureDirection":
        _text = el.text or "child_to_parent"
        _measure_direction = _text
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            if _measure_direction != "child_to_parent":
                raise ValueError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, measure_direction=_measure_direction)


class X(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "X":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("x")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "X":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Y(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Y":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("y")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Y":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Z(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Z":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("z")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Z":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Force(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Force":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("force")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Force":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class Torque(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Torque":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("torque")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Torque":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class ForceTorque(Model):
    def __init__(
        self,
        sdf_version: str,
        frame: "Frame" = None,
        measure_direction: "MeasureDirection" = None,
        force: "Force" = None,
        torque: "Torque" = None
    ):
        self.__version__ = sdf_version
        self.frame = frame
        self.measure_direction = measure_direction
        self.force = force
        self.torque = torque

    def to_version(self, target_version: str) -> "ForceTorque":
        if self.measure_direction is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {target_version} (added in 1.5)")
        if self.force is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {target_version} (added in 1.7)")
        if self.torque is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame.to_version(target_version) if self.frame is not None else None
        kwargs["measure_direction"] = self.measure_direction.to_version(target_version) if self.measure_direction is not None else None
        kwargs["force"] = self.force.to_version(target_version) if self.force is not None else None
        kwargs["torque"] = self.torque.to_version(target_version) if self.torque is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("force_torque")
        if self.frame is not None:
            el.append(self.frame.to_sdf(version))
        if self.measure_direction is not None:
            el.append(self.measure_direction.to_sdf(version))
        if self.force is not None:
            el.append(self.force.to_sdf(version))
        if self.torque is not None:
            el.append(self.torque.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ForceTorque":
        _c_frame = el.find("frame")
        _frame = Frame.from_sdf(_c_frame, version) if _c_frame is not None else None
        _c_measure_direction = el.find("measure_direction")
        _measure_direction = MeasureDirection.from_sdf(_c_measure_direction, version) if _c_measure_direction is not None else None
        if _measure_direction is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'measure_direction' is not supported in SDF version {version} (added in 1.5)")
        _c_force = el.find("force")
        _force = Force.from_sdf(_c_force, version) if _c_force is not None else None
        if _force is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'force' is not supported in SDF version {version} (added in 1.7)")
        _c_torque = el.find("torque")
        _torque = Torque.from_sdf(_c_torque, version) if _c_torque is not None else None
        if _torque is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'torque' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, frame=_frame, measure_direction=_measure_direction, force=_force, torque=_torque)


class Horizontal(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Horizontal":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("horizontal")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Horizontal":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Vertical(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Vertical":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Vertical":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class PositionSensing(Model):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "Horizontal" = None,
        vertical: "Vertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "PositionSensing":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("position_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "PositionSensing":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal, version) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical, version) if _c_vertical is not None else None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class VelocitySensing(Model):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "Horizontal" = None,
        vertical: "Vertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "VelocitySensing":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("velocity_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VelocitySensing":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal, version) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical, version) if _c_vertical is not None else None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Gps(Model):
    def __init__(
        self,
        sdf_version: str,
        position_sensing: "PositionSensing" = None,
        velocity_sensing: "VelocitySensing" = None
    ):
        self.__version__ = sdf_version
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_version(self, target_version: str) -> "Gps":
        kwargs = {"sdf_version": target_version}
        kwargs["position_sensing"] = self.position_sensing.to_version(target_version) if self.position_sensing is not None else None
        kwargs["velocity_sensing"] = self.velocity_sensing.to_version(target_version) if self.velocity_sensing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gps")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf(version))
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gps":
        _c_position_sensing = el.find("position_sensing")
        _position_sensing = PositionSensing.from_sdf(_c_position_sensing, version) if _c_position_sensing is not None else None
        _c_velocity_sensing = el.find("velocity_sensing")
        _velocity_sensing = VelocitySensing.from_sdf(_c_velocity_sensing, version) if _c_velocity_sensing is not None else None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class AngularVelocity(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "AngularVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("angular_velocity")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AngularVelocity":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class LinearAcceleration(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "LinearAcceleration":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("linear_acceleration")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LinearAcceleration":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class Localization(Model):
    def __init__(self, sdf_version: str, localization: str = "CUSTOM"):
        self.__version__ = sdf_version
        self.localization = localization

    def to_version(self, target_version: str) -> "Localization":
        kwargs = {"sdf_version": target_version}
        kwargs["localization"] = self.localization
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("localization")
        if self.localization is not None:
            el.text = self.localization
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Localization":
        _text = el.text or "CUSTOM"
        _localization = _text
        return cls(sdf_version=version, localization=_localization)


class CustomRpy(Model):
    def __init__(self, sdf_version: str, custom_rpy: Vector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if custom_rpy is None:
            custom_rpy = Vector3.from_sdf("0 0 0")
        self.custom_rpy = custom_rpy
        self.parent_frame = parent_frame

    def to_version(self, target_version: str) -> "CustomRpy":
        kwargs = {"sdf_version": target_version}
        kwargs["custom_rpy"] = self.custom_rpy
        kwargs["parent_frame"] = self.parent_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("custom_rpy")
        if self.custom_rpy is not None:
            el.text = self.custom_rpy.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "CustomRpy":
        _text = el.text or "0 0 0"
        _custom_rpy = Vector3.from_sdf(_text)
        _parent_frame = el.get("parent_frame", "")
        return cls(sdf_version=version, custom_rpy=_custom_rpy, parent_frame=_parent_frame)


class GravDirX(Model):
    def __init__(self, sdf_version: str, grav_dir_x: Vector3 = None, parent_frame: str = ""):
        self.__version__ = sdf_version
        if grav_dir_x is None:
            grav_dir_x = Vector3.from_sdf("1 0 0")
        self.grav_dir_x = grav_dir_x
        self.parent_frame = parent_frame

    def to_version(self, target_version: str) -> "GravDirX":
        kwargs = {"sdf_version": target_version}
        kwargs["grav_dir_x"] = self.grav_dir_x
        kwargs["parent_frame"] = self.parent_frame
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("grav_dir_x")
        if self.grav_dir_x is not None:
            el.text = self.grav_dir_x.to_sdf()
        if self.parent_frame is not None:
            el.set("parent_frame", self.parent_frame)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "GravDirX":
        _text = el.text or "1 0 0"
        _grav_dir_x = Vector3.from_sdf(_text)
        _parent_frame = el.get("parent_frame", "")
        return cls(sdf_version=version, grav_dir_x=_grav_dir_x, parent_frame=_parent_frame)


class OrientationReferenceFrame(Model):
    def __init__(
        self,
        sdf_version: str,
        localization: "Localization" = None,
        custom_rpy: "CustomRpy" = None,
        grav_dir_x: "GravDirX" = None
    ):
        self.__version__ = sdf_version
        self.localization = localization
        self.custom_rpy = custom_rpy
        self.grav_dir_x = grav_dir_x

    def to_version(self, target_version: str) -> "OrientationReferenceFrame":
        kwargs = {"sdf_version": target_version}
        kwargs["localization"] = self.localization.to_version(target_version) if self.localization is not None else None
        kwargs["custom_rpy"] = self.custom_rpy.to_version(target_version) if self.custom_rpy is not None else None
        kwargs["grav_dir_x"] = self.grav_dir_x.to_version(target_version) if self.grav_dir_x is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("orientation_reference_frame")
        if self.localization is not None:
            el.append(self.localization.to_sdf(version))
        if self.custom_rpy is not None:
            el.append(self.custom_rpy.to_sdf(version))
        if self.grav_dir_x is not None:
            el.append(self.grav_dir_x.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "OrientationReferenceFrame":
        _c_localization = el.find("localization")
        _localization = Localization.from_sdf(_c_localization, version) if _c_localization is not None else None
        _c_custom_rpy = el.find("custom_rpy")
        _custom_rpy = CustomRpy.from_sdf(_c_custom_rpy, version) if _c_custom_rpy is not None else None
        _c_grav_dir_x = el.find("grav_dir_x")
        _grav_dir_x = GravDirX.from_sdf(_c_grav_dir_x, version) if _c_grav_dir_x is not None else None
        return cls(sdf_version=version, localization=_localization, custom_rpy=_custom_rpy, grav_dir_x=_grav_dir_x)


class EnableOrientation(Model):
    def __init__(self, sdf_version: str, enable_orientation: bool = True):
        self.__version__ = sdf_version
        self.enable_orientation = enable_orientation

    def to_version(self, target_version: str) -> "EnableOrientation":
        if self.enable_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_orientation"] = self.enable_orientation
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_orientation")
        if self.enable_orientation is not None:
            el.text = str(self.enable_orientation).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EnableOrientation":
        _text = el.text or True
        _enable_orientation = _text.strip().lower() == 'true'
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            if _enable_orientation != True:
                raise ValueError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, enable_orientation=_enable_orientation)


class Imu(Model):
    _MIGRATIONS = [{"version": "1.6", "ops": [{"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}, {"type": "move", "from": "noise::type", "to": "linear_acceleration::z::noise::type"}, {"type": "move", "from": "noise::rate::mean", "to": "angular_velocity::z::noise::mean"}, {"type": "move", "from": "noise::rate::stddev", "to": "angular_velocity::z::noise::stddev"}, {"type": "move", "from": "noise::rate::bias_mean", "to": "angular_velocity::z::noise::bias_mean"}, {"type": "move", "from": "noise::rate::bias_stddev", "to": "angular_velocity::z::noise::bias_stddev"}, {"type": "move", "from": "noise::accel::mean", "to": "linear_acceleration::z::noise::mean"}, {"type": "move", "from": "noise::accel::stddev", "to": "linear_acceleration::z::noise::stddev"}, {"type": "move", "from": "noise::accel::bias_mean", "to": "linear_acceleration::z::noise::bias_mean"}, {"type": "move", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::z::noise::bias_stddev"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::y::noise::type"}, {"type": "copy", "from": "noise::type", "to": "angular_velocity::z::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::x::noise::type"}, {"type": "copy", "from": "noise::type", "to": "linear_acceleration::y::noise::type"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::x::noise::mean"}, {"type": "copy", "from": "noise::rate::mean", "to": "angular_velocity::y::noise::mean"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::x::noise::stddev"}, {"type": "copy", "from": "noise::rate::stddev", "to": "angular_velocity::y::noise::stddev"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::x::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_mean", "to": "angular_velocity::y::noise::bias_mean"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::rate::bias_stddev", "to": "angular_velocity::y::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::x::noise::mean"}, {"type": "copy", "from": "noise::accel::mean", "to": "linear_acceleration::y::noise::mean"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::x::noise::stddev"}, {"type": "copy", "from": "noise::accel::stddev", "to": "linear_acceleration::y::noise::stddev"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::x::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_mean", "to": "linear_acceleration::y::noise::bias_mean"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::x::noise::bias_stddev"}, {"type": "copy", "from": "noise::accel::bias_stddev", "to": "linear_acceleration::y::noise::bias_stddev"}]}]

    def __init__(
        self,
        sdf_version: str,
        topic: "Topic" = None,
        noise: "Noise" = None,
        angular_velocity: "AngularVelocity" = None,
        linear_acceleration: "LinearAcceleration" = None,
        orientation_reference_frame: "OrientationReferenceFrame" = None,
        enable_orientation: "EnableOrientation" = None
    ):
        self.__version__ = sdf_version
        self.topic = topic
        self.noise = noise
        self.angular_velocity = angular_velocity
        self.linear_acceleration = linear_acceleration
        self.orientation_reference_frame = orientation_reference_frame
        self.enable_orientation = enable_orientation

    def to_version(self, target_version: str) -> "Imu":
        if self.angular_velocity is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'angular_velocity' is not supported in SDF version {target_version} (added in 1.5)")
        if self.linear_acceleration is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'linear_acceleration' is not supported in SDF version {target_version} (added in 1.5)")
        if self.orientation_reference_frame is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'orientation_reference_frame' is not supported in SDF version {target_version} (added in 1.6)")
        if self.enable_orientation is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["angular_velocity"] = self.angular_velocity.to_version(target_version) if self.angular_velocity is not None else None
        kwargs["linear_acceleration"] = self.linear_acceleration.to_version(target_version) if self.linear_acceleration is not None else None
        kwargs["orientation_reference_frame"] = self.orientation_reference_frame.to_version(target_version) if self.orientation_reference_frame is not None else None
        kwargs["enable_orientation"] = self.enable_orientation.to_version(target_version) if self.enable_orientation is not None else None
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("imu")
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.angular_velocity is not None:
            el.append(self.angular_velocity.to_sdf(version))
        if self.linear_acceleration is not None:
            el.append(self.linear_acceleration.to_sdf(version))
        if self.orientation_reference_frame is not None:
            el.append(self.orientation_reference_frame.to_sdf(version))
        if self.enable_orientation is not None:
            el.append(self.enable_orientation.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Imu":
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic, version) if _c_topic is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        _c_angular_velocity = el.find("angular_velocity")
        _angular_velocity = AngularVelocity.from_sdf(_c_angular_velocity, version) if _c_angular_velocity is not None else None
        if _angular_velocity is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'angular_velocity' is not supported in SDF version {version} (added in 1.5)")
        _c_linear_acceleration = el.find("linear_acceleration")
        _linear_acceleration = LinearAcceleration.from_sdf(_c_linear_acceleration, version) if _c_linear_acceleration is not None else None
        if _linear_acceleration is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'linear_acceleration' is not supported in SDF version {version} (added in 1.5)")
        _c_orientation_reference_frame = el.find("orientation_reference_frame")
        _orientation_reference_frame = OrientationReferenceFrame.from_sdf(_c_orientation_reference_frame, version) if _c_orientation_reference_frame is not None else None
        if _orientation_reference_frame is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'orientation_reference_frame' is not supported in SDF version {version} (added in 1.6)")
        _c_enable_orientation = el.find("enable_orientation")
        _enable_orientation = EnableOrientation.from_sdf(_c_enable_orientation, version) if _c_enable_orientation is not None else None
        if _enable_orientation is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'enable_orientation' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, topic=_topic, noise=_noise, angular_velocity=_angular_velocity, linear_acceleration=_linear_acceleration, orientation_reference_frame=_orientation_reference_frame, enable_orientation=_enable_orientation)


class Scan(Model):
    def __init__(
        self,
        sdf_version: str,
        horizontal: "Horizontal" = None,
        vertical: "Vertical" = None
    ):
        self.__version__ = sdf_version
        self.horizontal = horizontal
        self.vertical = vertical

    def to_version(self, target_version: str) -> "Scan":
        kwargs = {"sdf_version": target_version}
        kwargs["horizontal"] = self.horizontal.to_version(target_version) if self.horizontal is not None else None
        kwargs["vertical"] = self.vertical.to_version(target_version) if self.vertical is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scan")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf(version))
        if self.vertical is not None:
            el.append(self.vertical.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Scan":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal, version) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical, version) if _c_vertical is not None else None
        return cls(sdf_version=version, horizontal=_horizontal, vertical=_vertical)


class Min(Model):
    def __init__(self, sdf_version: str, min: float = 0):
        self.__version__ = sdf_version
        self.min = min

    def to_version(self, target_version: str) -> "Min":
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min")
        if self.min is not None:
            el.text = str(self.min)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Min":
        _text = el.text or 0
        _min = _parse_double(_text)
        return cls(sdf_version=version, min=_min)


class Max(Model):
    def __init__(self, sdf_version: str, max: float = 0):
        self.__version__ = sdf_version
        self.max = max

    def to_version(self, target_version: str) -> "Max":
        kwargs = {"sdf_version": target_version}
        kwargs["max"] = self.max
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max")
        if self.max is not None:
            el.text = str(self.max)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Max":
        _text = el.text or 0
        _max = _parse_double(_text)
        return cls(sdf_version=version, max=_max)


class Resolution(Model):
    def __init__(self, sdf_version: str, resolution: float = 0):
        self.__version__ = sdf_version
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Resolution":
        kwargs = {"sdf_version": target_version}
        kwargs["resolution"] = self.resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("resolution")
        if self.resolution is not None:
            el.text = str(self.resolution)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Resolution":
        _text = el.text or 0
        _resolution = _parse_double(_text)
        return cls(sdf_version=version, resolution=_resolution)


class Range(Model):
    def __init__(
        self,
        sdf_version: str,
        min: "Min" = None,
        max: "Max" = None,
        resolution: "Resolution" = None
    ):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_version(self, target_version: str) -> "Range":
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min.to_version(target_version) if self.min is not None else None
        kwargs["max"] = self.max.to_version(target_version) if self.max is not None else None
        kwargs["resolution"] = self.resolution.to_version(target_version) if self.resolution is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("range")
        if self.min is not None:
            el.append(self.min.to_sdf(version))
        if self.max is not None:
            el.append(self.max.to_sdf(version))
        if self.resolution is not None:
            el.append(self.resolution.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Range":
        _c_min = el.find("min")
        _min = Min.from_sdf(_c_min, version) if _c_min is not None else None
        _c_max = el.find("max")
        _max = Max.from_sdf(_c_max, version) if _c_max is not None else None
        _c_resolution = el.find("resolution")
        _resolution = Resolution.from_sdf(_c_resolution, version) if _c_resolution is not None else None
        return cls(sdf_version=version, min=_min, max=_max, resolution=_resolution)


class Ray(Model):
    def __init__(
        self,
        sdf_version: str,
        scan: "Scan" = None,
        range: "Range" = None,
        noise: "Noise" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.scan = scan
        self.range = range
        self.noise = noise
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "Ray":
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ray")
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Ray":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan, version) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range, version) if _c_range is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        _c_visibility_mask = el.find("visibility_mask")
        _visibility_mask = VisibilityMask.from_sdf(_c_visibility_mask, version) if _c_visibility_mask is not None else None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)


class Rfidtag(Model):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "Rfidtag":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rfidtag")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Rfidtag":
        return cls(sdf_version=version)


class Rfid(Model):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "Rfid":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rfid")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Rfid":
        return cls(sdf_version=version)


class Radius(Model):
    def __init__(self, sdf_version: str, radius: float = 0.5):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Radius":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("radius")
        if self.radius is not None:
            el.text = str(self.radius)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Radius":
        _text = el.text or 0.5
        _radius = _parse_double(_text)
        return cls(sdf_version=version, radius=_radius)


class Geometry(Model):
    def __init__(self, sdf_version: str, geometry: str = "cone"):
        self.__version__ = sdf_version
        self.geometry = geometry

    def to_version(self, target_version: str) -> "Geometry":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["geometry"] = self.geometry
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("geometry")
        if self.geometry is not None:
            el.text = self.geometry
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Geometry":
        _text = el.text or "cone"
        _geometry = _text
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            if _geometry != "cone":
                raise ValueError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, geometry=_geometry)


class Sonar(Model):
    def __init__(
        self,
        sdf_version: str,
        min: "Min" = None,
        max: "Max" = None,
        radius: "Radius" = None,
        geometry: "Geometry" = None
    ):
        self.__version__ = sdf_version
        self.min = min
        self.max = max
        self.radius = radius
        self.geometry = geometry

    def to_version(self, target_version: str) -> "Sonar":
        if self.geometry is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["min"] = self.min.to_version(target_version) if self.min is not None else None
        kwargs["max"] = self.max.to_version(target_version) if self.max is not None else None
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sonar")
        if self.min is not None:
            el.append(self.min.to_sdf(version))
        if self.max is not None:
            el.append(self.max.to_sdf(version))
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sonar":
        _c_min = el.find("min")
        _min = Min.from_sdf(_c_min, version) if _c_min is not None else None
        _c_max = el.find("max")
        _max = Max.from_sdf(_c_max, version) if _c_max is not None else None
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius, version) if _c_radius is not None else None
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry, version) if _c_geometry is not None else None
        if _geometry is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'geometry' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, min=_min, max=_max, radius=_radius, geometry=_geometry)


class Essid(Model):
    def __init__(self, sdf_version: str, essid: str = "wireless"):
        self.__version__ = sdf_version
        self.essid = essid

    def to_version(self, target_version: str) -> "Essid":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("essid")
        if self.essid is not None:
            el.text = self.essid
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Essid":
        _text = el.text or "wireless"
        _essid = _text
        return cls(sdf_version=version, essid=_essid)


class Frequency(Model):
    def __init__(self, sdf_version: str, frequency: float = 2442):
        self.__version__ = sdf_version
        self.frequency = frequency

    def to_version(self, target_version: str) -> "Frequency":
        kwargs = {"sdf_version": target_version}
        kwargs["frequency"] = self.frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frequency")
        if self.frequency is not None:
            el.text = str(self.frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Frequency":
        _text = el.text or 2442
        _frequency = _parse_double(_text)
        return cls(sdf_version=version, frequency=_frequency)


class MinFrequency(Model):
    def __init__(self, sdf_version: str, min_frequency: float = 2412):
        self.__version__ = sdf_version
        self.min_frequency = min_frequency

    def to_version(self, target_version: str) -> "MinFrequency":
        kwargs = {"sdf_version": target_version}
        kwargs["min_frequency"] = self.min_frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_frequency")
        if self.min_frequency is not None:
            el.text = str(self.min_frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MinFrequency":
        _text = el.text or 2412
        _min_frequency = _parse_double(_text)
        return cls(sdf_version=version, min_frequency=_min_frequency)


class MaxFrequency(Model):
    def __init__(self, sdf_version: str, max_frequency: float = 2484):
        self.__version__ = sdf_version
        self.max_frequency = max_frequency

    def to_version(self, target_version: str) -> "MaxFrequency":
        kwargs = {"sdf_version": target_version}
        kwargs["max_frequency"] = self.max_frequency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_frequency")
        if self.max_frequency is not None:
            el.text = str(self.max_frequency)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxFrequency":
        _text = el.text or 2484
        _max_frequency = _parse_double(_text)
        return cls(sdf_version=version, max_frequency=_max_frequency)


class Gain(Model):
    def __init__(self, sdf_version: str, gain: float = 2.5):
        self.__version__ = sdf_version
        self.gain = gain

    def to_version(self, target_version: str) -> "Gain":
        kwargs = {"sdf_version": target_version}
        kwargs["gain"] = self.gain
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gain")
        if self.gain is not None:
            el.text = str(self.gain)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Gain":
        _text = el.text or 2.5
        _gain = _parse_double(_text)
        return cls(sdf_version=version, gain=_gain)


class Power(Model):
    def __init__(self, sdf_version: str, power: float = 14.50):
        self.__version__ = sdf_version
        self.power = power

    def to_version(self, target_version: str) -> "Power":
        kwargs = {"sdf_version": target_version}
        kwargs["power"] = self.power
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("power")
        if self.power is not None:
            el.text = str(self.power)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Power":
        _text = el.text or 14.50
        _power = _parse_double(_text)
        return cls(sdf_version=version, power=_power)


class Sensitivity(Model):
    def __init__(self, sdf_version: str, sensitivity: float = -90):
        self.__version__ = sdf_version
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Sensitivity":
        kwargs = {"sdf_version": target_version}
        kwargs["sensitivity"] = self.sensitivity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sensitivity")
        if self.sensitivity is not None:
            el.text = str(self.sensitivity)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sensitivity":
        _text = el.text or -90
        _sensitivity = _parse_double(_text)
        return cls(sdf_version=version, sensitivity=_sensitivity)


class Transceiver(Model):
    def __init__(
        self,
        sdf_version: str,
        essid: "Essid" = None,
        frequency: "Frequency" = None,
        min_frequency: "MinFrequency" = None,
        max_frequency: "MaxFrequency" = None,
        gain: "Gain" = None,
        power: "Power" = None,
        sensitivity: "Sensitivity" = None
    ):
        self.__version__ = sdf_version
        self.essid = essid
        self.frequency = frequency
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.gain = gain
        self.power = power
        self.sensitivity = sensitivity

    def to_version(self, target_version: str) -> "Transceiver":
        kwargs = {"sdf_version": target_version}
        kwargs["essid"] = self.essid.to_version(target_version) if self.essid is not None else None
        kwargs["frequency"] = self.frequency.to_version(target_version) if self.frequency is not None else None
        kwargs["min_frequency"] = self.min_frequency.to_version(target_version) if self.min_frequency is not None else None
        kwargs["max_frequency"] = self.max_frequency.to_version(target_version) if self.max_frequency is not None else None
        kwargs["gain"] = self.gain.to_version(target_version) if self.gain is not None else None
        kwargs["power"] = self.power.to_version(target_version) if self.power is not None else None
        kwargs["sensitivity"] = self.sensitivity.to_version(target_version) if self.sensitivity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("transceiver")
        if self.essid is not None:
            el.append(self.essid.to_sdf(version))
        if self.frequency is not None:
            el.append(self.frequency.to_sdf(version))
        if self.min_frequency is not None:
            el.append(self.min_frequency.to_sdf(version))
        if self.max_frequency is not None:
            el.append(self.max_frequency.to_sdf(version))
        if self.gain is not None:
            el.append(self.gain.to_sdf(version))
        if self.power is not None:
            el.append(self.power.to_sdf(version))
        if self.sensitivity is not None:
            el.append(self.sensitivity.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Transceiver":
        _c_essid = el.find("essid")
        _essid = Essid.from_sdf(_c_essid, version) if _c_essid is not None else None
        _c_frequency = el.find("frequency")
        _frequency = Frequency.from_sdf(_c_frequency, version) if _c_frequency is not None else None
        _c_min_frequency = el.find("min_frequency")
        _min_frequency = MinFrequency.from_sdf(_c_min_frequency, version) if _c_min_frequency is not None else None
        _c_max_frequency = el.find("max_frequency")
        _max_frequency = MaxFrequency.from_sdf(_c_max_frequency, version) if _c_max_frequency is not None else None
        _c_gain = el.find("gain")
        _gain = Gain.from_sdf(_c_gain, version) if _c_gain is not None else None
        _c_power = el.find("power")
        _power = Power.from_sdf(_c_power, version) if _c_power is not None else None
        _c_sensitivity = el.find("sensitivity")
        _sensitivity = Sensitivity.from_sdf(_c_sensitivity, version) if _c_sensitivity is not None else None
        return cls(sdf_version=version, essid=_essid, frequency=_frequency, min_frequency=_min_frequency, max_frequency=_max_frequency, gain=_gain, power=_power, sensitivity=_sensitivity)


class AlwaysOn(Model):
    def __init__(self, sdf_version: str, always_on: bool = False):
        self.__version__ = sdf_version
        self.always_on = always_on

    def to_version(self, target_version: str) -> "AlwaysOn":
        kwargs = {"sdf_version": target_version}
        kwargs["always_on"] = self.always_on
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("always_on")
        if self.always_on is not None:
            el.text = str(self.always_on).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AlwaysOn":
        _text = el.text or False
        _always_on = _text.strip().lower() == 'true'
        return cls(sdf_version=version, always_on=_always_on)


class UpdateRate(Model):
    def __init__(self, sdf_version: str, update_rate: float = 0):
        self.__version__ = sdf_version
        self.update_rate = update_rate

    def to_version(self, target_version: str) -> "UpdateRate":
        kwargs = {"sdf_version": target_version}
        kwargs["update_rate"] = self.update_rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("update_rate")
        if self.update_rate is not None:
            el.text = str(self.update_rate)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "UpdateRate":
        _text = el.text or 0
        _update_rate = _parse_double(_text)
        return cls(sdf_version=version, update_rate=_update_rate)


class Visualize(Model):
    def __init__(self, sdf_version: str, visualize: bool = False):
        self.__version__ = sdf_version
        self.visualize = visualize

    def to_version(self, target_version: str) -> "Visualize":
        kwargs = {"sdf_version": target_version}
        kwargs["visualize"] = self.visualize
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visualize")
        if self.visualize is not None:
            el.text = str(self.visualize).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Visualize":
        _text = el.text or False
        _visualize = _text.strip().lower() == 'true'
        return cls(sdf_version=version, visualize=_visualize)


class VerticalPosition(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VerticalPosition":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical_position")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VerticalPosition":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class VerticalVelocity(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "VerticalVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("vertical_velocity")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "VerticalVelocity":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class Altimeter(Model):
    def __init__(
        self,
        sdf_version: str,
        vertical_position: "VerticalPosition" = None,
        vertical_velocity: "VerticalVelocity" = None
    ):
        self.__version__ = sdf_version
        self.vertical_position = vertical_position
        self.vertical_velocity = vertical_velocity

    def to_version(self, target_version: str) -> "Altimeter":
        kwargs = {"sdf_version": target_version}
        kwargs["vertical_position"] = self.vertical_position.to_version(target_version) if self.vertical_position is not None else None
        kwargs["vertical_velocity"] = self.vertical_velocity.to_version(target_version) if self.vertical_velocity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("altimeter")
        if self.vertical_position is not None:
            el.append(self.vertical_position.to_sdf(version))
        if self.vertical_velocity is not None:
            el.append(self.vertical_velocity.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Altimeter":
        _c_vertical_position = el.find("vertical_position")
        _vertical_position = VerticalPosition.from_sdf(_c_vertical_position, version) if _c_vertical_position is not None else None
        _c_vertical_velocity = el.find("vertical_velocity")
        _vertical_velocity = VerticalVelocity.from_sdf(_c_vertical_velocity, version) if _c_vertical_velocity is not None else None
        return cls(sdf_version=version, vertical_position=_vertical_position, vertical_velocity=_vertical_velocity)


class AspectRatio(Model):
    def __init__(self, sdf_version: str, aspect_ratio: float = 1):
        self.__version__ = sdf_version
        self.aspect_ratio = aspect_ratio

    def to_version(self, target_version: str) -> "AspectRatio":
        kwargs = {"sdf_version": target_version}
        kwargs["aspect_ratio"] = self.aspect_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("aspect_ratio")
        if self.aspect_ratio is not None:
            el.text = str(self.aspect_ratio)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AspectRatio":
        _text = el.text or 1
        _aspect_ratio = _parse_double(_text)
        return cls(sdf_version=version, aspect_ratio=_aspect_ratio)


class LogicalCamera(Model):
    def __init__(
        self,
        sdf_version: str,
        near: "Near" = None,
        far: "Far" = None,
        aspect_ratio: "AspectRatio" = None,
        horizontal_fov: "HorizontalFov" = None
    ):
        self.__version__ = sdf_version
        self.near = near
        self.far = far
        self.aspect_ratio = aspect_ratio
        self.horizontal_fov = horizontal_fov

    def to_version(self, target_version: str) -> "LogicalCamera":
        kwargs = {"sdf_version": target_version}
        kwargs["near"] = self.near.to_version(target_version) if self.near is not None else None
        kwargs["far"] = self.far.to_version(target_version) if self.far is not None else None
        kwargs["aspect_ratio"] = self.aspect_ratio.to_version(target_version) if self.aspect_ratio is not None else None
        kwargs["horizontal_fov"] = self.horizontal_fov.to_version(target_version) if self.horizontal_fov is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("logical_camera")
        if self.near is not None:
            el.append(self.near.to_sdf(version))
        if self.far is not None:
            el.append(self.far.to_sdf(version))
        if self.aspect_ratio is not None:
            el.append(self.aspect_ratio.to_sdf(version))
        if self.horizontal_fov is not None:
            el.append(self.horizontal_fov.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "LogicalCamera":
        _c_near = el.find("near")
        _near = Near.from_sdf(_c_near, version) if _c_near is not None else None
        _c_far = el.find("far")
        _far = Far.from_sdf(_c_far, version) if _c_far is not None else None
        _c_aspect_ratio = el.find("aspect_ratio")
        _aspect_ratio = AspectRatio.from_sdf(_c_aspect_ratio, version) if _c_aspect_ratio is not None else None
        _c_horizontal_fov = el.find("horizontal_fov")
        _horizontal_fov = HorizontalFov.from_sdf(_c_horizontal_fov, version) if _c_horizontal_fov is not None else None
        return cls(sdf_version=version, near=_near, far=_far, aspect_ratio=_aspect_ratio, horizontal_fov=_horizontal_fov)


class Magnetometer(Model):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Magnetometer":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("magnetometer")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x, version) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y, version) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z, version) if _c_z is not None else None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class ReferenceAltitude(Model):
    def __init__(self, sdf_version: str, reference_altitude: float = 0.0):
        self.__version__ = sdf_version
        self.reference_altitude = reference_altitude

    def to_version(self, target_version: str) -> "ReferenceAltitude":
        kwargs = {"sdf_version": target_version}
        kwargs["reference_altitude"] = self.reference_altitude
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("reference_altitude")
        if self.reference_altitude is not None:
            el.text = str(self.reference_altitude)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ReferenceAltitude":
        _text = el.text or 0.0
        _reference_altitude = _parse_double(_text)
        return cls(sdf_version=version, reference_altitude=_reference_altitude)


class Pressure(Model):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Pressure":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pressure")
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pressure":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        return cls(sdf_version=version, noise=_noise)


class AirPressure(Model):
    def __init__(
        self,
        sdf_version: str,
        reference_altitude: "ReferenceAltitude" = None,
        pressure: "Pressure" = None
    ):
        self.__version__ = sdf_version
        self.reference_altitude = reference_altitude
        self.pressure = pressure

    def to_version(self, target_version: str) -> "AirPressure":
        kwargs = {"sdf_version": target_version}
        kwargs["reference_altitude"] = self.reference_altitude.to_version(target_version) if self.reference_altitude is not None else None
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("air_pressure")
        if self.reference_altitude is not None:
            el.append(self.reference_altitude.to_sdf(version))
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AirPressure":
        _c_reference_altitude = el.find("reference_altitude")
        _reference_altitude = ReferenceAltitude.from_sdf(_c_reference_altitude, version) if _c_reference_altitude is not None else None
        _c_pressure = el.find("pressure")
        _pressure = Pressure.from_sdf(_c_pressure, version) if _c_pressure is not None else None
        return cls(sdf_version=version, reference_altitude=_reference_altitude, pressure=_pressure)


class Lidar(Model):
    def __init__(
        self,
        sdf_version: str,
        scan: "Scan" = None,
        range: "Range" = None,
        noise: "Noise" = None,
        visibility_mask: "VisibilityMask" = None
    ):
        self.__version__ = sdf_version
        self.scan = scan
        self.range = range
        self.noise = noise
        self.visibility_mask = visibility_mask

    def to_version(self, target_version: str) -> "Lidar":
        if self.visibility_mask is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["scan"] = self.scan.to_version(target_version) if self.scan is not None else None
        kwargs["range"] = self.range.to_version(target_version) if self.range is not None else None
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        kwargs["visibility_mask"] = self.visibility_mask.to_version(target_version) if self.visibility_mask is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lidar")
        if self.scan is not None:
            el.append(self.scan.to_sdf(version))
        if self.range is not None:
            el.append(self.range.to_sdf(version))
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        if self.visibility_mask is not None:
            el.append(self.visibility_mask.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Lidar":
        _c_scan = el.find("scan")
        _scan = Scan.from_sdf(_c_scan, version) if _c_scan is not None else None
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range, version) if _c_range is not None else None
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise, version) if _c_noise is not None else None
        _c_visibility_mask = el.find("visibility_mask")
        _visibility_mask = VisibilityMask.from_sdf(_c_visibility_mask, version) if _c_visibility_mask is not None else None
        if _visibility_mask is not None and cmp_version(version, "1.9") < 0:
            raise ValueError(f"'visibility_mask' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, scan=_scan, range=_range, noise=_noise, visibility_mask=_visibility_mask)


class Navsat(Model):
    def __init__(
        self,
        sdf_version: str,
        position_sensing: "PositionSensing" = None,
        velocity_sensing: "VelocitySensing" = None
    ):
        self.__version__ = sdf_version
        self.position_sensing = position_sensing
        self.velocity_sensing = velocity_sensing

    def to_version(self, target_version: str) -> "Navsat":
        kwargs = {"sdf_version": target_version}
        kwargs["position_sensing"] = self.position_sensing.to_version(target_version) if self.position_sensing is not None else None
        kwargs["velocity_sensing"] = self.velocity_sensing.to_version(target_version) if self.velocity_sensing is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("navsat")
        if self.position_sensing is not None:
            el.append(self.position_sensing.to_sdf(version))
        if self.velocity_sensing is not None:
            el.append(self.velocity_sensing.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Navsat":
        _c_position_sensing = el.find("position_sensing")
        _position_sensing = PositionSensing.from_sdf(_c_position_sensing, version) if _c_position_sensing is not None else None
        _c_velocity_sensing = el.find("velocity_sensing")
        _velocity_sensing = VelocitySensing.from_sdf(_c_velocity_sensing, version) if _c_velocity_sensing is not None else None
        return cls(sdf_version=version, position_sensing=_position_sensing, velocity_sensing=_velocity_sensing)


class EnableMetrics(Model):
    def __init__(self, sdf_version: str, enable_metrics: bool = False):
        self.__version__ = sdf_version
        self.enable_metrics = enable_metrics

    def to_version(self, target_version: str) -> "EnableMetrics":
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["enable_metrics"] = self.enable_metrics
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("enable_metrics")
        if self.enable_metrics is not None:
            el.text = str(self.enable_metrics).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "EnableMetrics":
        _text = el.text or False
        _enable_metrics = _text.strip().lower() == 'true'
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            if _enable_metrics != False:
                raise ValueError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, enable_metrics=_enable_metrics)


class AirSpeed(Model):
    def __init__(self, sdf_version: str, pressure: "Pressure" = None):
        self.__version__ = sdf_version
        self.pressure = pressure

    def to_version(self, target_version: str) -> "AirSpeed":
        kwargs = {"sdf_version": target_version}
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("air_speed")
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "AirSpeed":
        _c_pressure = el.find("pressure")
        _pressure = Pressure.from_sdf(_c_pressure, version) if _c_pressure is not None else None
        return cls(sdf_version=version, pressure=_pressure)


class FrameId(Model):
    def __init__(self, sdf_version: str, frame_id: str = ""):
        self.__version__ = sdf_version
        self.frame_id = frame_id

    def to_version(self, target_version: str) -> "FrameId":
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["frame_id"] = self.frame_id
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame_id")
        if self.frame_id is not None:
            el.text = self.frame_id
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "FrameId":
        _text = el.text or ""
        _frame_id = _text
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            if _frame_id != "":
                raise ValueError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, frame_id=_frame_id)


class Sensor(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "__default__",
        plugin: List["Plugin"] = None,
        camera: "Camera" = None,
        contact: "Contact" = None,
        force_torque: "ForceTorque" = None,
        gps: "Gps" = None,
        imu: "Imu" = None,
        ray: "Ray" = None,
        rfidtag: "Rfidtag" = None,
        rfid: "Rfid" = None,
        sonar: "Sonar" = None,
        transceiver: "Transceiver" = None,
        always_on: "AlwaysOn" = None,
        update_rate: "UpdateRate" = None,
        visualize: "Visualize" = None,
        pose: "Pose" = None,
        topic: "Topic" = None,
        frame: List["Frame"] = None,
        altimeter: "Altimeter" = None,
        logical_camera: "LogicalCamera" = None,
        magnetometer: "Magnetometer" = None,
        air_pressure: "AirPressure" = None,
        lidar: "Lidar" = None,
        navsat: "Navsat" = None,
        enable_metrics: "EnableMetrics" = None,
        air_speed: "AirSpeed" = None,
        frame_id: "FrameId" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.plugin = plugin or []
        self.camera = camera
        self.contact = contact
        self.force_torque = force_torque
        self.gps = gps
        self.imu = imu
        self.ray = ray
        self.rfidtag = rfidtag
        self.rfid = rfid
        self.sonar = sonar
        self.transceiver = transceiver
        self.always_on = always_on
        self.update_rate = update_rate
        self.visualize = visualize
        self.pose = pose
        self.topic = topic
        self.frame = frame or []
        self.altimeter = altimeter
        self.logical_camera = logical_camera
        self.magnetometer = magnetometer
        self.air_pressure = air_pressure
        self.lidar = lidar
        self.navsat = navsat
        self.enable_metrics = enable_metrics
        self.air_speed = air_speed
        self.frame_id = frame_id

    def to_version(self, target_version: str) -> "Sensor":
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.altimeter is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'altimeter' is not supported in SDF version {target_version} (added in 1.5)")
        if self.logical_camera is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'logical_camera' is not supported in SDF version {target_version} (added in 1.5)")
        if self.magnetometer is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'magnetometer' is not supported in SDF version {target_version} (added in 1.5)")
        if self.air_pressure is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'air_pressure' is not supported in SDF version {target_version} (added in 1.6)")
        if self.lidar is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'lidar' is not supported in SDF version {target_version} (added in 1.6)")
        if self.navsat is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'navsat' is not supported in SDF version {target_version} (added in 1.7)")
        if self.enable_metrics is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {target_version} (added in 1.7)")
        if self.air_speed is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'air_speed' is not supported in SDF version {target_version} (added in 1.10)")
        if self.frame_id is not None and cmp_version(target_version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {target_version} (added in 1.12)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["camera"] = self.camera.to_version(target_version) if self.camera is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["force_torque"] = self.force_torque.to_version(target_version) if self.force_torque is not None else None
        kwargs["gps"] = self.gps.to_version(target_version) if self.gps is not None else None
        kwargs["imu"] = self.imu.to_version(target_version) if self.imu is not None else None
        kwargs["ray"] = self.ray.to_version(target_version) if self.ray is not None else None
        kwargs["rfidtag"] = self.rfidtag.to_version(target_version) if self.rfidtag is not None else None
        kwargs["rfid"] = self.rfid.to_version(target_version) if self.rfid is not None else None
        kwargs["sonar"] = self.sonar.to_version(target_version) if self.sonar is not None else None
        kwargs["transceiver"] = self.transceiver.to_version(target_version) if self.transceiver is not None else None
        kwargs["always_on"] = self.always_on.to_version(target_version) if self.always_on is not None else None
        kwargs["update_rate"] = self.update_rate.to_version(target_version) if self.update_rate is not None else None
        kwargs["visualize"] = self.visualize.to_version(target_version) if self.visualize is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["altimeter"] = self.altimeter.to_version(target_version) if self.altimeter is not None else None
        kwargs["logical_camera"] = self.logical_camera.to_version(target_version) if self.logical_camera is not None else None
        kwargs["magnetometer"] = self.magnetometer.to_version(target_version) if self.magnetometer is not None else None
        kwargs["air_pressure"] = self.air_pressure.to_version(target_version) if self.air_pressure is not None else None
        kwargs["lidar"] = self.lidar.to_version(target_version) if self.lidar is not None else None
        kwargs["navsat"] = self.navsat.to_version(target_version) if self.navsat is not None else None
        kwargs["enable_metrics"] = self.enable_metrics.to_version(target_version) if self.enable_metrics is not None else None
        kwargs["air_speed"] = self.air_speed.to_version(target_version) if self.air_speed is not None else None
        kwargs["frame_id"] = self.frame_id.to_version(target_version) if self.frame_id is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sensor")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.camera is not None:
            el.append(self.camera.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        if self.force_torque is not None:
            el.append(self.force_torque.to_sdf(version))
        if self.gps is not None:
            el.append(self.gps.to_sdf(version))
        if self.imu is not None:
            el.append(self.imu.to_sdf(version))
        if self.ray is not None:
            el.append(self.ray.to_sdf(version))
        if self.rfidtag is not None:
            el.append(self.rfidtag.to_sdf(version))
        if self.rfid is not None:
            el.append(self.rfid.to_sdf(version))
        if self.sonar is not None:
            el.append(self.sonar.to_sdf(version))
        if self.transceiver is not None:
            el.append(self.transceiver.to_sdf(version))
        if self.always_on is not None:
            el.append(self.always_on.to_sdf(version))
        if self.update_rate is not None:
            el.append(self.update_rate.to_sdf(version))
        if self.visualize is not None:
            el.append(self.visualize.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.altimeter is not None:
            el.append(self.altimeter.to_sdf(version))
        if self.logical_camera is not None:
            el.append(self.logical_camera.to_sdf(version))
        if self.magnetometer is not None:
            el.append(self.magnetometer.to_sdf(version))
        if self.air_pressure is not None:
            el.append(self.air_pressure.to_sdf(version))
        if self.lidar is not None:
            el.append(self.lidar.to_sdf(version))
        if self.navsat is not None:
            el.append(self.navsat.to_sdf(version))
        if self.enable_metrics is not None:
            el.append(self.enable_metrics.to_sdf(version))
        if self.air_speed is not None:
            el.append(self.air_speed.to_sdf(version))
        if self.frame_id is not None:
            el.append(self.frame_id.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Sensor":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _plugin = [Plugin.from_sdf(c, version) for c in el.findall("plugin")]
        _c_camera = el.find("camera")
        _camera = Camera.from_sdf(_c_camera, version) if _c_camera is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact, version) if _c_contact is not None else None
        _c_force_torque = el.find("force_torque")
        _force_torque = ForceTorque.from_sdf(_c_force_torque, version) if _c_force_torque is not None else None
        _c_gps = el.find("gps")
        _gps = Gps.from_sdf(_c_gps, version) if _c_gps is not None else None
        _c_imu = el.find("imu")
        _imu = Imu.from_sdf(_c_imu, version) if _c_imu is not None else None
        _c_ray = el.find("ray")
        _ray = Ray.from_sdf(_c_ray, version) if _c_ray is not None else None
        _c_rfidtag = el.find("rfidtag")
        _rfidtag = Rfidtag.from_sdf(_c_rfidtag, version) if _c_rfidtag is not None else None
        _c_rfid = el.find("rfid")
        _rfid = Rfid.from_sdf(_c_rfid, version) if _c_rfid is not None else None
        _c_sonar = el.find("sonar")
        _sonar = Sonar.from_sdf(_c_sonar, version) if _c_sonar is not None else None
        _c_transceiver = el.find("transceiver")
        _transceiver = Transceiver.from_sdf(_c_transceiver, version) if _c_transceiver is not None else None
        _c_always_on = el.find("always_on")
        _always_on = AlwaysOn.from_sdf(_c_always_on, version) if _c_always_on is not None else None
        _c_update_rate = el.find("update_rate")
        _update_rate = UpdateRate.from_sdf(_c_update_rate, version) if _c_update_rate is not None else None
        _c_visualize = el.find("visualize")
        _visualize = Visualize.from_sdf(_c_visualize, version) if _c_visualize is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic, version) if _c_topic is not None else None
        _frame = [Frame.from_sdf(c, version) for c in el.findall("frame")]
        if _frame and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_altimeter = el.find("altimeter")
        _altimeter = Altimeter.from_sdf(_c_altimeter, version) if _c_altimeter is not None else None
        if _altimeter is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'altimeter' is not supported in SDF version {version} (added in 1.5)")
        _c_logical_camera = el.find("logical_camera")
        _logical_camera = LogicalCamera.from_sdf(_c_logical_camera, version) if _c_logical_camera is not None else None
        if _logical_camera is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'logical_camera' is not supported in SDF version {version} (added in 1.5)")
        _c_magnetometer = el.find("magnetometer")
        _magnetometer = Magnetometer.from_sdf(_c_magnetometer, version) if _c_magnetometer is not None else None
        if _magnetometer is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'magnetometer' is not supported in SDF version {version} (added in 1.5)")
        _c_air_pressure = el.find("air_pressure")
        _air_pressure = AirPressure.from_sdf(_c_air_pressure, version) if _c_air_pressure is not None else None
        if _air_pressure is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'air_pressure' is not supported in SDF version {version} (added in 1.6)")
        _c_lidar = el.find("lidar")
        _lidar = Lidar.from_sdf(_c_lidar, version) if _c_lidar is not None else None
        if _lidar is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'lidar' is not supported in SDF version {version} (added in 1.6)")
        _c_navsat = el.find("navsat")
        _navsat = Navsat.from_sdf(_c_navsat, version) if _c_navsat is not None else None
        if _navsat is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'navsat' is not supported in SDF version {version} (added in 1.7)")
        _c_enable_metrics = el.find("enable_metrics")
        _enable_metrics = EnableMetrics.from_sdf(_c_enable_metrics, version) if _c_enable_metrics is not None else None
        if _enable_metrics is not None and cmp_version(version, "1.7") < 0:
            raise ValueError(f"'enable_metrics' is not supported in SDF version {version} (added in 1.7)")
        _c_air_speed = el.find("air_speed")
        _air_speed = AirSpeed.from_sdf(_c_air_speed, version) if _c_air_speed is not None else None
        if _air_speed is not None and cmp_version(version, "1.10") < 0:
            raise ValueError(f"'air_speed' is not supported in SDF version {version} (added in 1.10)")
        _c_frame_id = el.find("frame_id")
        _frame_id = FrameId.from_sdf(_c_frame_id, version) if _c_frame_id is not None else None
        if _frame_id is not None and cmp_version(version, "1.12") < 0:
            raise ValueError(f"'frame_id' is not supported in SDF version {version} (added in 1.12)")
        return cls(sdf_version=version, name=_name, type=_type, plugin=_plugin, camera=_camera, contact=_contact, force_torque=_force_torque, gps=_gps, imu=_imu, ray=_ray, rfidtag=_rfidtag, rfid=_rfid, sonar=_sonar, transceiver=_transceiver, always_on=_always_on, update_rate=_update_rate, visualize=_visualize, pose=_pose, topic=_topic, frame=_frame, altimeter=_altimeter, logical_camera=_logical_camera, magnetometer=_magnetometer, air_pressure=_air_pressure, lidar=_lidar, navsat=_navsat, enable_metrics=_enable_metrics, air_speed=_air_speed, frame_id=_frame_id)


class GearboxRatio(Model):
    def __init__(self, sdf_version: str, gearbox_ratio: float = 1.0):
        self.__version__ = sdf_version
        self.gearbox_ratio = gearbox_ratio

    def to_version(self, target_version: str) -> "GearboxRatio":
        if self.gearbox_ratio is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_ratio' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["gearbox_ratio"] = self.gearbox_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gearbox_ratio")
        if self.gearbox_ratio is not None:
            el.text = str(self.gearbox_ratio)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "GearboxRatio":
        _text = el.text or 1.0
        _gearbox_ratio = _parse_double(_text)
        if _gearbox_ratio is not None and cmp_version(version, "1.4") < 0:
            if _gearbox_ratio != 1.0:
                raise ValueError(f"'gearbox_ratio' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, gearbox_ratio=_gearbox_ratio)


class GearboxReferenceBody(Model):
    def __init__(self, sdf_version: str, gearbox_reference_body: str = "__default__"):
        self.__version__ = sdf_version
        self.gearbox_reference_body = gearbox_reference_body

    def to_version(self, target_version: str) -> "GearboxReferenceBody":
        if self.gearbox_reference_body is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["gearbox_reference_body"] = self.gearbox_reference_body
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("gearbox_reference_body")
        if self.gearbox_reference_body is not None:
            el.text = self.gearbox_reference_body
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "GearboxReferenceBody":
        _text = el.text or "__default__"
        _gearbox_reference_body = _text
        if _gearbox_reference_body is not None and cmp_version(version, "1.4") < 0:
            if _gearbox_reference_body != "__default__":
                raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, gearbox_reference_body=_gearbox_reference_body)


class ScrewThreadPitch(Model):
    def __init__(self, sdf_version: str, screw_thread_pitch: float = 1.0):
        self.__version__ = sdf_version
        self.screw_thread_pitch = screw_thread_pitch

    def to_version(self, target_version: str) -> "ScrewThreadPitch":
        if self.screw_thread_pitch is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {target_version} (added in 1.10)")
        kwargs = {"sdf_version": target_version}
        kwargs["screw_thread_pitch"] = self.screw_thread_pitch
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("screw_thread_pitch")
        if self.screw_thread_pitch is not None:
            el.text = str(self.screw_thread_pitch)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "ScrewThreadPitch":
        _text = el.text or 1.0
        _screw_thread_pitch = _parse_double(_text)
        if _screw_thread_pitch is not None and cmp_version(version, "1.10") < 0:
            if _screw_thread_pitch != 1.0:
                raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, screw_thread_pitch=_screw_thread_pitch)


class Joint(Model):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        type: str = "__default__",
        parent: "Parent" = None,
        child: "Child" = None,
        origin: "Origin" = None,
        thread_pitch: "ThreadPitch" = None,
        axis: "Axis" = None,
        axis2: "Axis2" = None,
        physics: "Physics" = None,
        pose: "Pose" = None,
        sensor: List["Sensor"] = None,
        gearbox_ratio: "GearboxRatio" = None,
        gearbox_reference_body: "GearboxReferenceBody" = None,
        frame: List["Frame"] = None,
        screw_thread_pitch: "ScrewThreadPitch" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.type = type
        self.parent = parent
        self.child = child
        self.origin = origin
        self.thread_pitch = thread_pitch
        self.axis = axis
        self.axis2 = axis2
        self.physics = physics
        self.pose = pose
        self.sensor = sensor or []
        self.gearbox_ratio = gearbox_ratio
        self.gearbox_reference_body = gearbox_reference_body
        self.frame = frame or []
        self.screw_thread_pitch = screw_thread_pitch

    def to_version(self, target_version: str) -> "Joint":
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.sensor is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'sensor' is not supported in SDF version {target_version} (added in 1.4)")
        if self.gearbox_ratio is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_ratio' is not supported in SDF version {target_version} (added in 1.4)")
        if self.gearbox_reference_body is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {target_version} (added in 1.4)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.screw_thread_pitch is not None and cmp_version(target_version, "1.10") < 0:
            raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {target_version} (added in 1.10)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["type"] = self.type
        kwargs["parent"] = self.parent.to_version(target_version) if self.parent is not None else None
        kwargs["child"] = self.child.to_version(target_version) if self.child is not None else None
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["thread_pitch"] = self.thread_pitch.to_version(target_version) if self.thread_pitch is not None else None
        kwargs["axis"] = self.axis.to_version(target_version) if self.axis is not None else None
        kwargs["axis2"] = self.axis2.to_version(target_version) if self.axis2 is not None else None
        kwargs["physics"] = self.physics.to_version(target_version) if self.physics is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["sensor"] = [c.to_version(target_version) for c in (self.sensor or [])]
        kwargs["gearbox_ratio"] = self.gearbox_ratio.to_version(target_version) if self.gearbox_ratio is not None else None
        kwargs["gearbox_reference_body"] = self.gearbox_reference_body.to_version(target_version) if self.gearbox_reference_body is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["screw_thread_pitch"] = self.screw_thread_pitch.to_version(target_version) if self.screw_thread_pitch is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("joint")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.parent is not None:
            el.append(self.parent.to_sdf(version))
        if self.child is not None:
            el.append(self.child.to_sdf(version))
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.thread_pitch is not None:
            el.append(self.thread_pitch.to_sdf(version))
        if self.axis is not None:
            el.append(self.axis.to_sdf(version))
        if self.axis2 is not None:
            el.append(self.axis2.to_sdf(version))
        if self.physics is not None:
            el.append(self.physics.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        for item in (self.sensor or []):
            el.append(item.to_sdf(version))
        if self.gearbox_ratio is not None:
            el.append(self.gearbox_ratio.to_sdf(version))
        if self.gearbox_reference_body is not None:
            el.append(self.gearbox_reference_body.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.screw_thread_pitch is not None:
            el.append(self.screw_thread_pitch.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Joint":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _c_parent = el.find("parent")
        _parent = Parent.from_sdf(_c_parent, version) if _c_parent is not None else None
        _c_child = el.find("child")
        _child = Child.from_sdf(_c_child, version) if _c_child is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin, version) if _c_origin is not None else None
        _c_thread_pitch = el.find("thread_pitch")
        _thread_pitch = ThreadPitch.from_sdf(_c_thread_pitch, version) if _c_thread_pitch is not None else None
        _c_axis = el.find("axis")
        _axis = Axis.from_sdf(_c_axis, version) if _c_axis is not None else None
        _c_axis2 = el.find("axis2")
        _axis2 = Axis2.from_sdf(_c_axis2, version) if _c_axis2 is not None else None
        _c_physics = el.find("physics")
        _physics = Physics.from_sdf(_c_physics, version) if _c_physics is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose, version) if _c_pose is not None else None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _sensor = [Sensor.from_sdf(c, version) for c in el.findall("sensor")]
        if _sensor and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'sensor' is not supported in SDF version {version} (added in 1.4)")
        _c_gearbox_ratio = el.find("gearbox_ratio")
        _gearbox_ratio = GearboxRatio.from_sdf(_c_gearbox_ratio, version) if _c_gearbox_ratio is not None else None
        if _gearbox_ratio is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'gearbox_ratio' is not supported in SDF version {version} (added in 1.4)")
        _c_gearbox_reference_body = el.find("gearbox_reference_body")
        _gearbox_reference_body = GearboxReferenceBody.from_sdf(_c_gearbox_reference_body, version) if _c_gearbox_reference_body is not None else None
        if _gearbox_reference_body is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'gearbox_reference_body' is not supported in SDF version {version} (added in 1.4)")
        _frame = [Frame.from_sdf(c, version) for c in el.findall("frame")]
        if _frame and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_screw_thread_pitch = el.find("screw_thread_pitch")
        _screw_thread_pitch = ScrewThreadPitch.from_sdf(_c_screw_thread_pitch, version) if _c_screw_thread_pitch is not None else None
        if _screw_thread_pitch is not None and cmp_version(version, "1.10") < 0:
            raise ValueError(f"'screw_thread_pitch' is not supported in SDF version {version} (added in 1.10)")
        return cls(sdf_version=version, name=_name, type=_type, parent=_parent, child=_child, origin=_origin, thread_pitch=_thread_pitch, axis=_axis, axis2=_axis2, physics=_physics, pose=_pose, sensor=_sensor, gearbox_ratio=_gearbox_ratio, gearbox_reference_body=_gearbox_reference_body, frame=_frame, screw_thread_pitch=_screw_thread_pitch)
