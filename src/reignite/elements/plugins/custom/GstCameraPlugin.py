from xml.etree import ElementTree as ET

from ...plugin import Plugin


@Plugin.register("GstCameraPlugin", "GstCameraPlugin")
class GstCameraPlugin(Plugin):
    def __init__(
            self,
            udp_host: str | None = None,
            udp_port: int | None = None,
            rtmp_location: str | None = None,
            use_basic_pipeline: bool | None = None,
            use_cuda: bool | None = None,
            image_topic: str | None = None,
            enable_topic: str | None = None,
            **kwargs
    ):
        self.udp_host = udp_host
        self.udp_port = udp_port
        self.rtmp_location = rtmp_location
        self.use_basic_pipeline = use_basic_pipeline
        self.use_cuda = use_cuda
        self.image_topic = image_topic
        self.enable_topic = enable_topic
        super().__init__(
            sdf_version=None,
            filename="GstCameraPlugin",
            name="GstCameraPlugin",
            **kwargs
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        udp_host_el = el.find("udp_host")
        udp_port_el = el.find("udp_port")
        rtmp_location_el = el.find("rtmp_location")
        use_basic_pipeline_el = el.find("use_basic_pipeline")
        use_cuda_el = el.find("use_cuda")
        image_topic_el = el.find("image_topic")
        enable_topic_el = el.find("enable_topic")

        return cls(
            udp_host=udp_host_el.text if udp_host_el is not None and udp_host_el.text is not None else None,
            udp_port=int(udp_port_el.text) if udp_port_el is not None and udp_port_el.text is not None else None,
            rtmp_location=rtmp_location_el.text if rtmp_location_el is not None and rtmp_location_el.text is not None else None,
            use_basic_pipeline=use_basic_pipeline_el.text.lower() == "true" if use_basic_pipeline_el is not None and use_basic_pipeline_el.text is not None else None,
            use_cuda=use_cuda_el.text.lower() == "true" if use_cuda_el is not None and use_cuda_el.text is not None else None,
            image_topic=image_topic_el.text if image_topic_el is not None and image_topic_el.text is not None else None,
            enable_topic=enable_topic_el.text if enable_topic_el is not None and enable_topic_el.text is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = super().to_sdf(version)

        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                if isinstance(v, bool):
                    child.text = "true" if v else "false"
                else:
                    child.text = str(v)
                el.append(child)

        _add("udp_host", self.udp_host)
        _add("udp_port", self.udp_port)
        _add("rtmp_location", self.rtmp_location)
        _add("use_basic_pipeline", self.use_basic_pipeline)
        _add("use_cuda", self.use_cuda)
        _add("image_topic", self.image_topic)
        _add("enable_topic", self.enable_topic)

        return el

    def to_version(self, target_version: str):
        return self
