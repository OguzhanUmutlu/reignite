from .._sdf.contact import Contact as _Contact


class Contact(_Contact):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = Contact._search(search)
        if self.collision is not None and self.collision.name == search:
            return self.collision.find_element(rest)
        return None
