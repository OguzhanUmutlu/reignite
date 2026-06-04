from .._sdf.model import Model as _Model
from ..utils.model import BaseModel


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

    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Model._search(search)
        return Model._find_help(self.frames, search, rest) \
            or Model._find_help(self.grippers, search, rest) \
            or Model._find_help(self.includes, search, rest) \
            or Model._find_help(self.joints, search, rest) \
            or Model._find_help(self.links, search, rest) \
            or Model._find_help(self.model_states, search, rest) \
            or Model._find_help(self.models, search, rest) \
            or Model._find_help(self.plugins, search, rest)
