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

    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Model.__search(search)
        return Model.__find_help(self.frames, search, rest) \
            or Model.__find_help(self.grippers, search, rest) \
            or Model.__find_help(self.includes, search, rest) \
            or Model.__find_help(self.joints, search, rest) \
            or Model.__find_help(self.links, search, rest) \
            or Model.__find_help(self.model_states, search, rest) \
            or Model.__find_help(self.models, search, rest) \
            or Model.__find_help(self.plugins, search, rest)
