from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel

_messages = {
    "bool": "gz.msgs.Boolean", "boolean": "gz.msgs.Boolean",
    "string": "gz.msgs.StringMsg", "str": "gz.msgs.StringMsg",
    "i32": "gz.msgs.Int32", "int32": "gz.msgs.Int32",
    "u32": "gz.msgs.UInt32", "uint32": "gz.msgs.UInt32",
    "i64": "gz.msgs.Int64", "int64": "gz.msgs.Int64",
    "u64": "gz.msgs.UInt64", "uint64": "gz.msgs.UInt64",
    "float": "gz.msgs.Float", "double": "gz.msgs.Double",

    "color": "gz.msgs.Color",
    "axisalignedbox": "gz.msgs.AxisAlignedBox", "aab": "gz.msgs.AxisAlignedBox",
    "sphericalcoordinates": "gz.msgs.SphericalCoordinates", "location": "gz.msgs.SphericalCoordinates",
    "inertial": "gz.msgs.Inertial",
    "pose": "gz.msgs.Pose",
    "plane": "gz.msgs.PlaneGeom",
    "quaternion": "gz.msgs.Quaternion",
    "vector2": "gz.msgs.Vector2d",
    "vector3": "gz.msgs.Vector3d",
}


@Plugin.register("gz-sim-triggered-publisher-system", "gz::sim::systems::TriggeredPublisher")
class TriggeredPublisherPlugin(Plugin):
    class Match(BaseModel):
        def __init__(self, value: str | None = None, field: str | None = None, tol: float | None = None,
                     inverted: bool = False):
            super().__init__(sdf_version=None)
            self.value = value
            self.field = field
            self.tol = tol
            self.inverted = inverted

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            f_attr = el.get("field")
            t_attr = el.get("tol")
            lt_attr = el.get("logic_type")
            return cls(
                value=el.text,
                field=f_attr,
                tol=float(t_attr) if t_attr is not None else None,
                inverted=(lt_attr == "negative")
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("match")
            e.set("logic_type", "negative" if self.inverted else "positive")
            if self.field is not None:
                e.set("field", str(self.field))
            if self.tol is not None:
                e.set("tol", str(self.tol))
            if self.value is not None:
                e.text = str(self.value)
            return e

        def to_version(self, target_version: str):
            return self

    class Input(BaseModel):
        def __init__(self, type: str | None = None, topic: str | None = None, matches: list["TriggeredPublisherPlugin.Match"] | None = None):
            super().__init__(sdf_version=None)
            self.type = type
            self.topic = topic
            self.matches = matches or []

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            t_attr = el.get("type")
            top_attr = el.get("topic")
            m_els = el.findall("match")
            return cls(
                type=t_attr,
                topic=top_attr,
                matches=[TriggeredPublisherPlugin.Match._from_sdf(m, version) for m in m_els] if m_els else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("input")
            if self.type is not None:
                e.set("type", str(self.type))
            if self.topic is not None:
                e.set("topic", str(self.topic))
            for m in self.matches:
                e.append(m.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            for m in self.matches:
                m.to_version(target_version)
            return self

    class Output(BaseModel):
        def __init__(self, type: str | None = None, topic: str | None = None, msg_content: str = ""):
            super().__init__(sdf_version=None)
            self.type = type
            self.topic = topic
            self.msg_content = msg_content

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            t_attr = el.get("type")
            top_attr = el.get("topic")
            return cls(
                type=t_attr,
                topic=top_attr,
                msg_content=el.text or ""
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("output")
            if self.type is not None:
                msg_type = _messages.get(self.type.lower(), self.type)
                e.set("type", msg_type)
            if self.topic is not None:
                e.set("topic", str(self.topic))
            if self.msg_content:
                e.text = str(self.msg_content)
            return e

        def to_version(self, target_version: str):
            return self

    class Service(BaseModel):
        def __init__(self, name: str | None = None, reqType: str | None = None, repType: str | None = None, reqMsg: str | None = None, timeout: int | None = None):
            super().__init__(sdf_version=None)
            self.name = name
            self.reqType = reqType
            self.repType = repType
            self.reqMsg = reqMsg
            self.timeout = timeout

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            n_attr = el.get("name")
            reqt_attr = el.get("reqType")
            rept_attr = el.get("repType")
            reqm_attr = el.get("reqMsg")
            to_attr = el.get("timeout")
            return cls(
                name=n_attr,
                reqType=reqt_attr,
                repType=rept_attr,
                reqMsg=reqm_attr,
                timeout=int(to_attr) if to_attr is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("service")
            if self.name is not None:
                e.set("name", str(self.name))
            if self.reqType is not None:
                e.set("reqType", str(self.reqType))
            if self.repType is not None:
                e.set("repType", str(self.repType))
            if self.reqMsg is not None:
                e.set("reqMsg", str(self.reqMsg))
            if self.timeout is not None:
                e.set("timeout", str(self.timeout))
            return e

        def to_version(self, target_version: str):
            return self

    def __init__(
            self,
            input: Input | None = None,
            outputs: list[Output] | None = None,
            services: list[Service] | None = None,
            delay_ms: int | None = None
    ):
        self.input = input
        self.outputs = outputs or []
        self.services = services or []
        self.delay_ms = delay_ms

        super().__init__(
            sdf_version=None,
            filename="gz-sim-triggered-publisher-system",
            name="gz::sim::systems::TriggeredPublisher"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        i_el = el.find("input")
        o_els = el.findall("output")
        s_els = el.findall("service")
        dms_el = el.find("delay_ms")

        return cls(
            input=cls.Input._from_sdf(i_el, version) if i_el is not None else None,
            outputs=[cls.Output._from_sdf(o, version) for o in o_els] if o_els else None,
            services=[cls.Service._from_sdf(s, version) for s in s_els] if s_els else None,
            delay_ms=int(dms_el.text) if dms_el is not None and dms_el.text is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::TriggeredPublisher", filename="gz-sim-triggered-publisher-system")
        if self.input is not None:
            el.append(self.input.to_sdf(version))
        for o in self.outputs:
            el.append(o.to_sdf(version))
        for s in self.services:
            el.append(s.to_sdf(version))
        if self.delay_ms is not None:
            child = ET.Element("delay_ms")
            child.text = str(self.delay_ms)
            el.append(child)
        return el

    def to_version(self, target_version: str):
        if self.input is not None:
            self.input.to_version(target_version)
        for o in self.outputs:
            o.to_version(target_version)
        for s in self.services:
            s.to_version(target_version)
        return self
