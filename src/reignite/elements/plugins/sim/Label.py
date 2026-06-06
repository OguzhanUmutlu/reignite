from xml.etree import ElementTree as ET

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

        self.label = label
        super().__init__(sdf_version=None, filename="gz-sim-label-system", name="gz::sim::systems::Label")

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        label_el = el.find('label')

        return cls(
            label=int(label_el.text) if label_el is not None and label_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Label",
                        filename="gz-sim-label-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('label', self.label)

        return el

    def to_version(self, target_version: str):
        return self

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        label_el = el.find('label')

        return cls(
            label=int(label_el.text) if label_el is not None and label_el.text is not None else None,
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name=self.name if hasattr(self, 'name') else "gz::sim::systems::Label",
                        filename="gz-sim-label-system")

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add('label', self.label)

        return el

    def to_version(self, target_version: str):
        return self
