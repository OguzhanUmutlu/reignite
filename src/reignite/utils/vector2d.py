class Vector2d:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def to_sdf(self):
        return f"{self.x} {self.y}"

    @staticmethod
    def from_sdf(text: str):
        try:
            x, y = (float(x) for x in text.split(" "))
        except:
            raise Exception(f"Invalid vector2d: {text}")
        return Vector2d(x, y)
