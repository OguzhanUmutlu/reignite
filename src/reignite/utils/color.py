class Color:
    def __init__(self, r: int, g: int, b: int, a: int):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def to_sdf(self):
        return f"{self.r / 255} {self.g / 255} {self.b / 255} {self.a / 255}"

    @staticmethod
    def from_sdf(text: str):
        try:
            r, g, b, a = (int(float(x) * 255) for x in text.split())
        except:
            raise Exception(f"Invalid color: {text}")
        return Color(r, g, b, a)
