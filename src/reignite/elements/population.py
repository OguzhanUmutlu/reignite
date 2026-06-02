from .._sdf.population import Population as _Population


class Population(_Population):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Population.__search(search)
        return Population.__find_help(self.frames, search, rest) \
            or Population.__find_help(self.models, search, rest)
