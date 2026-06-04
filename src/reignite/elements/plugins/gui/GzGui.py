from xml.etree import ElementTree as ET

from ....utils.errors import SDFError
from ....utils.model import BaseModel


class GzGui(BaseModel):
    class Anchor:
        def __init__(self, own: str, target: str):
            self.own = own
            self.target = target

    def __init__(self, title: str | None = None, delete_later: bool | None = None,
                 show_title_bar: bool | None = None, resizable: bool | None = None, width: float | None = None,
                 height: float | None = None, z: float | None = None, state: str | None = None,
                 anchor: str | None = None, anchors: list[Anchor | None] = None):
        super().__init__()
        self.title = title
        self.delete_later = delete_later
        self.show_title_bar = show_title_bar
        self.resizable = resizable
        self.width = width
        self.height = height
        self.z = z
        self.state = state  # docked or floating
        self.anchor = anchor
        self.anchors = anchors

    def to_version(self, target_version: str) -> "GzGui":
        return self

    def to_sdf(self, _=None) -> ET.Element:
        el = ET.Element("gz-gui")
        if self.title is not None:
            title_el = ET.Element("title")
            title_el.text = self.title
            el.append(title_el)
        if self.show_title_bar is not None:
            prop_el = ET.Element("property", key="showTitleBar", type="bool")
            prop_el.text = str(self.show_title_bar).lower()
            el.append(prop_el)
        if self.resizable is not None:
            prop_el = ET.Element("property", key="resizable", type="bool")
            prop_el.text = str(self.resizable).lower()
            el.append(prop_el)
        if self.width is not None:
            prop_el = ET.Element("property", key="width", type="double")
            prop_el.text = str(self.width)
            el.append(prop_el)
        if self.height is not None:
            prop_el = ET.Element("property", key="height", type="double")
            prop_el.text = str(self.height)
            el.append(prop_el)
        if self.z is not None:
            prop_el = ET.Element("property", key="z", type="double")
            prop_el.text = str(self.z)
            el.append(prop_el)
        if self.state is not None:
            prop_el = ET.Element("property", key="state", type="string")
            prop_el.text = self.state
            el.append(prop_el)
        if self.anchor is not None:
            anchors_el = ET.Element("anchors", target=self.anchor)
            for anchor in self.anchors or []:
                line_el = ET.Element("line")
                line_el.set("own", anchor.own)
                line_el.set("target", anchor.target)
                anchors_el.append(line_el)
            el.append(anchors_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "GzGui | SDFError":
        title = el.find("title")
        if title is not None:
            title = title.text
        show_title_bar = el.find("property[@key='showTitleBar']")
        if show_title_bar is not None:
            show_title_bar = show_title_bar.text == "true"
        resizable = el.find("property[@key='resizable']")
        if resizable is not None:
            resizable = resizable.text == "true"
        width = el.find("property[@key='width']")
        if width is not None:
            width = float(width.text)
        height = el.find("property[@key='height']")
        if height is not None:
            height = float(height.text)
        z = el.find("property[@key='z']")
        if z is not None:
            z = float(z.text)
        state = el.find("property[@key='state']")
        if state is not None:
            state = state.text
        _anchors = el.find("anchors")
        anchor = None
        anchors = None
        if _anchors is not None:
            anchor = _anchors.get("target")
            anchors = []
            for line in _anchors.findall("line"):
                own = line.find("own")
                target = line.find("target")
                if own is not None and target is not None:
                    anchors.append(cls.Anchor(own.text, target.text))
        return cls(title=title, show_title_bar=show_title_bar, resizable=resizable, width=width, height=height, z=z,
                   state=state, anchor=anchor, anchors=anchors)
