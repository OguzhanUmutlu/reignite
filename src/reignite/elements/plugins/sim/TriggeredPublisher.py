from reignite.elements.plugin import Plugin, ParentElement, TextElement

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


class TriggeredPublisher(Plugin):
    class Match(TextElement):
        def __init__(self, value: str, field: str | None = None, tol: float | None = None,
                     inverted: bool = False):
            attrs = {"logic_type": "negative" if inverted else "positive"}
            if field: attrs["field"] = field
            if tol: attrs["tol"] = str(tol)
            super().__init__("match", value, **attrs)

    class Input(ParentElement):
        def __init__(self, type: str, topic: str, matches: list["TriggeredPublisher.Match"] | None = None):
            super().__init__("input", matches or [], type=type, topic=topic)

    class Output(TextElement):
        def __init__(self, type: str, topic: str, msg_content: str):
            msg_type = _messages.get(type.lower(), type)
            super().__init__("output", msg_content, type=msg_type, topic=topic)

    class Service(TextElement):
        def __init__(self, name: str, reqType: str, repType: str, reqMsg: str, timeout: int):
            super().__init__("service", "", name=name, reqType=reqType,
                             repType=repType, reqMsg=reqMsg, timeout=str(timeout))

    def __init__(
            self,
            input: Input,
            outputs: list[Output] | None = None,
            services: list[Service] | None = None,
            delay_ms: int | None = None
    ):
        elements = [input, *(outputs or []), *(services or [])]

        if delay_ms is not None:
            elements.append(TextElement("delay_ms", str(delay_ms)))

        super().__init__(
            filename="gz-sim-triggered-publisher-system",
            name="gz::sim::systems::TriggeredPublisher",
            elements=elements
        )
