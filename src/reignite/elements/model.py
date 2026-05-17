from .._sdf.model import Model as _Model


class Model(_Model):
    def get_collisions(self):
        for link in self.links:
            yield from link.collisions

    def get_visuals(self):
        for link in self.links:
            yield from link.visuals

    def get_geometries(self):
        for link in self.links:
            yield from link.get_geometries()
