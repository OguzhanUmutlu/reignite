from .GzGui import GzGui
from ...plugin import Plugin


class PointCloudPlugin(Plugin):
    def __init__(
            self,
            float_v_topic: str | None = None,
            point_cloud_topic: str | None = None,
            name: str = "PointCloud",
            **gui_kwargs
    ):
        super().__init__(
            filename="PointCloud",
            name=name,
            elements=[
                GzGui(**gui_kwargs)
            ],
            float_v_topic=float_v_topic,
            point_cloud_topic=point_cloud_topic,
        )
