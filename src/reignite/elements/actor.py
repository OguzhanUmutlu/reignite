from .._sdf.actor import Actor as _Actor


class Actor(_Actor):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Actor._search(search)
        return Actor._find_help(self.animations, search, rest) \
            or Actor._find_help(self.frames, search, rest) \
            or Actor._find_help(self.joints, search, rest) \
            or Actor._find_help(self.links, search, rest)
