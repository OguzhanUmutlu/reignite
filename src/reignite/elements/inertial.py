from .._sdf.inertial import Inertial as _Inertial


class Inertial(_Inertial):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Inertial.__search(search)
        return Inertial.__find_help(self.frames, search, rest)
