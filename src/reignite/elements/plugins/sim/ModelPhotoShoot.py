from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("gz-sim-model-photo-shoot-system", "gz::sim::systems::ModelPhotoShoot")
class ModelPhotoShootPlugin(Plugin):
    def __init__(
            self,
            translation_data_file: str | None = None,
            random_joints_pose: bool | None = None,
    ):
        self.translation_data_file = translation_data_file
        self.random_joints_pose = random_joints_pose
        super().__init__(sdf_version=None, filename="gz-sim-model-photo-shoot-system",
                         name="gz::sim::systems::ModelPhotoShoot")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        translation_data_file_el = el.find('translation_data_file')
        random_joints_pose_el = el.find('random_joints_pose')

        return cls(
            translation_data_file=translation_data_file_el.text if translation_data_file_el is not None and translation_data_file_el.text is not None else None,
            random_joints_pose=random_joints_pose_el.text.lower() == 'true' if random_joints_pose_el is not None and random_joints_pose_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::ModelPhotoShoot",
                        filename="gz-sim-model-photo-shoot-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('translation_data_file', self.translation_data_file)
        _add('random_joints_pose', self.random_joints_pose)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        translation_data_file_el = el.find('translation_data_file')
        random_joints_pose_el = el.find('random_joints_pose')

        return cls(
            translation_data_file=translation_data_file_el.text if translation_data_file_el is not None and translation_data_file_el.text is not None else None,
            random_joints_pose=random_joints_pose_el.text.lower() == 'true' if random_joints_pose_el is not None and random_joints_pose_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::ModelPhotoShoot",
                        filename="gz-sim-model-photo-shoot-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('translation_data_file', self.translation_data_file)
        _add('random_joints_pose', self.random_joints_pose)

        return el

    def to_version(self, target_version: str):
        return self
