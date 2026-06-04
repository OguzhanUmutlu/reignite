from .._sdf.light import Light as _Light


class Light(_Light):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Light._search(search)
        return Light._find_help(self.frames, search, rest)
