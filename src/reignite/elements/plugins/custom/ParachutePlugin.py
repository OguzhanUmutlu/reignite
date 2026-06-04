from ...plugin import Plugin


@Plugin.register("ParachutePlugin", "ParachutePlugin")
class ParachutePlugin(Plugin):
    def __init__(
            self,
            parent_link: str | None = None,
            child_model: str | None = None,
            child_link: str | None = None,
            child_pose: list[float] | str | dict | None = None,
            cmd_topic: str | list[str] | None = None,
            **kwargs
    ):
        super().__init__(
            filename="ParachutePlugin",
            name="ParachutePlugin",
            parent_link=parent_link,
            child_model=child_model,
            child_link=child_link,
            child_pose=child_pose,
            cmd_topic=cmd_topic,
            **kwargs
        )
