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
        super().__init__(
            filename="GstCameraPlugin",
            name="GstCameraPlugin",
            udp_host=udp_host,
            udp_port=udp_port,
            rtmp_location=rtmp_location,
            use_basic_pipeline=use_basic_pipeline,
            use_cuda=use_cuda,
            image_topic=image_topic,
            enable_topic=enable_topic,
            **kwargs
        )
