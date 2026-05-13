from reignite.elements import Plugin


class SceneBroadcasterPlugin(Plugin):
    def __init__(self):
        super().__init__(name="gz::sim::systems::SceneBroadcaster", filename="gz-sim-scene-broadcaster-system")
