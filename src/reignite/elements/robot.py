from .._sdf.robot import Robot as _Robot


class Robot(_Robot):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Robot.__search(search)
        return Robot.__find_help(self.grippers, search, rest) \
            or Robot.__find_help(self.joints, search, rest) \
            or Robot.__find_help(self.links, search, rest) \
            or Robot.__find_help(self.plugins, search, rest)
