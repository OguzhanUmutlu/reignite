from __future__ import annotations

from xml.etree import ElementTree as ET

from .max_convex_hulls import MaxConvexHulls
from .voxel_resolution import VoxelResolution
from ...sdf1_11.models.convex_decomposition import ConvexDecomposition as _PrevConvexDecomposition


class ConvexDecomposition(_PrevConvexDecomposition):
    def __init__(
            self,
            max_convex_hulls: "MaxConvexHulls" = None,
            voxel_resolution: "VoxelResolution" = None
    ):
        super().__init__(max_convex_hulls=max_convex_hulls, voxel_resolution=voxel_resolution)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ConvexDecomposition":
        _base = _PrevConvexDecomposition.from_sdf(el)
        return cls(max_convex_hulls=_base.max_convex_hulls, voxel_resolution=_base.voxel_resolution)
