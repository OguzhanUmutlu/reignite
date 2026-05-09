class SDFError:
    def __init__(self, message: str, path: str = ""):
        self.message = message
        self.path = path

    def extend(self, part: str) -> "SDFError":
        new_path = f"{part}/{self.path}" if self.path else part
        return SDFError(self.message, new_path)

    def __str__(self):
        if self.path:
            return f"Error at {self.path}: {self.message}"
        return self.message
