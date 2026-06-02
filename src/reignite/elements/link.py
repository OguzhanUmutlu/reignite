from .._sdf.link import Link as _Link


class Link(_Link):
    def get_geometries(self):
        for visual in self.visuals:
            yield visual.geometry
        for collision in self.collisions:
            yield collision.geometry

    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Link.__search(search)
        if self.sensor is not None and self.sensor.name == search:
            return self.sensor.find_element(rest)
        return Link.__find_help(self.batteries, search, rest) \
            or Link.__find_help(self.collisions, search, rest) \
            or Link.__find_help(self.frames, search, rest) \
            or Link.__find_help(self.lights, search, rest) \
            or Link.__find_help(self.particle_emitters, search, rest) \
            or Link.__find_help(self.visuals, search, rest)
