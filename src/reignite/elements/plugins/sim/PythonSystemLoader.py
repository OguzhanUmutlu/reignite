from ...plugin import Plugin


@Plugin.register("gz-sim-python-system-loader-system", "gz::sim::systems::PythonSystemLoader")
class PythonSystemLoaderPlugin(Plugin):
    def __init__(
            self,
            module_name: str | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-python-system-loader-system",
            name="gz::sim::systems::PythonSystemLoader",
            module_name=module_name,
        )
