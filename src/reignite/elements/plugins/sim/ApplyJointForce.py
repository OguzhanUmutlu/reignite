from xml.etree import ElementTree as ET
from ...joint import Joint
from ...plugin import Plugin


@Plugin.register("gz-sim-apply-joint-force-system", "gz::sim::systems::ApplyJointForce")
class ApplyJointForcePlugin(Plugin):
    def __init__(
            self,
            joint_name: str | Joint
    ):
        self.joint_name = joint_name.name if isinstance(joint_name, Joint) else joint_name
        super().__init__(sdf_version=None, filename="gz-sim-apply-joint-force-system", name="gz::sim::systems::ApplyJointForce")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_el = el.find('joint_name')

        return cls(
            joint_name=int(joint_name_el.text) if joint_name_el is not None and joint_name_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::ApplyJointForce", filename="gz-sim-apply-joint-force-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('joint_name', self.joint_name)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        joint_name_el = el.find('joint_name')

        return cls(
            joint_name=int(joint_name_el.text) if joint_name_el is not None and joint_name_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::ApplyJointForce", filename="gz-sim-apply-joint-force-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('joint_name', self.joint_name)
            
        return el

    def to_version(self, target_version: str):
        return self
