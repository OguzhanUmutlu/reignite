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

    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = World.__search(search)
        if self.physics is not None and self.physics.name == search:
            return self.physics.find_element(rest)
        return World.__find_help(self.actors, search, rest) \
            or World.__find_help(self.models, search, rest) \
            or World.__find_help(self.frames, search, rest) \
            or World.__find_help(self.includes, search, rest) \
            or World.__find_help(self.joints, search, rest) \
            or World.__find_help(self.lights, search, rest) \
            or World.__find_help(self.models, search, rest) \
            or World.__find_help(self.plugins, search, rest) \
            or World.__find_help(self.populations, search, rest) \
            or World.__find_help(self.roads, search, rest)
