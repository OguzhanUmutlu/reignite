from .._sdf.model_state import ModelState as _ModelState


class ModelState(_ModelState):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = ModelState._search(search)
        return ModelState._find_help(self.frames, search, rest) \
            or ModelState._find_help(self.joint_states, search, rest) \
            or ModelState._find_help(self.link_states, search, rest) \
            or ModelState._find_help(self.model_states, search, rest)
