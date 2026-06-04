from .GzGui import GzGui
from ...plugin import Plugin


@Plugin.register("TransportPlotting", "TransportPlotting")
class TransportPlottingPlugin(Plugin):
    def __init__(
            self,
            name: str = "TransportPlotting",
            **gui_kwargs
    ):
        super().__init__(
            filename="TransportPlotting",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
        )
