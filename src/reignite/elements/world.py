from .._sdf.world import World as _World


class World(_World):
    def get_collisions(self):
        for model in self.models:
            yield from model.get_collisions()

    def get_visuals(self):
        for model in self.models:
            yield from model.get_visuals()

    def get_geometries(self):
        for model in self.models:
            yield from model.get_geometries()
