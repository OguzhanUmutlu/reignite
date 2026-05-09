from __future__ import annotations

from xml.etree import ElementTree as ET

from .cols import Cols
from .rows import Rows
from .step import Step
from ..model import Model


class Type(Model):
    def __init__(self, type: str = "stereographic"):
        self.type = type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _text = el.text or "stereographic"
        _type = _text
        return cls(type=_type)


class Distribution(Model):
    def __init__(
            self,
            type: "Type" = None,
            rows: "Rows" = None,
            cols: "Cols" = None,
            step: "Step" = None
    ):
        self.type = type
        self.rows = rows
        self.cols = cols
        self.step = step

    def to_sdf(self) -> ET.Element:
        el = ET.Element("distribution")
        if self.type is not None:
            el.append(self.type.to_sdf())
        if self.rows is not None:
            el.append(self.rows.to_sdf())
        if self.cols is not None:
            el.append(self.cols.to_sdf())
        if self.step is not None:
            el.append(self.step.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Distribution":
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type) if _c_type is not None else None
        _c_rows = el.find("rows")
        _rows = Rows.from_sdf(_c_rows) if _c_rows is not None else None
        _c_cols = el.find("cols")
        _cols = Cols.from_sdf(_c_cols) if _c_cols is not None else None
        _c_step = el.find("step")
        _step = Step.from_sdf(_c_step) if _c_step is not None else None
        return cls(type=_type, rows=_rows, cols=_cols, step=_step)
