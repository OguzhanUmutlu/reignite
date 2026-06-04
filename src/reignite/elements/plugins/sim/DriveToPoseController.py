from ...plugin import Plugin


@Plugin.register("gz-sim-drive-to-pose-controller-system", "gz::sim::systems::DriveToPoseController")
class DriveToPoseControllerPlugin(Plugin):
    def __init__(
            self,
            linear_p_gain: float = 1.0,
            angular_p_gain: float = 2.0,
            linear_deviation: float = 0.1,
            angular_deviation: float = 0.05
    ):
        if linear_p_gain < 0.0 or angular_p_gain < 0.0:
            raise ValueError("Proportional gains (linear_p_gain, angular_p_gain) must be non-negative.")

        if linear_deviation < 0.0 or angular_deviation < 0.0:
            raise ValueError("Allowable deviations (linear_deviation, angular_deviation) must be non-negative.")

        super().__init__(
            sdf_version=None,
            filename="gz-sim-drive-to-pose-controller-system",
            name="gz::sim::systems::DriveToPoseController",
            linear_p_gain=linear_p_gain,
            angular_p_gain=angular_p_gain,
            linear_deviation=linear_deviation,
            angular_deviation=angular_deviation
        )
