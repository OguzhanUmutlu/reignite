from .GzGui import GzGui
from ...plugin import Plugin, TextElement, ParentElement
from ....utils.color import Color, _ColorT, _color
from ....utils.pose import Pose, _PoseT, _pose


class MinimalScenePlugin(Plugin):
    def __init__(self,
                 camera_pose: _PoseT = _pose("0 -10 3 0 0.2 1.5708"),
                 ambient_light: _ColorT = _color("0.4 0.4 0.4"),
                 background_color: _ColorT = _color("0.4 0.4 0.4"),
                 near=0.1,
                 far=2000,
                 engine="ogre2",
                 scene="scene",

                 name="3D View", **gui_kwargs):
        super().__init__(name=name, filename="MinimalScene", elements=[
            GzGui(**{"title": "3D View", "show_title_bar": False, "state": "docked", **gui_kwargs}),
            ParentElement("camera_clip", [
                TextElement("near", near),
                TextElement("far", far)
            ])
        ], engine=engine, scene=scene, ambient_light=_color(ambient_light).to_sdf(),
                         background_color=_color(background_color).to_sdf(),
                         camera_pose=_pose(camera_pose).to_sdf())
