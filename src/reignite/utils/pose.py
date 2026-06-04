from __future__ import annotations

from math import radians, cos, sqrt, asin, sin, degrees, atan2, inf
from typing import Sequence

_PoseT = Sequence[float] | str | "Pose"

earth_radius = 6378137.0
meters_per_degree_lat = 111320.0


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


class Pose:
    origin: "Pose" = None

    def __init__(self,
                 x: float | Pose | None = None, y: float | None = None, z: float | None = None,
                 yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0,
                 lat: float | None = None, lon: float | None = None,
                 rel_alt: float | None = None, alt: float | None = None):
        self.yaw = yaw or 0.0
        self.pitch = pitch or 0.0
        self.roll = roll or 0.0

        if isinstance(x, Pose):
            self.set(x)
            return

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
                self.set_xy(x, y)
        else:
            if not isinstance(lat, float):
                raise ValueError("lat must be a float")
            if not isinstance(lon, float):
                raise ValueError("lon must be a float")
            self.lat = float(lat)
            self.lon = float(lon)

        if Pose.origin is not None and Pose.origin.lat == inf:
            # make the IDE happy
            self.x: float = 0.0
            self.y: float = 0.0
            self.z: float = 0.0
            self.rel_alt: float = 0.0

        self.ensure_float()

    def set_xy(self, x: float, y: float):
        d_lat = y / earth_radius
        d_lon = x / (earth_radius * cos(radians(Pose.origin.lat)))
        self.lat = Pose.origin.lat + degrees(d_lat)
        self.lon = Pose.origin.lon + degrees(d_lon)

    def ensure_float(self):
        self.lat = float(self.lat)
        self.lon = float(self.lon)
        self.alt = float(self.alt)
        self.yaw = float(self.yaw)
        self.pitch = float(self.pitch)
        self.roll = float(self.roll)

    def __getattr__(self, item):
        if item == "pose":
            return Pose(x=self.x, y=self.y, z=self.z, roll=self.roll, pitch=self.pitch, yaw=self.yaw)
        if item in ("x", "y"):
            if item == "x":
                d_lon = radians(self.lon - Pose.origin.lon)
                return earth_radius * d_lon * cos(radians(Pose.origin.lat))
            else:
                d_lat = radians(self.lat - Pose.origin.lat)
                return earth_radius * d_lat
        if item in ("z", "rel_alt"):
            return self.alt - Pose.origin.alt
        if item == "latE7":
            return int(self.lat * 1e7)
        if item == "lonE7":
            return int(self.lon * 1e7)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key in ("rel_alt", "z"):
            self.alt = Pose.origin.alt + value
        elif key == "x":
            d_lon = value / (earth_radius * cos(radians(Pose.origin.lat)))
            self.lon = Pose.origin.lon + degrees(d_lon)
        elif key == "y":
            d_lat = value / earth_radius
            self.lat = Pose.origin.lat + degrees(d_lat)
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
        self.ensure_float()

    def offset_bearing(self, bearing_deg: float, distance: float):
        meters_per_degree_lon = meters_per_degree_lat * cos(radians(self.lat))
        return Pose(
            lat=self.lat + (distance * cos(radians(bearing_deg))) / meters_per_degree_lat,
            lon=self.lon + (distance * sin(radians(bearing_deg))) / meters_per_degree_lon,
            alt=self.alt
        )

    def distance_to(self, other: Pose):
        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(other.lat)
        lon2 = radians(other.lon)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2.0) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2.0) ** 2
        c = 2.0 * asin(min(1.0, sqrt(a)))
        return earth_radius * c

    def bearing_to(self, other: Pose):
        lat1 = radians(self.lat)
        lat2 = radians(other.lat)
        dlon = radians(other.lon - self.lon)

        x = sin(dlon) * cos(lat2)
        y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)

        if x == 0.0 and y == 0.0:
            return 0.0

        return (degrees(atan2(x, y)) + 360.0) % 360.0

    def inclination_to(self, other: Pose):
        lat1 = radians(self.lat)
        lat2 = radians(other.lat)
        dlat = radians(other.lat - self.lat)
        dlon = radians(other.lon - self.lon)

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        ground_distance = earth_radius * c

        alt_difference = other.alt - self.alt

        if ground_distance == 0.0:
            return 90.0 if alt_difference > 0 else -90.0 if alt_difference < 0 else 0.0

        return degrees(atan2(alt_difference, ground_distance))

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

    def offset_enu(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        return Pose(
            lat=self.lat + degrees(y / earth_radius),
            lon=self.lon + degrees(x / (earth_radius * cos(radians(self.lat)))),
            alt=self.alt + z
        )

    def __repr__(self):
        return f"Pose(lat={self.lat}, lon={self.lon}, alt={self.alt}, yaw={self.yaw}, pitch={self.pitch}, roll={self.roll})"

    def to_sdf(self, _=None):
        return str(self)

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z} {self.roll} {self.pitch} {self.yaw}"


Pose.origin = Pose(lat=0.0, lon=0.0, alt=584.0)
