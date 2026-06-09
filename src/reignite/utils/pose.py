from __future__ import annotations

from math import radians, cos, sin, degrees, inf, sqrt, atan2, pi, tan, asinh, atan, sinh
from typing import Sequence

_PoseT = Sequence[float] | str | "Pose"

earth_radius = 6378137.0
meters_per_degree_lat = 111320.0

_SUPPORTED_INERTIAL_FRAMES = ("NED", "ENU", "NEU", "END")
_SUPPORTED_BODY_FRAMES = ("FRD", "FLU", "FRU", "FLD")


def _xyz_to_ned(x: float, y: float, z: float, frame: str) -> tuple[float, float, float]:
    if frame == "NED":
        return x, y, z
    if frame == "ENU":
        return y, x, -z
    if frame == "NEU":
        return x, y, -z
    if frame == "END":
        return y, x, z
    raise ValueError(f"Unsupported inertial frame: {frame!r}")


def _ned_to_xyz(n: float, e: float, d: float, frame: str) -> tuple[float, float, float]:
    if frame == "NED":
        return n, e, d
    if frame == "ENU":
        return e, n, -d
    if frame == "NEU":
        return n, e, -d
    if frame == "END":
        return e, n, d
    raise ValueError(f"Unsupported inertial frame: {frame!r}")


def _xyz_to_frd(x: float, y: float, z: float, frame: str) -> tuple[float, float, float]:
    if frame == "FRD":
        return x, y, z
    if frame == "FLU":
        return y, -x, z
    if frame == "FRU":
        return x, y, -z
    if frame == "FLD":
        return y, -x, -z
    raise ValueError(f"Unsupported body frame: {frame!r}")


def _frd_to_xyz(f: float, r: float, d: float, frame: str) -> tuple[float, float, float]:
    if frame == "FRD":
        return f, r, d
    if frame == "FLU":
        return -r, f, d
    if frame == "FRU":
        return f, r, -d
    if frame == "FLD":
        return -r, f, -d
    raise ValueError(f"Unsupported body frame: {frame!r}")


def _pose(value: Pose | Sequence[float] | str) -> Pose:
    if isinstance(value, Pose):
        return value
    if isinstance(value, str):
        parts = value.split()
        if len(parts) == 6:
            try:
                x, y, z, r, p, yw = (float(v) for v in parts)
                return Pose(x, y, z, r, p, yw)
            except ValueError:
                pass
        elif len(parts) == 0:
            return Pose()
    value = list(value) if not isinstance(value, str) else []
    if len(value) != 6:
        value += [0.0] * (6 - len(value))
    return Pose(*value[:6])


GAZEBO_FRAMES = ("ENU", "FLU")
ARDUPILOT_FRAMES = ("NED", "FRD")


class Pose:
    origin: "Pose" = None
    default_frames = ("ENU", "FLU")

    # lat and lon are in degrees
    def __init__(self,
                 x: float | Pose | None = None, y: float | None = None, z: float | None = None,
                 roll: float = 0.0, pitch: float = 0.0, yaw: float = 0.0,
                 roll_deg: float | None = None, pitch_deg: float | None = None, yaw_deg: float | None = None,
                 lat: float | None = None, lon: float | None = None,
                 rel_alt: float | None = None, alt: float | None = None,
                 inertial_frame: str | None = None, body_frame: str | None = None,
                 mercator_pos: tuple[int, int] | None = None):
        self.yaw = radians(yaw_deg) if yaw_deg is not None else yaw or 0.0
        self.pitch = radians(pitch_deg) if pitch_deg is not None else pitch or 0.0
        self.roll = radians(roll_deg) if roll_deg is not None else roll or 0.0
        self._inertial_frame = inertial_frame or self.__class__.default_frames[0]
        self._body_frame = body_frame or self.__class__.default_frames[1]

        if isinstance(x, Pose):
            self.set(x)
            return

        if mercator_pos is not None:
            lon = mercator_pos[0] * 360.0 - 180.0
            n = pi * (1.0 - 2.0 * mercator_pos[1])
            lat = degrees(atan(sinh(n)))

        if z is not None:
            rel_alt = z

        if alt is None:
            if rel_alt is None:
                self.alt: float = Pose.origin.alt
            else:
                self.alt: float = Pose.origin.alt + rel_alt
        elif Pose.origin is not None and rel_alt is not None and Pose.origin.alt + rel_alt != alt:
            raise ValueError("rel_alt and alt are inconsistent with origin altitude")
        else:
            self.alt: float = alt

        if (lat is None or lon is None) and (x is None and y is None):
            x = 0.0
            y = 0.0
        if x is not None and y is None:
            y = 0.0
        if y is not None and x is None:
            x = 0.0
        if (lat is not None and lon is not None) and (x is not None and y is not None):
            raise ValueError("Only one of lat/lon or x/y must be provided")
        if x is not None and y is not None:
            if Pose.origin is None:
                self.lat = 0.0
                self.lon = 0.0
            else:
                self._set_xy_in_frame(x, y, self._inertial_frame)
        else:
            if not isinstance(lat, float):
                raise ValueError("lat must be a float")
            if not isinstance(lon, float):
                raise ValueError("lon must be a float")
            self.lat = float(lat)
            self.lon = float(lon)

        if Pose.origin is not None and Pose.origin.lat == inf:
            self.x: float = 0.0
            self.y: float = 0.0
            self.z: float = 0.0
            self.rel_alt: float = 0.0
            self.yaw_deg: float = 0.0
            self.pitch_deg: float = 0.0
            self.roll_deg: float = 0.0
            self.mercator_pos: tuple[int, int] = (0, 0)

        self.ensure_float()

    @property
    def inertial_frame(self) -> str:
        return self._inertial_frame

    @inertial_frame.setter
    def inertial_frame(self, value: str):
        if value not in _SUPPORTED_INERTIAL_FRAMES:
            raise ValueError(
                f"Unsupported inertial frame {value!r}. "
                f"Supported: {_SUPPORTED_INERTIAL_FRAMES}"
            )
        self._inertial_frame = value

    @property
    def body_frame(self) -> str:
        return self._body_frame

    @body_frame.setter
    def body_frame(self, value: str):
        if value not in _SUPPORTED_BODY_FRAMES:
            raise ValueError(
                f"Unsupported body frame {value!r}. "
                f"Supported: {_SUPPORTED_BODY_FRAMES}"
            )
        self._body_frame = value

    def as_frame(self, inertial_frame: str | None = None, body_frame: str | None = None) -> Pose:
        target_inertial = inertial_frame or self._inertial_frame
        target_body = body_frame or self._body_frame

        p = Pose(lat=self.lat, lon=self.lon, alt=self.alt,
                 yaw=self.yaw, pitch=self.pitch, roll=self.roll,
                 inertial_frame=target_inertial, body_frame=target_body)
        return p

    def _set_xy_in_frame(self, x: float, y: float, frame: str):
        n, e, _d = _xyz_to_ned(x, y, 0.0, frame)
        d_lat = n / earth_radius
        d_lon = e / (earth_radius * cos(radians(Pose.origin.lat)))
        self.lat = Pose.origin.lat + degrees(d_lat)
        self.lon = Pose.origin.lon + degrees(d_lon)

    def _get_north_east(self) -> tuple[float, float]:
        d_lat = radians(self.lat - Pose.origin.lat)
        d_lon = radians(self.lon - Pose.origin.lon)
        n = earth_radius * d_lat
        e = earth_radius * d_lon * cos(radians(Pose.origin.lat))
        return n, e

    def _get_down(self) -> float:
        return -(self.alt - Pose.origin.alt)

    def set_xy(self, x: float, y: float):
        self._set_xy_in_frame(x, y, self._inertial_frame)

    def ensure_float(self):
        self.lat = float(self.lat)
        self.lon = float(self.lon)
        self.alt = float(self.alt)
        self.yaw = float(self.yaw)
        self.pitch = float(self.pitch)
        self.roll = float(self.roll)

    def __getattr__(self, item):
        if item == "mercator_pos":
            x = (self.lon + 180.0) / 360.0
            y = (1.0 - asinh(tan(radians(self.lat))) / pi) / 2.0
            return x, y
        if item == "yaw_deg":
            return degrees(self.yaw)
        if item == "pitch_deg":
            return degrees(self.pitch)
        if item == "roll_deg":
            return degrees(self.roll)
        if item == "pose":
            return Pose(x=self.x, y=self.y, z=self.z, roll=self.roll, pitch=self.pitch, yaw=self.yaw,
                        inertial_frame=self._inertial_frame, body_frame=self._body_frame)
        if item in ("x", "y", "z"):
            n, e = self._get_north_east()
            d = self._get_down()
            fx, fy, fz = _ned_to_xyz(n, e, d, self._inertial_frame)
            if item == "x":
                return fx
            if item == "y":
                return fy
            return fz
        if item in ("rel_alt",):
            return self.alt - Pose.origin.alt
        if item == "latE7":
            return int(self.lat * 1e7)
        if item == "lonE7":
            return int(self.lon * 1e7)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key == "yaw_deg":
            self.yaw = radians(value)
        elif key == "pitch_deg":
            self.pitch = radians(value)
        elif key == "roll_deg":
            self.roll = radians(value)
        elif key in ("rel_alt", "z"):
            self.alt = Pose.origin.alt + value
        elif key == "x":
            n, e = self._get_north_east()
            d = self._get_down()
            fx, fy, fz = _ned_to_xyz(n, e, d, self._inertial_frame)
            fx = value
            n, e, d = _xyz_to_ned(fx, fy, fz, self._inertial_frame)
            d_lat = n / earth_radius
            d_lon = e / (earth_radius * cos(radians(Pose.origin.lat)))
            self.lat = Pose.origin.lat + degrees(d_lat)
            self.lon = Pose.origin.lon + degrees(d_lon)
        elif key == "y":
            n, e = self._get_north_east()
            d = self._get_down()
            fx, fy, fz = _ned_to_xyz(n, e, d, self._inertial_frame)
            fy = value
            n, e, d = _xyz_to_ned(fx, fy, fz, self._inertial_frame)
            d_lat = n / earth_radius
            d_lon = e / (earth_radius * cos(radians(Pose.origin.lat)))
            self.lat = Pose.origin.lat + degrees(d_lat)
            self.lon = Pose.origin.lon + degrees(d_lon)
        elif key == "latE7":
            self.lat = value / 1e7
        elif key == "lonE7":
            self.lon = value / 1e7
        else:
            super().__setattr__(key, value)

    def set(self, location: Pose):
        self.lat = location.lat
        self.lon = location.lon
        self.alt = location.alt
        self.yaw = location.yaw
        self.pitch = location.pitch
        self.roll = location.roll
        self._inertial_frame = location._inertial_frame
        self._body_frame = location._body_frame
        self.ensure_float()

    def offset_bearing(self, bearing: float, distance: float) -> Pose:
        frame_x = distance * cos(bearing)
        frame_y = distance * sin(bearing)
        n, e, _ = _xyz_to_ned(frame_x, frame_y, 0.0, self._inertial_frame)
        d_lat = degrees(n / earth_radius)
        d_lon = degrees(e / (earth_radius * cos(radians(self.lat))))
        return Pose(lat=self.lat + d_lat, lon=self.lon + d_lon, alt=self.alt,
                    yaw=self.yaw, pitch=self.pitch, roll=self.roll,
                    inertial_frame=self._inertial_frame, body_frame=self._body_frame)

    def distance_to(self, other: Pose) -> float:
        d_lat = radians(other.lat - self.lat)
        d_lon = radians(other.lon - self.lon)
        a = sin(d_lat / 2) ** 2 + cos(radians(self.lat)) * cos(radians(other.lat)) * sin(d_lon / 2) ** 2
        return earth_radius * 2 * atan2(sqrt(a), sqrt(1 - a))

    def bearing_to(self, other: Pose) -> float:
        lat1 = radians(self.lat)
        lat2 = radians(other.lat)
        d_lon = radians(other.lon - self.lon)
        ned_e = sin(d_lon) * cos(lat2)
        ned_n = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(d_lon)
        fx, fy, _ = _ned_to_xyz(ned_n, ned_e, 0.0, self._inertial_frame)
        return atan2(fy, fx) % (2 * pi)

    def inclination_to(self, other: Pose) -> float:
        horiz = self.distance_to(other)
        ned_d = self.alt - other.alt
        _, _, fz = _ned_to_xyz(0.0, 0.0, ned_d, self._inertial_frame)
        if horiz == 0.0:
            return -(pi / 2) if fz > 0 else ((pi / 2) if fz < 0 else 0.0)
        return atan2(-fz, horiz)

    def offset(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> Pose:
        n, e, d = _xyz_to_ned(x, y, z, self._inertial_frame)
        d_lat = degrees(n / earth_radius)
        d_lon = degrees(e / (earth_radius * cos(radians(self.lat))))
        return Pose(lat=self.lat + d_lat, lon=self.lon + d_lon, alt=self.alt - d,
                    yaw=self.yaw, pitch=self.pitch, roll=self.roll,
                    inertial_frame=self._inertial_frame, body_frame=self._body_frame)

    def offset_body(self, forward: float = 0.0, left: float = 0.0, up: float = 0.0) -> Pose:
        x, y, z = _frd_to_xyz(forward, left, up, self._body_frame)
        return self.offset(x=x, y=y, z=z)

    def two_point_boundary(self, b: Pose, padding=50.0):
        min_lat = min(self.lat, b.lat)
        max_lat = max(self.lat, b.lat)
        min_lon = min(self.lon, b.lon)
        max_lon = max(self.lon, b.lon)

        lat_padding_deg = padding / meters_per_degree_lat

        avg_lat = (min_lat + max_lat) / 2.0
        lon_padding_deg = padding / (meters_per_degree_lat * cos(radians(avg_lat)))

        box_min_lat = min_lat - lat_padding_deg
        box_max_lat = max_lat + lat_padding_deg
        box_min_lon = min_lon - lon_padding_deg
        box_max_lon = max_lon + lon_padding_deg

        top_left = Pose(lat=box_max_lat, lon=box_min_lon, alt=self.alt)
        top_right = Pose(lat=box_max_lat, lon=box_max_lon, alt=self.alt)
        bottom_right = Pose(lat=box_min_lat, lon=box_max_lon, alt=self.alt)
        bottom_left = Pose(lat=box_min_lat, lon=box_min_lon, alt=self.alt)

        return [top_left, top_right, bottom_right, bottom_left]

    def __repr__(self):
        return f"Pose(lat={self.lat}, lon={self.lon}, alt={self.alt}, yaw={self.yaw}, pitch={self.pitch}, roll={self.roll})"

    def to_sdf(self, _=None):
        return str(self)

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z} {self.roll} {self.pitch} {self.yaw}"

    def __copy__(self):
        return Pose(self)

    @classmethod
    def set_default_frames(cls, inertial_frame: str, body_frame: str):
        if inertial_frame not in _SUPPORTED_INERTIAL_FRAMES:
            raise ValueError(
                f"Unsupported inertial frame {inertial_frame!r}. "
                f"Supported: {_SUPPORTED_INERTIAL_FRAMES}"
            )
        if body_frame not in _SUPPORTED_BODY_FRAMES:
            raise ValueError(
                f"Unsupported body frame {body_frame!r}. "
                f"Supported: {_SUPPORTED_BODY_FRAMES}"
            )
        cls.default_frames = (inertial_frame, body_frame)

    @staticmethod
    def pose_with_frames(inertial_frame: str, body_frame: str):
        class _PoseWithFrames(Pose):
            default_frames = (inertial_frame, body_frame)

        return _PoseWithFrames


class PoseAP(Pose):
    default_frames = ARDUPILOT_FRAMES


Pose.origin = Pose(lat=0.0, lon=0.0, alt=584.0)
