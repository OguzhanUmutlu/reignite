from .._sdf.state import State as _State


class State(_State):
    def find_element(self, search: str):
        if not search:
            return None
        search, rest = State.__search(search)
        return State.__find_help(self.joint_states, search, rest) \
            or State.__find_help(self.light_states, search, rest) \
            or State.__find_help(self.lights, search, rest) \
            or State.__find_help(self.model_states, search, rest) \
            or State.__find_help(self.models, search, rest)
