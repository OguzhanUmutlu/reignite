import xml.etree.ElementTree as ET

from .errors import SDFError


class BaseModel:
    def __init__(self, sdf_version: str = None):
        self.sdfversion = sdf_version

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str):
        res = cls._from_sdf(el, version)
        if isinstance(res, SDFError):
            raise ValueError(str(res))
        return res

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        raise NotImplementedError

    def to_sdf(self, version: str = None) -> ET.Element:
        raise NotImplementedError

    def to_version(self, target_version: str) -> "BaseModel":
        raise NotImplementedError

    def _find_element(self, search: str):
        return None

    def find_element(self, search: str, assert_class=None):
        result = self._find_element(search)
        if result is None:
            raise ValueError(f"Element not found: {search}")
        if assert_class is not None and not isinstance(result, assert_class):
            raise ValueError(
                f"Element '{search}' is not of expected type {assert_class.__name__}: {type(result).__name__}")
        return result

    @staticmethod
    def __find_help(s, search: str, rest: str):
        if s.name == search:
            return s.find_element(rest)
        return None

    @staticmethod
    def __search(search: str):
        spl = search.split("::")
        return spl[0], "::".join(spl[1:])
