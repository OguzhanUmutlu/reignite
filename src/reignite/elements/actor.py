from .._sdf.actor import Actor as _Actor


class Actor(_Actor):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Actor.__search(search)
        return Actor.__find_help(self.animations, search, rest) \
            or Actor.__find_help(self.frames, search, rest) \
            or Actor.__find_help(self.joints, search, rest) \
            or Actor.__find_help(self.links, search, rest)
