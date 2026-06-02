from .._sdf.gazebo import Gazebo as _Gazebo


class Gazebo(_Gazebo):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Gazebo.__search(search)
        return Gazebo.__find_help(self.actors, search, rest) \
            or Gazebo.__find_help(self.lights, search, rest) \
            or Gazebo.__find_help(self.models, search, rest) \
            or Gazebo.__find_help(self.worlds, search, rest)
