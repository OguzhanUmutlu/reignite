from ...plugin import Plugin


class NavSatPlugin(Plugin):
    def __init__(self):
        super().__init__(name="gz::sim::systems::NavSat", filename="gz-sim-navsat-system")
