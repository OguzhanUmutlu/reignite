from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("TapeMeasure", "TapeMeasure")
class TapeMeasurePlugin(Plugin):
    def __init__(
            self,
            name: str = "TapeMeasure",
            **gui_kwargs
    ):
        super().__init__(
            filename="TapeMeasure",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
