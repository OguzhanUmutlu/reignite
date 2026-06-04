from ...link import Link
from ...plugin import Plugin


@Plugin.register("gz-sim-lift-drag-system", "gz::sim::systems::LiftDrag")
class LiftDragPlugin(Plugin):
    def __init__(
            self,
            link_name: str | Link,
            cla: float = 1.0,
            cda: float = 0.01,
            cma: float = 0.0,
            alpha_stall: float = 1.57079632679,
            cla_stall: float = 0.0,
            cda_stall: float = 1.0,
            cma_stall: float = 0.0,
            air_density: float = 1.2041,
            radial_symmetry: bool = False,
            reversible: bool = False,
            area: float = 1.0,
            a0: float = 0.0,
            cp: tuple[float, float, float] = (0.0, 0.0, 0.0),
            cm_delta: float = 0.0,
            forward: tuple[float, float, float] = (1.0, 0.0, 0.0),
            upward: tuple[float, float, float] = (0.0, 0.0, 1.0),
            control_joint_rad_to_cl: float = 4.0,
            control_joint_name: str | None = None
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-lift-drag-system",
            name="gz::sim::systems::LiftDrag",
            link_name=link_name.name if isinstance(link_name, Link) else link_name,
            cla=cla,
            cda=cda,
            cma=cma,
            alpha_stall=alpha_stall,
            cla_stall=cla_stall,
            cda_stall=cda_stall,
            cma_stall=cma_stall,
            air_density=air_density,
            radial_symmetry=radial_symmetry,
            reversible=reversible,
            area=area,
            a0=a0,
            cp=cp,
            cm_delta=cm_delta,
            forward=forward,
            upward=upward,
            control_joint_rad_to_cl=control_joint_rad_to_cl,
            control_joint_name=control_joint_name
        )
