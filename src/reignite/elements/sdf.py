from .._sdf.sdf import Sdf as _Sdf


class Sdf(_Sdf):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Sdf._search(search)
        return Sdf._find_help(self.actors, search, rest) \
            or Sdf._find_help(self.lights, search, rest) \
            or Sdf._find_help(self.models, search, rest) \
            or Sdf._find_help(self.worlds, search, rest)
