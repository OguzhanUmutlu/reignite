from .._sdf.projector import Projector as _Projector


class Projector(_Projector):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Projector.__search(search)
        return Projector.__find_help(self.frames, search, rest) \
            or Projector.__find_help(self.plugins, search, rest)
