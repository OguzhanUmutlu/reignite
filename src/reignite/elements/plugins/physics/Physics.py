from ...plugin import Plugin


class PhysicsPlugin(Plugin):
    def __init__(self):
        super().__init__(name="gz::sim::systems::Physics", filename="gz-sim-physics-system")
