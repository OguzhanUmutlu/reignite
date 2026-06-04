from .._sdf.robot import Robot as _Robot


class Robot(_Robot):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Robot._search(search)
        return Robot._find_help(self.grippers, search, rest) \
            or Robot._find_help(self.joints, search, rest) \
            or Robot._find_help(self.links, search, rest) \
            or Robot._find_help(self.plugins, search, rest)
