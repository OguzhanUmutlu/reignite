from .._sdf.collision import Collision as _Collision


class Collision(_Collision):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Collision.__search(search)
        return Collision.__find_help(self.frames, search, rest)
