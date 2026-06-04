from ...plugin import Plugin


@Plugin.register("gz-sim-lens-flare-system", "gz::sim::systems::LensFlare")
class LensFlarePlugin(Plugin):
    def __init__(
            self,
            camera_name: str,
            light_name: str | None = None,
            scale: float = 1.0,
            color: tuple[float, float, float] = (1.4, 1.2, 1.0),
            occlusion_steps: int = 10
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-lens-flare-system",
            name="gz::sim::systems::LensFlare",
            camera_name=camera_name,
            light_name=light_name,
            scale=scale,
            color=color,
            occlusion_steps=occlusion_steps
        )
