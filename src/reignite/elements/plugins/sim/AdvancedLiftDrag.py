import math

from reignite.elements.joint import Joint
from reignite.elements.link import Link
from reignite.elements.plugin import Plugin, ParentElement, TextElement


@Plugin.register("gz-sim-advanced-lift-drag-system", "gz::sim::systems::AdvancedLiftDrag")
class AdvancedLiftDragPlugin(Plugin):
    class ControlSurface(ParentElement):
        def __init__(
                self,
                name: str | Joint,
                direction: float,
                CD_ctrl: float,
                CY_ctrl: float,
                CL_ctrl: float,
                Cell_ctrl: float,
                Cem_ctrl: float,
                Cen_ctrl: float
        ):
            if isinstance(name, Joint):
                name = name.name

            super().__init__(
                "control_surface",
                [
                    TextElement("name", name),
                    TextElement("direction", str(direction)),
                    TextElement("CD_ctrl", str(CD_ctrl)),
                    TextElement("CY_ctrl", str(CY_ctrl)),
                    TextElement("CL_ctrl", str(CL_ctrl)),
                    TextElement("Cell_ctrl", str(Cell_ctrl)),
                    TextElement("Cem_ctrl", str(Cem_ctrl)),
                    TextElement("Cen_ctrl", str(Cen_ctrl))
                ]
            )

    def __init__(
            self,
            link_name: str | Link,
            forward: list[float] | tuple[float, float, float] | str,
            upward: list[float] | tuple[float, float, float] | str,
            area: float = 1.0,
            air_density: float = 1.2041,
            radial_symmetry: bool = False,
            AR: float = 0.0,
            mac: float = 0.0,
            eff: float = 0.0,
            cp: list[float] | tuple[float, float, float] | str = (0.0, 0.0, 0.0),
            CL0: float = 0.0, CD0: float = 0.0, Cem0: float = 0.0,
            CLa: float = 0.0, CYa: float = 0.0, Cella: float = 0.0, Cema: float = 0.0, Cena: float = 0.0,
            CLb: float = 0.0, CYb: float = 0.0, Cellb: float = 0.0, Cemb: float = 0.0, Cenb: float = 0.0,
            alpha_stall: float = math.pi / 2.0,
            Cema_stall: float = 0.0,
            CDp: float = 0.0, CYp: float = 0.0, CLp: float = 0.0, Cellp: float = 0.0, Cemp: float = 0.0,
            Cenp: float = 0.0,
            CDq: float = 0.0, CYq: float = 0.0, CLq: float = 0.0, Cellq: float = 0.0, Cemq: float = 0.0,
            Cenq: float = 0.0,
            CDr: float = 0.0, CYr: float = 0.0, CLr: float = 0.0, Cellr: float = 0.0, Cemr: float = 0.0,
            Cenr: float = 0.0,
            control_surfaces: list[ControlSurface] | ControlSurface | None = None,
            num_ctrl_surfaces: int | None = None,
            control_joint_rad_to_cl: float = 4.0
    ):
        resolved_link_name = link_name.name if isinstance(link_name, Link) else link_name

        elements = []
        if control_surfaces is not None:
            if isinstance(control_surfaces, AdvancedLiftDragPlugin.ControlSurface):
                control_surfaces = [control_surfaces]
            elements.extend(control_surfaces)

        if num_ctrl_surfaces is None:
            num_ctrl_surfaces = len(control_surfaces) if control_surfaces else 0

        if isinstance(forward, (list, tuple)):
            forward = " ".join(map(str, forward))
        if isinstance(upward, (list, tuple)):
            upward = " ".join(map(str, upward))
        if isinstance(cp, (list, tuple)):
            cp = " ".join(map(str, cp))

        super().__init__(
            sdf_version=None,
            filename="gz-sim-advanced-lift-drag-system",
            name="gz::sim::systems::AdvancedLiftDrag",
            elements=elements,
            link_name=resolved_link_name,
            forward=forward,
            upward=upward,
            area=area,
            air_density=air_density,
            radial_symmetry=radial_symmetry,
            AR=AR,
            mac=mac,
            eff=eff,
            cp=cp,
            CL0=CL0, CD0=CD0, Cem0=Cem0,
            CLa=CLa, CYa=CYa, Cella=Cella, Cema=Cema, Cena=Cena,
            CLb=CLb, CYb=CYb, Cellb=Cellb, Cemb=Cemb, Cenb=Cenb,
            alpha_stall=alpha_stall,
            Cema_stall=Cema_stall,
            CDp=CDp, CYp=CYp, CLp=CLp, Cellp=Cellp, Cemp=Cemp, Cenp=Cenp,
            CDq=CDq, CYq=CYq, CLq=CLq, Cellq=Cellq, Cemq=Cemq, Cenq=Cenq,
            CDr=CDr, CYr=CYr, CLr=CLr, Cellr=Cellr, Cemr=Cemr, Cenr=Cenr,
            num_ctrl_surfaces=num_ctrl_surfaces,
            control_joint_rad_to_cl=control_joint_rad_to_cl
        )
