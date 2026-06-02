from .._sdf.gui import Gui as _Gui


class Gui(_Gui):
    class Camera(_Gui.Camera):
        def find_element(self, search: str):
            if not search:
                return None
            search, rest = Gui.Camera.__search(search)
            if self.track_visual is not None and self.track_visual.name == search:
                return self.track_visual.find_element(rest)
            return Gui.Camera.__find_help(self.frames, search, rest)

    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Gui.__search(search)
        if self.camera is not None and self.camera.name == search:
            return self.camera.find_element(rest)
        return Gui.__find_help(self.plugins, search, rest)
