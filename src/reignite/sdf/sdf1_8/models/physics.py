from __future__ import annotations

from xml.etree import ElementTree as ET

from .provide_feedback import ProvideFeedback
from ...sdf1_7.models.ode import Ode as _PrevOde
from ...sdf1_7.models.physics import Physics as _PrevPhysics
from ...sdf1_7.models.simbody import Simbody as _PrevSimbody


class Simbody(_PrevSimbody):
    def __init__(self, must_be_loop_joint: "MustBeLoopJoint" = None):
        super().__init__(must_be_loop_joint=must_be_loop_joint)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Simbody":
        _base = _PrevSimbody.from_sdf(el)
        return cls(must_be_loop_joint=_base.must_be_loop_joint)


class Ode(_PrevOde):
    def __init__(self, slip: "Slip" = None):
        super().__init__()
        self.slip = slip

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.slip is not None:
            el.append(self.slip.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_slip = el.find("slip")
        _slip = Slip.from_sdf(_c_slip) if _c_slip is not None else None
        return cls(slip=_slip)


class Physics(_PrevPhysics):
    def __init__(
            self,
            simbody: "Simbody" = None,
            ode: "Ode" = None,
            provide_feedback: "ProvideFeedback" = None
    ):
        super().__init__(simbody=simbody, ode=ode, provide_feedback=provide_feedback)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Physics":
        _base = _PrevPhysics.from_sdf(el)
        return cls(simbody=_base.simbody, ode=_base.ode, provide_feedback=_base.provide_feedback)
