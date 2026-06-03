from ...plugin import Plugin


class SensorsPlugin(Plugin):
    def __init__(self, render_engine: str = "ogre2"):
        super().__init__(name="gz::sim::systems::Sensors", filename="gz-sim-sensors-system",
                         render_engine=render_engine)
