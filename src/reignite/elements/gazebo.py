from .._sdf.gazebo import Gazebo as _Gazebo


class Gazebo(_Gazebo):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Gazebo._search(search)
        return Gazebo._find_help(self.actors, search, rest) \
            or Gazebo._find_help(self.lights, search, rest) \
            or Gazebo._find_help(self.models, search, rest) \
            or Gazebo._find_help(self.worlds, search, rest)
