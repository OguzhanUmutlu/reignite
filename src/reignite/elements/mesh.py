from .._sdf.mesh import Mesh as _Mesh


class Mesh(_Mesh):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = Mesh.__search(search)
        if self.submesh is not None and self.submesh.name == search:
            return self.submesh.find_element(rest)
        return None
