from __future__ import annotations

from xml.etree import ElementTree as ET

from .max_convex_hulls import MaxConvexHulls
from .voxel_resolution import VoxelResolution
from ..model import Model


class ConvexDecomposition(Model):
    def __init__(
            self,
            max_convex_hulls: "MaxConvexHulls" = None,
            voxel_resolution: "VoxelResolution" = None
    ):
        self.max_convex_hulls = max_convex_hulls
        self.voxel_resolution = voxel_resolution

    def to_sdf(self) -> ET.Element:
        el = ET.Element("convex_decomposition")
        if self.max_convex_hulls is not None:
            el.append(self.max_convex_hulls.to_sdf())
        if self.voxel_resolution is not None:
            el.append(self.voxel_resolution.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ConvexDecomposition":
        _c_max_convex_hulls = el.find("max_convex_hulls")
        _max_convex_hulls = MaxConvexHulls.from_sdf(_c_max_convex_hulls) if _c_max_convex_hulls is not None else None
        _c_voxel_resolution = el.find("voxel_resolution")
        _voxel_resolution = VoxelResolution.from_sdf(_c_voxel_resolution) if _c_voxel_resolution is not None else None
        return cls(max_convex_hulls=_max_convex_hulls, voxel_resolution=_voxel_resolution)
