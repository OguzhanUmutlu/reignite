from reignite.elements import Plugin


class UserCommandsPlugin(Plugin):
    def __init__(self):
        super().__init__(name="gz::sim::systems::UserCommands", filename="gz-sim-user-commands-system")
