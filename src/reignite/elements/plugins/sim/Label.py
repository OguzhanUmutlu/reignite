from ...plugin import Plugin


@Plugin.register("gz-sim-label-system", "gz::sim::systems::Label")
class LabelPlugin(Plugin):
    def __init__(
            self,
            label: int
    ):
        if not isinstance(label, int):
            raise TypeError("label must be an integer.")

        if label < 0 or label > 255:
            raise ValueError(f"label value {label} is not in [0-255] range.")

        super().__init__(
            sdf_version=None,
            filename="gz-sim-label-system",
            name="gz::sim::systems::Label",
            label=label
        )
