from ...plugin import Plugin


class EnvironmentPreloadPlugin(Plugin):
    def __init__(
            self,
            data: str,
            ignore_time: bool = False,
            time: str = "t",
            reference: str = "global",
            units: str = "radians",
            x: str = "x",
            y: str = "y",
            z: str = "z"
    ):
        if not data:
            raise ValueError("data (environmental data file path) is required.")

        if reference not in ["global", "spherical", "ecef"]:
            raise ValueError(f"Unknown reference '{reference}'. Must be 'global', 'spherical', or 'ecef'.")

        if reference == "spherical" and units not in ["degrees", "radians"]:
            raise ValueError(f"Unrecognized unit '{units}'. Must be 'degrees' or 'radians'.")

        super().__init__(
            sdf_version=None,
            filename="gz-sim-environment-preload-system",
            name="gz::sim::systems::EnvironmentPreload",
            data=data,
            ignore_time=ignore_time,
            time=time,
            reference=reference,
            units=units,
            x=x,
            y=y,
            z=z
        )
