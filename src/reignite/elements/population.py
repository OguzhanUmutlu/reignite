from .._sdf.population import Population as _Population


class Population(_Population):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Population._search(search)
        return Population._find_help(self.frames, search, rest) \
            or Population._find_help(self.models, search, rest)
