from xml.etree import ElementTree as ET
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
        self.link_name = link_name.name if isinstance(link_name, Link) else link_name
        self.cla = cla
        self.cda = cda
        self.cma = cma
        self.alpha_stall = alpha_stall
        self.cla_stall = cla_stall
        self.cda_stall = cda_stall
        self.cma_stall = cma_stall
        self.air_density = air_density
        self.radial_symmetry = radial_symmetry
        self.reversible = reversible
        self.area = area
        self.a0 = a0
        self.cp = cp
        self.cm_delta = cm_delta
        self.forward = forward
        self.upward = upward
        self.control_joint_rad_to_cl = control_joint_rad_to_cl
        self.control_joint_name = control_joint_name
        super().__init__(sdf_version=None, filename="gz-sim-lift-drag-system", name="gz::sim::systems::LiftDrag")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        cla_el = el.find('cla')
        cda_el = el.find('cda')
        cma_el = el.find('cma')
        alpha_stall_el = el.find('alpha_stall')
        cla_stall_el = el.find('cla_stall')
        cda_stall_el = el.find('cda_stall')
        cma_stall_el = el.find('cma_stall')
        air_density_el = el.find('air_density')
        radial_symmetry_el = el.find('radial_symmetry')
        reversible_el = el.find('reversible')
        area_el = el.find('area')
        a0_el = el.find('a0')
        cp_el = el.find('cp')
        cm_delta_el = el.find('cm_delta')
        forward_el = el.find('forward')
        upward_el = el.find('upward')
        control_joint_rad_to_cl_el = el.find('control_joint_rad_to_cl')
        control_joint_name_el = el.find('control_joint_name')

        def _parse_tuple(el_node):
            if el_node is None or not el_node.text: return None
            parts = el_node.text.split()
            if len(parts) == 3:
                return (float(parts[0]), float(parts[1]), float(parts[2]))
            return None

        return cls(
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            cla=float(cla_el.text) if cla_el is not None and cla_el.text is not None else None,
            cda=float(cda_el.text) if cda_el is not None and cda_el.text is not None else None,
            cma=float(cma_el.text) if cma_el is not None and cma_el.text is not None else None,
            alpha_stall=float(alpha_stall_el.text) if alpha_stall_el is not None and alpha_stall_el.text is not None else None,
            cla_stall=float(cla_stall_el.text) if cla_stall_el is not None and cla_stall_el.text is not None else None,
            cda_stall=float(cda_stall_el.text) if cda_stall_el is not None and cda_stall_el.text is not None else None,
            cma_stall=float(cma_stall_el.text) if cma_stall_el is not None and cma_stall_el.text is not None else None,
            air_density=float(air_density_el.text) if air_density_el is not None and air_density_el.text is not None else None,
            radial_symmetry=radial_symmetry_el.text.lower() in ("true", "1", "yes", "t") if radial_symmetry_el is not None and radial_symmetry_el.text is not None else None,
            reversible=reversible_el.text.lower() in ("true", "1", "yes", "t") if reversible_el is not None and reversible_el.text is not None else None,
            area=float(area_el.text) if area_el is not None and area_el.text is not None else None,
            a0=float(a0_el.text) if a0_el is not None and a0_el.text is not None else None,
            cp=_parse_tuple(cp_el),
            cm_delta=float(cm_delta_el.text) if cm_delta_el is not None and cm_delta_el.text is not None else None,
            forward=_parse_tuple(forward_el),
            upward=_parse_tuple(upward_el),
            control_joint_rad_to_cl=float(control_joint_rad_to_cl_el.text) if control_joint_rad_to_cl_el is not None and control_joint_rad_to_cl_el.text is not None else None,
            control_joint_name=control_joint_name_el.text if control_joint_name_el is not None and control_joint_name_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LiftDrag", filename="gz-sim-lift-drag-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                elif isinstance(v, tuple):
                    child.text = " ".join(map(str, v))
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link_name', self.link_name)
        _add('cla', self.cla)
        _add('cda', self.cda)
        _add('cma', self.cma)
        _add('alpha_stall', self.alpha_stall)
        _add('cla_stall', self.cla_stall)
        _add('cda_stall', self.cda_stall)
        _add('cma_stall', self.cma_stall)
        _add('air_density', self.air_density)
        _add('radial_symmetry', self.radial_symmetry)
        _add('reversible', self.reversible)
        _add('area', self.area)
        _add('a0', self.a0)
        _add('cp', self.cp)
        _add('cm_delta', self.cm_delta)
        _add('forward', self.forward)
        _add('upward', self.upward)
        _add('control_joint_rad_to_cl', self.control_joint_rad_to_cl)
        _add('control_joint_name', self.control_joint_name)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        link_name_el = el.find('link_name')
        cla_el = el.find('cla')
        cda_el = el.find('cda')
        cma_el = el.find('cma')
        alpha_stall_el = el.find('alpha_stall')
        cla_stall_el = el.find('cla_stall')
        cda_stall_el = el.find('cda_stall')
        cma_stall_el = el.find('cma_stall')
        air_density_el = el.find('air_density')
        radial_symmetry_el = el.find('radial_symmetry')
        reversible_el = el.find('reversible')
        area_el = el.find('area')
        a0_el = el.find('a0')
        cp_el = el.find('cp')
        cm_delta_el = el.find('cm_delta')
        forward_el = el.find('forward')
        upward_el = el.find('upward')
        control_joint_rad_to_cl_el = el.find('control_joint_rad_to_cl')
        control_joint_name_el = el.find('control_joint_name')

        def _parse_tuple(el_node):
            if el_node is None or not el_node.text: return None
            parts = el_node.text.split()
            if len(parts) == 3:
                return (float(parts[0]), float(parts[1]), float(parts[2]))
            return None

        return cls(
            link_name=link_name_el.text if link_name_el is not None and link_name_el.text is not None else None,
            cla=float(cla_el.text) if cla_el is not None and cla_el.text is not None else None,
            cda=float(cda_el.text) if cda_el is not None and cda_el.text is not None else None,
            cma=float(cma_el.text) if cma_el is not None and cma_el.text is not None else None,
            alpha_stall=float(alpha_stall_el.text) if alpha_stall_el is not None and alpha_stall_el.text is not None else None,
            cla_stall=float(cla_stall_el.text) if cla_stall_el is not None and cla_stall_el.text is not None else None,
            cda_stall=float(cda_stall_el.text) if cda_stall_el is not None and cda_stall_el.text is not None else None,
            cma_stall=float(cma_stall_el.text) if cma_stall_el is not None and cma_stall_el.text is not None else None,
            air_density=float(air_density_el.text) if air_density_el is not None and air_density_el.text is not None else None,
            radial_symmetry=radial_symmetry_el.text.lower() in ("true", "1", "yes", "t") if radial_symmetry_el is not None and radial_symmetry_el.text is not None else None,
            reversible=reversible_el.text.lower() in ("true", "1", "yes", "t") if reversible_el is not None and reversible_el.text is not None else None,
            area=float(area_el.text) if area_el is not None and area_el.text is not None else None,
            a0=float(a0_el.text) if a0_el is not None and a0_el.text is not None else None,
            cp=_parse_tuple(cp_el),
            cm_delta=float(cm_delta_el.text) if cm_delta_el is not None and cm_delta_el.text is not None else None,
            forward=_parse_tuple(forward_el),
            upward=_parse_tuple(upward_el),
            control_joint_rad_to_cl=float(control_joint_rad_to_cl_el.text) if control_joint_rad_to_cl_el is not None and control_joint_rad_to_cl_el.text is not None else None,
            control_joint_name=control_joint_name_el.text if control_joint_name_el is not None and control_joint_name_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::LiftDrag", filename="gz-sim-lift-drag-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                elif isinstance(v, tuple):
                    child.text = " ".join(map(str, v))
                else:
                    child.text = str(v)
                el.append(child)
                
        _add('link_name', self.link_name)
        _add('cla', self.cla)
        _add('cda', self.cda)
        _add('cma', self.cma)
        _add('alpha_stall', self.alpha_stall)
        _add('cla_stall', self.cla_stall)
        _add('cda_stall', self.cda_stall)
        _add('cma_stall', self.cma_stall)
        _add('air_density', self.air_density)
        _add('radial_symmetry', self.radial_symmetry)
        _add('reversible', self.reversible)
        _add('area', self.area)
        _add('a0', self.a0)
        _add('cp', self.cp)
        _add('cm_delta', self.cm_delta)
        _add('forward', self.forward)
        _add('upward', self.upward)
        _add('control_joint_rad_to_cl', self.control_joint_rad_to_cl)
        _add('control_joint_name', self.control_joint_name)
            
        return el

    def to_version(self, target_version: str):
        return self
