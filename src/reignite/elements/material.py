from ..sdf.material import *  # noqa: F401
from ..utils import Color


class SimpleMaterial(Material):
    def __init__(self, color: Color):
        super().__init__(
            ambient=color,
            diffuse=color,
            emissive=color,
            specular=Color(0.5, 0.5, 0.5)
        )
