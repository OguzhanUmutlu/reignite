from typing import List

from reignite.utils import Pose
from .frame import Frame
from .sensor import Sensor
from .._sdf.joint import Joint as _Joint


class Joint(_Joint):
    def __init__(
            self,
            sdf_version: str | None = None,
            axis: "Joint.Axis | None" = None,
            axis2: "Joint.Axis2 | None" = None,
            child: "Joint.Child | None" = None,
            frames: List["Frame"] | None = None,
            gearbox_ratio: float | None = None,
            gearbox_reference_body: str | None = None,
            name: str | None = None,
            origin: "Joint.Origin | None" = None,
            parent: "Joint.Parent | None" = None,
            physics: "Joint.Physics | None" = None,
            pose: "Pose | None" = None,
            screw_thread_pitch: float | None = None,
            sensor: "Sensor | None" = None,
            thread_pitch: float | None = None,
            type: str | None = None
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
