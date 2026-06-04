from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-acoustic-comms-system", "gz::sim::systems::AcousticComms")
class AcousticCommsPlugin(Plugin):
    class PropagationModel(BaseModel):
        def __init__(
                self,
                source_power: float | None = None,
                noise_level: float | None = None,
                spectral_efficiency: float | None = None,
                seed: int | None = None
        ):
            super().__init__(sdf_version=None)
            self.source_power = source_power
            self.noise_level = noise_level
            self.spectral_efficiency = spectral_efficiency
            self.seed = seed

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            sp_el = el.find("source_power")
            nl_el = el.find("noise_level")
            se_el = el.find("spectral_efficiency")
            sd_el = el.find("seed")
            
            return cls(
                source_power=float(sp_el.text) if sp_el is not None and sp_el.text is not None else None,
                noise_level=float(nl_el.text) if nl_el is not None and nl_el.text is not None else None,
                spectral_efficiency=float(se_el.text) if se_el is not None and se_el.text is not None else None,
                seed=int(sd_el.text) if sd_el is not None and sd_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("propagation_model")
            
            def _add(k, v):
                if v is not None:
                    child = ET.Element(k)
                    child.text = str(v)
                    e.append(child)
                    
            _add("source_power", self.source_power)
            _add("noise_level", self.noise_level)
            _add("spectral_efficiency", self.spectral_efficiency)
            _add("seed", self.seed)
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            max_range: float = 1000.0,
            speed_of_sound: float = 343.0,
            collision_time_per_byte: float = 0.0,
            propagation_model: PropagationModel | None = None
    ):
        self.max_range = max_range
        self.speed_of_sound = speed_of_sound
        self.collision_time_per_byte = collision_time_per_byte
        self.propagation_model = propagation_model

        super().__init__(
            sdf_version=None,
            filename="gz-sim-acoustic-comms-system",
            name="gz::sim::systems::AcousticComms"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        mr_el = el.find("max_range")
        ss_el = el.find("speed_of_sound")
        ct_el = el.find("collision_time_per_byte")
        pm_el = el.find("propagation_model")
        
        return cls(
            max_range=float(mr_el.text) if mr_el is not None and mr_el.text is not None else 1000.0,
            speed_of_sound=float(ss_el.text) if ss_el is not None and ss_el.text is not None else 343.0,
            collision_time_per_byte=float(ct_el.text) if ct_el is not None and ct_el.text is not None else 0.0,
            propagation_model=cls.PropagationModel._from_sdf(pm_el, version) if pm_el is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::AcousticComms", filename="gz-sim-acoustic-comms-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                child.text = str(v)
                el.append(child)
                
        _add("max_range", self.max_range)
        _add("speed_of_sound", self.speed_of_sound)
        _add("collision_time_per_byte", self.collision_time_per_byte)
        
        if self.propagation_model is not None:
            el.append(self.propagation_model.to_sdf(version))
            
        return el

    def to_version(self, target_version: str):
        if self.propagation_model is not None:
            self.propagation_model = self.propagation_model.to_version(target_version)
        return self
