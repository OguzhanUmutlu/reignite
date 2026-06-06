from xml.etree import ElementTree as ET

from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-physics-system", "gz::sim::systems::Physics")
class PhysicsPlugin(Plugin):
    class Engine(BaseModel):
        def __init__(self, filename: str | None = None):
            super().__init__(sdf_version=None)
            self.filename = filename

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            f_el = el.find("filename")
            return cls(filename=f_el.text if f_el is not None else None)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("engine")
            if self.filename is not None:
                child = ET.Element("filename")
                child.text = str(self.filename)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            enforce_fixed_constraint: bool | None = None,
            include_entity_names: bool | None = None,
            engine: Engine | str | None = None,
    ):
        if isinstance(engine, str):
            engine = PhysicsPlugin.Engine(engine)

        self.enforce_fixed_constraint = enforce_fixed_constraint
        self.include_entity_names = include_entity_names
        self.engine = engine

        super().__init__(
            sdf_version=None,
            filename="gz-sim-physics-system",
            name="gz::sim::systems::Physics"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        efc_el = el.find("enforce_fixed_constraint")
        ien_el = el.find("include_entity_names")
        eng_el = el.find("engine")

        return cls(
            enforce_fixed_constraint=efc_el.text.lower() == 'true' if efc_el is not None and efc_el.text is not None else None,
            include_entity_names=ien_el.text.lower() == 'true' if ien_el is not None and ien_el.text is not None else None,
            engine=cls.Engine._from_sdf(eng_el, version) if eng_el is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::Physics", filename="gz-sim-physics-system")
        if self.engine is not None:
            el.append(self.engine.to_sdf(version))

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add("enforce_fixed_constraint", self.enforce_fixed_constraint)
        _add("include_entity_names", self.include_entity_names)
        return el

    def to_version(self, target_version: str):
        if self.engine is not None:
            self.engine.to_version(target_version)
        return self
