from .._sdf.link import Link as _Link


class Link(_Link):
    def get_geometries(self):
        for visual in self.visuals:
            yield visual.geometry
        for collision in self.collisions:
            yield collision.geometry
