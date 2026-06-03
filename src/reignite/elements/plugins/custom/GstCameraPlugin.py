from typing import Optional
from ...plugin import Plugin

class GstCameraPlugin(Plugin):
    def __init__(
            self,
            udp_host: Optional[str] = None,
            udp_port: Optional[int] = None,
            rtmp_location: Optional[str] = None,
            use_basic_pipeline: Optional[bool] = None,
            use_cuda: Optional[bool] = None,
            image_topic: Optional[str] = None,
            enable_topic: Optional[str] = None,
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
