from .._sdf.collision import Collision as _Collision


class Collision(_Collision):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Collision._search(search)
        return Collision._find_help(self.frames, search, rest)
