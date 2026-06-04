from xml.etree import ElementTree as ET
from .GzGui import GzGui
from ...plugin import Plugin
from ....utils.color import _ColorT, _color
from ....utils.pose import _PoseT, _pose


@Plugin.register("MinimalScene", "3D View")
class MinimalScenePlugin(Plugin):
    def __init__(self,
                 camera_pose: _PoseT | None = "0 -10 3 0 0.2 1.5708",
                 ambient_light: _ColorT | None = "0.4 0.4 0.4",
                 background_color: _ColorT | None = "0.4 0.4 0.4",
                 near: float | None = 0.1,
                 far: float | None = 2000.0,
                 engine: str | None = "ogre2",
                 scene: str | None = "scene",
                 name: str = "3D View", 
                 **gui_kwargs):
        self.camera_pose = camera_pose
        self.ambient_light = ambient_light
        self.background_color = background_color
        self.near = near
        self.far = far
        self.engine = engine
        self.scene = scene
        self.name = name
        
        gui_params = {"title": "3D View", "show_title_bar": False, "state": "docked"}
        gui_params.update(gui_kwargs)
        self.gz_gui = GzGui(**gui_params)
        
        super().__init__(name=name, filename="MinimalScene")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        gui_el = el.find("gz-gui")
        gui_kwargs = {}
        if gui_el is not None:
            gui = GzGui._from_sdf(gui_el, version)
            for k in ["anchors", "anchor", "state", "z", "height", "width", "resizable", "show_title_bar", "delete_later", "title"]:
                if hasattr(gui, k) and getattr(gui, k) is not None:
                    gui_kwargs[k] = getattr(gui, k)
                    
        name = el.get("name", "3D View")
        
        camera_pose_el = el.find("camera_pose")
        ambient_light_el = el.find("ambient_light")
        background_color_el = el.find("background_color")
        engine_el = el.find("engine")
        scene_el = el.find("scene")
        
        near = None
        far = None
        camera_clip_el = el.find("camera_clip")
        if camera_clip_el is not None:
            near_el = camera_clip_el.find("near")
            far_el = camera_clip_el.find("far")
            if near_el is not None and near_el.text is not None:
                near = float(near_el.text)
            if far_el is not None and far_el.text is not None:
                far = float(far_el.text)

        return cls(
            name=name,
            camera_pose=camera_pose_el.text if camera_pose_el is not None and camera_pose_el.text is not None else None,
            ambient_light=ambient_light_el.text if ambient_light_el is not None and ambient_light_el.text is not None else None,
            background_color=background_color_el.text if background_color_el is not None and background_color_el.text is not None else None,
            engine=engine_el.text if engine_el is not None and engine_el.text is not None else None,
            scene=scene_el.text if scene_el is not None and scene_el.text is not None else None,
            near=near,
            far=far,
            **gui_kwargs
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name, filename="MinimalScene")
        
        if self.gz_gui is not None:
            el.append(self.gz_gui.to_sdf(version))
            
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add("engine", self.engine)
        _add("scene", self.scene)
        if self.ambient_light is not None:
            _add("ambient_light", _color(self.ambient_light).to_sdf())
        if self.background_color is not None:
            _add("background_color", _color(self.background_color).to_sdf())
        if self.camera_pose is not None:
            _add("camera_pose", _pose(self.camera_pose).to_sdf())
            
        if self.near is not None or self.far is not None:
            clip_el = ET.Element("camera_clip")
            if self.near is not None:
                near_el = ET.Element("near")
                near_el.text = str(self.near)
                clip_el.append(near_el)
            if self.far is not None:
                far_el = ET.Element("far")
                far_el.text = str(self.far)
                clip_el.append(far_el)
            el.append(clip_el)

        return el

    def to_version(self, target_version: str):
        return self
