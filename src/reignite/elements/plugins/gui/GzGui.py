from typing import Optional
from xml.etree import ElementTree as ET

from ....utils.errors import SDFError
from ....utils.model import BaseModel


class GzGui(BaseModel):
    class Anchor:
        def __init__(self, own: str, target: str):
            self.own = own
            self.target = target

    def __init__(self, title: Optional[str] = None, delete_later: Optional[bool] = None,
                 show_title_bar: Optional[bool] = None, resizable: Optional[bool] = None, width: Optional[float] = None,
                 height: Optional[float] = None, z: Optional[float] = None, state: Optional[str] = None,
                 anchor: Optional[str] = None, anchors: Optional[list[Anchor]] = None):
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
            el.append(ET.Element("title", text=self.title))
        if self.show_title_bar is not None:
            el.append(ET.Element("property", text=str(self.show_title_bar).lower(), key="showTitleBar", type="bool"))
        if self.resizable is not None:
            el.append(ET.Element("property", text=str(self.resizable).lower(), key="resizable", type="bool"))
        if self.width is not None:
            el.append(ET.Element("property", text=str(self.width), key="width", type="double"))
        if self.height is not None:
            el.append(ET.Element("property", text=str(self.height), key="height", type="double"))
        if self.z is not None:
            el.append(ET.Element("property", text=str(self.z), key="z", type="double"))
        if self.state is not None:
            el.append(ET.Element("property", text=self.state, key="state", type="string"))
        if self.anchor is not None:
            anchors_el = ET.Element("anchors", target=self.anchor)
            for anchor in self.anchors or []:
                line_el = ET.Element("line")
                line_el.append(ET.Element("own", text=anchor.own))
                line_el.append(ET.Element("target", text=anchor.target))
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
                    anchors.append((own.text, target.text))
        return cls(title=title, show_title_bar=show_title_bar, resizable=resizable, width=width, height=height, z=z,
                   state=state, anchor=anchor, anchors=anchors)
