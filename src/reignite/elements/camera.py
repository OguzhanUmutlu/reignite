from .._sdf.camera import Camera as _Camera


class Camera(_Camera):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Camera._search(search)
        return Camera._find_help(self.frames, search, rest)
