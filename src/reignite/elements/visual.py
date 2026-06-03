from .._sdf.visual import Visual as _Visual


class Visual(_Visual):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Visual.__search(search)
        return Visual.__find_help(self.frames, search, rest) \
            or Visual.__find_help(self.plugins, search, rest)
