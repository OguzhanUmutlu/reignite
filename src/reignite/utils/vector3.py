class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def to_sdf(self):
        return f"{self.x} {self.y} {self.z}"

    @staticmethod
    def from_sdf(text: str):
        try:
            x, y, z = (float(x) for x in text.split(" "))
        except:
            raise Exception(f"Invalid vector3: {text}")
        return Vector3(x, y, z)
