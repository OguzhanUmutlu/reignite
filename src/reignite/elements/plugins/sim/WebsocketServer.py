from xml.etree import ElementTree as ET
from reignite.elements.plugin import Plugin
from reignite.utils.model import BaseModel


@Plugin.register("gz-sim-websocket-server-system", "gz::sim::systems::WebsocketServer")
class WebsocketServerPlugin(Plugin):
    class Subscription(BaseModel):
        def __init__(self, msg_type: str | None = None, limit: int | None = None):
            super().__init__(sdf_version=None)
            self.msg_type = msg_type
            self.limit = limit

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            mt_el = el.find("msg_type")
            l_el = el.find("limit")
            return cls(
                msg_type=mt_el.text if mt_el is not None else None,
                limit=int(l_el.text) if l_el is not None and l_el.text is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("subscription")
            if self.msg_type is not None:
                child = ET.Element("msg_type")
                child.text = str(self.msg_type)
                e.append(child)
            if self.limit is not None:
                child = ET.Element("limit")
                child.text = str(self.limit)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

    class SubscriptionLimitPerConnection(BaseModel):
        def __init__(self, subscriptions: list["WebsocketServerPlugin.Subscription"] | None = None):
            super().__init__(sdf_version=None)
            self.subscriptions = subscriptions or []

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            s_els = el.findall("subscription")
            return cls(
                subscriptions=[WebsocketServerPlugin.Subscription._from_sdf(s, version) for s in s_els] if s_els else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("subscription_limit_per_connection")
            if self.subscriptions:
                for s in self.subscriptions:
                    e.append(s.to_sdf(version))
            return e

        def to_version(self, target_version: str):
            for s in self.subscriptions:
                s.to_version(target_version)
            return self

    class Ssl(BaseModel):
        def __init__(self, cert_file: str | None = None, private_key_file: str | None = None):
            super().__init__(sdf_version=None)
            self.cert_file = cert_file
            self.private_key_file = private_key_file

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str):
            cf_el = el.find("cert_file")
            pkf_el = el.find("private_key_file")
            return cls(
                cert_file=cf_el.text if cf_el is not None else None,
                private_key_file=pkf_el.text if pkf_el is not None else None
            )

        def to_sdf(self, version: str | None = None) -> ET.Element:
            e = ET.Element("ssl")
            if self.cert_file is not None:
                child = ET.Element("cert_file")
                child.text = str(self.cert_file)
                e.append(child)
            if self.private_key_file is not None:
                child = ET.Element("private_key_file")
                child.text = str(self.private_key_file)
                e.append(child)
            return e

        def to_version(self, target_version: str):
            return self

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
        self.publication_hz = publication_hz
        self.authorization_key = authorization_key
        self.admin_authorization_key = admin_authorization_key
        self.port = port
        self.max_connections = max_connections
        self.queue_size_per_connection = queue_size_per_connection
        self.subscription_limit_per_connection = subscription_limit_per_connection
        self.ssl = ssl

        super().__init__(
            sdf_version=None,
            filename="gz-sim-websocket-server-system",
            name="gz::sim::systems::WebsocketServer"
        )

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        phz_el = el.find("publication_hz")
        ak_el = el.find("authorization_key")
        aak_el = el.find("admin_authorization_key")
        p_el = el.find("port")
        mc_el = el.find("max_connections")
        qspc_el = el.find("queue_size_per_connection")
        slpc_el = el.find("subscription_limit_per_connection")
        s_el = el.find("ssl")

        return cls(
            publication_hz=float(phz_el.text) if phz_el is not None and phz_el.text is not None else None,
            authorization_key=ak_el.text if ak_el is not None else None,
            admin_authorization_key=aak_el.text if aak_el is not None else None,
            port=int(p_el.text) if p_el is not None and p_el.text is not None else None,
            max_connections=int(mc_el.text) if mc_el is not None and mc_el.text is not None else None,
            queue_size_per_connection=int(qspc_el.text) if qspc_el is not None and qspc_el.text is not None else None,
            subscription_limit_per_connection=cls.SubscriptionLimitPerConnection._from_sdf(slpc_el, version) if slpc_el is not None else None,
            ssl=cls.Ssl._from_sdf(s_el, version) if s_el is not None else None
        )

    def to_sdf(self, version: str | None = None) -> ET.Element:
        el = ET.Element("plugin", name="gz::sim::systems::WebsocketServer", filename="gz-sim-websocket-server-system")
        if self.subscription_limit_per_connection is not None:
            el.append(self.subscription_limit_per_connection.to_sdf(version))
        if self.ssl is not None:
            el.append(self.ssl.to_sdf(version))
            
        def _add(k, v):
            if v is not None:
                child = ET.Element(k)
                child.text = str(v)
                el.append(child)
                
        _add("publication_hz", self.publication_hz)
        _add("authorization_key", self.authorization_key)
        _add("admin_authorization_key", self.admin_authorization_key)
        _add("port", self.port)
        _add("max_connections", self.max_connections)
        _add("queue_size_per_connection", self.queue_size_per_connection)
        
        return el

    def to_version(self, target_version: str):
        if self.subscription_limit_per_connection is not None:
            self.subscription_limit_per_connection.to_version(target_version)
        if self.ssl is not None:
            self.ssl.to_version(target_version)
        return self
