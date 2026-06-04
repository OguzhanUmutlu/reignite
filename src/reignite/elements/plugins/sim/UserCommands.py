from ...plugin import Plugin


@Plugin.register("gz-sim-user-commands-system", "gz::sim::systems::UserCommands")
class UserCommandsPlugin(Plugin):
    def __init__(
            self,
            set_all_light_entities: bool | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-user-commands-system",
            name="gz::sim::systems::UserCommands",
            set_all_light_entities=set_all_light_entities,
        )
