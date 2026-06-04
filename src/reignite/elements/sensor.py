from .._sdf.sensor import Sensor as _Sensor


class Sensor(_Sensor):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Sensor._search(search)
        if self.camera is not None and self.camera.name == search:
            return self.camera.find_element(rest)
        return Sensor._find_help(self.frames, search, rest) \
            or Sensor._find_help(self.plugins, search, rest)
