from .._sdf.audio_source import AudioSource as _AudioSource


class AudioSource(_AudioSource):
    def _find_element(self, search: str):
        if not search:
            return None
        search, rest = AudioSource._search(search)
        return AudioSource._find_help(self.frames, search, rest)
