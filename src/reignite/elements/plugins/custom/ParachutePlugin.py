from xml.etree import ElementTree as ET
from ...plugin import Plugin
from ....utils.pose import _PoseT, _pose


@Plugin.register("ParachutePlugin", "ParachutePlugin")
class ParachutePlugin(Plugin):
    def __init__(
            self,
            parent_link: str | None = None,
            child_model: str | None = None,
            child_link: str | None = None,
            child_pose: _PoseT | None = None,
            cmd_topic: str | list[str] | None = None,
            **kwargs
    ):
        self.parent_link = parent_link
        self.child_model = child_model
        self.child_link = child_link
        self.child_pose = child_pose
        self.cmd_topic = cmd_topic
        super().__init__(
            sdf_version=None,
            filename="ParachutePlugin",
            name="ParachutePlugin",
            **kwargs
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        parent_link_el = el.find("parent_link")
        child_model_el = el.find("child_model")
        child_link_el = el.find("child_link")
        child_pose_el = el.find("child_pose")
        cmd_topic_els = el.findall("cmd_topic")

        if len(cmd_topic_els) == 1:
            cmd_topic = cmd_topic_els[0].text if cmd_topic_els[0].text is not None else None
        elif len(cmd_topic_els) > 1:
            cmd_topic = [t.text for t in cmd_topic_els if t.text is not None]
        else:
            cmd_topic = None

        return cls(
            parent_link=parent_link_el.text if parent_link_el is not None and parent_link_el.text is not None else None,
            child_model=child_model_el.text if child_model_el is not None and child_model_el.text is not None else None,
            child_link=child_link_el.text if child_link_el is not None and child_link_el.text is not None else None,
            child_pose=child_pose_el.text if child_pose_el is not None and child_pose_el.text is not None else None,
            cmd_topic=cmd_topic
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = super().to_sdf(version)
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add("parent_link", self.parent_link)
        _add("child_model", self.child_model)
        _add("child_link", self.child_link)
        if self.child_pose is not None:
            _add("child_pose", _pose(self.child_pose).to_sdf())
            
        if isinstance(self.cmd_topic, list):
            for t in self.cmd_topic:
                _add("cmd_topic", t)
        else:
            _add("cmd_topic", self.cmd_topic)
            
        return el

    def to_version(self, target_version: str):
        return self
