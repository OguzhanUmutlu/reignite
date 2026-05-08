class Pose:
    def __init__(self, x=0.0, y=0.0, z=0.0, roll=0.0, pitch=0.0, yaw=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def to_sdf(self):
        return f"{self.x} {self.y} {self.z} {self.roll} {self.pitch} {self.yaw}"

    @staticmethod
    def from_sdf(text: str):
        try:
            x, y, z, roll, pitch, yaw = (float(x) for x in text.split())
        except:
            raise Exception(f"Invalid pose: {text}")
        return Pose(x, y, z, roll, pitch, yaw)
