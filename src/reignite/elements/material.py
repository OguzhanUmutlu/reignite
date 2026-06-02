from .._sdf.material import Material
from ..utils import Color


class SimpleMaterial(Material):
    def __init__(self, color: Color):
        super().__init__(
            ambient=color,
            diffuse=color,
            emissive=color,
            specular=Color(127, 127, 127)
        )
