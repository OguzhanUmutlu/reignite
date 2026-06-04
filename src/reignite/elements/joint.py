from typing import List

import reignite
from reignite.utils import Pose

from .._sdf.joint import Joint as _Joint


class Joint(_Joint):
    def __init__(
            self,
            sdf_version: str | None = None,
            axis: "Joint.Axis | None" = None,
            axis2: "Joint.Axis2 | None" = None,
            child: "Joint.Child | str | None" = None,
            frames: List["reignite.elements.Frame"] | None = None,
            gearbox_ratio: float | None = 1.0,
            gearbox_reference_body: str | None = "__default__",
            name: str | None = "__default__",
            origin: "Joint.Origin | None" = None,
            parent: "Joint.Parent | str | None" = None,
            physics: "Joint.Physics | None" = None,
            pose: "Pose | None" = None,
            screw_thread_pitch: float | None = 1.0,
            sensor: "reignite.elements.Sensor | None" = None,
            thread_pitch: float | None = 1.0,
            type: str | None = "__default__"
    ):
        if isinstance(parent, str):
            parent = Joint.Parent(parent=parent)
        if isinstance(child, str):
            child = Joint.Child(child=child)

        super().__init__(
            sdf_version=sdf_version,
            axis=axis,
            axis2=axis2,
            child=child,
            frames=frames,
            gearbox_ratio=gearbox_ratio,
            gearbox_reference_body=gearbox_reference_body,
            name=name,
            origin=origin,
            parent=parent,
            physics=physics,
            pose=pose,
            screw_thread_pitch=screw_thread_pitch,
            sensor=sensor,
            thread_pitch=thread_pitch,
            type=type
        )

    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Joint._search(search)
        if self.sensor is not None and self.sensor.name == search:
            return self.sensor.find_element(rest)
        return Joint._find_help(self.frames, search, rest)
