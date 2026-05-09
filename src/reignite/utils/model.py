import xml.etree.ElementTree as ET

from .errors import SDFError


class BaseModel:
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

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
