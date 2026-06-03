from reignite.elements.plugin import Plugin, ParentElement, TextElement


class WebsocketServerPlugin(Plugin):
    class Subscription(ParentElement):
        def __init__(self, msg_type: str, limit: int):
            super().__init__(
                "subscription",
                TextElement("msg_type", msg_type),
                TextElement("limit", str(limit))
            )

    class SubscriptionLimitPerConnection(ParentElement):
        def __init__(self, subscriptions: list["WebsocketServerPlugin.Subscription"]):
            super().__init__("subscription_limit_per_connection", *subscriptions)

    class Ssl(ParentElement):
        def __init__(self, cert_file: str, private_key_file: str):
            super().__init__(
                "ssl",
                TextElement("cert_file", cert_file),
                TextElement("private_key_file", private_key_file)
            )

    def __init__(
            self,
            publication_hz: float | None = None,
            authorization_key: str | None = None,
            admin_authorization_key: str | None = None,
            port: int | None = None,
            max_connections: int | None = None,
            queue_size_per_connection: int | None = None,
            subscription_limit_per_connection: SubscriptionLimitPerConnection | None = None,
            ssl: Ssl | None = None,
    ):
        super().__init__(
            sdf_version=None,
            filename="gz-sim-websocket-server-system",
            name="gz::sim::systems::WebsocketServer",
            publication_hz=publication_hz,
            authorization_key=authorization_key,
            admin_authorization_key=admin_authorization_key,
            port=port,
            max_connections=max_connections,
            queue_size_per_connection=queue_size_per_connection,
            subscription_limit_per_connection=subscription_limit_per_connection,
            ssl=ssl,
        )
