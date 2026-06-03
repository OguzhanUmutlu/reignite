from .._sdf.material import Material
from ..utils.color import Color, _ColorT


class SimpleMaterial(Material):
    def __init__(self, color: Color, metalness=0.0, roughness=0.3):
        if color.a != 255:
            super().__init__(
                ambient=color, diffuse=color, double_sided=True,
                pbr=Material.Pbr(
                    metal=Material.Pbr.Metal(
                        albedo_map=f"{color}", metalness=f"{metalness}", roughness=f"{roughness}",
                        emissive_map=f"{color}"
                    )
                )
            )
        else:
            super().__init__(
                ambient=color,
                diffuse=color,
                emissive=color,
                specular=Color(127, 127, 127)
            )


class ScriptMaterial(Material):
    def __init__(
            self, name: str, uris: list[str] | None = None, uri=None,
            ambient: _ColorT | None = None,
            diffuse: _ColorT | None = None,
            double_sided: bool | None = False,
            emissive: _ColorT | None = None,
            lighting: bool | None = True,
            render_order: float | None = 0.0,
            shininess: float | None = 0,
            specular: _ColorT | None = None
    ):
        uris = uris or []
        if uri is not None:
            uris.append(uri)
        super().__init__(
            script=Material.Script(
                uris=uris,
                name=name
            ),
            ambient=ambient,
            diffuse=diffuse,
            double_sided=double_sided,
            emissive=emissive,
            lighting=lighting,
            render_order=render_order,
            shininess=shininess,
            specular=specular
        )
