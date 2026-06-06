from xml.etree import ElementTree as ET

from reignite import BaseModel
from reignite.elements.plugin import Plugin
from .GzGui import GzGui
from ....utils.color import _ColorT, _color
from ....utils.pose import _PoseT, _pose


@Plugin.register("GridConfig", "GridConfig")
class GridConfigPlugin(Plugin):
    class Insert(BaseModel):
        def __init__(
                self,
                cell_count: int | None = None,
                cell_length: float | None = None,
                color: _ColorT | None = None,
                horizontal_cell_count: int | None = None,
                pose: _PoseT | None = None,
                vertical_cell_count: int | None = None,
        ):
            self.cell_count = cell_count
            self.cell_length = cell_length
            self.color = color
            self.horizontal_cell_count = horizontal_cell_count
            self.pose = pose
            self.vertical_cell_count = vertical_cell_count
            super().__init__(sdf_version=None)

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            cell_count_el = el.find("cell_count")
            cell_length_el = el.find("cell_length")
            color_el = el.find("color")
            horizontal_cell_count_el = el.find("horizontal_cell_count")
            pose_el = el.find("pose")
            vertical_cell_count_el = el.find("vertical_cell_count")

            return cls(
                cell_count=int(
                    cell_count_el.text) if cell_count_el is not None and cell_count_el.text is not None else None,
                cell_length=float(
                    cell_length_el.text) if cell_length_el is not None and cell_length_el.text is not None else None,
                color=color_el.text if color_el is not None and color_el.text is not None else None,
                horizontal_cell_count=int(
                    horizontal_cell_count_el.text) if horizontal_cell_count_el is not None and horizontal_cell_count_el.text is not None else None,
                pose=pose_el.text if pose_el is not None and pose_el.text is not None else None,
                vertical_cell_count=int(
                    vertical_cell_count_el.text) if vertical_cell_count_el is not None and vertical_cell_count_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            el = ET.Element("insert")

            def _add(k, v):
                if v is not None:
                    child = ET.Element(k)
                    child.text = str(v)
                    el.append(child)

            _add("cell_count", self.cell_count)
            _add("cell_length", self.cell_length)
            if self.color is not None:
                _add("color", _color(self.color).to_sdf())
            _add("horizontal_cell_count", self.horizontal_cell_count)
            if self.pose is not None:
                _add("pose", _pose(self.pose).to_sdf())
            _add("vertical_cell_count", self.vertical_cell_count)

            return el

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            cell_count: int | None = None,
            cell_length: float | None = None,
            color: _ColorT | None = None,
            horizontal_cell_count: int | None = None,
            insert: Insert | list[Insert] | None = None,
            pose: _PoseT | None = None,
            vertical_cell_count: int | None = None,
            name: str = "GridConfig",
            **gui_kwargs
    ):
        self.cell_count = cell_count
        self.cell_length = cell_length
        self.color = color
        self.horizontal_cell_count = horizontal_cell_count
        if insert is not None:
            self.insert = [insert] if isinstance(insert, GridConfigPlugin.Insert) else insert
        else:
            self.insert = []
        self.pose = pose
        self.vertical_cell_count = vertical_cell_count
        self.name = name
        self.gz_gui = GzGui(**gui_kwargs)

        super().__init__(
            sdf_version=None,
            filename="GridConfig",
            name=name
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        gui_el = el.find("gz-gui")
        gui_kwargs = {}
        if gui_el is not None:
            gui = GzGui._from_sdf(gui_el, version)
            for k in ["anchors", "anchor", "state", "z", "height", "width", "resizable", "show_title_bar",
                      "delete_later", "title"]:
                if hasattr(gui, k) and getattr(gui, k) is not None:
                    gui_kwargs[k] = getattr(gui, k)

        name = el.get("name")
        cell_count_el = el.find("cell_count")
        cell_length_el = el.find("cell_length")
        color_el = el.find("color")
        horizontal_cell_count_el = el.find("horizontal_cell_count")
        pose_el = el.find("pose")
        vertical_cell_count_el = el.find("vertical_cell_count")

        inserts = []
        for insert_el in el.findall("insert"):
            inserts.append(cls.Insert._from_sdf(insert_el, version))

        return cls(
            name=name if name is not None else "GridConfig",
            cell_count=int(
                cell_count_el.text) if cell_count_el is not None and cell_count_el.text is not None else None,
            cell_length=float(
                cell_length_el.text) if cell_length_el is not None and cell_length_el.text is not None else None,
            color=color_el.text if color_el is not None and color_el.text is not None else None,
            horizontal_cell_count=int(
                horizontal_cell_count_el.text) if horizontal_cell_count_el is not None and horizontal_cell_count_el.text is not None else None,
            pose=pose_el.text if pose_el is not None and pose_el.text is not None else None,
            vertical_cell_count=int(
                vertical_cell_count_el.text) if vertical_cell_count_el is not None and vertical_cell_count_el.text is not None else None,
            insert=inserts,
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="GridConfig")

        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                child.text = str(v)
                el.append(child)

        _add("cell_count", self.cell_count)
        _add("cell_length", self.cell_length)
        if self.color is not None:
            _add("color", _color(self.color).to_sdf())
        _add("horizontal_cell_count", self.horizontal_cell_count)
        if self.pose is not None:
            _add("pose", _pose(self.pose).to_sdf())
        _add("vertical_cell_count", self.vertical_cell_count)

        for ins in self.insert:
            el.append(ins.to_sdf(version))

        return el

    def to_version(self, target_version: str):
        return self
