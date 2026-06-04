from ...plugin import Plugin


@Plugin.register("gz-sim-model-photo-shoot-system", "gz::sim::systems::ModelPhotoShoot")
class ModelPhotoShootPlugin(Plugin):
    def __init__(
            self,
            translation_data_file: str | None = None,
            random_joints_pose: bool | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-model-photo-shoot-system",
            name="gz::sim::systems::ModelPhotoShoot",
            translation_data_file=translation_data_file,
            random_joints_pose=random_joints_pose,
        )
