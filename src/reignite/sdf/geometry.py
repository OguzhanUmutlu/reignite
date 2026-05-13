### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.version import cmp_version

if typing.TYPE_CHECKING:
    from ..elements.box import Box
    from ..elements.capsule import Capsule
    from ..elements.cone import Cone
    from ..elements.cylinder import Cylinder
    from ..elements.ellipsoid import Ellipsoid
    from ..elements.heightmap import Heightmap
    from ..elements.image import Image
    from ..elements.mesh import Mesh
    from ..elements.plane import Plane
    from ..elements.polyline import Polyline
    from ..elements.sphere import Sphere


class Geometry(BaseModel):
    class Empty(BaseModel):
        def __init__(self, sdf_version: str | None = None):
            super().__init__(sdf_version)

        def to_version(self, target_version: str) -> "Geometry.Empty":
            kwargs = {"sdf_version": target_version}
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("empty")
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Geometry.Empty | SDFError":
            return cls(sdf_version=version)

    def __init__(
        self,
        sdf_version: str | None = None,
        box: "Box" = None,
        capsule: "Capsule" = None,
        cone: "Cone" = None,
        cylinder: "Cylinder" = None,
        ellipsoid: "Ellipsoid" = None,
        empty: "Geometry.Empty" = None,
        heightmap: "Heightmap" = None,
        image: "Image" = None,
        mesh: "Mesh" = None,
        plane: "Plane" = None,
        polyline: "Polyline" = None,
        sphere: "Sphere" = None
    ):
        super().__init__(sdf_version)
        self.box = box
        self.capsule = capsule
        self.cone = cone
        self.cylinder = cylinder
        self.ellipsoid = ellipsoid
        self.empty = empty
        self.heightmap = heightmap
        self.image = image
        self.mesh = mesh
        self.plane = plane
        self.polyline = polyline
        self.sphere = sphere
        if self.box is not None:
            if getattr(self.box, '__version__', None) is None:
                self.box.__version__ = self.__version__
            elif getattr(self.box, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.box = self.box.to_version(self.__version__)
        if self.capsule is not None:
            if getattr(self.capsule, '__version__', None) is None:
                self.capsule.__version__ = self.__version__
            elif getattr(self.capsule, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.capsule = self.capsule.to_version(self.__version__)
        if self.cone is not None:
            if getattr(self.cone, '__version__', None) is None:
                self.cone.__version__ = self.__version__
            elif getattr(self.cone, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.cone = self.cone.to_version(self.__version__)
        if self.cylinder is not None:
            if getattr(self.cylinder, '__version__', None) is None:
                self.cylinder.__version__ = self.__version__
            elif getattr(self.cylinder, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.cylinder = self.cylinder.to_version(self.__version__)
        if self.ellipsoid is not None:
            if getattr(self.ellipsoid, '__version__', None) is None:
                self.ellipsoid.__version__ = self.__version__
            elif getattr(self.ellipsoid, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.ellipsoid = self.ellipsoid.to_version(self.__version__)
        if self.empty is not None:
            if getattr(self.empty, '__version__', None) is None:
                self.empty.__version__ = self.__version__
            elif getattr(self.empty, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.empty = self.empty.to_version(self.__version__)
        if self.heightmap is not None:
            if getattr(self.heightmap, '__version__', None) is None:
                self.heightmap.__version__ = self.__version__
            elif getattr(self.heightmap, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.heightmap = self.heightmap.to_version(self.__version__)
        if self.image is not None:
            if getattr(self.image, '__version__', None) is None:
                self.image.__version__ = self.__version__
            elif getattr(self.image, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.image = self.image.to_version(self.__version__)
        if self.mesh is not None:
            if getattr(self.mesh, '__version__', None) is None:
                self.mesh.__version__ = self.__version__
            elif getattr(self.mesh, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.mesh = self.mesh.to_version(self.__version__)
        if self.plane is not None:
            if getattr(self.plane, '__version__', None) is None:
                self.plane.__version__ = self.__version__
            elif getattr(self.plane, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.plane = self.plane.to_version(self.__version__)
        if self.polyline is not None:
            if getattr(self.polyline, '__version__', None) is None:
                self.polyline.__version__ = self.__version__
            elif getattr(self.polyline, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.polyline = self.polyline.to_version(self.__version__)
        if self.sphere is not None:
            if getattr(self.sphere, '__version__', None) is None:
                self.sphere.__version__ = self.__version__
            elif getattr(self.sphere, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.sphere = self.sphere.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Geometry":
        from ..elements.box import Box
        from ..elements.capsule import Capsule
        from ..elements.cone import Cone
        from ..elements.cylinder import Cylinder
        from ..elements.ellipsoid import Ellipsoid
        from ..elements.heightmap import Heightmap
        from ..elements.image import Image
        from ..elements.mesh import Mesh
        from ..elements.plane import Plane
        from ..elements.polyline import Polyline
        from ..elements.sphere import Sphere
        if self.capsule is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'capsule' is not supported in SDF version {target_version} (added in 1.8)")
        if self.cone is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'cone' is not supported in SDF version {target_version} (added in 1.11)")
        if self.ellipsoid is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'ellipsoid' is not supported in SDF version {target_version} (added in 1.8)")
        if self.empty is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'empty' is not supported in SDF version {target_version} (added in 1.3)")
        if self.polyline is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'polyline' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["box"] = self.box.to_version(target_version) if self.box is not None else None
        kwargs["capsule"] = self.capsule.to_version(target_version) if self.capsule is not None else None
        kwargs["cone"] = self.cone.to_version(target_version) if self.cone is not None else None
        kwargs["cylinder"] = self.cylinder.to_version(target_version) if self.cylinder is not None else None
        kwargs["ellipsoid"] = self.ellipsoid.to_version(target_version) if self.ellipsoid is not None else None
        kwargs["empty"] = self.empty.to_version(target_version) if self.empty is not None else None
        kwargs["heightmap"] = self.heightmap.to_version(target_version) if self.heightmap is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["mesh"] = self.mesh.to_version(target_version) if self.mesh is not None else None
        kwargs["plane"] = self.plane.to_version(target_version) if self.plane is not None else None
        kwargs["polyline"] = self.polyline.to_version(target_version) if self.polyline is not None else None
        kwargs["sphere"] = self.sphere.to_version(target_version) if self.sphere is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.box import Box
        from ..elements.capsule import Capsule
        from ..elements.cone import Cone
        from ..elements.cylinder import Cylinder
        from ..elements.ellipsoid import Ellipsoid
        from ..elements.heightmap import Heightmap
        from ..elements.image import Image
        from ..elements.mesh import Mesh
        from ..elements.plane import Plane
        from ..elements.polyline import Polyline
        from ..elements.sphere import Sphere
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("geometry")
        if self.box is not None:
            el.append(self.box.to_sdf(version))
        if self.capsule is not None:
            el.append(self.capsule.to_sdf(version))
        if self.cone is not None:
            el.append(self.cone.to_sdf(version))
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf(version))
        if self.ellipsoid is not None:
            el.append(self.ellipsoid.to_sdf(version))
        if self.empty is not None:
            el.append(self.empty.to_sdf(version))
        if self.heightmap is not None:
            el.append(self.heightmap.to_sdf(version))
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.mesh is not None:
            el.append(self.mesh.to_sdf(version))
        if self.plane is not None:
            el.append(self.plane.to_sdf(version))
        if self.polyline is not None:
            el.append(self.polyline.to_sdf(version))
        if self.sphere is not None:
            el.append(self.sphere.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Geometry | SDFError":
        from ..elements.box import Box
        from ..elements.capsule import Capsule
        from ..elements.cone import Cone
        from ..elements.cylinder import Cylinder
        from ..elements.ellipsoid import Ellipsoid
        from ..elements.heightmap import Heightmap
        from ..elements.image import Image
        from ..elements.mesh import Mesh
        from ..elements.plane import Plane
        from ..elements.polyline import Polyline
        from ..elements.sphere import Sphere
        _c_box = el.find("box")
        if _c_box is not None:
            _res = Box._from_sdf(_c_box, version)
            if isinstance(_res, SDFError):
                return _res.extend("box")
            _box = _res
        else:
            _box = None
        _c_capsule = el.find("capsule")
        if _c_capsule is not None:
            _res = Capsule._from_sdf(_c_capsule, version)
            if isinstance(_res, SDFError):
                return _res.extend("capsule")
            _capsule = _res
        else:
            _capsule = None
        if _capsule is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'capsule' is not supported in SDF version {version} (added in 1.8)")
        _c_cone = el.find("cone")
        if _c_cone is not None:
            _res = Cone._from_sdf(_c_cone, version)
            if isinstance(_res, SDFError):
                return _res.extend("cone")
            _cone = _res
        else:
            _cone = None
        if _cone is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'cone' is not supported in SDF version {version} (added in 1.11)")
        _c_cylinder = el.find("cylinder")
        if _c_cylinder is not None:
            _res = Cylinder._from_sdf(_c_cylinder, version)
            if isinstance(_res, SDFError):
                return _res.extend("cylinder")
            _cylinder = _res
        else:
            _cylinder = None
        _c_ellipsoid = el.find("ellipsoid")
        if _c_ellipsoid is not None:
            _res = Ellipsoid._from_sdf(_c_ellipsoid, version)
            if isinstance(_res, SDFError):
                return _res.extend("ellipsoid")
            _ellipsoid = _res
        else:
            _ellipsoid = None
        if _ellipsoid is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'ellipsoid' is not supported in SDF version {version} (added in 1.8)")
        _c_empty = el.find("empty")
        if _c_empty is not None:
            _res = cls.Empty._from_sdf(_c_empty, version)
            if isinstance(_res, SDFError):
                return _res.extend("empty")
            _empty = _res
        else:
            _empty = None
        if _empty is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'empty' is not supported in SDF version {version} (added in 1.3)")
        _c_heightmap = el.find("heightmap")
        if _c_heightmap is not None:
            _res = Heightmap._from_sdf(_c_heightmap, version)
            if isinstance(_res, SDFError):
                return _res.extend("heightmap")
            _heightmap = _res
        else:
            _heightmap = None
        _c_image = el.find("image")
        if _c_image is not None:
            _res = Image._from_sdf(_c_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        else:
            _image = None
        _c_mesh = el.find("mesh")
        if _c_mesh is not None:
            _res = Mesh._from_sdf(_c_mesh, version)
            if isinstance(_res, SDFError):
                return _res.extend("mesh")
            _mesh = _res
        else:
            _mesh = None
        _c_plane = el.find("plane")
        if _c_plane is not None:
            _res = Plane._from_sdf(_c_plane, version)
            if isinstance(_res, SDFError):
                return _res.extend("plane")
            _plane = _res
        else:
            _plane = None
        _c_polyline = el.find("polyline")
        if _c_polyline is not None:
            _res = Polyline._from_sdf(_c_polyline, version)
            if isinstance(_res, SDFError):
                return _res.extend("polyline")
            _polyline = _res
        else:
            _polyline = None
        if _polyline is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'polyline' is not supported in SDF version {version} (added in 1.5)")
        _c_sphere = el.find("sphere")
        if _c_sphere is not None:
            _res = Sphere._from_sdf(_c_sphere, version)
            if isinstance(_res, SDFError):
                return _res.extend("sphere")
            _sphere = _res
        else:
            _sphere = None
        return cls(sdf_version=version, box=_box, capsule=_capsule, cone=_cone, cylinder=_cylinder, ellipsoid=_ellipsoid, empty=_empty, heightmap=_heightmap, image=_image, mesh=_mesh, plane=_plane, polyline=_polyline, sphere=_sphere)
