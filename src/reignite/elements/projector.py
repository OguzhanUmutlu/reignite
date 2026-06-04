from .._sdf.projector import Projector as _Projector


class Projector(_Projector):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Projector._search(search)
        return Projector._find_help(self.frames, search, rest) \
            or Projector._find_help(self.plugins, search, rest)
