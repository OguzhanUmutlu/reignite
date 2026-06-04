from reignite import BaseModel
from reignite.elements.plugin import Plugin, ParentElement, TextElement
from .GzGui import GzGui


@Plugin.register("GridConfig", "GridConfig")
class GridConfigPlugin(Plugin):
    class Insert(ParentElement):
        def __init__(
                self,
                cell_count: int | None = None,
                cell_length: float | None = None,
                color: str | list[float] | None = None,
                horizontal_cell_count: int | None = None,
                pose: str | list[float] | None = None,
                vertical_cell_count: int | None = None,
        ):
            if isinstance(color, list):
                color = " ".join(map(str, color))
            if isinstance(pose, list):
                pose = " ".join(map(str, pose))

            super().__init__(
                "insert",
                [
                    TextElement("cell_count", str(cell_count)) if cell_count is not None else None,
                    TextElement("cell_length", str(cell_length)) if cell_length is not None else None,
                    TextElement("color", color) if color is not None else None,
                    TextElement("horizontal_cell_count",
                                str(horizontal_cell_count)) if horizontal_cell_count is not None else None,
                    TextElement("pose", pose) if pose is not None else None,
                    TextElement("vertical_cell_count",
                                str(vertical_cell_count)) if vertical_cell_count is not None else None
                ]
            )

    def __init__(
            self,
            cell_count: int | None = None,
            cell_length: float | None = None,
            color: str | list[float] | None = None,
            horizontal_cell_count: int | None = None,
            insert: Insert | list[Insert] | None = None,
            pose: str | list[float] | None = None,
            vertical_cell_count: int | None = None,
            name: str = "GridConfig",
            **gui_kwargs
    ):
        elements: list[BaseModel] = [GzGui(**gui_kwargs)]
        if insert is not None:
            if isinstance(insert, GridConfigPlugin.Insert):
                insert = [insert]
            elements.extend(insert)

        if isinstance(color, list):
            color = " ".join(map(str, color))
        if isinstance(pose, list):
            pose = " ".join(map(str, pose))

        super().__init__(
            filename="GridConfig",
            name=name,
            elements=elements,
            cell_count=cell_count,
            cell_length=cell_length,
            color=color,
            horizontal_cell_count=horizontal_cell_count,
            pose=pose,
            vertical_cell_count=vertical_cell_count,
        )
