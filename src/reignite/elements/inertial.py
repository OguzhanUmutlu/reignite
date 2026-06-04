from .._sdf.inertial import Inertial as _Inertial


class Inertial(_Inertial):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Inertial._search(search)
        return Inertial._find_help(self.frames, search, rest)
