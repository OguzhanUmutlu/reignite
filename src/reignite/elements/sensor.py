from .._sdf.sensor import Sensor as _Sensor


class Sensor(_Sensor):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Sensor.__search(search)
        if self.camera is not None and self.camera.name == search:
            return self.camera.find_element(rest)
        return Sensor.__find_help(self.frames, search, rest) \
            or Sensor.__find_help(self.plugins, search, rest)
