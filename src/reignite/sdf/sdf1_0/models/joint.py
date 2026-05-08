from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .parent import Parent
from .child import Child
from .origin import Origin
from .thread_pitch import ThreadPitch
from .axis import Axis
from .axis2 import Axis2
from .physics import Physics


class Joint(Model):
    def __init__(
        self,
        name: str = "__default__",
        type: str = "__default__",
        parent: "Parent" = None,
        child: "Child" = None,
        origin: "Origin" = None,
        thread_pitch: "ThreadPitch" = None,
        axis: "Axis" = None,
        axis2: "Axis2" = None,
        physics: "Physics" = None
    ):
        self.name = name
        self.type = type
        self.parent = parent
        self.child = child
        self.origin = origin
        self.thread_pitch = thread_pitch
        self.axis = axis
        self.axis2 = axis2
        self.physics = physics

    def to_sdf(self) -> ET.Element:
        el = ET.Element("joint")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.parent is not None:
            el.append(self.parent.to_sdf())
        if self.child is not None:
            el.append(self.child.to_sdf())
        if self.origin is not None:
            el.append(self.origin.to_sdf())
        if self.thread_pitch is not None:
            el.append(self.thread_pitch.to_sdf())
        if self.axis is not None:
            el.append(self.axis.to_sdf())
        if self.axis2 is not None:
            el.append(self.axis2.to_sdf())
        if self.physics is not None:
            el.append(self.physics.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Joint":
        _name = el.get("name", "__default__")
        _type = el.get("type", "__default__")
        _c_parent = el.find("parent")
        _parent = Parent.from_sdf(_c_parent) if _c_parent is not None else None
        _c_child = el.find("child")
        _child = Child.from_sdf(_c_child) if _c_child is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin) if _c_origin is not None else None
        _c_thread_pitch = el.find("thread_pitch")
        _thread_pitch = ThreadPitch.from_sdf(_c_thread_pitch) if _c_thread_pitch is not None else None
        _c_axis = el.find("axis")
        _axis = Axis.from_sdf(_c_axis) if _c_axis is not None else None
        _c_axis2 = el.find("axis2")
        _axis2 = Axis2.from_sdf(_c_axis2) if _c_axis2 is not None else None
        _c_physics = el.find("physics")
        _physics = Physics.from_sdf(_c_physics) if _c_physics is not None else None
        return cls(name=_name, type=_type, parent=_parent, child=_child, origin=_origin, thread_pitch=_thread_pitch, axis=_axis, axis2=_axis2, physics=_physics)
