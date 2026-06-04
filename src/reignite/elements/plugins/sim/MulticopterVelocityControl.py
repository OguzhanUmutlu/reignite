from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin


@Plugin.register("gz-sim-multicopter-control-system", "gz::sim::systems::MulticopterVelocityControl")
class MulticopterVelocityControlPlugin(Plugin):
    def __init__(
            self,
            angularRateGain: list[float] | str | None = None,
            maximumLinearAcceleration: list[float] | str | None = None,
            maximumLinearVelocity: list[float] | str | None = None,
            maximumAngularVelocity: list[float] | str | None = None,
            linearVelocityNoiseMean: list[float] | str | None = None,
            linearVelocityNoiseStdDev: list[float] | str | None = None,
            angularVelocityNoiseMean: list[float] | str | None = None,
            angularVelocityNoiseStdDev: list[float] | str | None = None,
            robotNamespace: str | None = None,
            commandSubTopic: str | None = None,
            enableSubTopic: str | None = None,
    ):
        self.angularRateGain = angularRateGain
        self.maximumLinearAcceleration = maximumLinearAcceleration
        self.maximumLinearVelocity = maximumLinearVelocity
        self.maximumAngularVelocity = maximumAngularVelocity
        self.linearVelocityNoiseMean = linearVelocityNoiseMean
        self.linearVelocityNoiseStdDev = linearVelocityNoiseStdDev
        self.angularVelocityNoiseMean = angularVelocityNoiseMean
        self.angularVelocityNoiseStdDev = angularVelocityNoiseStdDev
        
        for k in ["angularRateGain", "maximumLinearAcceleration", "maximumLinearVelocity", "maximumAngularVelocity", "linearVelocityNoiseMean", "linearVelocityNoiseStdDev", "angularVelocityNoiseMean", "angularVelocityNoiseStdDev"]:
            val = getattr(self, k)
            if isinstance(val, list):
                setattr(self, k, " ".join(map(str, val)))

        self.robotNamespace = robotNamespace
        self.commandSubTopic = commandSubTopic
        self.enableSubTopic = enableSubTopic
        super().__init__(sdf_version=None, filename="gz-sim-multicopter-control-system", name="gz::sim::systems::MulticopterVelocityControl")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        angularRateGain_els = el.findall('angularRateGain')
        angularRateGain_vals = [e.text for e in angularRateGain_els if e.text is not None] if angularRateGain_els else None
        maximumLinearAcceleration_els = el.findall('maximumLinearAcceleration')
        maximumLinearAcceleration_vals = [e.text for e in maximumLinearAcceleration_els if e.text is not None] if maximumLinearAcceleration_els else None
        maximumLinearVelocity_els = el.findall('maximumLinearVelocity')
        maximumLinearVelocity_vals = [e.text for e in maximumLinearVelocity_els if e.text is not None] if maximumLinearVelocity_els else None
        maximumAngularVelocity_els = el.findall('maximumAngularVelocity')
        maximumAngularVelocity_vals = [e.text for e in maximumAngularVelocity_els if e.text is not None] if maximumAngularVelocity_els else None
        linearVelocityNoiseMean_els = el.findall('linearVelocityNoiseMean')
        linearVelocityNoiseMean_vals = [e.text for e in linearVelocityNoiseMean_els if e.text is not None] if linearVelocityNoiseMean_els else None
        linearVelocityNoiseStdDev_els = el.findall('linearVelocityNoiseStdDev')
        linearVelocityNoiseStdDev_vals = [e.text for e in linearVelocityNoiseStdDev_els if e.text is not None] if linearVelocityNoiseStdDev_els else None
        angularVelocityNoiseMean_els = el.findall('angularVelocityNoiseMean')
        angularVelocityNoiseMean_vals = [e.text for e in angularVelocityNoiseMean_els if e.text is not None] if angularVelocityNoiseMean_els else None
        angularVelocityNoiseStdDev_els = el.findall('angularVelocityNoiseStdDev')
        angularVelocityNoiseStdDev_vals = [e.text for e in angularVelocityNoiseStdDev_els if e.text is not None] if angularVelocityNoiseStdDev_els else None
        robotNamespace_el = el.find('robotNamespace')
        commandSubTopic_el = el.find('commandSubTopic')
        enableSubTopic_el = el.find('enableSubTopic')

        return cls(
            angularRateGain=angularRateGain_vals,
            maximumLinearAcceleration=maximumLinearAcceleration_vals,
            maximumLinearVelocity=maximumLinearVelocity_vals,
            maximumAngularVelocity=maximumAngularVelocity_vals,
            linearVelocityNoiseMean=linearVelocityNoiseMean_vals,
            linearVelocityNoiseStdDev=linearVelocityNoiseStdDev_vals,
            angularVelocityNoiseMean=angularVelocityNoiseMean_vals,
            angularVelocityNoiseStdDev=angularVelocityNoiseStdDev_vals,
            robotNamespace=robotNamespace_el.text if robotNamespace_el is not None and robotNamespace_el.text is not None else None,
            commandSubTopic=commandSubTopic_el.text if commandSubTopic_el is not None and commandSubTopic_el.text is not None else None,
            enableSubTopic=enableSubTopic_el.text if enableSubTopic_el is not None and enableSubTopic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::MulticopterVelocityControl", filename="gz-sim-multicopter-control-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.angularRateGain is not None:
            for v in (self.angularRateGain if isinstance(self.angularRateGain, list) else [self.angularRateGain]):
                _add('angularRateGain', v)
        if self.maximumLinearAcceleration is not None:
            for v in (self.maximumLinearAcceleration if isinstance(self.maximumLinearAcceleration, list) else [self.maximumLinearAcceleration]):
                _add('maximumLinearAcceleration', v)
        if self.maximumLinearVelocity is not None:
            for v in (self.maximumLinearVelocity if isinstance(self.maximumLinearVelocity, list) else [self.maximumLinearVelocity]):
                _add('maximumLinearVelocity', v)
        if self.maximumAngularVelocity is not None:
            for v in (self.maximumAngularVelocity if isinstance(self.maximumAngularVelocity, list) else [self.maximumAngularVelocity]):
                _add('maximumAngularVelocity', v)
        if self.linearVelocityNoiseMean is not None:
            for v in (self.linearVelocityNoiseMean if isinstance(self.linearVelocityNoiseMean, list) else [self.linearVelocityNoiseMean]):
                _add('linearVelocityNoiseMean', v)
        if self.linearVelocityNoiseStdDev is not None:
            for v in (self.linearVelocityNoiseStdDev if isinstance(self.linearVelocityNoiseStdDev, list) else [self.linearVelocityNoiseStdDev]):
                _add('linearVelocityNoiseStdDev', v)
        if self.angularVelocityNoiseMean is not None:
            for v in (self.angularVelocityNoiseMean if isinstance(self.angularVelocityNoiseMean, list) else [self.angularVelocityNoiseMean]):
                _add('angularVelocityNoiseMean', v)
        if self.angularVelocityNoiseStdDev is not None:
            for v in (self.angularVelocityNoiseStdDev if isinstance(self.angularVelocityNoiseStdDev, list) else [self.angularVelocityNoiseStdDev]):
                _add('angularVelocityNoiseStdDev', v)
        _add('robotNamespace', self.robotNamespace)
        _add('commandSubTopic', self.commandSubTopic)
        _add('enableSubTopic', self.enableSubTopic)
            
        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        angularRateGain_els = el.findall('angularRateGain')
        angularRateGain_vals = [e.text for e in angularRateGain_els if e.text is not None] if angularRateGain_els else None
        maximumLinearAcceleration_els = el.findall('maximumLinearAcceleration')
        maximumLinearAcceleration_vals = [e.text for e in maximumLinearAcceleration_els if e.text is not None] if maximumLinearAcceleration_els else None
        maximumLinearVelocity_els = el.findall('maximumLinearVelocity')
        maximumLinearVelocity_vals = [e.text for e in maximumLinearVelocity_els if e.text is not None] if maximumLinearVelocity_els else None
        maximumAngularVelocity_els = el.findall('maximumAngularVelocity')
        maximumAngularVelocity_vals = [e.text for e in maximumAngularVelocity_els if e.text is not None] if maximumAngularVelocity_els else None
        linearVelocityNoiseMean_els = el.findall('linearVelocityNoiseMean')
        linearVelocityNoiseMean_vals = [e.text for e in linearVelocityNoiseMean_els if e.text is not None] if linearVelocityNoiseMean_els else None
        linearVelocityNoiseStdDev_els = el.findall('linearVelocityNoiseStdDev')
        linearVelocityNoiseStdDev_vals = [e.text for e in linearVelocityNoiseStdDev_els if e.text is not None] if linearVelocityNoiseStdDev_els else None
        angularVelocityNoiseMean_els = el.findall('angularVelocityNoiseMean')
        angularVelocityNoiseMean_vals = [e.text for e in angularVelocityNoiseMean_els if e.text is not None] if angularVelocityNoiseMean_els else None
        angularVelocityNoiseStdDev_els = el.findall('angularVelocityNoiseStdDev')
        angularVelocityNoiseStdDev_vals = [e.text for e in angularVelocityNoiseStdDev_els if e.text is not None] if angularVelocityNoiseStdDev_els else None
        robotNamespace_el = el.find('robotNamespace')
        commandSubTopic_el = el.find('commandSubTopic')
        enableSubTopic_el = el.find('enableSubTopic')

        return cls(
            angularRateGain=angularRateGain_vals,
            maximumLinearAcceleration=maximumLinearAcceleration_vals,
            maximumLinearVelocity=maximumLinearVelocity_vals,
            maximumAngularVelocity=maximumAngularVelocity_vals,
            linearVelocityNoiseMean=linearVelocityNoiseMean_vals,
            linearVelocityNoiseStdDev=linearVelocityNoiseStdDev_vals,
            angularVelocityNoiseMean=angularVelocityNoiseMean_vals,
            angularVelocityNoiseStdDev=angularVelocityNoiseStdDev_vals,
            robotNamespace=robotNamespace_el.text if robotNamespace_el is not None and robotNamespace_el.text is not None else None,
            commandSubTopic=commandSubTopic_el.text if commandSubTopic_el is not None and commandSubTopic_el.text is not None else None,
            enableSubTopic=enableSubTopic_el.text if enableSubTopic_el is not None and enableSubTopic_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::MulticopterVelocityControl", filename="gz-sim-multicopter-control-system")
        
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)
                
        if self.angularRateGain is not None:
            for v in (self.angularRateGain if isinstance(self.angularRateGain, list) else [self.angularRateGain]):
                _add('angularRateGain', v)
        if self.maximumLinearAcceleration is not None:
            for v in (self.maximumLinearAcceleration if isinstance(self.maximumLinearAcceleration, list) else [self.maximumLinearAcceleration]):
                _add('maximumLinearAcceleration', v)
        if self.maximumLinearVelocity is not None:
            for v in (self.maximumLinearVelocity if isinstance(self.maximumLinearVelocity, list) else [self.maximumLinearVelocity]):
                _add('maximumLinearVelocity', v)
        if self.maximumAngularVelocity is not None:
            for v in (self.maximumAngularVelocity if isinstance(self.maximumAngularVelocity, list) else [self.maximumAngularVelocity]):
                _add('maximumAngularVelocity', v)
        if self.linearVelocityNoiseMean is not None:
            for v in (self.linearVelocityNoiseMean if isinstance(self.linearVelocityNoiseMean, list) else [self.linearVelocityNoiseMean]):
                _add('linearVelocityNoiseMean', v)
        if self.linearVelocityNoiseStdDev is not None:
            for v in (self.linearVelocityNoiseStdDev if isinstance(self.linearVelocityNoiseStdDev, list) else [self.linearVelocityNoiseStdDev]):
                _add('linearVelocityNoiseStdDev', v)
        if self.angularVelocityNoiseMean is not None:
            for v in (self.angularVelocityNoiseMean if isinstance(self.angularVelocityNoiseMean, list) else [self.angularVelocityNoiseMean]):
                _add('angularVelocityNoiseMean', v)
        if self.angularVelocityNoiseStdDev is not None:
            for v in (self.angularVelocityNoiseStdDev if isinstance(self.angularVelocityNoiseStdDev, list) else [self.angularVelocityNoiseStdDev]):
                _add('angularVelocityNoiseStdDev', v)
        _add('robotNamespace', self.robotNamespace)
        _add('commandSubTopic', self.commandSubTopic)
        _add('enableSubTopic', self.enableSubTopic)
            
        return el

    def to_version(self, target_version: str):
        return self
