from .._sdf.link_state import LinkState as _LinkState


class LinkState(_LinkState):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = LinkState._search(search)
        return LinkState._find_help(self.collision_states, search, rest)
