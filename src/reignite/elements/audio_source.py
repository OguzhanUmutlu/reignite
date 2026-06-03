from .._sdf.audio_source import AudioSource as _AudioSource


class AudioSource(_AudioSource):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = AudioSource.__search(search)
        return AudioSource.__find_help(self.frames, search, rest)
