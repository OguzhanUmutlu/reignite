from xml.etree import ElementTree as ET
import math

from reignite.elements.joint import Joint
from reignite.elements.link import Link
from reignite.elements.plugin import Plugin, ParentElement, TextElement


from reignite.utils.model import BaseModel

@Plugin.register("gz-sim-advanced-lift-drag-system", "gz::sim::systems::AdvancedLiftDrag")
class AdvancedLiftDragPlugin(Plugin):
    class ControlSurface(BaseModel):
        def __init__(
                self,
                name: str | Joint | None = None,
                direction: float | None = None,
                CD_ctrl: float | None = None,
                CY_ctrl: float | None = None,
                CL_ctrl: float | None = None,
                Cell_ctrl: float | None = None,
                Cem_ctrl: float | None = None,
                Cen_ctrl: float | None = None
        ):
            super().__init__(sdf_version=None)
            self.name = name.name if isinstance(name, Joint) else name
            self.direction = direction
            self.CD_ctrl = CD_ctrl
            self.CY_ctrl = CY_ctrl
            self.CL_ctrl = CL_ctrl
            self.Cell_ctrl = Cell_ctrl
            self.Cem_ctrl = Cem_ctrl
            self.Cen_ctrl = Cen_ctrl

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            name_el = el.find("name")
            direction_el = el.find("direction")
            CD_ctrl_el = el.find("CD_ctrl")
            CY_ctrl_el = el.find("CY_ctrl")
            CL_ctrl_el = el.find("CL_ctrl")
            Cell_ctrl_el = el.find("Cell_ctrl")
            Cem_ctrl_el = el.find("Cem_ctrl")
            Cen_ctrl_el = el.find("Cen_ctrl")
            
            return cls(
                name=name_el.text if name_el is not None else None,
                direction=float(direction_el.text) if direction_el is not None and direction_el.text is not None else None,
                CD_ctrl=float(CD_ctrl_el.text) if CD_ctrl_el is not None and CD_ctrl_el.text is not None else None,
                CY_ctrl=float(CY_ctrl_el.text) if CY_ctrl_el is not None and CY_ctrl_el.text is not None else None,
                CL_ctrl=float(CL_ctrl_el.text) if CL_ctrl_el is not None and CL_ctrl_el.text is not None else None,
                Cell_ctrl=float(Cell_ctrl_el.text) if Cell_ctrl_el is not None and Cell_ctrl_el.text is not None else None,
                Cem_ctrl=float(Cem_ctrl_el.text) if Cem_ctrl_el is not None and Cem_ctrl_el.text is not None else None,
                Cen_ctrl=float(Cen_ctrl_el.text) if Cen_ctrl_el is not None and Cen_ctrl_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("control_surface")
            
            def _add(k, v):
                if v is not None:
                    child = ET.Element(k)
                    child.text = str(v)
                    e.append(child)
                    
            _add("name", self.name)
            _add("direction", self.direction)
            _add("CD_ctrl", self.CD_ctrl)
            _add("CY_ctrl", self.CY_ctrl)
            _add("CL_ctrl", self.CL_ctrl)
            _add("Cell_ctrl", self.Cell_ctrl)
            _add("Cem_ctrl", self.Cem_ctrl)
            _add("Cen_ctrl", self.Cen_ctrl)
            return e

        def to_version(self, target_version: str):
            return self

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

        self.link_name = resolved_link_name
        self.forward = forward
        self.upward = upward
        self.area = area
        self.air_density = air_density
        self.radial_symmetry = radial_symmetry
        self.AR = AR
        self.mac = mac
        self.eff = eff
        self.cp = cp
        self.CL0 = CL0
        self.CD0 = CD0
        self.Cem0 = Cem0
        self.CLa = CLa
        self.CYa = CYa
        self.Cella = Cella
        self.Cema = Cema
        self.Cena = Cena
        self.CLb = CLb
        self.CYb = CYb
        self.Cellb = Cellb
        self.Cemb = Cemb
        self.Cenb = Cenb
        self.alpha_stall = alpha_stall
        self.Cema_stall = Cema_stall
        self.CDp = CDp
        self.CYp = CYp
        self.CLp = CLp
        self.Cellp = Cellp
        self.Cemp = Cemp
        self.Cenp = Cenp
        self.CDq = CDq
        self.CYq = CYq
        self.CLq = CLq
        self.Cellq = Cellq
        self.Cemq = Cemq
        self.Cenq = Cenq
        self.CDr = CDr
        self.CYr = CYr
        self.CLr = CLr
        self.Cellr = Cellr
        self.Cemr = Cemr
        self.Cenr = Cenr
        self.control_surfaces = control_surfaces
        self.num_ctrl_surfaces = num_ctrl_surfaces
        self.control_joint_rad_to_cl = control_joint_rad_to_cl
        super().__init__(sdf_version=None, filename="gz-sim-advanced-lift-drag-system", name=name)

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        forward_els = el.findall('forward')
        forward_vals = [e.text for e in forward_els if e.text is not None] if forward_els else None
        upward_els = el.findall('upward')
        upward_vals = [e.text for e in upward_els if e.text is not None] if upward_els else None
        area_el = el.find('area')
        air_density_el = el.find('air_density')
        radial_symmetry_el = el.find('radial_symmetry')
        AR_el = el.find('AR')
        mac_el = el.find('mac')
        eff_el = el.find('eff')
        cp_els = el.findall('cp')
        cp_vals = [e.text for e in cp_els if e.text is not None] if cp_els else None
        CL0_el = el.find('CL0')
        CD0_el = el.find('CD0')
        Cem0_el = el.find('Cem0')
        CLa_el = el.find('CLa')
        CYa_el = el.find('CYa')
        Cella_el = el.find('Cella')
        Cema_el = el.find('Cema')
        Cena_el = el.find('Cena')
        CLb_el = el.find('CLb')
        CYb_el = el.find('CYb')
        Cellb_el = el.find('Cellb')
        Cemb_el = el.find('Cemb')
        Cenb_el = el.find('Cenb')
        alpha_stall_el = el.find('alpha_stall')
        Cema_stall_el = el.find('Cema_stall')
        CDp_el = el.find('CDp')
        CYp_el = el.find('CYp')
        CLp_el = el.find('CLp')
        Cellp_el = el.find('Cellp')
        Cemp_el = el.find('Cemp')
        Cenp_el = el.find('Cenp')
        CDq_el = el.find('CDq')
        CYq_el = el.find('CYq')
        CLq_el = el.find('CLq')
        Cellq_el = el.find('Cellq')
        Cemq_el = el.find('Cemq')
        Cenq_el = el.find('Cenq')
        CDr_el = el.find('CDr')
        CYr_el = el.find('CYr')
        CLr_el = el.find('CLr')
        Cellr_el = el.find('Cellr')
        Cemr_el = el.find('Cemr')
        Cenr_el = el.find('Cenr')
        control_surfaces_els = el.findall('control_surface')
        control_surfaces_vals = [cls.ControlSurface._from_sdf(c, version) for c in control_surfaces_els] if control_surfaces_els else None
        num_ctrl_surfaces_el = el.find('num_ctrl_surfaces')
        control_joint_rad_to_cl_el = el.find('control_joint_rad_to_cl')

        return cls(
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            forward=forward_vals,
            upward=upward_vals,
            area=float(area_el.text) if area_el is not None and area_el.text is not None else None,
            air_density=float(air_density_el.text) if air_density_el is not None and air_density_el.text is not None else None,
            radial_symmetry=radial_symmetry_el.text.lower() == 'true' if radial_symmetry_el is not None and radial_symmetry_el.text is not None else None,
            AR=float(AR_el.text) if AR_el is not None and AR_el.text is not None else None,
            mac=float(mac_el.text) if mac_el is not None and mac_el.text is not None else None,
            eff=float(eff_el.text) if eff_el is not None and eff_el.text is not None else None,
            cp=cp_vals,
            CL0=float(CL0_el.text) if CL0_el is not None and CL0_el.text is not None else None,
            CD0=float(CD0_el.text) if CD0_el is not None and CD0_el.text is not None else None,
            Cem0=float(Cem0_el.text) if Cem0_el is not None and Cem0_el.text is not None else None,
            CLa=float(CLa_el.text) if CLa_el is not None and CLa_el.text is not None else None,
            CYa=float(CYa_el.text) if CYa_el is not None and CYa_el.text is not None else None,
            Cella=float(Cella_el.text) if Cella_el is not None and Cella_el.text is not None else None,
            Cema=float(Cema_el.text) if Cema_el is not None and Cema_el.text is not None else None,
            Cena=float(Cena_el.text) if Cena_el is not None and Cena_el.text is not None else None,
            CLb=float(CLb_el.text) if CLb_el is not None and CLb_el.text is not None else None,
            CYb=float(CYb_el.text) if CYb_el is not None and CYb_el.text is not None else None,
            Cellb=float(Cellb_el.text) if Cellb_el is not None and Cellb_el.text is not None else None,
            Cemb=float(Cemb_el.text) if Cemb_el is not None and Cemb_el.text is not None else None,
            Cenb=float(Cenb_el.text) if Cenb_el is not None and Cenb_el.text is not None else None,
            alpha_stall=float(alpha_stall_el.text) if alpha_stall_el is not None and alpha_stall_el.text is not None else None,
            Cema_stall=float(Cema_stall_el.text) if Cema_stall_el is not None and Cema_stall_el.text is not None else None,
            CDp=float(CDp_el.text) if CDp_el is not None and CDp_el.text is not None else None,
            CYp=float(CYp_el.text) if CYp_el is not None and CYp_el.text is not None else None,
            CLp=float(CLp_el.text) if CLp_el is not None and CLp_el.text is not None else None,
            Cellp=float(Cellp_el.text) if Cellp_el is not None and Cellp_el.text is not None else None,
            Cemp=float(Cemp_el.text) if Cemp_el is not None and Cemp_el.text is not None else None,
            Cenp=float(Cenp_el.text) if Cenp_el is not None and Cenp_el.text is not None else None,
            CDq=float(CDq_el.text) if CDq_el is not None and CDq_el.text is not None else None,
            CYq=float(CYq_el.text) if CYq_el is not None and CYq_el.text is not None else None,
            CLq=float(CLq_el.text) if CLq_el is not None and CLq_el.text is not None else None,
            Cellq=float(Cellq_el.text) if Cellq_el is not None and Cellq_el.text is not None else None,
            Cemq=float(Cemq_el.text) if Cemq_el is not None and Cemq_el.text is not None else None,
            Cenq=float(Cenq_el.text) if Cenq_el is not None and Cenq_el.text is not None else None,
            CDr=float(CDr_el.text) if CDr_el is not None and CDr_el.text is not None else None,
            CYr=float(CYr_el.text) if CYr_el is not None and CYr_el.text is not None else None,
            CLr=float(CLr_el.text) if CLr_el is not None and CLr_el.text is not None else None,
            Cellr=float(Cellr_el.text) if Cellr_el is not None and Cellr_el.text is not None else None,
            Cemr=float(Cemr_el.text) if Cemr_el is not None and Cemr_el.text is not None else None,
            Cenr=float(Cenr_el.text) if Cenr_el is not None and Cenr_el.text is not None else None,
            control_surfaces=control_surfaces_vals,
            num_ctrl_surfaces=int(num_ctrl_surfaces_el.text) if num_ctrl_surfaces_el is not None and num_ctrl_surfaces_el.text is not None else None,
            control_joint_rad_to_cl=float(control_joint_rad_to_cl_el.text) if control_joint_rad_to_cl_el is not None and control_joint_rad_to_cl_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::AdvancedLiftDrag", filename="gz-sim-advanced-lift-drag-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link_name', self.link_name)
        if self.forward is not None:
            for v in (self.forward if isinstance(self.forward, list) else [self.forward]):
                _add('forward', v)
        if self.upward is not None:
            for v in (self.upward if isinstance(self.upward, list) else [self.upward]):
                _add('upward', v)
        _add('area', self.area)
        _add('air_density', self.air_density)
        _add('radial_symmetry', self.radial_symmetry)
        _add('AR', self.AR)
        _add('mac', self.mac)
        _add('eff', self.eff)
        if self.cp is not None:
            for v in (self.cp if isinstance(self.cp, list) else [self.cp]):
                _add('cp', v)
        _add('CL0', self.CL0)
        _add('CD0', self.CD0)
        _add('Cem0', self.Cem0)
        _add('CLa', self.CLa)
        _add('CYa', self.CYa)
        _add('Cella', self.Cella)
        _add('Cema', self.Cema)
        _add('Cena', self.Cena)
        _add('CLb', self.CLb)
        _add('CYb', self.CYb)
        _add('Cellb', self.Cellb)
        _add('Cemb', self.Cemb)
        _add('Cenb', self.Cenb)
        _add('alpha_stall', self.alpha_stall)
        _add('Cema_stall', self.Cema_stall)
        _add('CDp', self.CDp)
        _add('CYp', self.CYp)
        _add('CLp', self.CLp)
        _add('Cellp', self.Cellp)
        _add('Cemp', self.Cemp)
        _add('Cenp', self.Cenp)
        _add('CDq', self.CDq)
        _add('CYq', self.CYq)
        _add('CLq', self.CLq)
        _add('Cellq', self.Cellq)
        _add('Cemq', self.Cemq)
        _add('Cenq', self.Cenq)
        _add('CDr', self.CDr)
        _add('CYr', self.CYr)
        _add('CLr', self.CLr)
        _add('Cellr', self.Cellr)
        _add('Cemr', self.Cemr)
        _add('Cenr', self.Cenr)
        if self.control_surfaces is not None:
            for v in (self.control_surfaces if isinstance(self.control_surfaces, list) else [self.control_surfaces]):
                el.append(v.to_sdf(version))
        _add('num_ctrl_surfaces', self.num_ctrl_surfaces)
        _add('control_joint_rad_to_cl', self.control_joint_rad_to_cl)
            
        return el

    def to_version(self, target_version: str):
        if self.control_surfaces is not None:
            for v in (self.control_surfaces if isinstance(self.control_surfaces, list) else [self.control_surfaces]):
                v.to_version(target_version)
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        forward_els = el.findall('forward')
        forward_vals = [e.text for e in forward_els if e.text is not None] if forward_els else None
        upward_els = el.findall('upward')
        upward_vals = [e.text for e in upward_els if e.text is not None] if upward_els else None
        area_el = el.find('area')
        air_density_el = el.find('air_density')
        radial_symmetry_el = el.find('radial_symmetry')
        AR_el = el.find('AR')
        mac_el = el.find('mac')
        eff_el = el.find('eff')
        cp_els = el.findall('cp')
        cp_vals = [e.text for e in cp_els if e.text is not None] if cp_els else None
        CL0_el = el.find('CL0')
        CD0_el = el.find('CD0')
        Cem0_el = el.find('Cem0')
        CLa_el = el.find('CLa')
        CYa_el = el.find('CYa')
        Cella_el = el.find('Cella')
        Cema_el = el.find('Cema')
        Cena_el = el.find('Cena')
        CLb_el = el.find('CLb')
        CYb_el = el.find('CYb')
        Cellb_el = el.find('Cellb')
        Cemb_el = el.find('Cemb')
        Cenb_el = el.find('Cenb')
        alpha_stall_el = el.find('alpha_stall')
        Cema_stall_el = el.find('Cema_stall')
        CDp_el = el.find('CDp')
        CYp_el = el.find('CYp')
        CLp_el = el.find('CLp')
        Cellp_el = el.find('Cellp')
        Cemp_el = el.find('Cemp')
        Cenp_el = el.find('Cenp')
        CDq_el = el.find('CDq')
        CYq_el = el.find('CYq')
        CLq_el = el.find('CLq')
        Cellq_el = el.find('Cellq')
        Cemq_el = el.find('Cemq')
        Cenq_el = el.find('Cenq')
        CDr_el = el.find('CDr')
        CYr_el = el.find('CYr')
        CLr_el = el.find('CLr')
        Cellr_el = el.find('Cellr')
        Cemr_el = el.find('Cemr')
        Cenr_el = el.find('Cenr')
        control_surfaces_els = el.findall('control_surfaces')
        control_surfaces_vals = [e.text for e in control_surfaces_els if e.text is not None] if control_surfaces_els else None
        num_ctrl_surfaces_el = el.find('num_ctrl_surfaces')
        control_joint_rad_to_cl_el = el.find('control_joint_rad_to_cl')
        name = el.get('name')
        direction_el = el.find('direction')
        CD_ctrl_el = el.find('CD_ctrl')
        CY_ctrl_el = el.find('CY_ctrl')
        CL_ctrl_el = el.find('CL_ctrl')
        Cell_ctrl_el = el.find('Cell_ctrl')
        Cem_ctrl_el = el.find('Cem_ctrl')
        Cen_ctrl_el = el.find('Cen_ctrl')

        return cls(
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            forward=forward_vals,
            upward=upward_vals,
            area=float(area_el.text) if area_el is not None and area_el.text is not None else None,
            air_density=float(air_density_el.text) if air_density_el is not None and air_density_el.text is not None else None,
            radial_symmetry=radial_symmetry_el.text.lower() == 'true' if radial_symmetry_el is not None and radial_symmetry_el.text is not None else None,
            AR=float(AR_el.text) if AR_el is not None and AR_el.text is not None else None,
            mac=float(mac_el.text) if mac_el is not None and mac_el.text is not None else None,
            eff=float(eff_el.text) if eff_el is not None and eff_el.text is not None else None,
            cp=cp_vals,
            CL0=float(CL0_el.text) if CL0_el is not None and CL0_el.text is not None else None,
            CD0=float(CD0_el.text) if CD0_el is not None and CD0_el.text is not None else None,
            Cem0=float(Cem0_el.text) if Cem0_el is not None and Cem0_el.text is not None else None,
            CLa=float(CLa_el.text) if CLa_el is not None and CLa_el.text is not None else None,
            CYa=float(CYa_el.text) if CYa_el is not None and CYa_el.text is not None else None,
            Cella=float(Cella_el.text) if Cella_el is not None and Cella_el.text is not None else None,
            Cema=float(Cema_el.text) if Cema_el is not None and Cema_el.text is not None else None,
            Cena=float(Cena_el.text) if Cena_el is not None and Cena_el.text is not None else None,
            CLb=float(CLb_el.text) if CLb_el is not None and CLb_el.text is not None else None,
            CYb=float(CYb_el.text) if CYb_el is not None and CYb_el.text is not None else None,
            Cellb=float(Cellb_el.text) if Cellb_el is not None and Cellb_el.text is not None else None,
            Cemb=float(Cemb_el.text) if Cemb_el is not None and Cemb_el.text is not None else None,
            Cenb=float(Cenb_el.text) if Cenb_el is not None and Cenb_el.text is not None else None,
            alpha_stall=float(alpha_stall_el.text) if alpha_stall_el is not None and alpha_stall_el.text is not None else None,
            Cema_stall=float(Cema_stall_el.text) if Cema_stall_el is not None and Cema_stall_el.text is not None else None,
            CDp=float(CDp_el.text) if CDp_el is not None and CDp_el.text is not None else None,
            CYp=float(CYp_el.text) if CYp_el is not None and CYp_el.text is not None else None,
            CLp=float(CLp_el.text) if CLp_el is not None and CLp_el.text is not None else None,
            Cellp=float(Cellp_el.text) if Cellp_el is not None and Cellp_el.text is not None else None,
            Cemp=float(Cemp_el.text) if Cemp_el is not None and Cemp_el.text is not None else None,
            Cenp=float(Cenp_el.text) if Cenp_el is not None and Cenp_el.text is not None else None,
            CDq=float(CDq_el.text) if CDq_el is not None and CDq_el.text is not None else None,
            CYq=float(CYq_el.text) if CYq_el is not None and CYq_el.text is not None else None,
            CLq=float(CLq_el.text) if CLq_el is not None and CLq_el.text is not None else None,
            Cellq=float(Cellq_el.text) if Cellq_el is not None and Cellq_el.text is not None else None,
            Cemq=float(Cemq_el.text) if Cemq_el is not None and Cemq_el.text is not None else None,
            Cenq=float(Cenq_el.text) if Cenq_el is not None and Cenq_el.text is not None else None,
            CDr=float(CDr_el.text) if CDr_el is not None and CDr_el.text is not None else None,
            CYr=float(CYr_el.text) if CYr_el is not None and CYr_el.text is not None else None,
            CLr=float(CLr_el.text) if CLr_el is not None and CLr_el.text is not None else None,
            Cellr=float(Cellr_el.text) if Cellr_el is not None and Cellr_el.text is not None else None,
            Cemr=float(Cemr_el.text) if Cemr_el is not None and Cemr_el.text is not None else None,
            Cenr=float(Cenr_el.text) if Cenr_el is not None and Cenr_el.text is not None else None,
            control_surfaces=control_surfaces_vals,
            num_ctrl_surfaces=int(num_ctrl_surfaces_el.text) if num_ctrl_surfaces_el is not None and num_ctrl_surfaces_el.text is not None else None,
            control_joint_rad_to_cl=float(control_joint_rad_to_cl_el.text) if control_joint_rad_to_cl_el is not None and control_joint_rad_to_cl_el.text is not None else None,
            name=name if name is not None else None,
            direction=float(direction_el.text) if direction_el is not None and direction_el.text is not None else None,
            CD_ctrl=float(CD_ctrl_el.text) if CD_ctrl_el is not None and CD_ctrl_el.text is not None else None,
            CY_ctrl=float(CY_ctrl_el.text) if CY_ctrl_el is not None and CY_ctrl_el.text is not None else None,
            CL_ctrl=float(CL_ctrl_el.text) if CL_ctrl_el is not None and CL_ctrl_el.text is not None else None,
            Cell_ctrl=float(Cell_ctrl_el.text) if Cell_ctrl_el is not None and Cell_ctrl_el.text is not None else None,
            Cem_ctrl=float(Cem_ctrl_el.text) if Cem_ctrl_el is not None and Cem_ctrl_el.text is not None else None,
            Cen_ctrl=float(Cen_ctrl_el.text) if Cen_ctrl_el is not None and Cen_ctrl_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::AdvancedLiftDrag", filename="gz-sim-advanced-lift-drag-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link_name', self.link_name)
        if self.forward is not None:
            for v in (self.forward if isinstance(self.forward, list) else [self.forward]):
                _add('forward', v)
        if self.upward is not None:
            for v in (self.upward if isinstance(self.upward, list) else [self.upward]):
                _add('upward', v)
        _add('area', self.area)
        _add('air_density', self.air_density)
        _add('radial_symmetry', self.radial_symmetry)
        _add('AR', self.AR)
        _add('mac', self.mac)
        _add('eff', self.eff)
        if self.cp is not None:
            for v in (self.cp if isinstance(self.cp, list) else [self.cp]):
                _add('cp', v)
        _add('CL0', self.CL0)
        _add('CD0', self.CD0)
        _add('Cem0', self.Cem0)
        _add('CLa', self.CLa)
        _add('CYa', self.CYa)
        _add('Cella', self.Cella)
        _add('Cema', self.Cema)
        _add('Cena', self.Cena)
        _add('CLb', self.CLb)
        _add('CYb', self.CYb)
        _add('Cellb', self.Cellb)
        _add('Cemb', self.Cemb)
        _add('Cenb', self.Cenb)
        _add('alpha_stall', self.alpha_stall)
        _add('Cema_stall', self.Cema_stall)
        _add('CDp', self.CDp)
        _add('CYp', self.CYp)
        _add('CLp', self.CLp)
        _add('Cellp', self.Cellp)
        _add('Cemp', self.Cemp)
        _add('Cenp', self.Cenp)
        _add('CDq', self.CDq)
        _add('CYq', self.CYq)
        _add('CLq', self.CLq)
        _add('Cellq', self.Cellq)
        _add('Cemq', self.Cemq)
        _add('Cenq', self.Cenq)
        _add('CDr', self.CDr)
        _add('CYr', self.CYr)
        _add('CLr', self.CLr)
        _add('Cellr', self.Cellr)
        _add('Cemr', self.Cemr)
        _add('Cenr', self.Cenr)
        if self.control_surfaces is not None:
            for v in (self.control_surfaces if isinstance(self.control_surfaces, list) else [self.control_surfaces]):
                _add('control_surfaces', v)
        _add('num_ctrl_surfaces', self.num_ctrl_surfaces)
        _add('control_joint_rad_to_cl', self.control_joint_rad_to_cl)
        _add('direction', self.direction)
        _add('CD_ctrl', self.CD_ctrl)
        _add('CY_ctrl', self.CY_ctrl)
        _add('CL_ctrl', self.CL_ctrl)
        _add('Cell_ctrl', self.Cell_ctrl)
        _add('Cem_ctrl', self.Cem_ctrl)
        _add('Cen_ctrl', self.Cen_ctrl)
            
        return el

    def to_version(self, target_version: str):
        return self
