from reignite.elements import Plugin
from reignite.elements.plugin import TextElement, ParentElement
from reignite.elements.plugins.gui.GzGui import GzGui
from reignite.utils.color import Color
from reignite.utils.pose import Pose


class MinimalScenePlugin(Plugin):
    def __init__(self,
                 camera_pose=Pose.from_sdf("0 -10 3 0 0.2 1.5708"),
                 ambient_light=Color.from_sdf("0.4 0.4 0.4"),
                 background_color=Color.from_sdf("0.4 0.4 0.4"),
                 near=0.1,
                 far=2000,
                 engine="ogre2",
                 scene="scene",

                 name="3D View", **gui_kwargs):
        super().__init__(name=name, filename="MinimalScene", elements=[
            GzGui(**{"title": "3D View", "showTitleBar": False, "state": "docked", **gui_kwargs}),
            TextElement("engine", engine),
            TextElement("scene", scene),
            TextElement("ambient_light", ambient_light.to_sdf()),
            TextElement("background_color", background_color.to_sdf()),
            TextElement("camera_pose", camera_pose.to_sdf()),
            ParentElement("camera_clip", [
                TextElement("near", near),
                TextElement("far", far)
            ])
        ])
