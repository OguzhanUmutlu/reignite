from .._sdf.light import Light as _Light


class Light(_Light):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Light.__search(search)
        return Light.__find_help(self.frames, search, rest)
