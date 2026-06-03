from .._sdf.joint import Joint as _Joint


class Joint(_Joint):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Joint.__search(search)
        if self.sensor is not None and self.sensor.name == search:
            return self.sensor.find_element(rest)
        return Joint.__find_help(self.frames, search, rest)
