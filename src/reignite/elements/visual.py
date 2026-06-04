from .._sdf.visual import Visual as _Visual


class Visual(_Visual):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Visual._search(search)
        return Visual._find_help(self.frames, search, rest) \
            or Visual._find_help(self.plugins, search, rest)
