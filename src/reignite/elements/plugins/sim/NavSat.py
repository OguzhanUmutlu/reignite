from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-navsat-system", "gz::sim::systems::NavSat")
class NavSatPlugin(Plugin):
    def __init__(self):
        super().__init__(filename="gz-sim-navsat-system", name="gz::sim::systems::NavSat")
